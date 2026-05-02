# CLAUDE.md Versions

Three versions of the vault operating schema. Pick the one that fits your workflow and copy it to the vault root as `CLAUDE.md`.

| Version | File | Best for |
|---|---|---|
| **B — Starter** (current default) | `CLAUDE.md` at vault root | New users — clean, minimal, everything you need |
| **A — Full** | `CLAUDE-A-full.md` | Power users who want the complete schema with lint workflow and quality checklists |
| **C — Template** | `CLAUDE-C-template.md` | Used by `init.py` to generate a personalized CLAUDE.md with `${variable}` substitution |

## How to switch

Replace the vault root `CLAUDE.md` with your preferred version:

```bash
# Switch to Full (Version A)
cp _meta/claude-versions/CLAUDE-A-full.md CLAUDE.md

# Reset to Starter (Version B)
# Just run: python3 init.py
```

## Differences

**Version A adds over B:**
- Full ingest workflow (7 steps vs 5)
- Lint workflow (find orphans, stale claims, broken links)
- Quality checklists for knowledge pages, project pages, indices
- Obsidian integration notes

**Version C adds over B:**
- `${vault_name}`, `${user_name}`, `${agent_name}` placeholders for init.py
- Used automatically when you run `python3 init.py`
