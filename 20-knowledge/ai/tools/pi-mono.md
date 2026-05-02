---
url: https://github.com/badlogic/pi-mono
title: pi-mono
source_doc: https://github.com/badlogic/pi-mono#readme
description: AI agent toolkit — coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods
author: Mario Zechner (badlogic)
git_repo: https://github.com/badlogic/pi-mono
license: MIT
category: AI Agent Toolkit
pricing: Free
open_source: true
tags:
  - bookmark
  - monorepo
  - ai-agent-toolkit
  - coding-agent
  - cli
  - tui
  - slack-bot
  - vllm
  - typescript
  - unified-llm-api
---

# pi-mono

> An AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods — all in one monorepo.

## Overview

**pi-mono** is the umbrella monorepo by Mario Zechner (creator of libGDX) containing the full pi ecosystem for building and operating AI agents. It's not just one tool — it's a complete toolkit.

| Package | NPM / Usage | Description |
|---------|-------------|-------------|
| **pi-coding-agent** | `@mariozechner/pi-coding-agent` | Interactive coding agent CLI |
| **pi-agent-core** | `@mariozechner/pi-agent-core` | Agent runtime with tool calling |
| **pi-llm** | `@mariozechner/pi-llm` | Unified multi-provider LLM API |
| **pi-tui** | `@mariozechner/pi-tui` | Terminal UI library with diff rendering |
| **pi-web-ui** | `@mariozechner/pi-web-ui` | Web components for AI chat interfaces |
| **pi-mom** | `@mariozechner/pi-mom` | Slack bot delegating to pi coding agent |
| **pi-pods** | `@mariozechner/pi-pods` | CLI for managing vLLM deployments |

## Philosophy

Pi's approach is **"opinions by omission"** — a minimal core you extend:

| Feature | Pi's Approach |
|---------|-------------|
| **MCP** | Via extensions, not built-in |
| **Sub-agents** | Via extensions |
| **Permission popups** | Run in container or build with extensions |
| **Plan mode** | Write plans to file or extend |
| **To-dos** | Use TODO.md or build with extensions |
| **Background bash** | Use tmux for observability |

## Quick Start

```bash
# Clone the repo
git clone https://github.com/badlogic/pi-mono.git
cd pi-mono

# Install dependencies
npm install
npm run build

# Run the coding agent
npm run pi
```

## pi-llm: Unified LLM API

One interface for multiple providers:

| Provider | Status |
|----------|--------|
| OpenAI | ✅ |
| Anthropic | ✅ |
| Google (Gemini) | ✅ |
| Azure | ✅ |
| Amazon Bedrock | ✅ |
| Mistral | ✅ |
| Groq | ✅ |
| Cerebras | ✅ |
| xAI | ✅ |
| OpenRouter | ✅ |
| Hugging Face | ✅ |
| 20+ more | ✅ |

## pi-coding-agent ([[pi-coding-agent]])

The flagship interactive coding agent:
- TypeScript extensions
- Skills (agentskills.io standard)
- Prompt templates
- Session branching and forking
- Print/JSON/RPC/SKD modes

## Session Sharing

Mario encourages sharing public OSS sessions to improve models:

```bash
# Install share tool
pi install git:badlogic/pi-share-hf

# Publish sessions to Hugging Face
pi share-hf
```

Dataset: [badlogicgames/pi-mono on HF](https://huggingface.co/datasets/badlogicgames/pi-mono)

## Contributing

- Issues and PRs from new contributors are auto-closed by default
- Maintainers review auto-closed issues daily
- See `CONTRIBUTING.md` and `AGENTS.md`

## Related

- [[pi-coding-agent]] — The interactive coding agent (detailed note)
- [[libgdx]] — Mario Zechner's previous famous project
- [[claude-code]] — Comparison target
- [[hermes-agent]] — Open-source alternative

---

*Last updated: 2026-04-27*
