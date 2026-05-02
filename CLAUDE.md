# MemVault — Operating Schema

**For:** Claude Code, Codex, opencode, and other AI assistants
**Purpose:** Maintain a compounding knowledge system that gets smarter with use

---

## Core Philosophy

This vault follows the **LLM Wiki pattern**: raw sources feed into an AI-maintained knowledge graph that compounds over time. The AI handles synthesis; the human handles curation.

**Key principle:** *Never just store — always connect.*

---

## Routing Rules

When storing content, use this table:

| Content Type | Destination |
|---|---|
| Unprocessed capture | `00-inbox/` |
| Daily log | `10-notes/10-daily/YYYY-MM-DD.md` |
| Idea or brainstorm | `10-notes/20-ideas/` |
| Meeting notes | `10-notes/30-meetings/` |
| AI providers | `20-knowledge/ai/providers/` |
| AI models | `20-knowledge/ai/models/` |
| AI concepts | `20-knowledge/ai/concepts/` |
| AI tools | `20-knowledge/ai/tools/` |
| Tech platforms | `20-knowledge/tech/` |
| Business knowledge | `20-knowledge/business/` |
| Active project docs | `30-projects/YYYY-name/` |
| Bookmarks / saved pages | `40-library/bookmarks/` |
| Books, papers, courses | `40-library/` |
| Session artifacts | `50-system/conversations/` |
| Completed work | `90-archive/` |

**Rule:** If unsure, use `00-inbox/` with tag `#agent-review`. Never create new top-level directories. See `VAULT_MANIFEST.json` for the full canonical routing map.

---

## Ingest Workflow

When new content arrives:

1. **Extract** — identify key entities, concepts, facts
2. **Route** — determine destination using the table above
3. **Synthesize** — create or update wiki pages with new information
4. **Connect** — add `[[wikilinks]]` to related pages
5. **Index** — update the relevant `index.md` file

New agent-created content goes to `00-inbox/` first with `#agent-review`. Human reviews and moves to permanent location.

---

## Query Workflow

When answering questions:

1. **Search** — read relevant `index.md` files first
2. **Drill** — follow wikilinks to specific pages
3. **Synthesize** — combine information from multiple sources
4. **Cite** — reference specific files (`path/to/file.md`)
5. **File back** — if the answer generates new insights, write them to `20-knowledge/`

---

## File Conventions

**Naming:** `kebab-case-descriptive.md` — no spaces, no dates unless time-bound

**Frontmatter (required on all knowledge files):**
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

**Tag conventions:** `status/` · `type/` · `#p0` through `#p3` · `#agent-review`

---

## Tips

1. **Before creating, check if it exists** — search indices first
2. **Prefer updating over duplicating** — extend existing pages
3. **Link everything** — connections are as valuable as content
4. **Maintain indices** — they are the entry point for discovery
5. **Log your actions** — append to daily notes and project logs
6. **Ask before archiving** — don't move files without confirmation

---

> *The vault is not a filing cabinet. It's a living system that gets smarter with every interaction.*
