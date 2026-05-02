---
title: "Adding a New Agent Framework"
description: "How to configure a new AI agent to work with this vault"
created: 2026-01-01
tags:
  - type/docs
---

## What Agents Need

| File | Purpose |
|---|---|
| `CLAUDE.md` | Operating schema — routing rules, workflows, conventions |
| `AGENTS.md` | Session checklist — what to read, how to write |
| `SOUL.md` | Identity and values |
| `VAULT_MANIFEST.json` | Machine-readable routing rules |

Most modern agent frameworks (Claude Code, Codex, opencode) read one of these files automatically at session start. Check your framework's docs for the exact file it reads.

---

## Adding Claude Code

1. Install: `npm install -g @anthropic-ai/claude-code`
2. Run `claude` from the vault root — it reads `CLAUDE.md` automatically.
3. Optional: add a `.claude/settings.json` for permissions and hooks.

---

## Adding Codex (OpenAI)

1. Install: `npm install -g @openai/codex`
2. Run `codex` from the vault root — point it to `AGENTS.md` as context.
3. Set `OPENAI_API_KEY` in `.env`.

---

## Adding opencode

1. Install: `npm install -g opencode-ai` (or via Homebrew)
2. Configure `~/.config/opencode/opencode.json` to point workspace at vault root.
3. Set the appropriate API key in `.env`.

---

## Adding Any Other Framework

1. Identify which instruction file the framework reads (often `AGENTS.md`, `CLAUDE.md`, or a custom path).
2. Ensure that file contains: vault structure rules, routing table, writing conventions.
3. Test by asking the agent: "Where should I store a new AI model knowledge page?" — correct answer: `20-knowledge/ai/models/`.
