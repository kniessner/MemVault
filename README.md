# MemVault

MemVault is a structured Obsidian vault designed to work with AI agents. It implements the [LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): raw sources flow in, the AI synthesizes and links them, and the result is a knowledge graph that compounds over time. The human curates; the agent maintains.

## Quickstart

### Path A — Agent setup (no terminal needed)

1. **Clone or download** this repository into a folder of your choice
2. **Open the folder in Obsidian** — File → Open Vault → select the folder
3. **Start your AI agent** from inside the vault directory
4. The agent reads `BOOTSTRAP.md` and guides you through a short Q&A to personalize the vault
5. Done — `BOOTSTRAP.md` is deleted when setup is complete

### Path B — CLI setup

```bash
python3 init.py        # guided setup
python3 init.py --dry-run   # preview without writing
```

Requires Python 3.8+ (pre-installed on macOS and Linux). On Windows, use WSL — the script explains how.

---

## What You Get

| Folder | Purpose |
|---|---|
| `00-inbox/` | Quick-capture landing zone — dump anything here first |
| `10-notes/` | Daily notes, ideas, meeting logs, personal notes |
| `12-mocs/` | Maps of Content — curated wayfinding pages between domains |
| `20-knowledge/` | Evergreen knowledge: AI, tech, business, concepts |
| `30-projects/` | Active project docs, specs, and decision logs |
| `40-library/` | Bookmarks, books, papers, media |
| `50-system/` | Agent rules, scripts, state files |
| `90-archive/` | Completed projects and cold storage |
| `_meta/` | Templates and vault metadata |

## Key Files

| File | Purpose |
|---|---|
| `SOUL.md` | Agent identity and behavioral rules |
| `USER.md` | Your profile — name, timezone, preferences |
| `AGENTS.md` | Session checklist for AI agents |
| `CLAUDE.md` | Vault operating schema and routing rules |
| `MEMORY.md` | Top-level index linking all vault branches |
| `IDENTITY.md` | Agent persona (name, emoji, vibe) |
| `TOOLS.md` | Environment reference: SSH, API keys, research tools |
| `BOOTSTRAP.md` | First-run setup ritual (deleted after use) |

## CLAUDE.md Variants

Three versions of the operating schema are included — pick the one that fits:

| Version | File | Description |
|---|---|---|
| Starter (default) | `CLAUDE.md` | Clean, minimal — everything a new vault needs |
| Full | `_meta/claude-versions/CLAUDE-A-full.md` | Adds lint workflow and quality checklists |
| Template | `_meta/claude-versions/CLAUDE-C-template.md` | Used by `init.py` for personalized generation |

See `_meta/claude-versions/README.md` for how to swap versions.

## Further Reading

- [`_meta/docs/architecture.md`](./_meta/docs/architecture.md) — how the vault works
- [`_meta/docs/token-efficiency.md`](./_meta/docs/token-efficiency.md) — conventions for lean AI context
- [`VAULT-ARCHITECTURE.md`](./VAULT-ARCHITECTURE.md) — naming conventions, tag taxonomy, workflows
