---
title: Mixtral 8x22B
provider: Mistral AI
release_date: 2024-04-17
context: 65000
status: active
tags: [model, mistral, open-weight, moe]
---

# Mixtral 8x22B

> Mistral's MoE powerhouse — 141B total parameters with only 39B active per token, delivering frontier performance at efficient inference cost.

## Overview

Mixtral 8x22B uses Sparse Mixture of Experts (MoE) architecture with 8 expert networks. Only 2 experts are active per token, making it as fast as a 39B model while having 141B total parameters worth of knowledge.

| Attribute | Value |
|-----------|-------|
| **Provider** | Mistral AI |
| **Release** | April 2024 |
| **Architecture** | Sparse Mixture of Experts (MoE) |
| **Total Parameters** | 141 billion |
| **Active Parameters** | 39 billion |
| **Experts** | 8 (2 active per token) |
| **Context** | 65K tokens |
| **License** | Apache 2.0 |

---

## Specifications

| Capability | Description |
|------------|-------------|
| **Text** | ✅ Native |
| **Multilingual** | ✅ 12+ languages |
| **Code** | ✅ Strong |
| **Math** | ✅ Good |
| **Function Calling** | ✅ Available |
| **Long Context** | ✅ 65K |

---

## Performance Benchmarks

| Benchmark | Mixtral 8x22B | Llama 2 70B | GPT-3.5 |
|-----------|---------------|-------------|---------|
| MMLU | 77.8% | 69.9% | 70.0% |
| HumanEval | 64.6% | 29.9% | 48.1% |
| MATH | 49.8% | 13.8% | 34.1% |
| BBH | 81.3% | 76.8% | 70.1% |

**Outperforms Llama 2 70B while being faster to run.**

---

## MoE Architecture

```
Input Token
     ↓
Router → Selects 2 of 8 Experts
     ↓
Expert A (17.5B params) ──┐
                          ├─ Combine → Output
Expert B (17.5B params) ──┘
     ↑
Only 39B params active!
```

**Benefits:**
- Larger total knowledge (141B)
- Faster inference (39B active)
- Lower VRAM than dense 141B model

---

## Pricing (API)

| Provider | Input | Output |
|----------|-------|--------|
| **Mistral API** | $2.00/M tokens | $6.00/M tokens |
| **Together AI** | $1.80/M tokens | $5.40/M tokens |
| **Groq** | $0.27/M tokens | $0.27/M tokens |
| **Local (free)** | VRAM cost | VRAM cost |

---

## API Example

```python
from openai import OpenAI

# Mistral API
client = OpenAI(
    api_key="your-mistral-key",
    base_url="https://api.mistral.ai/v1"
)

response = client.chat.completions.create(
    model="open-mixtral-8x22b",
    messages=[{"role": "user", "content": "Explain quantum computing"}]
)

# Groq (ultra-fast)
client = OpenAI(
    api_key="your-groq-key",
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="mixtral-8x22b-instruct",
    messages=[{"role": "user", "content": "Write a Python function"}]
)
# 500+ tokens/sec

# Local with Ollama
# ollama pull mixtral:8x22b
```

---

## Use Cases

### Best For
- ✅ **Cost-efficient inference** — MoE efficiency
- ✅ **Multilingual apps** — 12+ languages
- ✅ **Code generation** — Strong performance
- ✅ **Open deployment** — Apache 2.0 license
- ✅ **High-throughput APIs** — Groq integration
- ✅ **Research** — Full weights available

### Not For
- ❌ Maximum reasoning (use Claude/o3)
- ❌ Ultra-long context (65K limit)
- ❌ Vision tasks (text only)
- ❌ Native tool use (not as polished)

---

## Hardware Requirements

| Setup | VRAM | Notes |
|-------|------|-------|
| **Q4 quantization** | ~80 GB | Single A100 80GB |
| **Q4 + offloading** | ~48 GB + RAM | A6000 or dual GPU |
| **8-bit** | ~160 GB | Dual A100 |
| **Full precision** | ~320 GB | Multi-node |

---

## Fine-tuning

```python
# With Hugging Face + PEFT
from transformers import AutoModelForCausalLM
from peft import LoraConfig

model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mixtral-8x22B-Instruct-v0.1",
    load_in_4bit=True
)

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj", "gate"],  # Include gate for MoE
)
```

---

## Comparison: Mixtral vs Alternatives

| Model | Params | Active | Open | Coding | Price |
|-------|--------|--------|------|--------|-------|
| **Mixtral 8x22B** | 141B | 39B | ✅ | ⭐⭐⭐⭐ | $2/$6 |
| **Llama 3 70B** | 70B | 70B | ✅ | ⭐⭐⭐⭐⭐ | $0.59/$0.79 |
| **GPT-4o mini** | Unknown | Unknown | ❌ | ⭐⭐⭐⭐ | $0.15/$0.60 |
| **Command R+** | 104B | 104B | ✅ | ⭐⭐⭐⭐ | $3/$15 |

---

## Mixtral Family

| Model | Size | Best For |
|-------|------|----------|
| **Mixtral 8x7B** | 47B total / 13B active | Smaller, faster |
| **Mixtral 8x22B** | 141B total / 39B active | Quality, efficiency |

---

## Resources

- **Mistral AI**: https://mistral.ai
- **Hugging Face**: https://huggingface.co/mistralai
- **API Docs**: https://docs.mistral.ai
- **Paper**: *Mixtral of Experts* (mistral.ai/news/mixtral-of-experts)

---

## Related

- [[20-knowledge/ai/providers/groq|Groq]] — Fast Mixtral inference
- [[llama-3-1|Llama 3.1]] — Alternative open model
- [[20-knowledge/ai/tools/llama-cpp|llama.cpp]] — Local MoE support

---

*Last updated: 2026-04-05*
