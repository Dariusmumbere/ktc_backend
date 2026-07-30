import os
import io
import re
import json
import uuid
import logging
import datetime as dt
from decimal import Decimal
from typing import Optional, List, Union

from fastapi import FastAPI, Depends, HTTPException, status, UploadFile, File, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, EmailStr, Field

from sqlalchemy import (
    create_engine, Column, Integer, String, Float, Boolean, DateTime,
    ForeignKey, Text, Enum as SAEnum
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Session
from sqlalchemy.exc import IntegrityError

from passlib.context import CryptContext
from jose import jwt, JWTError

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger("ktc_ipfms")
logging.basicConfig(level=logging.INFO)

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    # Render / Heroku style URLs use the old "postgres://" scheme; SQLAlchemy
    # (via psycopg2) needs "postgresql://".
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

if not DATABASE_URL:
    DATABASE_URL = "sqlite:///./ktc.db"

JWT_SECRET = os.getenv("JWT_SECRET", "change-this-secret-in-production")
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 12  # 12 hours

# --------------------------------------------------------------------------
# Backblaze B2 (S3-compatible) object storage
# --------------------------------------------------------------------------
# Same bucket / endpoint / credential pattern used across our other
# applications (e.g. ScienceTech Academy). Accountability documents for
# KTC-IPFMS are stored in that same bucket, under their own folder prefix
# ("ktc-documents/<requisition_id>/<uuid>.<ext>") so they never collide with
# course images, avatars, certificates, etc. from other apps sharing the
# bucket. User signatures live under their own prefix
# ("ktc-signatures/<user_id>/<uuid>.<ext>") for the same reason.
B2_BUCKET_NAME = os.getenv("B2_BUCKET_NAME", "uploads-dir")
B2_ENDPOINT_URL = os.getenv("B2_ENDPOINT_URL", "https://s3.us-east-005.backblazeb2.com")
B2_KEY_ID = os.getenv("B2_KEY_ID", "0055ca7845641d30000000002")
B2_APPLICATION_KEY = os.getenv("B2_APPLICATION_KEY", "K005NNeGM9r28ujQ3jvNEQy2zUiu0TI")
B2_DOCUMENTS_FOLDER = "ktc-documents"
B2_SIGNATURES_FOLDER = "ktc-signatures"

b2_client = boto3.client(
    "s3",
    endpoint_url=B2_ENDPOINT_URL,
    aws_access_key_id=B2_KEY_ID,
    aws_secret_access_key=B2_APPLICATION_KEY,
)

CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")
origins = ["*"] if CORS_ORIGINS.strip() == "*" else [o.strip() for o in CORS_ORIGINS.split(",")]

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login", auto_error=False)

ROLES = [
    "admin",       # System Administrator
    "staff",       # Staff Member
    "hod",         # Head of Department
    "treasurer",   # Senior Treasurer
    "clerk",       # Town Clerk
    "auditor",     # Internal Auditor
]

# --------------------------------------------------------------------------
# Shared numeric amount parser
# --------------------------------------------------------------------------
# IMPORTANT: this is the ONE place amounts (baseline, planned target, Q1-Q4)
# get turned into a Python float, and it is used at every point a value can
# enter or leave the system:
#   - Excel import (values come in as text or native numbers from openpyxl)
#   - Manual create/update via the API (values come in as JSON — normally a
#     number, but a client could send a string)
#   - Every read/response (BudgetCode.allocated_amount /
#     BudgetCode.available_balance and budget_code_to_out) — so if a row's
#     underlying value is ever anything other than a clean float (e.g. a
#     legacy row written before this fix, or a value that reached the DB
#     through some other path), it is re-interpreted correctly on the way
#     out instead of silently rendering as 0 or crashing the response.
#
# Having ONE parser instead of one at import-time and a different, separate
# conversion at display-time is deliberate: two independent implementations
# is exactly how a value can be "fixed" going in but still show wrong going
# out (or vice-versa).
_THOUSANDS_SPACE_RE = re.compile(r"(?<=\d)[\s\u00A0\u2009\u202F](?=\d)")
_AMOUNT_CURRENCY_NOISE = ("UGX", "Ugx", "ugx", "USH", "Ush", "ush", "/=", "=", "%")


def parse_amount_verbose(v):
    """Parse any raw value (native number, text, None) into a float.

    Returns (value, ok, original_text):
      - value: the parsed float (0.0 if v was empty/None, or if parsing
        ultimately failed)
      - ok: False only when a genuinely non-empty, non-numeric value had to
        be discarded — lets callers that care (the Excel importer) warn the
        user instead of staying silent
      - original_text: the original value as text, for error messages
    """
    if v is None:
        return 0.0, True, ""
    if isinstance(v, bool):
        return 0.0, True, str(v)
    if isinstance(v, (int, float, Decimal)):
        return float(v), True, str(v)

    original = str(v)
    s = original.strip()
    if s == "":
        return 0.0, True, s

    negative = False
    if s.startswith("(") and s.endswith(")"):
        negative = True
        s = s[1:-1].strip()
    elif s.startswith("-"):
        negative = True
        s = s[1:].strip()

    # Normalise assorted unicode space characters (non-breaking, thin, etc.)
    # to plain spaces before we treat them as thousands separators.
    s = s.replace("\u00A0", " ").replace("\u2009", " ").replace("\u202F", " ")

    for token in _AMOUNT_CURRENCY_NOISE:
        s = s.replace(token, "")
    s = s.strip()

    # Remove thousands separators: commas, and spaces sitting between digits
    # (e.g. "1 200 000").
    s = s.replace(",", "")
    s = _THOUSANDS_SPACE_RE.sub("", s)
    s = s.strip()

    if s == "" or s == "-":
        return 0.0, True, original.strip()

    try:
        result = float(s)
    except (TypeError, ValueError):
        return 0.0, False, original.strip()

    return (-result if negative else result), True, original.strip()


def parse_amount(v) -> float:
    """Best-effort float conversion — never raises, defaults to 0.0."""
    value, _ok, _original = parse_amount_verbose(v)
    return value


# --------------------------------------------------------------------------
# Models
# --------------------------------------------------------------------------

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), unique=True, nullable=False)
    code = Column(String(20), unique=True, nullable=False)
    created_at = Column(DateTime, default=dt.datetime.utcnow)

    users = relationship("User", back_populates="department")
    budget_codes = relationship("BudgetCode", back_populates="department")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)
    # Position (job title) is a free-text field filled in manually by the
    # administrator when creating the account (e.g. "Senior Accountant",
    # "Community Development Officer") — it is not tied to a fixed list.
    position = Column(String(150), nullable=True)
    telephone = Column(String(40), nullable=True)
    # Object key of this user's uploaded signature image inside Backblaze
    # B2 (e.g. "ktc-signatures/7/9f3c1a2b....png"), or NULL if the user
    # hasn't uploaded one yet. Stored exactly like accountability document
    # keys so it can be streamed back out through the same /files route.
    signature_path = Column(String(500), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=dt.datetime.utcnow)

    department = relationship("Department", back_populates="users")

    @property
    def signature_url(self):
        return f"/files/{self.signature_path}" if self.signature_path else None


class WorkPlan(Base):
    __tablename__ = "work_plans"
    id = Column(Integer, primary_key=True, index=True)
    financial_year = Column(String(20), nullable=False)   # e.g. "2026/27"
    title = Column(String(200), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=dt.datetime.utcnow)

    budget_codes = relationship("BudgetCode", back_populates="work_plan")


class BudgetCode(Base):
    """
    A single row of the Council's "New Budget Estimates Data Entry Form":
    Department | Service Area | Programme | Sub Programme | Budget Output
    Code | Budget Output Description | PIAP Output Description | PIAP
    Output Indicator | Unit of Measure | Baseline Value | Planned Target |
    Actual Output | Q1 | Q2 | Q3 | Q4 | Total Budget | Funding Source |
    Responsible Party
    """
    __tablename__ = "budget_codes"
    id = Column(Integer, primary_key=True, index=True)
    work_plan_id = Column(Integer, ForeignKey("work_plans.id"), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    service_area = Column(String(150))
    code = Column(String(30), nullable=False)                  # Budget Output Code
    output_description = Column(String(255), nullable=False)   # Budget Output Description
    programme = Column(String(150))
    sub_programme = Column(String(150))
    piap_output_description = Column(String(255))
    piap_output_indicator = Column(String(255))
    unit_of_measure = Column(String(50))
    baseline_value = Column(Float, default=0)
    planned_target = Column(Float, default=0)
    actual_output = Column(String(255))
    # Quarterly planned amounts (UGX) — these replace a single manually
    # entered "allocated amount"; the total is derived from their sum.
    q1_amount = Column(Float, default=0)
    q2_amount = Column(Float, default=0)
    q3_amount = Column(Float, default=0)
    q4_amount = Column(Float, default=0)
    funding_source = Column(String(100), default="Local Revenue")  # Revenue Source
    responsible_party = Column(String(150))

    work_plan = relationship("WorkPlan", back_populates="budget_codes")
    department = relationship("Department", back_populates="budget_codes")
    activities = relationship("Activity", back_populates="budget_code")

    @property
    def allocated_amount(self):
        # Defensive: parse_amount() rather than trusting the raw column
        # value directly. This means a row whose quarterly figures were
        # ever stored oddly (e.g. non-numeric) still totals correctly
        # instead of the sum silently excluding it or raising.
        return (
            parse_amount(self.q1_amount) + parse_amount(self.q2_amount) +
            parse_amount(self.q3_amount) + parse_amount(self.q4_amount)
        )

    @property
    def committed_amount(self):
        # sum of requisitions not rejected/returned
        db = SessionLocal()
        try:
            reqs = db.query(Requisition).filter(
                Requisition.budget_code_id == self.id,
                Requisition.status.notin_(["rejected", "returned", "draft"])
            ).all()
            return sum(r.amount_requested for r in reqs)
        finally:
            db.close()

    @property
    def available_balance(self):
        return self.allocated_amount - self.committed_amount


class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True)
    budget_code_id = Column(Integer, ForeignKey("budget_codes.id"), nullable=False)
    name = Column(String(255), nullable=False)
    quarter = Column(String(10), default="Q1")  # Q1-Q4
    is_active = Column(Boolean, default=True)

    budget_code = relationship("BudgetCode", back_populates="activities")


class Requisition(Base):
    __tablename__ = "requisitions"
    id = Column(Integer, primary_key=True, index=True)
    ref_no = Column(String(40), unique=True, nullable=False)
    requester_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    budget_code_id = Column(Integer, ForeignKey("budget_codes.id"), nullable=False)
    activity_id = Column(Integer, ForeignKey("activities.id"), nullable=True)
    activity_details = Column(Text)
    # Subject line of the requisition (e.g. "Monitoring roads for 3rd Qtr
    # works") — shown on the requisition form and in listings.
    subject = Column(String(255), nullable=True)
    # JSON-encoded list of line items entered via the sectioned line-item
    # builder in the "New Requisition" modal — each item has item_no,
    # description, units, qty, rate, amount. amount_requested (below) is
    # always the sum of these, computed server-side at creation time.
    line_items = Column(Text, nullable=True)
    amount_requested = Column(Float, nullable=False)
    status = Column(String(20), default="draft")
    # draft, submitted, hod_approved, treasurer_approved, approved,
    # rejected, returned, accounting_pending, accounted
    current_stage = Column(String(20), default="hod")  # hod / treasurer / clerk / done
    created_at = Column(DateTime, default=dt.datetime.utcnow)
    updated_at = Column(DateTime, default=dt.datetime.utcnow)

    requester = relationship("User", foreign_keys=[requester_id])
    department = relationship("Department")
    budget_code = relationship("BudgetCode")
    activity = relationship("Activity")
    approvals = relationship("ApprovalHistory", back_populates="requisition", order_by="ApprovalHistory.id")
    documents = relationship("Document", back_populates="requisition")
    accountability = relationship("AccountabilityRecord", back_populates="requisition", uselist=False)


class ApprovalHistory(Base):
    __tablename__ = "approval_history"
    id = Column(Integer, primary_key=True, index=True)
    requisition_id = Column(Integer, ForeignKey("requisitions.id"), nullable=False)
    stage = Column(String(20), nullable=False)   # hod / treasurer / clerk
    actor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    action = Column(String(20), nullable=False)  # approve / reject / return
    comments = Column(Text)
    created_at = Column(DateTime, default=dt.datetime.utcnow)

    requisition = relationship("Requisition", back_populates="approvals")
    actor = relationship("User")


class AccountabilityRecord(Base):
    __tablename__ = "accountability_records"
    id = Column(Integer, primary_key=True, index=True)
    requisition_id = Column(Integer, ForeignKey("requisitions.id"), unique=True, nullable=False)
    auditor_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    status = Column(String(20), default="pending")  # pending / verified / flagged
    remarks = Column(Text)
    updated_at = Column(DateTime, default=dt.datetime.utcnow)

    requisition = relationship("Requisition", back_populates="accountability")
    auditor = relationship("User")


class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    requisition_id = Column(Integer, ForeignKey("requisitions.id"), nullable=False)
    filename = Column(String(255), nullable=False)
    # stored_path now holds the Backblaze B2 *object key* (e.g.
    # "ktc-documents/42/9f3c1a2b....pdf"), not a local filesystem path.
    stored_path = Column(String(500), nullable=False)
    doc_type = Column(String(50), default="supporting")  # supporting / receipt / voucher / attendance / other
    uploaded_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=dt.datetime.utcnow)

    requisition = relationship("Requisition", back_populates="documents")


class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    message = Column(String(500), nullable=False)
    category = Column(String(30), default="info")
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=dt.datetime.utcnow)
    link_requisition_id = Column(Integer, ForeignKey("requisitions.id"), nullable=True)


class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    action = Column(String(150), nullable=False)
    details = Column(Text)
    created_at = Column(DateTime, default=dt.datetime.utcnow)


Base.metadata.create_all(bind=engine)


def _run_lightweight_migrations():
    """
    Add newly introduced columns to an already-existing database without
    requiring a full migration tool. Safe to run on every startup: each
    ALTER is wrapped so a column that already exists (or a backend, like
    SQLite, that behaves differently) never crashes the app.
    """
    statements = [
        # BudgetCode — earlier additions
        "ALTER TABLE budget_codes ADD COLUMN indicator VARCHAR(255)",
        "ALTER TABLE budget_codes ADD COLUMN q1_amount FLOAT DEFAULT 0",
        "ALTER TABLE budget_codes ADD COLUMN q2_amount FLOAT DEFAULT 0",
        "ALTER TABLE budget_codes ADD COLUMN q3_amount FLOAT DEFAULT 0",
        "ALTER TABLE budget_codes ADD COLUMN q4_amount FLOAT DEFAULT 0",
        # BudgetCode — "New Budget Estimates Data Entry Form" fields
        "ALTER TABLE budget_codes ADD COLUMN service_area VARCHAR(150)",
        "ALTER TABLE budget_codes ADD COLUMN piap_output_description VARCHAR(255)",
        "ALTER TABLE budget_codes ADD COLUMN piap_output_indicator VARCHAR(255)",
        "ALTER TABLE budget_codes ADD COLUMN actual_output VARCHAR(255)",
        "ALTER TABLE budget_codes ADD COLUMN responsible_party VARCHAR(150)",
        # Users — Position & Telephone
        "ALTER TABLE users ADD COLUMN position VARCHAR(150)",
        "ALTER TABLE users ADD COLUMN telephone VARCHAR(40)",
        # Users — Signature (object key of the uploaded signature image)
        "ALTER TABLE users ADD COLUMN signature_path VARCHAR(500)",
        # Requisitions — Subject & sectioned Line Items (New Requisition
        # modal / printable form)
        "ALTER TABLE requisitions ADD COLUMN subject VARCHAR(255)",
        "ALTER TABLE requisitions ADD COLUMN line_items TEXT",
    ]
    with engine.connect() as conn:
        for stmt in statements:
            try:
                conn.exec_driver_sql(stmt)
                conn.commit()
            except Exception:
                conn.rollback()  # column already exists (or backend quirk) — ignore

    # One-time backfill: if a legacy row has data in the old "indicator"
    # column but nothing in the new "piap_output_indicator" column, copy it
    # across so nothing already entered is lost.
    try:
        with engine.connect() as conn:
            conn.exec_driver_sql(
                "UPDATE budget_codes SET piap_output_indicator = indicator "
                "WHERE (piap_output_indicator IS NULL OR piap_output_indicator = '') "
                "AND indicator IS NOT NULL AND indicator <> ''"
            )
            conn.commit()
    except Exception:
        pass


_run_lightweight_migrations()

# --------------------------------------------------------------------------
# Schemas
# --------------------------------------------------------------------------

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: str
    full_name: str
    user_id: int


class LoginIn(BaseModel):
    email: EmailStr
    password: str
    # The role the person selected on the "Signing in as" dropdown. Optional
    # for backwards compatibility (e.g. API clients that don't send it), but
    # when present it must match the account's actual role.
    role: Optional[str] = None


class UserOut(BaseModel):
    id: int
    full_name: str
    email: str
    role: str
    department_id: Optional[int] = None
    position: Optional[str] = None
    telephone: Optional[str] = None
    is_active: bool
    signature_url: Optional[str] = None

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: str
    department_id: Optional[int] = None
    position: Optional[str] = None
    telephone: Optional[str] = None


class DepartmentIn(BaseModel):
    name: str
    code: str


class DepartmentOut(DepartmentIn):
    id: int
    class Config:
        from_attributes = True


class WorkPlanIn(BaseModel):
    financial_year: str
    title: str


class WorkPlanOut(WorkPlanIn):
    id: int
    is_active: bool
    class Config:
        from_attributes = True


class BudgetCodeIn(BaseModel):
    work_plan_id: int
    department_id: int
    service_area: Optional[str] = None
    code: str
    output_description: str
    programme: Optional[str] = None
    sub_programme: Optional[str] = None
    piap_output_description: Optional[str] = None
    piap_output_indicator: Optional[str] = None
    unit_of_measure: Optional[str] = None
    # Accept a number OR text: the form always sends a clean number, but any
    # other API client might send "1,200,000" — parse_amount() in the
    # endpoint below handles either.
    baseline_value: Union[float, int, str] = 0
    planned_target: Union[float, int, str] = 0
    actual_output: Optional[str] = None
    q1_amount: Union[float, int, str] = 0
    q2_amount: Union[float, int, str] = 0
    q3_amount: Union[float, int, str] = 0
    q4_amount: Union[float, int, str] = 0
    funding_source: str = "Local Revenue"
    responsible_party: Optional[str] = None


class BudgetCodeUpdate(BaseModel):
    """Partial update — every field optional, only what's sent gets changed.
    Lets an admin correct a specific row (e.g. one that was zeroed out by an
    earlier bad import) without deleting and recreating it."""
    service_area: Optional[str] = None
    code: Optional[str] = None
    output_description: Optional[str] = None
    programme: Optional[str] = None
    sub_programme: Optional[str] = None
    piap_output_description: Optional[str] = None
    piap_output_indicator: Optional[str] = None
    unit_of_measure: Optional[str] = None
    baseline_value: Optional[Union[float, int, str]] = None
    planned_target: Optional[Union[float, int, str]] = None
    actual_output: Optional[str] = None
    q1_amount: Optional[Union[float, int, str]] = None
    q2_amount: Optional[Union[float, int, str]] = None
    q3_amount: Optional[Union[float, int, str]] = None
    q4_amount: Optional[Union[float, int, str]] = None
    funding_source: Optional[str] = None
    responsible_party: Optional[str] = None


class BudgetCodeOut(BaseModel):
    id: int
    work_plan_id: int
    department_id: int
    department_name: Optional[str] = None
    service_area: Optional[str] = None
    code: str
    output_description: str
    programme: Optional[str] = None
    sub_programme: Optional[str] = None
    piap_output_description: Optional[str] = None
    piap_output_indicator: Optional[str] = None
    unit_of_measure: Optional[str] = None
    baseline_value: float
    planned_target: float
    actual_output: Optional[str] = None
    q1_amount: float
    q2_amount: float
    q3_amount: float
    q4_amount: float
    funding_source: str
    responsible_party: Optional[str] = None
    allocated_amount: float
    committed_amount: float
    available_balance: float

    class Config:
        from_attributes = True


class BudgetCodeImportResult(BaseModel):
    created: int
    skipped: int
    errors: List[str] = []


class ActivityIn(BaseModel):
    budget_code_id: int
    name: str
    quarter: str = "Q1"


class ActivityOut(ActivityIn):
    id: int
    is_active: bool
    class Config:
        from_attributes = True


class RequisitionLineItemIn(BaseModel):
    """One row from the sectioned line-item builder in the 'New
    Requisition' modal. A section header row (e.g. '01 Field fuel') and its
    priced lines all share the same item_no; qty/rate are optional since
    some lines (facilitation, transport, etc.) have their amount typed in
    directly rather than computed from qty x rate."""
    item_no: int
    description: str
    units: Optional[str] = None
    qty: Optional[float] = None
    rate: Optional[float] = None
    amount: float = 0


class RequisitionIn(BaseModel):
    budget_code_id: int
    activity_id: Optional[int] = None
    subject: str
    line_items: List[RequisitionLineItemIn]


class ApprovalActionIn(BaseModel):
    action: str  # approve / reject / return
    comments: Optional[str] = None


class AccountabilityIn(BaseModel):
    status: str  # verified / flagged / pending
    remarks: Optional[str] = None


# --------------------------------------------------------------------------
# Auth helpers
# --------------------------------------------------------------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = dt.datetime.utcnow() + dt.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if token is None:
        raise credentials_exception
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None or not user.is_active:
        raise credentials_exception
    return user


def require_roles(*roles):
    def checker(user: User = Depends(get_current_user)):
        if user.role not in roles:
            raise HTTPException(status_code=403, detail="You do not have permission to perform this action")
        return user
    return checker


def log_action(db: Session, user_id: Optional[int], action: str, details: str = ""):
    entry = AuditLog(user_id=user_id, action=action, details=details)
    db.add(entry)
    db.commit()


def notify(db: Session, user_id: int, message: str, category: str = "info", requisition_id: Optional[int] = None):
    n = Notification(user_id=user_id, message=message, category=category, link_requisition_id=requisition_id)
    db.add(n)
    db.commit()


def notify_role(db: Session, role: str, message: str, category: str = "info", requisition_id: Optional[int] = None):
    users = db.query(User).filter(User.role == role, User.is_active == True).all()
    for u in users:
        notify(db, u.id, message, category, requisition_id)


# --------------------------------------------------------------------------
# Backblaze B2 storage helpers
# --------------------------------------------------------------------------
# Mirrors the upload/delete pattern used in our other apps: object keys are
# namespaced under a folder prefix, content is streamed straight into the
# bucket, and errors are surfaced as clean HTTP 500s rather than raw
# botocore exceptions.

async def upload_document_to_b2(file: UploadFile, requisition_id: int) -> str:
    """Upload an accountability document to Backblaze B2 and return its object key."""
    try:
        ext = os.path.splitext(file.filename or "")[1].lower()
        key = f"{B2_DOCUMENTS_FOLDER}/{requisition_id}/{uuid.uuid4().hex}{ext}"
        file_content = await file.read()
        b2_client.put_object(
            Bucket=B2_BUCKET_NAME,
            Key=key,
            Body=file_content,
            ContentType=file.content_type or "application/octet-stream",
        )
        logger.info(f"Document uploaded to B2: {key}")
        return key
    except Exception as e:
        logger.error(f"Error uploading document to B2: {e}")
        raise HTTPException(status_code=500, detail=f"Error uploading document: {str(e)}")


async def upload_signature_to_b2(file: UploadFile, user_id: int) -> str:
    """Upload a user's signature image to Backblaze B2 and return its object key."""
    try:
        ext = os.path.splitext(file.filename or "")[1].lower()
        key = f"{B2_SIGNATURES_FOLDER}/{user_id}/{uuid.uuid4().hex}{ext}"
        file_content = await file.read()
        b2_client.put_object(
            Bucket=B2_BUCKET_NAME,
            Key=key,
            Body=file_content,
            ContentType=file.content_type or "image/png",
        )
        logger.info(f"Signature uploaded to B2: {key}")
        return key
    except Exception as e:
        logger.error(f"Error uploading signature to B2: {e}")
        raise HTTPException(status_code=500, detail=f"Error uploading signature: {str(e)}")


def delete_document_from_b2(key: str):
    try:
        b2_client.delete_object(Bucket=B2_BUCKET_NAME, Key=key)
        logger.info(f"Document deleted from B2: {key}")
    except Exception as e:
        # Never let a storage cleanup failure break the calling request.
        logger.warning(f"Error deleting document from B2: {e}")


# --------------------------------------------------------------------------
# App
# --------------------------------------------------------------------------

app = FastAPI(title="KTC-IPFMS API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def seed_data():
    """
    Idempotent startup seeding.

    IMPORTANT: this must never crash the app. Earlier versions gated seeding
    purely on `User.count() == 0`, which is unsafe: if a prior deploy created
    the Department row but then failed/restarted before the User row was
    committed (or if the users table was ever cleared independently of
    departments), the count-based check becomes true again and the app tries
    to re-insert a Department with a name that already has a UNIQUE
    constraint on it -> IntegrityError -> "Application startup failed."

    Fix: look up each seed row by its natural/unique key first (get-or-create)
    instead of relying on a derived count, and wrap the whole routine in a
    try/except so a seeding hiccup never takes the whole API down.
    """
    db = SessionLocal()
    try:
        admin_email = os.getenv("ADMIN_EMAIL", "admin@karugutu.town.go.ug")
        admin_password = os.getenv("ADMIN_PASSWORD", "Admin@2026")
        default_dept_name = "Administration and Support Services"
        default_dept_code = "ADM"

        # 1) Get-or-create the default department by its unique name.
        dep = db.query(Department).filter(Department.name == default_dept_name).first()
        if not dep:
            # Also guard against the code already existing under a
            # different name (code is unique too).
            dep = db.query(Department).filter(Department.code == default_dept_code).first()
        if not dep:
            dep = Department(name=default_dept_name, code=default_dept_code)
            db.add(dep)
            try:
                db.commit()
                db.refresh(dep)
            except IntegrityError:
                # Another worker/process created it concurrently — fetch it.
                db.rollback()
                dep = db.query(Department).filter(Department.name == default_dept_name).first()

        # 2) Get-or-create the admin user by its unique email.
        existing_admin = db.query(User).filter(User.email == admin_email).first()
        if not existing_admin:
            admin = User(
                full_name="System Administrator",
                email=admin_email,
                hashed_password=hash_password(admin_password),
                role="admin",
                position="System Administrator",
                department_id=dep.id if dep else None,
            )
            db.add(admin)
            try:
                db.commit()
                log_action(db, None, "system.seed", f"Seeded initial admin account {admin_email}")
            except IntegrityError:
                db.rollback()
                logger.info("Admin user already existed (created concurrently); skipping seed insert.")
    except Exception as exc:  # noqa: BLE001 - never let seeding crash startup
        db.rollback()
        logger.warning("Startup seeding skipped due to error: %s", exc)
    finally:
        db.close()


# ---------------------------- Auth ----------------------------------------

@app.post("/api/auth/login", response_model=Token)
def login(payload: LoginIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    if not user.is_active:
        raise HTTPException(status_code=403, detail="This account has been deactivated")
    # If the person selected a role on the "Signing in as" dropdown, make
    # sure it actually matches the account's role. This catches the common
    # mistake of, say, a Head of Department selecting "Staff Member" and
    # then being confused about missing approval permissions.
    if payload.role and payload.role != user.role:
        raise HTTPException(
            status_code=401,
            detail="The role you selected does not match this account. Please choose the correct role and try again."
        )
    token = create_access_token({"sub": str(user.id), "role": user.role})
    log_action(db, user.id, "auth.login", f"{user.email} logged in")
    return Token(access_token=token, role=user.role, full_name=user.full_name, user_id=user.id)


@app.get("/api/auth/me", response_model=UserOut)
def me(user: User = Depends(get_current_user)):
    return user


# ---------------------------- Users ----------------------------------------

@app.get("/api/users", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db), user: User = Depends(require_roles("admin"))):
    return db.query(User).order_by(User.created_at.desc()).all()


@app.post("/api/users", response_model=UserOut)
def create_user(payload: UserCreate, db: Session = Depends(get_db), admin: User = Depends(require_roles("admin"))):
    if payload.role not in ROLES:
        raise HTTPException(status_code=400, detail="Invalid role supplied")
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=400, detail="A user with this email already exists")
    new_user = User(
        full_name=payload.full_name,
        email=payload.email,
        hashed_password=hash_password(payload.password),
        role=payload.role,
        department_id=payload.department_id,
        position=payload.position,
        telephone=payload.telephone,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    log_action(db, admin.id, "user.create", f"Created user {new_user.email} ({new_user.role})")
    return new_user


@app.patch("/api/users/{user_id}/toggle-active", response_model=UserOut)
def toggle_user_active(user_id: int, db: Session = Depends(get_db), admin: User = Depends(require_roles("admin"))):
    target = db.query(User).filter(User.id == user_id).first()
    if not target:
        raise HTTPException(status_code=404, detail="User not found")
    target.is_active = not target.is_active
    db.commit()
    db.refresh(target)
    log_action(db, admin.id, "user.toggle_active", f"{target.email} active={target.is_active}")
    return target


# ---------------------------- User Signatures -------------------------------
# Every user manages their OWN signature (stored under their account, in
# their personal "settings"). It is uploaded once here and, from then on,
# automatically attached wherever that user's name appears on a printed
# requisition form — as the requester, or as the HOD/Treasurer/Clerk who
# actioned an approval stage — with no per-requisition action needed.

_ALLOWED_SIGNATURE_EXT = {".png", ".jpg", ".jpeg"}


@app.post("/api/users/me/signature", response_model=UserOut)
async def upload_my_signature(file: UploadFile = File(...), db: Session = Depends(get_db),
                               user: User = Depends(get_current_user)):
    ext = os.path.splitext(file.filename or "")[1].lower()
    if ext not in _ALLOWED_SIGNATURE_EXT:
        raise HTTPException(status_code=400, detail="Only PNG and JPG images are allowed for a signature")

    old_path = user.signature_path
    new_key = await upload_signature_to_b2(file, user.id)
    user.signature_path = new_key
    db.commit()
    db.refresh(user)

    # Clean up the previous signature image only after the new one is
    # safely committed, so a failed upload never leaves the user with no
    # signature at all.
    if old_path:
        delete_document_from_b2(old_path)

    log_action(db, user.id, "user.signature_upload", f"{user.email} uploaded a new signature")
    return user


@app.delete("/api/users/me/signature", response_model=UserOut)
def delete_my_signature(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if user.signature_path:
        old_path = user.signature_path
        user.signature_path = None
        db.commit()
        db.refresh(user)
        delete_document_from_b2(old_path)
        log_action(db, user.id, "user.signature_remove", f"{user.email} removed their signature")
    return user


# ---------------------------- Departments -----------------------------------

@app.get("/api/departments", response_model=List[DepartmentOut])
def list_departments(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return db.query(Department).order_by(Department.name).all()


@app.post("/api/departments", response_model=DepartmentOut)
def create_department(payload: DepartmentIn, db: Session = Depends(get_db), admin: User = Depends(require_roles("admin"))):
    if db.query(Department).filter(Department.code == payload.code).first():
        raise HTTPException(status_code=400, detail="Department code already exists")
    if db.query(Department).filter(Department.name == payload.name).first():
        raise HTTPException(status_code=400, detail="Department name already exists")
    dep = Department(**payload.dict())
    db.add(dep)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Department name or code already exists")
    db.refresh(dep)
    log_action(db, admin.id, "department.create", dep.name)
    return dep


# ---------------------------- Work Plans ------------------------------------

@app.get("/api/workplans", response_model=List[WorkPlanOut])
def list_workplans(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return db.query(WorkPlan).order_by(WorkPlan.financial_year.desc()).all()


@app.post("/api/workplans", response_model=WorkPlanOut)
def create_workplan(payload: WorkPlanIn, db: Session = Depends(get_db), admin: User = Depends(require_roles("admin"))):
    wp = WorkPlan(**payload.dict())
    db.add(wp)
    db.commit()
    db.refresh(wp)
    log_action(db, admin.id, "workplan.create", f"{wp.title} ({wp.financial_year})")
    return wp


# ---------------------------- Budget Codes ----------------------------------

def budget_code_to_out(bc: BudgetCode) -> BudgetCodeOut:
    # Every numeric field is re-parsed with parse_amount() here rather than
    # trusted as-is. This is what makes the fix "self-healing": even a row
    # whose q1-q4/baseline/target ended up stored oddly for any reason will
    # display correctly on every read from now on, with no need to touch
    # the database directly or re-import the source workbook.
    return BudgetCodeOut(
        id=bc.id, work_plan_id=bc.work_plan_id, department_id=bc.department_id,
        department_name=bc.department.name if bc.department else None,
        service_area=bc.service_area,
        code=bc.code, output_description=bc.output_description, programme=bc.programme,
        sub_programme=bc.sub_programme,
        piap_output_description=bc.piap_output_description,
        piap_output_indicator=bc.piap_output_indicator,
        unit_of_measure=bc.unit_of_measure,
        baseline_value=parse_amount(bc.baseline_value), planned_target=parse_amount(bc.planned_target),
        actual_output=bc.actual_output,
        q1_amount=parse_amount(bc.q1_amount), q2_amount=parse_amount(bc.q2_amount),
        q3_amount=parse_amount(bc.q3_amount), q4_amount=parse_amount(bc.q4_amount),
        funding_source=bc.funding_source,
        responsible_party=bc.responsible_party,
        allocated_amount=bc.allocated_amount, committed_amount=bc.committed_amount,
        available_balance=bc.available_balance,
    )


@app.get("/api/budget-codes", response_model=List[BudgetCodeOut])
def list_budget_codes(work_plan_id: Optional[int] = None, department_id: Optional[int] = None,
                       search: Optional[str] = None,
                       db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    q = db.query(BudgetCode)
    if work_plan_id:
        q = q.filter(BudgetCode.work_plan_id == work_plan_id)
    if department_id:
        q = q.filter(BudgetCode.department_id == department_id)
    if search:
        like = f"%{search}%"
        q = q.filter(BudgetCode.output_description.ilike(like) | BudgetCode.code.ilike(like))
    return [budget_code_to_out(bc) for bc in q.order_by(BudgetCode.code).all()]


_BUDGET_CODE_NUMERIC_FIELDS = ("baseline_value", "planned_target", "q1_amount", "q2_amount", "q3_amount", "q4_amount")


@app.post("/api/budget-codes", response_model=BudgetCodeOut)
def create_budget_code(payload: BudgetCodeIn, db: Session = Depends(get_db), admin: User = Depends(require_roles("admin"))):
    data = payload.dict()
    for f in _BUDGET_CODE_NUMERIC_FIELDS:
        data[f] = parse_amount(data[f])
    bc = BudgetCode(**data)
    db.add(bc)
    db.commit()
    db.refresh(bc)
    log_action(db, admin.id, "budget_code.create", f"{bc.code} - {bc.output_description}")
    return budget_code_to_out(bc)


@app.patch("/api/budget-codes/{bc_id}", response_model=BudgetCodeOut)
def update_budget_code(bc_id: int, payload: BudgetCodeUpdate, db: Session = Depends(get_db),
                        admin: User = Depends(require_roles("admin"))):
    """
    Correct a single budget code row directly — in particular, this is the
    fix for rows that were already zeroed out by an earlier bad import: the
    parsing fix in /api/budget-codes/import only protects *future* imports,
    it cannot retroactively recover a value that was already overwritten
    with 0 in the database. Use this endpoint (or re-import the same source
    workbook) to put the correct figure back.
    """
    bc = db.query(BudgetCode).filter(BudgetCode.id == bc_id).first()
    if not bc:
        raise HTTPException(status_code=404, detail="Budget code not found")
    data = payload.dict(exclude_unset=True)
    for f in _BUDGET_CODE_NUMERIC_FIELDS:
        if f in data:
            data[f] = parse_amount(data[f])
    for field, value in data.items():
        setattr(bc, field, value)
    db.commit()
    db.refresh(bc)
    log_action(db, admin.id, "budget_code.update", f"{bc.code} - {bc.output_description}")
    return budget_code_to_out(bc)


# ---- Excel import ----------------------------------------------------------
# Expected column headers (case-insensitive, order-independent) on the first
# worksheet, row 1:
#   Department, Service Area, Programme, Sub Programme, Budget Output Code,
#   Budget Output Description, PIAP Output Description, PIAP Output
#   Indicator, Unit of Measure, Baseline Value, Planned Target, Actual
#   Output, Q1 (UGX), Q2 (UGX), Q3 (UGX), Q4 (UGX), Funding Source,
#   Responsible Party
# "Department" is matched against existing department names (case
# insensitive); a department that doesn't exist yet is skipped with an
# error message rather than silently dropped, so the user knows to create
# it (or fix a typo) first. "Total Budget (UGX)" is ignored if present,
# since it is always recomputed as Q1+Q2+Q3+Q4.

_IMPORT_COLUMN_ALIASES = {
    "department": "department",
    "service area": "service_area",
    "programme": "programme",
    "program": "programme",
    "sub programme": "sub_programme",
    "sub-programme": "sub_programme",
    "sub program": "sub_programme",
    "budget output code": "code",
    "budget output": "output_description",
    "budget output description": "output_description",
    "piap output description": "piap_output_description",
    "piap output indicator": "piap_output_indicator",
    "unit of measure": "unit_of_measure",
    "baseline value": "baseline_value",
    "baseline": "baseline_value",
    "planned target": "planned_target",
    "target": "planned_target",
    "actual output": "actual_output",
    "q1(ugx)": "q1_amount", "q1 (ugx)": "q1_amount", "q1": "q1_amount",
    "q2(ugx)": "q2_amount", "q2 (ugx)": "q2_amount", "q2": "q2_amount",
    "q3(ugx)": "q3_amount", "q3 (ugx)": "q3_amount", "q3": "q3_amount",
    "q4(ugx)": "q4_amount", "q4 (ugx)": "q4_amount", "q4": "q4_amount",
    "funding source": "funding_source",
    "revenue source": "funding_source",
    "responsible party": "responsible_party",
}

# Human-friendly labels used only for error/warning messages surfaced back
# to the person importing the workbook, so a bad cell can be traced back to
# exactly which column produced it.
_NUMERIC_FIELD_LABELS = {
    "baseline_value": "Baseline Value",
    "planned_target": "Planned Target",
    "q1_amount": "Q1 (UGX)",
    "q2_amount": "Q2 (UGX)",
    "q3_amount": "Q3 (UGX)",
    "q4_amount": "Q4 (UGX)",
}


@app.post("/api/budget-codes/import", response_model=BudgetCodeImportResult)
async def import_budget_codes(work_plan_id: int, file: UploadFile = File(...),
                               db: Session = Depends(get_db),
                               admin: User = Depends(require_roles("admin"))):
    """
    Bulk-create Budget Estimates rows from an uploaded Excel workbook so a
    user can prepare the "New Budget Estimates Data Entry Form" data offline
    (e.g. in the Council's existing spreadsheet template) and have every row
    populate directly into the system, instead of typing each one in
    manually.
    """
    try:
        import openpyxl
    except ImportError:
        raise HTTPException(
            status_code=500,
            detail="Excel import is not available on this server — the 'openpyxl' package is not installed."
        )

    wp = db.query(WorkPlan).filter(WorkPlan.id == work_plan_id).first()
    if not wp:
        raise HTTPException(status_code=400, detail="Selected work plan does not exist")

    ext = os.path.splitext(file.filename or "")[1].lower()
    if ext not in (".xlsx", ".xlsm"):
        raise HTTPException(status_code=400, detail="Please upload a .xlsx Excel workbook")

    content = await file.read()
    try:
        wb = openpyxl.load_workbook(io.BytesIO(content), data_only=True)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not read the Excel file: {e}")

    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        raise HTTPException(status_code=400, detail="The uploaded workbook appears to be empty")

    header = [str(h).strip().lower() if h is not None else "" for h in rows[0]]
    col_map = {}  # column index -> field name
    for idx, h in enumerate(header):
        field = _IMPORT_COLUMN_ALIASES.get(h)
        if field:
            col_map[idx] = field

    if "output_description" not in col_map.values() or "code" not in col_map.values():
        raise HTTPException(
            status_code=400,
            detail="The workbook must at least include 'Budget Output Code' and 'Budget Output Description' columns"
        )

    departments_by_name = {d.name.strip().lower(): d for d in db.query(Department).all()}

    created = 0
    skipped = 0
    errors: List[str] = []

    # Numeric cells go through the single shared parse_amount_verbose() —
    # the same parser used for manual create/update and for every read —
    # so import, entry, and display can never drift out of sync again. The
    # only import-specific behaviour is turning a failed parse into a
    # visible warning instead of a silent zero.
    def _num(v, field_key: str = None, row_idx: int = None, row_warnings: list = None):
        value, ok, original = parse_amount_verbose(v)
        if not ok and row_warnings is not None:
            label = _NUMERIC_FIELD_LABELS.get(field_key, field_key or "value")
            loc = f"Row {row_idx}: " if row_idx else ""
            row_warnings.append(f"{loc}could not read '{original}' as a number for {label} — treated as 0")
        return value

    def _text(v):
        return str(v).strip() if v is not None else None

    for row_idx, row in enumerate(rows[1:], start=2):
        if row is None or all(c is None or str(c).strip() == "" for c in row):
            continue  # blank row
        data = {}
        for idx, field in col_map.items():
            data[field] = row[idx] if idx < len(row) else None

        dept_name = _text(data.get("department"))
        dept = departments_by_name.get(dept_name.lower()) if dept_name else None
        if not dept:
            skipped += 1
            errors.append(f"Row {row_idx}: department '{dept_name or ''}' was not found — skipped")
            continue

        code = _text(data.get("code"))
        output_description = _text(data.get("output_description"))
        if not code or not output_description:
            skipped += 1
            errors.append(f"Row {row_idx}: missing Budget Output Code or Description — skipped")
            continue

        row_warnings: List[str] = []

        bc = BudgetCode(
            work_plan_id=work_plan_id,
            department_id=dept.id,
            service_area=_text(data.get("service_area")),
            code=code,
            output_description=output_description,
            programme=_text(data.get("programme")),
            sub_programme=_text(data.get("sub_programme")),
            piap_output_description=_text(data.get("piap_output_description")),
            piap_output_indicator=_text(data.get("piap_output_indicator")),
            unit_of_measure=_text(data.get("unit_of_measure")),
            baseline_value=_num(data.get("baseline_value"), "baseline_value", row_idx, row_warnings),
            planned_target=_num(data.get("planned_target"), "planned_target", row_idx, row_warnings),
            actual_output=_text(data.get("actual_output")),
            q1_amount=_num(data.get("q1_amount"), "q1_amount", row_idx, row_warnings),
            q2_amount=_num(data.get("q2_amount"), "q2_amount", row_idx, row_warnings),
            q3_amount=_num(data.get("q3_amount"), "q3_amount", row_idx, row_warnings),
            q4_amount=_num(data.get("q4_amount"), "q4_amount", row_idx, row_warnings),
            funding_source=_text(data.get("funding_source")) or "Local Revenue",
            responsible_party=_text(data.get("responsible_party")),
        )
        db.add(bc)
        created += 1
        errors.extend(row_warnings)

    db.commit()
    log_action(db, admin.id, "budget_code.import",
               f"Imported {created} row(s) into work plan #{work_plan_id} from {file.filename} ({skipped} skipped)")
    return BudgetCodeImportResult(created=created, skipped=skipped, errors=errors[:20])


# ---------------------------- Activities ------------------------------------

@app.get("/api/activities", response_model=List[ActivityOut])
def list_activities(budget_code_id: Optional[int] = None, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    q = db.query(Activity).filter(Activity.is_active == True)
    if budget_code_id:
        q = q.filter(Activity.budget_code_id == budget_code_id)
    return q.all()


@app.post("/api/activities", response_model=ActivityOut)
def create_activity(payload: ActivityIn, db: Session = Depends(get_db), admin: User = Depends(require_roles("admin"))):
    act = Activity(**payload.dict())
    db.add(act)
    db.commit()
    db.refresh(act)
    log_action(db, admin.id, "activity.create", act.name)
    return act


# ---------------------------- Requisitions ----------------------------------

def gen_ref_no(db: Session) -> str:
    year = dt.datetime.utcnow().year
    count = db.query(Requisition).count() + 1
    return f"KTC-REQ-{year}-{count:05d}"


def _parse_requisition_line_items(raw: Optional[str]) -> list:
    """Line items are stored as a JSON-encoded string; this always returns
    a list (empty if there's nothing stored / it can't be parsed) so
    callers never have to special-case None or bad JSON."""
    if not raw:
        return []
    try:
        parsed = json.loads(raw)
        return parsed if isinstance(parsed, list) else []
    except (TypeError, ValueError):
        return []


def requisition_to_dict(r: Requisition) -> dict:
    return {
        "id": r.id,
        "ref_no": r.ref_no,
        "requester_id": r.requester_id,
        "requester_name": r.requester.full_name if r.requester else None,
        # The requester's own signature, attached automatically wherever
        # this requisition is printed — no per-form action needed.
        "requester_signature_url": r.requester.signature_url if r.requester else None,
        "department_id": r.department_id,
        "department_name": r.department.name if r.department else None,
        "budget_code_id": r.budget_code_id,
        "budget_code": r.budget_code.code if r.budget_code else None,
        "budget_output": r.budget_code.output_description if r.budget_code else None,
        "activity_id": r.activity_id,
        "activity_name": r.activity.name if r.activity else None,
        "activity_details": r.activity_details,
        "subject": r.subject,
        "line_items": _parse_requisition_line_items(r.line_items),
        "amount_requested": r.amount_requested,
        "status": r.status,
        "current_stage": r.current_stage,
        "created_at": r.created_at.isoformat() if r.created_at else None,
        "updated_at": r.updated_at.isoformat() if r.updated_at else None,
        "approvals": [
            {
                "stage": a.stage, "actor": a.actor.full_name if a.actor else None,
                "action": a.action, "comments": a.comments,
                # The approving officer's signature, for this specific
                # approval action — used to stamp the correct signature
                # into the matching block of the printed form.
                "actor_signature_url": a.actor.signature_url if a.actor else None,
                "created_at": a.created_at.isoformat() if a.created_at else None,
            } for a in r.approvals
        ],
        "documents": [
            # d.stored_path is the Backblaze B2 object key. The /files
            # route below streams the object straight out of B2, so the
            # frontend's existing "${API_BASE}${d.url}" link pattern keeps
            # working unchanged.
            {"id": d.id, "filename": d.filename, "doc_type": d.doc_type, "url": f"/files/{d.stored_path}"}
            for d in r.documents
        ],
        "accountability": {
            "status": r.accountability.status if r.accountability else None,
            "remarks": r.accountability.remarks if r.accountability else None,
            "has_voucher": any(d.doc_type == "voucher" for d in r.documents),
            "has_documents": len(r.documents) > 0,
        } if r.accountability else None,
    }


@app.get("/api/requisitions")
def list_requisitions(status_filter: Optional[str] = Query(None, alias="status"),
                       mine: bool = False,
                       db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    q = db.query(Requisition)
    if user.role == "staff" or mine:
        q = q.filter(Requisition.requester_id == user.id)
    elif user.role == "hod":
        q = q.filter(Requisition.department_id == user.department_id)
    if status_filter:
        q = q.filter(Requisition.status == status_filter)
    reqs = q.order_by(Requisition.created_at.desc()).all()
    return [requisition_to_dict(r) for r in reqs]


@app.get("/api/requisitions/{req_id}")
def get_requisition(req_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    r = db.query(Requisition).filter(Requisition.id == req_id).first()
    if not r:
        raise HTTPException(status_code=404, detail="Requisition not found")
    return requisition_to_dict(r)


@app.post("/api/requisitions")
def create_requisition(payload: RequisitionIn, submit: bool = False,
                        db: Session = Depends(get_db),
                        user: User = Depends(require_roles("staff", "hod", "admin"))):
    bc = db.query(BudgetCode).filter(BudgetCode.id == payload.budget_code_id).first()
    if not bc:
        raise HTTPException(status_code=400, detail="Selected budget code does not exist")

    if not payload.line_items:
        raise HTTPException(status_code=400, detail="Please add at least one line item")

    total = sum((li.amount or 0) for li in payload.line_items)
    if total <= 0:
        raise HTTPException(status_code=400, detail="Please add at least one priced line item")

    r = Requisition(
        ref_no=gen_ref_no(db),
        requester_id=user.id,
        department_id=user.department_id or bc.department_id,
        budget_code_id=payload.budget_code_id,
        activity_id=payload.activity_id,
        subject=payload.subject,
        line_items=json.dumps([li.dict() for li in payload.line_items]),
        amount_requested=total,
        status="draft",
        current_stage="hod",
    )
    db.add(r)
    db.commit()
    db.refresh(r)

    if submit:
        _submit_requisition(r, db, user)

    log_action(db, user.id, "requisition.create", r.ref_no)
    return requisition_to_dict(r)


def _submit_requisition(r: Requisition, db: Session, user: User):
    # Budget validation
    bc = r.budget_code
    if r.activity_id:
        act = db.query(Activity).filter(Activity.id == r.activity_id, Activity.budget_code_id == bc.id).first()
        if not act:
            raise HTTPException(status_code=400, detail="The selected activity is not part of the approved work plan for this budget code")
    if bc.available_balance < r.amount_requested:
        raise HTTPException(
            status_code=400,
            detail=f"Insufficient available budget. Available balance is UGX {bc.available_balance:,.0f}, requested UGX {r.amount_requested:,.0f}"
        )
    r.status = "submitted"
    r.current_stage = "hod"
    r.updated_at = dt.datetime.utcnow()
    db.commit()
    notify_role(db, "hod", f"New requisition {r.ref_no} awaiting your approval", "approval_request", r.id)


@app.post("/api/requisitions/{req_id}/submit")
def submit_requisition(req_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    r = db.query(Requisition).filter(Requisition.id == req_id).first()
    if not r:
        raise HTTPException(status_code=404, detail="Requisition not found")
    if r.requester_id != user.id and user.role != "admin":
        raise HTTPException(status_code=403, detail="You can only submit your own requisitions")
    if r.status not in ("draft", "returned"):
        raise HTTPException(status_code=400, detail="Only draft or returned requisitions can be submitted")
    _submit_requisition(r, db, user)
    log_action(db, user.id, "requisition.submit", r.ref_no)
    return requisition_to_dict(r)


STAGE_ROLE = {"hod": "hod", "treasurer": "treasurer", "clerk": "clerk"}
NEXT_STAGE = {"hod": "treasurer", "treasurer": "clerk", "clerk": "done"}
STAGE_STATUS = {"hod": "hod_approved", "treasurer": "treasurer_approved", "clerk": "approved"}


@app.post("/api/requisitions/{req_id}/approve-action")
def approval_action(req_id: int, payload: ApprovalActionIn,
                     db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    r = db.query(Requisition).filter(Requisition.id == req_id).first()
    if not r:
        raise HTTPException(status_code=404, detail="Requisition not found")

    stage = r.current_stage
    if stage not in STAGE_ROLE:
        raise HTTPException(status_code=400, detail="This requisition is not awaiting approval")
    if user.role != STAGE_ROLE[stage] and user.role != "admin":
        raise HTTPException(status_code=403, detail=f"Only the {STAGE_ROLE[stage].upper()} can act on this stage")
    if payload.action not in ("approve", "reject", "return"):
        raise HTTPException(status_code=400, detail="Action must be approve, reject or return")

    history = ApprovalHistory(
        requisition_id=r.id, stage=stage, actor_id=user.id,
        action=payload.action, comments=payload.comments,
    )
    db.add(history)

    if payload.action == "approve":
        # re-verify budget at treasurer stage
        if stage == "treasurer" and r.budget_code.available_balance < 0:
            raise HTTPException(status_code=400, detail="Budget has since been exhausted for this code")
        r.status = STAGE_STATUS[stage]
        nxt = NEXT_STAGE[stage]
        if nxt == "done":
            # Fully approved: the requisition now sits on the internal
            # auditor's wall pending accountability documents (this is
            # exactly the "pending until all accountability documents are
            # uploaded, including the payment voucher" behaviour) — an
            # AccountabilityRecord is created in "pending" status and only
            # moves to "verified" once the auditor reviews the uploads.
            r.current_stage = "done"
            r.status = "approved"
            acc = AccountabilityRecord(requisition_id=r.id, status="pending")
            db.add(acc)
            notify_role(db, "auditor", f"Requisition {r.ref_no} approved - accountability documents required", "accountability_pending", r.id)
            notify(
                db, r.requester_id,
                f"Your requisition {r.ref_no} has been fully approved. Please upload the accountability "
                f"documents (payment voucher, receipts, attendance sheets, etc.) for this requisition.",
                "accountability_pending", r.id
            )
        else:
            r.current_stage = nxt
            notify_role(db, nxt, f"Requisition {r.ref_no} awaiting your approval", "approval_request", r.id)
    elif payload.action == "reject":
        r.status = "rejected"
        r.current_stage = "closed"
        notify(db, r.requester_id, f"Your requisition {r.ref_no} was rejected", "rejection", r.id)
    else:  # return
        r.status = "returned"
        r.current_stage = "hod"
        notify(db, r.requester_id, f"Your requisition {r.ref_no} was returned for correction", "rejection", r.id)

    r.updated_at = dt.datetime.utcnow()
    db.commit()
    log_action(db, user.id, f"requisition.{payload.action}", f"{r.ref_no} at stage {stage}")
    return requisition_to_dict(r)


@app.get("/api/approvals/pending")
def pending_approvals(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if user.role not in ("hod", "treasurer", "clerk", "admin"):
        raise HTTPException(status_code=403, detail="Not an approver role")
    stage_for_role = {"hod": "hod", "treasurer": "treasurer", "clerk": "clerk"}
    if user.role == "admin":
        reqs = db.query(Requisition).filter(Requisition.current_stage.in_(["hod", "treasurer", "clerk"])).all()
    else:
        stage = stage_for_role[user.role]
        q = db.query(Requisition).filter(Requisition.current_stage == stage)
        if user.role == "hod":
            q = q.filter(Requisition.department_id == user.department_id)
        reqs = q.all()
    return [requisition_to_dict(r) for r in reqs]


# ---------------------------- Documents (Backblaze B2) -----------------------

@app.post("/api/requisitions/{req_id}/documents")
async def upload_document(req_id: int, doc_type: str = "supporting", file: UploadFile = File(...),
                           db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    r = db.query(Requisition).filter(Requisition.id == req_id).first()
    if not r:
        raise HTTPException(status_code=404, detail="Requisition not found")

    # Accountability documents can only be attached once the requisition has
    # cleared full approval (i.e. an AccountabilityRecord exists for it), and
    # only by the staff member/project officer responsible for the requisition
    # (or an administrator). This matches the intended workflow: the auditor
    # reviews what has been uploaded, they do not upload on the requester's
    # behalf. The requisition stays on the internal auditor's wall until
    # every required accountability document — including the payment
    # voucher — has been uploaded and the auditor marks it verified.
    if not r.accountability:
        raise HTTPException(
            status_code=400,
            detail="This requisition is not yet awaiting accountability documents. "
                   "It must be fully approved before documents can be uploaded."
        )
    if user.id != r.requester_id and user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Only the original requester or an administrator can upload accountability documents for this requisition"
        )
    if r.accountability.status == "verified":
        raise HTTPException(status_code=400, detail="This requisition's accountability has already been verified")

    allowed_ext = {".pdf", ".docx", ".jpg", ".jpeg", ".png"}
    ext = os.path.splitext(file.filename or "")[1].lower()
    if ext not in allowed_ext:
        raise HTTPException(status_code=400, detail="Only PDF, DOCX, JPG and PNG files are allowed")

    object_key = await upload_document_to_b2(file, r.id)

    doc = Document(requisition_id=r.id, filename=file.filename, stored_path=object_key,
                    doc_type=doc_type, uploaded_by=user.id)
    db.add(doc)

    # If a previous auditor review had flagged this requisition, a fresh
    # upload puts it back into "pending" so the auditor knows to re-review it.
    if r.accountability.status == "flagged":
        r.accountability.status = "pending"

    db.commit()
    log_action(db, user.id, "document.upload", f"{file.filename} on {r.ref_no}")
    notify_role(db, "auditor", f"New accountability document uploaded for {r.ref_no}", "accountability_pending", r.id)
    return {"id": doc.id, "filename": doc.filename, "doc_type": doc.doc_type, "url": f"/files/{object_key}"}


@app.get("/files/{filename:path}")
async def stream_document(filename: str, request: Request, db: Session = Depends(get_db)):
    """
    Stream an accountability document (or a user's signature image) straight
    out of Backblaze B2.

    Files are addressed by their B2 object key (e.g.
    "ktc-documents/42/9f3c1a2b....pdf" or "ktc-signatures/7/ab12....png")
    and proxied here rather than served from local disk, so uploads survive
    redeploys and restarts. HTTP Range requests are honoured so
    PDFs/images preview quickly in the browser instead of having to
    download in full first.
    """
    clean_key = filename.split("?")[0].strip("/")
    if not clean_key:
        raise HTTPException(status_code=400, detail="Filename is required")

    try:
        head = b2_client.head_object(Bucket=B2_BUCKET_NAME, Key=clean_key)
    except ClientError:
        raise HTTPException(status_code=404, detail="File not found in storage")

    file_size = head["ContentLength"]
    content_type = head.get("ContentType") or "application/octet-stream"

    range_header = request.headers.get("Range")
    get_kwargs = {"Bucket": B2_BUCKET_NAME, "Key": clean_key}
    status_code = 200
    content_range = None
    content_length = file_size

    if range_header:
        try:
            _, range_value = range_header.split("=", 1)
            start_str, end_str = range_value.split("-", 1)
            start = int(start_str) if start_str.strip() else 0
            end = int(end_str) if end_str.strip() else file_size - 1
            end = min(end, file_size - 1)
            if start > end or start >= file_size:
                raise HTTPException(status_code=416, detail="Range Not Satisfiable")
            get_kwargs["Range"] = f"bytes={start}-{end}"
            content_length = end - start + 1
            status_code = 206
            content_range = f"bytes {start}-{end}/{file_size}"
        except (ValueError, AttributeError):
            pass

    try:
        b2_response = b2_client.get_object(**get_kwargs)
    except ClientError:
        raise HTTPException(status_code=502, detail="Storage fetch error")

    doc = db.query(Document).filter(Document.stored_path == clean_key).first()
    if doc:
        display_name = doc.filename
    else:
        display_name = clean_key.split("/")[-1]

    def _stream(body, chunk_size: int = 65536):
        with body as stream:
            while True:
                chunk = stream.read(chunk_size)
                if not chunk:
                    break
                yield chunk

    headers = {
        "Content-Type": content_type,
        "Content-Length": str(content_length),
        "Accept-Ranges": "bytes",
        "Content-Disposition": f'inline; filename="{display_name}"',
        "Cache-Control": "private, max-age=3600",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, HEAD, OPTIONS",
        "Access-Control-Expose-Headers": "Content-Range, Content-Length, Accept-Ranges",
    }
    if content_range:
        headers["Content-Range"] = content_range

    return StreamingResponse(
        _stream(b2_response["Body"]),
        status_code=status_code,
        headers=headers,
        media_type=content_type,
    )


# ---------------------------- Accountability --------------------------------

@app.post("/api/requisitions/{req_id}/accountability")
def update_accountability(req_id: int, payload: AccountabilityIn,
                           db: Session = Depends(get_db), user: User = Depends(require_roles("auditor", "admin"))):
    r = db.query(Requisition).filter(Requisition.id == req_id).first()
    if not r or not r.accountability:
        raise HTTPException(status_code=404, detail="No accountability record found for this requisition")

    # Hard server-side gate: a requisition stays on the internal auditor's
    # wall until every required accountability document — including the
    # Payment Voucher — has actually been uploaded. The auditor cannot mark
    # a requisition "verified" without documents attached, regardless of
    # what the client sends.
    if payload.status == "verified":
        if not r.documents:
            raise HTTPException(
                status_code=400,
                detail="Cannot verify: no accountability documents have been uploaded for this requisition yet."
            )
        has_voucher = any(d.doc_type == "voucher" for d in r.documents)
        if not has_voucher:
            raise HTTPException(
                status_code=400,
                detail="Cannot verify: a Payment Voucher must be uploaded for this requisition before it can be verified."
            )

    r.accountability.status = payload.status
    r.accountability.remarks = payload.remarks
    r.accountability.auditor_id = user.id
    r.accountability.updated_at = dt.datetime.utcnow()
    if payload.status == "verified":
        r.status = "accounted"
    db.commit()
    log_action(db, user.id, "accountability.update", f"{r.ref_no} -> {payload.status}")
    if payload.status == "flagged":
        notify(
            db, r.requester_id,
            f"Accountability documents for {r.ref_no} were flagged: {payload.remarks or 'see remarks'}",
            "rejection", r.id
        )
    elif payload.status == "verified":
        notify(db, r.requester_id, f"Accountability for {r.ref_no} has been verified", "approval_completed", r.id)
    return requisition_to_dict(r)


@app.get("/api/accountability/pending")
def accountability_pending(db: Session = Depends(get_db), user: User = Depends(require_roles("auditor", "admin"))):
    reqs = db.query(Requisition).join(AccountabilityRecord).filter(AccountabilityRecord.status != "verified").all()
    return [requisition_to_dict(r) for r in reqs]


# ---------------------------- Notifications ---------------------------------

@app.get("/api/notifications")
def list_notifications(unread_only: bool = False, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    q = db.query(Notification).filter(Notification.user_id == user.id)
    if unread_only:
        q = q.filter(Notification.is_read == False)
    items = q.order_by(Notification.created_at.desc()).limit(50).all()
    return [
        {"id": n.id, "message": n.message, "category": n.category, "is_read": n.is_read,
         "created_at": n.created_at.isoformat(), "requisition_id": n.link_requisition_id}
        for n in items
    ]


@app.patch("/api/notifications/{note_id}/read")
def mark_notification_read(note_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    n = db.query(Notification).filter(Notification.id == note_id, Notification.user_id == user.id).first()
    if not n:
        raise HTTPException(status_code=404, detail="Notification not found")
    n.is_read = True
    db.commit()
    return {"ok": True}


@app.patch("/api/notifications/read-all")
def mark_all_read(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    db.query(Notification).filter(Notification.user_id == user.id, Notification.is_read == False).update({"is_read": True})
    db.commit()
    return {"ok": True}


# ---------------------------- Dashboard & Reports ----------------------------

@app.get("/api/dashboard/stats")
def dashboard_stats(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    base = db.query(Requisition)
    if user.role == "staff":
        base = base.filter(Requisition.requester_id == user.id)
    elif user.role == "hod":
        base = base.filter(Requisition.department_id == user.department_id)

    pending = base.filter(Requisition.current_stage.in_(["hod", "treasurer", "clerk"])).count()
    approved = base.filter(Requisition.status.in_(["approved", "accounted"])).count()
    rejected = base.filter(Requisition.status == "rejected").count()

    all_codes = db.query(BudgetCode).all()
    total_budget_sum = sum(bc.allocated_amount for bc in all_codes)
    utilized = sum(bc.committed_amount for bc in all_codes)

    recent = base.order_by(Requisition.created_at.desc()).limit(6).all()

    return {
        "pending_approvals": pending,
        "approved_requisitions": approved,
        "rejected_requisitions": rejected,
        "total_budget": total_budget_sum,
        "budget_utilized": utilized,
        "utilization_pct": round((utilized / total_budget_sum * 100), 1) if total_budget_sum else 0,
        "recent_activity": [
            {"ref_no": r.ref_no, "status": r.status, "amount": r.amount_requested,
             "department": r.department.name if r.department else None,
             "created_at": r.created_at.isoformat()}
            for r in recent
        ],
    }


@app.get("/api/reports/audit-view/{req_id}")
def audit_view(req_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    r = db.query(Requisition).filter(Requisition.id == req_id).first()
    if not r:
        raise HTTPException(status_code=404, detail="Requisition not found")
    return requisition_to_dict(r)


@app.get("/api/reports/audit-logs")
def get_audit_logs(db: Session = Depends(get_db), user: User = Depends(require_roles("admin", "auditor", "clerk"))):
    logs = db.query(AuditLog).order_by(AuditLog.created_at.desc()).limit(300).all()
    return [
        {"id": l.id, "user": l.user_id, "action": l.action, "details": l.details,
         "created_at": l.created_at.isoformat()}
        for l in logs
    ]


@app.get("/api/health")
def health():
    return {"status": "ok", "time": dt.datetime.utcnow().isoformat()}
