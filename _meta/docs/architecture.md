---
title: "Vault Architecture"
description: "How MemVault is structured and why"
created: 2026-01-01
tags:
  - type/docs
---

## Core Philosophy

MemVault follows the **LLM Wiki pattern**: AI agents maintain interlinked markdown files that compound over time. Raw sources feed the knowledge graph; the graph grows smarter with each interaction.

> *Never just store — always connect.*

---

## Three-Layer Architecture

| Layer | Folders | Purpose |
|---|---|---|
| Raw Sources | `00-inbox`, `10-notes`, `40-library` | Immutable captures — never modify source files |
| Knowledge Graph | `20-knowledge`, `30-projects`, `12-mocs` | AI-maintained, interlinked evergreen knowledge |
| System | `50-system`, `_meta` | Agent rules, state, templates, scripts |

---

## Folder Reference

| Folder | Purpose | Example content |
|---|---|---|
| `00-inbox/` | Unprocessed captures | Quick notes, URLs to review |
| `10-notes/10-daily/` | Daily notes | `2026-01-01.md` |
| `10-notes/20-ideas/` | Ideas and brainstorms | Concept drafts |
| `10-notes/30-meetings/` | Meeting notes | Decisions, action items |
| `10-notes/50-personal/` | Personal notes (gitignored) | Private journal entries |
| `12-mocs/` | Maps of Content | Domain wayfinding pages |
| `20-knowledge/ai/` | AI knowledge | Providers, models, concepts, tools |
| `20-knowledge/tech/` | Tech platforms | Supabase, Render, Fly.io |
| `20-knowledge/business/` | Business knowledge | Pricing models, operations |
| `20-knowledge/concepts/` | General concepts | Mental models, frameworks |
| `30-projects/` | Active project docs | Specs, decisions, logs |
| `40-library/` | Reference library | Books, bookmarks, movies |
| `50-system/` | Agent infrastructure | Scripts, state, logs, config |
| `50-system/conversations/` | Session artifacts | Research, summaries (transient) |
| `_meta/templates/` | Page templates | `_template-project.md` |
| `90-archive/` | Cold storage | Completed/inactive projects |
| `_meta/docs/` | Vault documentation | Architecture, token efficiency, troubleshooting |
| `_meta/claude-versions/` | CLAUDE.md variants | Alternative operating schemas |
| `_assets/` | Media assets | Images, PDFs, attachments |
| `50-system/skills/` | Agent skills | Extensible skill definitions |

---

## Routing Rules

Agents use `VAULT_MANIFEST.json` at the vault root to determine where to store content. The manifest defines canonical routes for all content types.

**Default rule:** when in doubt, route to `00-inbox/` with the `#agent-review` tag. Never create new top-level directories.

---

## Identity Layer

| File | Purpose |
|---|---|
| `SOUL.md` | Agent values and vault hard rules |
| `USER.md` | Human profile (name, timezone, preferences) |
| `AGENTS.md` | Session checklist for AI agents |
| `CLAUDE.md` | Vault operating schema (routing, workflows) |
| `IDENTITY.md` | Agent persona (name, tone) |
| `VAULT-ARCHITECTURE.md` | Naming and tag conventions |

---

## Quality Standards

**Knowledge pages:**
- Fact-checked and properly attributed
- Cross-referenced to related pages
- Updated when new information arrives
- No orphan pages — every page must be reachable

**Project pages:**
- Current status clearly stated at the top
- Decision log maintained
- Next actions identified

**Index files:**
- One-line summary per entry
- Organized by category
- Updated after every major ingest
