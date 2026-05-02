---
url: https://github.com/features/copilot/cli/
title: GitHub Copilot CLI
description: Ask, edit, and generate code directly in your terminal with natural language
source_doc: https://github.com/features/copilot/cli/
created: 2026-04-27
author: GitHub
parent: GitHub Copilot
category: AI Coding Assistants
license: Proprietary
pricing: Included with Copilot ($10-39/mo)
open_source: false
tags:
  - bookmark
  - github
  - copilot
  - cli
  - terminal
  - coding-agent
  - ai-assistant
  - natural-language
---

# GitHub Copilot CLI

> Read, write, and run code where you work—your terminal. Code faster, smarter, together.

## Overview

**GitHub Copilot CLI** extends GitHub Copilot from your IDE into the command line. Ask natural-language questions, get shell commands explained, generate scripts, and get completions directly in your terminal sessions.

| Attribute | Value |
|-----------|-------|
| **Provider** | GitHub (Microsoft) |
| **Parent** | GitHub Copilot |
| **Pricing** | Included with Copilot ($10-39/mo) |
| **Installation** | `gh extension install github/gh-copilot` |
| **Availability** | macOS, Linux, Windows (WSL) |

## Installation

```bash
# Install the GitHub CLI extension for copilot
gh extension install github/gh-copilot

gh auth login
```

## What It Does

| Command | Purpose |
|---------|---------|
| `gh copilot suggest` | Natural-language → shell command suggestions |
| `gh copilot explain` | Explain what a command does |
| `gh copilot generate` | Generate code snippets from prompts |

## Modes

| Mode | Description |
|------|-------------|
| **Interactive** | Conversational mode with follow-up questions |
| **One-shot** | Single query + response |
| **Explain** | Paste a command, get human-readable explanation |
| **Generate** | Describe what you want, get the code |

## Key Features

| Feature | Description |
|---------|-------------|
| **Natural language queries** | "How do I find all .log files modified in the last 24 hours?" |
| **Command explanations** | Paste a complex command, get a breakdown |
| **Interactive follow-up** | Ask clarifying questions to refine results |
| **Shell-agnostic** | Works in bash, zsh, fish, PowerShell |
| **Context-aware** | Considers your current directory and workflow |

## Example Usage

```bash
# Get a command suggestion
gh copilot suggest "deploy my app to AWS"

# Explain a command
gh copilot explain "kubectl get pods -n kube-system"

# Generate a shell script
gh copilot generate "bash script that backs up postgres DB daily"
```

## Integration with GitHub Copilot

| Product | Where It Works |
|---------|----------------|
| **Copilot in IDE** | VS Code, JetBrains, Vim, Neovim |
| **Copilot CLI** | Terminal (your current shell) |
| **Copilot Chat** | IDE sidebar, GitHub.com |
| **Copilot Workspace** | GitHub Issues → PR generation |

## Pricing

| Plan | Price | CLI Access |
|------|-------|-----------|
| **Copilot Individual** | $10/mo ($100/yr) | ✅ Included |
| **Copilot Business** | $19/user/mo | ✅ Included |
| **Copilot Enterprise** | $39/user/mo | ✅ Included |
| **Copilot Free** (limited) | Free | Included |

## Comparison

| | Copilot CLI | Claude Code | Pi | Factory |
|---|-------------|-------------|-----|---------|
| **Scope** | Terminal suggestions | Full coding agent | Coding CLI | Enterprise agents |
| **Integration** | Terminal only | Terminal | Terminal | Everywhere |
| **Depth** | Suggestions + explanations | Full end-to-end tasks | Customizable | Enterprise workflows |
| **Price** | $10-39/mo | Free tier ($15/mo) | Free | Enterprise |

## See Also

- [[github-copilot]] — IDE plugin overview
- [[claude-code]] — Anthropic's CLI agent
- [[pi-coding-agent]] — Mario Zechner's terminal agent
- [[factory-ai]] — Enterprise agent platform

---

*Last updated: 2026-04-27*
