---
title: "Token Efficiency Conventions"
description: "Rules for keeping AI context windows lean and files scannable"
created: 2026-01-01
tags:
  - type/docs
---

## Why This Matters

Agents read vault files on every session. Bloated files waste tokens, increase cost, and reduce coherence — the agent spends its context budget on boilerplate instead of reasoning. Lean files mean faster, cheaper, more accurate sessions.

---

## File Size Limits

| File type | Soft limit | Hard limit |
|---|---|---|
| Agent config (`SOUL.md`, `USER.md`, `AGENTS.md`) | 200 lines | 500 lines |
| `CLAUDE.md` | 300 lines | 600 lines |
| Knowledge page | 150 lines | 400 lines |
| Index file | 100 lines | 200 lines |
| Daily note, session artifact | no limit | — |

When a file approaches its hard limit, split it or archive stale sections to `90-archive/`.

---

## Frontmatter Rules

- **Required:** `title`, `created`, `tags`
- **`description`:** one sentence, ≤ 120 characters — this is what agents read when scanning indices
- **Forbidden:** multi-paragraph descriptions, `author` fields, `version` fields in knowledge pages

---

## What NOT to Put in Agent-Readable Files

- Lengthy onboarding explanations — put those in `docs/` for humans
- Multiple examples of the same pattern — one canonical example is enough
- Deprecated content without a `#status/archived` tag
- Infrastructure details (SSH hosts, IPs, port numbers)
- API keys or tokens (use `.env`)

---

## Naming Conventions

| Pattern | Example |
|---|---|
| Knowledge page | `retrieval-augmented-generation.md` |
| Daily note | `2026-01-01.md` |
| Project folder | `2026-project-name/` |
| Template | `_template-project.md` |
| Meta/hidden | `_process.md` |

---

## Context Window Strategy

- `SOUL.md` + `USER.md` + `AGENTS.md` combined should stay under 4K tokens
- `CLAUDE.md` is operational (routing, workflows), not instructional (tutorials, onboarding)
- Index files are tables of one-line summaries — not content replicas
- Session artifacts in `50-system/conversations/` are transient — distill to `20-knowledge/` within 48h
