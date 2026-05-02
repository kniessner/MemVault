---
cssclass: dashboard
tags: [type/index, type/dashboard, knowledge]
---

# Knowledge Base

```dataviewjs
const S = {
  card:  `background:var(--background-secondary);border-radius:12px;padding:16px 18px;`,
  row:   `display:flex;align-items:center;gap:8px;padding:6px 10px;background:var(--background-primary);border-radius:6px;font-size:0.85em;`,
  label: `font-size:0.68em;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;opacity:0.4;display:block;margin-bottom:10px;`,
  badge: `margin-left:auto;opacity:0.38;font-size:0.76em;white-space:nowrap;`,
  link:  `text-decoration:none;`,
};
function div(p, s="") { return p.createEl("div", { attr: { style: s }}); }
function lnk(p, t, h, s="") { return p.createEl("a", { text:t, cls:"internal-link", attr:{"data-href":h, href:h, style:S.link+s }}); }

const root = div(dv.container, "display:flex;flex-direction:column;gap:12px;");

// ── Gather knowledge files ──
const knowledgeFiles = app.vault.getFiles().filter(f =>
  f.path.startsWith("20-knowledge/") && f.extension === "md"
);

const knowledgeDirs = {};
for (const f of knowledgeFiles) {
  const parts = f.path.replace("20-knowledge/", "").split("/");
  const dir = parts[0];
  if (dir === "index.md" || dir === "README.md" || dir.startsWith("_")) continue;
  if (!knowledgeDirs[dir]) knowledgeDirs[dir] = { dir, files: [], mtime: 0, entry: null };
  knowledgeDirs[dir].files.push(f);
  if (f.stat.mtime > knowledgeDirs[dir].mtime) knowledgeDirs[dir].mtime = f.stat.mtime;
  const rel = f.path.replace(`20-knowledge/${dir}/`, "");
  if (f.name === "README.md" && !rel.includes("/")) knowledgeDirs[dir].entry = f.path;
  else if (f.name === "index.md" && !rel.includes("/") && !knowledgeDirs[dir].entry) knowledgeDirs[dir].entry = f.path;
  else if (!rel.includes("/") && !knowledgeDirs[dir].entry) knowledgeDirs[dir].entry = f.path;
}
const categories = Object.values(knowledgeDirs).sort((a,b) => b.mtime - a.mtime);

// ── Stats bar ──
const statsBar = div(root, S.card + "display:flex;gap:20px;");
const recent7d = categories.filter(c => (Date.now() - c.mtime) < 7 * 86400000).length;
const stale30d = categories.filter(c => (Date.now() - c.mtime) > 30 * 86400000).length;
const totalFiles = knowledgeFiles.filter(f => !["index.md","README.md","_template.md"].includes(f.name)).length;
for (const [n, l] of [[categories.length, "Categories"], [totalFiles, "Articles"], [recent7d, "Updated (7d)"], [stale30d, "Stale (30d+)"]]) {
  const s = div(statsBar, "text-align:center;flex:1;");
  s.createEl("div", { text: `${n}`, attr: { style: "font-size:1.4em;font-weight:700;" }});
  s.createEl("div", { text: l, attr: { style: "opacity:0.4;font-size:0.75em;text-transform:uppercase;letter-spacing:0.05em;" }});
}

// ── Category cards ──
const wrap = div(root, S.card);
wrap.createEl("span", { text: "Knowledge Categories", attr: { style: S.label }});
const grid = div(wrap, "display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:8px;");

const categoryIcons = {
  "ai": "🤖",
  "business": "💼",
  "concepts": "💡",
  "tech": "⚙️"
};

for (const c of categories) {
  const age = Math.floor((Date.now() - c.mtime) / 86400000);
  const accent = age <= 7 ? "var(--interactive-accent)" : age > 30 ? "var(--text-faint)" : "var(--background-modifier-border)";
  const href = c.entry ? c.entry.replace(/\.md$/, "") : `20-knowledge/${c.dir}`;
  const contentFiles = c.files.filter(f => !["index.md","README.md","_template.md"].includes(f.name));

  const card = div(grid, `background:var(--background-primary);border-radius:10px;padding:14px 16px;border-left:3px solid ${accent};`);

  const header = div(card, "display:flex;align-items:center;gap:6px;margin-bottom:8px;");
  const icon = categoryIcons[c.dir] || "📚";
  header.createEl("span", { text: icon });
  lnk(header, c.dir.charAt(0).toUpperCase() + c.dir.slice(1), href, "font-weight:700;font-size:0.92em;");

  const meta = div(card, "display:flex;justify-content:space-between;opacity:0.45;font-size:0.76em;margin-bottom:8px;");
  meta.createEl("span", { text: `${contentFiles.length} articles` });
  meta.createEl("span", { text: age === 0 ? "today" : age + "d ago" });

  const recentFiles = contentFiles.sort((a,b) => b.stat.mtime - a.stat.mtime).slice(0, 3);
  for (const f of recentFiles) {
    const r = div(card, "padding:2px 0;font-size:0.78em;opacity:0.6;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;");
    r.createEl("span", { text: "· " });
    lnk(r, f.basename, f.path);
  }
}

// ── Recent updates ──
const recentWrap = div(root, S.card);
recentWrap.createEl("span", { text: "Recently Updated", attr: { style: S.label }});
const recentList = div(recentWrap, "display:flex;flex-direction:column;gap:6px;");

const allContentFiles = knowledgeFiles
  .filter(f => !["index.md","README.md","_template.md"].includes(f.name))
  .sort((a,b) => b.stat.mtime - a.stat.mtime)
  .slice(0, 10);

for (const f of allContentFiles) {
  const age = Math.floor((Date.now() - f.stat.mtime) / 86400000);
  const row = div(recentList, S.row);
  const category = f.path.split("/")[1];
  const icon = categoryIcons[category] || "📚";
  row.createEl("span", { text: icon });
  lnk(row, f.basename, f.path);
  row.createEl("span", { text: age === 0 ? "today" : age + "d ago", attr: { style: S.badge }});
}

// ── Links ──
const links = div(root, S.card + "opacity:0.5;font-size:0.82em;");
links.createEl("span", { text: "Related", attr: { style: S.label }});
const linkGrid = div(links, "display:flex;gap:12px;");
lnk(linkGrid, "📦 Projects", "30-projects/index", "font-size:0.85em;");
lnk(linkGrid, "📅 Daily Notes", "10-notes/10-daily", "font-size:0.85em;");
lnk(linkGrid, "📚 Library", "40-library/index", "font-size:0.85em;");
lnk(linkGrid, "🏠 Home", "Home", "font-size:0.85em;");

// ── Quick Actions ──
const actions = div(root, S.card + "font-size:0.82em;");
actions.createEl("span", { text: "Quick Actions", attr: { style: S.label }});
const actionLinks = div(actions, "display:flex;gap:12px;flex-wrap:wrap;margin-top:8px;");
lnk(actionLinks, "🤖 AI", "20-knowledge/ai/index", "font-size:0.85em;");
lnk(actionLinks, "💼 Business", "20-knowledge/business/index", "font-size:0.85em;");
lnk(actionLinks, "💡 Concepts", "20-knowledge/concepts/index", "font-size:0.85em;");
lnk(actionLinks, "⚙️ Tech", "20-knowledge/tech/index", "font-size:0.85em;");
```
