---
title: Kilo AI / KiloCode
url: https://kilo.ai
founded: 2024
category: ai-code-assistant
tags: [vscode-extension, jetbrains, cli, ai-coding, open-source]
pricing: free
open_source: true
---

# Kilo AI / KiloCode

> "The Open Source AI Coding Agent for VS Code, JetBrains, and your CLI"

## Overview

**Kilo AI** (also known as **KiloCode**) is an open-source AI coding agent that works across multiple editors and the command line. It's marketed as "the most popular open source AI coding agent" with support for 500+ models.

| Attribute | Value |
|-----------|-------|
| **Founded** | 2024 |
| **Type** | IDE Extension + CLI |
| **License** | Open Source |
| **Price** | Free |
| **GitHub** | https://github.com/Kilo-Org/kilocode |

## Supported Platforms

- **VS Code** — Full extension available
- **JetBrains** — IntelliJ, PyCharm, WebStorm, etc.
- **CLI** — Command-line interface for terminal use

## Key Features

### Multi-Model Support
- **500+ Models** — Connect to virtually any LLM
- **Local Models** — Ollama, LM Studio support
- **Cloud APIs** — OpenAI, Anthropic, Google, Mistral
- **Custom Endpoints** — Any OpenAI-compatible API

### Secure & Local-First
- **Privacy-focused** — Code stays local when using local models
- **No Data Retention** — Doesn't store your code
- **Self-hosted Options** — Run your own inference

### Developer Experience
- **Natural Language Commands** — "Refactor this function"
- **Code Generation** — Write code from descriptions
- **Code Explanation** — Understand complex codebases
- **Bug Fixing** — Identify and fix issues
- **Test Generation** — Auto-generate unit tests

## Installation

### VS Code
```bash
code --install-extension kilo.kilo-code
```

### JetBrains
Install from JetBrains Marketplace: "KiloCode"

### CLI
```bash
npm install -g @kilo-ai/cli
# or
pip install kilo-ai
```

## Configuration

```json
{
  "kilo.model": "claude-3-5-sonnet-20241022",
  "kilo.apiKey": "sk-ant-...",
  "kilo.provider": "anthropic"
}
```

## CLI Usage

```bash
# Ask a question
kilo "How do I implement JWT auth in Express?"

# Generate code
kilo generate "Create a React component for a login form"

# Review code
kilo review src/auth.js

# Refactor
kilo refactor src/utils.js --prompt "Use async/await instead of callbacks"
```

## Comparison

| Feature | Kilo AI | GitHub Copilot | Cody |
|---------|---------|----------------|------|
| Price | Free | $10-19/mo | Free/Paid |
| Open Source | ✅ | ❌ | Partial |
| IDE Support | VS Code, JetBrains, CLI | VS Code only | VS Code, JetBrains |
| Model Choice | 500+ | OpenAI only | Multiple |
| CLI Available | ✅ | ❌ | ✅ |

## Related

- [Website](https://kilo.ai)
- [GitHub Repository](https://github.com/Kilo-Org/kilocode)
- [Documentation](https://docs.kilo.ai)
- [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=kilo.kilo-code)

---

*Last updated: 2026-04-05*