---
title: Hermes Desktop
category: tools
url: https://github.com/fathah/hermes-desktop
founded: 2025
tags: [hermes, desktop, gui, electron, tauri, multi-provider]
pricing: free
license: MIT
platforms: [macos, linux]
---

# Hermes Desktop

> Native desktop application for installing, configuring, and chatting with Hermes Agent.

![Hermes Desktop Header](https://github.com/user-attachments/assets/80585955-3bae-4aee-af90-a1e61757ccb8)

## Overview

Hermes Desktop provides a **graphical interface** for Hermes Agent, wrapping the CLI functionality in a native desktop experience. It handles installation, configuration, and day-to-day usage through a unified GUI rather than terminal commands.

| Attribute | Value |
|-----------|-------|
| **Repository** | github.com/fathah/hermes-desktop |
| **Platforms** | macOS (.dmg), Linux (.AppImage, .deb) |
| **Stack** | Likely Tauri/Electron (native wrapper) |
| **License** | MIT |
| **Status** | Active development (beta) |

## Features

### Installation & Setup
- Guided first-run install with progress tracking
- Automatic dependency resolution
- Uses official Hermes install script (`install.sh`)
- Installs to `~/.hermes`

### Multi-Provider Support
Supports 12+ providers out of the box:
- OpenRouter, Anthropic, OpenAI
- Google (Gemini), xAI (Grok)
- Nous Portal, Qwen, MiniMax
- Hugging Face, Groq
- Local endpoints (LM Studio, Ollama, vLLM, llama.cpp)

### Chat Interface
| Feature | Description |
|---------|-------------|
| **Streaming** | SSE streaming with live responses |
| **Tool Progress** | Visual indicators during tool execution |
| **Markdown** | Full markdown rendering |
| **Syntax Highlighting** | Code blocks with language detection |

### Slash Commands (22 total)

| Command | Purpose |
|---------|---------|
| `/new` | Start new session |
| `/clear` | Clear current chat |
| `/fast` | Enable fast mode |
| `/web` | Web search context |
| `/image` | Image generation mode |
| `/browse` | Browser tool mode |
| `/code` | Code-focused mode |
| `/shell` | Shell command mode |
| `/usage` | Token/cost statistics |
| `/help` | Show available commands |
| `/tools` | Tool configuration |
| `/skills` | Skill management |
| `/model` | Model switcher |
| `/memory` | Memory management |
| `/persona` | Persona switcher |
| `/version` | Version info |
| `/compact` | Compact mode |
| `/compress` | Compress context |
| `/undo` | Undo last action |
| `/retry` | Retry last request |
| `/debug` | Debug mode |
| `/status` | System status |

### Token Tracking
- Live prompt/completion token counts
- Cost display in chat footer
- Usage statistics via `/usage` command

### Session Management
- Project organization
- Tag-based filtering
- Session history browser

## Installation

### macOS
```bash
# Download .dmg from releases
# Install to /Applications

# Fix code-signing issue (not notarized)
xattr -cr "/Applications/Hermes Agent.app"
# Or: Right-click → Open → Open
```

### Linux
```bash
# AppImage
chmod +x Hermes-Desktop.AppImage
./Hermes-Desktop.AppImage

# Or .deb
sudo dpkg -i hermes-desktop.deb
```

## Storage Locations

Uses same paths as CLI:
```
~/.hermes/
├── config.yaml       # Settings
├── .env              # API keys
├── sessions/         # Conversation history
└── skills/           # User skills
```

## Memory Integration

- `/memory` command to manage user memory
- Same native memory as CLI (no external provider)
- No Mem0 or semantic search integration (yet)

## Comparison: Desktop vs CLI vs WebUI

| Feature | CLI | Desktop | WebUI |
|---------|-----|---------|-------|
| Learning curve | Higher | Lower | Medium |
| Terminal feel | Full | None | Some |
| File preview | Basic | Good | Good |
| Token visualization | Text | Graphical | Graphical |
| Keyboard shortcuts | Full | Partial | Browser |
| Resource usage | Lowest | Higher | Medium |
| Offline capable | Yes | Yes | No* |

*WebUI requires server, but can work offline if server is local

## Use Cases

| User Type | Recommendation |
|-----------|----------------|
| Terminal-native | ❌ Use CLI |
| GUI preference | ✅ Desktop |
| New to Hermes | ✅ Desktop (guided setup) |
| Multi-provider setup | ✅ Desktop (easy switching) |
| Low-resource system | ❌ Use CLI |

## GitHub Activity

- **Releases:** Regular builds at github.com/fathah/hermes-desktop/releases
- **Issues:** Active bug reporting and feature requests
- **Contributing:** Open to PRs

## MacOS Security Note

The app is **not code-signed or notarized**. Apple will block it on first launch.

**Workaround:**
```bash
xattr -cr "/Applications/Hermes Agent.app"
```

Or manually approve via System Preferences → Security & Privacy.

## Related

- [Hermes WebUI](./hermes-webui.md) — Browser-based alternative
- [Hermes Agent](../providers/hermes-agent.md) — Core framework
- [CLI Setup](../../getting-started/hermes-cli-setup.md) — Terminal setup guide

---

*Archived: 2026-04-19*  
*Source: GitHub repository README*
