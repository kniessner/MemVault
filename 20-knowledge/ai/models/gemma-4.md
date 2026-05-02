---
name: Gemma 4
provider: Google DeepMind
license: Apache 2.0
release_date: 2026-04-02
architecture: Dense + MoE
context_window: 128K-256K
url: https://ollama.com/library/gemma4
official_url: https://deepmind.google/models/gemma/
wikipedia: https://en.wikipedia.org/wiki/Gemma_(language_model)
category: Local Models
tags:
  - open-source
  - google
  - gemma
  - vision
  - audio
  - tools
  - thinking
  - moe
  - multimodal
  - ollama
---

# Gemma 4

Google DeepMind's latest open-weights model family, released April 2, 2026. Notable for being the first Gemma release under the permissive Apache 2.0 license (previous versions used the more restrictive Gemma License).

## Key Features

| Feature | Details |
|---------|---------|
| **License** | Apache 2.0 (fully open source) |
| **Capabilities** | Vision, audio (edge models), tools, reasoning/thinking |
| **Context** | 128K (edge models), 256K (26B/31B) |
| **Modalities** | Text, image, video, audio (E2B/E4B only) |
| **Arena Rank** | 31B: 3rd place, 26B: 6th place (text leaderboard) |

## Model Variants

### Edge/Local Models
| Model | Effective Params | Size (Ollama) | Context | Audio | Best For |
|-------|------------------|---------------|---------|-------|----------|
| **E2B** | 2B | 7.2GB | 128K | Yes | Phones, minimal resources |
| **E4B** | 4B | 9.6GB | 128K | Yes | Laptops, tablets, edge devices |

The "E" stands for "effective parameters" — these are optimized for edge deployment with native multimodal support including audio.

### Cloud/Server Models
| Model | Architecture | Size (Ollama) | Context | Audio | Best For |
|-------|--------------|---------------|---------|-------|----------|
| **26B** | MoE (4B active) | ~26B | 256K | No | Balanced performance |
| **31B** | Dense | 9.6GB | 256K | No | Maximum capability |

**Note:** The 26B is a Mixture-of-Experts model with only 4B active parameters per forward pass, making it more efficient than the 31B dense model.

## Ollama Quick Start

```bash
# Edge models (with audio support)
ollama run gemma4:e2b   # 7.2GB - smallest, fastest
ollama run gemma4:e4b   # 9.6GB - balanced edge

# Cloud models (highest capability)
ollama run gemma4:26b   # MoE architecture
ollama run gemma4:31b   # Dense, highest quality
ollama run gemma4:31b-cloud  # Cloud-optimized variant
```

## Capabilities

### Built-in Features
- **Vision** — All variants support image and video input
- **Audio** — E2B and E4B models have native audio input
- **Tools/Functions** — Native tool calling support
- **Thinking** — Reasoning/thought generation (can be disabled)
- **Multilingual** — Supports 140+ languages

### Use Cases
Google designed Gemma 4 for:
- **Reasoning** — Complex problem solving
- **Agentic workflows** — Tool-using agents
- **Coding** — Code generation and analysis
- **Multimodal understanding** — Vision + audio + text

## Architecture Notes

- **Dense models** (E2B, E4B, 31B) — Standard transformer architecture
- **MoE model** (26B) — Mixture-of-Experts with 4B active parameters
- **Vision encoder** — SigLIP (same as Gemma 3)
- **Attention** — Grouped-query attention (GQA)
- **Quantization** — QAT (quantization-aware training) versions available

## Comparison to Gemma 3

| | Gemma 3 | Gemma 4 |
|---|---------|---------|
| License | Gemma License | **Apache 2.0** |
| Audio | No | **Yes (E2B/E4B)** |
| Vision | Yes | Yes |
| Tools | Yes | Yes |
| Context | 128K | **128K-256K** |
| MoE | No | **Yes (26B)** |

## Why It Matters

1. **Truly open** — Apache 2.0 license means commercial use, modification, redistribution all permitted
2. **Edge-first audio** — First open model with native audio support on small parameter counts
3. **Frontier performance** — 31B ranked 3rd on Arena text leaderboard, competing with much larger models
4. **Efficient MoE** — 26B MoE delivers strong performance with only 4B active parameters
5. **Native Ollama support** — Easy local deployment without complex setup

## Related

- [[gemma-3]] — Previous generation
- [[gemma-2]] — Earlier generation
- [[google-deepmind]] — Model developer
- [[ollama]] — Local deployment platform
- [[mixture-of-experts]] — MoE architecture explanation
- [[paligemma]] — Vision-language variant
- [[medgemma]] — Medical domain variant

---

*Source: Google DeepMind, Ollama Library, Wikipedia*
*Captured: 2026-04-10*
*Downloads: 2M+ (Ollama)*
