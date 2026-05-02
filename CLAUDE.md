# MemVault — Operating Schema

**For:** Claude Code, Codex, opencode, and other AI assistants
**Purpose:** Maintain a compounding knowledge system that gets smarter with use

---

## How This Vault Works

MemVault implements the **Compounding Knowledge Pattern** — a structured approach where an AI agent doesn't just retrieve information, it actively maintains and grows a knowledge graph in Obsidian. Every source you add, every question you ask, and every insight the agent produces gets synthesized into durable wiki pages that compound over time. The vault is the persistent artifact. Conversations are ephemeral; the wiki is permanent.

**The agent writes; the human curates.** You decide what sources matter and which answers to keep. The agent does the summarizing, cross-referencing, filing, and bookkeeping that makes a knowledge base actually useful over time.

**Three operations:**

- **Ingest** — A source arrives. The agent reads it, extracts key information, updates relevant pages across the wiki, and adds the source to the library. A single article might update 5-10 pages.
- **Query** — You ask a question. The agent searches the wiki, synthesizes an answer with citations, and files any valuable new insights back as wiki pages.
- **Lint** — Periodically check for orphans, stale claims, missing links, and contradictions. The wiki stays healthy because maintenance is cheap for the agent.

---

## Routing Rules

| Content Type | Destination |
|---|---|
| Unprocessed capture | `00-inbox/` |
| Daily log | `10-notes/10-daily/YYYY-MM-DD.md` |
| Idea or brainstorm | `10-notes/20-ideas/` |
| Meeting notes | `10-notes/30-meetings/` |
| AI providers | `20-knowledge/ai/providers/` |
| AI models | `20-knowledge/ai/models/` |
| AI concepts | `20-knowl30-projects |
| AI tools | `20-knowledge/ai/tools/` |
| Tech platforms | `20-knowledge/tech/` |
| Business knowledge | `20-knowledge/business/` |
| Active project docs | `30-projects-active/YYYY-name/` |
| Bookmarks / saved pages | `40-library/bookmarks/` |
| Books, papers, courses | `40-library/` |
| Session artifacts | `50-system/conversations/` |
| Completed work | `90-archive/` |

**Rule:** If unsure, use `00-inbox/` with tag `#agent-review`. Never create new top-level directories. See `VAULT_MANIFEST.json` for the full routing map.

---

## Ingest Workflow

When new content arrives:

1. **Extract** — identify key entities, concepts, facts
2. **Route** — determine destination using the routing table
3. **Synthesize** — create or update wiki pages with the new information
4. **Connect** — add `[[wikilinks]]` to related pages
5. **Index** — update the relevant `*-index.md` file

New agent-created content goes to `00-inbox/` first with `#agent-review`. Human reviews and moves to permanent location.

**Critical:** Don't just store — always connect. A bookmark without links to related knowledge is a dead end. A concept page without cross-references is an island. The value compounds through links.

---

## Query Workflow

When answering questions:

1. **Search** — read relevant `*-index.md` files first
2. **Drill** — follow wikilinks to specific pages
3. **Synthesize** — combine information from multiple sources
4. **Cite** — reference specific files (`path/to/file.md`)
5. **File back** — if the answer generates new insights, write them to `20-knowledge/`

---

## File Conventions

**Naming:** `kebab-case-descriptive.md` — no spaces, no dates unless time-bound

Examples:
- `retrieval-augmented-generation.md` (knowledge page)
- `2026-05-02.md` (daily note — date prefix required)
- `_template-project.md` (template — underscore prefix)

**Frontmatter (required on knowledge files):**
```yaml
---
title: "Page Title"
description: "One-line summary (≤120 chars)"
created: YYYY-MM-DD
tags:
  - status/active
  - type/note
---
```

**Links:** Use `[[filename]]` or `[[filename|Display Text]]` — link liberally

**Tags:** `status/` · `type/` · `#p0` through `#p3` · `#agent-review`

---

## The Three Layers

| Layer | Folders | Rule |
|---|---|---|
| **Capture** | `00-inbox/`, `10-notes/` | Ephemeral — raw thoughts, daily logs, unprocessed |
| **Knowledge** | `20-knowledge/`, `12-mocs/`, `30-projects-active/` | Curated — agent-maintained, interlinked, evergreen |
| **Reference** | `40-library/`, `_assets/` | Immutable — sources stay as-is, never modify |

Raw sources are never modified — the agent reads them and writes synthesized knowledge. The knowledge layer is where all the compounding happens.

---

## Tips

1. **Before creating, check if it exists** — search indices first
2. **Prefer updating over duplicating** — extend existing pages
3. **Link everything** — connections are as valuable as content
4. **Maintain indices** — they are the entry point for discovery
5. **Log your actions** — append to daily notes and project logs
6. **Ask before archiving** — don't move files without confirmation
7. **Never just store** — always connect to existing knowledge

---

> *The vault is not a filing cabinet. It's a living system that gets smarter with every interaction.*