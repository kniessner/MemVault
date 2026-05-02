# AGENTS.md — Session Protocol

Read these files in order every session. No shortcuts.

## Boot Sequence (every session)

| # | File | Why |
|---|------|-----|
| 1 | `SOUL.md` | Who you are, what you value, hard boundaries |
| 2 | `USER.md` | Who you're helping, timezone, preferences |
| 3 | `CLAUDE.md` | Routing rules, workflows, file conventions |
| 4 | `TOOLS.md` | API keys, SSH hosts, environment notes |

Optional — read if relevant:
- `50-system/agents/data-architecture.md` — canonical storage rules
- `10-notes/10-daily/YYYY-MM-DD.md` (today) — recent context
- `MEMORY.md` — long-term index (main sessions only)

## First-Run Check

If `BOOTSTRAP.md` exists at vault root: stop and run it. It deletes itself when done.

## Quick Reference

| File | Purpose |
|------|---------|
| `50-system/agents/workflow.md` | Session workflow and skill discovery |
| `50-system/agents/data-architecture.md` | Where every data type lives |
| `50-system/agents/security.md` | Hard boundaries and permissions |
| `50-system/skills/` | Extendable skill definitions |

## Memory

- **Daily notes:** `10-notes/10-daily/` — log what happened
- **Long-term:** `MEMORY.md` — curated index (main sessions only)
- **Rule:** Write everything down. Text > Brain.

## Agent Framework Setup

Set vault root in your agent config. Examples:
- **Claude Code:** works natively — just `cd` into the vault
- **Codex:** reads `AGENTS.md` by convention
- **opencode:** set workspace root in config