---
url: https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent
title: Pi Coding Agent
description: Minimal terminal coding harness - adapt to your workflows without forking
created: 2026-04-10
author: Mario Zechner
license: MIT
version: 0.66.1
npm: "@mariozechner/pi-coding-agent"
category: Coding Agents
tags:
  - bookmark
  - coding-agent
  - terminal
  - cli
  - typescript
  - extensible
  - mcp-alternative
---

# Pi Coding Agent

![Pi Logo](https://shittycodingagent.ai/logo.svg)

**A minimal terminal coding harness. Adapt pi to your workflows, not the other way around.**

## What It Is

Pi is a terminal-based AI coding agent by Mario Zechner (creator of libGDX). Unlike other agents that dictate workflows, Pi is aggressively extensible—you customize it via TypeScript extensions, skills, prompt templates, and themes without modifying core internals.

## Philosophy: Opinions by Omission

Pi ships with powerful defaults but intentionally skips features other tools bake in:

| Feature | Pi's Approach |
|---------|---------------|
| **MCP** | Not built-in. Build CLI tools with READMEs (Skills) or add MCP via extensions |
| **Sub-agents** | Not built-in. Spawn via tmux or build your own with extensions |
| **Permission popups** | Not built-in. Run in container or build confirmation flows with extensions |
| **Plan mode** | Not built-in. Write plans to files or build with extensions |
| **To-dos** | Not built-in. They confuse models—use TODO.md or build with extensions |
| **Background bash** | Not built-in. Use tmux for full observability |

**Core principle:** If you want it, build it or install a package that does it your way.

## Four Operating Modes

| Mode | Use Case |
|------|----------|
| **Interactive** | Default TUI with editor, commands, session tree |
| **Print** (`-p`) | One-shot: `pi -p "refactor this file"` |
| **JSON** (`--mode json`) | Programmatic integration, event streaming |
| **RPC** (`--mode rpc`) | Process integration over stdin/stdout |
| **SDK** | Embed in your own apps |

## Key Features

### Extension System
TypeScript modules that extend Pi with:
- Custom tools (or replace built-in ones)
- Custom commands and keyboard shortcuts
- Event handlers
- UI components (custom editors, status lines, overlays)
- Sub-agents, plan mode, MCP servers
- Games while waiting (yes, Doom runs in Pi)

```typescript
export default function (pi: ExtensionAPI) {
  pi.registerTool({ name: "deploy", ... });
  pi.registerCommand("stats", { ... });
  pi.on("tool_call", async (event, ctx) => { ... });
}
```

### Skills (Agent Skills Standard)
On-demand capability packages following [agentskills.io](https://agentskills.io):

```markdown
<!-- SKILL.md -->
# Code Review Skill
Use this skill when asked to review code.

## Steps
1. Check for security issues
2. Look for performance problems
3. Suggest improvements
```

Invoke via `/skill:name` or let the agent auto-load them.

### Prompt Templates
Reusable prompts as Markdown files:

```markdown
<!-- review.md -->
Review this code for bugs, security issues, and performance problems.
Focus on: {{focus}}
```

Type `/review` to expand in chat.

### Sessions & Branching
Sessions stored as JSONL with tree structure (id/parentId). Navigate history:
- **`/tree`** — Jump to any point in session, branch in-place
- **`/fork`** — Create new session from current branch
- **`/compact`** — Manual context compaction
- **Auto-compaction** — Triggers on context overflow

### Package Ecosystem
Install extensions, skills, prompts, themes via npm or git:

```bash
pi install npm:@foo/pi-tools
pi install git:github.com/user/repo
pi install https://github.com/user/repo@v1
pi list
pi update
pi config  # enable/disable resources
```

Packages install to `~/.pi/agent/` (global) or `.pi/` (project-local).

## Built-in Tools

Default: `read`, `bash`, `edit`, `write`

Optional: `grep`, `find`, `ls`

Extensions can add or replace tools entirely.

## Provider Support

**Subscriptions:** Claude Pro/Max, ChatGPT Plus/Pro (Codex), GitHub Copilot, Gemini CLI, Antigravity

**API Keys:** Anthropic, OpenAI, Azure, Google, Amazon Bedrock, Mistral, Groq, Cerebras, xAI, OpenRouter, Vercel AI Gateway, Hugging Face, Kimi, MiniMax, and more.

Custom providers via `~/.pi/agent/models.json` or extensions.

## Quick Start

```bash
npm install -g @mariozechner/pi-coding-agent

# API key
export ANTHROPIC_API_KEY=***
pi

# Or OAuth subscription
pi
/login
```

## Interactive Mode

From top to bottom:
1. **Startup header** — shortcuts, loaded AGENTS.md, skills, extensions
2. **Messages** — user messages, assistant responses, tool calls, errors
3. **Editor** — input area (border color = thinking level)
4. **Footer** — working dir, session name, tokens, cost, context usage, model

### Editor Features
- `@` — fuzzy file search
- Tab — path completion
- Shift+Enter — multi-line
- Ctrl+V — paste images
- `!command` — run bash, send output to LLM
- `!!command` — run bash, don't send

### Commands

| Command | Description |
|---------|-------------|
| `/login`, `/logout` | OAuth auth |
| `/model` | Switch models (Ctrl+L) |
| `/settings` | Thinking level, theme, transport |
| `/tree` | Session tree navigation |
| `/fork` | Fork current session |
| `/compact [prompt]` | Compact context |
| `/resume` | Browse previous sessions |
| `/share` | Upload as private GitHub gist |
| `/reload` | Reload extensions, skills, prompts |

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| Ctrl+C | Clear editor |
| Ctrl+C x2 | Quit |
| Escape | Cancel/abort |
| Escape x2 | Open `/tree` |
| Ctrl+L | Model selector |
| Ctrl+P / Shift+Ctrl+P | Cycle scoped models |
| Shift+Tab | Cycle thinking level |
| Ctrl+O | Collapse/expand tool output |
| Ctrl+T | Collapse/expand thinking blocks |

## Context Files

Pi loads `AGENTS.md` (or `CLAUDE.md`) from:
- `~/.pi/agent/AGENTS.md` (global)
- Parent directories (walking up from cwd)
- Current directory

Replace system prompt: `.pi/SYSTEM.md` (project) or `~/.pi/agent/SYSTEM.md` (global)

## Session Sharing for OSS

Mario encourages sharing public OSS sessions to improve models:

```bash
# Install share tool
pi install git:badlogic/pi-share-hf

# Publish sessions to Hugging Face
pi share-hf
```

Dataset: [badlogicgames/pi-mono on HF](https://huggingface.co/datasets/badlogicgames/pi-mono)

## vs Other Agents

| | Pi | Claude Code | Codex | Hermes |
|---|-----|-------------|-------|--------|
| **Philosophy** | Minimal core, you extend | Full-featured | Full-featured | Full-featured |
| **MCP** | Via extension | Native | Native | Native |
| **Sub-agents** | Via extension | Native | Native | Native |
| **Plan mode** | Via extension/skills | Native | Native | Native |
| **Extensibility** | TypeScript extensions | Limited | Limited | Skills/tools |
| **Self-hostable** | Yes | No | No | Yes |

## Why It's Interesting

1. **Philosophy of omission** — Other agents bundle features you might not want. Pi lets you compose your own.
2. **Aggressive extensibility** — Extensions can replace core tools, add UI components, even run games.
3. **Skills standard** — [agentskills.io](https://agentskills.io) is a promising interoperability format.
4. **Session tree** — Branching/forking without losing history is genuinely useful.
5. **Package ecosystem** — npm/git-based sharing of workflows.
6. **OSS session sharing** — Mario publishes his own work sessions for model training.

## Related

- [[libgdx]] — Mario Zechner's previous famous project
- [[claude-code]] — Comparison target
- [[codex-cli]] — Comparison target
- [[mcp]] — Model Context Protocol (Pi's alternative take)
- [[agentskills]] — Skill standard Pi implements

---

*Source: GitHub — badlogic/pi-mono/packages/coding-agent*
*Captured: 2026-04-10*
