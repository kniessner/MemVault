---
title: Groq
url: https://groq.com
founded: 2016
category: inference-provider
tags: [inference, lpu, fast, api, openai-compatible]
pricing: pay-per-token
free_tier: yes
---

# Groq

> "Inference is Fuel for AI" — Groq delivers fast, low-cost inference that doesn't flake when things get real.

![Groq Homepage](assets/groq-homepage.png)

## Overview

Groq is an **inference provider** specializing in ultra-fast AI model serving. Unlike competitors using GPUs, Groq pioneered the **LPU (Language Processing Unit)** — custom silicon purpose-built for inference.

| Attribute | Value |
|-----------|-------|
| **Founded** | 2016 |
| **API Type** | OpenAI-compatible |
| **Free Tier** | ✅ Yes (up to defined limits) |
| **Key Differentiator** | LPU custom hardware, extreme speed |
| **Developer Count** | 3M+ developers and teams |

## LPU Architecture

The **Language Processing Unit (LPU)** is Groq's custom inference chip:

| Feature | Description |
|---------|-------------|
| **Single-Core Design** | On-chip SRAM (hundreds of MB) as primary weight storage, not cache |
| **Custom Compiler** | Static scheduling, deterministic execution |
| **Power Efficiency** | Air-cooled, no complex infrastructure needed |
| **Chip-to-Chip** | Direct connectivity via plesiosynchronous protocol |

**Speed claim:** Llama 3.1 8B at **840+ tokens/sec**

## Pricing (Per 1M Tokens)

### Language Models

| Model | Input | Output | Speed (T/s) | Context |
|-------|-------|--------|-------------|---------|
| **Llama 3.1 8B** | $0.05 | $0.08 | 840 | 128K |
| **GPT OSS 20B** | $0.075 | $0.30 | 1,000 | 128K |
| **Llama 4 Scout** | $0.11 | $0.34 | 594 | 128K |
| **GPT OSS 120B** | $0.15 | $0.60 | 500 | 128K |
| **Llama 4 Maverick** | $0.20 | $0.60 | 562 | 128K |
| **Qwen3 32B** | $0.29 | $0.59 | 662 | 131K |
| **Llama 3.3 70B** | $0.59 | $0.79 | 394 | 128K |
| **Kimi K2-0905 1T** | $1.00 | $3.00 | 200 | 256K |

### Speech & Audio

| Model | Price | Notes |
|-------|-------|-------|
| **Whisper V3 Large** | $0.111/hour | 217x speed factor |
| **Whisper V3 Turbo** | $0.04/hour | 228x speed factor |
| **Orpheus English** | $22/M chars | 100 chars/sec |
| **Orpheus Arabic** | $40/M chars | 100 chars/sec |

### Prompt Caching Discounts

| Model | Cached Input (discount) |
|-------|------------------------|
| GPT OSS 20B | $0.0375 (50% off) |
| GPT OSS 120B | $0.075 (50% off) |
| Kimi K2-0905 | $0.50 (50% off) |

## API Quick Start

```python
import os
import openai

client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

## Key Features

- ✅ OpenAI-compatible API (drop-in replacement)
- ✅ Global data centers for low latency
- ✅ Prompt caching for repeated context
- ✅ Built-in compound systems (web search, code execution)
- ✅ Free tier available

## Notable Customers

- **McLaren F1 Team** — Official partner for real-time AI inference
- **PGA of America** — Performance-critical applications
- **Fintool** — 7.4x speed increase, 89% cost reduction
- **Opennote** — Education-focused AI tools

## Rate Limits (Developer Plan)

| Model | TPM | RPM |
|-------|-----|-----|
| Llama 3.1 8B | 250K | 1,000 |
| Llama 3.3 70B | 300K | 1,000 |
| Whisper Large | 200K ASH | 300 |
| Whisper Turbo | 400K ASH | 400 |

## Related

- [LPU Architecture Deep Dive](https://groq.com/lpu-architecture)
- [Groq Pricing](https://groq.com/pricing)
- [Groq Docs](https://console.groq.com/docs)
- [Model: Llama 3.1 8B](../models/llama-3.1-8b.md) *(create if needed)*

## Recent News

- **Sep 2025**: Raised $750M as inference demand surges
- **Aug 2025**: Day-zero support for OpenAI open models
- **May 2025**: Optimized for MoE & large models

---

*Last updated: 2026-03-05*
