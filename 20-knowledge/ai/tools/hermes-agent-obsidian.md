---
title: "Hermes Agent - Obsidian Plugin"
url: https://anthonymaio.substack.com/p/getting-started-with-hermes-agent
author: Anthony Maio
source: Substack
published: 2025-01-06
category: tool
type: obsidian-plugin
tags: [ai, obsidian, plugin, hermes-agent, knowledge-management, vault-automation]
status: documentation
created: 2025-01-06
---

# Getting Started with Hermes Agent

> Source: [Anthony Maio on Substack](https://anthonymaio.substack.com/p/getting-started-with-hermes-agent)

## Overview

This article by **Anthony Maio** provides a comprehensive guide to getting started with **Hermes Agent**, an AI-powered companion for Obsidian vault management. The guide covers installation, configuration, and basic usage of the Hermes Agent plugin.

## What is Hermes Agent?

Hermes Agent transforms Obsidian from a passive note-taking tool into an active, AI-augmented knowledge management system. It bridges the gap between static knowledge storage and dynamic AI agent capabilities.

**Core Value Proposition:** *Your notes don't just store knowledge — they activate it.*

## Key Features

### Chat Interface
- Persistent sidebar chat panel
- Message threading with persistence to vault
- Tool call visualization with expandable cards
- Multi-agent selector (Hermes, Claude Code, Codex, OpenCode)
- Inline chat widget embedded in notes

### Vault Management Tools
- **`vault_audit`** — 7-phase health check (broken links, duplicates, orphans)
- **`vault_defrag`** — Archive old projects and clean structure
- **`vault_inbox`** — Triage capture folder with PARA suggestions

### Context System
- Active note detection and sync
- Text selection capture
- Multi-note selection for bulk context
- Canvas integration (nodes + edges)
- Backlink awareness with snippets
- Daily note bridge for tasks

### Advanced Systems
- **Task Sync** — Two-way synchronization between agent todos and Obsidian tasks
- **Skills System** — YAML skill definitions with built-in templates
- **Semantic Search** — Embedding-based vault search with similarity matching

## Installation

### Prerequisites
- Obsidian v1.5.0 or later
- Hermes Agent gateway running locally (default: `http://localhost:8642`)
- (Optional) Claude Code CLI for multi-agent support
- (Optional) Codex CLI for OpenAI integration

### Setup Steps

1. **Download the plugin** from GitHub releases
2. **Enable in Obsidian**:
   - Settings → Community Plugins → Browse
   - Search "Hermes Agent"
   - Install and enable
3. **Configure gateway**:
   - Settings → Hermes Agent
   - Set Gateway URL (default: `http://localhost:8642`)
   - Add authentication token if required
4. **Test connection** using the settings tab

## Usage

### Chat Commands
| Command | Function |
|---------|----------|
| `/audit` | Run comprehensive vault health check |
| `/defrag` | Preview vault defragmentation |
| `/inbox` | Triage capture folder items |
| `/help` | Show available commands |

### Keyboard Shortcuts
- `Cmd/Ctrl + Shift + H` — Open Hermes chat
- `Cmd/Ctrl + Shift + A` — Ask about selection
- `Cmd/Ctrl + Shift + Q` — Quick inline chat

### Context Menu
- Right-click selection → "Ask Hermes"
- Right-click selection → "Summarize"
- Right-click selection → "Explain"
- Right-click file → "Summarize with Hermes"

## Configuration Options

### Coding Agents
- **Claude Code** — Enable Anthropic CLI integration
- **Codex** — Enable OpenAI CLI integration
- **OpenCode** — Cloud-based agent (requires API key)

### Feature Toggles
- **Canvas Integration** — Include canvas nodes as context
- **Daily Note Bridge** — Auto-include daily note tasks
- **Task Sync** — Sync agent todos with Obsidian tasks
- **Semantic Search** — Enable embedding-based search

### Advanced Settings
- **Context Depth** — Number of recent notes to include (0-10)
- **Max Selection Length** — Character limit for selection (100-5000)

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   OBSIDIAN HERMES PLUGIN                 │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   CHAT       │  │   CONTEXT    │  │   ACTIONS    │  │
│  │   INTERFACE  │  │   BRIDGE     │  │   ENGINE     │  │
│  │              │  │              │  │              │  │
│  │ • Sidebar    │  │ • Note sync  │  │ • Commands   │  │
│  │ • Inline     │  │ • Selection  │  │ • Skills     │  │
│  │ • Multi-agent│  │ • Canvas     │  │ • Templates  │  │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  │
│         │                 │                 │          │
│         └─────────────────┼─────────────────┘          │
│                           │                            │
│                    ┌──────┴──────┐                     │
│                    │   HERMES    │                     │
│                    │   AGENT     │                     │
│                    │   GATEWAY   │                     │
│                    └─────────────┘                     │
└─────────────────────────────────────────────────────────┘
```

## Best Practices

1. **Regular Audits** — Run `/audit` weekly to maintain vault health
2. **Capture Triage** — Use `/inbox` daily to process 00-cap/active/
3. **Task Integration** — Enable Task Sync for seamless workflow
4. **Context Awareness** — Keep notes in PARA structure for better agent context

## Troubleshooting

### Connection Issues
- Verify gateway is running on correct port
- Check authentication token
- Test connection in settings tab

### Missing Agents
- Ensure CLI tools are installed (claude, codex)
- Check "Check" button in settings for availability

### Performance
- Adjust context depth if slow
- Disable semantic search for large vaults
- Use selection instead of full notes when possible

## Related Resources

- [[OBSIDIAN-HERMES-IMPLEMENTATION-SUMMARY]] — Technical implementation details
- [[HERMES-VAULT-TOOLS]] — Vault management tools documentation
- [[My-Brain-Is-Full-Crew-analysis]] — Inspiration and patterns
- [[hermes-agent]] — Core Hermes agent documentation

## External Links

- Original Article: https://anthonymaio.substack.com/p/getting-started-with-hermes-agent
- Author: Anthony Maio on Substack
- Repository: (Add when publicly available)

---

**Note:** This documentation combines information from Anthony Maio's article with implementation details from the ClaudeVault project.
