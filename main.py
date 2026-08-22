<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>KTC-IPFMS — Karugutu Town Council</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,500;8..60,600;8..60,700&family=Inter:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
<style>
/* ==========================================================================
KTC-IPFMS — Design tokens
Institutional teal + ink navy + ledger gold. Serif display for authority,
Inter for interface, Plex Mono for reference numbers & figures.
========================================================================== */
:root{
--navy-950:#0A1F2B;
--navy-900:#0D2B3A;
--teal-700:#0F5C52;
--teal-600:#146B5F;
--teal-500:#1C8577;
--gold-600:#B9852F;
--gold-500:#C99A3E;
--gold-100:#F6ECD8;
--paper:#F3F6F5;
--paper-raised:#FFFFFF;
--ink-900:#152226;
--ink-700:#3B4C51;
--ink-500:#6B7C80;
--line:#DEE6E4;
--line-strong:#C7D2D0;
--success:#1F8A5F;
--success-bg:#E6F4ED;
--danger:#B8382A;
--danger-bg:#FBEAE7;
--warning:#B7790E;
--warning-bg:#FBF1DE;
--info:#2E5E8C;
--info-bg:#E9F1FA;
--wp-head-bg:#F0B90B;
--wp-head-text:#3A2900;
--radius:10px;
--radius-sm:6px;
--radius-lg:16px;
--shadow-sm:0 1px 2px rgba(10,31,43,.06), 0 1px 1px rgba(10,31,43,.04);
--shadow-md:0 8px 24px rgba(10,31,43,.09), 0 2px 8px rgba(10,31,43,.06);
--shadow-lg:0 24px 56px rgba(10,31,43,.20), 0 4px 14px rgba(10,31,43,.08);
--shadow-ring:0 0 0 3px rgba(28,133,119,.14);
--shadow-gold-ring:0 0 0 3px rgba(201,154,62,.18);
--ease:cubic-bezier(.22,1,.36,1);
--font-display:'Source Serif 4', Georgia, serif;
--font-body:'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
--font-mono:'IBM Plex Mono', ui-monospace, monospace;
}
*,*::before,*::after{box-sizing:border-box;}
html,body{height:100%;}
body{
margin:0; background:var(--paper); color:var(--ink-900);
font-family:var(--font-body); font-size:14px; line-height:1.5;
-webkit-font-smoothing:antialiased; -moz-osx-font-smoothing:grayscale;
text-rendering:optimizeLegibility;
}
button{font-family:inherit;}
a{color:inherit;}
::selection{background:var(--gold-100); color:var(--navy-950);}
:focus-visible{outline:2px solid var(--teal-500); outline-offset:2px; border-radius:4px;}
::-webkit-scrollbar{width:10px;height:10px;}
::-webkit-scrollbar-thumb{background:var(--line-strong);border-radius:8px;}
::-webkit-scrollbar-thumb:hover{background:var(--teal-500);}
::-webkit-scrollbar-track{background:transparent;}
@media (prefers-reduced-motion: reduce){
*,*::before,*::after{animation-duration:.001ms !important; animation-iteration-count:1 !important; transition-duration:.001ms !important; scroll-behavior:auto !important;}
}
@keyframes fadeInUp{from{opacity:0; transform:translateY(8px);} to{opacity:1; transform:translateY(0);}}
@keyframes fadeIn{from{opacity:0;} to{opacity:1;}}
@keyframes scaleIn{from{opacity:0; transform:scale(.97) translateY(6px);} to{opacity:1; transform:scale(1) translateY(0);}}
/* ---------------- Seal / crest (signature element) ---------------- */
.crest{ width:38px;height:38px;flex-shrink:0; filter:drop-shadow(0 3px 6px rgba(10,31,43,.35)); border-radius:7px; overflow:hidden; background:rgba(255,255,255,.06); }
.crest img{width:100%;height:100%;display:block; object-fit:cover;}
/* ---------------- Login ---------------- */
#login-screen{
min-height:100vh; display:flex; align-items:center; justify-content:center;
position:relative; overflow:hidden;
background:
radial-gradient(1100px 600px at 15% -10%, rgba(28,133,119,.35), transparent 60%),
radial-gradient(900px 500px at 110% 10%, rgba(201,154,62,.20), transparent 55%),
linear-gradient(180deg, var(--navy-950), var(--navy-900) 60%, #0B2530);
padding:24px;
}
#login-screen::before{
content:""; position:absolute; inset:0; pointer-events:none; opacity:.5;
background-image:
repeating-linear-gradient(0deg, rgba(255,255,255,.035) 0 1px, transparent 1px 34px),
repeating-linear-gradient(90deg, rgba(255,255,255,.02) 0 1px, transparent 1px 34px);
}
#login-screen::after{
content:""; position:absolute; left:50%; top:50%; width:900px; height:900px; margin:-450px 0 0 -450px;
background:radial-gradient(circle, rgba(201,154,62,.10), transparent 62%); pointer-events:none;
}
.login-card{
width:100%; max-width:420px; background:var(--paper-raised); border-radius:var(--radius-lg);
box-shadow:var(--shadow-lg); overflow:hidden; border:1px solid rgba(255,255,255,.08);
position:relative; z-index:1; animation:scaleIn .5s var(--ease) both;
}
.login-band{
background:linear-gradient(120deg, var(--teal-700), var(--teal-600) 55%, var(--teal-500));
padding:30px 30px 26px; color:#fff; position:relative; overflow:hidden;
}
.login-band::before{
content:""; position:absolute; right:-40px; top:-40px; width:160px; height:160px; border-radius:50%;
background:radial-gradient(circle, rgba(255,255,255,.14), transparent 70%);
}
.login-band::after{
content:""; position:absolute; inset:auto 0 0 0; height:4px;
background:linear-gradient(90deg, var(--gold-500), rgba(201,154,62,.15) 75%, transparent);
}
.login-band .brand-row{display:flex; align-items:center; gap:12px; position:relative;}
.login-band h1{font-family:var(--font-display); font-size:19.5px; font-weight:600; margin:0; letter-spacing:.15px;}
.login-band p{margin:4px 0 0; font-size:12.5px; color:rgba(255,255,255,.85); letter-spacing:.1px;}
.login-body{padding:30px 30px 32px;}
.field{margin-bottom:16px;}
.field label{display:block; font-size:11px; font-weight:700; color:var(--ink-700); margin-bottom:6px; letter-spacing:.6px; text-transform:uppercase;}
.field input, .field select, .field textarea{
width:100%; padding:11px 13px; border:1.5px solid var(--line); border-radius:var(--radius-sm);
font-size:14px; font-family:inherit; background:#fff; color:var(--ink-900); transition:border-color .15s var(--ease), box-shadow .15s var(--ease);
}
.field input:hover, .field select:hover{border-color:var(--line-strong);}
.field input:focus, .field select:focus, .field textarea:focus{
border-color:var(--teal-500); box-shadow:var(--shadow-ring);
}
.password-field-wrap{position:relative;}
.password-field-wrap input{padding-right:42px;}
.password-toggle-btn{
position:absolute; right:4px; top:50%; transform:translateY(-50%);
width:32px; height:32px; display:flex; align-items:center; justify-content:center;
background:transparent; border:none; border-radius:6px; padding:0; margin:0;
color:var(--ink-500); cursor:pointer; transition:color .15s var(--ease), background .15s var(--ease);
}
.password-toggle-btn svg{width:18px; height:18px;}
.password-toggle-btn:hover{color:var(--teal-600); background:var(--paper);}
.password-toggle-btn:focus-visible{outline:2px solid var(--teal-500); outline-offset:1px;}
.rev-custom-field{display:none; margin-top:8px;}
.btn{
display:inline-flex; align-items:center; justify-content:center; gap:8px;
padding:10px 18px; border-radius:var(--radius-sm); border:1px solid transparent;
font-weight:600; font-size:13.5px; cursor:pointer; transition:transform .12s var(--ease), box-shadow .18s var(--ease), background .15s var(--ease), border-color .15s var(--ease);
white-space:nowrap; position:relative;
}
.btn:active{transform:translateY(1px) scale(.99);}
.btn-icon{width:14px; height:14px; flex-shrink:0;}
.foot-nowrap{flex-wrap:nowrap;}
@media (max-width:480px){
.foot-nowrap{gap:6px;}
.foot-nowrap .btn{padding:10px 10px; font-size:12.5px;}
}
.btn-primary{background:var(--teal-700); color:#fff; box-shadow:var(--shadow-sm);}
.btn-primary:hover{background:var(--teal-600); box-shadow:0 6px 16px rgba(15,92,82,.32);}
.btn-primary:focus-visible{box-shadow:var(--shadow-ring);}
.btn-gold{background:var(--gold-600); color:#fff;}
.btn-gold:hover{background:var(--gold-500); box-shadow:0 6px 16px rgba(185,133,47,.32);}
.btn-ghost{background:transparent; color:var(--ink-700); border-color:var(--line);}
.btn-ghost:hover{background:var(--paper); border-color:var(--line-strong);}
.btn-danger{background:var(--danger); color:#fff;}
.btn-danger:hover{background:#a03024; box-shadow:0 6px 16px rgba(184,56,42,.28);}
.btn-block{width:100%;}
.btn:disabled{opacity:.55; cursor:not-allowed; transform:none;}
.login-error{
background:var(--danger-bg); color:var(--danger); border:1px solid rgba(184,56,42,.25);
padding:10px 12px; border-radius:var(--radius-sm); font-size:13px; margin-bottom:14px; display:none;
animation:fadeIn .2s var(--ease);
}
.login-hint{margin-top:18px; font-size:11.5px; color:var(--ink-500); text-align:center; line-height:1.6;}
/* ---------------- App shell ---------------- */
#app-screen{display:none; height:100vh; overflow:hidden;}
.shell{display:flex; height:100vh;}
.sidebar{
width:232px; flex-shrink:0; background:linear-gradient(185deg, var(--navy-950), var(--navy-900));
color:#DCE7E5; display:flex; flex-direction:column; padding:18px 12px;
border-right:1px solid rgba(255,255,255,.05); position:relative;
}
.sidebar::after{
content:""; position:absolute; right:0; top:0; bottom:0; width:1px;
background:linear-gradient(180deg, transparent, rgba(201,154,62,.35), transparent);
}
.sidebar .brand{display:flex; align-items:center; gap:10px; padding:6px 8px 18px; border-bottom:1px solid rgba(255,255,255,.08); margin-bottom:14px;}
.sidebar .brand-name{font-family:var(--font-display); font-size:14px; font-weight:600; color:#fff; line-height:1.25;}
.sidebar .brand-name small{display:block; font-family:var(--font-body); font-weight:500; font-size:10px; color:rgba(255,255,255,.55); letter-spacing:.6px; text-transform:uppercase; margin-top:2px;}
.nav-group{margin-bottom:6px;}
.nav-label{font-size:10px; text-transform:uppercase; letter-spacing:.9px; color:rgba(255,255,255,.35); padding:14px 10px 6px; font-weight:700;}
.nav-item{
display:flex; align-items:center; gap:10px; padding:9px 10px; border-radius:8px; cursor:pointer;
font-size:13px; font-weight:500; color:rgba(220,231,229,.82); margin-bottom:2px; transition:background .15s var(--ease), color .15s var(--ease), transform .12s var(--ease);
border:none; background:none; width:100%; text-align:left;
}
.nav-item svg{width:17px;height:17px; flex-shrink:0; opacity:.85; transition:opacity .15s var(--ease);}
.nav-item:hover{background:rgba(255,255,255,.07); color:#fff; transform:translateX(1px);}
.nav-item:hover svg{opacity:1;}
.nav-item.active{background:linear-gradient(90deg, var(--teal-700), rgba(15,92,82,.75)); color:#fff; box-shadow:inset 3px 0 0 var(--gold-500);}
.nav-item.active svg{opacity:1;}
.sidebar-footer{margin-top:auto; padding:10px 8px 4px; border-top:1px solid rgba(255,255,255,.08);}
.user-chip{display:flex; align-items:center; gap:9px; padding:8px; border-radius:8px; transition:background .15s var(--ease); cursor:pointer; border:none; background:none; width:100%; text-align:left;}
.user-chip:hover{background:rgba(255,255,255,.05);}
.avatar{
width:33px;height:33px;border-radius:50%; background:linear-gradient(135deg, var(--gold-500), var(--gold-600));
color:#fff; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:12.5px; flex-shrink:0;
box-shadow:0 0 0 2px rgba(255,255,255,.12), 0 2px 6px rgba(0,0,0,.3);
}
.user-chip .u-name{font-size:12.5px; font-weight:600; color:#fff; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;}
.user-chip .u-role{font-size:10.5px; color:rgba(255,255,255,.5); text-transform:capitalize;}
.logout-link{font-size:11.5px; color:rgba(255,255,255,.45); margin-top:6px; display:block; padding:0 8px; cursor:pointer; transition:color .15s var(--ease);}
.logout-link:hover{color:var(--gold-500);}
.main{flex:1; display:flex; flex-direction:column; min-width:0; overflow:hidden;}
.topbar{
min-height:64px; flex-shrink:0; background:rgba(255,255,255,.86); backdrop-filter:blur(10px) saturate(1.4); -webkit-backdrop-filter:blur(10px) saturate(1.4);
border-bottom:1px solid var(--line); box-shadow:0 1px 0 rgba(10,31,43,.02);
display:flex; align-items:center; justify-content:space-between; padding:0 22px; position:relative; z-index:10; flex-wrap:wrap; gap:10px;
}
.topbar-title{font-family:var(--font-display); font-size:22px; font-weight:600; letter-spacing:.1px; color:var(--teal-700);}
.topbar-sub{font-size:11.5px; color:var(--ink-500); margin-top:1px;}
.topbar-title-wrap{min-width:0; flex:1;}
.topbar-title-wrap-center{text-align:center;}
.topbar-title-lg{font-size:23px; font-weight:600; line-height:1.32; color:var(--teal-700); letter-spacing:.1px; max-width:640px; margin:0 auto;}
@media (min-width:901px){
.topbar-title-wrap-center{display:flex; justify-content:center;}
.topbar-title-lg{white-space:nowrap; max-width:none; font-size:clamp(13px,1.5vw,22px);}
}
.topbar-right{display:flex; align-items:center; gap:14px; padding:10px 0;}
.topbar.topbar-workplan{border-bottom:none !important; box-shadow:none !important;}
.topbar.topbar-workplan .topbar-title-wrap{display:none !important;}
#view-workplan > .card:first-of-type{flex-wrap:nowrap !important;}
#view-workplan > .card:first-of-type #wp-select{width:auto !important; min-width:0 !important; flex:1 1 auto !important;}
#view-workplan > .card:first-of-type > div[style*="display:flex"]{flex-shrink:0 !important;}
@media (max-width:640px){
#view-workplan > .card:first-of-type{flex-wrap:wrap !important;}
#view-workplan > .card:first-of-type #wp-select{width:100% !important;}
}
#wp-main-table-wrap{max-height:600px !important;}
.icon-btn{
position:relative; width:36px;height:36px; border-radius:9px; border:1px solid var(--line); background:#fff;
display:flex; align-items:center; justify-content:center; cursor:pointer; color:var(--ink-700);
transition:background .15s var(--ease), border-color .15s var(--ease), transform .12s var(--ease);
}
.icon-btn:hover{background:var(--paper); border-color:var(--teal-500); color:var(--teal-700); transform:translateY(-1px);}
.icon-btn:active{transform:translateY(0);}
.icon-btn svg{width:17px;height:17px;}
.icon-btn-sm{width:28px;height:28px;border-radius:7px;}
.icon-btn-sm svg{width:14px;height:14px;}
/* ---------------- Table titles + their icon actions (Add / Import etc) ---------------- */
.table-title-row{display:flex; align-items:center; gap:8px; flex-wrap:wrap;}
.table-title-actions{display:flex; align-items:center; gap:6px; flex-shrink:0;}
/* Pull the Annual Work Plan title (dropdown container) right up to the top
   of the view, removing the large empty band that used to sit above it. */
.content:has(> #view-workplan.active){padding-top:0;}
#view-workplan{margin:0;}
#view-workplan > .card:first-of-type{margin:0 !important; padding-top:8px !important; padding-bottom:10px !important;}
.badge-dot{
position:absolute; top:-4px; right:-4px; min-width:16px; height:16px; padding:0 4px; border-radius:9px;
background:var(--danger); color:#fff; font-size:9.5px; font-weight:700; display:flex; align-items:center; justify-content:center;
box-shadow:0 0 0 2px #fff;
}
.content{flex:1; overflow-y:auto; padding:24px 26px 60px;}
.view{display:none;}
.view.active{display:block; animation:fadeInUp .35s var(--ease) both;}
/* ---------------- Notification panel ---------------- */
.notif-panel{
position:absolute; top:58px; right:22px; width:340px; max-height:420px; overflow-y:auto;
background:rgba(255,255,255,.98); backdrop-filter:blur(14px); border:1px solid var(--line); border-radius:var(--radius); box-shadow:var(--shadow-lg);
z-index:80; display:none;
}
.notif-panel.show{display:block; animation:scaleIn .2s var(--ease);}
.notif-panel-head{display:flex; justify-content:space-between; align-items:center; padding:12px 14px; border-bottom:1px solid var(--line);}
.notif-panel-head h4{margin:0; font-size:13px;}
.notif-panel-head span{font-size:11.5px; color:var(--teal-600); cursor:pointer; font-weight:600; transition:color .15s var(--ease);}
.notif-panel-head span:hover{color:var(--teal-700);}
.notif-item{padding:11px 14px; border-bottom:1px solid #F0F3F2; font-size:12.5px; display:flex; gap:9px; transition:background .12s var(--ease);}
.notif-item:hover{background:#FAFCFB;}
.notif-item:last-child{border-bottom:none;}
.notif-item .dot{width:7px;height:7px;border-radius:50%; margin-top:5px; flex-shrink:0; background:var(--teal-500);}
.notif-item.unread{background:#F7FBFA;}
.notif-item .msg{color:var(--ink-900);}
.notif-item .time{color:var(--ink-500); font-size:10.5px; margin-top:2px;}
.notif-empty{padding:24px 14px; text-align:center; color:var(--ink-500); font-size:12.5px;}
/* ---------------- Section headers, cards ---------------- */
.section-head{display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:18px; flex-wrap:wrap; gap:12px;}
.section-head h2{font-family:var(--font-display); font-size:22px; margin:0; font-weight:600; letter-spacing:.1px;}
.section-head .sub{color:var(--ink-500); font-size:12.5px; margin-top:2px;}
.card{background:var(--paper-raised); border:1px solid var(--line); border-radius:var(--radius); box-shadow:var(--shadow-sm); transition:box-shadow .2s var(--ease), border-color .2s var(--ease);}
.card-pad{padding:18px 20px;}
/* Dashboard stat cards (home tab — deliberately distinct treatment) */
.stat-grid{display:grid; grid-template-columns:repeat(4,1fr); gap:16px; margin-bottom:22px;}
.stat-card{
background:var(--paper-raised); border:1px solid var(--line); border-radius:var(--radius);
padding:18px 20px; position:relative; overflow:hidden;
transition:transform .2s var(--ease), box-shadow .2s var(--ease), border-color .2s var(--ease);
}
.stat-card:hover{transform:translateY(-2px); box-shadow:var(--shadow-md); border-color:var(--line-strong);}
.stat-card::before{
content:""; position:absolute; left:0; top:0; bottom:0; width:4px; background:var(--teal-600);
}
.stat-card::after{
content:""; position:absolute; right:-30px; top:-30px; width:90px; height:90px; border-radius:50%;
background:radial-gradient(circle, rgba(15,92,82,.06), transparent 70%); pointer-events:none;
}
.stat-card.gold::before{background:var(--gold-600);}
.stat-card.gold::after{background:radial-gradient(circle, rgba(185,133,47,.08), transparent 70%);}
.stat-card.danger::before{background:var(--danger);}
.stat-card.danger::after{background:radial-gradient(circle, rgba(184,56,42,.07), transparent 70%);}
.stat-card.navy::before{background:var(--navy-900);}
.stat-card.navy::after{background:radial-gradient(circle, rgba(10,31,43,.08), transparent 70%);}
.stat-label{font-size:10.5px; text-transform:uppercase; letter-spacing:.6px; color:var(--ink-500); font-weight:700;}
.stat-value{font-family:var(--font-mono); font-size:29px; font-weight:600; margin-top:8px; color:var(--navy-950); letter-spacing:-.2px;}
.stat-foot{font-size:11.5px; color:var(--ink-500); margin-top:6px;}
.dash-grid{display:grid; grid-template-columns:1.4fr 1fr; gap:18px;}
@media (max-width:1100px){ .dash-grid{grid-template-columns:1fr;} .stat-grid{grid-template-columns:repeat(2,1fr);} }
.util-bar-track{height:10px; border-radius:6px; background:#EAF0EF; overflow:hidden; margin-top:10px; box-shadow:inset 0 1px 2px rgba(10,31,43,.06);}
.util-bar-fill{height:100%; background:linear-gradient(90deg, var(--teal-600), var(--teal-500)); border-radius:6px; transition:width .7s var(--ease); box-shadow:0 0 8px rgba(28,133,119,.5);}
.timeline{list-style:none; margin:0; padding:0;}
.timeline li{display:flex; gap:12px; padding:11px 0; border-bottom:1px solid #F0F3F2; transition:transform .15s var(--ease);}
.timeline li:hover{transform:translateX(2px);}
.timeline li:last-child{border-bottom:none;}
.tl-stamp{
width:30px; height:30px; border-radius:50%; border:2px solid var(--teal-600); color:var(--teal-600);
display:flex; align-items:center; justify-content:center; flex-shrink:0; font-size:13px; font-weight:700;
background:#F7FBFA; box-shadow:0 1px 3px rgba(10,31,43,.08);
}
.tl-body{flex:1; min-width:0;}
.tl-title{font-size:12.5px; font-weight:600;}
.tl-meta{font-size:11px; color:var(--ink-500); margin-top:1px;}
/* ---------------- Table styling (echoes the reference work-plan grid) ---------------- */
.table-wrap{overflow-x:auto; border-radius:var(--radius); border:1px solid var(--line); box-shadow:var(--shadow-sm);}
table{width:100%; border-collapse:collapse; min-width:720px; background:#fff;}
thead th{
background:var(--navy-950); color:#fff; font-size:10.5px; text-transform:uppercase; letter-spacing:.5px;
padding:12px; text-align:left; font-weight:700; white-space:nowrap; position:sticky; top:0;
box-shadow:0 1px 0 rgba(201,154,62,.35);
}
/* Work Plan & Budget grid gets a distinct deep-yellow header treatment
(per Council request) instead of the navy header used elsewhere. */
#view-workplan .table-wrap thead th{
background:var(--wp-head-bg);
color:var(--wp-head-text);
box-shadow:0 1px 0 rgba(58,41,0,.35);
}
/* Department Budget Summary table (nested white card, inside the teal
header band) needs its own explicit, high-contrast treatment — the
deep-yellow work-plan header and the app-wide near-white row striping
are both too low-contrast in that context to read clearly. Header uses
solid navy + white text (like the main app tables); rows alternate a
clearly visible mint/white band with bold, dark, explicitly-colored text
so figures stand out regardless of the surrounding white card.
Column titles are centered; row content is left aligned, per Council
request, overriding the generic .num right-alignment for this table. */
#wp-dept-summary-table thead th{
background:var(--teal-700) !important;
color:#FFFFFF !important;
box-shadow:0 1px 0 rgba(201,154,62,.35) !important;
text-align:center;
}
#wp-dept-summary-body tr:nth-child(odd){background:#D6EEE6;}
#wp-dept-summary-body tr:nth-child(even){background:#FFFFFF;}
#wp-dept-summary-body tr{border-bottom:1px solid var(--line-strong);}
#wp-dept-summary-body tr:hover{background:var(--gold-100);}
#wp-dept-summary-body td{color:var(--ink-900); font-weight:600; text-align:left;}
#wp-dept-summary-body td.mono, #wp-dept-summary-body td.num{color:var(--navy-950); font-weight:700; text-align:left;}
#wp-dept-summary-wrap tfoot td{text-align:left;}
#view-workplan .table-wrap tfoot tr{background:#EAF0EF !important;}
#view-workplan .table-wrap tfoot td{color:var(--navy-950); font-weight:700;}
/* Requisitions list & Approval Queue tables — widened by at least half so
key columns (Ref No., Requester, Status/Stage, Date) have sufficient room
instead of feeling cramped; the surrounding .table-wrap already scrolls
horizontally if needed. */
#req-list-table{min-width:1080px;}
#req-list-table th:nth-child(1), #req-list-table td:nth-child(1){min-width:150px;}
#req-list-table th:nth-child(2), #req-list-table td:nth-child(2){min-width:190px;}
#req-list-table th:nth-child(3), #req-list-table td:nth-child(3){min-width:160px;}
#req-list-table th:nth-child(6), #req-list-table td:nth-child(6){min-width:150px;}
#req-list-table th:nth-child(7), #req-list-table td:nth-child(7){min-width:150px;}
#req-list-table th:nth-child(8), #req-list-table td:nth-child(8){min-width:150px;}
#approval-queue-table{min-width:1080px;}
#approval-queue-table th:nth-child(1), #approval-queue-table td:nth-child(1){min-width:150px;}
#approval-queue-table th:nth-child(2), #approval-queue-table td:nth-child(2){min-width:190px;}
#approval-queue-table th:nth-child(3), #approval-queue-table td:nth-child(3){min-width:160px;}
#approval-queue-table th:nth-child(7), #approval-queue-table td:nth-child(7){min-width:150px;}
/* Users & Roles table — widened so the Name/Email/Role/Department columns
each have sufficient room instead of feeling cramped; the surrounding
.table-wrap already scrolls horizontally if needed. */
#users-table{min-width:1120px;}
#users-table th:nth-child(1), #users-table td:nth-child(1){min-width:170px;}
#users-table th:nth-child(2), #users-table td:nth-child(2){min-width:220px;}
#users-table th:nth-child(3), #users-table td:nth-child(3){min-width:160px;}
#users-table th:nth-child(4), #users-table td:nth-child(4){min-width:140px;}
#users-table th:nth-child(5), #users-table td:nth-child(5){min-width:130px;}
#users-table th:nth-child(6), #users-table td:nth-child(6){min-width:160px;}
#users-table th:nth-child(7), #users-table td:nth-child(7){min-width:110px;}
#users-table th:nth-child(8), #users-table td:nth-child(8){min-width:90px;}
#users-table th:nth-child(9), #users-table td:nth-child(9){min-width:90px;}
tbody td{padding:11.5px 12px; border-bottom:1px solid #EEF2F1; font-size:12.5px; white-space:normal; overflow-wrap:break-word; word-break:break-word; vertical-align:top;}
tbody tr{transition:background .12s var(--ease);}
tbody tr:nth-child(even){background:#FAFCFB;}
tbody tr:hover{background:var(--gold-100);}
tbody tr:last-child td {
border-bottom: none;
}
td.wrap, th.wrap{white-space:normal;}
.num{font-family:var(--font-mono); text-align:center;}
.mono{font-family:var(--font-mono);}
/* ---------------- Revenue Sources Summary table --------------------------
Same high-contrast treatment as the Department Budget Summary table
(solid teal header, alternating mint/white rows), displayed above it.
THIS TABLE STAYS EXACTLY AS IT IS — its Approved Budget Amount column is
obtained automatically from the Revenue Source by Category for the FY 2026/27 below it (each row's
Category Total = sum of that source's sub rows). Row content (body rows)
is left-aligned per Council request — only the column headers stay
centered. */
#wp-revenue-summary-table thead th{
background:var(--teal-700) !important;
color:#FFFFFF !important;
box-shadow:0 1px 0 rgba(201,154,62,.35) !important;
text-align:center;
}
#wp-revenue-summary-body tr:nth-child(odd){background:#D6EEE6;}
#wp-revenue-summary-body tr:nth-child(even){background:#FFFFFF;}
#wp-revenue-summary-body tr{border-bottom:1px solid var(--line-strong);}
#wp-revenue-summary-body tr:hover{background:var(--gold-100);}
#wp-revenue-summary-body td{color:var(--ink-900); font-weight:600; text-align:left; vertical-align:top;}
#wp-revenue-summary-body td.mono, #wp-revenue-summary-body td.num{color:var(--navy-950); font-weight:700; text-align:left;}
#wp-revenue-summary-wrap tfoot td{text-align:left;}
#wp-revenue-summary-wrap{max-height:260px; overflow-x:auto; overflow-y:auto;}
#wp-revenue-summary-wrap thead th{position:sticky; top:0; z-index:3;}
#wp-revenue-summary-wrap tfoot tr{position:sticky; bottom:0; z-index:3; text-align:left !important;}
#wp-revenue-summary-table thead th{padding:8px 9px; font-size:9.5px; line-height:1.25;}
#wp-revenue-summary-body td{padding:7px 9px; font-size:11.5px;}
/* Functional Definition column in the summary table: allow each point to
sit on its own line (line breaks are inserted when the data is rendered)
rather than running on as one continuous line of text. */
#wp-revenue-summary-body td.rev-func-def{white-space:normal; line-height:1.5;}
#wp-revenue-detail-wrap{max-height:420px; overflow-x:auto; overflow-y:auto;}
#wp-revenue-detail-wrap thead th{
position:sticky; top:0; z-index:3;
background:var(--teal-700) !important; color:#FFFFFF !important;
box-shadow:0 1px 0 rgba(201,154,62,.35) !important; text-align:center;
padding:8px 9px; font-size:9.5px; line-height:1.25;
}
#wp-revenue-detail-body td{padding:7px 9px; font-size:11.5px; color:var(--ink-900); text-align:left; vertical-align:top;}
#wp-revenue-detail-body td.num, #wp-revenue-detail-body td.mono{text-align:left;}
#wp-revenue-detail-body tr.rev-cat-head td{background:var(--gold-100); font-weight:700; color:var(--navy-950); border-bottom:1px solid var(--line-strong);}
#wp-revenue-detail-body tr.rev-cat-head:hover td{background:var(--gold-100);}
#wp-revenue-detail-body tr.rev-item-row td{background:#FFFFFF;}
#wp-revenue-detail-body tr.rev-item-row:hover td{background:#FAFCFB;}
#wp-revenue-detail-body tr.rev-item-row td.rev-item-desc{padding-left:30px; color:var(--ink-700);}
#wp-revenue-detail-body tr.rev-total-row td{background:#D6EEE6; font-weight:700; color:var(--navy-950); border-bottom:1px solid var(--line-strong);}
#wp-revenue-detail-body tr.rev-total-row:hover td{background:#D6EEE6;}
#wp-revenue-detail-body tr.rev-add-row td{background:#FFF9EC; padding:8px 9px;}
#wp-revenue-detail-body tr.rev-add-row input{width:100%; border:1px solid var(--line); border-radius:6px; padding:6px 8px; font-size:12px; background:#fff;}
#wp-revenue-detail-body tr.rev-add-row input:focus{border-color:var(--teal-500); outline:none; box-shadow:var(--shadow-ring);}
/* Functional Definition column in the Revenue Entry (detail) table: each
point begins on its own line rather than running together as one line. */
#wp-revenue-detail-body td.rev-func-def{white-space:normal; line-height:1.5;}
.rev-auto-chip{display:inline-flex; align-items:center; gap:4px; background:var(--success-bg); color:var(--success); border-radius:10px; padding:1.5px 8px; font-size:9.5px; font-weight:700; margin-left:6px; vertical-align:middle;}
.rev-auto-chip::before{content:""; width:6px; height:6px; border-radius:2px; background:var(--success);}
/* ---------------- Work Plan & Budget: compact, height-constrained,
dual-scrollable tables (Department Budget Summary + main grid) ---------- */
#wp-dept-summary-wrap{overflow-x:auto;}
#wp-main-table-wrap{max-height:440px; min-height:220px; overflow-x:auto; overflow-y:auto;}
#wp-dept-summary-wrap thead th, #wp-main-table-wrap thead th{position:sticky; top:0; z-index:3;}
#wp-dept-summary-wrap tfoot tr{position:sticky; bottom:0; z-index:3;}
#wp-dept-summary-table thead th{padding:8px 9px; font-size:9.5px; line-height:1.25;}
#wp-dept-summary-body td{padding:7px 9px; font-size:11.5px;}
#wp-main-table{min-width:1810px;}
#wp-main-table thead th{padding:8px 6px; font-size:9px; line-height:1.25; letter-spacing:.3px;}
#wp-main-table tbody td{padding:6.5px 6px; font-size:11px; font-weight:400; line-height:1.3;}
#wp-main-table td.wrap, #wp-main-table th.wrap{white-space:normal; max-width:118px;}
/* Funding Source (18th column): give it noticeably less room than before */
#wp-main-table th:nth-child(18), #wp-main-table td:nth-child(18){white-space:normal; max-width:78px; width:78px;}
/* Department (1st column): wrap the name across two lines to use the
narrower column width efficiently rather than forcing extra scroll */
#wp-main-table th:nth-child(1), #wp-main-table td:nth-child(1){white-space:normal; max-width:104px; width:104px;}
/* Budget Output Description (6th column): holds long narrative text, so
give it noticeably more room than the other wrapped columns. Widened by
half its original width (260px -> 390px) for extra room. */
#wp-main-table th:nth-child(6), #wp-main-table td:nth-child(6){white-space:normal; max-width:390px; width:390px;}
/* PIAP Output Description (7th) and PIAP Output Indicator (8th) columns —
sit between Budget Output Code/Description and Unit of Measure — need
noticeably more room than the other wrapped columns since they hold
long narrative text. PIAP Output Description is widened by half its
original width (220px -> 330px) for extra room. */
#wp-main-table th:nth-child(7), #wp-main-table td:nth-child(7){white-space:normal; max-width:330px; width:330px;}
#wp-main-table th:nth-child(8), #wp-main-table td:nth-child(8){white-space:normal; max-width:220px; width:220px;}
/* Q1–Q4 and Total Budget columns: keep numbers compact */
#wp-main-table th:nth-child(13), #wp-main-table td:nth-child(13),
#wp-main-table th:nth-child(14), #wp-main-table td:nth-child(14),
#wp-main-table th:nth-child(15), #wp-main-table td:nth-child(15),
#wp-main-table th:nth-child(16), #wp-main-table td:nth-child(16),
#wp-main-table th:nth-child(17), #wp-main-table td:nth-child(17){max-width:92px; width:92px;}
.toolbar{display:flex; gap:10px; align-items:center; margin-bottom:14px; flex-wrap:wrap;}
.search-box{position:relative; flex:1; min-width:220px;}
.search-box svg{position:absolute; left:11px; top:50%; transform:translateY(-50%); width:15px;height:15px; color:var(--ink-500); pointer-events:none;}
.search-box input{width:100%; padding:9px 12px 9px 34px; border:1.5px solid var(--line); border-radius:var(--radius-sm); font-size:13px; transition:border-color .15s var(--ease), box-shadow .15s var(--ease); background:#fff;}
.search-box input:focus{border-color:var(--teal-500); box-shadow:var(--shadow-ring);}
select.filter-select{padding:9px 12px; border:1.5px solid var(--line); border-radius:var(--radius-sm); font-size:13px; background:#fff; transition:border-color .15s var(--ease);}
select.filter-select:focus{border-color:var(--teal-500); box-shadow:var(--shadow-ring);}
/* ---------------- Badges / pills ---------------- */
.pill{display:inline-flex; align-items:center; gap:5px; padding:3.5px 10px; border-radius:20px; font-size:10.5px; font-weight:700; text-transform:capitalize; letter-spacing:.2px;}
.pill::before{content:""; width:5px; height:5px; border-radius:50%; background:currentColor; flex-shrink:0; opacity:.85;}
.pill-draft{background:#EEF1F1; color:var(--ink-700);}
.pill-submitted{background:var(--info-bg); color:var(--info);}
.pill-hod_approved, .pill-treasurer_approved{background:var(--warning-bg); color:var(--warning);}
.pill-approved, .pill-accounted, .pill-verified{background:var(--success-bg); color:var(--success);}
.pill-rejected, .pill-flagged{background:var(--danger-bg); color:var(--danger);}
.pill-returned{background:#F1E9FB; color:#6A3FA0;}
.pill-pending{background:var(--warning-bg); color:var(--warning);}
/* ---------------- Modal ---------------- */
.overlay{position:fixed; inset:0; background:rgba(10,20,26,.6); backdrop-filter:blur(3px); display:none; align-items:center; justify-content:center; z-index:100; padding:20px;}
.overlay.show{display:flex; animation:fadeIn .18s var(--ease);}
.modal{background:#fff; border-radius:var(--radius-lg); width:100%; max-width:560px; max-height:88vh; overflow-y:auto; box-shadow:var(--shadow-lg); animation:scaleIn .25s var(--ease);}
.modal-lg{max-width:760px;}
.modal-head{display:flex; justify-content:space-between; align-items:center; padding:18px 22px; border-bottom:1px solid var(--line);}
.modal-head h3{margin:0; font-family:var(--font-display); font-size:17.5px; font-weight:600;}
.modal-close{background:none; border:none; cursor:pointer; color:var(--ink-500); font-size:20px; line-height:1; width:30px; height:30px; border-radius:7px; display:flex; align-items:center; justify-content:center; transition:background .15s var(--ease), color .15s var(--ease);}
.modal-close:hover{background:var(--danger-bg); color:var(--danger);}
.modal-head-actions{display:flex; align-items:center; gap:4px; flex-shrink:0;}
/* The New/Edit Requisition modal's title is centered in its header bar
   (rather than left-aligned like other modals) — the maximize/close
   buttons are taken out of flow so the title can center against the
   full header width. */
#modal-req .modal-head{position:relative; justify-content:center;}
#modal-req .modal-head-actions{position:absolute; right:22px; top:50%; transform:translateY(-50%);}
.modal-max-btn{background:none; border:none; cursor:pointer; color:var(--ink-500); font-size:15px; line-height:1; width:30px; height:30px; border-radius:7px; display:flex; align-items:center; justify-content:center; transition:background .15s var(--ease), color .15s var(--ease);}
.modal-max-btn:hover{background:var(--gold-100); color:var(--navy-950);}
/* Maximized state — the modal expands to 60% of the viewport width (with
   a slightly taller height so there's a bit more vertical room for the
   requisition form) so wide tables (the requisition meta table /
   line-item table) get the extra width instead of scrolling in a
   cramped box, while still leaving a visible margin around it.
   Minimizing (toggling the class off) simply restores the modal's
   normal centred size. */
.overlay.overlay-maximized{padding:0;}
.modal.modal-maximized{
width:60vw !important; max-width:60vw !important; height:68vh !important; max-height:68vh !important; margin:0 !important; border-radius:var(--radius-lg) !important;
display:flex; flex-direction:column;
overflow:hidden !important;
}
/* The Requisition modal specifically gets extra vertical room (taller,
same width as other maximized modals) so more of the requisition form
is visible without scrolling. This only affects the modal's own height,
not the height of any requisition row/field inside it. */
#modal-req .modal.modal-maximized,
#modal-req-detail .modal.modal-maximized{height:100vh !important; max-height:100vh !important; margin:0 auto !important;}
/* The outer .modal normally scrolls (see .modal above), which — when
maximized — let the modal-head (and its minimize/close buttons) scroll
out of view along with the body content. Locking the outer element and
only letting modal-body scroll keeps the head, with its buttons, stuck
in place at all times. */
.modal.modal-maximized .modal-head{flex-shrink:0; position:sticky; top:0; z-index:2; background:#fff;}
.modal.modal-maximized .modal-body{flex:1; overflow-y:auto;}
.modal.modal-maximized .modal-foot{flex-shrink:0;}
/* Inside a maximized modal, the requisition paper-form and its tables
should use the full width now available instead of staying capped at
their normal narrow max-width. */
.modal.modal-maximized .req-form-paper,
.modal.modal-maximized table.req-form-meta-table,
.modal.modal-maximized table.req-form-table,
.modal.modal-maximized .pv-form{
max-width:100% !important; width:100% !important;
}
.modal-body{padding:20px 22px;}
.modal-foot{padding:16px 22px; border-top:1px solid var(--line); display:flex; justify-content:flex-end; gap:10px; flex-wrap:wrap;}
.form-grid{display:grid; grid-template-columns:1fr 1fr; gap:0 14px;}
.form-grid .span2{grid-column:1/-1;}
/* ---------------- Toasts ---------------- */
#toast-stack{position:fixed; bottom:20px; right:20px; z-index:200; display:flex; flex-direction:column; gap:10px;}
.toast{
background:var(--navy-950); color:#fff; padding:13px 16px; border-radius:10px; box-shadow:var(--shadow-lg);
font-size:13px; min-width:260px; max-width:360px; display:flex; align-items:flex-start; gap:10px;
animation:toast-in .35s var(--ease); backdrop-filter:blur(6px);
}
.toast.success{border-left:4px solid var(--success);}
.toast.error{border-left:4px solid var(--danger);}
.toast.info{border-left:4px solid var(--teal-500);}
@keyframes toast-in{from{opacity:0; transform:translateY(12px) scale(.96);} to{opacity:1; transform:translateY(0) scale(1);}}
.empty-state{padding:50px 20px; text-align:center; color:var(--ink-500);}
.empty-state svg{width:38px;height:38px; color:var(--line-strong); margin-bottom:10px;}
.loading-row{padding:40px; text-align:center; color:var(--ink-500); font-size:13px;}
.spinner{
width:16px;height:16px; border:2px solid rgba(255,255,255,.35); border-top-color:#fff; border-radius:50%;
display:inline-block; animation:spin .7s linear infinite;
}
.spinner-dark{border:2px solid var(--line-strong); border-top-color:var(--teal-600);}
@keyframes spin{to{transform:rotate(360deg);}}
.tabs-sub{display:flex; gap:4px; border-bottom:1px solid var(--line); margin-bottom:18px;}
.tabs-sub button{
background:none; border:none; padding:9px 4px; margin-right:22px; font-size:13px; font-weight:600; color:var(--ink-500);
cursor:pointer; border-bottom:2px solid transparent; margin-bottom:-1px;
}
.tabs-sub button.active{color:var(--teal-700); border-color:var(--teal-600);}
.detail-grid{display:grid; grid-template-columns:1fr 1fr; gap:14px 22px; margin-bottom:16px;}
.detail-label{font-size:10.5px; text-transform:uppercase; letter-spacing:.4px; color:var(--ink-500); font-weight:700;}
.detail-value{font-size:13.5px; margin-top:2px; font-weight:500;}
.help-text{font-size:11.5px; color:var(--ink-500); margin-top:4px;}
.divider{height:1px; background:var(--line); margin:16px 0;}
.kicker{font-size:10.5px; text-transform:uppercase; letter-spacing:.7px; color:var(--gold-600); font-weight:700;}
/* ---------------- Section groups inside forms ---------------- */
.field-section{margin-top:4px;}
.field-section .kicker{display:block; margin-bottom:2px;}
/* ---------------- My Settings / Signature ---------------- */
.sig-preview-box{
width:180px; height:80px; border:1.5px dashed var(--line-strong); border-radius:var(--radius-sm);
display:flex; align-items:center; justify-content:center; background:var(--paper); overflow:hidden; flex-shrink:0;
}
.sig-preview-box img{max-width:100%; max-height:100%; object-fit:contain;}
/* ---------------- Printable Requisition Form (mirrors the Council's paper form) ---------------- */
/* All fixed pixel sizing in this block (fonts, padding, margins, heights)
   is scaled to 86% of its original 100% value — this is the on-screen
   default requisition layout size. Percentage widths (table width:100%
   etc.) are left alone since they're already relative to the paper's own
   container, not an absolute size. */
.req-form-paper{
background:#fff; padding:8.6px 5.2px 5.2px; font-family:var(--font-body); color:#181818;
}
/* Requisition form header — a single pre-composed banner image (header.jpg)
   replaces the old text+crest+seal composite so the on-screen form matches
   the Council's printed letterhead exactly. */
.rf-header-img{display:block; width:91%; height:auto; margin:0 auto 8.6px; border-radius:4px;}
.req-form-header{text-align:center; margin-bottom:1.7px;}
.req-form-header .rf-title{font-family:var(--font-display); font-size:19.5px; font-weight:800; letter-spacing:.34px; text-transform:uppercase; margin-top:6px;}
.rf-refno{text-align:right; font-size:10.75px; margin:1.7px 0 8.6px; font-weight:600;}
.rf-refno .mono{color:#b8382a; font-weight:800;}
table.req-form-meta-table{width:100%; max-width:100%; table-layout:fixed; box-sizing:border-box; border-collapse:collapse; margin:6.9px 0 12.04px; font-size:10.75px; border:1px solid #333;}
table.req-form-meta-table td{border:1px solid #333; padding:4.3px 6.9px; vertical-align:bottom; overflow-wrap:break-word; word-break:break-word;}
table.req-form-meta-table td strong{margin-right:5.2px;}
table.req-form-meta-table td .rf-fill{display:inline-block; min-height:13.76px; vertical-align:bottom;}
table.req-form-meta-table td .rf-fill img{max-height:37.84px; max-width:154.8px; object-fit:contain; vertical-align:bottom;}
.req-form-subject{font-size:10.75px; margin:0 0 12.04px; line-height:2;}
.req-form-subject strong{white-space:nowrap; margin-right:3.44px;}
.req-form-subject .rf-dots{border-bottom:1px dotted #666; display:inline-block;}
table.req-form-table{width:100%; max-width:100%; table-layout:fixed; box-sizing:border-box; border-collapse:collapse; margin-bottom:12.04px; font-size:10.32px; border:1px solid #e2790f;}
/* Requisition / Payment Voucher line-item table rules are orange per
   Council request, so the printed and on-screen line grid stands out
   from the rest of the black-ruled paper form. */
table.req-form-table th, table.req-form-table td{border:1px solid #e2790f; padding:5.16px 6.9px; overflow-wrap:break-word; word-break:break-word;}
table.req-form-table th{background:#fdf1e2; font-size:9.03px; text-transform:uppercase; text-align:left; color:#8a4a09;}
table.req-form-table td.num, table.req-form-table th.num{text-align:right; font-family:var(--font-mono);}
table.req-form-table tr.rf-section-head td{font-weight:700; background:#fffaf3;}
table.req-form-table tr.rf-subtotal td{font-weight:700; border-top:2px double #e2790f;}
table.req-form-table tr.rf-grand td{font-weight:700; border-top:2px double #e2790f; background:#fdf1e2; font-size:10.75px; text-transform:uppercase;}
.req-form-words{font-size:10.75px; margin-bottom:25.8px; line-height:2;}
.req-form-words strong{white-space:nowrap; margin-right:3.44px;}
.req-form-words .rf-dots{border-bottom:1px dotted #666; display:inline-block;}
.req-form-signatures{display:grid; grid-template-columns:repeat(3,1fr); border:1px solid #333; margin-top:15.48px;}
.req-form-signatures > div{padding:11px 13px 13px; border-left:1px solid #333;}
.req-form-signatures > div:first-child{border-left:none;}
.req-form-signatures .sig-role{font-size:11.5px; font-weight:600; margin-bottom:24px;}
.req-form-signatures .sig-line{border-bottom:1px dotted #666; margin-bottom:8px; height:44px; display:flex; align-items:flex-end; padding-bottom:1.72px;}
/* Space between the dotted signature line and the role label — shows the
   authorizer's name pulled from the system (auto-filled when they attach
   their signature) while staying an editable field on the entry form. */
.req-form-signatures .sig-name-fill{margin:0 0 6px;}
.req-form-signatures .sig-name-fill input{width:100%; border:none; background:transparent; font:inherit; font-size:11px; font-weight:600; text-align:center; color:#181818; padding:2px 4px;}
.req-form-signatures .sig-name-fill input::placeholder{font-weight:400; color:var(--ink-500);}
.req-form-signatures .sig-name-fill input:focus{outline:1px dashed var(--gold-600); background:#fffdf2; border-radius:3px;}
.req-form-signatures .sig-name{margin:0 0 6px; font-size:11px; font-weight:600; text-align:center; min-height:14px;}
/* Unscoped so every signature box — including the Payment Voucher's Vote
Book / Verified by / Passed Payment / payee / witness / cashier boxes,
which sit in a plain table rather than inside .req-form-signatures — gets
the same enlarged, clearly-visible signature image once one is attached. */
.sig-line img{max-height:37.84px; max-width:95%; object-fit:contain;}
.req-form-signatures .sig-label{font-size:11.5px; font-weight:800;}
@media print{
@page{ size:A4; margin:12mm; }
body *{visibility:hidden;}
#print-form-container, #print-form-container *{visibility:visible;}
.overlay#modal-print-form{position:absolute; inset:auto; background:none; padding:0;}
#print-form-container{position:absolute; top:0; left:0; width:100%; max-width:none; box-shadow:none; border:none; max-height:none;}
.no-print{display:none !important;}
/* The 86% on-screen sizing above is a screen-only default — restore the
   original full-size dimensions for the physical printed page. */
#print-form-container .req-form-paper{padding:10px 6px 6px;}
#print-form-container .rf-header-img{width:91%; margin:0 auto 10px;}
#print-form-container .req-form-header{margin-bottom:2px;}
#print-form-container .req-form-header .rf-title{font-size:23px; letter-spacing:.45px; margin-top:7px;}
#print-form-container .rf-refno{font-size:12.5px; margin:2px 0 10px;}
#print-form-container table.req-form-meta-table{margin:8px 0 14px; font-size:12.5px;}
#print-form-container table.req-form-meta-table td{padding:5px 8px;}
#print-form-container table.req-form-meta-table td strong{margin-right:6px;}
#print-form-container table.req-form-meta-table td .rf-fill{min-height:16px;}
#print-form-container table.req-form-meta-table td .rf-fill img{max-height:44px; max-width:180px;}
#print-form-container .req-form-subject{font-size:12.5px; margin:0 0 14px;}
#print-form-container .req-form-subject strong{margin-right:4px;}
#print-form-container table.req-form-table{margin-bottom:14px; font-size:12px;}
#print-form-container table.req-form-table th, #print-form-container table.req-form-table td{padding:6px 8px;}
#print-form-container table.req-form-table th{font-size:10.5px;}
#print-form-container table.req-form-table tr.rf-grand td{font-size:12.5px;}
#print-form-container .req-form-words{font-size:12.5px; margin-bottom:30px;}
#print-form-container .req-form-words strong{margin-right:4px;}
#print-form-container .req-form-signatures{margin-top:18px;}
#print-form-container .req-form-signatures > div{padding:12px 14px 14px;}
#print-form-container .req-form-signatures .sig-role{font-size:13px; margin-bottom:28px;}
#print-form-container .req-form-signatures .sig-line{margin-bottom:9px; height:50px; padding-bottom:2px;}
#print-form-container .sig-line img{max-height:44px;}
#print-form-container .req-form-signatures .sig-name-fill, #print-form-container .req-form-signatures .sig-name{margin:0 0 8px; font-size:13px;}
#print-form-container .req-form-signatures .sig-label{font-size:13px;}
}
/* ---------------- Requisition data-entry form (styled as the paper form itself) ---------------- */
.req-digital-controls{background:var(--paper); border:1px solid var(--line); border-radius:var(--radius-sm); padding:12px 14px 14px; margin-bottom:16px;}
.req-digital-controls .form-grid{margin-top:8px;}
table.req-form-meta-table.entry td{padding:5px 8px;}
table.req-form-meta-table.entry .rf-field{display:flex; align-items:baseline; gap:4px;}
table.req-form-meta-table.entry .rf-field strong{white-space:nowrap; font-size:12px;}
table.req-form-meta-table.entry input, table.req-form-meta-table.entry select, table.req-form-meta-table.entry textarea{flex:1; min-width:0; border:none; background:transparent; font:inherit; font-size:12.5px; color:#181818; padding:2px 0;}
table.req-form-meta-table.entry input[readonly]{color:#333;}
table.req-form-meta-table.entry input:focus, table.req-form-meta-table.entry select:focus, table.req-form-meta-table.entry textarea:focus{outline:1px dashed var(--gold-600); background:#fffdf2; border-radius:3px;}
/* Read-only, system-filled fields (System User Name, Email, Role, Date,
Activity Budget Limit/Balance) don't need to stretch across the rest of
the cell — they hug their own content so the value sits immediately
after the colon instead of leaving a wide empty gap. */
table.req-form-meta-table.entry .rf-field-tight{display:inline-flex; gap:4px; max-width:100%;}
table.req-form-meta-table.entry .rf-field-tight .rf-fill{flex:none; font-size:12.5px; color:#333; overflow-wrap:break-word; word-break:break-word; min-height:auto;}
table.req-form-meta-table.entry .rf-field-desc textarea{width:100%; resize:none; overflow:hidden; white-space:pre-wrap; word-wrap:break-word; overflow-wrap:break-word; line-height:1.35; min-height:20px; display:block;}
.req-form-subject.entry{display:flex; align-items:baseline; gap:6px;}
.req-form-subject.entry input{flex:1; border:none; border-bottom:1px dotted #888; background:transparent; font:inherit; font-size:12.5px; padding:2px 4px;}
.req-form-subject.entry input:focus{outline:none; border-bottom:1px dotted var(--gold-600); background:#fffdf2;}
table.req-form-table.entry td{padding:3px 4px;}
table.req-form-table.entry input{width:100%; border:none; background:transparent; font:inherit; font-size:12px; padding:4px 4px; color:#181818;}
table.req-form-table.entry input:focus{outline:1px dashed var(--gold-600); background:#fffdf2; border-radius:3px;}
table.req-form-table.entry input[data-li-field="qty"], table.req-form-table.entry input[data-li-field="rate"], table.req-form-table.entry input[data-li-field="amount"]{text-align:right; font-family:var(--font-mono);}
/* Description column is a textarea so long text wraps onto new lines and
grows the row, instead of a single-line input that hides overflow text. */
table.req-form-table.entry textarea[data-li-field="description"]{
width:100%; border:none; background:transparent; font:inherit; font-size:12px; padding:4px 4px; color:#181818;
resize:none; overflow:hidden; white-space:pre-wrap; word-wrap:break-word; line-height:1.35; display:block; min-height:20px;
}
table.req-form-table.entry textarea[data-li-field="description"]:focus{outline:1px dashed var(--gold-600); background:#fffdf2; border-radius:3px;}
table.req-form-table.entry td.no-print{padding:3px 2px; text-align:center; vertical-align:middle;}
table.req-form-table.entry .rf-row-remove, table.req-form-table.entry .rf-row-add{background:none; border:1px solid var(--line); border-radius:4px; color:var(--ink-500); cursor:pointer; font-size:11px; line-height:1; padding:3px 4px; margin:1px;}
table.req-form-table.entry .rf-row-remove:hover{color:#fff; background:var(--danger, #b8382a); border-color:var(--danger, #b8382a);}
table.req-form-table.entry .rf-row-add:hover{color:#fff; background:var(--teal-600); border-color:var(--teal-600);}
/* Ledger tables (meta table, line-item table) always close every row and
   column with a visible rule, including empty trailing cells such as the
   remove-line column and grand-total spacer cells. */
table.req-form-meta-table td:last-child{border-right:1px solid #333;}
table.req-form-meta-table tr:last-child td{border-bottom:1px solid #333;}
table.req-form-table th:last-child, table.req-form-table td:last-child{border-right:1px solid #e2790f;}
table.req-form-table tr:last-child td, table.req-form-table tfoot tr:last-child td{border-bottom:1px solid #e2790f;}
table.req-form-table.entry tr.rf-grand td{font-family:var(--font-mono);}
/* Budget Output Code search field (replaces the old <select> dropdown) */
.rf-bc-search-wrap{position:relative; flex:1; min-width:0;}
.rf-bc-search-wrap input{width:100%;}
.rf-bc-results{
display:none; position:absolute; z-index:40; top:100%; left:0; right:0; margin-top:2px;
background:#fff; border:1px solid var(--line); border-radius:6px; box-shadow:0 8px 20px rgba(10,20,26,.14);
max-height:220px; overflow-y:auto; text-align:left;
}
.rf-bc-results.open{display:block;}
.rf-bc-results .rf-bc-opt{padding:7px 10px; font-size:12px; cursor:pointer; border-bottom:1px solid var(--line);}
.rf-bc-results .rf-bc-opt:last-child{border-bottom:none;}
.rf-bc-results .rf-bc-opt:hover, .rf-bc-results .rf-bc-opt.active{background:#fdf1e2;}
.rf-bc-results .rf-bc-opt .rf-bc-code{font-weight:700; font-family:var(--font-mono); margin-right:6px;}
.rf-bc-results .rf-bc-empty{padding:8px 10px; font-size:12px; color:var(--ink-500);}
.req-form-words.entry{font-size:12.5px; margin-bottom:18px;}
.req-form-signatures.preview .sig-line{border-bottom:1px dotted #ccc;}
.req-form-signatures.preview{opacity:.7;}
/* ---------------- Attach-signature buttons + Cheque Payment Voucher (entry form) ---------------- */
.sig-attach-btn{display:inline-flex; align-items:center; gap:4px; font-size:10.5px; padding:3px 8px; margin-top:4px; border:1px dashed var(--gold-600, #b8860b); background:#fffdf2; color:#7a5b00; border-radius:5px; cursor:pointer;}
.sig-attach-btn:hover{background:#fff4d6;}
.rf-sig-slot{display:flex; flex-direction:row; align-items:center; flex-wrap:wrap; gap:8px;}
.rf-sig-slot .rf-fill{flex:1 1 auto; min-width:60px;}
.rf-sig-slot .sig-attach-btn{flex-basis:100%;}
.pv-form{margin-top:26px; padding-top:18px; border-top:2px dashed var(--line);}
.pv-form .rf-title{margin-top:2px;}
.pv-certify{font-size:11.5px; line-height:1.7; border:1px solid #333; padding:10px 12px; margin:10px 0 14px;}
.pv-certify p{margin:0 0 8px;}
.pv-certify p:last-child{margin-bottom:0;}
/* Authority / Total / Approved Vote / Account No / Approved Estimate / Cheque
   Instruction No — on the paper form these are plain fill-in-the-blank lines
   inside the same bordered box as the certify paragraphs below, not a boxed
   mini-table, so they're styled to match that (dotted fill, no cell borders). */
.pv-plain-line{display:flex; flex-wrap:wrap; gap:6px; align-items:baseline; font-size:12.5px; margin-bottom:8px;}
.pv-plain-line strong{white-space:nowrap; font-weight:700;}
.pv-plain-line .rf-dots{flex:1; min-width:80px;}
.pv-plain-line.entry input{flex:1; min-width:80px; border:none; border-bottom:1px dotted #888; background:transparent; font:inherit; font-size:12.5px; padding:2px 4px;}
.pv-plain-line.entry input:focus{outline:none; border-bottom:1px dotted var(--gold-600); background:#fffdf2;}
table.pv-block-table{width:100%; border-collapse:collapse; font-size:12px; margin-bottom:14px;}
table.pv-block-table td{border:1px solid #333; padding:6px 8px; vertical-align:top;}
table.pv-block-table td strong{display:block; font-size:11px; margin-bottom:4px;}
table.pv-block-table input{width:100%; border:none; background:transparent; font:inherit; font-size:12.5px; color:#181818; padding:2px 2px;}
table.pv-block-table input:focus{outline:1px dashed var(--gold-600); background:#fffdf2; border-radius:3px;}
.pv-received-line{font-size:12.5px; line-height:2; margin-bottom:14px;}
.pv-received-line input{border:none; border-bottom:1px dotted #888; background:transparent; font:inherit; font-size:12.5px; padding:2px 4px; text-align:center;}
.pv-received-line input:focus{outline:none; border-bottom:1px dotted var(--gold-600); background:#fffdf2;}
.pv-received-line input.pv-day{width:44px;}
.pv-received-line input.pv-words{width:60%; min-width:180px; text-align:left;}
/* ---------------- Hamburger / responsive sidebar ---------------- */
.hamburger-btn{display:none;}
.sidebar-backdrop{display:none;}
@media (max-width: 900px){
.hamburger-btn{display:flex;}
.sidebar{
position:fixed; top:0; left:0; bottom:0; z-index:150; width:250px;
transform:translateX(-100%); transition:transform .25s var(--ease);
}
.sidebar.open{transform:translateX(0); box-shadow:var(--shadow-lg);}
.sidebar-backdrop{
display:none; position:fixed; inset:0; background:rgba(10,20,26,.55); z-index:140;
}
.sidebar-backdrop.show{display:block; animation:fadeIn .2s var(--ease);}
.stat-grid{grid-template-columns:repeat(2,1fr);}
.form-grid{grid-template-columns:1fr;}
.detail-grid{grid-template-columns:1fr;}
.content{padding:18px 16px 50px;}
}
@media (max-width:560px){
.stat-grid{grid-template-columns:1fr;}
.topbar{padding:0 14px;}
.topbar-title-lg{font-size:18px; line-height:1.3;}
.content{padding:14px 12px 50px;}
.toolbar{flex-direction:column; align-items:stretch;}
.req-form-meta{grid-template-columns:1fr;}
.req-form-signatures{grid-template-columns:1fr;}
}
#wp-dept-summary-wrap tfoot td {
text-align: left !important;
}
/* Align all table headers in the green div to the left */
#wp-revenue-summary-wrap thead th,
#wp-dept-summary-wrap thead th,
#wp-revenue-detail-wrap thead th {
  text-align: left !important;
}
/* ---------------- Clear-all header icon buttons ---------------- */
.th-clear-btn{
background:none; border:none; cursor:pointer; padding:4px; border-radius:5px;
display:inline-flex; align-items:center; justify-content:center;
color:inherit; opacity:.85; transition:background .15s var(--ease), color .15s var(--ease), opacity .15s var(--ease);
vertical-align:middle; flex-shrink:0;
}
.topbar.topbar-workplan .topbar-title-wrap{display:flex !important;}
.th-clear-btn:hover{background:rgba(184,56,42,.9); color:#fff; opacity:1;}
.th-clear-btn svg{width:14px;height:14px; display:block; pointer-events:none;}
.th-with-clear{display:flex; align-items:center; justify-content:space-between; gap:6px; white-space:nowrap;}
</style>
</head>
<body>
<!-- ===================== LOGIN ===================== -->
<div id="login-screen">
<div class="login-card">
<div class="login-band">
<div class="brand-row">
<div class="crest"><img src="logoo.jpeg" alt="Karugutu Town Council Crest" /></div>
<div>
<h1>Karugutu Town Council</h1>
<p>Integrated Public Financial Management System</p>
</div>
</div>
</div>
<div class="login-body">
<div class="login-error" id="login-error"></div>
<form id="login-form" autocomplete="off">
<div class="field">
<label>Signing in as</label>
<select id="login-role" required>
<option value="">— Select your role —</option>
<option value="staff">Staff Member</option>
<option value="hod">Head of Department</option>
<option value="treasurer">Senior Treasurer</option>
<option value="clerk">Town Clerk</option>
<option value="auditor">Internal Auditor</option>
<option value="admin">System Administrator</option>
</select>
</div>
<div class="field">
<label>Email address</label>
<input type="email" id="login-email" required autocomplete="off" placeholder="you@karugutu.town.go.ug" />
</div>
<div class="field">
<label>Password</label>
<div class="password-field-wrap">
<input type="password" id="login-password" required autocomplete="new-password" placeholder="••••••••" />
<button type="button" class="password-toggle-btn" id="login-password-toggle" aria-label="Show password" title="Show password">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7-11-7-11-7z"/><circle cx="12" cy="12" r="3"/></svg>
</button>
</div>
</div>
<button type="submit" class="btn btn-primary btn-block" id="login-btn">Sign in to your account</button>
</form>
<p class="login-hint">Access is restricted to authorised Council personnel. Contact your System Administrator for account issues.</p>
</div>
</div>
</div>
<!-- ===================== APP ===================== -->
<div id="app-screen">
<div class="sidebar-backdrop" id="sidebar-backdrop"></div>
<div class="shell">
<aside class="sidebar">
<div class="brand">
<div class="crest"><img src="logoo.jpeg" alt="Karugutu Town Council Crest" /></div>
<div class="brand-name">Karugutu Town Council
<small>KTC-IPFMS</small>
</div>
</div>
<div class="nav-group">
<button class="nav-item active" data-view="dashboard">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="7" height="9" rx="1.5"/><rect x="14" y="3" width="7" height="5" rx="1.5"/><rect x="14" y="12" width="7" height="9" rx="1.5"/><rect x="3" y="16" width="7" height="5" rx="1.5"/></svg>
Dashboard
</button>
<button class="nav-item" data-view="workplan">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 5h16M4 5v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V5M9 9h6M9 13h6M9 17h3"/></svg>
Work Plan &amp; Budget
</button>
<button class="nav-item" data-view="requisitions" style="font-size:12px; line-height:1.25;">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9 3h6l1 3H8l1-3z"/><path d="M6 6h12v14a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V6z"/><path d="M9 11h6M9 15h4"/></svg>
Requisition Voucher, Payment Voucher and Accountability documents
</button>
<button class="nav-item" data-view="approvals">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="9"/></svg>
Approvals
</button>
<button class="nav-item" data-view="accountability">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 19.5V6a2 2 0 0 1 2-2h9l5 5v10.5a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z"/><path d="M14 4v5h5"/></svg>
Accountability
</button>
<button class="nav-item" data-view="reports">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 19V5a1 1 0 0 1 1-1h9l6 6v9a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1z"/><path d="M9 12h6M9 16h4"/></svg>
Audit &amp; Reports
</button>
</div>
<div class="nav-group" id="admin-nav-group" style="display:none;">
<div class="nav-label">Administration</div>
<button class="nav-item" data-view="users">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17.5" cy="8.5" r="2.3"/><path d="M15.5 14a5.5 5.5 0 0 1 5 6"/></svg>
Users &amp; Roles
</button>
<button class="nav-item" data-view="departments">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 21V8l9-5 9 5v13"/><path d="M9 21v-6h6v6M3 21h18"/></svg>
Departments
</button>
</div>
<div class="sidebar-footer">
<button class="user-chip" id="user-chip-btn" title="My Settings &amp; Signature">
<div class="avatar" id="sb-avatar">A</div>
<div style="min-width:0;">
<div class="u-name" id="sb-name">—</div>
<div class="u-role" id="sb-role">—</div>
</div>
</button>
<span class="logout-link" id="logout-btn">Sign out</span>
</div>
</aside>
<main class="main">
<div class="topbar">
<button class="icon-btn hamburger-btn" id="hamburger-btn" title="Menu">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
</button>
<div class="topbar-title-wrap" id="topbar-title-wrap">
<div class="topbar-title" id="topbar-title">Dashboard</div>
<div class="topbar-sub" id="topbar-sub">Overview of financial activity</div>
</div>
<div class="topbar-right">
<span id="wp-fy-title" style="display:none;">—</span>
<button class="icon-btn" id="notif-btn" title="Notifications">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6 8a6 6 0 1 1 12 0c0 5 2 6 2 6H4s2-1 2-6z"/><path d="M9.5 20a2.5 2.5 0 0 0 5 0"/></svg>
<span class="badge-dot" id="notif-badge" style="display:none;">0</span>
</button>
</div>
</div>
<div class="notif-panel" id="notif-panel">
<div class="notif-panel-head">
<h4>Notifications</h4>
<span id="mark-all-read">Mark all read</span>
</div>
<div id="notif-list"></div>
</div>
<div class="content">
<!-- ===== DASHBOARD ===== -->
<div class="view active" id="view-dashboard">
<div class="section-head">
<div>
<h2>Financial Overview</h2>
<div class="sub" id="dash-fy-label">Current position across all requisitions</div>
</div>
</div>
<div class="stat-grid">
<div class="stat-card">
<div class="stat-label">Pending Approvals</div>
<div class="stat-value" id="stat-pending">—</div>
<div class="stat-foot">Awaiting action in the workflow</div>
</div>
<div class="stat-card gold">
<div class="stat-label">Approved Requisitions</div>
<div class="stat-value" id="stat-approved">—</div>
<div class="stat-foot">Fully cleared to accountability</div>
</div>
<div class="stat-card danger">
<div class="stat-label">Rejected Requisitions</div>
<div class="stat-value" id="stat-rejected">—</div>
<div class="stat-foot">Closed without disbursement</div>
</div>
<div class="stat-card navy">
<div class="stat-label">Total Budget (UGX)</div>
<div class="stat-value" id="stat-budget" style="font-size:22px;">—</div>
<div class="stat-foot">Across all active budget codes</div>
</div>
</div>
<div class="dash-grid">
<div class="card card-pad">
<div class="kicker">Recent Activity</div>
<ul class="timeline" id="recent-activity-list" style="margin-top:8px;">
<li class="loading-row"><span class="spinner spinner-dark"></span></li>
</ul>
</div>
<div class="card card-pad">
<div class="kicker">Budget Utilisation</div>
<div style="font-family:var(--font-mono); font-size:24px; font-weight:600; margin-top:8px;" id="util-pct">—</div>
<div class="util-bar-track"><div class="util-bar-fill" id="util-bar" style="width:0%;"></div></div>
<div class="help-text" id="util-detail">Loading budget position…</div>
<div class="divider"></div>
<div class="kicker">Quick Actions</div>
<div style="display:flex; flex-direction:column; gap:8px; margin-top:10px;">
<button class="btn btn-primary btn-block" id="qa-new-req">New Requisition</button>
<button class="btn btn-ghost btn-block" data-view-link="approvals">Review Approval Queue</button>
</div>
</div>
</div>
<div class="card card-pad" style="margin-top:18px;">
<div class="kicker">Budget by Department</div>
<div class="help-text" style="margin-top:2px;">Total allocated budget (UGX) across all work plans, by department</div>
<div id="dept-chart" style="margin-top:16px;">
<div class="loading-row"><span class="spinner spinner-dark"></span></div>
</div>
</div>
</div>
<!-- ===== WORK PLAN & BUDGET (styled per reference) ===== -->
<div class="view" id="view-workplan">
<div class="card" style="background:#fff; border:none; padding:16px 20px; margin:0; display:flex; align-items:center; justify-content:center; gap:16px; flex-wrap:wrap; box-shadow:none; width:100%; box-sizing:border-box;">
<select class="filter-select" id="wp-select" style="flex:1 1 auto; width:100%; min-width:260px; max-width:none; text-align:center; text-align-last:center; font-family:var(--font-display); font-weight:600; font-size:17px; color:var(--navy-950); padding:12px 14px; border-radius:var(--radius-sm);"></select>
<div style="display:flex; align-items:center; gap:8px; flex-shrink:0;">
<button class="icon-btn" id="wp-new-workplan-btn" title="Add Annual Work Plan &amp; Budget Estimates" style="display:none;">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 5v14M5 12h14"/></svg>
</button>
<button class="icon-btn" id="wp-edit-workplan-btn" title="Edit Annual Work Plan &amp; Budget Estimates" style="display:none;">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg>
</button>
<!-- Downloads the full Annual Work Plan & Budget PDF (all sections + revenue/workplan tables) -->
<button class="icon-btn" id="wp-download-pdf-btn" title="Download Annual Work Plan &amp; Budget as PDF">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3v12"/><path d="M7 10l5 5 5-5"/><path d="M5 21h14"/></svg>
</button>
</div>
</div>
<input type="file" id="wp-import-revenue-file" accept=".xlsx,.xls" style="display:none;" />
<input type="file" id="wp-import-file" accept=".xlsx,.xls" style="display:none;" />
<div style="background:linear-gradient(120deg, var(--teal-700), var(--teal-500)); border-radius:14px; padding:20px 24px; color:#fff; margin-bottom:20px; box-shadow:var(--shadow-md);">
<div class="card" style="background:rgba(255,255,255,.97); border:none; overflow:hidden;">
<div style="padding:14px 18px 4px;">
<div class="kicker" id="wp-title-revenue-summary" style="font-size:13px; color:var(--navy-950);">APPROVED SUMMARY OF THE COUNCIL BUDGET FRAMEWORK PAPER AND PRELIMINARY REVENUE ESTIMATES FOR FY 2026/2027</div>
</div>
<div class="table-wrap" id="wp-revenue-summary-wrap" style="border:none; box-shadow:none; margin:10px 16px 16px;">
<table id="wp-revenue-summary-table">
<thead>
<tr>
<th>Revenue Source</th>
<th>Revenue Source Definition</th>
<th>Revenue Source Amount (UGX)</th>
</tr>
</thead>
<tbody id="wp-revenue-summary-body">
<tr><td colspan="3" class="loading-row"><span class="spinner spinner-dark"></span></td></tr>
</tbody>
<tfoot>
<tr style="font-weight:700; background:#EAF0EF; text-align:left;">
<td colspan="2">Total Revenue</td>
<td class="num mono" id="wp-revenue-summary-total">—</td>
</tr>
</tfoot>
</table>
</div>
</div>
<div class="card" style="background:rgba(255,255,255,.97); border:none; overflow:hidden; margin-top:16px;">
<div style="padding:14px 18px 4px;">
<div class="kicker" id="wp-title-dept-summary" style="font-size:13px; color:var(--navy-950);">APPROVED DEPARTMENTAL SUMMARY OF THE COUNCIL ANNUAL WORK PLAN AND EXPENDITURE ESTIMATES FOR FY 2026/2027</div>
</div>
<div class="table-wrap" id="wp-dept-summary-wrap" style="border:none; box-shadow:none; margin:10px 16px 16px;">
<table id="wp-dept-summary-table">
<thead>
<tr>
<th>Department</th>
<th>Q1<br>(UGX)</th>
<th>Q2<br>(UGX)</th>
<th>Q3<br>(UGX)</th>
<th>Q4<br>(UGX)</th>
<th>Total Budget<br>(UGX)</th>
<th>Uncommitted Departmental<br>Balance (UGX)</th>
</tr>
</thead>
<tbody id="wp-dept-summary-body">
<tr><td colspan="7" class="loading-row"><span class="spinner spinner-dark"></span></td></tr>
</tbody>
<tfoot>
<tr style="font-weight:700; background:#EAF0EF; text-align:left;">
<td colspan="1">Sub Total</td>
<td class="num mono" id="wp-summary-q1">—</td>
<td class="num mono" id="wp-summary-q2">—</td>
<td class="num mono" id="wp-summary-q3">—</td>
<td class="num mono" id="wp-summary-q4">—</td>
<td class="num mono" id="wp-summary-total">—</td>
<td class="num mono" id="wp-summary-uncommitted">—</td>
</tr>
</tfoot>
</table>
</div>
</div>
</div>
<div class="card" style="background:rgba(255,255,255,.97); border:none; overflow:hidden; margin-top:16px;">
<div style="padding:14px 18px 4px;">
<div class="table-title-row">
<div class="kicker" id="wp-title-revenue-detail" style="font-size:13px; color:var(--navy-950);">APPROVED COUNCIL BUDGET FRAMEWORK PAPER AND PRELIMINARY REVENUE ESTIMATES FOR FY 2026/2027</div>
<div class="table-title-actions">
<button type="button" class="icon-btn icon-btn-sm" id="wp-new-revenue-btn" style="display:none;" title="Add Revenue Sources">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 5v14M5 12h14"/></svg>
</button>
<button type="button" class="icon-btn icon-btn-sm" id="wp-import-revenue-btn" style="display:none;" title="Import Revenue Sources From Excel">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3v12"/><path d="M7 8l5-5 5 5"/><path d="M5 21h14"/></svg>
</button>
</div>
</div>
</div>
<div class="table-wrap" id="wp-revenue-detail-wrap" style="border:none; box-shadow:none; margin:10px 16px 16px;">
<table id="wp-revenue-detail-table">
<thead>
<tr>
<th>PBS Fund Code</th>
<th>Revenue Source</th>
<th>Revenue Item (Functional Definition)</th>
<th>Approved Budget Estimates<br> by Revenue Source (UGX)</th>
<th>Approved Budget Estimate<br> by Revenue Source Category
(UGX)</th>
<th>
<span class="th-with-clear">
<span></span>
<button type="button" class="th-clear-btn" id="wp-revenue-clear-btn" style="display:none;" title="Clear all revenue sources — deletes every revenue source and sub row in this table for the selected work plan">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18"/><path d="M8 6V4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2"/><path d="M19 6l-1 14a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1L5 6"/><path d="M10 11v6M14 11v6"/></svg>
</button>
</span>
</th>
</tr>
</thead>
<tbody id="wp-revenue-detail-body">
<tr><td colspan="6" class="loading-row"><span class="spinner spinner-dark"></span></td></tr>
</tbody>
</table>
</div>
</div>
<br>
<div class="toolbar">
<div class="search-box">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
<input type="text" id="wp-search" placeholder="Search budget outputs, codes…" />
</div>
<select class="filter-select" id="wp-dept-filter"><option value="">All Departments</option></select>
</div>
<div class="table-title-row" id="wp-main-table-heading" style="margin-bottom:10px;">
<div class="kicker" id="wp-title-main-table" style="font-size:13px; color:var(--navy-950);">APPROVED COUNCIL ANNUAL WORK PLAN AND EXPENDITURE ESTIMATES FOR FY 2026/2027</div>
<div class="table-title-actions">
<button type="button" class="icon-btn icon-btn-sm" id="wp-new-btn" style="display:none;" title="Add Activity Output & Expenditure Estimates">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 5v14M5 12h14"/></svg>
</button>
<button type="button" class="icon-btn icon-btn-sm" id="wp-import-btn" style="display:none;" title="Import Activity & Budget Estimates From Excel">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3v12"/><path d="M7 8l5-5 5 5"/><path d="M5 21h14"/></svg>
</button>
</div>
</div>
<div class="table-wrap" id="wp-main-table-wrap">
<table id="wp-main-table">
<thead>
<tr>
<th class="wrap">Department</th>
<th class="wrap">Service<br>Area</th>
<th class="wrap">Programme</th>
<th class="wrap">Sub<br>Programme</th>
<th class="wrap">Budget Output<br>Code</th>
<th class="wrap">Budget Output<br>Description</th>
<th class="wrap">PIAP Output<br>Description</th>
<th class="wrap">PIAP Output<br>Indicator</th>
<th class="wrap">Unit of<br>Measure</th>
<th class="wrap">Baseline<br>Value</th>
<th class="wrap">Planned<br>Target</th>
<th class="wrap">Actual<br>Output</th>
<th class="wrap">Q1<br>(UGX)</th>
<th class="wrap">Q2<br>(UGX)</th>
<th class="wrap">Q3<br>(UGX)</th>
<th class="wrap">Q4<br>(UGX)</th>
<th class="wrap">Total Budget<br>(UGX)</th>
<th class="wrap">Funding<br>Source</th>
<th class="wrap">Responsible<br>Party</th>
<th>
<span class="th-with-clear">
<span></span>
<button type="button" class="th-clear-btn" id="wp-clear-btn" style="display:none;" title="Clear all activity &amp; budget estimate rows — deletes every row in this table for the selected work plan">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18"/><path d="M8 6V4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2"/><path d="M19 6l-1 14a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1L5 6"/><path d="M10 11v6M14 11v6"/></svg>
</button>
</span>
</th>
</tr>
</thead>
<tbody id="wp-table-body">
<tr><td colspan="20" class="loading-row"><span class="spinner spinner-dark"></span></td></tr>
</tbody>
</table>
</div>
<div class="card card-pad" style="margin-top:18px;">
<div class="kicker">📊 Baseline vs. Planned Target vs. Actual Output — by Department</div>
<div class="help-text" style="margin-top:2px;">Maps previous performance (Baseline Value) against the Planned Target and the Actual Output Delivered for each department, to pinpoint achievement and variance margins clearly (reflects the department filter and search currently applied above).</div>
<div id="wp-output-chart" style="margin-top:16px; overflow-x:auto;">
<div class="loading-row"><span class="spinner spinner-dark"></span></div>
</div>
</div>
<div class="card card-pad" style="margin-top:18px;">
<div class="kicker">🥧 Budget Share by Department</div>
<div class="help-text" style="margin-top:2px;">Proportion of total allocated budget contributed by each department (reflects the department filter and search currently applied above)</div>
<div id="wp-pie-chart" style="margin-top:16px; display:flex; gap:28px; flex-wrap:wrap; align-items:center;">
<div class="loading-row"><span class="spinner spinner-dark"></span></div>
</div>
</div>
</div>
<!-- ===== REQUISITIONS ===== -->
<div class="view" id="view-requisitions">
<div class="section-head">
<div>
<h2>Financial Requisitions</h2>
<div class="sub">Create, track and submit requisitions against approved budget codes</div>
</div>
<button class="btn btn-primary" id="new-req-btn">Add New Requisition</button>
</div>
<div class="toolbar">
<div class="search-box">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
<input type="text" id="req-search" placeholder="Search by reference number or subject…" />
</div>
<select class="filter-select" id="req-status-filter">
<option value="">All Statuses</option>
<option value="draft">Draft</option>
<option value="submitted">Submitted</option>
<option value="hod_approved">HOD Approved</option>
<option value="treasurer_approved">Treasurer Approved</option>
<option value="approved">Fully Approved</option>
<option value="rejected">Rejected</option>
<option value="returned">Returned</option>
<option value="accounted">Accounted</option>
</select>
</div>
<div class="table-wrap">
<table id="req-list-table">
<thead>
<tr><th>Ref No.</th><th>Requester</th><th>Department</th><th class="wrap">Subject</th><th>Amount (UGX)</th><th>Status</th><th>Stage</th><th>Date</th><th></th></tr>
</thead>
<tbody id="req-table-body"><tr><td colspan="9" class="loading-row"><span class="spinner spinner-dark"></span></td></tr></tbody>
</table>
</div>
</div>
<!-- ===== APPROVALS ===== -->
<div class="view" id="view-approvals">
<div class="section-head">
<div>
<h2>Approval Queue</h2>
<div class="sub">Items awaiting your decision at your stage of the workflow</div>
</div>
</div>
<div class="table-wrap">
<table id="approval-queue-table">
<thead>
<tr><th>Ref No.</th><th>Requester</th><th>Department</th><th class="wrap">Subject</th><th>Amount (UGX)</th><th>Available Balance</th><th>Stage</th><th></th></tr>
</thead>
<tbody id="approval-table-body"><tr><td colspan="8" class="loading-row"><span class="spinner spinner-dark"></span></td></tr></tbody>
</table>
</div>
</div>
<!-- ===== ACCOUNTABILITY ===== -->
<div class="view" id="view-accountability">
<div class="section-head">
<div>
<h2>Accountability</h2>
<div class="sub">Verify supporting documentation for fully approved requisitions</div>
</div>
</div>
<div class="table-wrap">
<table>
<thead>
<tr><th>Ref No.</th><th>Department</th><th>Amount (UGX)</th><th>Documents</th><th>Status</th><th></th></tr>
</thead>
<tbody id="acc-table-body"><tr><td colspan="6" class="loading-row"><span class="spinner spinner-dark"></span></td></tr></tbody>
</table>
</div>
</div>
<!-- ===== REPORTS / AUDIT ===== -->
<div class="view" id="view-reports">
<div class="section-head">
<div>
<h2>Audit &amp; Reports</h2>
<div class="sub">System-wide activity log and single-page audit views</div>
</div>
</div>
<div class="tabs-sub">
<button class="active" data-subtab="audit-log">System Audit Log</button>
<button data-subtab="audit-view">Requisition Audit View</button>
</div>
<div id="subtab-audit-log">
<div class="table-wrap">
<table>
<thead><tr><th>Timestamp</th><th>User ID</th><th>Action</th><th class="wrap">Details</th></tr></thead>
<tbody id="audit-log-body"><tr><td colspan="4" class="loading-row"><span class="spinner spinner-dark"></span></td></tr></tbody>
</table>
</div>
</div>
<div id="subtab-audit-view" style="display:none;">
<div class="card card-pad" style="max-width:420px; margin-bottom:18px;">
<label style="font-size:12px; font-weight:600; color:var(--ink-700); display:block; margin-bottom:6px;">Enter Requisition Reference or ID</label>
<div style="display:flex; gap:8px;">
<input type="text" id="audit-view-search" placeholder="e.g. 12" style="flex:1; padding:9px 12px; border:1.5px solid var(--line); border-radius:var(--radius-sm);" />
<button class="btn btn-primary" id="audit-view-btn">View</button>
</div>
</div>
<div id="audit-view-result"></div>
</div>
</div>
<!-- ===== USERS ===== -->
<div class="view" id="view-users">
<div class="section-head">
<div>
<h2>Users &amp; Roles</h2>
<div class="sub">Manage Council staff accounts and role-based access</div>
</div>
<button class="btn btn-primary" id="new-user-btn">+ New User</button>
</div>
<div class="table-wrap">
<table id="users-table">
<thead><tr><th>Name</th><th>Email</th><th>Position</th><th>Telephone</th><th>Password</th><th>Role</th><th>Department</th><th>Status</th><th></th><th></th></tr></thead>
<tbody id="users-table-body"><tr><td colspan="10" class="loading-row"><span class="spinner spinner-dark"></span></td></tr></tbody>
</table>
</div>
</div>
<!-- ===== DEPARTMENTS ===== -->
<div class="view" id="view-departments">
<div class="section-head">
<div>
<h2>Departments</h2>
<div class="sub">Organisational units used across work plans and requisitions</div>
</div>
<button class="btn btn-primary" id="new-dept-btn">+ New Department</button>
</div>
<div class="table-wrap">
<table>
<thead><tr><th>Code</th><th>Name</th><th>Abbreviation</th><th></th></tr></thead>
<tbody id="depts-table-body"><tr><td colspan="4" class="loading-row"><span class="spinner spinner-dark"></span></td></tr></tbody>
</table>
</div>
</div>
</div>
</main>
</div>
</div>
<div id="toast-stack"></div>
<!-- ===== MODAL: New / Submit Requisition (styled as the Council's paper Funds Requisition Form) ===== -->
<div class="overlay" id="modal-req">
<div class="modal modal-lg" style="max-width:800px;">
<div class="modal-head"><h3 id="req-modal-title">New Requisition</h3><div class="modal-head-actions"><button type="button" class="modal-max-btn" id="modal-req-max-btn" onclick="toggleModalMaximize('modal-req')" title="Maximize">⛶</button><button class="modal-close" data-close="modal-req">&times;</button></div></div>
<div class="modal-body">
<!-- Paper-form replica: fill this in exactly as you would the printed Funds Requisition Form -->
<div class="req-form-paper" id="req-form-entry" style="border:1px solid var(--line); border-radius:var(--radius-sm); padding:14px 16px 18px;">
<img src="header.jpg" alt="Ntoroko District Local Government — Karugutu Town Council" class="rf-header-img"/>
<div class="req-form-header"><div class="rf-title">Funds Requisition Form</div></div>
<div class="rf-refno">Ref No. <span class="mono" id="req-form-refno-preview">(assigned on save)</span></div>
<table class="req-form-meta-table entry">
<tr>
<td style="width:36%;"><div class="rf-field rf-field-tight"><strong>System User Name:</strong><span class="rf-fill" id="req-form-sysuser"></span></div></td>
<td style="width:32%;"><div class="rf-field rf-field-tight"><strong>Email:</strong><span class="rf-fill" id="req-form-sysemail"></span></div></td>
<td style="width:32%;"><div class="rf-field rf-field-tight"><strong>Role:</strong><span class="rf-fill" id="req-form-sysrole"></span></div></td>
</tr>
<tr>
<td style="width:33.33%;"><div class="rf-field"><strong>Financial Year:</strong><select id="req-form-fy">
<option value="2026/27">2026/27</option>
<option value="2027/28">2027/28</option>
<option value="2028/29">2028/29</option>
<option value="2029/30">2029/30</option>
</select></div></td>
<td style="width:33.33%;"><div class="rf-field"><strong>Quarter:</strong><select id="req-form-quarter">
<option value="Q1">Q1</option>
<option value="Q2">Q2</option>
<option value="Q3">Q3</option>
<option value="Q4">Q4</option>
</select></div></td>
<td style="width:33.34%;"><div class="rf-field rf-field-tight"><strong>Date:</strong><span class="rf-fill" id="req-form-date"></span></div></td>
</tr>
<tr>
<td colspan="3" style="width:100%;"><div class="rf-field"><strong>Department:</strong><select id="req-form-department"></select></div></td>
</tr>
<tr>
<td style="width:33.33%;"><div class="rf-field"><strong>Requisitioner:</strong><input type="text" id="req-form-names" placeholder="Enter your full name"/></div></td>
<td style="width:33.33%;"><div class="rf-field"><strong>Mob. No.:</strong><input type="text" id="req-form-mobile" placeholder="e.g. 0772 123456"/></div></td>
<td style="width:33.34%;"><div class="rf-field"><strong>Position:</strong><input type="text" id="req-form-position" placeholder="e.g. Senior Accountant"/></div></td>
</tr>
<tr>
<td colspan="3">
<div class="rf-field rf-sig-slot">
<strong>Requisitioner Signature:</strong>
<div class="rf-fill" id="req-sig-requester"></div>
<button type="button" class="sig-attach-btn no-print" id="req-sig-requester-btn" onclick="attachSignature('req-sig-requester', this)">🖊 Attach My Signature</button>
</div>
</td>
</tr>
<tr>
<td style="width:33.33%;"><div class="rf-field"><strong>Budget Output Code:</strong>
<div class="rf-bc-search-wrap">
<input type="text" id="req-form-budgetcode-search" autocomplete="off" placeholder="Type the budget output code…"/>
<input type="hidden" id="req-form-budgetcode"/>
<div class="rf-bc-results" id="req-form-budgetcode-results"></div>
</div>
</div></td>
<td style="width:33.33%;"><div class="rf-field rf-field-tight"><strong>Activity Budget Limit:</strong><span class="rf-fill" id="req-form-budgetlimit">—</span></div></td>
<td style="width:33.34%;"><div class="rf-field rf-field-tight"><strong>Activity Budget Balance:</strong><span class="rf-fill" id="req-form-budgetbalance">—</span></div></td>
</tr>
<tr>
<td colspan="3"><div class="rf-field rf-field-desc"><strong>Budget Output Description:</strong><textarea id="req-form-budgetdesc" readonly rows="1" placeholder="—"></textarea></div></td>
</tr>
<tr>
<td colspan="3"><div class="rf-field"><strong>Activity Description(Subject):</strong><input type="text" id="req-subject" placeholder="e.g. Monitoring roads for 3rd Qtr works"/></div></td>
</tr>
</table>
<table class="req-form-table entry">
<thead><tr><th style="width:13%;">Sub Activity<br>S/No.</th><th>Description</th><th style="width:8%;">Units</th><th style="width:8%;">Qty</th><th style="width:11%;">Rate</th><th class="num" style="width:13%;">Amount</th><th class="no-print" style="width:52px;">Line</th></tr></thead>
<tbody id="req-lineitems-body"></tbody>
<tfoot><tr class="rf-grand"><td colspan="5" style="text-align:right;">GRAND TOTAL</td><td class="num">UGX <span id="req-grand-total">0</span></td><td class="no-print"></td></tr></tfoot>
</table>
<div style="display:flex; gap:8px; margin:10px 0 16px; flex-wrap:wrap; justify-content:flex-end;" class="no-print">
<button class="btn btn-ghost" data-close="modal-req"><svg class="btn-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="1.8"/><path d="M9 9L15 15M15 9L9 15" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>Cancel</button>
<button type="button" class="btn btn-ghost" id="req-print-draft"><svg class="btn-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6 9V3H18V9" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><rect x="4" y="9" width="16" height="8" rx="1.5" stroke="currentColor" stroke-width="1.8"/><rect x="7" y="14" width="10" height="6" stroke="currentColor" stroke-width="1.8"/></svg>Print</button>
<button class="btn btn-primary" id="req-route-hod-mid"><svg class="btn-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="1.8"/><path d="M8 12.5L10.5 15L16 9" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><span id="req-route-hod-mid-label">Submit to Head of Department</span></button>
</div>
<div class="req-form-words entry"><strong>Amount in words:</strong> <span id="req-amount-words">—</span></div>
<div class="req-form-signatures preview">
<div><div class="sig-role">Recommended by,</div><div class="sig-line" id="req-sig-hod"></div><button type="button" class="sig-attach-btn no-print" id="req-sig-hod-btn" data-sig-role="hod" onclick="attachSignature('req-sig-hod', this, 'hod')">🖊 Attach Signature</button><div class="sig-name-fill no-print"><input type="text" id="req-sig-hod-name" placeholder="Name of authorizer"/></div><div class="sig-label">Head of Department</div></div>
<div><div class="sig-role">Checked and approved by,</div><div class="sig-line" id="req-sig-treasurer"></div><button type="button" class="sig-attach-btn no-print" id="req-sig-treasurer-btn" data-sig-role="treasurer" onclick="attachSignature('req-sig-treasurer', this, 'treasurer')">🖊 Attach Signature</button><div class="sig-name-fill no-print"><input type="text" id="req-sig-treasurer-name" placeholder="Name of authorizer"/></div><div class="sig-label">Senior Treasurer</div></div>
<div><div class="sig-role">Authorised by</div><div class="sig-line" id="req-sig-clerk"></div><button type="button" class="sig-attach-btn no-print" id="req-sig-clerk-btn" data-sig-role="clerk" onclick="attachSignature('req-sig-clerk', this, 'clerk')">🖊 Attach Signature</button><div class="sig-name-fill no-print"><input type="text" id="req-sig-clerk-name" placeholder="Name of authorizer"/></div><div class="sig-label">Town Clerk</div></div>
</div>
<div class="req-route-stack no-print" style="display:grid; grid-template-columns:repeat(3,1fr); gap:8px; margin:12px 0 0;">
<div style="display:flex; justify-content:center;"><button type="button" class="btn btn-ghost" id="req-route-treasurer" disabled title="Available once the Head of Department has approved this requisition"><svg class="btn-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="1.8"/><path d="M8 12H16M16 12L12.5 8.5M16 12L12.5 15.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Forward to Senior Treasurer</button></div>
<div style="display:flex; justify-content:center;"><button type="button" class="btn btn-ghost" id="req-route-clerk" disabled title="Available once the Senior Treasurer has approved this requisition"><svg class="btn-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="1.8"/><path d="M8 12H16M16 12L12.5 8.5M16 12L12.5 15.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Forward to Town Clerk</button></div>
<div style="display:flex; justify-content:center;"><button type="button" class="btn btn-ghost" id="req-route-auditor" disabled title="Available once the Town Clerk has approved this requisition"><svg class="btn-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="1.8"/><path d="M8 12H16M16 12L12.5 8.5M16 12L12.5 15.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Forward to Internal Auditor</button></div>
</div>
</div>
<!-- ===== Cheque Payment Voucher — same header/council masthead as the Requisition Form above, filled in together with it in the same modal ===== -->
<div class="pv-form" id="pv-form-entry">
<img src="header.jpg" alt="Ntoroko District Local Government — Karugutu Town Council" class="rf-header-img"/>
<div class="req-form-header"><div class="rf-title">Cheque Payment Voucher</div></div>
<div class="rf-refno">Voucher No. <span class="mono" id="pv-form-refno-preview">(assigned on save)</span></div>
<table class="req-form-meta-table entry">
<tr>
<td style="width:50%;"><div class="rf-field"><strong>Department:</strong><input type="text" id="pv-form-department" readonly/></div></td>
<td style="width:50%;"><div class="rf-field"><strong>Cheque No:</strong><input type="text" id="pv-cheque-no" placeholder="e.g. 004521"/></div></td>
</tr>
<tr>
<td><div class="rf-field"><strong>Budget Output Code:</strong><input type="text" id="pv-form-budgetcode" placeholder="e.g. 000123"/></div></td>
<td><div class="rf-field"><strong>Payment Voucher Reference No:</strong><input type="text" id="pv-form-pvref" placeholder="e.g. PV/2026/001"/></div></td>
</tr>
<tr>
<td><div class="rf-field"><strong>Dr. To:</strong><input type="text" id="pv-dr-to" placeholder="Payee name"/></div></td>
<td><div class="rf-field"><strong>Address:</strong><input type="text" id="pv-address" placeholder="Payee address"/></div></td>
</tr>
</table>
<table class="req-form-table entry">
<thead><tr><th style="width:10%;">Date</th><th>Detailed description of service or article</th><th colspan="2" style="width:20%; text-align:center;">Taken on charge expenditure</th><th class="num" style="width:14%;">Amount (Shs)</th></tr>
<tr><th></th><th></th><th style="width:10%;">Ledger Folio</th><th style="width:10%;">Date</th><th class="num"></th></tr>
</thead>
<tbody id="pv-lineitems-body"></tbody>
<tfoot><tr class="rf-grand"><td colspan="4" style="text-align:right;">TOTAL</td><td class="num">UGX <span id="pv-grand-total">0</span></td></tr></tfoot>
</table>
<div class="pv-certify">
<div class="pv-plain-line entry"><strong>Authority</strong><input type="text" id="pv-authority" placeholder="e.g. Approved work plan / Council minute ref."/><strong>Total</strong><input type="text" id="pv-total-shs" readonly/></div>
<div class="pv-plain-line entry"><strong>Approved vote</strong><input type="text" id="pv-approved-vote"/><strong>Account No.</strong><input type="text" id="pv-account-no"/></div>
<div class="pv-plain-line entry"><strong>approved Estimate</strong><input type="text" id="pv-approved-estimate"/><strong>Cheque payment instruction No</strong><input type="text" id="pv-instruction-no"/></div>
<p style="margin-top:10px;"><strong>I HEREBY CERTIFY</strong> that the above amount is correct and was incurred under the authority quoted, that the above services has been duly and properly performed / supplies have been received in good condition: that the payment price charge is in accordance with regulations the terms of contract or agreement which are fair and reasonable and that the above expenditure of Shs (in words) <span id="pv-amount-words">—</span> will not cause an excess over the provision made under the authority quoted on this voucher or under programme/sub-programme shown below:</p>
<p><strong>I FURTHER CERTIFY</strong> that the stores that have been taken on charge, or are expendable, as indicated above.</p>
</div>
<div class="req-form-signatures preview" style="grid-template-columns:repeat(2,1fr);">
<div><div class="sig-role">Signature,</div><div class="sig-line" id="pv-sig-controller"></div><button type="button" class="sig-attach-btn no-print" id="pv-sig-controller-btn" data-sig-role="hod" onclick="attachSignature('pv-sig-controller', this, 'hod')">🖊 Attach Signature</button><div class="sig-name-fill no-print"><input type="text" id="pv-sig-controller-name" placeholder="Name of authorizer"/></div><div class="sig-label">Vote Controller</div></div>
<div><div class="sig-role">Signature,</div><div class="sig-line" id="pv-sig-clerk"></div><button type="button" class="sig-attach-btn no-print" id="pv-sig-clerk-btn" data-sig-role="clerk" onclick="attachSignature('pv-sig-clerk', this, 'clerk')">🖊 Attach Signature</button><div class="sig-name-fill no-print"><input type="text" id="pv-sig-clerk-name" placeholder="Name of authorizer"/></div><div class="sig-label">Town Clerk</div></div>
</div>
<div class="pv-received-line" style="margin-top:14px;">
Received / paid this Day <input type="text" class="pv-day" id="pv-day"/> ................. 20<input type="text" class="pv-day" id="pv-year" style="width:36px;"/> in payment of the above account he Sum of shillings <input type="text" class="pv-words" id="pv-words-line" readonly/> (in words).
</div>
<table class="pv-block-table">
<tr>
<td style="width:34%;">
<strong>Entered In Vote Book</strong>
<div class="help-text" style="margin:0 0 6px;">(To be completed by office of origin)</div>
Date: <input type="text" id="pv-vb-date"/><br/>
<div class="rf-sig-slot" style="margin-top:6px;"><div class="sig-line" id="pv-sig-vb" style="width:100%;"></div><button type="button" class="sig-attach-btn no-print" id="pv-sig-vb-btn" onclick="attachSignature('pv-sig-vb', this)">🖊 Attach Signature</button></div>
Department – Clerk: <input type="text" id="pv-vb-dept"/>
</td>
<td style="width:33%;">
<strong>Verified by</strong>
Date: <input type="text" id="pv-verified-date"/><br/>
<div class="rf-sig-slot" style="margin-top:6px;"><div class="sig-line" id="pv-sig-verified" style="width:100%;"></div><button type="button" class="sig-attach-btn no-print" id="pv-sig-verified-btn" onclick="attachSignature('pv-sig-verified', this)">🖊 Attach Signature</button></div>
</td>
<td style="width:33%;">
<strong>Passed Payment for (HoF)</strong>
Shs: <input type="text" id="pv-passed-shs" readonly/><br/>
Date: <input type="text" id="pv-passed-date"/><br/>
<div class="rf-sig-slot" style="margin-top:6px;"><div class="sig-line" id="pv-sig-passed" style="width:100%;"></div><button type="button" class="sig-attach-btn no-print" id="pv-sig-passed-btn" data-sig-role="treasurer" onclick="attachSignature('pv-sig-passed', this, 'treasurer')">🖊 Attach Signature</button></div>
</td>
</tr>
</table>
<table class="pv-block-table">
<tr>
<td colspan="2">
<div class="rf-sig-slot"><strong>Signature of payee</strong><div class="sig-line" id="pv-sig-payee" style="width:100%;"></div><button type="button" class="sig-attach-btn no-print" id="pv-sig-payee-btn" onclick="attachSignature('pv-sig-payee', this)">🖊 Attach Signature</button></div>
</td>
</tr>
<tr>
<td>
<div class="rf-sig-slot"><strong>Signature of witness to payment</strong><div class="sig-line" id="pv-sig-witness" style="width:100%;"></div><button type="button" class="sig-attach-btn no-print" id="pv-sig-witness-btn" onclick="attachSignature('pv-sig-witness', this)">🖊 Attach Signature</button></div>
</td>
<td>
<div class="rf-sig-slot"><strong>Signature of paying officer (cashier)</strong><div class="sig-line" id="pv-sig-cashier" style="width:100%;"></div><button type="button" class="sig-attach-btn no-print" id="pv-sig-cashier-btn" onclick="attachSignature('pv-sig-cashier', this)">🖊 Attach Signature</button></div>
</td>
</tr>
</table>
<table class="pv-block-table">
<tr>
<td style="width:60%;">
<strong>Inter-departmental Clearance</strong><input type="text" id="pv-inter-clearance"/>
<strong style="margin-top:8px;">Program of Estimate</strong><input type="text" id="pv-program-estimate"/>
<strong style="margin-top:8px;">Sub Program</strong><input type="text" id="pv-sub-program"/>
<strong style="margin-top:8px;">Item</strong><input type="text" id="pv-item"/>
</td>
<td style="width:40%; text-align:right; vertical-align:bottom;">
<strong>Total Shs</strong><input type="text" id="pv-total-shs-2" readonly style="text-align:right; font-weight:700; font-size:15px;"/>
</td>
</tr>
</table>
</div>
</div>
<div class="modal-foot foot-nowrap">
<button class="btn btn-ghost" data-close="modal-req"><svg class="btn-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="1.8"/><path d="M9 9L15 15M15 9L9 15" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>Cancel</button>
<button class="btn btn-primary" id="req-route-hod"><svg class="btn-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="1.8"/><path d="M8 12.5L10.5 15L16 9" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><span id="req-route-hod-label">Submit to Head of Department</span></button>
</div>
</div>
</div>
<!-- ===== MODAL: Requisition Detail ===== -->
<div class="overlay" id="modal-req-detail">
<div class="modal modal-lg">
<div class="modal-head"><h3 id="rd-title">Requisition</h3><div class="modal-head-actions"><button type="button" class="modal-max-btn" id="modal-req-detail-max-btn" onclick="toggleModalMaximize('modal-req-detail')" title="Maximize">⛶</button><button class="modal-close" data-close="modal-req-detail">&times;</button></div></div>
<div class="modal-body" id="rd-body"></div>
<div class="modal-foot" id="rd-foot"></div>
</div>
</div>
<!-- ===== MODAL: Printable Requisition Form (Karugutu Town Council paper layout) ===== -->
<div class="overlay" id="modal-print-form">
<div class="modal modal-lg" id="print-form-container" style="max-width:760px;">
<div class="modal-head no-print"><h3>Requisition Form</h3><button class="modal-close" data-close="modal-print-form">&times;</button></div>
<div class="modal-body" id="pf-body"></div>
<div class="modal-foot no-print">
<button class="btn btn-ghost" data-close="modal-print-form">Close</button>
<button class="btn btn-primary" onclick="window.print()">Print</button>
</div>
</div>
</div>
<!-- ===== MODAL: My Settings (profile + signature) ===== -->
<div class="overlay" id="modal-settings">
<div class="modal">
<div class="modal-head"><h3>My Settings</h3><button class="modal-close" data-close="modal-settings">&times;</button></div>
<div class="modal-body">
<div class="detail-grid" style="margin-bottom:6px;">
<div><div class="detail-label">Name</div><div class="detail-value" id="set-name">—</div></div>
<div><div class="detail-label">Role</div><div class="detail-value" id="set-role">—</div></div>
<div><div class="detail-label">Email</div><div class="detail-value" id="set-email">—</div></div>
<div><div class="detail-label">Department</div><div class="detail-value" id="set-dept">—</div></div>
</div>
</div>
<div class="modal-foot">
<button class="btn btn-ghost" data-close="modal-settings">Close</button>
</div>
</div>
</div>
<!-- ===== MODAL: New User ===== -->
<div class="overlay" id="modal-user">
<div class="modal">
<div class="modal-head"><h3 id="u-modal-title">New User</h3><button class="modal-close" data-close="modal-user">&times;</button></div>
<div class="modal-body">
<div class="form-grid">
<div class="field span2"><label>Full Name</label><input type="text" id="u-name"/></div>
<div class="field span2"><label>Email</label><input type="email" id="u-email"/></div>
<div class="field"><label id="u-password-label">Temporary Password</label><input type="text" id="u-password"/></div>
<div class="field"><label>Position</label><input type="text" id="u-position" placeholder="e.g. Senior Accountant"/></div>
<div class="field"><label>Telephone</label><input type="text" id="u-telephone" placeholder="e.g. 0700 000 000"/></div>
<div class="field"><label>Role</label>
<select id="u-role">
<option value="staff">Requisitioner</option>
<option value="hod">First Level Approver</option>
<option value="treasurer">Budget Controller</option>
<option value="clerk">Accounting Officer</option>
<option value="admin">Local System Administrator</option>
</select>
</div>
<div class="field span2"><label id="u-department-label">Department</label><select id="u-department"></select><div class="help-text" id="u-department-hint" style="display:none; margin-top:4px;">Required for Head of Department accounts — a Head of Department without a Department assigned will not see any requisitions awaiting their approval.</div></div>
</div>
<div class="divider"></div>
<div class="field-section">
<span class="kicker">Signature</span>
<div class="help-text" style="margin-top:4px;">Upload an image of this user's signature (PNG or JPG). It's attached automatically wherever their name appears on a printed Requisition Form — as requester, or when they approve, recommend or authorise at their stage.</div>
<div style="margin-top:14px; display:flex; align-items:center; gap:16px; flex-wrap:wrap;">
<div class="sig-preview-box" id="u-sig-preview-box">
<span id="u-sig-preview-empty" style="font-size:11px; color:var(--ink-500); padding:0 10px; text-align:center;">No signature uploaded</span>
<img id="u-sig-preview-img" style="display:none;" />
</div>
<div style="display:flex; flex-direction:column; gap:8px;">
<input type="file" id="u-sig-file-input" accept=".png,.jpg,.jpeg" style="display:none;" />
<button type="button" class="btn btn-primary" id="u-sig-upload-btn">Upload Signature</button>
<button type="button" class="btn btn-ghost" id="u-sig-remove-btn" style="display:none;">Remove Signature</button>
</div>
</div>
<div class="login-error" id="u-sig-error" style="margin-top:10px;"></div>
</div>
</div>
<div class="modal-foot">
<button class="btn btn-ghost" data-close="modal-user">Cancel</button>
<button class="btn btn-primary" id="u-create-btn">Create User</button>
</div>
</div>
</div>
<!-- ===== MODAL: New Department ===== -->
<div class="overlay" id="modal-dept">
<div class="modal">
<div class="modal-head"><h3 id="d-modal-title">New Department</h3><button class="modal-close" data-close="modal-dept">&times;</button></div>
<div class="modal-body">
<div class="field"><label>Department Name</label><input type="text" id="d-name"/></div>
<div class="field"><label>Department Code</label><input type="text" id="d-code" placeholder="e.g. FIN"/></div>
<div class="field"><label>Abbreviation</label><input type="text" id="d-abbr" placeholder="e.g. AMS"/><div class="help-text" style="margin-top:4px;">Used on the Departments page and in generated reference numbers. Leave blank to auto-generate from the Department Name.</div></div>
</div>
<div class="modal-foot">
<button class="btn btn-ghost" data-close="modal-dept">Cancel</button>
<button class="btn btn-primary" id="d-create-btn">Create Department</button>
</div>
</div>
</div>
<!-- ===== MODAL: New / Edit Budget Estimates Data Entry Form ===== -->
<div class="overlay" id="modal-bc">
<div class="modal modal-lg">
<div class="modal-head"><h3 id="bc-modal-title">New Budget Estimates Data Entry Form</h3><button class="modal-close" data-close="modal-bc">&times;</button></div>
<div class="modal-body">
<div class="field-section">
<span class="kicker">Placement</span>
<div class="form-grid" style="margin-top:8px;">
<div class="field"><label>Work Plan</label><select id="bc-workplan"></select></div>
<div class="field"><label>Department</label><select id="bc-department"></select></div>
<div class="field span2"><label>Service Area</label><input type="text" id="bc-service-area" placeholder="e.g. Health, Education, Roads"/></div>
</div>
</div>
<div class="divider"></div>
<div class="field-section">
<span class="kicker">Output Details</span>
<div class="form-grid" style="margin-top:8px;">
<div class="field"><label>Budget Output Code</label><input type="text" id="bc-code" placeholder="e.g. 10103"/></div>
<div class="field"><label>Unit of Measure</label><input type="text" id="bc-unit" placeholder="Number / %"/></div>
<div class="field span2"><label>Budget Output Description</label><input type="text" id="bc-desc"/></div>
<div class="field"><label>Programme</label><input type="text" id="bc-programme"/></div>
<div class="field"><label>Sub-Programme</label><input type="text" id="bc-subprogramme"/></div>
<div class="field span2"><label>PIAP Output Description</label><input type="text" id="bc-piap-desc" placeholder="Programme Implementation Action Plan output description"/></div>
<div class="field span2"><label>PIAP Output Indicator</label><input type="text" id="bc-piap-indicator" placeholder="Programme Implementation Action Plan indicator"/></div>
</div>
</div>
<div class="divider"></div>
<div class="field-section">
<span class="kicker">Targets, Quarterly Plan &amp; Funding</span>
<div class="form-grid" style="margin-top:8px;">
<div class="field"><label>Baseline Value</label><input type="number" id="bc-baseline" value="0"/></div>
<div class="field"><label>Planned Target</label><input type="number" id="bc-target" value="0"/></div>
<div class="field span2"><label>Baseline Note <span style="font-weight:400;color:var(--ink-500);">(optional — narrative baseline, e.g. "25% of Council area mapped for vectors")</span></label><input type="text" id="bc-baseline-note" placeholder="Free-text baseline detail, if any"/></div>
<div class="field span2"><label>Target Note <span style="font-weight:400;color:var(--ink-500);">(optional — narrative target, e.g. "Conduct 4 quarterly vector surveillance exercises")</span></label><input type="text" id="bc-target-note" placeholder="Free-text target detail, if any"/></div>
<div class="field span2"><label>Actual Output</label><input type="text" id="bc-actual" placeholder="Actual output achieved so far"/></div>
<div class="field"><label>Q1 (UGX)</label><input type="number" id="bc-q1" value="0"/></div>
<div class="field"><label>Q2 (UGX)</label><input type="number" id="bc-q2" value="0"/></div>
<div class="field"><label>Q3 (UGX)</label><input type="number" id="bc-q3" value="0"/></div>
<div class="field"><label>Q4 (UGX)</label><input type="number" id="bc-q4" value="0"/></div>
<div class="field"><label>Total Budget (UGX)</label><input type="text" id="bc-total" value="0" readonly style="background:var(--paper); font-family:var(--font-mono);"/></div>
<div class="field"><label>Funding Source</label><input type="text" id="bc-funding" value="Local Revenue"/></div>
<div class="field span2"><label>Responsible Party</label><input type="text" id="bc-responsible" placeholder="e.g. Head of Department, Officer name"/></div>
</div>
<div class="help-text">Total Budget is the sum of Q1–Q4 and is calculated automatically.</div>
</div>
</div>
<div class="modal-foot">
<button class="btn btn-ghost" data-close="modal-bc">Cancel</button>
<button class="btn btn-primary" id="bc-create-btn">Create Budget Estimate</button>
</div>
</div>
</div>
<!-- ===== MODAL: New / Edit Work Plan ===== -->
<div class="overlay" id="modal-wp">
<div class="modal modal-lg">
<div class="modal-head"><h3 id="wpn-modal-title">New Work Plan</h3><button class="modal-close" data-close="modal-wp">&times;</button></div>
<div class="modal-body">
<div class="form-grid">
<div class="field"><label>Financial Year</label><input type="text" id="wpn-fy" placeholder="e.g. 2026/27"/></div>
<div class="field"><label>Title</label><input type="text" id="wpn-title" placeholder="e.g. Annual Work Plan and Budget"/></div>
</div>
<div class="help-text">Once created, this work plan becomes available for budget codes to be attached to.</div>
<div class="divider"></div>
<span class="kicker">Table Headings For This Work Plan</span>
<div class="help-text" style="margin-top:2px; margin-bottom:10px;">These are the headings shown above the four Work Plan &amp; Budget tables. Leave any of them blank to fall back to a default built from the financial year above.</div>
<div class="field"><label>Revenue Summary Table Heading</label><input type="text" id="wpn-title-revenue-summary" placeholder="e.g. APPROVED SUMMARY OF THE COUNCIL BUDGET FRAMEWORK PAPER AND PRELIMINARY REVENUE ESTIMATES FOR FY 2026/2027"/></div>
<div class="field"><label>Departmental Summary Table Heading</label><input type="text" id="wpn-title-dept-summary" placeholder="e.g. APPROVED DEPARTMENTAL SUMMARY OF THE COUNCIL ANNUAL WORK PLAN AND EXPENDITURE ESTIMATES FOR FY 2026/2027"/></div>
<div class="field"><label>Revenue Estimates Table Heading</label><input type="text" id="wpn-title-revenue-detail" placeholder="e.g. APPROVED COUNCIL BUDGET FRAMEWORK PAPER AND PRELIMINARY REVENUE ESTIMATES FOR FY 2026/2027"/></div>
<div class="field"><label>Annual Work Plan Table Heading</label><input type="text" id="wpn-title-main-table" placeholder="e.g. APPROVED COUNCIL ANNUAL WORK PLAN AND EXPENDITURE ESTIMATES FOR FY 2026/2027"/></div>
</div>
<div class="modal-foot">
<button class="btn btn-ghost" data-close="modal-wp">Cancel</button>
<button class="btn btn-primary" id="wpn-create-btn">Create Work Plan</button>
</div>
</div>
</div>
<!-- ===== MODAL: New / Edit Revenue Source (category + sub rows) ===== -->
<div class="overlay" id="modal-rev">
<div class="modal modal-lg">
<div class="modal-head"><h3 id="rev-modal-title">New Revenue Source</h3><button class="modal-close" data-close="modal-rev">&times;</button></div>
<div class="modal-body">
<div class="field"><label>Work Plan</label><select id="rev-workplan"></select></div>
<div class="form-grid">
<div class="field">
<label>PBS Fund Code</label>
<select id="rev-fund-code"></select>
<input type="text" id="rev-fund-code-custom" class="rev-custom-field" placeholder="e.g. 001" />
</div>
<div class="field">
<label>Revenue Source</label>
<select id="rev-source-name"></select>
<input type="text" id="rev-source-name-custom" class="rev-custom-field" placeholder="e.g. Central Government Transfers (GoU)" />
</div>
</div>
<div class="field">
<label>Functional Definition Title</label>
<select id="rev-functional-def"></select>
<textarea id="rev-functional-def-custom" class="rev-custom-field" rows="3" placeholder="e.g. Regular structural wage, non-wage recurrent and capital grants&#10;Each new line becomes its own point on the printed table"></textarea>
</div>
<div class="field-section">
<span class="kicker">Sub Rows — Revenue Items</span>
<div class="table-wrap" style="margin-top:8px;">
<table>
<thead>
<tr><th class="wrap">Revenue Item (Functional Definition)</th><th>Approved Estimate (UGX)</th><th></th></tr>
</thead>
<tbody id="rev-items-body"></tbody>
</table>
</div>
<div style="display:flex; gap:8px; margin-top:10px; flex-wrap:wrap;">
<button type="button" class="btn btn-ghost" id="rev-add-item-btn">+ Add Sub Row</button>
</div>
<div class="help-text">Each sub row is one revenue item under the functional definition title above. The Category Total — and therefore the Approved Budget Amount shown in the Summary of Sources of Revenue — is obtained automatically as the sum of these sub rows.</div>
</div>
<div class="field"><label>Approved Budget Amount (UGX) — used only when there are no sub rows</label><input type="number" id="rev-amount" value="0" /></div>
</div>
<div class="modal-foot">
<button class="btn btn-ghost" data-close="modal-rev">Cancel</button>
<button class="btn btn-primary" id="rev-create-btn">Create Revenue Source</button>
</div>
</div>
</div>
<!-- ===== MODAL: Single-page Document Viewer (Auditor review) ===== -->
<div class="overlay" id="modal-doc-view">
<div class="modal modal-lg" style="max-width:940px;">
<div class="modal-head"><h3 id="dv-title">Accountability Documents</h3><button class="modal-close" data-close="modal-doc-view">&times;</button></div>
<div class="modal-body" id="dv-body" style="max-height:70vh;"></div>
<div class="modal-foot" id="dv-foot"></div>
</div>
</div>
<!-- ===== MODAL: Upload document ===== -->
<div class="overlay" id="modal-upload">
<div class="modal">
<div class="modal-head"><h3>Upload Accountability Document</h3><button class="modal-close" data-close="modal-upload">&times;</button></div>
<div class="modal-body">
<div class="field"><label>Document Type</label>
<select id="up-type">
<option value="receipt">Receipt</option>
<option value="attendance">Attendance Sheet</option>
<option value="voucher">Payment Voucher</option>
<option value="supporting">Supporting Document</option>
<option value="other">Other</option>
</select>
</div>
<div class="field"><label>File (PDF, DOCX, JPG, PNG)</label><input type="file" id="up-file" accept=".pdf,.docx,.jpg,.jpeg,.png"/></div>
</div>
<div class="modal-foot">
<button class="btn btn-ghost" data-close="modal-upload">Cancel</button>
<button class="btn btn-primary" id="up-submit-btn">Upload</button>
</div>
</div>
</div>
<script>
/* ==========================================================================
KTC-IPFMS — Frontend application logic (vanilla JS, no build step)
========================================================================== */
// ---- Configuration --------------------------------------------------------
const KTC_BACKEND_URL = 'https://ktc-backend-5yz9.onrender.com';
const API_BASE = localStorage.getItem('ktc_api_base') || KTC_BACKEND_URL;
let STATE = {
token: localStorage.getItem('ktc_token') || null,
role: localStorage.getItem('ktc_role') || null,
name: localStorage.getItem('ktc_name') || null,
userId: localStorage.getItem('ktc_user_id') || null,
email: null,
position: null,
departments: [],
workplans: [],
budgetCodes: [],
revenueSources: [],
revItems: [],
currentReqId: null,
editingBudgetCodeId: null,
editingWorkPlanId: null,
editingDepartmentId: null,
editingUserId: null,
editingRequisitionId: null,
editingRevenueSourceId: null,
reqLineItems: [],
reqBudgetCodesForDept: [],
signatureUrl: null,
};

const REVENUE_SUMMARY_CATEGORIES = [
  {
    key: 'gou',
    pbs_fund_code: '001',
    source_of_financing_name: 'Central Government Transfers (GoU)',
    functional_definition: 'Regular structural wage, non-wage recurrent, and capital grants.',
    match: (r) => {
      const code = String(r.pbs_fund_code || '').trim();
      const name = String(r.source_of_financing_name || '').toLowerCase();
      return code === '001' || name.includes('central government') || name.includes('gou') || name.includes('transfers');
    }
  },
  {
    key: 'lr',
    pbs_fund_code: '002',
    source_of_financing_name: 'Locally Raised Revenues (LR)',
    functional_definition: 'Internally collected fees, levies, licenses, and operational fines.',
    match: (r) => {
      const code = String(r.pbs_fund_code || '').trim();
      const name = String(r.source_of_financing_name || '').toLowerCase();
      return code === '002' || name.includes('locally raised') || name.includes('local revenue') || /\blr\b/.test(name);
    }
  },
  {
    key: 'mdp',
    pbs_fund_code: '400',
    source_of_financing_name: 'Multi-lateral Development Partners',
    functional_definition: 'International institutional donor funding (e.g., World Bank, UNICEF).',
    match: (r) => {
      const code = String(r.pbs_fund_code || '').trim();
      const name = String(r.source_of_financing_name || '').toLowerCase();
      return code === '400' || name.includes('multi-lateral') || name.includes('multilateral') || name.includes('development partner') || name.includes('donor');
    }
  },
];

function categorizeRevenueSource(r) {
  for (const cat of REVENUE_SUMMARY_CATEGORIES) {
    if (cat.match(r)) return cat.key;
  }
  return null; // entries that don't match any of the three fixed categories are excluded from the summary totals
}
// ---- Revenue Source modal: PBS Fund Code / Revenue Source / Functional Definition
// are drawn from the fixed REVENUE_SUMMARY_CATEGORIES constants as dropdowns (plus
// an "Other" option for anything outside the three standard categories).
const REV_CUSTOM_VALUE = '__custom__';
const REV_FIELD_MAP = {
  'rev-fund-code': { customId: 'rev-fund-code-custom', catField: 'pbs_fund_code' },
  'rev-source-name': { customId: 'rev-source-name-custom', catField: 'source_of_financing_name' },
  'rev-functional-def': { customId: 'rev-functional-def-custom', catField: 'functional_definition' },
};
function populateRevDropdowns() {
  for (const [selectId, cfg] of Object.entries(REV_FIELD_MAP)) {
    const optsHtml = REVENUE_SUMMARY_CATEGORIES.map(c =>
      `<option value="${c.key}">${escapeHtml(c.pbs_fund_code)} — ${escapeHtml(c[cfg.catField])}</option>`
    ).join('');
    document.getElementById(selectId).innerHTML =
      `<option value="">— Select —</option>${optsHtml}<option value="${REV_CUSTOM_VALUE}">Other (type manually)</option>`;
  }
}
function setRevCustomVisible(selectId, visible) {
  const el = document.getElementById(REV_FIELD_MAP[selectId].customId);
  el.style.display = visible ? '' : 'none';
  if (!visible) el.value = '';
}
function onRevCategorySelect(changedId) {
  const val = document.getElementById(changedId).value;
  if (val === REV_CUSTOM_VALUE) { setRevCustomVisible(changedId, true); return; }
  setRevCustomVisible(changedId, false);
  if (!val) return;
  // The three fields describe one fixed category — keep them in sync.
  for (const otherId of Object.keys(REV_FIELD_MAP)) {
    if (otherId === changedId) continue;
    document.getElementById(otherId).value = val;
    setRevCustomVisible(otherId, false);
  }
}
function getRevFieldValue(selectId) {
  const cfg = REV_FIELD_MAP[selectId];
  const val = document.getElementById(selectId).value;
  if (val === REV_CUSTOM_VALUE) return document.getElementById(cfg.customId).value.trim();
  if (!val) return '';
  const cat = REVENUE_SUMMARY_CATEGORIES.find(c => c.key === val);
  return cat ? cat[cfg.catField] : '';
}
// ---- Fetch helper -----------------------------------------------------------
// fetchWithTimeout wraps the raw network call with an AbortController-based
// timeout, since a hung request (e.g. a backend host that's slow to wake up)
// would otherwise leave the caller waiting indefinitely instead of failing
// in a way the retry logic below can act on.
async function fetchWithTimeout(url, opts, timeoutMs) {
const controller = new AbortController();
const timer = setTimeout(() => controller.abort(), timeoutMs);
try {
return await fetch(url, { ...opts, signal: controller.signal });
} finally {
clearTimeout(timer);
}
}
async function api(path, opts = {}) {
const headers = opts.headers || {};
if (!(opts.body instanceof FormData)) headers['Content-Type'] = 'application/json';
if (STATE.token) headers['Authorization'] = 'Bearer ' + STATE.token;
// Network-level failures (DNS/connection errors, a cold backend instance
// timing out, a dropped connection, etc.) surface here as a rejected
// promise rather than an HTTP error response — retry once after a short
// pause before giving up, since these are frequently transient (e.g. a
// free-tier host waking from sleep on the very first request).
let res;
try {
res = await fetchWithTimeout(API_BASE + path, { ...opts, headers }, 20000);
} catch (networkErr) {
try {
await new Promise(r => setTimeout(r, 1500));
res = await fetchWithTimeout(API_BASE + path, { ...opts, headers }, 30000);
} catch (retryErr) {
throw new Error('Could not reach the server. Please check your connection and try again in a moment.');
}
}
if (res.status === 401) {
logout();
throw new Error('Session expired. Please sign in again.');
}
let data = null;
try { data = await res.json(); } catch (e) { /* no body */ }
if (!res.ok) {
const msg = (data && data.detail) ? (typeof data.detail === 'string' ? data.detail : JSON.stringify(data.detail)) : 'Something went wrong';
throw new Error(msg);
}
return data;
}
// ---- Toasts -----------------------------------------------------------------
function toast(message, type = 'info') {
const stack = document.getElementById('toast-stack');
const el = document.createElement('div');
el.className = 'toast ' + type;
el.textContent = message;
stack.appendChild(el);
setTimeout(() => { el.style.opacity = '0'; el.style.transition = 'opacity .3s'; setTimeout(() => el.remove(), 300); }, 4200);
}
function money(n) {
if (typeof n === 'string') {
const cleaned = n.replace(/[,\s\u00A0]/g, '').replace(/UGX|Ugx|ugx/g, '');
n = cleaned === '' ? 0 : Number(cleaned);
} else {
n = Number(n || 0);
}
if (!Number.isFinite(n)) n = 0;
return n.toLocaleString('en-UG', { maximumFractionDigits: 0 });
}
function parseNumericLoose(v) {
if (v === null || v === undefined) return null;
if (typeof v === 'number') return Number.isFinite(v) ? v : null;
let s = String(v).replace(/[,\s\u00A0]/g, '').replace(/UGX|Ugx|ugx|%/g, '').trim();
if (s === '') return null;
const n = Number(s);
return Number.isFinite(n) ? n : null;
}
function fmtDate(iso) {
if (!iso) return '—';
const d = new Date(iso);
return d.toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' }) + ' • ' +
d.toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' });
}
// Uganda's financial year runs 1 Jul – 30 Jun, split into calendar quarters
// Q1 Jul-Sep, Q2 Oct-Dec, Q3 Jan-Mar, Q4 Apr-Jun. These are only used to
// pre-select a sensible default on the Financial Year / Quarter fields —
// the requisitioner can always change either before saving.
function currentFinancialYearGuess() {
const now = new Date();
const y = now.getFullYear();
const startYear = now.getMonth() >= 6 ? y : y - 1; // getMonth() 6 = July
return `${startYear}/${String((startYear + 1) % 100).padStart(2, '0')}`;
}
function currentQuarterGuess() {
const m = new Date().getMonth(); // 0-11
if (m >= 6 && m <= 8) return 'Q1';
if (m >= 9 && m <= 11) return 'Q2';
if (m >= 0 && m <= 2) return 'Q3';
return 'Q4';
}
function initials(name) {
if (!name) return '?';
return name.split(' ').filter(Boolean).slice(0,2).map(w => w[0]).join('').toUpperCase();
}
function statusLabel(s) { return (s || '').replace(/_/g, ' '); }
// Role labels used ONLY in the admin "New/Edit User" modal and the Users
// table — a display-only relabeling for that screen. Every other place in
// the system (login screen, sidebar, requisition forms, notifications,
// approval history, etc.) still uses the original role names via
// statusLabel(), and the underlying role codes stored in the database are
// unchanged.
const ADMIN_USER_ROLE_LABELS = {
staff: 'Requisitioner',
hod: 'First Level Approver',
treasurer: 'Budget Controller',
clerk: 'Accounting Officer',
admin: 'Local System Administrator',
};
function adminRoleLabel(role) { return ADMIN_USER_ROLE_LABELS[role] || statusLabel(role); }
function escapeHtml(s) { const d = document.createElement('div'); d.textContent = s || ''; return d.innerHTML; }
// Strict separation of concern: shows a department using its NAME ONLY.
// The PBS department code is a distinct identifier and is intentionally
// never appended here — this is used for the Departments page's own
// Department column, user records, requisitions, dept-output charts, etc.
function deptLabel(d) { if (!d) return null; return d.name; }
// Shows a department as "<code>: <name>" (e.g. "090: Community Based
// Services"). Used for the Annual Work Plan & Budget Estimates table's
// Department column (via the backend-supplied `department_code_and_name`
// field on each budget code — see renderBudgetCodes()), the Department
// Budget Summary table (renderDeptSummaryTable()), and every dropdown that
// lists departments (Work Plan filter, Budget Code form, Requisition form,
// User form — see loadDepartments()). NOT used for the Departments page's
// own Department column, which shows name alone via deptLabel() above.
function deptLabelWithCode(d) { if (!d) return null; return d.code ? `${d.code}: ${d.name}` : d.name; }
// ---- Multi-point text formatting (e.g. Functional Definition cells) --------
// Renders a block of text as one line per "point" instead of one continuous
// run-on line. If the source text already contains real line breaks, each
// line becomes its own point. Otherwise, if it looks like it packs several
// numbered/lettered/bulleted points onto a single line (e.g. "1. ... 2. ..."
// or "(a) ... (b) ..." or "• ... • ..."), it is split at those markers so
// each point still starts on a new line.
function formatMultilinePoints(text) {
if (text === null || text === undefined || String(text).trim() === '') return '—';
let normalized = String(text).replace(/\r\n/g, '\n').replace(/\r/g, '\n');
let points = normalized.split('\n').map(s => s.trim()).filter(Boolean);
if (points.length <= 1) {
const candidate = normalized.trim();
const parts = candidate
.split(/(?=\d+\s*[.)]\s+)|(?=\([a-zA-Z0-9]+\)\s+)|(?=[•▪‣•]\s+)/g)
.map(s => s.trim())
.filter(Boolean);
points = parts.length > 1 ? parts : [candidate];
}
return points.map(p => escapeHtml(p)).join('<br>');
}
// ---- Number-to-words (for the "Amount in words" line on the printed form) --
function numberToWords(n) {
n = Math.floor(Math.abs(Number(n) || 0));
const ones = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten',
'Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen'];
const tens = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety'];
function chunk(num) {
let str = '';
if (num >= 100) { str += ones[Math.floor(num / 100)] + ' Hundred '; num %= 100; }
if (num >= 20) { str += tens[Math.floor(num / 10)] + ' '; num %= 10; }
if (num > 0) { str += ones[num] + ' '; }
return str.trim();
}
if (n === 0) return 'Zero';
const units = [{ v: 1000000000, l: 'Billion' }, { v: 1000000, l: 'Million' }, { v: 1000, l: 'Thousand' }, { v: 1, l: '' }];
let result = '';
let remainder = n;
for (const u of units) {
if (remainder >= u.v) {
const count = Math.floor(remainder / u.v);
result += chunk(count) + (u.l ? ' ' + u.l + ' ' : ' ');
remainder %= u.v;
}
}
return result.trim().replace(/\s+/g, ' ');
}
function numberToWordsUGX(amount) {
const rounded = Math.round(Number(amount) || 0);
if (rounded === 0) return 'Zero shillings only';
return `${numberToWords(rounded)} Shillings Only`;
}
// ---- Auth ---------------------------------------------------------------------
document.getElementById('login-password-toggle').addEventListener('click', () => {
const input = document.getElementById('login-password');
const btn = document.getElementById('login-password-toggle');
const showing = input.type === 'text';
input.type = showing ? 'password' : 'text';
btn.setAttribute('aria-label', showing ? 'Show password' : 'Hide password');
btn.title = showing ? 'Show password' : 'Hide password';
btn.innerHTML = showing
? '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7-11-7-11-7z"/><circle cx="12" cy="12" r="3"/></svg>'
: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M17.94 17.94A10.94 10.94 0 0 1 12 19c-7 0-11-7-11-7a19.4 19.4 0 0 1 4.22-5.06M9.9 4.24A10.4 10.4 0 0 1 12 4c7 0 11 7 11 7a19.5 19.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/><path d="M1 1l22 22"/></svg>';
});
document.getElementById('login-form').addEventListener('submit', async (e) => {
e.preventDefault();
const role = document.getElementById('login-role').value;
const email = document.getElementById('login-email').value.trim();
const password = document.getElementById('login-password').value;
const errEl = document.getElementById('login-error');
const btn = document.getElementById('login-btn');
errEl.style.display = 'none';
if (!role) {
errEl.textContent = 'Please select the role you are signing in as.';
errEl.style.display = 'block';
return;
}
btn.disabled = true; btn.innerHTML = '<span class="spinner"></span> Signing in…';
try {
const data = await api('/api/auth/login', { method: 'POST', body: JSON.stringify({ email, password, role }) });
STATE.token = data.access_token; STATE.role = data.role; STATE.name = data.full_name; STATE.userId = data.user_id;
localStorage.setItem('ktc_token', STATE.token);
localStorage.setItem('ktc_role', STATE.role);
localStorage.setItem('ktc_name', STATE.name);
localStorage.setItem('ktc_user_id', STATE.userId);
enterApp();
} catch (err) {
errEl.textContent = err.message || 'Unable to sign in. Please check your credentials.';
errEl.style.display = 'block';
} finally {
btn.disabled = false; btn.innerHTML = 'Sign in to your account';
}
});
function logout() {
STATE = { ...STATE, token: null, role: null, name: null, userId: null, signatureUrl: null, email: null, position: null };
localStorage.removeItem('ktc_token'); localStorage.removeItem('ktc_role');
localStorage.removeItem('ktc_name'); localStorage.removeItem('ktc_user_id');
document.getElementById('app-screen').style.display = 'none';
document.getElementById('login-screen').style.display = 'flex';
stopIdleTimer();
}
document.getElementById('logout-btn').addEventListener('click', logout);
// ---- Inactivity auto-logout (10 minutes) ----------------------------------
// The session token itself is now long-lived — signing a user out is
// handled here, purely based on real inactivity, so an actively-working
// user is never logged out mid-task the way a fixed-lifetime token used to.
const IDLE_TIMEOUT_MS = 10 * 60 * 1000;
let idleTimer = null;
function resetIdleTimer() {
if (!STATE.token) return;
clearTimeout(idleTimer);
idleTimer = setTimeout(() => {
if (STATE.token) {
logout();
toast('You have been signed out after 10 minutes of inactivity', 'error');
}
}, IDLE_TIMEOUT_MS);
}
function stopIdleTimer() {
clearTimeout(idleTimer);
idleTimer = null;
}
['mousedown', 'mousemove', 'keydown', 'wheel', 'scroll', 'touchstart', 'click'].forEach(evt => {
document.addEventListener(evt, () => { if (STATE.token) resetIdleTimer(); }, { passive: true });
});
async function enterApp() {
document.getElementById('login-screen').style.display = 'none';
document.getElementById('app-screen').style.display = 'block';
document.getElementById('sb-name').textContent = STATE.name;
document.getElementById('sb-role').textContent = statusLabel(STATE.role);
document.getElementById('sb-avatar').textContent = initials(STATE.name);
document.getElementById('admin-nav-group').style.display = (STATE.role === 'admin') ? 'block' : 'none';
applyRoleVisibility();
await loadDepartments();
await loadWorkplans();
switchView('dashboard');
refreshNotifications();
setInterval(refreshNotifications, 30000);
api('/api/auth/me').then(me => { STATE.signatureUrl = me.signature_url || null; STATE.departmentId = me.department_id || null; STATE.email = me.email || null; STATE.position = me.position || null; STATE.telephone = me.telephone || null; }).catch(() => {});
resetIdleTimer();
}
function applyRoleVisibility() {
const navMap = {
approvals: ['hod', 'treasurer', 'clerk', 'admin'],
accountability: ['auditor', 'admin'],
reports: ['admin', 'auditor', 'clerk', 'treasurer', 'hod', 'staff'],
};
document.querySelectorAll('.nav-item[data-view]').forEach(btn => {
const v = btn.dataset.view;
if (navMap[v] && !navMap[v].includes(STATE.role)) btn.style.display = 'none';
else btn.style.display = 'flex';
});
document.getElementById('wp-new-btn').style.display = (STATE.role === 'admin') ? 'inline-flex' : 'none';
document.getElementById('wp-new-workplan-btn').style.display = (STATE.role === 'admin') ? 'inline-flex' : 'none';
document.getElementById('wp-edit-workplan-btn').style.display = (STATE.role === 'admin') ? 'inline-flex' : 'none';
document.getElementById('wp-import-btn').style.display = (STATE.role === 'admin') ? 'inline-flex' : 'none';
document.getElementById('wp-new-revenue-btn').style.display = (STATE.role === 'admin') ? 'inline-flex' : 'none';
document.getElementById('wp-import-revenue-btn').style.display = (STATE.role === 'admin') ? 'inline-flex' : 'none';
document.getElementById('new-req-btn').style.display = (['staff','hod','admin'].includes(STATE.role)) ? 'inline-flex' : 'none';
document.getElementById('qa-new-req').style.display = (['staff','hod','admin'].includes(STATE.role)) ? 'block' : 'none';
document.getElementById('wp-revenue-clear-btn').style.display = (STATE.role === 'admin') ? 'inline-flex' : 'none';
document.getElementById('wp-clear-btn').style.display = (STATE.role === 'admin') ? 'inline-flex' : 'none';
}
// ---- Navigation -----------------------------------------------------------
const VIEW_TITLES = {
dashboard: ['Dashboard', 'Overview of financial activity'],
workplan: ['Programme-Based Budgeting System (PBS) and Integrated Financial Management System (IFMS)', ''],
requisitions: ['Requisitions', 'Requisition tracking and submission'],
approvals: ['Approvals', 'Three-stage approval workflow'],
accountability: ['Accountability', 'Post-approval documentation and verification'],
reports: ['Audit & Reports', 'System-wide activity and audit trail'],
users: ['Users & Roles', 'Account and access management'],
departments: ['Departments', 'Organisational structure'],
};
function switchView(view) {
document.querySelectorAll('.nav-item[data-view]').forEach(b => b.classList.toggle('active', b.dataset.view === view));
document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
document.getElementById('view-' + view).classList.add('active');
document.getElementById('topbar-title').textContent = VIEW_TITLES[view][0];
document.getElementById('topbar-sub').textContent = VIEW_TITLES[view][1];
const topbarTitleEl = document.getElementById('topbar-title');
const topbarTitleWrap = document.getElementById('topbar-title-wrap');
const topbarSubEl = document.getElementById('topbar-sub');
const isWorkplanView = (view === 'workplan');
topbarTitleEl.classList.toggle('topbar-title-lg', isWorkplanView);
topbarTitleWrap.classList.toggle('topbar-title-wrap-center', isWorkplanView);
topbarSubEl.style.display = isWorkplanView ? 'none' : '';
document.querySelector('.topbar').classList.toggle('topbar-workplan', isWorkplanView);
closeNotifPanel();
if (view === 'dashboard') loadDashboard();
if (view === 'workplan') loadWorkplanView();
if (view === 'requisitions') loadRequisitions();
if (view === 'approvals') loadApprovals();
if (view === 'accountability') loadAccountability();
if (view === 'reports') loadAuditLog();
if (view === 'users') loadUsers();
if (view === 'departments') loadDepartmentsView();
}
document.querySelectorAll('.nav-item[data-view]').forEach(btn => {
btn.addEventListener('click', () => { switchView(btn.dataset.view); closeSidebar(); });
});
document.querySelectorAll('[data-view-link]').forEach(btn => {
btn.addEventListener('click', () => { switchView(btn.dataset.viewLink); closeSidebar(); });
});
// ---- Mobile sidebar (hamburger) --------------------------------------------
function openSidebar() {
document.querySelector('.sidebar').classList.add('open');
document.getElementById('sidebar-backdrop').classList.add('show');
}
function closeSidebar() {
document.querySelector('.sidebar').classList.remove('open');
document.getElementById('sidebar-backdrop').classList.remove('show');
}
function toggleSidebar() {
const sb = document.querySelector('.sidebar');
if (sb.classList.contains('open')) closeSidebar(); else openSidebar();
}
document.getElementById('hamburger-btn').addEventListener('click', toggleSidebar);
document.getElementById('sidebar-backdrop').addEventListener('click', closeSidebar);
// ---- Modals -----------------------------------------------------------------
function openModal(id) { document.getElementById(id).classList.add('show'); }
function closeModal(id) {
const overlay = document.getElementById(id);
overlay.classList.remove('show');
// Reset to normal size on close so the next time it's opened it starts
// un-maximized, rather than remembering the last maximize state.
const modal = overlay.querySelector('.modal');
if (modal) modal.classList.remove('modal-maximized');
overlay.classList.remove('overlay-maximized');
const btn = document.getElementById(id + '-max-btn');
if (btn) { btn.textContent = '⛶'; btn.title = 'Maximize'; }
}
document.querySelectorAll('[data-close]').forEach(el => el.addEventListener('click', () => closeModal(el.dataset.close)));
// Toggles a modal (by its overlay id) between its normal centred size and
// a fullscreen size that fills the entire page — used by the Requisition
// form and Requisition view/detail modals so their wide tables get room
// to expand instead of scrolling in a small box. Toggling again (minimize)
// restores the modal to its original size.
function toggleModalMaximize(modalId) {
const overlay = document.getElementById(modalId);
if (!overlay) return;
const modal = overlay.querySelector('.modal');
if (!modal) return;
const maximized = modal.classList.toggle('modal-maximized');
overlay.classList.toggle('overlay-maximized', maximized);
const btn = document.getElementById(modalId + '-max-btn');
if (btn) { btn.textContent = maximized ? '⧉' : '⛶'; btn.title = maximized ? 'Minimize' : 'Maximize'; }
}
document.querySelectorAll('.overlay').forEach(ov => ov.addEventListener('click', (e) => { if (e.target === ov && ov.id !== 'modal-req') ov.classList.remove('show'); }));
// ---- My Settings (profile only — signature now lives on the New/Edit User modal) --------
document.getElementById('user-chip-btn').addEventListener('click', openSettingsModal);
async function openSettingsModal() {
openModal('modal-settings');
document.getElementById('set-name').textContent = STATE.name || '—';
document.getElementById('set-role').textContent = statusLabel(STATE.role);
try {
const me = await api('/api/auth/me');
document.getElementById('set-name').textContent = me.full_name || '—';
document.getElementById('set-role').textContent = statusLabel(me.role);
document.getElementById('set-email').textContent = me.email || '—';
const dept = STATE.departments.find(d => d.id === me.department_id);
document.getElementById('set-dept').textContent = deptLabel(dept) || '—';
STATE.signatureUrl = me.signature_url || null;
} catch (e) { toast(e.message, 'error'); }
}
// ---- Notifications ------------------------------------------------------------
document.getElementById('notif-btn').addEventListener('click', async () => {
const panel = document.getElementById('notif-panel');
panel.classList.toggle('show');
if (panel.classList.contains('show')) await renderNotifications();
});
function closeNotifPanel() { document.getElementById('notif-panel').classList.remove('show'); }
document.getElementById('mark-all-read').addEventListener('click', async () => {
await api('/api/notifications/read-all', { method: 'PATCH' });
refreshNotifications(); renderNotifications();
});
async function refreshNotifications() {
try {
const items = await api('/api/notifications?unread_only=true');
const badge = document.getElementById('notif-badge');
if (items.length > 0) { badge.style.display = 'flex'; badge.textContent = items.length > 9 ? '9+' : items.length; }
else badge.style.display = 'none';
} catch (e) { /* silent */ }
}
async function renderNotifications() {
const list = document.getElementById('notif-list');
list.innerHTML = '<div class="loading-row"><span class="spinner spinner-dark"></span></div>';
try {
const items = await api('/api/notifications');
if (items.length === 0) { list.innerHTML = '<div class="notif-empty">You have no notifications yet.</div>'; return; }
list.innerHTML = items.map(n => `
<div class="notif-item ${n.is_read ? '' : 'unread'}">
<div class="dot"></div>
<div><div class="msg">${escapeHtml(n.message)}</div><div class="time">${fmtDate(n.created_at)}</div></div>
</div>`).join('');
} catch (e) { list.innerHTML = '<div class="notif-empty">Could not load notifications.</div>'; }
}
// ---- Departments / Work Plans (shared reference data) --------------------------
async function loadDepartments() {
STATE.departments = await api('/api/departments');
const selects = ['wp-dept-filter', 'u-department', 'bc-department', 'req-form-department'];
selects.forEach(id => {
const el = document.getElementById(id);
if (!el) return;
const keepFirst = id === 'wp-dept-filter';
el.innerHTML = (keepFirst ? '<option value="">All Departments</option>' : '<option value="">— Select —</option>') +
STATE.departments.map(d => `<option value="${d.id}">${escapeHtml(deptLabelWithCode(d))}</option>`).join('');
});
}
async function loadWorkplans() {
STATE.workplans = await api('/api/workplans');
const wpSel = document.getElementById('wp-select');
const bcSel = document.getElementById('bc-workplan');
const revSel = document.getElementById('rev-workplan');
const opts = STATE.workplans.map(w => `<option value="${w.id}" style="text-align:center;">${escapeHtml(w.title)} — FY ${escapeHtml(w.financial_year)}</option>`).join('');
if (wpSel) wpSel.innerHTML = opts || '<option value="">No work plans yet</option>';
if (bcSel) bcSel.innerHTML = opts || '<option value="">No work plans yet</option>';
if (revSel) revSel.innerHTML = opts || '<option value="">No work plans yet</option>';
applyWorkplanTableTitles();
}
// ---- Work-plan table headings (the 4 Work Plan & Budget table titles) --------------
// Each work plan carries its own heading for the 4 tables below; switching
// the "Annual Work Plan" dropdown swaps all 4 headings to match. They are
// only ever edited from the New/Edit Work Plan modal (see wpn-* fields).
const WORKPLAN_TABLE_TITLE_FIELDS = {
'wp-title-revenue-summary': 'title_revenue_summary',
'wp-title-dept-summary': 'title_dept_summary',
'wp-title-revenue-detail': 'title_revenue_detail',
'wp-title-main-table': 'title_main_table',
};
function applyWorkplanTableTitles() {
const wpVal = document.getElementById('wp-select').value;
const wp = STATE.workplans.find(w => String(w.id) === String(wpVal));
for (const [elId, field] of Object.entries(WORKPLAN_TABLE_TITLE_FIELDS)) {
const el = document.getElementById(elId);
if (el && wp && wp[field]) el.textContent = wp[field];
}
}
// ---- Dashboard -----------------------------------------------------------------
async function loadDashboard() {
try {
const s = await api('/api/dashboard/stats');
document.getElementById('stat-pending').textContent = s.pending_approvals;
document.getElementById('stat-approved').textContent = s.approved_requisitions;
document.getElementById('stat-rejected').textContent = s.rejected_requisitions;
document.getElementById('stat-budget').textContent = money(s.total_budget);
document.getElementById('util-pct').textContent = s.utilization_pct + '%';
document.getElementById('util-bar').style.width = Math.min(s.utilization_pct, 100) + '%';
document.getElementById('util-detail').textContent = `UGX ${money(s.budget_utilized)} committed of UGX ${money(s.total_budget)} allocated`;
const list = document.getElementById('recent-activity-list');
if (s.recent_activity.length === 0) {
list.innerHTML = '<li class="empty-state" style="padding:20px 0;">No activity recorded yet.</li>';
} else {
list.innerHTML = s.recent_activity.map(r => `
<li>
<div class="tl-stamp">${statusIcon(r.status)}</div>
<div class="tl-body">
<div class="tl-title">${r.ref_no} <span class="pill pill-${r.status}" style="margin-left:6px;">${statusLabel(r.status)}</span></div>
<div class="tl-meta">${escapeHtml(r.department || '—')} • UGX ${money(r.amount)} • ${fmtDate(r.created_at)}</div>
</div>
</li>`).join('');
}
renderDeptChart(s.budget_by_department || []);
} catch (e) { toast(e.message, 'error'); }
}
function statusIcon(status) {
if (['approved','accounted'].includes(status)) return '✓';
if (status === 'rejected') return '✕';
if (status === 'returned') return '↺';
return '…';
}
document.getElementById('qa-new-req').addEventListener('click', () => openRequisitionModal());
function renderDeptChart(data) {
const el = document.getElementById('dept-chart');
if (!el) return;
if (!data || data.length === 0) {
el.innerHTML = '<div class="empty-state" style="padding:20px;">No budget data yet.</div>';
return;
}
const sorted = [...data].sort((a, b) => (b.amount || 0) - (a.amount || 0));
const max = Math.max(...sorted.map(d => Number(d.amount) || 0), 1);
const palette = ['var(--teal-600)', 'var(--gold-600)', 'var(--navy-900)', 'var(--teal-500)', 'var(--danger)', 'var(--info)'];
el.innerHTML = sorted.map((d, i) => {
const pct = Math.max((Number(d.amount) || 0) / max * 100, 1.5);
return `
<div style="margin-bottom:14px;">
<div style="display:flex; justify-content:space-between; align-items:baseline; font-size:12.5px; margin-bottom:5px; gap:10px;">
<span style="font-weight:600; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${escapeHtml(d.department)}</span>
<span class="mono" style="color:var(--ink-500); flex-shrink:0;">UGX ${money(d.amount)}</span>
</div>
<div class="util-bar-track">
<div class="util-bar-fill" style="width:${pct}%; background:${palette[i % palette.length]}; box-shadow:none;"></div>
</div>
</div>`;
}).join('');
}
// ---- Work Plan & Budget view -----------------------------------------------------
async function loadWorkplanView() {
await loadWorkplans();
await renderBudgetCodes();
await renderRevenueSources();
}
document.getElementById('wp-select').addEventListener('change', () => { applyWorkplanTableTitles(); renderBudgetCodes(); renderRevenueSources(); });
document.getElementById('wp-download-pdf-btn').addEventListener('click', downloadWorkPlanPdf);
// Fetches the PDF as a blob (auth header can't ride a plain <a href>) and triggers a save.
async function downloadWorkPlanPdf() {
const wpId = document.getElementById('wp-select').value;
if (!wpId) { toast('Select a work plan first', 'error'); return; }
const btn = document.getElementById('wp-download-pdf-btn');
btn.disabled = true;
try {
const res = await fetch(`${API_BASE}/api/work-plans/${wpId}/report-pdf`, { headers: { Authorization: 'Bearer ' + STATE.token } });
if (!res.ok) throw new Error('Could not generate the PDF');
const blob = await res.blob();
const url = URL.createObjectURL(blob);
const a = document.createElement('a');
a.href = url;
a.download = `Annual_Work_Plan_FY_${document.getElementById('wp-fy-title').textContent.replace('/', '-')}.pdf`;
document.body.appendChild(a); a.click(); a.remove();
URL.revokeObjectURL(url);
} catch (e) { toast(e.message, 'error'); }
finally { btn.disabled = false; }
}
document.getElementById('wp-dept-filter').addEventListener('change', renderBudgetCodes);
document.getElementById('wp-search').addEventListener('input', debounce(renderBudgetCodes, 300));
// Renders the "Revenue Sources Summary" table (unchanged, per Council request)
// AND the new "Revenue Source by Category for the FY 2026/27" detail (categories with sub rows) that
// appears right after the summary. The summary's Approved Budget Amount for
// each source is obtained automatically on the backend as the Category Total
// (sum of that source's sub-row Approved Estimates).
async function renderRevenueSources() {
  const tbody = document.getElementById('wp-revenue-summary-body');
  const totalEl = document.getElementById('wp-revenue-summary-total');
  tbody.innerHTML = '<tr><td colspan="3" class="loading-row"><span class="spinner spinner-dark"></span></td></tr>';
  const wpId = document.getElementById('wp-select').value;
  try {
    let path = '/api/revenue-sources';
    if (wpId) path += `?work_plan_id=${wpId}`;
    const sources = await api(path);
    STATE.revenueSources = sources;
    renderRevenueDetailTable(sources);

    // Sum each matching source's Category Total (auto-derived from its sub
    // rows) into one of the three fixed Council revenue categories.
    const categoryTotals = { gou: 0, lr: 0, mdp: 0 };
    sources.forEach(r => {
      const key = categorizeRevenueSource(r);
      if (key) categoryTotals[key] += Number(r.approved_budget_amount) || 0;
    });

    tbody.innerHTML = REVENUE_SUMMARY_CATEGORIES.map(cat => `
      <tr>
        <td>${escapeHtml(cat.pbs_fund_code)} — ${escapeHtml(cat.source_of_financing_name)}</td>
        <td class="rev-func-def">${formatMultilinePoints(cat.functional_definition)}</td>
        <td class="num mono">${money(categoryTotals[cat.key])}</td>
      </tr>`).join('');

    const total = categoryTotals.gou + categoryTotals.lr + categoryTotals.mdp;
    totalEl.textContent = 'UGX ' + money(total);
  } catch (e) {
    // Even on error, keep the three fixed rows visible with zeroed amounts
    // rather than an empty-state message, since their content is constant.
    tbody.innerHTML = REVENUE_SUMMARY_CATEGORIES.map(cat => `
      <tr>
        <td>${escapeHtml(cat.pbs_fund_code)} — ${escapeHtml(cat.source_of_financing_name)}</td>
        <td class="rev-func-def">${formatMultilinePoints(cat.functional_definition)}</td>
        <td class="num mono">0</td>
      </tr>`).join('');
    totalEl.textContent = 'UGX 0';
    toast(e.message, 'error');
    renderRevenueDetailTable([]);
  }
}
// Renders the "Revenue Source by Category for the FY 2026/27": one category head row per revenue source
// (PBS Fund Code + Revenue Source + Functional Definition title), its sub rows
// (revenue items with Approved Estimates), an inline "+ Sub Row" adder and an
// Auto Category Total row (sum of sub rows) — mirroring the Council's sheet.
function renderRevenueDetailTable(sources) {
const tbody = document.getElementById('wp-revenue-detail-body');
if (!sources || sources.length === 0) {
tbody.innerHTML = '<tr><td colspan="6"><div class="empty-state" style="padding:16px;">No revenue sources recorded for this work plan yet. Use "+ Add Revenue Sources" below to create the first category with its sub rows.</div></td></tr>';
return;
}
const admin = STATE.role === 'admin';
let html = '';
sources.forEach(r => {
const items = r.items || [];
const total = (r.category_total != null) ? Number(r.category_total) : (Number(r.approved_budget_amount) || 0);
html += `
<tr class="rev-cat-head">
<td class="mono">${escapeHtml(r.pbs_fund_code || '—')}</td>
<td class="wrap">${escapeHtml(r.source_of_financing_name || '—')}</td>
<td class="wrap rev-func-def">${formatMultilinePoints(r.functional_definition)}</td>
<td></td>
<td></td>
<td style="white-space:nowrap; text-align:right;">${admin ? `
<button class="btn btn-ghost" style="padding:4px 8px; font-size:10.5px;" onclick="toggleRevAddItemRow(${r.id})">+ Sub Row</button>
<button class="btn btn-ghost" style="padding:4px 8px; font-size:10.5px; margin-left:4px;" onclick="openEditRevenueSource(${r.id})">Edit</button>
<button class="btn btn-danger" style="padding:4px 8px; font-size:10.5px; margin-left:4px;" onclick="deleteRevenueSource(${r.id})">Delete</button>` : ''}</td>
</tr>`;
items.forEach(it => {
html += `
<tr class="rev-item-row">
<td></td>
<td></td>
<td class="rev-item-desc wrap">${escapeHtml(it.description)}</td>
<td class="num mono">${money(it.amount)}</td>
<td></td>
<td style="text-align:right;">${admin ? `<button class="btn btn-ghost" style="padding:3px 7px; font-size:10.5px;" title="Remove sub row" onclick="deleteRevItem(${it.id})">✕</button>` : ''}</td>
</tr>`;
});
html += `
<tr class="rev-add-row" id="rev-add-row-${r.id}" style="display:none;">
<td></td>
<td></td>
<td><input type="text" id="rev-new-item-desc-${r.id}" placeholder="Revenue item, e.g. Unconditional Grant – Non-Wage" /></td>
<td><input type="number" id="rev-new-item-amt-${r.id}" value="0" /></td>
<td></td>
<td style="white-space:nowrap; text-align:right;">
<button class="btn btn-primary" style="padding:4px 8px; font-size:10.5px;" onclick="saveRevNewItem(${r.id})">Save</button>
<button class="btn btn-ghost" style="padding:4px 8px; font-size:10.5px; margin-left:4px;" onclick="toggleRevAddItemRow(${r.id})">✕</button>
</td>
</tr>
<tr class="rev-total-row">
<td></td>
<td></td>
<td>Category Total</td>
<td></td>
<td class="num mono">${money(total)}<span class="rev-auto-chip">Auto</span></td>
<td></td>
</tr>`;
});
tbody.innerHTML = html;
}
function toggleRevAddItemRow(id) {
const row = document.getElementById('rev-add-row-' + id);
if (!row) return;
row.style.display = (row.style.display === 'none') ? 'table-row' : 'none';
if (row.style.display !== 'none') {
const f = document.getElementById('rev-new-item-desc-' + id);
if (f) f.focus();
}
}
async function saveRevNewItem(id) {
const descEl = document.getElementById('rev-new-item-desc-' + id);
const amtEl = document.getElementById('rev-new-item-amt-' + id);
const desc = (descEl.value || '').trim();
const amt = Number(amtEl.value || 0);
if (!desc) { toast('Please enter the revenue item description', 'error'); return; }
try {
await api(`/api/revenue-sources/${id}/items`, { method: 'POST', body: JSON.stringify({ description: desc, amount: amt }) });
toast('Sub row added — Category Total and Summary updated', 'success');
renderRevenueSources();
} catch (e) { toast(e.message, 'error'); }
}
async function deleteRevItem(itemId) {
if (!confirm('Remove this sub row? The Category Total and the Summary of Sources of Revenue will update automatically.')) return;
try {
await api(`/api/revenue-source-items/${itemId}`, { method: 'DELETE' });
toast('Sub row removed', 'success');
renderRevenueSources();
} catch (e) { toast(e.message, 'error'); }
}
// ---- Clear all: Revenue Sources (source of revenue table) --------------------
document.getElementById('wp-revenue-clear-btn').addEventListener('click', async () => {
const wpId = document.getElementById('wp-select').value;
if (!wpId) { toast('Please select a work plan first', 'error'); return; }
if (!confirm('Clear ALL revenue sources (and their sub rows) for this work plan? This cannot be undone.')) return;
// Empty the tables on screen immediately so the clear feels instant, rather
// than waiting on the network round trip before anything visibly changes.
document.getElementById('wp-revenue-detail-body').innerHTML = '<tr><td colspan="6"><div class="empty-state" style="padding:16px;">Clearing…</div></td></tr>';
document.getElementById('wp-revenue-summary-body').innerHTML = '<tr><td colspan="3" class="loading-row"><span class="spinner spinner-dark"></span></td></tr>';
try {
const result = await api(`/api/revenue-sources/clear?work_plan_id=${wpId}`, { method: 'DELETE' });
toast(`Cleared ${result.deleted} revenue source(s)`, 'success');
} catch (e) { toast(e.message, 'error'); } finally {
renderRevenueSources();
}
});
// ---- Clear all: Annual Work Plan / Budget Estimates ---------------------------
document.getElementById('wp-clear-btn').addEventListener('click', async () => {
const wpId = document.getElementById('wp-select').value;
if (!wpId) { toast('Please select a work plan first', 'error'); return; }
if (!confirm('Clear ALL activity & budget estimate rows for this work plan? This cannot be undone.')) return;
// Empty the main table and the dependent Department Budget Summary table
// on screen immediately, before the request even resolves.
document.getElementById('wp-table-body').innerHTML = '<tr><td colspan="20"><div class="empty-state" style="padding:16px;">Clearing…</div></td></tr>';
renderDeptSummaryTable([]);
try {
const result = await api(`/api/budget-codes/clear?work_plan_id=${wpId}`, { method: 'DELETE' });
let msg = `Cleared ${result.deleted} budget estimate row(s)`;
if (result.skipped) msg += `, ${result.skipped} skipped (have requisitions on record)`;
toast(msg, 'success');
} catch (e) { toast(e.message, 'error'); } finally {
renderBudgetCodes();
}
});
// Renders the "Department Budget Summary" table in the work-plan header.
function renderDeptSummaryTable(codes) {
const tbody = document.getElementById('wp-dept-summary-body');
const totalsIds = { q1: 'wp-summary-q1', q2: 'wp-summary-q2', q3: 'wp-summary-q3', q4: 'wp-summary-q4', total: 'wp-summary-total', uncommitted: 'wp-summary-uncommitted' };
if (!codes || codes.length === 0) {
tbody.innerHTML = '<tr><td colspan="7"><div class="empty-state" style="padding:16px;">No budget codes to summarise.</div></td></tr>';
Object.values(totalsIds).forEach(id => document.getElementById(id).textContent = 'UGX 0');
return;
}
const map = {};
codes.forEach(c => {
const name = c.department_code_and_name || c.department_name || 'Unassigned';
if (!map[name]) map[name] = { deptId: c.department_id, q1: 0, q2: 0, q3: 0, q4: 0, total: 0, uncommitted: 0 };
map[name].q1 += Number(c.q1_amount) || 0;
map[name].q2 += Number(c.q2_amount) || 0;
map[name].q3 += Number(c.q3_amount) || 0;
map[name].q4 += Number(c.q4_amount) || 0;
map[name].total += Number(c.allocated_amount) || 0;
map[name].uncommitted += Number(c.available_balance) || 0;
});
const rows = Object.entries(map).sort((a, b) => b[1].total - a[1].total);
tbody.innerHTML = rows.map(([name, v]) => {
return `
<tr>
<td>${escapeHtml(name)}</td>
<td class="num mono">${money(v.q1)}</td>
<td class="num mono">${money(v.q2)}</td>
<td class="num mono">${money(v.q3)}</td>
<td class="num mono">${money(v.q4)}</td>
<td class="num mono">${money(v.total)}</td>
<td class="num mono">${money(v.uncommitted)}</td>
</tr>`;
}).join('');
const grand = rows.reduce((acc, [, v]) => {
acc.q1 += v.q1; acc.q2 += v.q2; acc.q3 += v.q3; acc.q4 += v.q4; acc.total += v.total; acc.uncommitted += v.uncommitted;
return acc;
}, { q1: 0, q2: 0, q3: 0, q4: 0, total: 0, uncommitted: 0 });
document.getElementById(totalsIds.q1).textContent = money(grand.q1);
document.getElementById(totalsIds.q2).textContent = money(grand.q2);
document.getElementById(totalsIds.q3).textContent = money(grand.q3);
document.getElementById(totalsIds.q4).textContent = money(grand.q4);
document.getElementById(totalsIds.total).textContent = money(grand.total);
document.getElementById(totalsIds.uncommitted).textContent = money(grand.uncommitted);
}
function renderDeptOutputChart(codes) {
const el = document.getElementById('wp-output-chart');
if (!el) return;
if (!codes || codes.length === 0) {
el.innerHTML = '<div class="empty-state" style="padding:20px;">No budget data yet.</div>';
return;
}
// Note: baseline_value/planned_target are a best-effort numeric figure —
// for rows where the source workbook recorded a narrative or multi-part
// value (see baseline_note/target_note, shown in the table and on hover),
// this is only the first number found in that text, not a precise total.
const map = {};
codes.forEach(c => {
const name = c.department_name || 'Unassigned';
if (!map[name]) map[name] = { baseline: 0, target: 0, actual: 0, actualRows: 0, totalRows: 0 };
map[name].baseline += Number(c.baseline_value) || 0;
map[name].target += Number(c.planned_target) || 0;
const av = parseNumericLoose(c.actual_output);
if (av !== null) { map[name].actual += av; map[name].actualRows += 1; }
map[name].totalRows += 1;
});
const rows = Object.entries(map).map(([name, v]) => ({
name,
baseline: v.baseline,
target: v.target,
actual: v.actual,
actualRows: v.actualRows,
totalRows: v.totalRows,
variance: v.actual - v.target,
achievementPct: v.target > 0 ? Math.round((v.actual / v.target) * 100) : (v.actual > 0 ? 100 : 0),
})).sort((a, b) => b.target - a.target);
const COLOR_BASELINE = '#6B7C80';
const COLOR_TARGET = '#146B5F';
const COLOR_ACTUAL = '#B9852F';
const COLOR_TEXT = '#3B4C51';
const COLOR_AXIS = '#C7D2D0';
const maxVal = Math.max(...rows.map(r => Math.max(r.baseline, r.target, r.actual)), 1);
const groupW = 170;
const barW = 24;
const gap = 4;
const chartW = Math.max(600, rows.length * groupW);
const chartH = 320;
const baseline = chartH - 84;
const plotH = baseline - 24;
let bars = '';
rows.forEach((r, i) => {
const cx = i * groupW + groupW / 2;
const bH = Math.max((r.baseline / maxVal) * plotH, 1);
const tH = Math.max((r.target / maxVal) * plotH, 1);
const aH = Math.max((r.actual / maxVal) * plotH, 1);
const bx = cx - (barW * 1.5) - gap;
const tx = cx - (barW / 2);
const ax = cx + (barW / 2) + gap;
const by = baseline - bH;
const ty = baseline - tH;
const ay = baseline - aH;
const shortName = r.name.length > 15 ? r.name.slice(0, 14) + '…' : r.name;
const varianceLabel = r.variance >= 0 ? `+${money(r.variance)}` : `−${money(Math.abs(r.variance))}`;
const varianceColor = r.variance >= 0 ? '#1F8A5F' : '#B8382A';
const reportedNote = r.actualRows < r.totalRows ? ` (${r.actualRows}/${r.totalRows} outputs reported numerically)` : '';
bars += `
<rect x="${bx}" y="${by}" width="${barW}" height="${bH}" rx="4" fill="${COLOR_BASELINE}"></rect>
<text x="${bx + barW / 2}" y="${by - 5}" text-anchor="middle" font-size="8.5" font-family="IBM Plex Mono, ui-monospace, monospace" fill="${COLOR_TEXT}">${money(r.baseline)}</text>
<rect x="${tx}" y="${ty}" width="${barW}" height="${tH}" rx="4" fill="${COLOR_TARGET}"></rect>
<text x="${tx + barW / 2}" y="${ty - 5}" text-anchor="middle" font-size="8.5" font-family="IBM Plex Mono, ui-monospace, monospace" fill="${COLOR_TEXT}">${money(r.target)}</text>
<rect x="${ax}" y="${ay}" width="${barW}" height="${aH}" rx="4" fill="${COLOR_ACTUAL}"></rect>
<text x="${ax + barW / 2}" y="${ay - 5}" text-anchor="middle" font-size="8.5" font-family="IBM Plex Mono, ui-monospace, monospace" fill="${COLOR_TEXT}">${money(r.actual)}</text>
<text x="${cx}" y="${baseline + 20}" text-anchor="middle" font-size="10.5" font-weight="600" fill="${COLOR_TEXT}">${escapeHtml(shortName)}</text>
<text x="${cx}" y="${baseline + 34}" text-anchor="middle" font-size="9.5" font-weight="700" fill="${varianceColor}">${varianceLabel} vs target</text>
<title>${escapeHtml(r.name)}: Baseline ${money(r.baseline)}, Target ${money(r.target)}, Actual ${money(r.actual)}${reportedNote} — ${r.achievementPct}% of target achieved</title>
`;
});
el.innerHTML = `
<div style="display:flex; gap:18px; align-items:center; margin-bottom:10px; font-size:11.5px; color:var(--ink-700); flex-wrap:wrap;">
<span style="display:inline-flex; align-items:center; gap:6px;"><span style="width:12px;height:12px;border-radius:3px;background:${COLOR_BASELINE}; display:inline-block;"></span>Baseline Value</span>
<span style="display:inline-flex; align-items:center; gap:6px;"><span style="width:12px;height:12px;border-radius:3px;background:${COLOR_TARGET}; display:inline-block;"></span>Planned Target</span>
<span style="display:inline-flex; align-items:center; gap:6px;"><span style="width:12px;height:12px;border-radius:3px;background:${COLOR_ACTUAL}; display:inline-block;"></span>Actual Output Delivered</span>
</div>
<svg viewBox="0 0 ${chartW} ${chartH}" width="100%" height="${chartH}" style="min-width:${chartW}px; display:block;">
<line x1="0" y1="${baseline}" x2="${chartW}" y2="${baseline}" stroke="${COLOR_AXIS}" stroke-width="1"></line>
${bars}
</svg>
`;
}
function renderDeptPieChart(codes) {
const el = document.getElementById('wp-pie-chart');
if (!el) return;
if (!codes || codes.length === 0) {
el.innerHTML = '<div class="empty-state" style="padding:20px;">No budget data yet.</div>';
return;
}
const map = {};
codes.forEach(c => {
const name = c.department_name || 'Unassigned';
map[name] = (map[name] || 0) + (Number(c.allocated_amount) || 0);
});
const rows = Object.entries(map).sort((a, b) => b[1] - a[1]);
const total = rows.reduce((s, [, v]) => s + v, 0) || 1;
const palette = ['#146B5F', '#B9852F', '#0A1F2B', '#1C8577', '#B8382A', '#2E5E8C', '#6A3FA0', '#C99A3E', '#1F8A5F', '#6B7C80'];
let acc = 0;
const stops = rows.map(([, v], i) => {
const pct = (v / total) * 100;
const start = acc;
acc += pct;
return `${palette[i % palette.length]} ${start.toFixed(2)}% ${acc.toFixed(2)}%`;
}).join(', ');
const legend = rows.map(([name, v], i) => {
const pct = ((v / total) * 100).toFixed(1);
return `
<div style="display:flex; align-items:center; gap:9px; font-size:12.5px; margin-bottom:8px;">
<span style="width:12px;height:12px;border-radius:3px; background:${palette[i % palette.length]}; flex-shrink:0;"></span>
<span style="font-weight:600; flex:0 1 auto; max-width:150px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${escapeHtml(name)}</span>
<span class="mono" style="color:var(--ink-500); flex-shrink:0;">UGX ${money(v)}</span>
<span class="mono" style="color:var(--gold-600); font-weight:700; flex-shrink:0;">${pct}%</span>
</div>`;
}).join('');
el.innerHTML = `
<div style="width:200px; height:200px; border-radius:50%; background:conic-gradient(${stops}); flex-shrink:0; box-shadow:var(--shadow-sm); border:1px solid var(--line);"></div>
<div style="flex:1; min-width:240px;">${legend}</div>
`;
}
async function renderBudgetCodes() {
const tbody = document.getElementById('wp-table-body');
tbody.innerHTML = '<tr><td colspan="20" class="loading-row"><span class="spinner spinner-dark"></span></td></tr>';
const wpId = document.getElementById('wp-select').value;
const deptId = document.getElementById('wp-dept-filter').value;
const search = document.getElementById('wp-search').value.trim();
const wp = STATE.workplans.find(w => String(w.id) === String(wpId));
document.getElementById('wp-fy-title').textContent = wp ? wp.financial_year : '—';
try {
let path = '/api/budget-codes?';
if (wpId) path += `work_plan_id=${wpId}&`;
if (deptId) path += `department_id=${deptId}&`;
if (search) path += `search=${encodeURIComponent(search)}&`;
const codes = await api(path);
STATE.budgetCodes = codes;
renderDeptSummaryTable(codes);
if (codes.length === 0) {
tbody.innerHTML = `<tr><td colspan="20"><div class="empty-state">No budget codes found. ${STATE.role === 'admin' ? 'Create one to get started.' : 'Ask your Administrator to set up the work plan.'}</div></td></tr>`;
renderDeptOutputChart([]);
renderDeptPieChart([]);
return;
}
tbody.innerHTML = codes.map(c => `
<tr>
<td class="wrap">${escapeHtml(c.department_code_and_name || c.department_name || '—')}</td>
<td class="wrap">${escapeHtml(c.service_area || '—')}</td>
<td class="wrap">${escapeHtml(c.programme || '—')}</td>
<td class="wrap">${escapeHtml(c.sub_programme || '—')}</td>
<td class="mono">${escapeHtml(c.code)}</td>
<td class="wrap">${escapeHtml(c.output_description)}</td>
<td class="wrap">${escapeHtml(c.piap_output_description || '—')}</td>
<td class="wrap">${escapeHtml(c.piap_output_indicator || '—')}</td>
<td>${escapeHtml(c.unit_of_measure || '—')}</td>
<td class="${c.baseline_note ? 'wrap' : 'num'}" ${c.baseline_note ? `title="Recorded as: ${escapeHtml(c.baseline_note)}"` : ''}>${c.baseline_note ? escapeHtml(c.baseline_note) : money(c.baseline_value)}</td>
<td class="${c.target_note ? 'wrap' : 'num'}" ${c.target_note ? `title="Recorded as: ${escapeHtml(c.target_note)}"` : ''}>${c.target_note ? escapeHtml(c.target_note) : money(c.planned_target)}</td>
<td class="wrap">${escapeHtml(c.actual_output || '—')}</td>
<td class="num mono">${money(c.q1_amount)}</td>
<td class="num mono">${money(c.q2_amount)}</td>
<td class="num mono">${money(c.q3_amount)}</td>
<td class="num mono">${money(c.q4_amount)}</td>
<td class="num mono">${money(c.allocated_amount)}</td>
<td class="wrap">${escapeHtml(c.funding_source)}</td>
<td class="wrap">${escapeHtml(c.responsible_party || '—')}</td>
<td style="white-space:nowrap;">${STATE.role === 'admin' ? `<button class="btn btn-ghost" style="padding:6px 10px;" onclick="openEditBudgetCode(${c.id})">Edit</button> <button class="btn btn-danger" style="padding:6px 10px; margin-left:4px;" onclick="deleteBudgetCode(${c.id})">Delete</button>` : ''}</td>
</tr>`).join('');
renderDeptOutputChart(codes);
renderDeptPieChart(codes);
} catch (e) {
tbody.innerHTML = `<tr><td colspan="20"><div class="empty-state">${escapeHtml(e.message)}</div></td></tr>`;
renderDeptSummaryTable([]);
renderDeptOutputChart([]);
renderDeptPieChart([]);
}
}
async function deleteBudgetCode(id) {
const c = STATE.budgetCodes.find(x => x.id === id);
if (!confirm(`Delete budget code ${c ? c.code : id}? This cannot be undone.`)) return;
try {
await api(`/api/budget-codes/${id}`, { method: 'DELETE' });
toast('Budget estimate deleted', 'success');
renderBudgetCodes();
} catch (e) { toast(e.message, 'error'); }
}
function resetBudgetCodeForm() {
STATE.editingBudgetCodeId = null;
document.getElementById('bc-modal-title').textContent = 'New Budget Estimates Data Entry Form';
document.getElementById('bc-create-btn').textContent = 'Create Budget Estimate';
['bc-service-area','bc-code','bc-unit','bc-desc','bc-programme','bc-subprogramme','bc-piap-desc','bc-piap-indicator','bc-actual','bc-responsible','bc-baseline-note','bc-target-note'].forEach(id => document.getElementById(id).value = '');
['bc-baseline','bc-target','bc-q1','bc-q2','bc-q3','bc-q4'].forEach(id => document.getElementById(id).value = 0);
document.getElementById('bc-total').value = '0';
document.getElementById('bc-funding').value = 'Local Revenue';
}
document.getElementById('wp-new-btn').addEventListener('click', () => {
const wpVal = document.getElementById('wp-select').value;
const deptVal = document.getElementById('wp-dept-filter').value;
document.getElementById('bc-workplan').innerHTML = document.getElementById('wp-select').innerHTML;
resetBudgetCodeForm();
if (wpVal) document.getElementById('bc-workplan').value = wpVal;
if (deptVal) document.getElementById('bc-department').value = deptVal;
openModal('modal-bc');
});
function openEditBudgetCode(id) {
const c = STATE.budgetCodes.find(x => x.id === id);
if (!c) { toast('Could not find that budget code — try refreshing.', 'error'); return; }
document.getElementById('bc-workplan').innerHTML = document.getElementById('wp-select').innerHTML;
STATE.editingBudgetCodeId = id;
document.getElementById('bc-modal-title').textContent = `Edit Budget Estimate — ${c.code}`;
document.getElementById('bc-create-btn').textContent = 'Save Changes';
document.getElementById('bc-workplan').value = c.work_plan_id;
document.getElementById('bc-department').value = c.department_id;
document.getElementById('bc-service-area').value = c.service_area || '';
document.getElementById('bc-code').value = c.code || '';
document.getElementById('bc-unit').value = c.unit_of_measure || '';
document.getElementById('bc-desc').value = c.output_description || '';
document.getElementById('bc-programme').value = c.programme || '';
document.getElementById('bc-subprogramme').value = c.sub_programme || '';
document.getElementById('bc-piap-desc').value = c.piap_output_description || '';
document.getElementById('bc-piap-indicator').value = c.piap_output_indicator || '';
document.getElementById('bc-actual').value = c.actual_output || '';
document.getElementById('bc-baseline').value = c.baseline_value || 0;
document.getElementById('bc-baseline-note').value = c.baseline_note || '';
document.getElementById('bc-target').value = c.planned_target || 0;
document.getElementById('bc-target-note').value = c.target_note || '';
document.getElementById('bc-q1').value = c.q1_amount || 0;
document.getElementById('bc-q2').value = c.q2_amount || 0;
document.getElementById('bc-q3').value = c.q3_amount || 0;
document.getElementById('bc-q4').value = c.q4_amount || 0;
document.getElementById('bc-funding').value = c.funding_source || 'Local Revenue';
document.getElementById('bc-responsible').value = c.responsible_party || '';
recalcBcTotal();
openModal('modal-bc');
}
function recalcBcTotal() {
const q1 = Number(document.getElementById('bc-q1').value || 0);
const q2 = Number(document.getElementById('bc-q2').value || 0);
const q3 = Number(document.getElementById('bc-q3').value || 0);
const q4 = Number(document.getElementById('bc-q4').value || 0);
document.getElementById('bc-total').value = money(q1 + q2 + q3 + q4);
}
['bc-q1','bc-q2','bc-q3','bc-q4'].forEach(id => document.getElementById(id).addEventListener('input', recalcBcTotal));
document.getElementById('bc-create-btn').addEventListener('click', async () => {
const payload = {
work_plan_id: Number(document.getElementById('bc-workplan').value),
department_id: Number(document.getElementById('bc-department').value),
service_area: document.getElementById('bc-service-area').value.trim(),
code: document.getElementById('bc-code').value.trim(),
output_description: document.getElementById('bc-desc').value.trim(),
programme: document.getElementById('bc-programme').value.trim(),
sub_programme: document.getElementById('bc-subprogramme').value.trim(),
piap_output_description: document.getElementById('bc-piap-desc').value.trim(),
piap_output_indicator: document.getElementById('bc-piap-indicator').value.trim(),
unit_of_measure: document.getElementById('bc-unit').value.trim(),
baseline_value: Number(document.getElementById('bc-baseline').value || 0),
baseline_note: document.getElementById('bc-baseline-note').value.trim() || null,
planned_target: Number(document.getElementById('bc-target').value || 0),
target_note: document.getElementById('bc-target-note').value.trim() || null,
actual_output: document.getElementById('bc-actual').value.trim(),
q1_amount: Number(document.getElementById('bc-q1').value || 0),
q2_amount: Number(document.getElementById('bc-q2').value || 0),
q3_amount: Number(document.getElementById('bc-q3').value || 0),
q4_amount: Number(document.getElementById('bc-q4').value || 0),
funding_source: document.getElementById('bc-funding').value.trim() || 'Local Revenue',
responsible_party: document.getElementById('bc-responsible').value.trim(),
};
if (!payload.work_plan_id || !payload.department_id || !payload.code || !payload.output_description) {
toast('Please complete all required fields', 'error'); return;
}
try {
if (STATE.editingBudgetCodeId) {
await api(`/api/budget-codes/${STATE.editingBudgetCodeId}`, { method: 'PATCH', body: JSON.stringify(payload) });
toast('Budget estimate updated', 'success');
} else {
await api('/api/budget-codes', { method: 'POST', body: JSON.stringify(payload) });
toast('Budget estimate created', 'success');
}
closeModal('modal-bc');
renderBudgetCodes();
} catch (e) { toast(e.message, 'error'); }
});
document.getElementById('wp-new-workplan-btn').addEventListener('click', () => {
STATE.editingWorkPlanId = null;
document.getElementById('wpn-modal-title').textContent = 'New Work Plan';
document.getElementById('wpn-create-btn').textContent = 'Create Work Plan';
document.getElementById('wpn-fy').value = '';
document.getElementById('wpn-title').value = '';
document.getElementById('wpn-title-revenue-summary').value = '';
document.getElementById('wpn-title-dept-summary').value = '';
document.getElementById('wpn-title-revenue-detail').value = '';
document.getElementById('wpn-title-main-table').value = '';
openModal('modal-wp');
});
document.getElementById('wp-edit-workplan-btn').addEventListener('click', () => {
const wpVal = document.getElementById('wp-select').value;
const wp = STATE.workplans.find(w => String(w.id) === String(wpVal));
if (!wp) { toast('Please select a work plan to edit first', 'error'); return; }
STATE.editingWorkPlanId = wp.id;
document.getElementById('wpn-modal-title').textContent = `Edit Work Plan — ${wp.title}`;
document.getElementById('wpn-create-btn').textContent = 'Save Changes';
document.getElementById('wpn-fy').value = wp.financial_year;
document.getElementById('wpn-title').value = wp.title;
document.getElementById('wpn-title-revenue-summary').value = wp.title_revenue_summary || '';
document.getElementById('wpn-title-dept-summary').value = wp.title_dept_summary || '';
document.getElementById('wpn-title-revenue-detail').value = wp.title_revenue_detail || '';
document.getElementById('wpn-title-main-table').value = wp.title_main_table || '';
openModal('modal-wp');
});
document.getElementById('wpn-create-btn').addEventListener('click', async () => {
const financial_year = document.getElementById('wpn-fy').value.trim();
const title = document.getElementById('wpn-title').value.trim();
const title_revenue_summary = document.getElementById('wpn-title-revenue-summary').value.trim();
const title_dept_summary = document.getElementById('wpn-title-dept-summary').value.trim();
const title_revenue_detail = document.getElementById('wpn-title-revenue-detail').value.trim();
const title_main_table = document.getElementById('wpn-title-main-table').value.trim();
if (!financial_year || !title) { toast('Please complete both fields', 'error'); return; }
const payload = { financial_year, title, title_revenue_summary, title_dept_summary, title_revenue_detail, title_main_table };
try {
if (STATE.editingWorkPlanId) {
await api(`/api/workplans/${STATE.editingWorkPlanId}`, { method: 'PATCH', body: JSON.stringify(payload) });
toast('Work plan updated', 'success');
closeModal('modal-wp');
await loadWorkplans();
document.getElementById('wp-select').value = STATE.editingWorkPlanId;
applyWorkplanTableTitles();
renderBudgetCodes();
renderRevenueSources();
} else {
const wp = await api('/api/workplans', { method: 'POST', body: JSON.stringify(payload) });
toast('Work plan created', 'success');
closeModal('modal-wp');
await loadWorkplans();
document.getElementById('wp-select').value = wp.id;
applyWorkplanTableTitles();
renderBudgetCodes();
renderRevenueSources();
}
} catch (e) { toast(e.message, 'error'); }
});
// ---- Revenue Sources (category + sub rows) -----------------------------------
function resetRevenueSourceForm() {
STATE.editingRevenueSourceId = null;
STATE.revItems = [];
document.getElementById('rev-modal-title').textContent = 'New Revenue Source';
document.getElementById('rev-create-btn').textContent = 'Create Revenue Source';
populateRevDropdowns();
for (const selectId of Object.keys(REV_FIELD_MAP)) {
document.getElementById(selectId).value = '';
setRevCustomVisible(selectId, false);
}
document.getElementById('rev-amount').value = 0;
renderRevItems();
}
// Sub-row builder inside the Revenue Source form (mirrors the sub rows in the
// Revenue Source by Category for the FY 2026/27 / reference image).
function renderRevItems() {
const tbody = document.getElementById('rev-items-body');
if (!STATE.revItems.length) {
tbody.innerHTML = '<tr><td colspan="3"><div class="help-text" style="padding:10px;">No sub rows yet — click "+ Add Sub Row" to add revenue items under the functional definition title.</div></td></tr>';
return;
}
tbody.innerHTML = STATE.revItems.map((it, idx) => `
<tr>
<td class="wrap"><input type="text" value="${escapeHtml(it.description)}" placeholder="e.g. Unconditional Grant – Non-Wage" style="width:100%; border:1px solid var(--line); border-radius:6px; padding:6px 8px; font-size:12.5px;" oninput="updateRevItem(${idx},'description',this.value)"/></td>
<td><input type="number" value="${it.amount ?? 0}" style="width:130px; border:1px solid var(--line); border-radius:6px; padding:6px 8px; font-size:12.5px; font-family:var(--font-mono);" oninput="updateRevItem(${idx},'amount',this.value)"/></td>
<td><button type="button" class="btn btn-ghost" style="padding:5px 9px;" onclick="removeRevItem(${idx})">✕</button></td>
</tr>`).join('');
}
function updateRevItem(idx, field, value) {
const it = STATE.revItems[idx];
if (!it) return;
it[field] = (field === 'amount') ? Number(value || 0) : value;
}
function removeRevItem(idx) {
STATE.revItems.splice(idx, 1);
renderRevItems();
}
document.getElementById('rev-add-item-btn').addEventListener('click', () => {
STATE.revItems.push({ description: '', amount: 0 });
renderRevItems();
});
for (const selectId of Object.keys(REV_FIELD_MAP)) {
document.getElementById(selectId).addEventListener('change', () => onRevCategorySelect(selectId));
}
document.getElementById('wp-new-revenue-btn').addEventListener('click', () => {
const wpVal = document.getElementById('wp-select').value;
document.getElementById('rev-workplan').innerHTML = document.getElementById('wp-select').innerHTML;
resetRevenueSourceForm();
if (wpVal) document.getElementById('rev-workplan').value = wpVal;
openModal('modal-rev');
});
function openEditRevenueSource(id) {
const r = STATE.revenueSources.find(x => x.id === id);
if (!r) { toast('Could not find that revenue source — try refreshing.', 'error'); return; }
document.getElementById('rev-workplan').innerHTML = document.getElementById('wp-select').innerHTML;
STATE.editingRevenueSourceId = id;
document.getElementById('rev-modal-title').textContent = `Edit Revenue Source — ${r.source_of_financing_name || ''}`;
document.getElementById('rev-create-btn').textContent = 'Save Changes';
document.getElementById('rev-workplan').value = r.work_plan_id;
populateRevDropdowns();
const matchedKey = categorizeRevenueSource(r);
if (matchedKey) {
for (const selectId of Object.keys(REV_FIELD_MAP)) {
document.getElementById(selectId).value = matchedKey;
setRevCustomVisible(selectId, false);
}
} else {
document.getElementById('rev-fund-code').value = REV_CUSTOM_VALUE;
document.getElementById('rev-source-name').value = REV_CUSTOM_VALUE;
document.getElementById('rev-functional-def').value = REV_CUSTOM_VALUE;
setRevCustomVisible('rev-fund-code', true);
setRevCustomVisible('rev-source-name', true);
setRevCustomVisible('rev-functional-def', true);
document.getElementById('rev-fund-code-custom').value = r.pbs_fund_code || '';
document.getElementById('rev-source-name-custom').value = r.source_of_financing_name || '';
document.getElementById('rev-functional-def-custom').value = r.functional_definition || '';
}
document.getElementById('rev-amount').value = r.approved_budget_amount || 0;
STATE.revItems = (r.items || []).map(it => ({ description: it.description, amount: it.amount }));
renderRevItems();
openModal('modal-rev');
}
async function deleteRevenueSource(id) {
const r = STATE.revenueSources.find(x => x.id === id);
if (!confirm(`Delete revenue source "${r ? r.source_of_financing_name : id}" and all its sub rows? This cannot be undone.`)) return;
try {
await api(`/api/revenue-sources/${id}`, { method: 'DELETE' });
toast('Revenue source deleted', 'success');
renderRevenueSources();
} catch (e) { toast(e.message, 'error'); }
}
document.getElementById('rev-create-btn').addEventListener('click', async () => {
const payload = {
work_plan_id: Number(document.getElementById('rev-workplan').value),
pbs_fund_code: getRevFieldValue('rev-fund-code').trim(),
source_of_financing_name: getRevFieldValue('rev-source-name').trim(),
functional_definition: getRevFieldValue('rev-functional-def').trim(),
approved_budget_amount: Number(document.getElementById('rev-amount').value || 0),
items: STATE.revItems
.filter(it => it.description && it.description.trim() !== '')
.map(it => ({ description: it.description.trim(), amount: Number(it.amount) || 0 })),
};
if (!payload.work_plan_id || !payload.source_of_financing_name) {
toast('Please complete the work plan and revenue source name fields', 'error'); return;
}
try {
if (STATE.editingRevenueSourceId) {
await api(`/api/revenue-sources/${STATE.editingRevenueSourceId}`, { method: 'PATCH', body: JSON.stringify(payload) });
toast('Revenue source updated — totals recalculated', 'success');
} else {
await api('/api/revenue-sources', { method: 'POST', body: JSON.stringify(payload) });
toast('Revenue source created', 'success');
}
closeModal('modal-rev');
renderRevenueSources();
} catch (e) { toast(e.message, 'error'); }
});
// ---- Import Revenue Sources from Excel ---------------------------------------
document.getElementById('wp-import-revenue-btn').addEventListener('click', () => {
const wpVal = document.getElementById('wp-select').value;
if (!wpVal) { toast('Please select a work plan to import into first', 'error'); return; }
document.getElementById('wp-import-revenue-file').click();
});
document.getElementById('wp-import-revenue-file').addEventListener('change', async (e) => {
const file = e.target.files[0];
if (!file) return;
const wpVal = document.getElementById('wp-select').value;
const fd = new FormData();
fd.append('file', file);
try {
toast('Importing revenue sources from Excel…', 'info');
const result = await api(`/api/revenue-sources/import?work_plan_id=${wpVal}`, { method: 'POST', body: fd });
toast(`Imported ${result.created} revenue source row(s)${result.skipped ? `, skipped ${result.skipped}` : ''}`, 'success');
if (result.errors && result.errors.length) {
toast(`${result.errors.length} row warning(s) — first: ${result.errors[0]}`, 'error');
}
renderRevenueSources();
} catch (err) { toast(err.message, 'error'); }
finally { e.target.value = ''; }
});
// ---- Import Budget Estimates from Excel ------------------------------------
document.getElementById('wp-import-btn').addEventListener('click', () => {
const wpVal = document.getElementById('wp-select').value;
if (!wpVal) { toast('Please select a work plan to import into first', 'error'); return; }
document.getElementById('wp-import-file').click();
});
document.getElementById('wp-import-file').addEventListener('change', async (e) => {
const file = e.target.files[0];
if (!file) return;
const wpVal = document.getElementById('wp-select').value;
const fd = new FormData();
fd.append('file', file);
try {
toast('Importing budget estimates from Excel…', 'info');
const result = await api(`/api/budget-codes/import?work_plan_id=${wpVal}`, { method: 'POST', body: fd });
toast(`Imported ${result.created} budget estimate row(s)${result.skipped ? `, skipped ${result.skipped}` : ''}`, 'success');
if (result.errors && result.errors.length) {
const total = result.total_warnings || result.errors.length;
const shownNote = total > result.errors.length ? ` (showing first ${result.errors.length} of ${total})` : '';
toast(`${total} row warning(s)${shownNote} — first: ${result.errors[0]}`, 'error');
}
renderBudgetCodes();
} catch (err) { toast(err.message, 'error'); }
finally { e.target.value = ''; }
});
// ---- Requisitions --------------------------------------------------------------
function resetReqLineItems() {
// Start every new requisition with three Sub Activity sections (S/N 01,
// 02 and 03), each with 5 blank priced lines underneath it, so there's
// room to fill the form without needing an "Add Sub Activity" control
// (removed — sections are now fixed at three per requisition).
STATE.reqLineItems = [];
for (let sectionNo = 1; sectionNo <= 3; sectionNo++) {
STATE.reqLineItems.push({ item_no: sectionNo, description: '', units: '', qty: null, rate: null, amount: 0, isHeader: true });
for (let i = 0; i < 5; i++) {
STATE.reqLineItems.push({ item_no: sectionNo, description: '', units: '', qty: null, rate: null, amount: 0, isHeader: false, ledger_folio: '', charge_date: '' });
}
}
}
function currentReqSectionNo() {
if (!STATE.reqLineItems.length) return 1;
return STATE.reqLineItems[STATE.reqLineItems.length - 1].item_no;
}
function insertReqLineItemAfter(idx) {
const ref = STATE.reqLineItems[idx];
const sectionNo = ref ? ref.item_no : currentReqSectionNo();
STATE.reqLineItems.splice(idx + 1, 0, { item_no: sectionNo, description: '', units: '', qty: 0, rate: 0, amount: 0, isHeader: false, ledger_folio: '', charge_date: '' });
renderReqLineItems();
}
function updateReqLineItem(idx, field, value) {
const li = STATE.reqLineItems[idx];
if (!li) return;
if (field === 'qty' || field === 'rate') {
li[field] = value === '' ? null : Number(value);
if (li.qty != null && li.rate != null && !Number.isNaN(li.qty) && !Number.isNaN(li.rate)) {
li.amount = li.qty * li.rate;
}
} else if (field === 'amount') {
li.amount = Number(value || 0);
} else {
li[field] = value;
}
renderReqLineItems();
}
function removeReqLineItem(idx) {
STATE.reqLineItems.splice(idx, 1);
if (STATE.reqLineItems.length === 0) resetReqLineItems();
renderReqLineItems();
}
function reqLineItemsGrandTotal() {
return STATE.reqLineItems.reduce((sum, li) => sum + (Number(li.amount) || 0), 0);
}
function renderReqLineItems() {
const tbody = document.getElementById('req-lineitems-body');
const pvTbody = document.getElementById('pv-lineitems-body');
const activeEl = document.activeElement;
const activeIdx = activeEl && activeEl.dataset ? activeEl.dataset.liIdx : null;
const activeField = activeEl && activeEl.dataset ? activeEl.dataset.liField : null;
const chargeDate = document.getElementById('req-form-date') ? document.getElementById('req-form-date').textContent : '';
let lastNo = null;
tbody.innerHTML = STATE.reqLineItems.map((li, idx) => {
const showNo = li.item_no !== lastNo;
lastNo = li.item_no;
return `<tr>
<td style="font-weight:700;">${showNo ? 'S/N ' + String(li.item_no).padStart(2,'0') : ''}</td>
<td class="wrap"><textarea data-li-idx="${idx}" data-li-field="description" rows="1" placeholder="${li.isHeader ? 'Sub activity title, e.g. Field fuel' : 'Item description'}" oninput="updateReqLineItem(${idx},'description',this.value)">${escapeHtml(li.description)}</textarea></td>
<td><input type="text" data-li-idx="${idx}" data-li-field="units" value="${escapeHtml(li.units||'')}" oninput="updateReqLineItem(${idx},'units',this.value)"/></td>
<td><input type="number" data-li-idx="${idx}" data-li-field="qty" value="${li.qty ?? ''}" oninput="updateReqLineItem(${idx},'qty',this.value)"/></td>
<td><input type="number" data-li-idx="${idx}" data-li-field="rate" value="${li.rate ?? ''}" oninput="updateReqLineItem(${idx},'rate',this.value)"/></td>
<td><input type="number" data-li-idx="${idx}" data-li-field="amount" value="${li.amount ?? 0}" oninput="updateReqLineItem(${idx},'amount',this.value)"/></td>
<td class="no-print" style="white-space:nowrap;"><button type="button" class="rf-row-add" title="Add line" onclick="insertReqLineItemAfter(${idx})">＋</button><button type="button" class="rf-row-remove" title="Remove line" onclick="removeReqLineItem(${idx})">✕</button></td>
</tr>`;
}).join('');
// Payment Voucher table mirrors the same line items (so the same work
// isn't entered twice) but adds the two "Taken on charge expenditure"
// columns — Ledger Folio and a per-line charge Date — which only appear
// on the voucher.
if (pvTbody) {
let lastPvNo = null;
pvTbody.innerHTML = STATE.reqLineItems.filter(li => !li.isHeader || li.description).map((li, idx) => {
const showNo = li.item_no !== lastPvNo;
lastPvNo = li.item_no;
return `<tr>
<td>${showNo ? escapeHtml(chargeDate || '') : ''}</td>
<td class="wrap">${escapeHtml(li.description || '')}</td>
<td><input type="text" data-pv-li-idx="${idx}" data-pv-li-field="ledger_folio" value="${escapeHtml(li.ledger_folio||'')}" oninput="updatePvLineItem(${idx},'ledger_folio',this.value)"/></td>
<td><input type="text" data-pv-li-idx="${idx}" data-pv-li-field="charge_date" value="${escapeHtml(li.charge_date||'')}" oninput="updatePvLineItem(${idx},'charge_date',this.value)"/></td>
<td class="num">${li.amount ? money(li.amount) : ''}</td>
</tr>`;
}).join('');
}
const grandTotal = reqLineItemsGrandTotal();
const words = grandTotal > 0 ? numberToWordsUGX(grandTotal) : '—';
document.getElementById('req-grand-total').textContent = money(grandTotal);
document.getElementById('req-amount-words').textContent = words;
const pvGrandTotalEl = document.getElementById('pv-grand-total');
if (pvGrandTotalEl) {
pvGrandTotalEl.textContent = money(grandTotal);
document.getElementById('pv-total-shs').value = grandTotal > 0 ? `UGX ${money(grandTotal)}` : '';
document.getElementById('pv-total-shs-2').value = grandTotal > 0 ? `UGX ${money(grandTotal)}` : '';
document.getElementById('pv-passed-shs').value = grandTotal > 0 ? `UGX ${money(grandTotal)}` : '';
document.getElementById('pv-amount-words').textContent = words;
document.getElementById('pv-words-line').value = grandTotal > 0 ? words : '';
}
if (activeIdx !== null && activeField) {
const el = tbody.querySelector(`[data-li-idx="${activeIdx}"][data-li-field="${activeField}"]`);
if (el) { el.focus(); const v = el.value; el.value = ''; el.value = v; }
}
// Every description cell is a textarea (not a single-line input) so long
// item descriptions wrap onto new lines instead of being hidden past the
// edge of the cell — grow each one to fit its content right after paint.
tbody.querySelectorAll('textarea[data-li-field="description"]').forEach(autoGrowTextarea);
}
function autoGrowTextarea(el) {
el.style.height = 'auto';
el.style.height = el.scrollHeight + 'px';
}
function updatePvLineItem(idx, field, value) {
const li = STATE.reqLineItems[idx];
if (!li) return;
li[field] = value;
}
// ---- Attach Signature (entry forms) --------------------------------------------
// Fills the signature box nearest wherever this was clicked with whichever
// signature is on file for the account currently signed in. Actual
// approval-stage signatures are still recorded automatically from the
// approval history once a requisition is approved — this is a preview for
// whoever happens to be filling the box in front of them right now.
// Strictly role-gated: a box marked with a required role (Head of
// Department, Senior Treasurer, Town Clerk) can only be signed by an account
// currently signed in as that exact role — never by anyone else, and never
// by the System Administrator on someone else's behalf.
const SIG_ROLE_LABELS = { hod: 'Head of Department', treasurer: 'Senior Treasurer', clerk: 'Town Clerk' };
function attachSignature(targetId, btn, requiredRole) {
const el = document.getElementById(targetId);
if (!el) return;
if (requiredRole && STATE.role !== requiredRole) {
toast(`Only the ${SIG_ROLE_LABELS[requiredRole] || requiredRole} can attach a signature here`, 'error');
return;
}
if (!STATE.signatureUrl) {
toast('No signature on file yet — upload one in My Settings first', 'error');
return;
}
el.innerHTML = `<img src="${API_BASE}${STATE.signatureUrl}" alt="Signature"/>`;
// Once a signature has been placed, the "Attach Signature" prompt for that
// box is no longer relevant — remove it rather than leaving it visible.
if (btn) btn.style.display = 'none';
// Pull the authorizer's name from the system straight into the name field
// beneath the signature line — left editable in case it needs correcting.
const nameField = document.getElementById(targetId + '-name');
if (nameField && !nameField.value.trim()) nameField.value = STATE.name || '';
}
// Shows/hides each "Attach Signature" button according to whether the
// signed-in account's role is allowed to sign that particular box. Boxes
// with no required role (e.g. Signature of payee/witness/cashier, which
// aren't tied to a system role) stay visible for whoever is filling the
// form. Called whenever the New/Edit Requisition modal opens.
function refreshSignatureButtonVisibility() {
document.querySelectorAll('.sig-attach-btn[data-sig-role]').forEach(btn => {
const requiredRole = btn.getAttribute('data-sig-role');
btn.style.display = (STATE.role === requiredRole) ? '' : 'none';
});
}
async function openRequisitionModal(editReq) {
STATE.editingRequisitionId = editReq ? editReq.id : null;
document.getElementById('req-modal-title').textContent = editReq ? `Edit Requisition — ${editReq.ref_no}` : 'New Requisition';
document.getElementById('req-route-hod-label').textContent = editReq ? 'Save & Submit to Head of Department' : 'Submit to Head of Department';
document.getElementById('req-route-hod-mid-label').textContent = editReq ? 'Save & Submit to Head of Department' : 'Submit to Head of Department';
// Fill in the paper-form fields that mirror who's submitting this and when.
const deptSel = document.getElementById('req-form-department');
deptSel.value = String((editReq ? editReq.department_id : STATE.departmentId) || '');
// Row 1 — System user identity fields; always mirror the signed-in
// account, never editable, regardless of new vs. edit mode.
document.getElementById('req-form-sysuser').textContent = STATE.name || '—';
document.getElementById('req-form-sysemail').textContent = STATE.email || '—';
document.getElementById('req-form-sysrole').textContent = statusLabel(STATE.role) || '—';
// Row 2 — Financial Year / Quarter / Date.
document.getElementById('req-form-fy').value = editReq && editReq.financial_year ? editReq.financial_year : currentFinancialYearGuess();
document.getElementById('req-form-quarter').value = editReq && editReq.quarter ? editReq.quarter : currentQuarterGuess();
document.getElementById('req-form-date').textContent = editReq ? fmtDate(editReq.created_at) : fmtDate(new Date().toISOString());
// Row 3 — Position (defaults to the account's own position on file, but
// stays editable in case it needs adjusting for this requisition).
document.getElementById('req-form-position').value = editReq ? (editReq.requester_position || STATE.position || '') : (STATE.position || '');
// Requisitioner (just the name, no "Full names" label suffix) is typed by the person filling the
// form rather than being a read-only mirror of the account name — it's
// pre-filled with the account's name as a starting point either way.
document.getElementById('req-form-names').value = editReq ? (editReq.requester_name || STATE.name || '') : (STATE.name || '');
// Mob. No. — the requisitioner's own telephone, pre-filled from the
// account's own number on file either way, same reasoning as above.
document.getElementById('req-form-mobile').value = editReq ? (editReq.requester_mobile || STATE.telephone || '') : (STATE.telephone || '');
document.getElementById('req-form-refno-preview').textContent = editReq ? editReq.ref_no : '(assigned on save)';
document.getElementById('pv-form-refno-preview').textContent = editReq ? editReq.ref_no : '(assigned on save)';
syncPvDepartment();
loadReqBudgetCodes(deptSel.value, editReq ? editReq.budget_code_id : null).then(() => {
// If the requisition was saved with a typed Budget Output Code that
// doesn't correspond to a known BudgetCode record, still show it here
// (once loadReqBudgetCodes has finished resetting the field) so it
// isn't lost when re-opening the form.
if (editReq && !editReq.budget_code_id && editReq.budget_output_code_text) {
document.getElementById('req-form-budgetcode-search').value = editReq.budget_output_code_text;
}
});
// Clear the Attach Signature boxes and voucher-only fields for a fresh form,
// then re-show every "Attach Signature" button (a fresh form has nothing
// signed yet) before role-gating and requester pre-fill run below.
const allSigBoxIds = ['req-sig-requester','req-sig-hod','req-sig-treasurer','req-sig-clerk',
'pv-sig-controller','pv-sig-clerk','pv-sig-vb','pv-sig-verified','pv-sig-passed',
'pv-sig-payee','pv-sig-cashier','pv-sig-witness'];
allSigBoxIds.forEach(id => {
const b = document.getElementById(id); if (b) b.innerHTML = '';
const btn = document.getElementById(id + '-btn'); if (btn) btn.style.display = '';
const nameField = document.getElementById(id + '-name'); if (nameField) nameField.value = '';
});
// The requester's own signature is the one box that's actually recorded on
// the requisition itself — pre-fill it only when reopening a record that was
// already signed (i.e. editing an existing requisition). A brand-new
// requisition always starts with this box empty and its "Attach My
// Signature" button showing, even though the account already has a
// signature on file — the requester must explicitly click to attach it.
const requesterSigUrl = editReq ? editReq.requester_signature_url : null;
if (requesterSigUrl) {
document.getElementById('req-sig-requester').innerHTML = `<img src="${API_BASE}${requesterSigUrl}" alt="Signature"/>`;
const reqBtn = document.getElementById('req-sig-requester-btn'); if (reqBtn) reqBtn.style.display = 'none';
}
refreshSignatureButtonVisibility();
const voucher = (editReq && editReq.voucher_data) ? editReq.voucher_data : {};
document.getElementById('pv-form-budgetcode').value = voucher.budget_output_code || '';
document.getElementById('pv-form-pvref').value = voucher.pv_reference_no || '';
document.getElementById('pv-dr-to').value = voucher.dr_to || '';
document.getElementById('pv-cheque-no').value = voucher.cheque_no || '';
document.getElementById('pv-address').value = voucher.address || '';
document.getElementById('pv-authority').value = voucher.authority || '';
document.getElementById('pv-approved-vote').value = voucher.approved_vote || '';
document.getElementById('pv-account-no').value = voucher.account_no || '';
document.getElementById('pv-approved-estimate').value = voucher.approved_estimate || '';
document.getElementById('pv-instruction-no').value = voucher.cheque_instruction_no || '';
document.getElementById('pv-day').value = voucher.payment_day || '';
document.getElementById('pv-year').value = voucher.payment_month_year || '';
document.getElementById('pv-vb-date').value = voucher.entered_vote_book_date || '';
document.getElementById('pv-vb-dept').value = '';
document.getElementById('pv-verified-date').value = voucher.verified_by_date || '';
document.getElementById('pv-passed-date').value = voucher.passed_payment_date || '';
document.getElementById('pv-inter-clearance').value = voucher.inter_dept_clearance || '';
document.getElementById('pv-program-estimate').value = voucher.program_of_estimate || '';
document.getElementById('pv-sub-program').value = voucher.sub_program || '';
document.getElementById('pv-item').value = voucher.item || '';
// Reset the line items and paint the paper form right away so it appears
// on screen the instant the button is clicked.
if (!editReq) { resetReqLineItems(); document.getElementById('req-subject').value = ''; }
if (editReq) {
document.getElementById('req-subject').value = editReq.subject || '';
if (editReq.line_items && editReq.line_items.length) {
STATE.reqLineItems = editReq.line_items.map(li => ({ ...li, isHeader: li.qty == null && li.rate == null && !li.amount }));
} else {
resetReqLineItems();
}
}
renderReqLineItems();
openModal('modal-req');
// The requisition form's wide table needs room to breathe, so it opens
// maximized (fullscreen) by default rather than in its small centred
// size — the user can still tap the minimize button to shrink it back.
toggleModalMaximize('modal-req');
}
document.getElementById('new-req-btn').addEventListener('click', () => openRequisitionModal());
document.getElementById('req-form-department').addEventListener('change', () => { syncPvDepartment(); loadReqBudgetCodes(document.getElementById('req-form-department').value, null); });
function syncPvDepartment() {
const deptSel = document.getElementById('req-form-department');
const dept = STATE.departments.find(d => String(d.id) === String(deptSel.value));
const pvDept = document.getElementById('pv-form-department');
if (pvDept) pvDept.value = deptLabel(dept) || '—';
}
// Populates the Budget Output Code search results for the chosen
// department, and keeps "Activity Budget Limit" / "Activity Budget
// Balance" / "Budget Output Description" in sync with whichever code is
// picked — mirrors the paper form, where these are read straight off the
// selected budget output. The code field itself is free-typed (not a
// locked dropdown): the results list below it is just a lookup aid, and
// typing a code that isn't on file is still accepted as-is.
async function loadReqBudgetCodes(departmentId, selectedId) {
const searchEl = document.getElementById('req-form-budgetcode-search');
const hiddenEl = document.getElementById('req-form-budgetcode');
STATE.reqBudgetCodesForDept = [];
hiddenEl.value = '';
searchEl.value = '';
clearReqBudgetFields();
closeReqBudgetCodeResults();
if (!departmentId) return;
try {
const codes = await api(`/api/budget-codes?department_id=${departmentId}`);
STATE.reqBudgetCodesForDept = codes;
if (selectedId) {
const bc = codes.find(c => String(c.id) === String(selectedId));
if (bc) selectReqBudgetCode(bc);
}
} catch (e) { /* budget codes are optional on this form; fail quietly */ }
}
function clearReqBudgetFields() {
document.getElementById('req-form-budgetlimit').textContent = '—';
document.getElementById('req-form-budgetbalance').textContent = '—';
document.getElementById('req-form-budgetdesc').value = '';
autoGrowTextarea(document.getElementById('req-form-budgetdesc'));
}
function updateReqBudgetLimit() {
const hiddenEl = document.getElementById('req-form-budgetcode');
const limitEl = document.getElementById('req-form-budgetlimit');
const balanceEl = document.getElementById('req-form-budgetbalance');
const descEl = document.getElementById('req-form-budgetdesc');
const codes = STATE.reqBudgetCodesForDept || [];
const bc = codes.find(c => String(c.id) === String(hiddenEl.value));
limitEl.textContent = bc ? `UGX ${money(bc.allocated_amount)}` : '—';
balanceEl.textContent = bc ? `UGX ${money(bc.available_balance)}` : '—';
descEl.value = bc ? (bc.output_description || '') : '';
autoGrowTextarea(descEl);
}
// Selecting from the dropdown fills the code field with the code alone
// (no " — description" suffix) — the description has its own row below.
function selectReqBudgetCode(bc) {
document.getElementById('req-form-budgetcode').value = bc.id;
document.getElementById('req-form-budgetcode-search').value = bc.code;
updateReqBudgetLimit();
closeReqBudgetCodeResults();
}
// Typing a code and moving on without picking from the dropdown still
// tries to match it against the department's known codes (exact,
// case-insensitive) so the limit/balance/description auto-fill even
// without an explicit selection; a code with no match is simply kept as
// free text and the read-only fields stay blank.
function tryMatchTypedReqBudgetCode() {
const searchEl = document.getElementById('req-form-budgetcode-search');
const hiddenEl = document.getElementById('req-form-budgetcode');
if (hiddenEl.value) return; // already resolved to a known code
const typed = searchEl.value.trim().toLowerCase();
if (!typed) { clearReqBudgetFields(); return; }
const codes = STATE.reqBudgetCodesForDept || [];
const bc = codes.find(c => (c.code || '').toLowerCase() === typed);
if (bc) { selectReqBudgetCode(bc); } else { clearReqBudgetFields(); }
}
function closeReqBudgetCodeResults() {
const resultsEl = document.getElementById('req-form-budgetcode-results');
resultsEl.classList.remove('open');
resultsEl.innerHTML = '';
}
function renderReqBudgetCodeResults(query) {
const resultsEl = document.getElementById('req-form-budgetcode-results');
const codes = STATE.reqBudgetCodesForDept || [];
const q = (query || '').trim().toLowerCase();
const matches = q
? codes.filter(c => (c.code || '').toLowerCase().includes(q) || (c.output_description || '').toLowerCase().includes(q))
: codes;
if (!codes.length) {
resultsEl.innerHTML = '<div class="rf-bc-empty">Select a Department first, or type a Budget Output Code directly.</div>';
} else if (!matches.length) {
resultsEl.innerHTML = '<div class="rf-bc-empty">No matching budget output code on file — you can still type it in directly.</div>';
} else {
// Dropdown lists the Budget Output Code only — the description has its
// own dedicated row on the form and should not be repeated here.
resultsEl.innerHTML = matches.slice(0, 30).map(c =>
`<div class="rf-bc-opt" data-bc-id="${c.id}"><span class="rf-bc-code">${escapeHtml(c.code)}</span></div>`
).join('');
resultsEl.querySelectorAll('.rf-bc-opt').forEach(opt => {
opt.addEventListener('mousedown', (e) => {
e.preventDefault();
const bc = (STATE.reqBudgetCodesForDept || []).find(c => String(c.id) === opt.dataset.bcId);
if (bc) selectReqBudgetCode(bc);
});
});
}
resultsEl.classList.add('open');
}
function wireReqBudgetCodeSearch() {
const searchEl = document.getElementById('req-form-budgetcode-search');
const hiddenEl = document.getElementById('req-form-budgetcode');
searchEl.addEventListener('input', () => {
// Typing again after a selection was made clears the selected id until
// a fresh choice is made (or the typed text is re-matched on blur), so
// a half-edited search string can't be silently submitted as if it
// were still the old pick.
hiddenEl.value = '';
clearReqBudgetFields();
renderReqBudgetCodeResults(searchEl.value);
});
searchEl.addEventListener('focus', () => renderReqBudgetCodeResults(searchEl.value));
searchEl.addEventListener('blur', () => { tryMatchTypedReqBudgetCode(); setTimeout(closeReqBudgetCodeResults, 120); });
}
wireReqBudgetCodeSearch();
async function submitNewRequisition(submitNow) {
// In case the person is still focused in the Budget Output Code field
// (or typed a code and clicked straight to Submit without tabbing away),
// resolve it against known codes one more time before reading its value.
tryMatchTypedReqBudgetCode();
const subject = document.getElementById('req-subject').value.trim();
const departmentId = document.getElementById('req-form-department').value;
const lineItems = STATE.reqLineItems
.filter(li => li.description && li.description.trim() !== '')
.map(li => ({
item_no: li.item_no,
description: li.description.trim(),
units: li.units ? li.units.trim() : null,
qty: li.qty,
rate: li.rate,
amount: Number(li.amount) || 0,
}));
const total = lineItems.reduce((s, li) => s + (Number(li.amount) || 0), 0);
const voucher = {
budget_output_code: document.getElementById('pv-form-budgetcode').value.trim() || null,
pv_reference_no: document.getElementById('pv-form-pvref').value.trim() || null,
dr_to: document.getElementById('pv-dr-to').value.trim() || null,
cheque_no: document.getElementById('pv-cheque-no').value.trim() || null,
address: document.getElementById('pv-address').value.trim() || null,
authority: document.getElementById('pv-authority').value.trim() || null,
approved_vote: document.getElementById('pv-approved-vote').value.trim() || null,
account_no: document.getElementById('pv-account-no').value.trim() || null,
approved_estimate: document.getElementById('pv-approved-estimate').value.trim() || null,
cheque_instruction_no: document.getElementById('pv-instruction-no').value.trim() || null,
payment_day: document.getElementById('pv-day').value.trim() || null,
payment_month_year: document.getElementById('pv-year').value.trim() || null,
entered_vote_book_date: document.getElementById('pv-vb-date').value.trim() || null,
verified_by_date: document.getElementById('pv-verified-date').value.trim() || null,
passed_payment_date: document.getElementById('pv-passed-date').value.trim() || null,
inter_dept_clearance: document.getElementById('pv-inter-clearance').value.trim() || null,
program_of_estimate: document.getElementById('pv-program-estimate').value.trim() || null,
sub_program: document.getElementById('pv-sub-program').value.trim() || null,
item: document.getElementById('pv-item').value.trim() || null,
};
const payload = {
department_id: departmentId ? Number(departmentId) : null,
budget_code_id: document.getElementById('req-form-budgetcode').value ? Number(document.getElementById('req-form-budgetcode').value) : null,
budget_output_code_text: document.getElementById('req-form-budgetcode-search').value.trim() || null,
subject,
financial_year: document.getElementById('req-form-fy').value || null,
quarter: document.getElementById('req-form-quarter').value || null,
requester_name: document.getElementById('req-form-names').value.trim() || null,
requester_position: document.getElementById('req-form-position').value.trim() || null,
requester_mobile: document.getElementById('req-form-mobile').value.trim() || null,
line_items: lineItems,
voucher,
};
const requisitionerName = document.getElementById('req-form-names').value.trim();
if (!payload.department_id || !requisitionerName || !subject || total <= 0) {
toast('Please select a department, enter the requisitioner\'s name, complete the subject and add at least one priced line item', 'error'); return;
}
try {
if (STATE.editingRequisitionId) {
const id = STATE.editingRequisitionId;
await api(`/api/requisitions/${id}`, { method: 'PATCH', body: JSON.stringify(payload) });
if (submitNow) {
await api(`/api/requisitions/${id}/submit`, { method: 'POST' });
}
toast(submitNow ? 'Requisition updated and submitted for approval' : 'Requisition changes saved', 'success');
} else {
await api(`/api/requisitions?submit=${submitNow}`, { method: 'POST', body: JSON.stringify(payload) });
toast(submitNow ? 'Requisition submitted for approval' : 'Requisition saved as draft', 'success');
}
closeModal('modal-req');
loadRequisitions();
} catch (e) { toast(e.message, 'error'); }
}
document.getElementById('req-route-hod').addEventListener('click', () => submitNewRequisition(true));
document.getElementById('req-route-hod-mid').addEventListener('click', () => submitNewRequisition(true));
// Print the form as currently filled in, without needing to save first —
// builds a lightweight object shaped like the saved-requisition payload
// that renderPrintFormHtml() already knows how to render.
document.getElementById('req-print-draft').addEventListener('click', () => {
tryMatchTypedReqBudgetCode();
const deptSel = document.getElementById('req-form-department');
const dept = STATE.departments.find(d => String(d.id) === deptSel.value);
const bcId = document.getElementById('req-form-budgetcode').value;
const bc = (STATE.reqBudgetCodesForDept || []).find(c => String(c.id) === String(bcId));
const draft = {
ref_no: document.getElementById('req-form-refno-preview').textContent || '(unsaved draft)',
created_at: new Date().toISOString(),
department_name: deptLabel(dept) || '—',
requester_name: document.getElementById('req-form-names').value.trim() || STATE.name || '—',
requester_mobile: document.getElementById('req-form-mobile').value.trim() || null,
requester_position: document.getElementById('req-form-position').value.trim() || null,
requester_signature_url: document.getElementById('req-sig-requester').innerHTML.trim() ? STATE.signatureUrl : null,
budget_code: bc ? bc.code : (document.getElementById('req-form-budgetcode-search').value.trim() || null),
budget_output: bc ? bc.output_description : document.getElementById('req-form-budgetdesc').value,
activity_budget_limit: bc ? bc.allocated_amount : null,
activity_budget_balance: bc ? bc.available_balance : null,
subject: document.getElementById('req-subject').value.trim(),
line_items: STATE.reqLineItems.filter(li => li.description && li.description.trim() !== ''),
voucher_data: {
budget_output_code: document.getElementById('pv-form-budgetcode').value.trim() || null,
dr_to: document.getElementById('pv-dr-to').value.trim() || null,
address: document.getElementById('pv-address').value.trim() || null,
cheque_no: document.getElementById('pv-cheque-no').value.trim() || null,
},
approvals: [],
};
document.getElementById('pf-body').innerHTML = renderPrintFormHtml(draft);
openModal('modal-print-form');
});
document.getElementById('req-search').addEventListener('input', debounce(loadRequisitions, 300));
document.getElementById('req-status-filter').addEventListener('change', loadRequisitions);
async function loadRequisitions() {
const tbody = document.getElementById('req-table-body');
tbody.innerHTML = '<tr><td colspan="9" class="loading-row"><span class="spinner spinner-dark"></span></td></tr>';
const status = document.getElementById('req-status-filter').value;
const search = document.getElementById('req-search').value.trim().toLowerCase();
try {
let path = '/api/requisitions';
if (status) path += `?status=${status}`;
let items = await api(path);
if (search) items = items.filter(r => (r.ref_no + ' ' + (r.subject||r.activity_details||'')).toLowerCase().includes(search));
if (items.length === 0) { tbody.innerHTML = '<tr><td colspan="9"><div class="empty-state">No requisitions found.</div></td></tr>'; return; }
STATE_REQUISITIONS_CACHE = items;
tbody.innerHTML = items.map(r => {
const isOwnerOrAdmin = (r.requester_id == STATE.userId || STATE.role === 'admin');
const isEditable = isOwnerOrAdmin && (r.status === 'draft' || r.status === 'returned');
return `
<tr>
<td class="mono">${r.ref_no}</td>
<td>${escapeHtml(r.requester_name || '—')}</td>
<td>${escapeHtml(r.department_name || '—')}</td>
<td class="wrap">${escapeHtml(r.subject || r.activity_details || '—')}</td>
<td class="num mono">${money(r.amount_requested)}</td>
<td><span class="pill pill-${r.status}">${statusLabel(r.status)}</span></td>
<td>${escapeHtml(statusLabel(r.current_stage))}</td>
<td>${fmtDate(r.created_at)}</td>
<td style="white-space:nowrap;">
<button class="btn btn-ghost" style="padding:6px 10px;" onclick="viewRequisition(${r.id})">View</button>
${(r.accountability && r.accountability.status !== 'verified' && isOwnerOrAdmin) ? `<button class="btn btn-gold" style="padding:6px 10px; margin-left:6px;" onclick="openUploadModal(${r.id})">Upload</button>` : ''}
${isEditable ? `<button class="btn btn-ghost" style="padding:6px 10px; margin-left:6px;" onclick="editRequisition(${r.id})">Edit</button>` : ''}
${isEditable ? `<button class="btn btn-danger" style="padding:6px 10px; margin-left:6px;" onclick="deleteRequisition(${r.id})">Delete</button>` : ''}
</td>
</tr>`;
}).join('');
} catch (e) { tbody.innerHTML = `<tr><td colspan="9"><div class="empty-state">${escapeHtml(e.message)}</div></td></tr>`; }
}
let STATE_REQUISITIONS_CACHE = [];
async function editRequisition(id) {
try {
const r = await api(`/api/requisitions/${id}`);
openRequisitionModal(r);
} catch (e) { toast(e.message, 'error'); }
}
async function deleteRequisition(id) {
const r = STATE_REQUISITIONS_CACHE.find(x => x.id === id);
if (!confirm(`Delete requisition ${r ? r.ref_no : id}? This cannot be undone.`)) return;
try {
await api(`/api/requisitions/${id}`, { method: 'DELETE' });
toast('Requisition deleted', 'success');
loadRequisitions();
} catch (e) { toast(e.message, 'error'); }
}
async function viewRequisition(id) {
STATE.currentReqId = id;
const body = document.getElementById('rd-body');
const foot = document.getElementById('rd-foot');
body.innerHTML = '<div class="loading-row"><span class="spinner spinner-dark"></span></div>';
foot.innerHTML = '';
openModal('modal-req-detail');
// This view also has a wide paper-form layout, so open it maximized
// (fullscreen) by default, same as the New Requisition form — the
// minimize button lets the user shrink it back down.
toggleModalMaximize('modal-req-detail');
try {
const r = await api(`/api/requisitions/${id}`);
document.getElementById('rd-title').textContent = r.ref_no;
// Show the same filled-in paper-form view used on the Requisition tab
// (Funds Requisition Form + Cheque Payment Voucher, read-only with the
// saved data and signatures) rather than a separate summary layout, so
// "View" always mirrors what was actually filled and submitted.
body.innerHTML = `
<div style="margin-bottom:4px;"><span class="pill pill-${r.status}">${statusLabel(r.status)}</span></div>
${renderFilledRequisitionFormHtml(r)}
${r.accountability ? `<div class="divider"></div><div class="kicker">Accountability</div><div style="margin-top:8px;"><span class="pill pill-${r.accountability.status}">${statusLabel(r.accountability.status)}</span><div class="tl-meta" style="margin-top:6px;">${escapeHtml(r.accountability.remarks||'No remarks yet')}</div>${(r.accountability.status !== 'verified' && (r.requester_id == STATE.userId || STATE.role === 'admin')) ? '<div class="help-text" style="margin-top:6px;">Upload the Payment Voucher, Official Receipts, Signed Attendance Sheets and any other supporting documents for this requisition.</div>' : ''}</div>` : ''}
`;
let footHtml = `<button class="btn btn-ghost" onclick="openPrintForm(${r.id})"><svg class="btn-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6 9V3H18V9" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><rect x="4" y="9" width="16" height="8" rx="1.5" stroke="currentColor" stroke-width="1.8"/><rect x="7" y="14" width="10" height="6" stroke="currentColor" stroke-width="1.8"/></svg>Print Requisition Form</button>`;
if (r.status === 'draft' && (r.requester_id == STATE.userId || STATE.role === 'admin')) {
footHtml += `<button class="btn btn-primary" onclick="submitExisting(${r.id})">Submit for Approval</button>`;
}
const stageRole = { hod: 'hod', treasurer: 'treasurer', clerk: 'clerk' }[r.current_stage];
if (stageRole && (STATE.role === stageRole || STATE.role === 'admin')) {
footHtml += `
<button class="btn btn-danger" onclick="actOnRequisition(${r.id}, 'reject')">Reject</button>
<button class="btn btn-ghost" onclick="actOnRequisition(${r.id}, 'return')">Return for Correction</button>
<button class="btn btn-primary" onclick="actOnRequisition(${r.id}, 'approve')">Approve</button>`;
}
const canUpload = r.accountability && r.accountability.status !== 'verified' && (r.requester_id == STATE.userId || STATE.role === 'admin');
if (canUpload) {
footHtml += `<button class="btn btn-gold" onclick="openUploadModal(${r.id})">Upload Accountability Document</button>`;
}
if (r.accountability && (STATE.role === 'auditor' || STATE.role === 'admin')) {
footHtml += `<button class="btn btn-primary" onclick="closeModal('modal-req-detail'); openDocumentViewer(${r.id});">Review Documents &amp; Verify</button>`;
}
foot.innerHTML = footHtml;
} catch (e) { body.innerHTML = `<div class="empty-state">${escapeHtml(e.message)}</div>`; }
}
async function submitExisting(id) {
try { await api(`/api/requisitions/${id}/submit`, { method: 'POST' }); toast('Requisition submitted', 'success'); closeModal('modal-req-detail'); loadRequisitions(); }
catch (e) { toast(e.message, 'error'); }
}
async function actOnRequisition(id, action) {
let comments = '';
if (action !== 'approve') {
comments = prompt(`Please provide comments for this ${action === 'reject' ? 'rejection' : 'return'}:`) || '';
}
try {
await api(`/api/requisitions/${id}/approve-action`, { method: 'POST', body: JSON.stringify({ action, comments }) });
toast(`Requisition ${action}d`, action === 'approve' ? 'success' : 'info');
closeModal('modal-req-detail');
loadApprovals(); loadRequisitions(); loadDashboard();
} catch (e) { toast(e.message, 'error'); }
}
// ---- Printable Requisition Form (mirrors the Council's paper layout) -------
async function openPrintForm(reqId) {
const body = document.getElementById('pf-body');
body.innerHTML = '<div class="loading-row"><span class="spinner spinner-dark"></span></div>';
openModal('modal-print-form');
try {
const r = await api(`/api/requisitions/${reqId}`);
body.innerHTML = renderPrintFormHtml(r);
} catch (e) { body.innerHTML = `<div class="empty-state">${escapeHtml(e.message)}</div>`; }
}
// Shared computation used by both the read-only "View" form and the
// printable form: line-item rows (both the Requisition Form grid and the
// mirrored Payment Voucher grid), running totals, amount-in-words, and
// every signature image URL resolved from the approval trail.
function computeReqFormParts(r) {
const items = r.line_items || [];
const voucher = r.voucher_data || {};
let rowsHtml = '';
let pvRowsHtml = '';
let lastNo = null;
let sectionSum = 0;
let grandTotal = 0;
const flushSection = () => {
if (lastNo !== null) {
rowsHtml += `<tr class="rf-subtotal"><td colspan="5" style="text-align:right;">Sub Total</td><td class="num">${money(sectionSum)}</td></tr>`;
}
};
const submissionDate = fmtDate(r.created_at);
items.forEach((li, i) => {
if (li.item_no !== lastNo) {
flushSection();
lastNo = li.item_no;
sectionSum = 0;
}
const isHeaderRow = (li.qty == null && li.rate == null && (!li.amount || Number(li.amount) === 0));
const showNo = (i === 0 || items[i-1].item_no !== li.item_no);
rowsHtml += `<tr class="${isHeaderRow ? 'rf-section-head' : ''}">
<td>${showNo ? 'S/N ' + String(li.item_no).padStart(2,'0') : ''}</td>
<td class="wrap">${escapeHtml(li.description)}</td>
<td>${escapeHtml(li.units || '')}</td>
<td class="num">${li.qty ? money(li.qty) : ''}</td>
<td class="num">${li.rate ? money(li.rate) : ''}</td>
<td class="num">${li.amount ? money(li.amount) : ''}</td>
</tr>`;
if (!isHeaderRow) {
pvRowsHtml += `<tr>
<td>${showNo ? escapeHtml(submissionDate) : ''}</td>
<td class="wrap">${escapeHtml(li.description)}</td>
<td>${escapeHtml(li.ledger_folio || '')}</td>
<td>${escapeHtml(li.charge_date || '')}</td>
<td class="num">${li.amount ? money(li.amount) : ''}</td>
</tr>`;
}
sectionSum += Number(li.amount) || 0;
grandTotal += Number(li.amount) || 0;
});
flushSection();
const subject = r.subject || r.activity_details || '';
const words = numberToWordsUGX(grandTotal);
const requesterSigUrl = r.requester_signature_url || null;
const hodSigUrl = findStageSignatureUrl(r, 'hod');
const treasurerSigUrl = findStageSignatureUrl(r, 'treasurer');
const clerkSigUrl = findStageSignatureUrl(r, 'clerk');
// Authorizer's name from the system for the space between the dotted
// signature line and the role label — resolved from the same approval
// record as their signature image.
const hodName = findStageActorName(r, 'hod');
const treasurerName = findStageActorName(r, 'treasurer');
const clerkName = findStageActorName(r, 'clerk');
const sigImg = (url) => url ? `<img src="${API_BASE}${url}" alt="Signature" />` : '';
const dots = (text) => `<span class="rf-dots">${escapeHtml(text || '').padEnd(1,'\u00A0') || '&nbsp;'}</span>`;
return { items, voucher, rowsHtml, pvRowsHtml, grandTotal, subject, words, submissionDate, requesterSigUrl, hodSigUrl, treasurerSigUrl, clerkSigUrl, hodName, treasurerName, clerkName, sigImg, dots };
}
function findStageSignatureUrl(r, stage) {
const approvals = r.approvals || [];
for (let i = approvals.length - 1; i >= 0; i--) {
const a = approvals[i];
if (a.stage === stage && a.action === 'approve' && a.actor_signature_url) {
return a.actor_signature_url;
}
}
return null;
}
function findStageActorName(r, stage) {
const approvals = r.approvals || [];
for (let i = approvals.length - 1; i >= 0; i--) {
const a = approvals[i];
if (a.stage === stage && a.action === 'approve' && a.actor) {
return a.actor;
}
}
return null;
}
// The Cheque Payment Voucher half of the form — identical markup whether
// it's reached via "View" or via "Print", since both mirror the same
// paper document filled in together with the Requisition Form.
function renderPvFormHtml(r, parts) {
const { voucher, pvRowsHtml, grandTotal, words, hodSigUrl, clerkSigUrl, hodName, clerkName, sigImg, dots } = parts;
return `
<div class="pv-form">
<img src="header.jpg" alt="Ntoroko District Local Government — Karugutu Town Council" class="rf-header-img"/>
<div class="req-form-header"><div class="rf-title">Cheque Payment Voucher</div></div>
<div class="rf-refno">Voucher No. <span class="mono">${escapeHtml(r.ref_no)}</span></div>
<table class="req-form-meta-table">
<tr>
<td style="width:50%;"><strong>Department:</strong><span class="rf-fill">${escapeHtml(r.department_name || '—')}</span></td>
<td style="width:50%;"><strong>Cheque No:</strong><span class="rf-fill">${escapeHtml(voucher.cheque_no || '—')}</span></td>
</tr>
<tr>
<td><strong>Budget Output Code:</strong><span class="rf-fill">${escapeHtml(voucher.budget_output_code || '—')}</span></td>
<td><strong>Payment Voucher Reference No:</strong><span class="rf-fill">${escapeHtml(voucher.pv_reference_no || '—')}</span></td>
</tr>
<tr>
<td><strong>Dr. To:</strong><span class="rf-fill">${escapeHtml(voucher.dr_to || '—')}</span></td>
<td><strong>Address:</strong><span class="rf-fill">${escapeHtml(voucher.address || '—')}</span></td>
</tr>
</table>
<table class="req-form-table">
<thead><tr><th style="width:10%;">Date</th><th>Detailed description of service or article</th><th colspan="2" style="width:20%; text-align:center;">Taken on charge expenditure</th><th class="num" style="width:14%;">Amount (Shs)</th></tr>
<tr><th></th><th></th><th style="width:10%;">Ledger Folio</th><th style="width:10%;">Date</th><th class="num"></th></tr>
</thead>
<tbody>
${pvRowsHtml || '<tr><td colspan="5" style="text-align:center; color:#777;">No line items recorded</td></tr>'}
<tr class="rf-grand"><td colspan="4" style="text-align:right;">TOTAL</td><td class="num">UGX ${money(grandTotal)}</td></tr>
</tbody>
</table>
<div class="pv-certify">
<div class="pv-plain-line"><strong>Authority:</strong>${dots(voucher.authority)}<strong>Total</strong>${dots('UGX ' + money(grandTotal))}</div>
<div class="pv-plain-line"><strong>Approved vote</strong>${dots(voucher.approved_vote)}<strong>Account No.</strong>${dots(voucher.account_no)}</div>
<div class="pv-plain-line"><strong>approved Estimate</strong>${dots(voucher.approved_estimate)}<strong>Cheque payment instruction No</strong>${dots(voucher.cheque_instruction_no)}</div>
<p style="margin-top:10px;"><strong>I HEREBY CERTIFY</strong> that the above amount is correct and was incurred under the authority quoted, that the above services has been duly and properly performed / supplies have been received in good condition: that the payment price charge is in accordance with regulations the terms of contract or agreement which are fair and reasonable and that the above expenditure of Shs (in words) ${dots(words)} will not cause an excess over the provision made under the authority quoted on this voucher or under programme/sub-programme shown below:</p>
<p><strong>I FURTHER CERTIFY</strong> that the stores that have been taken on charge, or are expendable, as indicated above.</p>
</div>
<div class="req-form-signatures" style="grid-template-columns:repeat(2,1fr);">
<div><div class="sig-role">Signature,</div><div class="sig-line">${sigImg(hodSigUrl)}</div><div class="sig-name">${escapeHtml(hodName || '')}</div><div class="sig-label">Vote Controller</div></div>
<div><div class="sig-role">Signature,</div><div class="sig-line">${sigImg(clerkSigUrl)}</div><div class="sig-name">${escapeHtml(clerkName || '')}</div><div class="sig-label">Town Clerk</div></div>
</div>
<div class="pv-received-line" style="margin-top:14px;">
Received / paid this Day ${dots(voucher.payment_day)} ................. 20${dots(voucher.payment_month_year)} in payment of the above account he Sum of shillings ${dots(words)} (in words).
</div>
<table class="pv-block-table">
<tr>
<td style="width:34%;">
<strong>Entered In Vote Book</strong>
Date: ${dots(voucher.entered_vote_book_date)}<br/>
<div style="margin-top:16px;">Signature: __________________</div>
</td>
<td style="width:33%;">
<strong>Verified by</strong>
Date: ${dots(voucher.verified_by_date)}<br/>
<div style="margin-top:16px;">Signature: __________________</div>
</td>
<td style="width:33%;">
<strong>Passed Payment for (HoF)</strong>
Shs: UGX ${money(grandTotal)}<br/>
Date: ${dots(voucher.passed_payment_date)}<br/>
<div style="margin-top:6px;">Signature: __________________</div>
</td>
</tr>
</table>
<table class="pv-block-table">
<tr>
<td colspan="2"><strong>Signature of payee</strong><div style="margin-top:16px;">__________________</div></td>
</tr>
<tr>
<td><strong>Signature of witness to payment</strong><div style="margin-top:16px;">__________________</div></td>
<td><strong>Signature of paying officer (cashier)</strong><div style="margin-top:16px;">__________________</div></td>
</tr>
</table>
<table class="pv-block-table">
<tr>
<td style="width:60%;">
<strong>Inter-departmental Clearance:</strong> ${escapeHtml(voucher.inter_dept_clearance || '—')}<br/>
<strong>Program of Estimate:</strong> ${escapeHtml(voucher.program_of_estimate || '—')}<br/>
<strong>Sub Program:</strong> ${escapeHtml(voucher.sub_program || '—')}<br/>
<strong>Item:</strong> ${escapeHtml(voucher.item || '—')}
</td>
<td style="width:40%; text-align:right; vertical-align:bottom;">
<strong>Total Shs</strong>
<div style="font-weight:700; font-size:15px;">UGX ${money(grandTotal)}</div>
</td>
</tr>
</table>
</div>
`;
}
// ---- Print form (mirrors the Council's simplified paper layout exactly) --
function renderPrintFormHtml(r) {
const parts = computeReqFormParts(r);
const { rowsHtml, grandTotal, subject, words, submissionDate, requesterSigUrl, hodSigUrl, treasurerSigUrl, clerkSigUrl, hodName, treasurerName, clerkName, sigImg, dots } = parts;
const budgetRow = `
<tr>
<td><strong>Budget Output Code:</strong><span class="rf-fill">${escapeHtml(r.budget_code || '—')}</span></td>
<td><strong>Activity Budget Limit:</strong><span class="rf-fill">${r.activity_budget_limit != null ? 'UGX ' + money(r.activity_budget_limit) : '—'}</span></td>
<td><strong>Activity Budget Balance:</strong><span class="rf-fill">${r.activity_budget_balance != null ? 'UGX ' + money(r.activity_budget_balance) : '—'}</span></td>
</tr>`;
return `
<div class="req-form-paper">
<img src="header.jpg" alt="Ntoroko District Local Government — Karugutu Town Council" class="rf-header-img"/>
<div class="req-form-header"><div class="rf-title">Funds Requisition Form</div></div>
<div class="rf-refno">No. <span class="mono">${escapeHtml(r.ref_no)}</span></div>
<table class="req-form-meta-table">
<tr>
<td style="width:50%;"><strong>Department:</strong><span class="rf-fill">${escapeHtml(r.department_name || '—')}</span></td>
<td style="width:50%;"><strong>Date of Submission:</strong><span class="rf-fill">${submissionDate}</span></td>
</tr>
<tr>
<td><strong>Names:</strong><span class="rf-fill">${escapeHtml(r.requester_name || '—')}</span></td>
<td><strong>Mob. No.:</strong><span class="rf-fill">${escapeHtml(r.requester_mobile || '—')}</span></td>
<td><strong>Requisitioner Signature:</strong><span class="rf-fill">${sigImg(requesterSigUrl)}</span></td>
</tr>
${budgetRow}
</table>
<div class="req-form-subject"><strong>Activity Description(Subject):</strong>${dots(subject)}</div>
<table class="req-form-table">
<thead><tr><th style="width:13%;">Sub Activity<br>S/No.</th><th>Description</th><th style="width:8%;">Units</th><th style="width:8%;">Qty</th><th style="width:11%;">Rate</th><th class="num" style="width:13%;">Amount</th></tr></thead>
<tbody>
${rowsHtml || '<tr><td colspan="6" style="text-align:center; color:#777;">No line items recorded</td></tr>'}
<tr class="rf-grand"><td colspan="5" style="text-align:right;">GRAND TOTAL</td><td class="num">${money(grandTotal)}</td></tr>
</tbody>
</table>
<div class="req-form-words"><strong>Amount in words:</strong>${dots(words)}</div>
<div class="req-form-signatures">
<div><div class="sig-role">Recommended by,</div><div class="sig-line">${sigImg(hodSigUrl)}</div><div class="sig-name">${escapeHtml(hodName || '')}</div><div class="sig-label">Head of Department</div></div>
<div><div class="sig-role">Checked and approved by,</div><div class="sig-line">${sigImg(treasurerSigUrl)}</div><div class="sig-name">${escapeHtml(treasurerName || '')}</div><div class="sig-label">Senior Treasurer</div></div>
<div><div class="sig-role">Authorised by</div><div class="sig-line">${sigImg(clerkSigUrl)}</div><div class="sig-name">${escapeHtml(clerkName || '')}</div><div class="sig-label">Town Clerk</div></div>
</div>
</div>
${renderPvFormHtml(r, parts)}
`;
}
// ---- "View" form — mirrors the full digital entry form (New/Edit
// Requisition modal) field-for-field, read-only, filled with the saved
// data: System User Name / Email / Role, Financial Year / Quarter / Date,
// Department / Position, Requisitioner / Mobile / Signature, Budget
// Output Code / Limit / Balance / Description, Subject, line items,
// amount in words, approval signatures, and the same Payment Voucher
// section — so "View" always shows exactly what was filled under the
// Requisition tab, not a shortened summary.
function renderFilledRequisitionFormHtml(r) {
const parts = computeReqFormParts(r);
const { rowsHtml, grandTotal, subject, words, submissionDate, requesterSigUrl, hodSigUrl, treasurerSigUrl, clerkSigUrl, hodName, treasurerName, clerkName, sigImg, dots } = parts;
const roleLabel = r.requester_role ? statusLabel(r.requester_role) : '—';
return `
<div class="req-form-paper">
<img src="header.jpg" alt="Ntoroko District Local Government — Karugutu Town Council" class="rf-header-img"/>
<div class="req-form-header"><div class="rf-title">Funds Requisition Form</div></div>
<div class="rf-refno">Ref No. <span class="mono">${escapeHtml(r.ref_no)}</span></div>
<table class="req-form-meta-table">
<tr>
<td style="width:36%;"><strong>System User Name:</strong><span class="rf-fill">${escapeHtml(r.requester_account_name || '—')}</span></td>
<td style="width:32%;"><strong>Email:</strong><span class="rf-fill">${escapeHtml(r.requester_email || '—')}</span></td>
<td style="width:32%;"><strong>Role:</strong><span class="rf-fill" style="text-transform:capitalize;">${escapeHtml(roleLabel)}</span></td>
</tr>
<tr>
<td style="width:33.33%;"><strong>Financial Year:</strong><span class="rf-fill">${escapeHtml(r.financial_year || '—')}</span></td>
<td style="width:33.33%;"><strong>Quarter:</strong><span class="rf-fill">${escapeHtml(r.quarter || '—')}</span></td>
<td style="width:33.34%;"><strong>Date:</strong><span class="rf-fill">${submissionDate}</span></td>
</tr>
<tr>
<td colspan="3" style="width:100%;"><strong>Department:</strong><span class="rf-fill">${escapeHtml(r.department_name || '—')}</span></td>
</tr>
<tr>
<td style="width:33.33%;"><strong>Requisitioner:</strong><span class="rf-fill">${escapeHtml(r.requester_name || '—')}</span></td>
<td style="width:33.33%;"><strong>Mob. No.:</strong><span class="rf-fill">${escapeHtml(r.requester_mobile || '—')}</span></td>
<td style="width:33.34%;"><strong>Position:</strong><span class="rf-fill">${escapeHtml(r.requester_position || '—')}</span></td>
</tr>
<tr>
<td colspan="3"><strong>Requisitioner Signature:</strong><span class="rf-fill">${sigImg(requesterSigUrl)}</span></td>
</tr>
<tr>
<td style="width:33.33%;"><strong>Budget Output Code:</strong><span class="rf-fill">${escapeHtml(r.budget_code || '—')}</span></td>
<td style="width:33.33%;"><strong>Activity Budget Limit:</strong><span class="rf-fill">${r.activity_budget_limit != null ? 'UGX ' + money(r.activity_budget_limit) : '—'}</span></td>
<td style="width:33.34%;"><strong>Activity Budget Balance:</strong><span class="rf-fill">${r.activity_budget_balance != null ? 'UGX ' + money(r.activity_budget_balance) : '—'}</span></td>
</tr>
<tr>
<td colspan="3"><strong>Budget Output Description:</strong><span class="rf-fill">${escapeHtml(r.budget_output || '—')}</span></td>
</tr>
<tr>
<td colspan="3"><strong>Activity Description(Subject):</strong><span class="rf-fill">${escapeHtml(subject || '—')}</span></td>
</tr>
</table>
<table class="req-form-table">
<thead><tr><th style="width:13%;">Sub Activity<br>S/No.</th><th>Description</th><th style="width:8%;">Units</th><th style="width:8%;">Qty</th><th style="width:11%;">Rate</th><th class="num" style="width:13%;">Amount</th></tr></thead>
<tbody>
${rowsHtml || '<tr><td colspan="6" style="text-align:center; color:#777;">No line items recorded</td></tr>'}
<tr class="rf-grand"><td colspan="5" style="text-align:right;">GRAND TOTAL</td><td class="num">${money(grandTotal)}</td></tr>
</tbody>
</table>
<div class="req-form-words"><strong>Amount in words:</strong>${dots(words)}</div>
<div class="req-form-signatures">
<div><div class="sig-role">Recommended by,</div><div class="sig-line">${sigImg(hodSigUrl)}</div><div class="sig-name">${escapeHtml(hodName || '')}</div><div class="sig-label">Head of Department</div></div>
<div><div class="sig-role">Checked and approved by,</div><div class="sig-line">${sigImg(treasurerSigUrl)}</div><div class="sig-name">${escapeHtml(treasurerName || '')}</div><div class="sig-label">Senior Treasurer</div></div>
<div><div class="sig-role">Authorised by</div><div class="sig-line">${sigImg(clerkSigUrl)}</div><div class="sig-name">${escapeHtml(clerkName || '')}</div><div class="sig-label">Town Clerk</div></div>
</div>
</div>
${renderPvFormHtml(r, parts)}
`;
}
// ---- Approvals ------------------------------------------------------------------
async function loadApprovals() {
const tbody = document.getElementById('approval-table-body');
tbody.innerHTML = '<tr><td colspan="8" class="loading-row"><span class="spinner spinner-dark"></span></td></tr>';
try {
const items = await api('/api/approvals/pending');
if (items.length === 0) { tbody.innerHTML = '<tr><td colspan="8"><div class="empty-state">Nothing awaiting your approval right now.</div></td></tr>'; return; }
tbody.innerHTML = items.map(r => {
const bc = STATE.budgetCodes.find(c => c.id === r.budget_code_id);
return `
<tr>
<td class="mono">${r.ref_no}</td>
<td>${escapeHtml(r.requester_name||'—')}</td>
<td>${escapeHtml(r.department_name||'—')}</td>
<td class="wrap">${escapeHtml(r.subject || r.activity_details || '—')}</td>
<td class="num mono">${money(r.amount_requested)}</td>
<td class="num mono">${bc ? money(bc.available_balance) : '—'}</td>
<td>${escapeHtml(statusLabel(r.current_stage))}</td>
<td><button class="btn btn-primary" style="padding:6px 10px;" onclick="viewRequisition(${r.id})">Review</button></td>
</tr>`;
}).join('');
} catch (e) { tbody.innerHTML = `<tr><td colspan="8"><div class="empty-state">${escapeHtml(e.message)}</div></td></tr>`; }
}
// ---- Accountability --------------------------------------------------------------
async function loadAccountability() {
const tbody = document.getElementById('acc-table-body');
tbody.innerHTML = '<tr><td colspan="6" class="loading-row"><span class="spinner spinner-dark"></span></td></tr>';
try {
const items = await api('/api/accountability/pending');
if (items.length === 0) { tbody.innerHTML = '<tr><td colspan="6"><div class="empty-state">No accountability records pending review.</div></td></tr>'; return; }
tbody.innerHTML = items.map(r => `
<tr>
<td class="mono">${r.ref_no}</td>
<td>${escapeHtml(r.department_name||'—')}</td>
<td class="num mono">${money(r.amount_requested)}</td>
<td>${r.documents.length} file(s)</td>
<td><span class="pill pill-${r.accountability ? r.accountability.status : 'pending'}">${statusLabel(r.accountability ? r.accountability.status : 'pending')}</span></td>
<td><button class="btn btn-primary" style="padding:6px 10px;" onclick="openDocumentViewer(${r.id})">Review</button></td>
</tr>`).join('');
} catch (e) { tbody.innerHTML = `<tr><td colspan="6"><div class="empty-state">${escapeHtml(e.message)}</div></td></tr>`; }
}
// ---- Single-page document viewer (Auditor review) --------------------------------
async function openDocumentViewer(reqId) {
STATE.currentReqId = reqId;
const body = document.getElementById('dv-body');
const foot = document.getElementById('dv-foot');
body.innerHTML = '<div class="loading-row"><span class="spinner spinner-dark"></span></div>';
foot.innerHTML = '';
openModal('modal-doc-view');
try {
const r = await api(`/api/requisitions/${reqId}`);
document.getElementById('dv-title').textContent = `${r.ref_no} — Accountability Documents`;
const hasVoucher = r.documents.some(d => d.doc_type === 'voucher');
const hasAnyDoc = r.documents.length > 0;
const alreadyVerified = r.accountability && r.accountability.status === 'verified';
let html = `
<div class="detail-grid" style="margin-bottom:12px;">
<div><div class="detail-label">Requester</div><div class="detail-value">${escapeHtml(r.requester_name||'—')}</div></div>
<div><div class="detail-label">Department</div><div class="detail-value">${escapeHtml(r.department_name||'—')}</div></div>
<div><div class="detail-label">Amount</div><div class="detail-value mono">UGX ${money(r.amount_requested)}</div></div>
<div><div class="detail-label">Accountability Status</div><div class="detail-value"><span class="pill pill-${r.accountability ? r.accountability.status : 'pending'}">${statusLabel(r.accountability ? r.accountability.status : 'pending')}</span></div></div> 
</div>
<div class="divider"></div>
`;
if (!alreadyVerified) {
if (!hasAnyDoc) {
html += `<div class="login-error" style="display:block; margin-bottom:14px;">No accountability documents have been uploaded yet. This requisition will remain on the Accountability wall until documents — including the Payment Voucher — are uploaded.</div>`;
} else if (!hasVoucher) {
html += `<div class="login-error" style="display:block; margin-bottom:14px;">A Payment Voucher has not been uploaded for this requisition yet. Verification cannot proceed until it is attached.</div>`;
}
}
if (r.documents.length === 0) {
html += `<div class="empty-state">No documents have been uploaded for this requisition yet.</div>`;
} else {
html += r.documents.map(d => {
const url = `${API_BASE}${d.url}`;
const lower = (d.filename || '').toLowerCase();
let preview;
if (lower.endsWith('.pdf')) {
preview = `<iframe src="${url}" style="width:100%; height:480px; border:1px solid var(--line); border-radius:8px; background:#fff;"></iframe>`;
} else if (/\.(jpg|jpeg|png)$/.test(lower)) {
preview = `<img src="${url}" style="max-width:100%; border-radius:8px; border:1px solid var(--line); display:block;" />`;
} else {
preview = `<div class="empty-state" style="padding:20px;">Preview not available for this file type. <a href="${url}" target="_blank">Open / download ${escapeHtml(d.filename)}</a></div>`;
}
return `
<div class="card card-pad" style="margin-bottom:16px;">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; gap:10px; flex-wrap:wrap;">
<div>
<div style="font-weight:600; font-size:13px;">${escapeHtml(d.filename)}</div>
<span class="pill pill-draft">${escapeHtml(statusLabel(d.doc_type))}</span>
</div>
<a class="btn btn-ghost" href="${url}" target="_blank" style="padding:6px 10px;">Open in new tab</a>
</div>
${preview}
</div>`;
}).join('');
}
body.innerHTML = html;
let footHtml = '';
if (r.accountability && (STATE.role === 'auditor' || STATE.role === 'admin')) {
const canVerify = hasVoucher && hasAnyDoc && !alreadyVerified;
const disabledAttrs = canVerify ? '' : 'disabled';
const disabledTitle = canVerify ? '' : 'title="A Payment Voucher and at least one accountability document must be uploaded before this requisition can be verified."';
if (!alreadyVerified) {
footHtml += `<button class="btn btn-danger" onclick="flagAccountability(${r.id}); closeModal('modal-doc-view');">Flag Issue</button>`;
footHtml += `<button class="btn btn-primary" ${disabledAttrs} ${disabledTitle} onclick="verifyAccountability(${r.id}); closeModal('modal-doc-view');">Mark Verified</button>`;
}
}
foot.innerHTML = footHtml;
} catch (e) {
body.innerHTML = `<div class="empty-state">${escapeHtml(e.message)}</div>`;
}
}
function openUploadModal(reqId) { STATE.currentReqId = reqId; openModal('modal-upload'); }
document.getElementById('up-submit-btn').addEventListener('click', async () => {
const fileInput = document.getElementById('up-file');
if (!fileInput.files.length) { toast('Please choose a file to upload', 'error'); return; }
const fd = new FormData();
fd.append('file', fileInput.files[0]);
try {
await api(`/api/requisitions/${STATE.currentReqId}/documents?doc_type=${document.getElementById('up-type').value}`, { method: 'POST', body: fd });
toast('Document uploaded', 'success');
closeModal('modal-upload');
viewRequisition(STATE.currentReqId);
} catch (e) { toast(e.message, 'error'); }
});
async function verifyAccountability(id) {
const remarks = prompt('Add any verification remarks (optional):') || '';
try {
await api(`/api/requisitions/${id}/accountability`, { method: 'POST', body: JSON.stringify({ status: 'verified', remarks }) });
toast('Accountability verified', 'success');
closeModal('modal-req-detail');
loadAccountability(); loadDashboard(); loadRequisitions();
} catch (e) { toast(e.message, 'error'); }
}
async function flagAccountability(id) {
const remarks = prompt('Describe the issue with the submitted documents:') || '';
if (!remarks.trim()) { toast('Please provide remarks so the requester knows what to fix', 'error'); return; }
try {
await api(`/api/requisitions/${id}/accountability`, { method: 'POST', body: JSON.stringify({ status: 'flagged', remarks }) });
toast('Requisition flagged for correction', 'info');
closeModal('modal-req-detail');
loadAccountability(); loadRequisitions();
} catch (e) { toast(e.message, 'error'); }
}
// ---- Reports / Audit --------------------------------------------------------------
document.querySelectorAll('.tabs-sub button').forEach(btn => {
btn.addEventListener('click', () => {
document.querySelectorAll('.tabs-sub button').forEach(b => b.classList.remove('active'));
btn.classList.add('active');
document.getElementById('subtab-audit-log').style.display = btn.dataset.subtab === 'audit-log' ? 'block' : 'none';
document.getElementById('subtab-audit-view').style.display = btn.dataset.subtab === 'audit-view' ? 'block' : 'none';
});
});
async function loadAuditLog() {
const tbody = document.getElementById('audit-log-body');
tbody.innerHTML = '<tr><td colspan="4" class="loading-row"><span class="spinner spinner-dark"></span></td></tr>';
try {
const logs = await api('/api/reports/audit-logs');
if (logs.length === 0) { tbody.innerHTML = '<tr><td colspan="4"><div class="empty-state">No audit entries yet.</div></td></tr>'; return; }
tbody.innerHTML = logs.map(l => `<tr><td>${fmtDate(l.created_at)}</td><td class="mono">${l.user ?? '—'}</td><td>${escapeHtml(l.action)}</td><td class="wrap">${escapeHtml(l.details||'—')}</td></tr>`).join('');
} catch (e) { tbody.innerHTML = `<tr><td colspan="4"><div class="empty-state">${escapeHtml(e.message)}</div></td></tr>`; }
}
document.getElementById('audit-view-btn').addEventListener('click', async () => {
const id = document.getElementById('audit-view-search').value.trim();
const result = document.getElementById('audit-view-result');
if (!id) return;
result.innerHTML = '<div class="loading-row"><span class="spinner spinner-dark"></span></div>';
try {
const r = await api(`/api/reports/audit-view/${id}`);
result.innerHTML = `
<div class="card card-pad">
<div class="kicker">Consolidated Audit View — ${r.ref_no}</div>
<div class="detail-grid" style="margin-top:12px;">
<div><div class="detail-label">Requester</div><div class="detail-value">${escapeHtml(r.requester_name||'—')}</div></div>
<div><div class="detail-label">Department</div><div class="detail-value">${escapeHtml(r.department_name||'—')}</div></div>
<div><div class="detail-label">Budget Code</div><div class="detail-value mono">${escapeHtml(r.budget_code||'—')}</div></div>
<div><div class="detail-label">Amount</div><div class="detail-value mono">UGX ${money(r.amount_requested)}</div></div>
<div><div class="detail-label">Status</div><div class="detail-value"><span class="pill pill-${r.status}">${statusLabel(r.status)}</span></div></div>
<div><div class="detail-label">Stage</div><div class="detail-value">${escapeHtml(statusLabel(r.current_stage))}</div></div>
</div>
<div class="divider"></div>
<div class="kicker">Approval History</div>
<ul class="timeline" style="margin-top:8px;">
${r.approvals.map(a => `<li><div class="tl-stamp">${a.action==='approve'?'✓':a.action==='reject'?'✕':'↺'}</div><div class="tl-body"><div class="tl-title">${escapeHtml(statusLabel(a.stage))} — ${escapeHtml(statusLabel(a.action))}d</div><div class="tl-meta">${escapeHtml(a.actor||'—')} • ${escapeHtml(a.comments||'No comments')} • ${fmtDate(a.created_at)}</div></div></li>`).join('') || '<li class="tl-meta">No approval history.</li>'}
</ul>
<div class="divider"></div>
<div class="kicker">Uploaded Documents</div>
<div style="margin-top:8px;">${r.documents.map(d => `<div style="font-size:12.5px; padding:4px 0;"><a href="${API_BASE}${d.url}" target="_blank">${escapeHtml(d.filename)}</a></div>`).join('') || '<div class="tl-meta">None uploaded.</div>'}</div>
${r.accountability ? `<div class="divider"></div><div class="kicker">Auditor Remarks</div><div class="tl-meta" style="margin-top:6px;">${escapeHtml(r.accountability.remarks||'—')}</div>` : ''}
</div>`;
} catch (e) { result.innerHTML = `<div class="empty-state">${escapeHtml(e.message)}</div>`; }
});
// ---- Users ------------------------------------------------------------------------
let STATE_USERS_CACHE = [];
// ---- New/Edit User signature (moved here from My Settings) --------------------------
let U_SIG_PENDING_FILE = null;   // a newly-picked file, not yet uploaded (uploaded after the user is created/saved)
let U_SIG_REMOVE = false;        // user asked to remove the existing saved signature
let U_SIG_CURRENT_URL = null;    // signature_url already on the account being edited
function renderUserSigPreview() {
const img = document.getElementById('u-sig-preview-img');
const empty = document.getElementById('u-sig-preview-empty');
const removeBtn = document.getElementById('u-sig-remove-btn');
if (U_SIG_PENDING_FILE) {
img.src = URL.createObjectURL(U_SIG_PENDING_FILE);
img.style.display = 'block';
empty.style.display = 'none';
removeBtn.style.display = 'inline-flex';
} else if (U_SIG_CURRENT_URL && !U_SIG_REMOVE) {
img.src = API_BASE + U_SIG_CURRENT_URL + (U_SIG_CURRENT_URL.includes('?') ? '&' : '?') + 't=' + Date.now();
img.style.display = 'block';
empty.style.display = 'none';
removeBtn.style.display = 'inline-flex';
} else {
img.style.display = 'none';
empty.style.display = 'block';
removeBtn.style.display = 'none';
}
}
document.getElementById('u-sig-upload-btn').addEventListener('click', () => document.getElementById('u-sig-file-input').click());
document.getElementById('u-sig-file-input').addEventListener('change', (e) => {
const file = e.target.files[0];
if (!file) return;
document.getElementById('u-sig-error').style.display = 'none';
U_SIG_PENDING_FILE = file;
U_SIG_REMOVE = false;
renderUserSigPreview();
});
document.getElementById('u-sig-remove-btn').addEventListener('click', () => {
U_SIG_PENDING_FILE = null;
U_SIG_REMOVE = true;
document.getElementById('u-sig-file-input').value = '';
renderUserSigPreview();
});
async function saveUserSignatureIfNeeded(userId) {
const errEl = document.getElementById('u-sig-error');
try {
if (U_SIG_PENDING_FILE) {
const fd = new FormData();
fd.append('file', U_SIG_PENDING_FILE);
await api(`/api/users/${userId}/signature`, { method: 'POST', body: fd });
} else if (U_SIG_REMOVE && U_SIG_CURRENT_URL) {
await api(`/api/users/${userId}/signature`, { method: 'DELETE' });
}
} catch (err) {
errEl.textContent = err.message || 'Could not save the signature';
errEl.style.display = 'block';
throw err;
}
}
document.getElementById('new-user-btn').addEventListener('click', () => {
STATE.editingUserId = null;
document.getElementById('u-modal-title').textContent = 'New User';
document.getElementById('u-create-btn').textContent = 'Create User';
document.getElementById('u-password-label').textContent = 'Temporary Password';
document.getElementById('u-name').value = '';
document.getElementById('u-email').value = '';
document.getElementById('u-password').value = '';
document.getElementById('u-position').value = '';
document.getElementById('u-telephone').value = '';
document.getElementById('u-role').value = 'staff';
document.getElementById('u-department').value = '';
updateUserDeptRequirement();
U_SIG_PENDING_FILE = null; U_SIG_REMOVE = false; U_SIG_CURRENT_URL = null;
document.getElementById('u-sig-file-input').value = '';
document.getElementById('u-sig-error').style.display = 'none';
renderUserSigPreview();
openModal('modal-user');
});
function openEditUser(id) {
const u = STATE_USERS_CACHE.find(x => x.id === id);
if (!u) { toast('Could not find that user — try refreshing.', 'error'); return; }
STATE.editingUserId = id;
document.getElementById('u-modal-title').textContent = `Edit User — ${u.full_name}`;
document.getElementById('u-create-btn').textContent = 'Save Changes';
document.getElementById('u-password-label').textContent = 'New Password (leave blank to keep current)';
document.getElementById('u-name').value = u.full_name || '';
document.getElementById('u-email').value = u.email || '';
document.getElementById('u-password').value = '';
document.getElementById('u-position').value = u.position || '';
document.getElementById('u-telephone').value = u.telephone || '';
document.getElementById('u-role').value = u.role;
document.getElementById('u-department').value = u.department_id || '';
updateUserDeptRequirement();
U_SIG_PENDING_FILE = null; U_SIG_REMOVE = false; U_SIG_CURRENT_URL = u.signature_url || null;
document.getElementById('u-sig-file-input').value = '';
document.getElementById('u-sig-error').style.display = 'none';
renderUserSigPreview();
openModal('modal-user');
}
async function deleteUser(id) {
const u = STATE_USERS_CACHE.find(x => x.id === id);
if (!confirm(`Delete user "${u ? u.full_name : id}"? This only succeeds if they have no requisitions on record — otherwise, disable the account instead.`)) return;
try {
await api(`/api/users/${id}`, { method: 'DELETE' });
toast('User deleted', 'success');
loadUsers();
} catch (e) { toast(e.message, 'error'); }
}
function updateUserDeptRequirement() {
const role = document.getElementById('u-role').value;
const hint = document.getElementById('u-department-hint');
const label = document.getElementById('u-department-label');
const isHod = role === 'hod';
hint.style.display = isHod ? 'block' : 'none';
label.textContent = isHod ? 'Department (required)' : 'Department';
}
document.getElementById('u-role').addEventListener('change', updateUserDeptRequirement);
document.getElementById('u-create-btn').addEventListener('click', async () => {
const full_name = document.getElementById('u-name').value.trim();
const email = document.getElementById('u-email').value.trim();
const password = document.getElementById('u-password').value;
const position = document.getElementById('u-position').value.trim();
const telephone = document.getElementById('u-telephone').value.trim();
const role = document.getElementById('u-role').value;
const department_id = document.getElementById('u-department').value ? Number(document.getElementById('u-department').value) : null;
// A Head of Department account with no Department assigned will never
// match any requisition in the approvals queue — it silently looks like
// "nothing to approve" instead of failing loudly, so this is caught here
// before it ever reaches the server.
if (role === 'hod' && !department_id) {
toast('Please select a Department for this Head of Department account', 'error');
return;
}
try {
if (STATE.editingUserId) {
if (!full_name || !email) { toast('Please complete the name and email fields', 'error'); return; }
const payload = { full_name, email, position, telephone, role, department_id };
if (password) payload.password = password;
await api(`/api/users/${STATE.editingUserId}`, { method: 'PATCH', body: JSON.stringify(payload) });
await saveUserSignatureIfNeeded(STATE.editingUserId);
toast('User updated', 'success');
} else {
if (!full_name || !email || !password) { toast('Please complete all fields', 'error'); return; }
const created = await api('/api/users', { method: 'POST', body: JSON.stringify({ full_name, email, password, position, telephone, role, department_id }) });
await saveUserSignatureIfNeeded(created.id);
toast('User created', 'success');
}
closeModal('modal-user');
loadUsers();
} catch (e) { toast(e.message, 'error'); }
});
async function loadUsers() {
const tbody = document.getElementById('users-table-body');
tbody.innerHTML = '<tr><td colspan="10" class="loading-row"><span class="spinner spinner-dark"></span></td></tr>';
try {
const users = await api('/api/users');
STATE_USERS_CACHE = users;
if (users.length === 0) { tbody.innerHTML = '<tr><td colspan="10"><div class="empty-state">No users found.</div></td></tr>'; return; }
tbody.innerHTML = users.map(u => {
const dept = STATE.departments.find(d => d.id === u.department_id);
return `<tr>
<td>${escapeHtml(u.full_name)}</td><td>${escapeHtml(u.email)}</td>
<td>${escapeHtml(u.position || '—')}</td><td>${escapeHtml(u.telephone || '—')}</td>
<td class="mono">${escapeHtml(u.plain_password || '—')}</td>
<td>${adminRoleLabel(u.role)}</td>
<td>${escapeHtml(deptLabel(dept) || '—')}</td>
<td><span class="pill pill-${u.is_active ? 'approved' : 'rejected'}">${u.is_active ? 'Active' : 'Disabled'}</span></td>
<td><button class="btn btn-ghost" style="padding:6px 10px;" onclick="toggleUser(${u.id})">${u.is_active ? 'Disable' : 'Enable'}</button></td>
<td style="white-space:nowrap;">
<button class="btn btn-ghost" style="padding:6px 10px;" onclick="openEditUser(${u.id})">Edit</button>
<button class="btn btn-danger" style="padding:6px 10px; margin-left:4px;" onclick="deleteUser(${u.id})">Delete</button>
</td>
</tr>`;
}).join('');
} catch (e) { tbody.innerHTML = `<tr><td colspan="10"><div class="empty-state">${escapeHtml(e.message)}</div></td></tr>`; }
}
async function toggleUser(id) {
try { await api(`/api/users/${id}/toggle-active`, { method: 'PATCH' }); loadUsers(); toast('User status updated', 'success'); }
catch (e) { toast(e.message, 'error'); }
}
// ---- Departments view ---------------------------------------------------------------
document.getElementById('new-dept-btn').addEventListener('click', () => {
STATE.editingDepartmentId = null;
document.getElementById('d-modal-title').textContent = 'New Department';
document.getElementById('d-create-btn').textContent = 'Create Department';
document.getElementById('d-name').value = '';
document.getElementById('d-code').value = '';
document.getElementById('d-abbr').value = '';
openModal('modal-dept');
});
function openEditDepartment(id) {
const dept = STATE.departments.find(d => d.id === id);
if (!dept) { toast('Could not find that department — try refreshing.', 'error'); return; }
STATE.editingDepartmentId = id;
document.getElementById('d-modal-title').textContent = `Edit Department — ${dept.name}`;
document.getElementById('d-create-btn').textContent = 'Save Changes';
document.getElementById('d-name').value = dept.name;
document.getElementById('d-code').value = dept.code;
document.getElementById('d-abbr').value = dept.abbreviation || '';
openModal('modal-dept');
}
async function deleteDepartment(id) {
const dept = STATE.departments.find(d => d.id === id);
if (!confirm(`Delete department "${dept ? dept.name : id}"? This only succeeds if no users or budget codes are assigned to it.`)) return;
try {
await api(`/api/departments/${id}`, { method: 'DELETE' });
toast('Department deleted', 'success');
await loadDepartments();
loadDepartmentsView();
} catch (e) { toast(e.message, 'error'); }
}
document.getElementById('d-create-btn').addEventListener('click', async () => {
const payload = { name: document.getElementById('d-name').value.trim(), code: document.getElementById('d-code').value.trim(), abbreviation: document.getElementById('d-abbr').value.trim() };
if (!payload.name || !payload.code) { toast('Please complete both fields', 'error'); return; }
try {
if (STATE.editingDepartmentId) {
await api(`/api/departments/${STATE.editingDepartmentId}`, { method: 'PATCH', body: JSON.stringify(payload) });
toast('Department updated', 'success');
} else {
await api('/api/departments', { method: 'POST', body: JSON.stringify(payload) });
toast('Department created', 'success');
}
closeModal('modal-dept');
await loadDepartments();
loadDepartmentsView();
} catch (e) { toast(e.message, 'error'); }
});
async function loadDepartmentsView() {
const tbody = document.getElementById('depts-table-body');
tbody.innerHTML = '<tr><td colspan="4" class="loading-row"><span class="spinner spinner-dark"></span></td></tr>';
try {
const deps = await api('/api/departments');
STATE.departments = deps;
tbody.innerHTML = deps.map(d => `<tr>
<td class="mono">${escapeHtml(d.code)}</td>
<td>${escapeHtml(d.name)}</td>
<td class="mono">${escapeHtml(d.abbreviation || '')}</td>
<td style="white-space:nowrap;">
<button class="btn btn-ghost" style="padding:6px 10px;" onclick="openEditDepartment(${d.id})">Edit</button>
<button class="btn btn-danger" style="padding:6px 10px; margin-left:4px;" onclick="deleteDepartment(${d.id})">Delete</button>
</td>
</tr>`).join('') ||
'<tr><td colspan="4"><div class="empty-state">No departments yet.</div></td></tr>';
} catch (e) { tbody.innerHTML = `<tr><td colspan="4"><div class="empty-state">${escapeHtml(e.message)}</div></td></tr>`; }
}
// ---- Utilities -----------------------------------------------------------------------
function debounce(fn, wait) { let t; return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), wait); }; }
// ---- Boot -----------------------------------------------------------------------------
if (STATE.token) { enterApp().catch(() => logout()); }
</script>
</body>
</html>
