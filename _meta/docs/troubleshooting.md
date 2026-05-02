---
title: "Troubleshooting"
description: "Common problems and fixes for MemVault setup"
created: 2026-01-01
tags:
  - type/docs
---

| Problem | Cause | Fix |
|---|---|---|
| `init.py` fails with "Python not found" | Python 3 not installed or not on PATH | Install Python 3 from python.org or via Homebrew (`brew install python`); verify with `python3 --version` |
| `init.py` fails on Windows | Script uses Unix-style paths | Run in WSL2, or use `py init.py` instead of `python3 init.py`; ensure line endings are LF |
| Agent creates files in wrong location | Agent hasn't read `VAULT_MANIFEST.json` | Explicitly tell the agent: "Read VAULT_MANIFEST.json before creating any files" — or add it to the session prompt |
| Obsidian doesn't show Dataview tables | Dataview plugin not installed or disabled | Install via Settings → Community Plugins → Browse → search "Dataview"; enable it |
| Wikilinks show as broken in Obsidian | Linked file doesn't exist or path is wrong | Check the exact filename (case-sensitive on Linux/WSL); create the missing page or fix the link |
| `.env` not being read by agent | Agent framework doesn't auto-load `.env` | Manually export variables (`export ANTHROPIC_API_KEY=...`) or use `python-dotenv` in your script |
| `init.py` says "vault already initialized" but I want to start over | Init guard file exists from a previous run | Delete `50-system/state/.initialized` (or equivalent guard file) and re-run `init.py` |
