---
title: Roo Code
url: https://roocode.com
founded: 2024
category: ai-code-assistant
tags: [vscode-extension, ai-coding, open-source, agentic-coding, multi-step]
pricing: free
open_source: true
---

# Roo Code

> "The AI dev team that gets things done"

## Overview

**Roo Code** is an open-source AI coding assistant that puts an entire "AI dev team" directly in your VS Code editor. It provides deep project-wide context, multi-step agentic coding, and unmatched developer-centric flexibility.

| Attribute | Value |
|-----------|-------|
| **Founded** | 2024 |
| **Type** | VS Code Extension |
| **License** | Apache 2.0 |
| **Price** | Free |
| **Repository** | https://github.com/RooVetGit/Roo-Code |

## Key Features

### AI Dev Team
- **Multiple AI Modes** — Switch between different AI personas:
  - **Code** — Writing and editing code
  - **Architect** — Planning and system design
  - **Debug** — Troubleshooting issues
  - **Ask** — General questions
  
### Agentic Coding
- **Multi-step Tasks** — AI breaks down complex tasks and executes them
- **File Context** — Deep understanding of your entire codebase
- **Auto-execution** — Can run commands, modify files, commit changes
- **Self-correction** — Detects errors and retries with fixes

### Flexibility
- **Custom Modes** — Create your own AI personas
- **Model Agnostic** — Works with OpenAI, Anthropic, Google, local models
- **OpenAI-compatible** — Use any OpenAI-compatible API

## VS Code Extension

Install from VS Code marketplace:

```
ext install RooVeterinaryInc.roo-cline
```

Or install from OpenVSX:

```
ext install RooVeterinaryInc.roo-cline
```

## Configuration

```json
{
  "roo.code.apiProvider": "openai",
  "roo.code.apiKey": "sk-...",
  "roo.code.model": "gpt-4o",
  "roo.code.autoApprove": false
}
```

## Comparison with Similar Tools

| Feature | Roo Code | GitHub Copilot | Cursor |
|---------|----------|----------------|--------|
| Price | Free | $10/mo | $20/mo |
| Open Source | ✅ | ❌ | ❌ |
| Multi-step Agents | ✅ | ❌ | ✅ |
| Custom Modes | ✅ | ❌ | Limited |
| Model Choice | Any | OpenAI only | Limited |

## Use Cases

1. **Feature Implementation** — "Add user authentication with JWT"
2. **Refactoring** — "Convert this class to use dependency injection"
3. **Debugging** — "Find and fix the memory leak in this module"
4. **Code Review** — "Review this PR for security issues"
5. **Documentation** — "Generate API docs for these endpoints"

## Related

- [GitHub Repository](https://github.com/RooVetGit/Roo-Code)
- [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=RooVeterinaryInc.roo-cline)
- [Documentation](https://docs.roocode.com)

---

*Last updated: 2026-04-05*