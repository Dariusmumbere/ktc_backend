"""
Karugutu Town Council Integrated Public Financial Management System (KTC-IPFMS)
Backend — single-file FastAPI application.

Run locally:
    pip install -r requirements.txt
    uvicorn main:app --reload

Deploy on Render:
    - Build command:  pip install -r requirements.txt
    - Start command:  uvicorn main:app --host 0.0.0.0 --port $PORT
    - Environment variables:
        DATABASE_URL   -> your Render PostgreSQL "Internal Database URL"
        JWT_SECRET     -> any long random string
        CORS_ORIGINS   -> e.g. https://your-frontend.onrender.com,http://localhost:5500
        ADMIN_EMAIL / ADMIN_PASSWORD -> optional, seeds the first System Administrator

If DATABASE_URL is not set, the app falls back to a local SQLite file (ktc.db)
so it can be run and demoed immediately.
"""

import os
import uuid
import shutil
import datetime as dt
from typing import Optional, List

from fastapi import FastAPI, Depends, HTTPException, status, UploadFile, File, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr, Field

from sqlalchemy import (
    create_engine, Column, Integer, String, Float, Boolean, DateTime,
    ForeignKey, Text, Enum as SAEnum
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Session

from passlib.context import CryptContext
from jose import jwt, JWTError

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ktc.db")
if DATABASE_URL.startswith("postgres://"):
    # Render / Heroku style URLs use the old "postgres://" scheme; SQLAlchemy
    # (via psycopg2) needs "postgresql://".
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

JWT_SECRET = os.getenv("JWT_SECRET", "change-this-secret-in-production")
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 12  # 12 hours

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

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
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=dt.datetime.utcnow)

    department = relationship("Department", back_populates="users")


class WorkPlan(Base):
    __tablename__ = "work_plans"
    id = Column(Integer, primary_key=True, index=True)
    financial_year = Column(String(20), nullable=False)   # e.g. "2026/27"
    title = Column(String(200), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=dt.datetime.utcnow)

    budget_codes = relationship("BudgetCode", back_populates="work_plan")


class BudgetCode(Base):
    __tablename__ = "budget_codes"
    id = Column(Integer, primary_key=True, index=True)
    work_plan_id = Column(Integer, ForeignKey("work_plans.id"), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    code = Column(String(30), nullable=False)
    output_description = Column(String(255), nullable=False)
    programme = Column(String(150))
    sub_programme = Column(String(150))
    unit_of_measure = Column(String(50))
    baseline_value = Column(Float, default=0)
    planned_target = Column(Float, default=0)
    allocated_amount = Column(Float, default=0)
    funding_source = Column(String(100), default="Local Revenue")

    work_plan = relationship("WorkPlan", back_populates="budget_codes")
    department = relationship("Department", back_populates="budget_codes")
    activities = relationship("Activity", back_populates="budget_code")

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


class UserOut(BaseModel):
    id: int
    full_name: str
    email: str
    role: str
    department_id: Optional[int] = None
    is_active: bool

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: str
    department_id: Optional[int] = None


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
    code: str
    output_description: str
    programme: Optional[str] = None
    sub_programme: Optional[str] = None
    unit_of_measure: Optional[str] = None
    baseline_value: float = 0
    planned_target: float = 0
    allocated_amount: float = 0
    funding_source: str = "Local Revenue"


class BudgetCodeOut(BaseModel):
    id: int
    work_plan_id: int
    department_id: int
    department_name: Optional[str] = None
    code: str
    output_description: str
    programme: Optional[str] = None
    sub_programme: Optional[str] = None
    unit_of_measure: Optional[str] = None
    baseline_value: float
    planned_target: float
    allocated_amount: float
    funding_source: str
    committed_amount: float
    available_balance: float

    class Config:
        from_attributes = True


class ActivityIn(BaseModel):
    budget_code_id: int
    name: str
    quarter: str = "Q1"


class ActivityOut(ActivityIn):
    id: int
    is_active: bool
    class Config:
        from_attributes = True


class RequisitionIn(BaseModel):
    budget_code_id: int
    activity_id: Optional[int] = None
    activity_details: str
    amount_requested: float


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

app.mount("/files", StaticFiles(directory=UPLOAD_DIR), name="files")


@app.on_event("startup")
def seed_data():
    db = SessionLocal()
    try:
        if db.query(User).count() == 0:
            dep = Department(name="Administration and Support Services", code="ADM")
            db.add(dep)
            db.commit()
            db.refresh(dep)

            admin_email = os.getenv("ADMIN_EMAIL", "admin@karugutu.town.go.ug")
            admin_password = os.getenv("ADMIN_PASSWORD", "Admin@2026")
            admin = User(
                full_name="System Administrator",
                email=admin_email,
                hashed_password=hash_password(admin_password),
                role="admin",
                department_id=dep.id,
            )
            db.add(admin)
            db.commit()
            log_action(db, None, "system.seed", f"Seeded initial admin account {admin_email}")
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


# ---------------------------- Departments -----------------------------------

@app.get("/api/departments", response_model=List[DepartmentOut])
def list_departments(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return db.query(Department).order_by(Department.name).all()


@app.post("/api/departments", response_model=DepartmentOut)
def create_department(payload: DepartmentIn, db: Session = Depends(get_db), admin: User = Depends(require_roles("admin"))):
    if db.query(Department).filter(Department.code == payload.code).first():
        raise HTTPException(status_code=400, detail="Department code already exists")
    dep = Department(**payload.dict())
    db.add(dep)
    db.commit()
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
    return BudgetCodeOut(
        id=bc.id, work_plan_id=bc.work_plan_id, department_id=bc.department_id,
        department_name=bc.department.name if bc.department else None,
        code=bc.code, output_description=bc.output_description, programme=bc.programme,
        sub_programme=bc.sub_programme, unit_of_measure=bc.unit_of_measure,
        baseline_value=bc.baseline_value, planned_target=bc.planned_target,
        allocated_amount=bc.allocated_amount, funding_source=bc.funding_source,
        committed_amount=bc.committed_amount, available_balance=bc.available_balance,
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


@app.post("/api/budget-codes", response_model=BudgetCodeOut)
def create_budget_code(payload: BudgetCodeIn, db: Session = Depends(get_db), admin: User = Depends(require_roles("admin"))):
    bc = BudgetCode(**payload.dict())
    db.add(bc)
    db.commit()
    db.refresh(bc)
    log_action(db, admin.id, "budget_code.create", f"{bc.code} - {bc.output_description}")
    return budget_code_to_out(bc)


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


def requisition_to_dict(r: Requisition) -> dict:
    return {
        "id": r.id,
        "ref_no": r.ref_no,
        "requester_id": r.requester_id,
        "requester_name": r.requester.full_name if r.requester else None,
        "department_id": r.department_id,
        "department_name": r.department.name if r.department else None,
        "budget_code_id": r.budget_code_id,
        "budget_code": r.budget_code.code if r.budget_code else None,
        "budget_output": r.budget_code.output_description if r.budget_code else None,
        "activity_id": r.activity_id,
        "activity_name": r.activity.name if r.activity else None,
        "activity_details": r.activity_details,
        "amount_requested": r.amount_requested,
        "status": r.status,
        "current_stage": r.current_stage,
        "created_at": r.created_at.isoformat() if r.created_at else None,
        "updated_at": r.updated_at.isoformat() if r.updated_at else None,
        "approvals": [
            {
                "stage": a.stage, "actor": a.actor.full_name if a.actor else None,
                "action": a.action, "comments": a.comments,
                "created_at": a.created_at.isoformat() if a.created_at else None,
            } for a in r.approvals
        ],
        "documents": [
            {"id": d.id, "filename": d.filename, "doc_type": d.doc_type, "url": f"/files/{os.path.basename(d.stored_path)}"}
            for d in r.documents
        ],
        "accountability": {
            "status": r.accountability.status if r.accountability else None,
            "remarks": r.accountability.remarks if r.accountability else None,
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

    r = Requisition(
        ref_no=gen_ref_no(db),
        requester_id=user.id,
        department_id=user.department_id or bc.department_id,
        budget_code_id=payload.budget_code_id,
        activity_id=payload.activity_id,
        activity_details=payload.activity_details,
        amount_requested=payload.amount_requested,
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
            r.current_stage = "done"
            r.status = "approved"
            acc = AccountabilityRecord(requisition_id=r.id, status="pending")
            db.add(acc)
            notify_role(db, "auditor", f"Requisition {r.ref_no} approved - accountability documents required", "accountability_pending", r.id)
            notify(db, r.requester_id, f"Your requisition {r.ref_no} has been fully approved", "approval_completed", r.id)
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


# ---------------------------- Documents -------------------------------------

@app.post("/api/requisitions/{req_id}/documents")
def upload_document(req_id: int, doc_type: str = "supporting", file: UploadFile = File(...),
                     db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    r = db.query(Requisition).filter(Requisition.id == req_id).first()
    if not r:
        raise HTTPException(status_code=404, detail="Requisition not found")
    allowed_ext = {".pdf", ".docx", ".jpg", ".jpeg", ".png"}
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in allowed_ext:
        raise HTTPException(status_code=400, detail="Only PDF, DOCX, JPG and PNG files are allowed")
    stored_name = f"{uuid.uuid4().hex}{ext}"
    stored_path = os.path.join(UPLOAD_DIR, stored_name)
    with open(stored_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    doc = Document(requisition_id=r.id, filename=file.filename, stored_path=stored_path,
                    doc_type=doc_type, uploaded_by=user.id)
    db.add(doc)
    db.commit()
    log_action(db, user.id, "document.upload", f"{file.filename} on {r.ref_no}")
    return {"id": doc.id, "filename": doc.filename, "doc_type": doc.doc_type, "url": f"/files/{stored_name}"}


# ---------------------------- Accountability --------------------------------

@app.post("/api/requisitions/{req_id}/accountability")
def update_accountability(req_id: int, payload: AccountabilityIn,
                           db: Session = Depends(get_db), user: User = Depends(require_roles("auditor", "admin"))):
    r = db.query(Requisition).filter(Requisition.id == req_id).first()
    if not r or not r.accountability:
        raise HTTPException(status_code=404, detail="No accountability record found for this requisition")
    r.accountability.status = payload.status
    r.accountability.remarks = payload.remarks
    r.accountability.auditor_id = user.id
    r.accountability.updated_at = dt.datetime.utcnow()
    if payload.status == "verified":
        r.status = "accounted"
    db.commit()
    log_action(db, user.id, "accountability.update", f"{r.ref_no} -> {payload.status}")
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

    total_budget = db.query(BudgetCode).with_entities(BudgetCode.allocated_amount).all()
    total_budget_sum = sum(v[0] for v in total_budget)
    all_codes = db.query(BudgetCode).all()
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
