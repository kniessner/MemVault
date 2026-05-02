---
cssclasses:
  - dashboard
  - home
  - index
tags:
  - dashboard
  - home
---

# MemVault

```dataviewjs
// ═══════════════════════════════════════════════════════
//  MemVault Dashboard  ·  Full-Width Bento Grid
// ═══════════════════════════════════════════════════════
const IGNORE = [".obsidian", "node_modules", ".git", ".claude", "50-system/skills"];
const allFiles = app.vault.getFiles(); // cached once

// ── Shared style tokens ──────────────────────────────────
const S = {
  card:   `background:var(--background-secondary);border-radius:12px;padding:16px 18px;`,
  cardSm: `background:var(--background-secondary);border-radius:10px;padding:12px 14px;`,
  chip:   `background:var(--background-primary);border-radius:8px;padding:10px 12px;`,
  label:  `font-size:0.68em;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;opacity:0.4;display:block;margin-bottom:10px;`,
  row:    `display:flex;align-items:center;gap:8px;padding:5px 8px;background:var(--background-primary);border-radius:6px;font-size:0.83em;`,
  badge:  `margin-left:auto;opacity:0.38;font-size:0.76em;white-space:nowrap;`,
  accent: `background:var(--interactive-accent);color:var(--text-on-accent);border-radius:10px;padding:1px 8px;font-size:0.7em;font-weight:700;`,
  link:   `text-decoration:none;`,
  mono:   `font-family:var(--font-monospace);`,
};

function el(parent, tag, opts = {}) {
  return parent.createEl(tag, opts);
}
function div(parent, style = "", cls = "") {
  return parent.createEl("div", { attr: { style }, cls });
}
function lnk(parent, text, href, style = "") {
  return parent.createEl("a", { text, cls: "internal-link", attr: { "data-href": href, href, style: S.link + style }});
}
function label(parent, text) {
  parent.createEl("span", { text, attr: { style: S.label }});
}
function badge(parent, text) {
  parent.createEl("span", { text, attr: { style: S.badge }});
}

const THREE_DAYS_MS = 3 * 86400000;
const SLOW_CACHE_TTL = 2 * 60 * 1000; // 2 min cache for expensive reads

// ═══════════════════════════════════════════════════════
//  PREFETCH — all async work runs here in parallel
// ═══════════════════════════════════════════════════════
const today    = dv.date("today");
const todayStr = today.toFormat("yyyy-MM-dd");
const daily    = dv.pages('"10-notes/10-daily"').where(p => p.file.name === todayStr).first();
const allSkills = allFiles.filter(f => f.path.startsWith("50-system/skills/") && f.name === "SKILL.md");
const qlFile    = allFiles.find(f => f.path === "50-system/quick-links.md");

// Skill contents cache
const mv = window.__mv_cache__ = window.__mv_cache__ || {};

const [dailyContent, skillContents, qlContent] = await Promise.all([
  // Daily note focus
  daily ? dv.io.load(daily.file.path).catch(() => null) : Promise.resolve(null),

  // Skill descriptions — use cached result if fresh enough
  (mv.skills && Date.now() - mv.skills.ts < SLOW_CACHE_TTL)
    ? Promise.resolve(mv.skills.data)
    : Promise.all(allSkills.map(f => app.vault.cachedRead(f).catch(() => "")))
        .then(d => { mv.skills = { ts: Date.now(), data: d }; return d; }),

  // Quick links file content
  qlFile ? dv.io.load(qlFile.path).catch(() => "") : Promise.resolve(""),
]);

// ── Hide container during synchronous DOM construction ───
dv.container.style.opacity = "0";

// ── Pre-compute projects ──
const _pFiles = allFiles.filter(f =>
  f.path.startsWith("30-projects-active/") && !f.path.includes("_template") && f.extension === "md"
);
const _pDirs = {};
for (const f of _pFiles) {
  const dir = f.path.replace("30-projects-active/", "").split("/")[0];
  if (!_pDirs[dir]) _pDirs[dir] = { dir, files: [], mtime: 0, entry: null };
  _pDirs[dir].files.push(f);
  if (f.stat.mtime > _pDirs[dir].mtime) _pDirs[dir].mtime = f.stat.mtime;
  const rel = f.path.replace(`30-projects-active/${dir}/`, "");
  if (f.name === "README.md" && !rel.includes("/")) _pDirs[dir].entry = f.path;
  else if (f.name.endsWith("-index.md") && !rel.includes("/") && !_pDirs[dir].entry) _pDirs[dir].entry = f.path;
  else if (!rel.includes("/") && !_pDirs[dir].entry) _pDirs[dir].entry = f.path;
}
const projects = Object.values(_pDirs).sort((a,b) => b.mtime - a.mtime);

// ── Root ─────────────────────────────────────────────────
const root = div(dv.container, "display:flex;flex-direction:column;gap:12px;");

// ═══════════════════════════════════════════════════════
//  1 · HEADER
// ═══════════════════════════════════════════════════════
const dayLabel = today.toFormat("cccc, MMMM d, yyyy");

const hdr = div(root, S.card + "display:flex;align-items:center;justify-content:space-between;");
const hL  = div(hdr);
el(hL, "div", { text: dayLabel, attr: { style: "font-size:1.15em;font-weight:700;letter-spacing:-0.02em;" }});

if (daily) {
  const m = dailyContent?.match(/## Focus\n([\s\S]*?)(?=\n##|\n---)/);
  const focus = m ? m[1].trim() : null;
  if (focus && focus !== "What's the main thing today?") {
    el(hL, "div", { text: focus, attr: { style: "opacity:0.55;font-size:0.86em;margin-top:3px;" }});
  } else {
    lnk(hL, "Set today's focus →", daily.file.path, "opacity:0.4;font-size:0.82em;display:inline-block;margin-top:3px;");
  }
} else {
  el(hL, "span", { text: "No daily note yet", attr: { style: "opacity:0.35;font-size:0.82em;" }});
}

const hR  = div(hdr, "text-align:right;opacity:0.4;font-size:0.78em;line-height:1.8;");
const mdC = allFiles.filter(f => f.extension === "md").length;
const skC = allSkills.length;
el(hR, "div", { text: `${mdC} notes · ${allFiles.length} files · ${skC} skills` });

// ═══════════════════════════════════════════════════════
//  2 · QUICK ACTIONS  (single row, 8 cols)
// ═══════════════════════════════════════════════════════
const ACTIONS = [
  { icon: "📝", label: "New Note",     href: "00-inbox/untitled" },
  { icon: "📅", label: "Today",        href: `10-notes/10-daily/${todayStr}` },
  { icon: "📁", label: "Projects",     href: "30-projects-active/projects-index" },
  { icon: "🛠",  label: "Skills",       href: "50-system/skills" },
  { icon: "📚", label: "Knowledge",    href: "20-knowledge/README" },
  { icon: "🗄",  label: "Bookmarks",   href: "40-library/bookmarks" },
  { icon: "📓", label: "Session Logs", href: "50-system/logs/session-logs" },
  { icon: "⚙️", label: "System",       href: "50-system" },
];

const aqWrap = div(root, S.cardSm);
const aqGrid = div(aqWrap, "display:grid;grid-template-columns:repeat(8,1fr);gap:6px;");
for (const a of ACTIONS) {
  const c = div(aqGrid, "background:var(--background-primary);border-radius:8px;padding:11px 6px;text-align:center;");
  el(c, "div", { text: a.icon, attr: { style: "font-size:1.15em;margin-bottom:3px;" }});
  lnk(c, a.label, a.href, "font-size:0.73em;font-weight:600;");
}

// ═══════════════════════════════════════════════════════
//  2B · QUICK LINKS  (external URLs — parsed from md list)
// ═══════════════════════════════════════════════════════
const qlLinks = [...(qlContent || "").matchAll(/^\s*\*\s*\[([^\]]+)\]\(([^\s)]+)[^)]*\)/gm)]
  .map(m => {
    const raw  = m[1].trim();
    const emo  = raw.match(/^\p{Extended_Pictographic}\s*/u);
    return { icon: emo ? emo[0].trim() : "🔗", label: emo ? raw.slice(emo[0].length) : raw, url: m[2] };
  });

if (qlLinks.length > 0) {
  const qlWrap = div(root, "background:var(--background-secondary);border-radius:10px;padding:7px 12px;display:flex;align-items:center;gap:6px;flex-wrap:wrap;");
  for (const ql of qlLinks) {
    const pill = div(qlWrap, "background:var(--background-primary);border-radius:20px;padding:4px 12px;display:flex;align-items:center;gap:5px;");
    el(pill, "span", { text: ql.icon, attr: { style: "font-size:0.85em;" }});
    const a = document.createElement("a");
    a.textContent = ql.label;
    a.href = ql.url;
    a.target = "_blank";
    a.rel = "noopener noreferrer";
    a.style.cssText = "font-size:0.76em;font-weight:600;text-decoration:none;color:inherit;white-space:nowrap;";
    pill.appendChild(a);
  }
  const addBtn = div(qlWrap, "background:var(--interactive-accent);border-radius:20px;padding:4px 11px;display:flex;align-items:center;cursor:pointer;flex-shrink:0;");
  el(addBtn, "span", { text: "+", attr: { style: "font-size:0.9em;font-weight:700;color:var(--text-on-accent);line-height:1;" }});

  const sep = div(qlWrap, "flex:1;");
  lnk(sep, "edit →", "50-system/quick-links", "font-size:0.65em;opacity:0.28;white-space:nowrap;");

  const qlForm = div(qlWrap, "width:100%;display:none;align-items:center;gap:5px;padding-top:5px;flex-wrap:wrap;");
  const iStyle = "font-size:0.76em;padding:4px 10px;border-radius:12px;border:1px solid var(--background-modifier-border);background:var(--background-primary);color:inherit;outline:none;";
  const lblInput = el(qlForm, "input", { attr: { placeholder: "🔗 Label", style: iStyle + "width:120px;" }});
  const urlInput = el(qlForm, "input", { attr: { placeholder: "https://...",  style: iStyle + "flex:1;min-width:180px;" }});
  const saveBtn  = el(qlForm, "button", { text: "Add", attr: { style: "font-size:0.74em;padding:4px 12px;border-radius:12px;background:var(--interactive-accent);color:var(--text-on-accent);border:none;cursor:pointer;" }});
  const cancelBtn= el(qlForm, "button", { text: "✕",   attr: { style: "font-size:0.74em;padding:4px 9px;border-radius:12px;background:var(--background-primary);border:1px solid var(--background-modifier-border);cursor:pointer;opacity:0.55;" }});

  const closeForm = () => { qlForm.style.display = "none"; lblInput.value = ""; urlInput.value = ""; };
  const doSave = async () => {
    const lbl = lblInput.value.trim(), url = urlInput.value.trim();
    if (!lbl || !url) return;
    const qf = app.vault.getAbstractFileByPath("50-system/quick-links.md");
    if (!qf) return;
    await app.vault.process(qf, c => c.trimEnd() + `\n* [${lbl}](${url})\n`);
    closeForm();
  };

  addBtn.addEventListener("click", () => {
    qlForm.style.display = qlForm.style.display === "none" ? "flex" : "none";
    if (qlForm.style.display === "flex") lblInput.focus();
  });
  saveBtn.addEventListener("click",  doSave);
  cancelBtn.addEventListener("click", closeForm);
  urlInput.addEventListener("keydown",  e => { if (e.key === "Enter") doSave(); });
  lblInput.addEventListener("keydown",  e => { if (e.key === "Tab" && !e.shiftKey) { e.preventDefault(); urlInput.focus(); } });
}

// ═══════════════════════════════════════════════════════
//  2C · QUICK CAPTURE
// ═══════════════════════════════════════════════════════
const qcWrap = div(root, "background:var(--background-secondary);border-radius:10px;padding:7px 12px;display:flex;flex-direction:column;gap:0;");
const qcRow  = div(qcWrap, "display:flex;align-items:center;gap:6px;flex-wrap:wrap;");

const fldStyle  = "font-size:0.76em;padding:4px 10px;border-radius:12px;border:1px solid var(--background-modifier-border);background:var(--background-primary);color:inherit;outline:none;";
const btnStyle  = "font-size:0.74em;padding:4px 12px;border-radius:12px;background:var(--interactive-accent);color:var(--text-on-accent);border:none;cursor:pointer;";
const xStyle    = "font-size:0.74em;padding:4px 9px;border-radius:12px;background:var(--background-primary);border:1px solid var(--background-modifier-border);cursor:pointer;opacity:0.55;";

const qcActions = [
  { id:"meeting", icon:"📋", label:"Meeting Note" },
  { id:"daily",   icon:"📅", label:"Add to Daily"  },
  { id:"task",    icon:"✅", label:"New Task"       },
];
const qcForms = {};
let qcOpen = null;

const closeQc = () => {
  if (qcOpen) {
    qcForms[qcOpen].form.style.display = "none";
    qcForms[qcOpen].btn.style.background = "var(--background-primary)";
    qcForms[qcOpen].btn.style.color = "inherit";
    qcOpen = null;
  }
};
const openQc = (id) => {
  if (qcOpen === id) { closeQc(); return; }
  closeQc();
  qcForms[id].form.style.display = "flex";
  qcForms[id].btn.style.background = "var(--interactive-accent)";
  qcForms[id].btn.style.color = "var(--text-on-accent)";
  qcOpen = id;
  qcForms[id].firstInput?.focus();
};

for (const act of qcActions) {
  const btn = div(qcRow, "background:var(--background-primary);border-radius:20px;padding:4px 12px;display:flex;align-items:center;gap:5px;cursor:pointer;flex-shrink:0;");
  el(btn, "span", { text: act.icon, attr: { style: "font-size:0.85em;" }});
  el(btn, "span", { text: act.label, attr: { style: "font-size:0.76em;font-weight:600;" }});
  const form = div(qcWrap, "display:none;align-items:center;gap:5px;padding-top:6px;flex-wrap:wrap;");
  qcForms[act.id] = { btn, form, firstInput: null };
  btn.addEventListener("click", () => openQc(act.id));
}

// ── Meeting Note form ──────────────────────────────────
{
  const f = qcForms["meeting"].form;
  const titleIn = el(f, "input", { attr: { placeholder: "Meeting title…", style: fldStyle + "flex:1;min-width:200px;" }});
  qcForms["meeting"].firstInput = titleIn;
  const saveBtn = el(f, "button", { text: "Create & Open", attr: { style: btnStyle }});
  el(f, "button", { text: "✕", attr: { style: xStyle }}).addEventListener("click", closeQc);

  const doMeeting = async () => {
    const title = titleIn.value.trim(); if (!title) return;
    try {
      const dateStr = today.toFormat("yyyy-MM-dd");
      const slug    = title.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
      const folder  = "10-notes/30-meetings";
      const path    = `${folder}/${dateStr}-${slug}.md`;
      const body    = `---\ntitle: "${title}"\ndate: ${dateStr}\ntags:\n  - meeting\n---\n\n## Attendees\n\n## Agenda\n\n## Notes\n\n## Action Items\n- [ ] \n`;
      if (!app.vault.getAbstractFileByPath(folder)) await app.vault.createFolder(folder);
      let file = app.vault.getAbstractFileByPath(path);
      if (!file) file = await app.vault.create(path, body);
      await app.workspace.getLeaf().openFile(file);
      titleIn.value = ""; closeQc();
    } catch(e) { new Notice("Meeting note error: " + e.message); }
  };
  saveBtn.addEventListener("click", doMeeting);
  titleIn.addEventListener("keydown", e => { if (e.key === "Enter") doMeeting(); });
}

// ── Add to Daily Note form ─────────────────────────────
{
  const f = qcForms["daily"].form;
  const noteIn = el(f, "input", { attr: { placeholder: "Add to today's note…", style: fldStyle + "flex:1;min-width:220px;" }});
  qcForms["daily"].firstInput = noteIn;
  const saveBtn = el(f, "button", { text: "Add", attr: { style: btnStyle }});
  el(f, "button", { text: "✕", attr: { style: xStyle }}).addEventListener("click", closeQc);

  const doDaily = async () => {
    const text = noteIn.value.trim(); if (!text) return;
    const dateStr = today.toFormat("yyyy-MM-dd");
    const path    = `10-notes/10-daily/${dateStr}.md`;
    const df      = app.vault.getAbstractFileByPath(path);
    if (df) {
      await app.vault.process(df, c => c.trimEnd() + `\n- ${text}\n`);
    } else {
      await app.vault.create(path, `---\ndate: ${dateStr}\ntags:\n  - daily\n---\n\n## Focus\nWhat's the main thing today?\n\n## Notes\n- ${text}\n`);
    }
    noteIn.value = ""; closeQc();
  };
  saveBtn.addEventListener("click", doDaily);
  noteIn.addEventListener("keydown", e => { if (e.key === "Enter") doDaily(); });
}

// ── New Task form ──────────────────────────────────────
{
  const f = qcForms["task"].form;
  const taskIn = el(f, "input", { attr: { placeholder: "Task description…", style: fldStyle + "flex:1;min-width:200px;" }});
  qcForms["task"].firstInput = taskIn;
  const projSel = el(f, "select", { attr: { style: fldStyle + "max-width:150px;" }});
  el(projSel, "option", { text: "— daily note —", attr: { value: "" }});
  for (const p of projects) {
    el(projSel, "option", { text: p.dir.replace(/^\d{4}-/, ""), attr: { value: p.dir }});
  }
  const saveBtn = el(f, "button", { text: "Add", attr: { style: btnStyle }});
  el(f, "button", { text: "✕", attr: { style: xStyle }}).addEventListener("click", closeQc);

  const doTask = async () => {
    const text = taskIn.value.trim(); if (!text) return;
    const proj = projSel.value;
    if (proj) {
      const taskPath = `30-projects-active/${proj}/tasks.md`;
      const tf = app.vault.getAbstractFileByPath(taskPath);
      if (tf) {
        await app.vault.process(tf, c => c.trimEnd() + `\n- [ ] ${text}\n`);
      } else {
        await app.vault.create(taskPath, `# Tasks\n\n- [ ] ${text}\n`);
      }
    } else {
      const dateStr = today.toFormat("yyyy-MM-dd");
      const path    = `10-notes/10-daily/${dateStr}.md`;
      const df      = app.vault.getAbstractFileByPath(path);
      if (df) {
        await app.vault.process(df, c => c.trimEnd() + `\n- [ ] ${text}\n`);
      } else {
        await app.vault.create(path, `---\ndate: ${dateStr}\ntags:\n  - daily\n---\n\n## Tasks\n- [ ] ${text}\n`);
      }
    }
    taskIn.value = ""; closeQc();
  };
  saveBtn.addEventListener("click", doTask);
  taskIn.addEventListener("keydown", e => { if (e.key === "Enter") doTask(); });
}

// ═══════════════════════════════════════════════════════
//  3 · PINNED
// ═══════════════════════════════════════════════════════
const pinnedPages = dv.pages().where(p =>
  p.tags && (p.tags.includes("pinned") || p.tags.includes("#pinned"))
).limit(10);
if (pinnedPages.length > 0) {
  const pinWrap = div(root, S.cardSm);
  label(pinWrap, "📌 Pinned");
  const pinRow = div(pinWrap, "display:flex;flex-wrap:wrap;gap:5px;");
  for (const p of pinnedPages) {
    const chip = div(pinRow, "background:var(--background-primary);border-radius:8px;padding:6px 12px;display:flex;align-items:center;gap:5px;");
    el(chip, "span", { text: "📌", attr: { style: "font-size:0.8em;opacity:0.5;" }});
    lnk(chip, p.file.basename, p.file.path, "font-size:0.84em;font-weight:500;");
  }
}

// ═══════════════════════════════════════════════════════
//  4 · SYSTEM + ACTIVITY  [1fr | 2fr]
// ═══════════════════════════════════════════════════════
const saGrid = div(root, "display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:12px;align-items:start;");

// ── 4A · SYSTEM ──────────────────────────────────────────
const sysWrap = div(saGrid, S.card);
label(sysWrap, "System");

function fmtBytes(b) {
  return b >= 1073741824 ? (b / 1073741824).toFixed(1) + " GB" : (b / 1048576).toFixed(0) + " MB";
}
function fmtUptime(s) {
  const d = Math.floor(s / 86400), h = Math.floor((s % 86400) / 3600), m = Math.floor((s % 3600) / 60);
  return d > 0 ? `${d}d ${h}h` : h > 0 ? `${h}h ${m}m` : `${m}m`;
}

let sysInfo;
try {
  const os = require("os");
  const cpus = os.cpus();
  const totalMem = os.totalmem(), freeMem = os.freemem();
  const type = os.type();
  sysInfo = {
    osLabel:  type === "Darwin" ? "macOS" : type === "Windows_NT" ? "Windows" : type,
    osIcon:   type === "Darwin" ? "🍎"    : type === "Windows_NT" ? "🪟"      : "🐧",
    hostname: os.hostname(),
    arch:     os.arch(),
    uptime:   os.uptime(),
    cpuModel: (cpus[0]?.model || "").replace(/\s+/g, " ").split("@")[0].trim(),
    cpuCores: cpus.length,
    totalMem, freeMem,
    usedMem:  totalMem - freeMem,
    memPct:   Math.round(((totalMem - freeMem) / totalMem) * 100),
  };
} catch {
  const ua = navigator.userAgent, plat = navigator.platform || "";
  const osLabel = plat.includes("Mac") || ua.includes("Mac") ? "macOS"
    : plat.includes("Win") || ua.includes("Windows") ? "Windows"
    : plat.includes("Linux") || ua.includes("Linux") ? "Linux" : "Unknown";
  sysInfo = {
    osLabel,
    osIcon:   osLabel === "macOS" ? "🍎" : osLabel === "Windows" ? "🪟" : osLabel === "Linux" ? "🐧" : "💻",
    hostname: null, arch: null, uptime: null,
    cpuModel: null, cpuCores: navigator.hardwareConcurrency || null,
    totalMem: null, freeMem: null, usedMem: null, memPct: null,
  };
}

const osRow = div(sysWrap, S.row + "margin-bottom:8px;");
el(osRow, "span", { text: sysInfo.osIcon });
el(osRow, "span", { text: sysInfo.osLabel, attr: { style: "font-weight:600;" }});
if (sysInfo.arch) el(osRow, "span", { text: sysInfo.arch, attr: { style: S.mono + "opacity:0.4;font-size:0.76em;" }});
if (sysInfo.hostname) badge(osRow, sysInfo.hostname);
if (sysInfo.uptime !== null) el(osRow, "span", { text: "↑ " + fmtUptime(sysInfo.uptime), attr: { style: "opacity:0.38;font-size:0.75em;white-space:nowrap;" }});

const hwGrid = div(sysWrap, "display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-bottom:8px;");

const cpuCard = div(hwGrid, "background:var(--background-primary);border-radius:8px;padding:9px 11px;");
el(cpuCard, "div", { text: "CPU", attr: { style: S.label + "margin-bottom:4px;" }});
el(cpuCard, "div", { text: sysInfo.cpuCores ? `${sysInfo.cpuCores} cores` : "—", attr: { style: "font-weight:600;font-size:0.88em;" }});
if (sysInfo.cpuModel) el(cpuCard, "div", { text: sysInfo.cpuModel, attr: { style: "opacity:0.42;font-size:0.72em;margin-top:2px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;" }});

const memCard = div(hwGrid, "background:var(--background-primary);border-radius:8px;padding:9px 11px;");
el(memCard, "div", { text: "Memory", attr: { style: S.label + "margin-bottom:4px;" }});
if (sysInfo.totalMem !== null) {
  const mc = sysInfo.memPct > 85 ? "var(--color-red)" : sysInfo.memPct > 65 ? "var(--color-orange)" : "var(--interactive-accent)";
  el(memCard, "div", { text: `${fmtBytes(sysInfo.usedMem)} / ${fmtBytes(sysInfo.totalMem)}`, attr: { style: "font-weight:600;font-size:0.88em;" }});
  const barBg = div(memCard, "background:var(--background-modifier-border);border-radius:3px;height:5px;margin-top:5px;overflow:hidden;");
  div(barBg, `background:${mc};height:100%;width:${sysInfo.memPct}%;border-radius:3px;`);
} else {
  el(memCard, "div", { text: "—", attr: { style: "opacity:0.4;font-size:0.88em;" }});
}

// ── 4B · ACTIVITY ────────────────────────────────────────
const actWrap = div(saGrid, S.card);
label(actWrap, "Activity · Recently Modified");

const FOLDER_FILTERS = [
  ["all",                "All"],
  ["10-notes",           "📝 Notes"],
  ["20-knowledge",       "💡 Knowledge"],
  ["30-projects-active", "📁 Projects"],
  ["40-library",         "📚 Library"],
  ["50-system",          "⚙️ System"],
  ["00-inbox",           "📥 Inbox"],
];
let activeFilter = "all";
const chipEls = {};

const filterRow = div(actWrap, "display:flex;flex-wrap:wrap;gap:4px;margin-bottom:8px;");
for (const [key, lbl] of FOLDER_FILTERS) {
  const isActive = key === "all";
  const chip = el(filterRow, "button", {
    text: lbl,
    attr: { style:
      `padding:2px 10px;border-radius:12px;font-size:0.74em;cursor:pointer;border:none;` +
      `background:${isActive ? "var(--interactive-accent)" : "var(--background-primary)"};` +
      `color:${isActive ? "var(--text-on-accent)" : "inherit"};`
    }
  });
  chipEls[key] = chip;
  chip.addEventListener("click", () => {
    activeFilter = key;
    for (const [k, c] of Object.entries(chipEls)) {
      c.style.background = k === activeFilter ? "var(--interactive-accent)" : "var(--background-primary)";
      c.style.color      = k === activeFilter ? "var(--text-on-accent)"     : "inherit";
    }
    for (const r of aGrid.querySelectorAll("[data-folder]")) {
      r.style.display = (activeFilter === "all" || r.dataset.folder === activeFilter) ? "" : "none";
    }
  });
}

const recent = allFiles
  .filter(f => f.extension === "md" && !IGNORE.some(i => f.path.includes(i)) && f.basename !== "Dashboard")
  .sort((a,b) => b.stat.mtime - a.stat.mtime).slice(0, 20);

const aGrid = div(actWrap, "display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:4px;");
const ICONS = { "10-notes":"📝","20-knowledge":"💡","30-projects-active":"📁","40-library":"📚","50-system":"⚙️","00-inbox":"📥" };
const nowMs = Date.now();
for (const f of recent) {
  const folder = f.path.split("/")[0];
  const age = Math.floor((nowMs - f.stat.mtime) / 86400000);
  const r = div(aGrid, S.row + "min-width:0;");
  r.setAttribute("data-folder", folder);
  el(r, "span", { text: ICONS[folder] || "📄" });
  lnk(r, f.basename, f.path, "flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;");
  badge(r, age === 0 ? "now" : age + "d");
}

// ═══════════════════════════════════════════════════════
//  5 · MAIN GRID  [2fr | 1fr]
// ═══════════════════════════════════════════════════════
const mainGrid = div(root, "display:grid;grid-template-columns:minmax(0,2fr) minmax(0,1fr);gap:12px;align-items:start;");
const leftCol  = div(mainGrid, "display:flex;flex-direction:column;gap:12px;");
const rightCol = div(mainGrid, "display:flex;flex-direction:column;gap:12px;");

// ── 5A · PROJECTS (left) ─────────────────────────────────
const projWrap = div(leftCol, S.card);
label(projWrap, "Projects");

const pGrid = div(projWrap, "display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:7px;");

for (const p of projects) {
  const age = Math.floor((Date.now() - p.mtime) / 86400000);
  const accentColor = age <= 3 ? "var(--interactive-accent)" : age > 14 ? "var(--text-faint)" : "var(--background-modifier-border)";
  const pCard = div(pGrid, `background:var(--background-primary);border-radius:8px;padding:11px 12px;border-left:3px solid ${accentColor};`);
  const href = p.entry ? p.entry.replace(/\.md$/, "") : `30-projects-active/${p.dir}`;
  lnk(pCard, p.dir.replace(/^\d{4}-/, ""), href, "font-weight:600;font-size:0.86em;display:block;margin-bottom:5px;");
  const contentFiles = p.files.filter(f => !f.name.endsWith("-index.md") && !["README.md","Project Dashboard.md"].includes(f.name));
  const meta = div(pCard, "display:flex;justify-content:space-between;opacity:0.4;font-size:0.74em;");
  el(meta, "span", { text: `${contentFiles.length}f` });
  el(meta, "span", { text: age === 0 ? "today" : age + "d" });
}

// ── 5B · TASKS (left) ────────────────────────────────────
const tWrap = div(leftCol, S.card);
label(tWrap, "Tasks");

const sevenForward = dv.date("today").plus({ days: 7 });
const upcomingTasks = dv.pages('"30-projects-active"').file.tasks
  .where(t => !t.completed && t.due && t.due <= sevenForward)
  .sort(t => t.due, "asc");

if (upcomingTasks.length > 0) {
  el(tWrap, "span", { text: "Due soon", attr: { style: S.label + "color:var(--color-orange);opacity:0.7;" }});
  const upList = div(tWrap, "display:flex;flex-direction:column;gap:3px;margin-bottom:12px;");
  for (const t of upcomingTasks) {
    const r = div(upList, S.row + "border-left:2px solid var(--color-orange);");
    el(r, "span", { text: "⏰", attr: { style: "font-size:0.85em;flex-shrink:0;" }});
    el(r, "span", { text: t.text.replace(/\[.*?\]/g,"").trim(), attr: { style: "flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;" }});
    el(r, "span", { text: t.due.toFormat("MM-dd"), attr: { style: S.badge + "color:var(--color-orange);opacity:1;" }});
    lnk(r, "↗", t.path, "opacity:0.3;font-size:0.8em;flex-shrink:0;");
  }
}

const openTasks = dv.pages('"30-projects-active"').file.tasks
  .where(t => !t.completed)
  .sort(t => t.due ?? "", "asc")
  .limit(20);

if (openTasks.length === 0 && upcomingTasks.length === 0) {
  el(tWrap, "p", { text: "All clear ✓", attr: { style: "opacity:0.4;font-size:0.85em;margin:0;" }});
} else if (openTasks.length > 0) {
  el(tWrap, "span", { text: "Open", attr: { style: S.label }});
  const byProject = {};
  for (const t of openTasks) {
    const proj = t.path.replace("30-projects-active/", "").split("/")[0];
    if (!byProject[proj]) byProject[proj] = [];
    byProject[proj].push(t);
  }
  for (const [proj, tasks] of Object.entries(byProject)) {
    el(tWrap, "div", { text: proj.replace(/^\d{4}-/, ""), attr: { style: "font-size:0.74em;font-weight:600;opacity:0.5;margin:8px 0 4px;padding-left:4px;" }});
    const tList = div(tWrap, "display:flex;flex-direction:column;gap:3px;");
    for (const t of tasks.slice(0, 5)) {
      const r = div(tList, S.row);
      el(r, "span", { text: "○", attr: { style: "opacity:0.4;font-size:0.9em;flex-shrink:0;" }});
      el(r, "span", { text: t.text.replace(/\[.*?\]/g,"").trim(), attr: { style: "flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;" }});
      if (t.due) el(r, "span", { text: t.due.toFormat("MM-dd"), attr: { style: S.badge + "color:var(--color-orange);" }});
      lnk(r, "↗", t.path, "opacity:0.3;font-size:0.8em;flex-shrink:0;");
    }
    if (tasks.length > 5) el(tWrap, "div", { text: `+${tasks.length-5} more`, attr: { style: "opacity:0.35;font-size:0.75em;margin:2px 0 4px 8px;" }});
  }
}

const sevenAgo  = dv.date("today").minus({ days: 7 });
const doneTasks = dv.pages('"30-projects-active"').file.tasks
  .where(t => t.completed && t.completion && t.completion >= sevenAgo)
  .sort(t => t.completion, "desc")
  .limit(6);

if (doneTasks.length > 0) {
  el(tWrap, "span", { text: `Completed · last 7 days`, attr: { style: S.label + "margin-top:14px;" }});
  const dList = div(tWrap, "display:flex;flex-direction:column;gap:3px;");
  for (const t of doneTasks) {
    const r = div(dList, S.row + "opacity:0.55;");
    el(r, "span", { text: "✓", attr: { style: "color:var(--color-green);font-size:0.85em;flex-shrink:0;" }});
    el(r, "span", { text: t.text.replace(/\[.*?\]/g,"").trim(), attr: { style: "flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;" }});
    lnk(r, "↗", t.path, "opacity:0.25;font-size:0.8em;flex-shrink:0;");
  }
}

// ── 5C · INBOX (right) ───────────────────────────────────
const inboxFiles = allFiles
  .filter(f => f.path.startsWith("00-inbox/") && f.extension === "md")
  .sort((a,b) => b.stat.mtime - a.stat.mtime);

const ibWrap = div(rightCol, S.card);
const ibH = div(ibWrap, "display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;");
el(ibH, "span", { text: "Inbox", attr: { style: S.label + "margin-bottom:0;" }});
if (inboxFiles.length > 0) {
  el(ibH, "span", { text: `${inboxFiles.length}`, attr: { style: S.accent }});
}
if (inboxFiles.length === 0) {
  el(ibWrap, "p", { text: "Inbox clear.", attr: { style: "opacity:0.4;font-size:0.85em;margin:0;" }});
} else {
  const ibList = div(ibWrap, "display:flex;flex-direction:column;gap:4px;");
  for (const f of inboxFiles.slice(0, 8)) {
    const r = div(ibList, S.row);
    el(r, "span", { text: "📄" });
    lnk(r, f.basename, f.path, "flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;");
    const age = Math.floor((Date.now() - f.stat.mtime) / 86400000);
    badge(r, age === 0 ? "today" : age + "d");
  }
}

// ── 5D · DAILY NOTES (right) ─────────────────────────────
const dailies = allFiles
  .filter(f => f.path.startsWith("10-notes/10-daily/") && /^\d{4}-\d{2}-\d{2}\.md$/.test(f.name))
  .sort((a,b) => b.name.localeCompare(a.name)).slice(0, 7);

const dnWrap = div(rightCol, S.card);
label(dnWrap, "Daily Notes");
if (dailies.length === 0) {
  el(dnWrap, "p", { text: "No daily notes yet.", attr: { style: "opacity:0.4;font-size:0.85em;margin:0;" }});
} else {
  const yest  = today.minus({ days: 1 }).toFormat("yyyy-MM-dd");
  const dnList = div(dnWrap, "display:flex;flex-direction:column;gap:3px;");
  for (const f of dailies) {
    const isToday = f.basename === todayStr;
    const lbl = isToday ? "Today" : f.basename === yest ? "Yesterday" : f.basename;
    const r = div(dnList, S.row + (isToday ? "border-left:2px solid var(--interactive-accent);" : ""));
    el(r, "span", { text: "📅" });
    lnk(r, lbl, f.path, isToday ? "font-weight:600;" : "");
  }
}

// ═══════════════════════════════════════════════════════
//  6 · KNOWLEDGE + LIBRARY | SKILLS  [1fr | 1fr]
// ═══════════════════════════════════════════════════════
const midGrid = div(root, "display:grid;grid-template-columns:1fr 1fr;gap:12px;align-items:start;");
const midLeft = div(midGrid, "display:flex;flex-direction:column;gap:12px;");

// ── 6A · KNOWLEDGE BASE ──────────────────────────────────
const kbWrap = div(midLeft, S.card);
label(kbWrap, "Knowledge Base");
const KB_FOLDERS = ["ai","tech","business","concepts"];
const KB_ICONS   = { ai:"🤖", tech:"💻", business:"📊", concepts:"🧠" };
const kbGrid = div(kbWrap, "display:grid;grid-template-columns:1fr 1fr;gap:8px;");

for (const folder of KB_FOLDERS) {
  const files = allFiles.filter(f =>
    f.path.startsWith(`20-knowledge/${folder}/`) &&
    f.extension === "md" && !["README.md"].includes(f.name) && !f.name.endsWith("-index.md")
  );
  if (!files.length) continue;
  const kCard = div(kbGrid, S.chip);
  const kH = div(kCard, "display:flex;align-items:center;gap:5px;margin-bottom:7px;");
  el(kH, "span", { text: KB_ICONS[folder] || "📁" });
  lnk(kH, folder.charAt(0).toUpperCase()+folder.slice(1), `20-knowledge/${folder}`, "font-weight:600;font-size:0.88em;");
  el(kH, "span", { text: `${files.length}`, attr: { style: "margin-left:auto;opacity:0.38;font-size:0.74em;background:var(--background-secondary);padding:1px 7px;border-radius:8px;" }});
  for (const f of files.sort((a,b) => b.stat.mtime - a.stat.mtime).slice(0, 4)) {
    const row = div(kCard, "font-size:0.8em;padding:2px 0;display:flex;align-items:center;gap:4px;");
    const a = document.createElement("a");
    a.textContent = f.basename; a.href = f.path;
    a.setAttribute("data-href", f.path); a.classList.add("internal-link");
    row.appendChild(a);
    if (Date.now() - f.stat.mtime <= THREE_DAYS_MS) {
      const dot = document.createElement("span");
      dot.textContent = "●";
      dot.style.cssText = "color:var(--interactive-accent);font-size:0.5em;opacity:0.8;flex-shrink:0;";
      row.appendChild(dot);
    }
  }
  if (files.length > 4) el(kCard, "div", { text: `+${files.length-4} more`, attr: { style: "opacity:0.35;font-size:0.75em;margin-top:3px;" }});
}

// ── 6B · LIBRARY ─────────────────────────────────────────
const libWrap = div(midLeft, S.card);
label(libWrap, "Library");

const bkFiles = allFiles.filter(f => f.path.startsWith("40-library/bookmarks/") && f.extension === "md");
const byDomain = {};
for (const f of bkFiles) {
  const d = f.path.replace("40-library/bookmarks/","").split("/")[0];
  if (!byDomain[d]) byDomain[d] = [];
  byDomain[d].push(f);
}
const domains = Object.entries(byDomain).sort((a,b) => b[1].length - a[1].length);
const chipRow = div(libWrap, "display:flex;flex-wrap:wrap;gap:5px;margin-bottom:10px;");
for (const [domain, files] of domains.slice(0, 10)) {
  const a = document.createElement("a");
  a.textContent = `${domain} (${files.length})`;
  a.href = `40-library/bookmarks/${domain}`;
  a.setAttribute("data-href", `40-library/bookmarks/${domain}`);
  a.classList.add("internal-link");
  a.style.cssText = "padding:3px 10px;background:var(--background-primary);border-radius:14px;font-size:0.78em;text-decoration:none;";
  libWrap.querySelector("div").appendChild(a);
}
el(libWrap, "div", { text: `${bkFiles.length} bookmarks · ${domains.length} domains`, attr: { style: "opacity:0.35;font-size:0.74em;margin-bottom:10px;" }});

const libLinks = [
  { icon:"🎬", label:"Movies",   href:"40-library/movies"   },
  { icon:"📖", label:"Books",    href:"40-library/books"    },
  { icon:"📄", label:"Papers",   href:"40-library/papers"   },
  { icon:"📦", label:"Datasets", href:"40-library/datasets" },
  { icon:"📚", label:"Courses",  href:"40-library/courses"  },
];
const llGrid = div(libWrap, "display:grid;grid-template-columns:1fr 1fr;gap:4px;");
for (const l of libLinks) {
  const r = div(llGrid, S.row);
  el(r, "span", { text: l.icon });
  lnk(r, l.label, l.href);
}

// ── 6C · SKILLS — uses prefetched skill contents ──────────
const skWrap = div(midGrid, S.card);
label(skWrap, "Skills");
const CAT_MAP = [
  ["Dev",       /mcp|build|server|git|code|coding|dev|typescript|python|agent|remote|chrome|frontend|netlify|d3|remotion/i, "💻"],
  ["System",    /system|disk|process|service|port|security|update|organiz|file|network|backup|log|cron/i, "🖥"],
  ["Knowledge", /obsidian|vault|note|project|skill|manager|bookmark|seo|session/i, "📓"],
  ["Research",  /search|web|fetch|http|api|intel/i, "🔍"],
  ["Media",     /audio|voice|speech|music|video|frame|clip|obs|image|photo|visual|pdf/i, "🎬"],
  ["Comms",     /telegram|slack|chat|message/i, "💬"],
];
const skillCats = {};
for (let i = 0; i < allSkills.length; i++) {
  const file    = allSkills[i];
  const content = skillContents[i] || "";
  const desc = (content.match(/^description:\s*(.+)/m) || [])[1] || "";
  const name = file.parent.name;
  let cat = "Other", icon = "🔧";
  for (const [l,r,e] of CAT_MAP) { if (r.test(desc)||r.test(name)) { cat=l; icon=e; break; } }
  if (!skillCats[cat]) skillCats[cat] = { icon, items: [] };
  skillCats[cat].items.push({ name, path: `50-system/skills/${name}/SKILL`, mtime: file.stat.mtime });
}
const skGrid = div(skWrap, "display:grid;grid-template-columns:1fr 1fr;gap:8px;");
for (const [cat, data] of Object.entries(skillCats).sort((a,b) => b[1].items.length - a[1].items.length)) {
  const sc = div(skGrid, S.chip);
  const sh = div(sc, "display:flex;align-items:center;gap:5px;margin-bottom:7px;");
  el(sh, "span", { text: data.icon });
  el(sh, "span", { text: cat, attr: { style: "font-weight:600;font-size:0.85em;" }});
  el(sh, "span", { text: `${data.items.length}`, attr: { style: "margin-left:auto;opacity:0.38;font-size:0.74em;background:var(--background-secondary);padding:1px 7px;border-radius:8px;" }});
  for (const s of data.items.sort((a,b) => a.name.localeCompare(b.name)).slice(0, 5)) {
    const sRow = div(sc, "font-size:0.8em;padding:2px 0;display:flex;align-items:center;gap:4px;");
    const a = document.createElement("a");
    a.textContent = s.name; a.href = s.path;
    a.setAttribute("data-href", s.path); a.classList.add("internal-link");
    sRow.appendChild(a);
    if (Date.now() - s.mtime <= THREE_DAYS_MS) {
      const dot = document.createElement("span");
      dot.textContent = "●";
      dot.style.cssText = "color:var(--interactive-accent);font-size:0.5em;opacity:0.8;flex-shrink:0;";
      sRow.appendChild(dot);
    }
  }
  if (data.items.length > 5) el(sc, "div", { text: `+${data.items.length-5} more`, attr: { style: "opacity:0.35;font-size:0.75em;margin-top:3px;" }});
}
el(skWrap, "div", { text: `${allSkills.length} skills total`, attr: { style: "opacity:0.3;font-size:0.73em;margin-top:8px;text-align:right;" }});

// ═══════════════════════════════════════════════════════
//  7 · FOOTER
// ═══════════════════════════════════════════════════════
el(root, "div", { text: "MemVault · Powered by Dataview + Obsidian", attr: { style: "text-align:center;opacity:0.2;font-size:0.7em;padding:8px 0 2px;" }});

// ── Fade in once DOM is fully built ──────────────────────
dv.container.style.transition = "opacity 0.18s ease";
dv.container.style.opacity    = "1";
```