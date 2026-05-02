# MemVault — Full Operating Schema (Version A)

> **This is the full-featured version.** To use: copy this file to your vault root and rename it `CLAUDE.md`.
> Current vault root `CLAUDE.md` is the Starter version (B). Swap if you want the full schema.

**For:** Claude Code, Codex, opencode, and other AI assistants
**Purpose:** Maintain a compounding knowledge system that gets smarter with use

---

## Core Philosophy

This vault follows the **LLM Wiki pattern**: Raw sources feed into an AI-maintained knowledge graph that compounds over time. The AI handles synthesis; the human handles curation.

**Key principle:** *Never just store — always connect.*

---

## Three-Layer Architecture

### 1. Raw Sources (Immutable)
- `00-inbox/` — Quick captures, unprocessed
- `40-library/` — Books, papers, bookmarks, media
- `10-notes/` — Daily notes, raw thoughts
- Images, PDFs, voice memos

**Rule:** Never modify source files. Extract and synthesize into the knowledge layer.

### 2. Knowledge Graph (AI-Maintained)
- `20-knowledge/` — Curated evergreen knowledge (AI, tech, business, concepts)
- `30-projects/` — Living project docs with specs, decisions, logs
- `12-mocs/` — Maps of Content connecting domains
- `_meta/` — System patterns, templates, schemas

**Rule:** Keep interlinked. Update when new sources arrive. Maintain indices and MOCs.

### 3. Conversation Artifacts (Session-to-Knowledge Pipeline)
- `50-system/conversations/` — AI session artifacts: raw research, intermediate reasoning, session summaries
- These are transient by design — distill into `20-knowledge/` or `40-library/` after review

---

## Operations

### Ingest Workflow

When a new source arrives:

1. **Acknowledge** → Confirm receipt and identify source type
2. **Extract** → Pull key entities, concepts, facts, quotes
3. **Route** → Determine correct destination based on content type
4. **Synthesize** → Create/update wiki pages with new information
5. **Connect** → Add cross-references to related pages
6. **Index** → Update relevant index files
7. **Log** → Append entry to session/project log

**Example ingest flow:**
```
User pastes article about new AI model
→ Extract: provider, model name, specs, pricing
→ Update: 20-knowledge/ai/providers/<provider>.md
→ Create: 20-knowledge/ai/models/<model>.md
→ Update: 20-knowledge/ai/index.md with new entry
→ Link: Related models, competing providers
→ Log: Ingest entry with timestamp
```

### Query Workflow

When answering questions:

1. **Search** → Read relevant index files first
2. **Drill** → Follow links to specific pages
3. **Synthesize** → Combine information from multiple sources
4. **Cite** → Reference specific files and sections
5. **Output** → Format based on question type:
   - Quick answer → Direct response
   - Analysis → Markdown document
   - Comparison → Table
   - Deep dive → New wiki page (file it!)

**Rule:** If the answer generates new insights, file them back into the vault.

### Lint Workflow

Periodically (or on request), health-check the vault:

- [ ] **Orphans** → Pages with no inbound links
- [ ] **Stale claims** → Contradicted by newer sources
- [ ] **Missing pages** → Important concepts mentioned but not documented
- [ ] **Broken links** → References to non-existent pages
- [ ] **Index drift** → Indices not reflecting current content
- [ ] **Contradictions** → Inconsistent information across pages

**Output:** Report with suggested fixes, prioritized by impact.

---

## Routing Rules

| Content Type | Destination | Examples |
|---|---|---|
| Unprocessed capture | `00-inbox/` | Quick notes, URLs to review |
| AI provider info | `20-knowledge/ai/providers/` | Anthropic, OpenAI, Groq |
| AI model specs | `20-knowledge/ai/models/` | Claude 3.7, GPT-4o |
| AI tools/frameworks | `20-knowledge/ai/tools/` | LangChain, llama.cpp |
| AI concepts | `20-knowledge/ai/concepts/` | RAG, agents, prompting |
| Tech platforms | `20-knowledge/tech/` | Supabase, Render |
| Business knowledge | `20-knowledge/business/` | Pricing models, ops |
| Active projects | `30-projects/YYYY-name/` | Code, specs, decisions |
| Daily notes | `10-notes/10-daily/` | YYYY-MM-DD.md |
| Ideas | `10-notes/20-ideas/` | Brainstorms, concepts |
| Meeting notes | `10-notes/30-meetings/` | Discussions, decisions |
| Books/courses | `40-library/` | Reviews, notes |
| Bookmarks | `40-library/bookmarks/` | Saved web pages |
| Maps of Content | `12-mocs/` | Domain wayfinding pages |
| Session artifacts | `50-system/conversations/` | Research, sessions |
| System config | `50-system/` | Scripts, settings, logs |
| Completed work | `90-archive/` | Old projects, cold storage |

**Rule:** Never create new top-level directories. Route to nearest canonical branch. If no fit, use `00-inbox/` with `#agent-review`. See `VAULT_MANIFEST.json` for full routing map.

---

## File Conventions

### Naming
- **Files:** `kebab-case-descriptive-name.md`
- **Projects:** `YYYY-project-name/`
- **Daily:** `YYYY-MM-DD.md`
- **Templates:** `_template-name.md` (underscore prefix = hidden/meta)

### Frontmatter (YAML)
```yaml
---
title: "Page Title"
description: "One-line summary (≤120 chars)"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - status/active
  - type/note
related:
  - "[[related-page]]"
---
```

**Required fields:** title, created
**Recommended:** description, tags, updated

### Body Format
- Headers (`#`, `##`, `###`) for structure
- Tables for comparisons
- Bullet lists for features/options
- Code blocks with language tags
- Wikilinks `[[page-name]]` for internal references

---

## Linking Strategy

- Use `[[filename]]` or `[[filename|Display Text]]`
- Link liberally — the graph view reveals connections
- Connect related concepts, source documents to synthesis pages
- Don't manually maintain backlinks — Obsidian handles these automatically

---

## Quality Standards

### For Knowledge Pages
- [ ] Accurate and fact-checked
- [ ] Properly attributed (sources cited)
- [ ] Cross-referenced to related pages
- [ ] Updated when new information arrives

### For Project Pages
- [ ] Current status clearly stated
- [ ] Decision log maintained
- [ ] Links to relevant resources
- [ ] Next actions identified

### For Indices
- [ ] Comprehensive (all relevant pages listed)
- [ ] One-line summaries for each entry
- [ ] Updated after major changes

---

## Special Files

### Indices (Update After Ingest)
- `20-knowledge/ai/index.md` — AI providers, models, tools
- `30-projects/index.md` — Active projects
- `40-library/index.md` — Books, movies, bookmarks

### Logs (Append-Only)
- `10-notes/10-daily/YYYY-MM-DD.md` — Daily activity
- Project-specific `decisions.md` or `log.md` files

### System Files
- `AGENTS.md` — Agent workspace rules and session checklist
- `SOUL.md` — Agent identity and values
- `VAULT-ARCHITECTURE.md` — Technical conventions
- `CLAUDE.md` — This document
- `VAULT_MANIFEST.json` — Canonical routing (ground truth)

---

## Tips for AI Assistants

1. **Before creating, check if it exists** — search indices first
2. **Prefer updating over duplicating** — extend existing pages
3. **Link everything** — connections are as valuable as content
4. **Maintain indices** — they're the entry point for discovery
5. **Log your actions** — append to relevant log files
6. **Ask before archiving** — don't move files without confirmation
7. **Use templates** — consistency aids discoverability

---

## Obsidian Integration

The human uses Obsidian as the UI for this vault:

- **Graph view** → See connections, find orphans
- **Dataview** → Query frontmatter for dynamic lists
- **Templates** → Consistent page structure
- **Daily notes** → Automatic date-based files

The AI writes; Obsidian displays. The human browses and directs.

---

> *The vault is not a filing cabinet. It's a living system that gets smarter with every interaction.*
>
> Your job: **Synthesize, connect, maintain.**
> Human's job: **Curate, question, think.**
> Together: **Compound knowledge over time.**
