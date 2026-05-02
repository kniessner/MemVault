---
title: AI Tools Index
created: 2026-04-05
updated: 2026-04-05
tags:
  - type/index
  - topic/ai
  - topic/tools
---

# 🛠️ AI Tools

*Frameworks, SDKs, platforms, and utilities for building AI-powered applications.*

---

## Categories

### Local LLM Deployment
Run models on your own hardware.

### Cloud AI Platforms
Managed inference and hosting.

### AI Development Frameworks
Build applications with LLMs.

### Vector Databases
Store and search embeddings.

### AI Coding Assistants
Tools for software development.

---

## Documented Tools

| Tool | Category | Description | File |
|------|----------|-------------|------|
| Agent Zero | Agent Framework | Autonomous AI agent OS | [[agent-zero]] |
| Claude Code LSP | Coding Assistant | LSP setup guide for Claude Code | [[claude-code-lsp]] |
| claw-code | Coding Agent | Clean-room Claude Code rewrite | [[claw-code]] |
| Factory AI | Enterprise Agents | Agent-native software development platform | [[factory-ai]] |
| Google AI Studio | Prototyping | Web IDE for Gemini models | [[google-ai-studio]] |
| Google Anti-Gravity | Easter Egg | Fun physics demo | [[google-antigravity]] |
| Hermes Desktop | Agent GUI | Native desktop app for Hermes | [[hermes-desktop]] |
| Hermes WebUI | Agent GUI | Browser interface for Hermes | [[hermes-webui]] |
| ITO AI | QA/Testing | Automated PR auditing | [[ito-ai]] |
| Kilo AI | Code Assistant | Open source coding agent | [[kilo-ai]] |
| llama.cpp | Local Inference | C++ inference engine | [[llama-cpp]] |
| Local LLM Tools | Overview | Comparison of local tools | [[local-llm-tools]] |
| Marimo | Python Notebooks | Reactive, Git-friendly Python notebooks | [[marimo]] |
|| Mem0 | Memory Layer | Vector-based AI memory service | [[mem0]] |
|| oMLX | Local Inference | macOS MLX server with SSD KV cache | [[omlx]] |
|| oh-my-codex | Coding Agent | Workflow layer for Codex CLI | [[oh-my-codex]] |
|| OpenCode SDK | SDK | TypeScript client for OpenCode server API | [[opencode-sdk]] |
|| Onyx | Enterprise Search | Open-source AI workplace search | [[onyx]] |
| Obsidian | Knowledge | Note-taking with AI plugins | [[obsidian]] |
| Open WebUI | Web Frontend | Self-hosted LLM interface | [[open-webui]] |
| PageIndex | RAG/Document | Vectorless reasoning-based retrieval | [[pageindex]] |
| Paperclip | Agent Orchestration | Human control plane for AI labor | [[paperclip]] |
| Pi Mono | Agent Toolkit | Monorepo: coding agent, LLM API, TUI, bot | [[pi-mono]] |
| Pi Coding Agent | Coding Agent | Minimal terminal coding harness | [[pi-coding-agent]] |
| Roo Code | Code Assistant | VS Code AI dev team | [[roo-code]] |
| Similar Tools | Comparison | Comprehensive tool comparison | [[similar-tools-comparison]] |
| Polyscope | Code Editor | AI-first coding cockpit | [[polyscope]] |
| VidMuse | Video Generation | AI video creation | [[vidmuse]] |
| Zed | Code Editor | Rust-based AI editor | [[zed]] |

### Data Science & Notebooks
| Tool | Type | Best For |
|------|------|----------|
| **[[marimo]]** | Notebook | Reactive, Git-friendly Python notebooks |
| **Jupyter** | Notebook | Traditional interactive computing |
| **Streamlit** | Web App | Python data apps |
| **Blink** | AI App Builder | Full-stack web/mobile apps from chat, includes cloud infra + agent hosting | [[blink]] |

---

## Quick Reference

### Local Inference
| Tool | Type | Best For | Complexity |
|------|------|----------|------------|
| **Ollama** | CLI/Server | Simplicity, scripting | ⭐ Easy |
| **LM Studio** | Desktop GUI | User-friendly local LLMs | ⭐ Easy |
| **llama.cpp** | Library | Performance, customization | ⭐⭐ Moderate |
| **Text Generation WebUI** | Web Interface | Power users | ⭐⭐ Moderate |
| **vLLM** | Server | High-throughput serving | ⭐⭐⭐ Advanced |

### Cloud Platforms
| Platform | Type | Best For |
|----------|------|----------|
| **OpenAI API** | API | Frontier models |
| **Anthropic API** | API | Claude, safety |
| **Groq** | API | Ultra-low latency |
| **Together AI** | API | Open models |
| **Replicate** | API | Model hosting |
| **Hugging Face** | Hub/Inference | Open source ecosystem |
| **Modal** | Serverless | Custom deployments |

### Frameworks
| Framework | Language | Best For |
|-----------|----------|----------|
| **Agent Zero** | Python | Autonomous agents, OS control |
| **LangChain** | Python/JS | Chaining, agents |
| **LlamaIndex** | Python/JS | RAG systems |
| **OpenClaw/Hermes** | Python | Agent architectures |
| **DSPy** | Python | Prompt optimization |
| **Outlines** | Python | Structured outputs |
| **Guidance** | Python | Constrained generation |

### QA & Testing
| Tool | Type | Best For |
|------|------|----------|
| **ITO AI** | GitHub App | Automated PR auditing |

### Agent Orchestration
| Tool | Type | Best For |
|------|------|----------|
| **[[paperclip]]** | Self-hosted | Autonomous company management with agents |
| **Agent Zero** | Agent Framework | Autonomous AI agent OS |
| **Hermes Agent** | Agent | Open-source multi-platform agent |
| **CrewAI** | Library | Agent teams and workflows |
| **n8n** | Workflow | Automation with AI nodes |

### Enterprise AI
| Tool | Type | Best For |
|------|------|----------|
| **[[factory-ai]]** | Enterprise Platform | Agent-native software development |
| **[[onyx]]** | Enterprise Search | AI workplace knowledge search |
| **Mem0** | Memory Layer | Vector-based AI memory service |
| **ITO AI** | QA/Testing | Automated PR auditing |

### AI Prototyping Platforms
| Tool | Provider | Price | Best For |
|------|----------|-------|----------|
| **[[google-ai-studio]]** | Google | Free | Gemini prototyping, 2M context |
| **OpenAI Playground** | OpenAI | Limited free | GPT model testing |
| **Anthropic Console** | Anthropic | Limited free | Claude prototyping |
| **Hugging Face Spaces** | Community | Free | Open models |

### Vector Databases
| Database | Type | Best For |
|----------|------|----------|
| **Pinecone** | Managed | Production RAG |
| **Weaviate** | OSS/Cloud | Semantic search |
| **Chroma** | OSS | Local development |
| **Qdrant** | OSS/Cloud | Filtering, hybrid |
| **pgvector** | Postgres | SQL-native |
| **Milvus** | OSS | Scale |

### AI Coding Tools
| Tool | Type | Best For | Price |
|------|------|----------|-------|
| **Claude Code** | CLI Agent | Complex tasks, refactoring | Free/Paid |
| **Claude Code LSP** | Setup Guide | Enable LSP for faster code nav | Free |
| **Factory** | Enterprise Platform | Agent-native dev, CI/CD integration | Enterprise |
| **GitHub Copilot** | IDE Plugin | Inline suggestions | $10-39/mo |
| **GitHub Copilot CLI** | Terminal | Natural-language command suggestions | $10-39/mo |
| **Cursor** | AI Editor | Full IDE replacement | $20/mo |
| **Windsurf** | AI Editor | Collaborative coding | $15/mo |
| **Continue** | IDE Plugin | Open source assistant | Free |
| **Aider** | CLI | Pair programming | Free |
| **Kilo AI** | IDE Plugin + CLI | Multi-platform coding | Free |
| **Pi** | CLI Agent | Minimal, extensible coding harness | Free |
| **Polyscope** | AI Code Editor | Autonomous coding cockpit | Unknown |
| **Roo Code** | VS Code Extension | AI dev team modes | Free |
| **Zed** | Code Editor | Native performance | Free |

---

## Selection Guide

### Starting a New AI Project
1. **Proof of concept**: OpenAI/Anthropic APIs
2. **Cost optimization**: Groq + smart caching
3. **Privacy requirement**: Ollama/lm-studio locally
4. **Scale**: Deploy on Modal/together/Replicate

### Building RAG
1. **Quick start**: LlamaIndex + OpenAI
2. **Production**: LangChain + Pinecone/Weaviate
3. **Open source**: LlamaIndex + Chroma/pgvector
4. **Complex**: Custom DSPy pipeline

### Local Development
1. **Just experimenting**: LM Studio
2. **CLI/scripts**: Ollama
3. **Power user**: llama.cpp + custom tooling
4. **API compatible**: Ollama server mode

---

## Resources

- **Providers**: `[[20-knowledge/ai/providers/index|AI Providers]]`
- **Models**: `[[20-knowledge/ai/models/index|AI Models]]`
- **Concepts**: `[[20-knowledge/ai/concepts/index|AI Concepts]]`

---

*Tools for building with AI.*

*Last updated: 2026-04-27 — Added: Factory AI, GitHub Copilot CLI, Marimo, Onyx, Paperclip, Pi Mono*
