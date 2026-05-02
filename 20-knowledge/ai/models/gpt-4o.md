---
title: GPT-4o
provider: OpenAI
release_date: 2024-05-13
context: 128000
status: active
tags: [model, openai, multimodal, frontier]
---

# GPT-4o

> "Omni" model — GPT-4-level intelligence with native multimodal capabilities (text, audio, image).

## Overview

GPT-4o ("o" for "omni") is OpenAI's flagship multimodal model. It matches GPT-4 Turbo performance on text while adding native audio and vision capabilities in a single model.

| Attribute | Value |
|-----------|-------|
| **Provider** | OpenAI |
| **Release** | May 2024 |
| **Parameters** | Undisclosed |
| **Context** | 128K tokens |
| **Knowledge Cutoff** | October 2023 |
| **API Model String** | `gpt-4o-2024-08-06` |

---

## Specifications

| Capability | Description |
|------------|-------------|
| **Text** | ✅ Native — GPT-4 level |
| **Vision** | ✅ Native — image understanding |
| **Audio** | ✅ Native — speech in/out |
| **Structured Output** | ✅ JSON mode, strict schema |
| **Function Calling** | ✅ Tools/Functions |
| **Fine-tuning** | ✅ Available |

---

## Performance Benchmarks

| Benchmark | GPT-4o | GPT-4 Turbo |
|-----------|--------|-------------|
| MMLU | 88.7% | 86.6% |
| HumanEval | 90.2% | 87.6% |
| MATH | 76.6% | 73.4% |
| MGSM | 90.3% | 88.0% |

---

## Pricing

| Tier | Input | Output | Cached Input |
|------|-------|--------|--------------|
| **Standard** | $2.50/M tokens | $10.00/M tokens | $1.25/M tokens |
| **Batch API** | $1.25/M tokens | $5.00/M tokens | — |

### Vision Pricing

Images are converted to tokens based on resolution:
- Low resolution: 85 tokens
- High resolution: 170 tokens + tiles (per 512x512)

---

## API Example

```python
from openai import OpenAI

client = OpenAI()

# Text only
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role": "user",
        "content": "Explain quantum computing"
    }]
)

# With vision
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Describe this image"},
            {
                "type": "image_url",
                "image_url": {"url": "https://example.com/image.jpg"}
            }
        ]
    }]
)

# Structured output
from pydantic import BaseModel

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

response = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[{"role": "user", "content": "..."}],
    response_format=CalendarEvent
)
```

---

## Use Cases

### Best For
- ✅ **General-purpose chatbots** — Reliable, fast responses
- ✅ **Multimodal apps** — Vision + text in single call
- ✅ **Content creation** — Marketing copy, documentation
- ✅ **Code assistance** — Strong coding performance
- ✅ **Document analysis** — OCR + understanding combined
- ✅ **Voice interfaces** — Natively handles audio

### Competitive vs
- **GPT-4 Turbo**: Same quality, 2x faster, 50% cheaper
- **Claude 3.5 Sonnet**: Better at coding, similar on general tasks
- **Gemini 1.5 Pro**: Smaller context, better at multimodal audio

---

## Limitations

1. **Knowledge cutoff** — October 2023 (no real-time info)
2. **Hallucinations** — Still generates false information
3. **Audio latency** — Not as fast as dedicated TTS systems
4. **Vision accuracy** — Can struggle with fine details, handwriting
5. **Math complexity** — o3/o1 better for hard reasoning

---

## Variants

| Variant | Description |
|---------|-------------|
| **GPT-4o** | Standard version |
| **GPT-4o-2024-08-06** | Structured output optimized |
| **GPT-4o-mini** | Smaller, faster, cheaper (see separate profile) |

---

## Comparison: GPT-4o vs Alternatives

| Model | Context | Multimodal | Speed | Price |
|-------|---------|------------|-------|-------|
| **GPT-4o** | 128K | Text, Image, Audio | Fast | $2.50/$10 |
| **Claude 3.5 Sonnet** | 200K | Text, Image | Medium | $3/$15 |
| **Gemini 1.5 Pro** | 2M | All modalities | Medium | $3.50/$10.50 |
| **GPT-4o mini** | 128K | Text, Image | Very Fast | $0.15/$0.60 |

---

## Resources

- **OpenAI Docs**: https://platform.openai.com/docs/models/gpt-4o
- **Pricing**: https://openai.com/pricing
- **API Reference**: https://platform.openai.com/docs/api-reference

---

## Related

- [[20-knowledge/ai/providers/openai|OpenAI Provider]]
- [[gpt-4o-mini|GPT-4o mini]] — Smaller, faster variant
- [[o3|o3]] — Reasoning-focused model
- [[claude-3-5-sonnet|Claude 3.5 Sonnet]] — Anthropic alternative
- [[gemini-1-5-pro|Gemini 1.5 Pro]] — Google alternative

---

*Last updated: 2026-04-05*
