# Agent Workflow — Every Session

## On Session Start — Read These

1. **SOUL.md** — your identity and values
2. **USER.md** — who you're helping
3. **CLAUDE.md** — vault navigation and routing rules
4. **TOOLS.md** — environment reference (SSH, API keys, devices)
5. **50-system/agents/data-architecture.md** — canonical storage rules
6. **10-notes/10-daily/YYYY-MM-DD.md** (today's date) — recent context

**Don't ask permission. Just do it.**

## Writing Rules

| Situation | Action |
|---|---|
| New knowledge from research | Draft to `00-inbox/` with `#agent-review` |
| Daily activity log | Append to `10-notes/10-daily/YYYY-MM-DD.md` |
| Session artifacts | `50-system/conversations/` (distill within 48h) |
| Project update | Edit relevant `30-projects-active/YYYY-name/` file |

**Rule:** Write everything down. Mental notes don't survive restarts. **Text > Brain**

## URL Handling

Every URL gets bookmarked immediately. Route to `40-library/bookmarks/` with frontmatter. Use the `bookmark` skill in `50-system/skills/bookmark/`.

## On Session End

- Append summary to today's daily note
- Update MEMORY.md if anything important changed
- Distill any session artifacts in `50-system/conversations/` to `20-knowledge/` if ready
