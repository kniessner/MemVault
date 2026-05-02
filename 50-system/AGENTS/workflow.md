# Agent Workflow — Every Session

## Boot Sequence

Read in order, no shortcuts:

1. `SOUL.md` — identity and values
2. `USER.md` — who you're helping
3. `CLAUDE.md` — routing rules and workflows
4. `TOOLS.md` — environment reference

Then read today's daily note (`10-notes/10-daily/YYYY-MM-DD.md`) for recent context.

If `BOOTSTRAP.md` exists at vault root: run it first. It deletes itself when done.

## Writing Rules

| Situation | Action |
|---|---|
| New knowledge from research | Draft to `00-inbox/` with `#agent-review` |
| Daily activity log | Append to `10-notes/10-daily/YYYY-MM-DD.md` |
| Session artifacts | `50-system/conversations/` — distill within 48h |
| Project update | Edit relevant `30-projects-active/YYYY-name/` file |
| URL received | Bookmark FIRST — use `50-system/skills/bookmark/` |

**Rule:** Write everything down. Mental notes don't survive restarts. **Text > Brain**

## Skill Discovery

Skills live in `50-system/skills/`. Each has a `SKILL.md` describing when and how to use it.

| Skill | When to Use |
|---|---|
| `obsidian` | Note creation, linking, templates, search, CLI operations |
| `bookmark` | Any URL — scrape, summarize, organize with frontmatter |
| `workspace-init` | Set up environment variables and navigation aliases |
| `file-organizer` | Clean up messy folders, find duplicates, restructure |
| `project-manager` | Create and manage projects in `30-projects-active/` |
| `session-summary` | Summarize current session stats, tools used, cost |
| `file-finder` | Advanced file search by name, size, date, content |
| `quick-backup` | Backup vault directories with compression and verification |

When a message contains a URL: invoke the bookmark skill immediately, before any other task.

## On Session End

- Append summary to today's daily note
- Update MEMORY.md if anything important changed
- Distill session artifacts from `50-system/conversations/` to `20-knowledge/` if ready