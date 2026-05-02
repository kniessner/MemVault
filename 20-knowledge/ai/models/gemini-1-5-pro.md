---
title: Gemini 1.5 Pro
provider: Google
release_date: 2024-02-15
context: 2000000
status: active
tags: [model, google, multimodal, long-context]
---

# Gemini 1.5 Pro

> Google's flagship model with up to **2 million token context** — natively multimodal and built for long-form understanding.

## Overview

Gemini 1.5 Pro is Google's most capable model for complex tasks across modalities. Its massive context window enables processing of entire books, hours of video, and large codebases in a single prompt.

| Attribute | Value |
|-----------|-------|
| **Provider** | Google DeepMind |
| **Release** | February 2024 |
| **Parameters** | Undisclosed |
| **Context** | 2,000,000 tokens (2 million) |
| **Knowledge Cutoff** | November 2023 |
| **API Model String** | `gemini-1.5-pro-002` |

---

## Specifications

| Capability | Description |
|------------|-------------|
| **Text** | ✅ Native — frontier quality |
| **Vision** | ✅ Native — images, charts, diagrams |
| **Video** | ✅ Native — up to 2 hours |
| **Audio** | ✅ Native — speech, music |
| **Function Calling** | ✅ Tool use |
| **Structured Output** | ✅ JSON mode |
| **Grounding** | ✅ Google Search integration |
| **System Instructions** | ✅ Custom behavior |

---

## Performance Benchmarks

| Benchmark | Gemini 1.5 Pro | Gemini 1.0 Ultra | Claude 3.5 |
|-----------|----------------|------------------|------------|
| MMLU | 86.5% | 83.7% | 88.7% |
| HumanEval | 84.1% | 74.4% | 92.0% |
| MATH | 71.9% | 53.2% | 71.1% |
| Video understanding | ⭐ Best-in-class | — | — |

---

## Pricing

| Tier | Input | Output | Context Caching |
|------|-------|--------|-----------------|
| **Standard** | $1.25/M tokens | $5.00/M tokens | $0.3125/M |
| **Long Context** | Same pricing up to 2M | — | — |
| **Grounding** | +$35/1000 requests | — | — |

### Free Tier

- 1,500 requests/day at no charge
- Rate limited but fully featured

---

## API Example

```python
import google.generativeai as genai

genai.configure(api_key="your-key")

# Initialize model
model = genai.GenerativeModel('gemini-1.5-pro-002')

# Text generation
response = model.generate_content("Explain quantum mechanics")

# With image
image = PIL.Image.open('diagram.png')
response = model.generate_content([
    "Describe what you see in this diagram",
    image
])

# With video (large files supported)
video_file = genai.upload_file(path='lecture.mp4')
response = model.generate_content([
    video_file,
    "Summarize the key points from this lecture"
])

# Function calling
model = genai.GenerativeModel(
    'gemini-1.5-pro-002',
    tools=[{
        'function': {
            'name': 'get_weather',
            'parameters': {
                'type': 'object',
                'properties': {'city': {'type': 'string'}}
            }
        }
    }]
)

# OpenAI-compatible API
from openai import OpenAI

client = OpenAI(
    api_key="your-key",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-1.5-pro-002",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

---

## Use Cases

### Best For
- ✅ **Video analysis** — Hours of video in single prompt
- ✅ **Large codebases** — Entire repos as context
- ✅ **Long document processing** — Books, legal docs, research
- ✅ **Multimodal reasoning** — Charts + text + images combined
- ✅ **Audio understanding** — Meetings, podcasts, lectures
- ✅ **Research synthesis** — Massive literature review

### What 2M Context Enables

| Content Type | Approximate Size |
|--------------|------------------|
| **Video** | ~2 hours |
| **Audio** | ~22 hours |
| **Code** | ~60,000 lines |
| **Text** | ~1.5 million words (~3 novels) |
| **PDF documents** | ~3,000 pages |

---

## Context Caching

Save money on repeated context:

```python
# Cache frequently used context
cached_content = genai.cached_content.create(
    model='gemini-1.5-pro-002',
    display_name='product-docs-cache',
    contents=[large_document],
    ttl='60m'
)

# Use cached context
model = genai.GenerativeModel.from_cached_content(cached_content)
response = model.generate_content("Question about the doc")
# 75% cheaper than sending full doc each time
```

---

## Grounding

Connect to Google Search for real-time info:

```python
response = model.generate_content(
    "What's the latest news about AI?",
    tools='google_search_retrieval'
)
# Returns grounded response with citations
```

---

## Limitations

1. **Coding performance** — Good but not best (Claude/GPT-4o better)
2. **Reasoning transparency** — Doesn't show thinking process (o1/o3 better)
3. **Ecosystem** — Smaller than OpenAI
4. **Creative writing** — Slightly less natural than Claude
5. **Availability** — Some features region-limited

---

## Variants

| Variant | Context | Best For |
|---------|---------|----------|
| **Gemini 1.5 Pro** | 2M | Complex tasks, long content |
| **Gemini 1.5 Flash** | 1M | Speed, cost-efficiency |
| **Gemini 2.0 Pro** | 2M | Next generation (experimental) |

---

## Comparison: Gemini 1.5 Pro vs Alternatives

| Model | Context | Multimodal | Best Use Case |
|-------|---------|------------|---------------|
| **Gemini 1.5 Pro** | 2M | All | Video, long docs, research |
| **Gemini 2.0 Pro** | 2M | All | Latest (experimental) |
| **Claude 3.5 Sonnet** | 200K | Text, Image | Coding, agentic tasks |
| **GPT-4o** | 128K | All | General purpose, ecosystem |
| **Kimi K1.6** | 2M+ | Text | Ultra-long documents |

---

## Resources

- **Google AI Studio**: https://aistudio.google.com (free prototyping)
- **API Docs**: https://ai.google.dev
- **Pricing**: https://ai.google.dev/pricing
- **Gemini App**: https://gemini.google.com

---

## Related

- [[20-knowledge/ai/providers/google|Google/Gemini Provider]]
- [[gemini-1-5-flash|Gemini 1.5 Flash]] — Faster, cheaper variant
- [[gemini-2-0-pro|Gemini 2.0 Pro]] — Next generation
- [[moonshot-kimi-k1-6|Kimi K1.6]] — Alternative 2M+ context

---

*Last updated: 2026-04-05*
