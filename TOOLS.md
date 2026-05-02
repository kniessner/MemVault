# TOOLS.md — Environment Reference

## SSH Hosts

| Alias | Host | User | Notes |
|---|---|---|---|
| myserver | example.host | ubuntu | Home server |

## API Keys

Set these in `.env` (never commit to git):

- `ANTHROPIC_API_KEY` — Claude / Claude Code
- `OPENAI_API_KEY` — Codex / ChatGPT

## Web Research

Priority order: local SearXNG → Web Fetch → Browser search

```
SearXNG (local)    → Primary search (privacy-respecting, no API key needed)
Web Fetch          → Direct URL content extraction
Browser            → Complex/JS sites (last resort)
```

## Custom Commands

_(Add your frequently-used commands here as you discover them)_

Example format:
```
- vault-sync → ~/your-vault/50-system/scripts/sync-vault.sh
- quick-research → ~/your-vault/50-system/scripts/quick-research.sh
```

## Notes

Add your own environment-specific notes here.
