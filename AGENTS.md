# AGENTS.md - Your Workspace

This folder is home. Treat it that way.

## On Session Start — Check First

**If `BOOTSTRAP.md` exists at vault root:** stop. Run the bootstrapping ritual in that file before anything else. It only runs once — the file deletes itself when done.

## Every Session - READ THESE

1. **Read `SOUL.md`** — this is who you are
2. **Read `USER.md`** — this is who you're helping
3. **Read `CLAUDE.md`** — vault navigation guide and structure
4. **Read `TOOLS.md`** — SSH hosts, API keys, devices, web research tools
5. **Read `50-system/AGENTS/workflow.md`** — every session checklist
6. **Read `50-system/AGENTS/data-architecture.md`** — canonical storage rules
7. **Read `10-notes/10-daily/YYYY-MM-DD*.md`** (today + yesterday) for recent context
8. **If in MAIN SESSION**: Also read `MEMORY.md`

**Don't ask permission. Just do it.**

## Quick Reference

| File | Purpose |
|------|---------|
| `50-system/AGENTS/workflow.md` | Every session checklist, skills discovery |
| `50-system/AGENTS/security.md` | Safety rules, boundaries, heartbeats |
| `50-system/AGENTS/orchestration.md` | Subagent protocol, cost tracking, notifications |
| `50-system/AGENTS/data-architecture.md` | Canonical storage map and write rules |
| `50-system/skills/` | Agent skills (obsidian, bookmark, etc.) |
| `TOOLS.md` | Environment-specific notes (SSH, API keys, web research) |

## Memory Structure

- **Daily notes:** `10-notes/10-daily/` — raw logs of what happened
- **Long-term:** `MEMORY.md` — curated memories (main session only)
- **Heartbeat state:** `50-system/state/heartbeat-checks.json`

**Rule:** Write everything down. "Mental notes" don't survive restarts. **Text > Brain**

## Agent Framework Configuration

See your agent framework's docs for workspace configuration.

Set your vault root path in the agent config so the assistant knows where to read and write files (e.g. `~/your-vault`).
