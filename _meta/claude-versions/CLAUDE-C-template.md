# ${vault_name} — Operating Schema (Version C: Template)

> **This is the template version** used by `init.py`. It contains `${variable}` placeholders
> that are filled in during setup. You can also use this to manually create a customized
> CLAUDE.md — just replace `${vault_name}`, `${agent_name}`, etc. with your values.

**For:** ${agent_frameworks}
**Purpose:** Maintain a compounding knowledge system that gets smarter with use

---

## Core Philosophy

This vault follows the **LLM Wiki pattern**: raw sources feed into an AI-maintained knowledge graph that compounds over time. The AI handles synthesis; the human handles curation.

**Key principle:** *Never just store — always connect.*

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
| AI concepts | `20-knowledge/ai/concepts/` |
| AI tools | `20-knowledge/ai/tools/` |
| Tech platforms | `20-knowledge/tech/` |
| Business knowledge | `20-knowledge/business/` |
| Active project docs | `30-projects/YYYY-name/` |
| Bookmarks / saved pages | `40-library/bookmarks/` |
| Books, papers, courses | `40-library/` |
| Session artifacts | `50-system/conversations/` |
| Completed work | `90-archive/` |

**Rule:** If unsure, use `00-inbox/` with `#agent-review`. Never create new top-level directories. See `VAULT_MANIFEST.json`.

---

## Ingest Workflow

1. **Extract** — identify key entities, concepts, facts
2. **Route** — determine destination using the table above
3. **Synthesize** — create or update wiki pages
4. **Connect** — add `[[wikilinks]]` to related pages
5. **Index** — update the relevant `index.md`

New agent-created content → `00-inbox/` with `#agent-review` first.

---

## Query Workflow

1. **Search** — read relevant `index.md` files first
2. **Drill** — follow wikilinks to specific pages
3. **Synthesize** — combine information from multiple sources
4. **Cite** — reference specific files
5. **File back** — if the answer generates new insights, write them to `20-knowledge/`

---

## File Conventions

**Naming:** `kebab-case-descriptive.md`

**Frontmatter:**
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

**Links:** `[[filename]]` or `[[filename|Display Text]]`

---

## Tips

1. Before creating, check if it exists — search indices first
2. Prefer updating over duplicating
3. Link everything — connections compound value
4. Maintain indices — they are the entry point for discovery
5. Log your actions — append to daily notes

---

> *The vault is not a filing cabinet. It's a living system that gets smarter with every interaction.*
>
> Configured for: ${user_name} · Agent: ${agent_name} · Vault: ${vault_name}
