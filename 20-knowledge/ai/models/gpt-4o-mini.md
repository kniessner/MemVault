---
title: GPT-4o mini
provider: OpenAI
release_date: 2024-07-18
context: 128000
status: active
tags: [model, openai, cost-effective, fast]
---

# GPT-4o mini

> Small but mighty — GPT-4o intelligence at a fraction of the cost, ideal for high-volume applications.

## Overview

GPT-4o mini is OpenAI's most cost-efficient small model. It outperforms GPT-3.5 Turbo across nearly all benchmarks while being significantly cheaper, making it ideal for scale-out applications.

| Attribute | Value |
|-----------|-------|
| **Provider** | OpenAI |
| **Release** | July 2024 |
| **Parameters** | Undisclosed (estimated 8B) |
| **Context** | 128K tokens |
| **Knowledge Cutoff** | October 2023 |
| **API Model String** | `gpt-4o-mini` |

---

## Specifications

| Capability | Description |
|------------|-------------|
| **Text** | ✅ Native |
| **Vision** | ✅ Native — image understanding |
| **Audio** | ❌ Not native |
| **Function Calling** | ✅ Full support |
| **Structured Output** | ✅ JSON mode |
| **Fine-tuning** | ✅ Available |

---

## Performance Benchmarks

| Benchmark | GPT-4o mini | GPT-3.5 Turbo | GPT-4o |
|-----------|-------------|---------------|--------|
| MMLU | 82.0% | 69.8% | 88.7% |
| HumanEval | 87.2% | 48.1% | 90.2% |
| MATH | 70.2% | 34.1% | 76.6% |
| MGSM | 87.2% | 48.8% | 90.3% |

**Key insight**: Beats GPT-3.5 on most tasks, approaches GPT-4o on simple tasks.

---

## Pricing

| Tier | Input | Output | Cached Input |
|------|-------|--------|--------------|
| **Standard** | $0.15/M tokens | $0.60/M tokens | $0.075/M |
| **Batch API** | $0.075/M tokens | $0.30/M tokens | — |

### Cost Comparison

| Model | Input | Output | Cost vs GPT-4o |
|-------|-------|--------|----------------|
| **GPT-4o mini** | $0.15/M | $0.60/M | 15x cheaper |
| **GPT-4o** | $2.50/M | $10.00/M | — |
| **Claude 3.5 Haiku** | ~$0.25/M | ~$1.25/M | 2x more expensive |

---

## API Example

```python
from openai import OpenAI

client = OpenAI()

# Basic completion
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Summarize this text"}]
)

# Classification (cost-effective at scale)
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "system",
        "content": "Classify sentiment as positive, neutral, or negative"
    }, {
        "role": "user",
        "content": customer_review
    }],
    response_format={"type": "json_object"}
)

# Vision
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Extract text from this image"},
            {"type": "image_url", "image_url": {"url": image_url}}
        ]
    }]
)
```

---

## Use Cases

### Best For
- ✅ **High-volume applications** — Cheap at scale
- ✅ **Classification** — Sentiment, intent, routing
- ✅ **Simple Q&A** — FAQ bots, support
- ✅ **Data extraction** — Structured data from text
- ✅ **Summarization** — Short-form content
- ✅ **Translation** — Fast language translation
- ✅ **Simple coding** — Boilerplate, snippets

### Not For
- ❌ Complex reasoning (use o3/o1)
- ❌ Creative writing (use Claude/GPT-4o)
- ❌ Advanced coding (use GPT-4o/Claude)
- ❌ Multi-step agentic workflows

---

## Comparison: GPT-4o mini vs Alternatives

| Model | Intelligence | Speed | Cost | Best For |
|-------|--------------|-------|------|----------|
| **GPT-4o mini** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | $0.15/$0.60 | Scale/simple tasks |
| **GPT-3.5 Turbo** | ⭐⭐⭐ | ⭐⭐⭐⭐ | $0.50/$1.50 | Legacy use |
| **Claude 3.5 Haiku** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | $0.25/$1.25 | Anthropic ecosystem |
| **Gemini 1.5 Flash** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | $0.075/$0.30 | Mixed workloads |
| **GPT-4o** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | $2.50/$10.00 | Quality tasks |

---

## Scaling Strategy

**Multi-tier approach:**

```python
def smart_completion(prompt, complexity="auto"):
    if complexity == "simple" or (complexity == "auto" and is_simple(prompt)):
        model = "gpt-4o-mini"  # 15x cheaper
    else:
        model = "gpt-4o"  # Better quality
    
    return client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )

# Cost optimization
# 90% simple tasks × $0.15 = $13.50
# 10% complex tasks × $2.50 = $2.50
# Total: $16 for 100K tokens (vs $250 all GPT-4o)
```

---

## Resources

- **OpenAI Docs**: https://platform.openai.com/docs/models/gpt-4o-mini
- **Pricing**: https://openai.com/pricing

---

## Related

- [[20-knowledge/ai/providers/openai|OpenAI Provider]]
- [[gpt-4o|GPT-4o]] — Full-size flagship
- [[claude-3-5-haiku|Claude 3.5 Haiku]] — Anthropic alternative

---

*Last updated: 2026-04-05*
