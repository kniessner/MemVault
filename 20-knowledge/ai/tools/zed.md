---
title: Zed
url: https://zed.dev
founded: 2021
category: ai-code-editor
tags: [code-editor, rust, ai-assisted, collaborative, high-performance]
pricing: free
open_source: true
---

# Zed

> "The editor designed for performance and collaboration"

## Overview

**Zed** is a high-performance code editor written in **Rust**, designed from the ground up for speed and real-time collaboration. It features built-in AI assistance and multiplayer code editing.

| Attribute | Value |
|-----------|-------|
| **Founded** | 2021 |
| **Developer** | Zed Industries (created by Nathan Sobo, ex-Atom/GitHub) |
| **License** | Open Source (GPL) |
| **Price** | Free |
| **Platforms** | macOS, Linux, Windows (beta) |
| **Written In** | Rust |

## Key Features

### AI Integration
- **Built-in AI Assistant** — Native AI chat panel with context awareness
- **GitHub Copilot Support** — Full Copilot integration for code completion
- **Multi-model Support** — Connect to OpenAI, Anthropic, and other providers
- **Inline Edits** — AI-powered code transformations directly in editor

### Performance
- **Rust-based** — Zero electron, native performance
- **GPU-accelerated** — Uses GPU for rendering smooth UI
- **Instant File Loading** — Handles massive codebases effortlessly
- **Low Memory Usage** — Significantly lighter than VS Code

### Collaboration
- **Real-time Multiplayer** — Multiple cursors, live editing
- **Built-in Channels** — Audio calls + screen sharing
- **Team Presence** — See who's viewing/editing what

## Comparison

| Feature | Zed | VS Code | Cursor |
|---------|-----|---------|--------|
| Native Performance | ✅ | ❌ Electron | ❌ Electron |
| Built-in AI | ✅ | ❌ Extension | ✅ |
| Collaboration | ✅ Native | ❌ Extension | ❌ |
| Rust-based | ✅ | ❌ | ❌ |
| Open Source | ✅ | ✅ | ❌ |

## Installation

```bash
# macOS
curl -fsSL https://zed.dev/install.sh | sh

# Or download from https://zed.dev/download
```

## AI Configuration

Zed supports multiple AI providers:

1. **OpenAI** — GPT-4, GPT-4o
2. **Anthropic** — Claude 3.5 Sonnet, Claude 3 Opus
3. **Google** — Gemini Pro
4. **GitHub Copilot** — Native integration

Settings: `~/.config/zed/settings.json`

```json
{
  "assistant": {
    "default_model": {
      "provider": "openai",
      "model": "gpt-4o"
    }
  }
}
```

## Remote Development

Zed supports SSH-based remote development:

```bash
zed ssh://user@server/path/to/project
```

## Extensions

Zed has a growing extension ecosystem:
- Language servers (LSP)
- Themes
- Custom keymaps
- Vim mode (built-in)

## Related

- [GitHub Repository](https://github.com/zed-industries/zed)
- [Documentation](https://zed.dev/docs)
- [Community](https://discord.gg/zed)

---

*Last updated: 2026-04-05*