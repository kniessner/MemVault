---
title: Hermes WebUI
url: https://github.com/nesquena/hermes-webui
founded: 2025
category: tools
tags: [hermes, web-ui, browser, interface, python, vanilla-js]
pricing: free
license: MIT
---

# Hermes WebUI

> Web browser interface for Hermes Agent — full CLI parity without the terminal.

![Hermes WebUI Screenshot](https://github.com/user-attachments/assets/6bf8af4c-209d-441e-8b92-6515d7a0c369)

## Overview

Hermes WebUI is a lightweight, dark-themed web application that provides **1:1 parity with the Hermes CLI experience** through a browser. No build step, no framework, no bundler — just Python and vanilla JavaScript.

| Attribute | Value |
|-----------|-------|
| **Repository** | github.com/nesquena/hermes-webui |
| **Stack** | Python backend + vanilla JS frontend |
| **License** | MIT |
| **Cost** | Free |
| **Setup** | Single command |

## Layout

Three-panel design:
- **Left:** Sessions sidebar + navigation + Hermes Control Center
- **Center:** Chat interface with streaming responses
- **Right:** Workspace file browser with inline preview

### Composer Footer
Always-visible controls at bottom:
- Model selector
- Profile switcher  
- Workspace controls
- **Token context ring** — circular indicator showing token usage

## Features

| Feature | Description |
|---------|-------------|
| **Session Management** | Projects, tags, tool call cards |
| **File Browser** | Navigate workspace with inline file preview |
| **Token Tracking** | Live prompt/completion counts |
| **Profile Support** | Full multi-profile switching |
| **Settings** | Password protection, display customization |
| **Light/Dark Mode** | Theme toggling |
| **SSH Tunnel Access** | Secure remote access |

## Installation

```bash
# Clone repo
git clone https://github.com/nesquena/hermes-webui.git
cd hermes-webui

# Start server (Python)
python server.py

# Access via SSH tunnel for security
ssh -L 8080:localhost:8080 your-server
```

## Access

```
Local:    http://localhost:8080
Tunneled: http://localhost:8080 (via SSH)
```

## Comparison to CLI

| Feature | CLI | WebUI |
|---------|-----|-------|
| Slash commands | ✅ | ✅ |
| Session persistence | ✅ | ✅ |
| File workspace | ✅ | ✅ (with preview) |
| Token tracking | ✅ | ✅ (visual ring) |
| Model switching | ✅ | ✅ |
| Profile management | ✅ | ✅ |
| Multi-platform | Terminal only | Browser-based |

## Memory Integration

Uses same `~/.hermes/` storage as CLI:
- `memory` tool → User notes
- `user` profile → Preferences
- Sessions → SQLite persistence
- Skills → `~/.hermes/skills/`

**Not a memory enhancement** — just a different interface.

## Use Cases

| Scenario | Recommendation |
|----------|----------------|
| Prefer GUI over terminal | ✅ Use WebUI |
| Need inline file preview | ✅ Use WebUI |
| Want visual token tracking | ✅ Use WebUI |
| Low-resource environment | ❌ Use CLI |
| Air-gapped/offline | ❌ Use CLI |

## Related

- [Hermes Desktop](./hermes-desktop.md) — Native desktop app alternative
- [Hermes Agent](../providers/hermes-agent.md) — Core agent framework
- [Agent Memory Systems](../concepts/agent-memory-systems.md) — Memory architecture

---

*Archived: 2026-04-19*  
*Source: GitHub repository analysis*
