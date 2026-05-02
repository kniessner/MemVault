---
title: llama.cpp
category: inference-engine
tags: [c++, ggml, quantization, optimized]
---

# llama.cpp

> LLM inference in C/C++ — minimal setup, state-of-the-art performance.

## Overview

llama.cpp is the **high-performance foundation** that powers most local LLM tools. Written in plain C/C++ with zero dependencies, it's optimized for maximum inference speed across diverse hardware.

| Attribute | Value |
|-----------|-------|
| **Author** | Georgi Gerganov (@ggerganov) |
| **License** | MIT |
| **Language** | C/C++ |
| **Key Differentiator** | Maximum performance, minimal dependencies |

## Features

### Hardware Optimizations

| Platform | Optimization |
|----------|--------------|
| Apple Silicon | ARM NEON, Accelerate, Metal |
| x86 | AVX, AVX2, AVX512, AMX |
| RISC-V | RVV, ZVFH, ZFH, ZICBOP |
| NVIDIA | Custom CUDA kernels |
| AMD | HIP backend |
| Other | Vulkan, SYCL, Moore Threads (MUSA) |

### Quantization

- **1.5-bit to 8-bit** integer quantization
- Formats: Q4_0, Q4_K_M, Q5_K_M, Q6_K, Q8_0
- Reduce memory by 70%+ with minimal quality loss
- CPU+GPU hybrid inference for large models

### Model Support

- LLaMA (1, 2, 3, 3.1, 3.2, 3.3)
- Mistral / Mixtral MoE
- Qwen, DeepSeek, Phi, Gemma
- DBRX, Jamba, Falcon
- And many more (see full list)

## Installation

```bash
# macOS
brew install llama.cpp

# Nix
nix-shell -p llama-cpp

# Windows
winget install llama.cpp

# Docker
docker run -v /path/to/models:/models ghcr.io/ggml-org/llama.cpp:full
```

## Usage

### CLI

```bash
# Basic generation
llama-cli -m my_model.gguf -p "Hello, world"

# Interactive mode
llama-cli -m my_model.gguf -cnv

# Download from HuggingFace
llama-cli -hf ggml-org/gemma-3-1b-it-GGUF
```

### Server (OpenAI-compatible)

```bash
llama-server -m my_model.gguf --port 8080

# Then use via API
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Hello"}]}'
```

### Web UI

`llama-server` now includes a modern WebUI for browser-based interaction.

## Advanced Features

- **Multimodal** — Vision model support (LLaVA)
- **Function calling** — Tool use capabilities
- **Speculative decoding** — Faster inference
- **Continuous batching** — Multiple concurrent requests
- **Grammar constraints** — Constrained generation

## Ecosystem

| Tool | Based on |
|------|----------|
| Ollama | llama.cpp |
| LM Studio | llama.cpp |
| GPT4All | llama.cpp |
| KoboldCPP | llama.cpp |

## When to Use Directly

- Maximum performance needed
- Custom deployments
- Container/server environments
- Research and experimentation
- Building your own tool

## Links

- [GitHub](https://github.com/ggml-org/llama.cpp)
- [Documentation](https://github.com/ggml-org/llama.cpp/tree/master/docs)
- [ggml library](https://github.com/ggml-org/ggml)
- [VS Code Extension](https://github.com/ggml-org/llama.vscode)
- [Vim Plugin](https://github.com/ggml-org/llama.vim)

---

*Last updated: 2026-03-05*
