---
title: Hermes Agent
url: https://github.com/NousResearch/hermes-agent
source_doc: https://anthonymaio.substack.com/p/getting-started-with-hermes-agent
author: Anthony Maio
founded: 2024
category: ai-agent-framework
tags: [autonomous-agent, open-source, nous-research, local-ai, memory-system, self-improving, messaging-gateway, multi-model]
pricing: free
open_source: true
license: MIT
---

# Hermes Agent

> An open-source, self-improving AI agent that lives on your machine, talks to you through existing chat apps, remembers everything across sessions, and gets smarter the longer you use it.

## Overview

**Hermes Agent** is an open-source autonomous AI agent developed by **Nous Research** (the same group behind the Hermes model family and the Atropos reinforcement learning framework). It's a persistent system that lives on your machine (or VPS, Docker container, or serverless function) and maintains multi-level memory across sessions.

Unlike most AI "agents" that are glorified chatbot wrappers, Hermes Agent is different:
- **Persistent Memory** — Remembers everything across sessions with SQLite-backed storage
- **Self-Improving** — Learns from interactions and auto-generates "skills" (workflows it writes for itself)
- **Multi-Platform** — Talks through Telegram, Discord, Slack, WhatsApp, Signal, Matrix
- **Model Agnostic** — Works with 200+ models via OpenRouter, not locked to any single provider
- **Local-First** — Runs entirely on your hardware or a $5 VPS

| Attribute | Value |
|-----------|-------|
| **Created By** | Nous Research |
| **License** | MIT (the whole thing) |
| **Price** | Free |
| **Repository** | https://github.com/NousResearch/hermes-agent |
| **Hardware Requirements** | Runs on $5 VPS |
| **Model Support** | 200+ via OpenRouter |

## Key Features

### 1. Persistent Memory System

Three-level memory architecture powered by SQLite:

| Level | Scope | Use Case |
|-------|-------|----------|
| **Short-term** | Per-task context | Current conversation flow |
| **Working** | Session persistence | Multi-turn tasks |
| **Long-term** | Cross-session | Preferences, patterns, skills |

### 2. Auto-Generated Skills

The agent recognizes patterns in your requests and writes **skills** (reusable workflows) for itself:
- Repetitive tasks → Automation
- Common patterns → Templates
- Project-specific needs → Custom tools

### 3. Multi-Platform Messaging Gateway

Connect your agent to existing messaging platforms:

| Platform | Status |
|----------|--------|
| Telegram | ✅ |
| Discord | ✅ |
| Slack | ✅ |
| WhatsApp | ✅ |
| Signal | ✅ |
| Matrix | ✅ |
| Home Assistant | ✅ |

### 4. Tool Ecosystem

Built-in tools covering major workflows:
- **Terminal** — Command execution with safety checks
- **File Operations** — Read, write, search, patch files
- **Web Tools** — Search (SearXNG), web extraction (Firecrawl/Trafilatura)
- **Web Browser** — Browserbase automation
- **Code Execution** — Python sandbox with Hermes tools access
- **Subagent Delegation** — Spawn isolated child agents
- **Skills System** — Auto-discover and install skills
- **MCP Support** — Model Context Protocol integration
- **Memory Management** — Persistent memory with search

### 5. Model Flexibility

**Does NOT require a Hermes model.** Bring any model you want:
- OpenAI (GPT-4o, etc.)
- Anthropic (Claude)
- Google (Gemini)
- Local models (Ollama, LM Studio)
- 200+ models via OpenRouter

## Architecture

```
Hermes Agent
├── CLI Interface          # Interactive terminal
├── Gateway Server         # Messaging platform bridge
├── Agent Core             # Conversation loop + planning
├── Tool Registry          # 15+ built-in tools
├── Memory System          # SQLite + FTS5 search
├── Skill System           # Auto-generating workflows
└── MCP Client             # External tool integration
```

## Installation

### Quick Start (Recommended)

```bash
# Install via pip
curl -fsSL https://install.hermes-agent.com | bash

# Or manual install
pip install hermes-agent

# Run setup wizard
hermes setup
```

### Manual Installation (Linux/macOS/WSL2)

```bash
# Clone repository
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -e .

# Run interactive setup
python run_agent.py --setup
```

### Configuration

After setup, configure your provider in `~/.hermes/config.yaml`:

```yaml
provider: openrouter
model: anthropic/claude-3-5-sonnet-20241022
api_key: sk-or-v1-...
```

## Messaging Platform Setup

### Telegram

1. Create bot via @BotFather, get token
2. Add to `~/.hermes/config.yaml`:
   ```yaml
   telegram:
     enabled: true
     bot_token: "YOUR_BOT_TOKEN"
   ```
3. Start gateway: `hermes gateway telegram`

### Discord

1. Create application at Discord Developer Portal
2. Create bot, enable Message Content Intent
3. Add token to config and run: `hermes gateway discord`

### Slack

1. Create app at Slack API
2. Install to workspace, copy Bot User OAuth Token
3. Subscribe to `app_mention` and `message.im` events
4. Start gateway: `hermes gateway slack`

## Safety Features

- **Sandboxed Execution** — Terminal commands run with user permissions
- **Approval Gates** — Dangerous commands require confirmation
- **Ctrl+C** — Kill current task instantly, agent keeps running
- **Skill Sandboxing** — Auto-generated skills are isolated

## Comparison: Hermes Agent vs OpenClaw

| Feature | Hermes Agent | OpenClaw |
|---------|--------------|----------|
| License | MIT | Restrictive |
| Memory | SQLite persistent | Limited |
| Self-Improving | ✅ Auto-skills | ❌ |
| Messaging | 6+ platforms | Discord only |
| Model Choice | 200+ | Limited |
| VPS Cost | $5/mo | Higher |
| Open Source | Fully | Partial |

## Related Projects

- **Nous Research** — https://nousresearch.com
- **Atropos** — RL training framework
- **Hermes Models** — Fine-tuned LLMs
- **Eve** — Anthony Maio's proprietary agent (commercial)

## Resources

- **Getting Started Guide** — https://anthonymaio.substack.com/p/getting-started-with-hermes-agent
- **GitHub Repository** — https://github.com/NousResearch/hermes-agent
- **Documentation** — https://docs.hermes-agent.com

---

*Last updated: 2026-04-06*
*Source: Anthony Maio's Substack article "Getting Started with Hermes Agent"*
