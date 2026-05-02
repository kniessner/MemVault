---
title: oh-my-codex (OMX)
description: Workflow layer for OpenAI Codex CLI with enhanced prompts, skills, and runtime management
url: https://yeachan-heo.github.io/oh-my-codex-website/
github: https://github.com/Yeachan-Heo/oh-my-codex
npm: https://www.npmjs.com/package/oh-my-codex
author: Yeachan Heo
maintainers:
  - Yeachan Heo
  - HaD0Yun
license: MIT
category: tool
tags:
  - codex
  - openai
  - cli
  - workflow
  - agent
  - coding-assistant
  - tmux
  - nodejs
status: active
requires:
  - Node.js 20+
  - @openai/codex
  - tmux (for team mode)
---

# oh-my-codex (OMX)

**oh-my-codex (OMX)** is a workflow layer for [OpenAI Codex CLI](https://github.com/openai/codex). It enhances the Codex experience without replacing it, adding better prompts, standardized workflows, and durable runtime management.

> *Start Codex stronger, then let OMX add better prompts, workflows, and runtime help when the work grows.*

## Core Philosophy

OMX does **not** replace Codex. It adds a better working layer around it:
- **Codex** does the actual agent work
- **OMX role keywords** make useful roles reusable
- **OMX skills** make common workflows reusable
- **`.omx/`** stores plans, logs, memory, and runtime state

## Installation

```bash
npm install -g @openai/codex oh-my-codex
```

### Requirements

- Node.js 20+
- Codex CLI installed: `npm install -g @openai/codex`
- Codex auth configured
- `tmux` on macOS/Linux (for team runtime)
- `psmux` on native Windows (for team mode)

## Quick Start

### Setup
```bash
omx setup
```

This installs:
- Prompts and skills
- AGENTS.md scaffolding
- `.codex/config.toml`
- OMX-managed native Codex hooks in `.codex/hooks.json`

### Launch (Recommended)
```bash
omx --madmax --high
```

## Canonical Workflow

The main OMX workflow consists of four key skills:

### 1. `$deep-interview` — Clarification
Use when the request or boundaries are unclear:
```
$deep-interview "clarify the authentication change"
```

### 2. `$ralplan` — Planning
Turn clarified scope into an approved architecture:
```
$ralplan "approve the auth plan and review tradeoffs"
```

### 3. `$ralph` — Persistent Completion
Single persistent owner pushing to completion:
```
$ralph "carry the approved plan to completion"
```

### 4. `$team` — Parallel Execution
Coordinated parallel execution for larger tasks:
```
$team 3:executor "execute the approved plan in parallel"
```

## Key Skills Reference

| Skill | Purpose |
|-------|---------|
| `$deep-interview` | Clarifying intent, boundaries, and non-goals |
| `$ralplan` | Approving implementation plan and tradeoffs |
| `$ralph` | Persistent completion and verification loops |
| `$team` | Coordinated parallel execution |
| `/skills` | Browse installed skills and helpers |

## Team Runtime

Durable tmux/worktree coordination for complex tasks:

```bash
# Start team
omx team 3:executor "fix the failing tests with verification"

# Manage team
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

### Platform Requirements for Team Mode

| Platform | Install Command |
|----------|----------------|
| macOS | `brew install tmux` |
| Ubuntu/Debian | `sudo apt install tmux` |
| Fedora | `sudo dnf install tmux` |
| Arch | `sudo pacman -S tmux` |
| Windows | `winget install psmux` |
| Windows (WSL2) | `sudo apt install tmux` |

## Other Commands

### Operator/Support Commands
- `omx doctor` — Verify installation
- `omx hud --watch` — Monitor status
- `omx explore --prompt "..."` — Read-only repository lookup
- `omx sparkshell <command>` — Shell-native inspection

### Examples
```bash
omx explore --prompt "find where team state is written"
omx sparkshell git status
omx sparkshell --tmux-pane %12 --tail-lines 400
```

## Project Structure

```
.omx/
├── plans/          # Approved plans
├── logs/           # Session logs
├── memory/         # Persistent memory
└── state/          # Runtime state

.codex/
├── config.toml     # Codex configuration
└── hooks.json      # Native Codex hook registrations
```

## Known Issues

### Intel Mac: High syspolicyd/trustd CPU
On some Intel Macs, OMX startup with `--madmax --high` can spike CPU while macOS Gatekeeper validates many concurrent process launches.

**Workarounds:**
- `xattr -dr com.apple.quarantine $(which omx)`
- Add terminal app to Developer Tools allowlist in macOS Security settings
- Use lower concurrency (avoid `--madmax --high`)

## Documentation

- [Getting Started](https://github.com/Yeachan-Heo/oh-my-codex/blob/main/docs/getting-started.html)
- [Demo Guide](https://github.com/Yeachan-Heo/oh-my-codex/blob/main/DEMO.md)
- [Agent Catalog](https://github.com/Yeachan-Heo/oh-my-codex/blob/main/docs/agents.html)
- [Skills Reference](https://github.com/Yeachan-Heo/oh-my-codex/blob/main/docs/skills.html)
- [Integrations](https://github.com/Yeachan-Heo/oh-my-codex/blob/main/docs/integrations.html)
- [OpenClaw Integration](https://github.com/Yeachan-Heo/oh-my-codex/blob/main/docs/openclaw-integration.md)

## Community

- **Discord**: [discord.gg/PUwSMR9XNk](https://discord.gg/PUwSMR9XNk)
- **Website**: [yeachan-heo.github.io/oh-my-codex-website/](https://yeachan-heo.github.io/oh-my-codex-website/)

## Core Team

| Role | Name | GitHub |
|------|------|--------|
| Creator & Lead | Yeachan Heo | [@Yeachan-Heo](https://github.com/Yeachan-Heo) |
| Maintainer | HaD0Yun | [@HaD0Yun](https://github.com/HaD0Yun) |

## Top Collaborators

- HaD0Yun ([@HaD0Yun](https://github.com/HaD0Yun))
- Junho Yeo ([@junhoyeo](https://github.com/junhoyeo))
- JiHongKim98 ([@JiHongKim98](https://github.com/JiHongKim98))
- HyunjunJeon ([@HyunjunJeon](https://github.com/HyunjunJeon))

## License

MIT

## Related

- [[providers/openai|OpenAI]]
- [[tools/claude-code|Claude Code]]
- [[../concepts/agents|AI Agents]]
