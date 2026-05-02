---
title: Gemini 1.5 Flash
provider: Google
release_date: 2024-05-21
context: 1000000
status: active
tags: [model, google, fast, cost-effective]
---

# Gemini 1.5 Flash

> Google's speed-optimized multimodal model — 1M context at ultra-low cost with blazing fast inference.

## Overview

Gemini 1.5 Flash is Google's fastest, most cost-efficient model. It maintains the multimodal capabilities of Pro with 1M context and adds speed optimization for high-volume applications.

| Attribute | Value |
|-----------|-------|
| **Provider** | Google DeepMind |
| **Release** | May 2024 |
| **Parameters** | Undisclosed |
| **Context** | 1M tokens (1 million) |
| **Knowledge Cutoff** | November 2023 |
| **API Model String** | `gemini-1.5-flash-002` |

---

## Specifications

| Capability | Description |
|------------|-------------|
| **Text** | ✅ Native |
| **Vision** | ✅ Native — images, charts |
| **Video** | ✅ Native — up to 1 hour |
| **Audio** | ✅ Native — speech, music |
| **Function Calling** | ✅ Yes |
| **System Instructions** | ✅ Yes |
| **Grounding** | ✅ Google Search |

---

## Performance Benchmarks

| Benchmark | Flash | Pro | Gap |
|-----------|-------|-----|-----|
| MMLU | 78.9% | 86.5% | -7.6% |
| HumanEval | 74.2% | 84.1% | -9.9% |
| MATH | 54.9% | 71.9% | -17% |
| Video QA | 73.5% | 80.3% | -6.8% |

**Trade-off: ~10% quality reduction for 2x speed and 10x cost reduction.**

---

## Pricing

| Tier | Input | Output | Context Caching |
|------|-------|--------|-----------------|
| **Up to 128K context** | $0.075/M | $0.30/M | $0.01875/M |
| **128K+ to 1M context** | $0.15/M | $0.60/M | $0.0375/M |

### Free Tier

- 1,500 requests/day at no charge
- Access to all capabilities

---

## API Example

```python
import google.generativeai as genai

genai.configure(api_key="your-key")

# Fast completion
model = genai.GenerativeModel('gemini-1.5-flash-002')

response = model.generate_content(
    "Quick summary of machine learning",
    generation_config=genai.types.GenerationConfig(
        temperature=0.7,
        max_output_tokens=500
    )
)

# With video (fast processing)
video = genai.upload_file('meeting.mp4')
response = model.generate_content([
    video,
    "Summarize the action items from this meeting"
])

# Batch processing
responses = model.generate_content(
    items,  # List of prompts
    stream=False  # Batch mode
)
```

---

## Use Cases

### Best For
- ✅ **High-volume applications** — Cheapest multimodal model
- ✅ **Real-time streaming** — Low latency responses
- ✅ **Chatbots** — Responsive conversational AI
- ✅ **Content moderation** — Fast classification
- ✅ **Video summarization** — Hour-long videos
- ✅ **Batch processing** — Large-scale generation
- ✅ **Simple coding** — Boilerplate, Common tasks

### Not For
- ❌ Complex reasoning (use Pro or o3)
- ❌ Research-grade coding (use Claude 3.5)
- ❌ Math competitions
- ❌ Safety-critical decisions

---

## Speed Benchmarks

| Task | Flash | Pro | Speedup |
|------|-------|-----|---------|
| Text generation (500 tokens) | 0.5s | 1.2s | 2.4x |
| Image analysis | 0.8s | 2.0s | 2.5x |
| Video hour analysis | 15s | 35s | 2.3x |
| Code completion | 0.6s | 1.5s | 2.5x |

---

## Comparison: Flash vs Alternatives

| Model | Context | Multimodal | Input Price | Best For |
|-------|---------|------------|-------------|----------|
| **Gemini 1.5 Flash** | 1M | ✅ All | $0.075/M | Multimodal at scale |
| **Gemini 2.0 Flash** | 1M | ✅ All | $0.10/M | Latest generation |
| **GPT-4o mini** | 128K | ✅ Text, Image | $0.15/M | OpenAI ecosystem |
| **Claude 3.5 Haiku** | 200K | ✅ Text, Image | $0.25/M | Anthropic ecosystem |
| **Llama 3.1 8B** | 128K | ❌ Text only | Free | Self-hosted |

---

## Gemini Family Comparison

| Model | Context | Speed | Price | Best For |
|-------|---------|-------|-------|----------|
| **Flash 1.5** | 1M | ⭐⭐⭐⭐⭐ | $0.075/M | Speed, cost |
| **Pro 1.5** | 2M | ⭐⭐⭐⭐ | $1.25/M | Quality, long context |
| **Flash 2.0** | 1M | ⭐⭐⭐⭐⭐ | $0.10/M | Latest speed |
| **Pro 2.0** | 2M | ⭐⭐⭐⭐ | Variable | Latest quality |

---

## When to Use Flash vs Pro

| Use Case | Recommendation |
|----------|----------------|
| Chatbot responses | Flash — fast, cheap |
| Document analysis | Pro — better accuracy |
| Video hour summary | Flash — fast enough |
| Research paper deep dive | Pro — better synthesis |
| Code review | Pro — better catch issues |
| Batch classification | Flash — scale economics |

---

## Resources

- **Google AI Studio**: https://aistudio.google.com
- **API Docs**: https://ai.google.dev
- **Pricing**: https://ai.google.dev/pricing

---

## Related

- [[20-knowledge/ai/providers/google|Google Provider]]
- [[gemini-1-5-pro|Gemini 1.5 Pro]] — Higher quality sibling
- [[gemini-2-0-flash|Gemini 2.0 Flash]] — Next generation
- [[20-knowledge/ai/models/gpt-4o-mini|GPT-4o mini]] — OpenAI alternative

---

*Last updated: 2026-04-05*
