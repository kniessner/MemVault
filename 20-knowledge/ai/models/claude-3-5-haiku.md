---
title: Claude 3.5 Haiku
provider: Anthropic
release_date: 2024-11-04
context: 200000
status: active
tags: [model, anthropic, fast, cost-effective]
---

# Claude 3.5 Haiku

> Anthropic's fastest model — 200K context with Sonnet-level intelligence at a fraction of the cost.

## Overview

Claude 3.5 Haiku is Anthropic's speed-optimized model. It matches or exceeds Claude 3 Opus intelligence while being significantly faster and cheaper than Claude 3.5 Sonnet.

| Attribute | Value |
|-----------|-------|
| **Provider** | Anthropic |
| **Release** | November 2024 |
| **Parameters** | Undisclosed (estimated ~40B) |
| **Context** | 200K tokens |
| **Speed** | Fastest in Claude family |
| **API Model String** | `claude-3-5-haiku-20241022` |

---

## Specifications

| Capability | Description |
|------------|-------------|
| **Text** | ✅ Native — near-Sonnet quality |
| **Vision** | ✅ Native — image understanding |
| **Speed** | ✅ Fastest Claude model |
| **Tool Use** | ✅ Full function calling |
| **Cost** | ✅ Cheapest Claude |

---

## Performance Benchmarks

| Benchmark | Haiku 3.5 | Sonnet 3.5 | Opus 3 | GPT-4o mini |
|-----------|-----------|------------|--------|-------------|
| MMLU | 81.5% | 88.7% | 86.8% | 82.0% |
| HumanEval | 86.5% | 92.0% | 84.9% | 87.2% |
| MATH | 71.7% | 71.1% | 60.1% | 70.2% |
| MGSM | 89.7% | 92.3% | 86.9% | 87.2% |

**Outperforms Claude 3 Opus on many benchmarks.**

---

## Pricing

| Model | Input | Output |
|-------|-------|--------|
| **Claude 3.5 Haiku** | $0.25/M tokens | $1.25/M tokens |
| **Claude 3.5 Sonnet** | $3.00/M tokens | $15.00/M tokens |
| **GPT-4o mini** | $0.15/M tokens | $0.60/M tokens |
| **Gemini 1.5 Flash** | $0.075/M tokens | $0.30/M tokens |

---

## API Example

```python
import anthropic

client = anthropic.Anthropic()

# Fast response
response = client.messages.create(
    model="claude-3-5-haiku-20241022",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": "Summarize this paragraph in one sentence"
    }]
)
# Typically 2-3x faster than Sonnet

# With vision
response = client.messages.create(
    model="claude-3-5-haiku-20241022",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/jpeg",
                    "data": image_data
                }
            },
            {"type": "text", "text": "Quick caption:"}
        ]
    }]
)
```

---

## Use Cases

### Best For
- ✅ **High-volume applications** — Cheap at scale
- ✅ **Fast responses** — Low latency requirements
- ✅ **Simple coding** — Boilerplate, simple functions
- ✅ **Classification** — Sentiment, intent, routing
- ✅ **Summarization** — Quick summaries
- ✅ **Data extraction** — Structured data from text
- ✅ **Chatbots** — Responsive conversational AI

### Not For
- ❌ Complex architecture (use Sonnet)
- ❌ Multi-step reasoning (use o3)
- ❌ Deep research synthesis
- ❌ Safety-critical complex decisions

---

## Claude Model Comparison

| Model | Speed | Quality | Price | Best For |
|-------|-------|---------|-------|----------|
| **Haiku 3.5** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | $0.25/$1.25 | Volume, speed |
| **Sonnet 3.5** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | $3/$15 | Quality, coding |
| **Opus 3** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | $15/$75 | Legacy (use Sonnet) |

---

## Speed Benchmarks

| Task | Haiku | Sonnet | Speedup |
|------|-------|--------|---------|
| Simple Q&A | ~500ms | ~1200ms | 2.4x |
| Code suggestion | ~800ms | ~2000ms | 2.5x |
| Image caption | ~600ms | ~1500ms | 2.5x |
| Document summary | ~2s | ~5s | 2.5x |

---

## Comparison: Haiku vs Alternatives

| Model | Speed | Quality | Price | Context |
|-------|-------|---------|-------|---------|
| **Claude 3.5 Haiku** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | $0.25/$1.25 | 200K |
| **GPT-4o mini** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | $0.15/$0.60 | 128K |
| **Gemini 1.5 Flash** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | $0.075/$0.30 | 1M |
| **Llama 3.1 8B** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Free (local) | 128K |

---

## Smart Routing Strategy

```python
def smart_route(prompt, complexity="auto"):
    if complexity == "simple":
        return "claude-3-5-haiku-20241022"
    elif complexity == "coding":
        return "claude-3-5-sonnet-20241022"
    else:
        # Auto-detect
        if len(prompt) < 100 and "?" in prompt:
            return "claude-3-5-haiku-20241022"  # Simple Q&A
        elif "def " in prompt or "class " in prompt:
            return "claude-3-5-sonnet-20241022"  # Code
        else:
            return "claude-3-5-sonnet-20241022"  # Default to quality

# Cost optimization example
# 80% simple queries × $0.25 = $20
# 20% complex queries × $3.00 = $60
# Total: $80 for 100K tokens (vs $300 all Sonnet)
```

---

## Resources

- **Anthropic Docs**: https://docs.anthropic.com
- **Model Card**: https://www.anthropic.com/news/claude-3-5-haiku
- **Pricing**: https://anthropic.com/pricing

---

## Related

- [[20-knowledge/ai/providers/anthropic|Anthropic Provider]]
- [[claude-3-5-sonnet|Claude 3.5 Sonnet]] — Higher quality sibling
- [[gpt-4o-mini|GPT-4o mini]] — OpenAI alternative
- [[gemini-1-5-flash|Gemini 1.5 Flash]] — Google alternative

---

*Last updated: 2026-04-05*
