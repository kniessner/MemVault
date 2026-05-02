# Security — Agent Boundaries

## Hard Rules

- **Private things stay private.** Never read or reference `10-notes/50-personal/` unless explicitly asked.
- **Never send half-baked replies** to any external messaging surface.
- **Ask before acting externally.** Web searches are fine. Sending emails, posting, or modifying shared services requires explicit user permission.
- **Never commit secrets to git.** API keys and tokens live in `.env` only.
- **Confirm before deleting.** Suggest archiving to `90-archive/` instead.
- **You're a guest.** Treat access to the user's files with respect.

## What You Can Do Without Asking

- Read any file in the vault (except `10-notes/50-personal/`)
- Create or update notes in `00-inbox/`, `10-notes/`, `20-knowledge/`, `30-projects-active/`, `40-library/`, `50-system/`
- Run read-only shell commands
- Append to daily notes and logs
- Bookmark URLs using the bookmark skill

## What Requires Explicit Permission

- External API calls beyond web search
- Sending messages (email, Telegram, Slack, etc.)
- Modifying shared infrastructure
- Deleting files (suggest archive instead)
- Accessing `10-notes/50-personal/`

## Session Boundary Rules

- **Session artifacts** (`50-system/conversations/`) are transient. Distill useful knowledge to `20-knowledge/` within 48 hours, then delete the raw artifact.
- **Daily notes** (`10-notes/10-daily/`) can be auto-appended but never auto-deleted.
- **Inbox items** (`00-inbox/`) must be reviewed by a human before moving to permanent branches. Tag with `#agent-review` and leave them.