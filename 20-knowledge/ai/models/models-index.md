---
title: AI Models Index
created: 2026-04-05
updated: 2026-04-05
tags:
  - type/index
  - topic/ai
  - topic/model
---

# 🧠 AI Models

*Reference profiles of large language models and their specifications.*

---

## Model Categories

### Text/Chat Models
General-purpose conversational models.

### Reasoning Models
Specialized for complex problem-solving with step-by-step reasoning.

### Multimodal Models
Process text, images, audio, and video.

### Code Models
Optimized for programming and software engineering.

### Embedding Models
Convert text to vector representations for similarity search.

---

## Frontier Model Comparison

| Model | Provider | Context | Input $/1M | Output $/1M | Best For |
|-------|----------|---------|-----------|-------------|----------|
| **Claude 3.7 Sonnet** | Anthropic | 200K | $3.00 | $15.00 | Coding, reasoning |
| **Claude 3.5 Haiku** | Anthropic | 200K | $0.25 | $1.25 | Speed, cost |
| **GPT-4o** | OpenAI | 128K | $2.50 | $10.00 | Multimodal, general |
| **GPT-4o mini** | OpenAI | 128K | $0.15 | $0.60 | Cost efficiency |
| **o3** | OpenAI | 200K | $10.00 | $40.00 | Complex reasoning |
| **o3 mini** | OpenAI | 200K | $1.10 | $4.40 | Fast reasoning |
| **Gemini 2.0 Pro** | Google | 2M | $0.00* | $0.00* | Research, long docs |
| **Gemini 2.0 Flash** | Google | 1M | $0.10 | $0.40 | Fast multimodal |
| **Kimi K2.5** | Moonshot | 256K-1M | ~$0.50 | ~$2.00 | Ultra-long context |

*Experimental pricing

---

## Long Context Models (1M+ tokens)

| Model | Provider | Context | Key Use Case |
|-------|----------|---------|--------------|
| Gemini 2.0 Pro | Google | 2M | Video analysis, books |
| Gemini 1.5 Pro | Google | 2M | Document processing |
| Kimi K1.6 | Moonshot | 2M+ | Codebase analysis |
| Kimi K2.5 1M | Moonshot | 1M | Long conversations |

---

## Local/Open Models

Run on your own hardware:

| Model | Size | Quantized | VRAM Required | Best For |
|-------|------|-----------|---------------|----------|
| Llama 3.3 70B | 70B | Q4 | ~40GB | High quality local |
| Llama 3.1 8B | 8B | Q4 | ~6GB | Consumer GPUs |
| Qwen3 32B | 32B | Q4 | ~20GB | Multilingual |
| DeepSeek-R1 32B | 32B | Q4 | ~20GB | Reasoning |
| Gemma 3 27B | 27B | Q4 | ~16GB | Vision |
| Mistral 7B | 7B | Q4 | ~5GB | Fast, efficient |

---

## Embedding Models

| Model | Provider | Dimensions | Max Tokens | Use Case |
|-------|----------|------------|------------|----------|
| text-embedding-3-large | OpenAI | 3072 | 8191 | General purpose |
| text-embedding-3-small | OpenAI | 1536 | 8191 | Cost-optimized |
| embedding-001 | Google | 768 | 2048 | Multilingual |
| nomic-embed-text | Nomic | 768 | 8192 | Open source |
| bge-m3 | BAAI | 1024 | 8192 | Multilingual |

---

## Documented Models

| Model | Provider | Context | Best For | File |
|-------|----------|---------|----------|------|
| **GPT-4o** | OpenAI | 128K | Multimodal flagship | [[gpt-4o]] |
| **GPT-4o mini** | OpenAI | 128K | Cost-effective, scale | [[gpt-4o-mini]] |
| **o3** | OpenAI | 200K | Complex reasoning | [[o3]] |
| **Claude 3.5 Sonnet** | Anthropic | 200K | Coding, reliability | [[claude-3-5-sonnet]] |
| **Claude 3.5 Haiku** | Anthropic | 200K | Fast, cost-effective | [[claude-3-5-haiku]] |
| **Gemini 1.5 Pro** | Google | 2M | Long context, video | [[gemini-1-5-pro]] |
| **Gemini 1.5 Flash** | Google | 1M | Fast, cheap multimodal | [[gemini-1-5-flash]] |
| **Llama 3.1** | Meta | 128K | Open, self-host | [[llama-3-1]] |
| **DeepSeek-R1** | DeepSeek | 128K | Reasoning, visible CoT | [[deepseek-r1]] |
| **Kimi K2.5** | Moonshot AI | 256K-1M | Ultra-long context | [[kimi-k2-5]] |
| **Mixtral 8x22B** | Mistral AI | 65K | MoE efficiency | [[mixtral-8x22b]] |
| Sonar Deep Research | Perplexity | 128K | Research | [[perplexity-sonar-deep-research]] |

---

## Model Selection Guide

### Best for Coding
1. Claude 3.7 Sonnet (reliability, context)
2. o3/o3 mini (reasoning)
3. Gemini 2.0 Pro (2M context for large codebases)

### Best for Cost-Efficiency
1. GPT-4o mini
2. Gemini 1.5 Flash
3. Claude 3.5 Haiku
4. LLama 3.1 8B (local, free)

### Best for Long Context
1. Gemini 2.0 Pro (2M)
2. Kimi K1.6 (2M+)
3. Claude 3.7 Sonnet (200K)
4. o3 (200K)

### Best for Multimodal
1. Gemini 2.0 Pro (text, image, video, audio)
2. GPT-4o (text, image, audio)
3. Claude 3.5 (text, image)

### Best for Reasoning
1. o3 (complex logic, math)
2. Claude 3.7 Sonnet (agentic tasks)
3. Gemini 2.0 Flash Thinking
4. DeepSeek-R1 (open source)

### Best for Local/Self-Hosted
1. Llama 3.3 70B (best quality)
2. Qwen3 32B (multilingual)
3. Llama 3.1 8B (efficient)
4. Mistral 7B (fast)

---

## Adding a New Model

Template structure:

```markdown
---
title: Model Name
provider: Provider Name
release_date: YYYY-MM-DD
context: 128K
status: active  # active, legacy, deprecated
---

# Model Name

## Overview

...description...

## Specifications

| Attribute | Value |
|-----------|-------|
| Provider | Provider |
| Parameters | XXB |
| Context | XXXK |
| Input Price | $X.XX/M |
| Output Price | $X.XX/M |

## Performance

### Benchmarks

| Benchmark | Score |
|-----------|-------|
| MMLU | XX% |
| HumanEval | XX% |

## Capabilities

- ✅ Feature 1
- ❌ Limitation 1

## Use Cases

...when to use this model...

## API Example

```python
...
```

---

*Last updated: YYYY-MM-DD*
```

---

*Frame models for reference. Check [[20-knowledge/ai/providers/index|provider pages]] for latest pricing.*

*Last updated: 2026-04-05*
