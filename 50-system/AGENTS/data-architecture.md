# Data Architecture — Canonical Storage

## Core Rule

One place per data type. Link, don't duplicate.

## Canonical Branches

| Data Type | Location | Notes |
|---|---|---|
| Quick captures | `00-inbox/` | Tag #agent-review |
| Daily activity | `10-notes/10-daily/` | YYYY-MM-DD.md |
| Ideas | `10-notes/20-ideas/` | Fleeting, not reviewed |
| Meeting notes | `10-notes/30-meetings/` | Distill decisions |
| AI providers | `20-knowledge/ai/providers/` | One file per provider |
| AI models | `20-knowledge/ai/models/` | One file per model |
| AI concepts | `20-knowledge/ai/concepts/` | Atomic, interlinked |
| Tech platforms | `20-knowledge/tech/` | One file per platform |
| Active projects | `30-projects-active/YYYY-name/` | README + decisions + log |
| Bookmarks | `40-library/bookmarks/` | One file per source |
| Books | `40-library/books/` | One file per book |
| Session artifacts | `50-system/conversations/` | Transient — distill within 48h |
| Scripts | `50-system/scripts/` | Shell/Python utilities |
| Runtime state | `50-system/state/` | JSON files |
| Completed work | `90-archive/` | Move, don't delete |

## Write Rules

1. **Capture vs Distill:** Raw thoughts → daily note or inbox. Stable knowledge → 20-knowledge.
2. **Project branching:** Project-specific content stays in `30-projects-active/YYYY-name/`. Multi-project knowledge goes to `20-knowledge/`.
3. **External research:** Bookmark the source, distill reusable conclusions to knowledge pages.
4. **No duplicates:** Check if a note already exists before creating a new one.
5. **File hygiene:** Descriptive names, update existing before creating new.

## Before Writing — Checklist

- [ ] What type of data is this?
- [ ] Where is the canonical location?
- [ ] Does a note already exist for this?
- [ ] Should I link instead of duplicate?
