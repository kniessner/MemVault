---
title: oMLX
description: Native macOS LLM inference server built on MLX with paged SSD KV caching
github: https://github.com/jundot/omlx
download: https://github.com/jundot/omlx/releases
license: Apache 2.0
platform: macOS 15+
category: tool
tags:
  - local-inference
  - mlx
  - apple-silicon
  - kv-cache
  - macos
  - oss
  - claude-code
  - openai-compatible
status: active
requires:
  - Apple Silicon (M1+)
  - macOS 15+
  - 16GB+ RAM (64GB+ recommended)
---

# oMLX

**oMLX** is a native macOS LLM inference server built on Apple's [MLX](https://github.com/ml-explore/mlx) framework. It features **paged SSD KV caching** that dramatically reduces agent response times from 30-90 seconds to under 5 seconds on Apple Silicon Macs.

## Key Differentiator: Paged SSD KV Caching

Traditional local inference tools (Ollama, LM Studio) keep KV cache in memory only. When coding agents shift context mid-session — which happens constantly — the entire cache gets invalidated and must be recomputed from scratch.

**oMLX's solution:**
- Persists every KV cache block to SSD in safetensors format
- Two-tier architecture: hot blocks in RAM, cold blocks on SSD (LRU policy)
- Previously cached prefixes are restored across requests and server restarts
- **TTFT (Time To First Token)**: From 30-90s → **under 5 seconds** on long contexts

## Performance Benchmarks

### Qwen3.5-122B-A10B 4-bit (M3 Ultra 512GB)

| Metric | Value |
|--------|-------|
| Prompt processing | 941 tok/s |
| Token generation | 54-57 tok/s |
| Continuous batching (8×) | 3.36× speedup |
| Peak memory (8k ctx) | 69 GB |

### Continuous Batching Speedup

| Batch Size | Token TPS | Speedup |
|------------|-----------|---------|
| 1× | 56.6 tok/s | 1.00× |
| 2× | 92.1 tok/s | 1.63× |
| 4× | 135.1 tok/s | 2.39× |
| 8× | 190.2 tok/s | 3.36× |

More benchmarks for Qwen3-Coder, MiniMax-M2.5, and GLM-5 available on [omlx.ai](https://omlx.ai).

## Features

### Core
- **Paged SSD KV caching** — Persistent cache across requests and restarts
- **Continuous batching** — Up to 4.14× speedup at 8× concurrency
- **Multi-model serving** — LLM, VLM, embedding, reranker simultaneously
- **LRU eviction** — Automatic memory management when RAM runs low

### API Compatibility
- **OpenAI-compatible** — `/v1/chat/completions` endpoint
- **Anthropic-compatible** — `/v1/messages` endpoint
- **Works with**: Claude Code, OpenClaw, Cursor, any OpenAI-compatible client

### Tool Support
- Multiple tool calling formats: JSON, Qwen, Gemma, GLM, MiniMax
- MCP tool integration
- Tool result trimming for oversized outputs

### Native macOS App
- Menu bar control (start/stop/monitor)
- Web dashboard for model management
- Built-in chat interface
- Real-time metrics
- HuggingFace model browser/downloader
- Signed, notarized, auto-update
- **Not Electron** — native Swift/SwiftUI

## Installation

### macOS App (Recommended)
```bash
# Download DMG from releases
curl -LO https://github.com/jundot/omlx/releases/latest/download/oMLX.dmg
```

Drag to Applications. Welcome screen guides through:
1. Model directory setup
2. Server start
3. First model download

### From Source
```bash
# Clone and install
git clone https://github.com/jundot/omlx
cd omlx && pip install -e .

# Start serving
omlx serve --model-dir ~/models
```

Server runs on `localhost:8000`.

## Configuration

The web dashboard generates config commands for popular tools:

### Claude Code
```bash
# Set oMLX as backend
export ANTHROPIC_API_KEY=dummy
export ANTHROPIC_BASE_URL=http://localhost:8000/v1
claude
```

### OpenClaw
```bash
export OPENAI_API_KEY=dummy
export OPENAI_BASE_URL=http://localhost:8000/v1
openclaw
```

### Cursor
Set API key to `dummy` and base URL to `http://localhost:8000/v1` in Cursor settings.

## Model Support

Any MLX-format model from HuggingFace:

| Model Family | Notes |
|--------------|-------|
| Qwen | Including MoE variants |
| LLaMA | All versions |
| Mistral | Including Mixtral |
| Gemma | Including VLM |
| DeepSeek | Auto `<think>` tag handling |
| MiniMax | Including M2.5 |
| GLM | Including GLM-5 |

**Model formats:** 4-bit, 6-bit, 8-bit quantization supported.

## FAQ

**Q: How is oMLX different from Ollama or LM Studio?**
> Ollama and LM Studio cache KV state in memory. When context shifts (constant with coding agents), cache invalidates and recomputes. oMLX persists every block to SSD — previously cached portions are always recoverable.

**Q: What hardware do I need?**
> Apple Silicon (M1+) with macOS 15+. Minimum 16GB RAM, recommended 64GB+ for larger models. Sweet spot: M-series Pro/Max with 64GB+.

**Q: Do I need to re-download models?**
> No. oMLX reuses your existing LM Studio model directory. Just point it at your models folder.

**Q: Does it work with Vision-Language Models?**
> Yes, since v0.2.0. Same paged SSD caching applies to VLMs.

## Resources

- **Website**: [omlx.ai](https://omlx.ai)
- **GitHub**: [github.com/jundot/omlx](https://github.com/jundot/omlx)
- **Releases**: [github.com/jundot/omlx/releases](https://github.com/jundot/omlx/releases)
- **Benchmarks**: [omlx.ai/benchmarks](https://omlx.ai/benchmarks)

## See Also

- [[tools/llama-cpp|llama.cpp]] — Cross-platform local inference
- [[tools/ollama|Ollama]] — Simple local LLM deployment
- [[tools/claude-code|Claude Code]] — Works as frontend
- [[providers/anthropic|Anthropic]] — Claude model provider
