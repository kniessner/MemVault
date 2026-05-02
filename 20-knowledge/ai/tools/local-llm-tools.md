---
title: Local LLM Tools
category: tools
tags: [local, comparison, deployment, opensource]
---

# Local LLM Tools

*Run AI on your own hardware — no cloud required, no data leaves your machine.*

---

## Quick Comparison

| Tool | Interface | Difficulty | Best For | Open Source |
|------|-----------|------------|----------|-------------|
| **Ollama** | CLI | ⭐ Easy | Quick start, scripting, OpenClaw | ✅ MIT |
| **llama.cpp** | CLI/C++ | ⭐⭐ Moderate | Maximum performance, customization | ✅ MIT |
| **LM Studio** | GUI | ⭐ Easy | GUI lovers, model comparison | ✅ Free |
| **GPT4All** | GUI | ⭐ Easy | Desktop users, privacy-focused | ✅ MIT |
| **LocalAI** | API | ⭐⭐⭐ Hard | API compatibility, enterprise | ✅ GPL |
| **KoboldCPP** | GUI/Web | ⭐⭐ Moderate | Roleplay, creative writing | ✅ AGPL |
| **vLLM** | API | ⭐⭐⭐ Hard | High-throughput serving | ✅ Apache |
| **Tabby** | API/IDE | ⭐⭐ Moderate | Code completion, self-hosted Copilot | ✅ Apache |

---

## Categories

### 🚀 Getting Started

**Ollama** — The "just works" choice
- One command install
- Pre-packaged models
- Perfect for beginners
- Integrates with OpenClaw

**LM Studio** — GUI-first approach
- Beautiful native interface
- Model browser from HuggingFace
- Side-by-side comparisons
- Local server mode

**GPT4All** — Privacy-focused
- Nomic AI's desktop app
- Runs entirely offline
- Cross-platform
- Free and open source

### ⚡ Power Users

**llama.cpp** — The Foundation
- Maximum performance
- Lowest-level control
- Zero dependencies
- Quantization king

**vLLM** — Production Serving
- PagedAttention for throughput
- Multi-GPU support
- OpenAI-compatible API
- Designed for servers

### 🏢 Enterprise/Self-Hosted

**LocalAI** — API Compatibility
- Drop-in OpenAI replacement
- Multiple backends (llama.cpp, transformers)
- Docker-first deployment
- Config-driven

**Tabby** — Code Intelligence
- Self-hosted GitHub Copilot alternative
- Code completion
- Repository indexing
- IDE extensions

### 🎭 Specialized

**KoboldCPP** — Creative Writing
- Optimized for roleplay
- SillyTavern integration
- Novel/erotica friendly
- GPU acceleration

**Text Generation WebUI** — (oobabooga)
- Gradio-based interface
- Extensive extensions
- LoRA support
- Text adventure mode

---

## Decision Tree

```
Just starting out?
├── Want GUI?
│   ├── LM Studio → Best GUI
│   └── GPT4All → Privacy focused
└── OK with CLI?
    └── Ollama → Best ecosystem

Need maximum performance?
├── llama.cpp → Optimize everything
└── vLLM → High-throughput serving

Deploying for team/company?
├── LocalAI → OpenAI API compatible
└── vLLM → Production scale

Coding assistant?
├── Tabby → GitHub Copilot alternative
├── Continue.dev → IDE extension
└── Ollama + OpenClaw → General purpose

Creative writing/RP?
└── KoboldCPP → Optimized for fiction
```

---

## Hardware Considerations

### Minimum (CPU only)
- 8GB RAM → 1B-3B models
- 16GB RAM → 7B models

### Recommended (GPU)
- 8GB VRAM → 7B-13B models (Q4)
- 16GB VRAM → 70B models (Q4)
- 24GB+ VRAM → 70B-405B models

### Inference Speed
| Setup | Tokens/sec (7B) |
|-------|-----------------|
| CPU (8 cores) | 5-10 |
| Apple M1 Pro | 30-50 |
| RTX 3060 | 40-60 |
| RTX 4090 | 100-150 |

---

## Privacy Comparison

All tools here run **100% locally** — no data sent to cloud. Differences:

| Tool | Telemetry | Updates |
|------|-----------|---------|
| Ollama | Opt-in anonymous | Automatic |
| llama.cpp | None | Manual |
| LM Studio | ? | Manual |
| GPT4All | None | Manual |
| LocalAI | None | Manual |

---

## Integration with OpenClaw

Best options for OpenClaw:

1. **Ollama** — Native integration (`ollama launch openclaw`)
2. **llama.cpp server** — OpenAI-compatible API
3. **LM Studio** — Local server mode
4. **LocalAI** — Drop-in OpenAI replacement

Recommended models for OpenClaw:
- `glm-4.7-flash` (~25GB VRAM, local)
- Cloud alternatives: `kimi-k2.5`, `minimax-m2.5`

See [Ollama + OpenClaw](../providers/ollama.md) for setup.

---

## Related

- [Ollama](../providers/ollama.md)
- [llama.cpp](llama-cpp.md)
- [LM Studio](../providers/lm-studio.md)

---

*Last updated: 2026-03-05*
