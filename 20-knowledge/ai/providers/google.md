---
title: Google DeepMind / Gemini
url: https://deepmind.google
gemini_url: https://gemini.google.com
founded: 2010 (DeepMind), 2023 (Gemini)
category: provider
tags: [ai, api, llm, gemini, multimodal, google]
pricing: pay-per-token
free_tier: yes
---

![Gemini Homepage](assets/gemini-homepage.png)

# Google DeepMind / Gemini

> "The most capable AI models for complex tasks" — Google's unified multimodal AI built on DeepMind research.

## Overview

Gemini is Google's flagship AI model family, developed by Google DeepMind. It represents the merger of Google's Brain team and DeepMind. Gemini is natively multimodal (trained on text, images, audio, video, code) and powers consumer products like Bard (now Gemini) and Pixel phones.

| Attribute | Value |
|-----------|-------|
| **Organization** | Google DeepMind |
| **Gemini Launch** | December 2023 |
| **DeepMind Founded** | 2010 (acquired by Google 2014) |
| **CEO** | Demis Hassabis (DeepMind) |
| **Key Differentiator** | Native multimodality, 2M context, Google integration |
| **API Format** | OpenAI-compatible via Gemini API |
| **Free Tier** | ✅ Yes (Gemini app, API credits) |

## Gemini Model Family

### Current Generation

| Model | Released | Context | Input Modes | Best For |
|-------|----------|---------|-------------|----------|
| **Gemini 2.0 Pro Experimental** | Dec 2024 | 2M | Text, image, video, audio | Complex reasoning, coding |
| **Gemini 2.0 Flash** | Dec 2024 | 1M | Multimodal | Fast, efficient |
| **Gemini 2.0 Flash Thinking** | Dec 2024 | 1M | Multimodal | Visible reasoning |
| **Gemini 2.0 Flash-Lite** | Feb 2025 | 1M | Multimodal | Cost-optimized |

### Previous Generation

| Model | Status | Notes |
|-------|--------|-------|
| **Gemini 1.5 Pro** | Active | 2M context, strong generalist |
| **Gemini 1.5 Flash** | Active | Fast, multimodal, 1M context |
| **Gemini 1.0 Ultra** | Legacy | First flagship, outdated |

### Deep Think Mode

Gemini 3.1 Deep Think: Advanced reasoning mode for:
- Complex math
- Competitive programming
- Scientific reasoning
- Multi-step logic puzzles

## Key Features

### Native Multimodality

Unlike models bolted together, Gemini was trained jointly on:
- Text
- Images
- Audio
- Video
- Code

### Long Context

- **2 million tokens standard** (Gemini 1.5 Pro, Gemini 2.0 Pro)
- Can process:
  - 2 hours of video
  - 22 hours of audio
  - 60,000 lines of code
  - Entire books

### Grounding

Connect to Google Search for real-time information with citations.

### Function Calling

```python
import google.generativeai as genai

genai.configure(api_key="your-api-key")

model = genai.GenerativeModel(
    model_name="gemini-2.0-pro-exp-02-05",
    tools=[{
        "function": {
            "name": "get_exchange_rate",
            "parameters": {
                "type": "object",
                "properties": {
                    "currency": {"type": "string"}
                }
            }
        }
    }]
)
```

### OpenAI-compatible API

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-gemini-api-key",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.0-pro-exp-02-05",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

## Products

### Consumer

| Product | Description |
|---------|-------------|
| **Gemini** | Chat interface (gemini.google.com) |
| **Gemini Advanced** | $20/mo, Gemini Pro access |
| **Pixel AI** | On-device Gemini Nano |
| **Workspace** | Docs, Sheets integration |

### Developer

| Platform | Description |
|----------|-------------|
| **Google AI Studio** | Free prototyping (aistudio.google.com) |
| **Gemini API** | Production API |
| **Vertex AI** | Enterprise Google Cloud platform |

## Pricing

### Gemini API

| Model | Input | Output | Context Caching |
|-------|-------|--------|-----------------|
| **Gemini 2.0 Pro** | $0.00 (experimental) | $0.00 | N/A |
| **Gemini 2.0 Flash** | $0.10/M | $0.40/M | $0.025/M |
| **Gemini 2.0 Flash-Lite** | $0.075/M | $0.30/M | N/A |
| **Gemini 1.5 Pro** | $1.25/M | $5.00/M | $0.3125/M |
| **Gemini 1.5 Flash** | $0.075/M | $0.30/M | $0.01875/M |

*2M context available with standard pricing (no premium for length)*

### Model Variations

- **Input**: Text, image, video, audio all same price
- **Context caching**: 75% discount for repeated context
- **Free tier**: 1,500 requests/day for Flash models

## Use Cases

- ✅ **Video analysis** — Hours of video in single prompt
- ✅ **Code understanding** — Entire codebases as context
- ✅ **Document processing** — Whole PDFs, books
- ✅ **Multimodal reasoning** — Charts + text + images
- ✅ **Research synthesis** — Massive literature review
- ✅ **Multi-turn conversations** — Maintains long memory

## Limitations

1. **Availability** — Some features US-first rollout
2. **Enterprise** — Stronger in Google Cloud ecosystem
3. **Reasoning trace** — Not always visible (unlike o1)
4. **Creative writing** — Sometimes less natural than Claude
5. **Privacy concerns** — Google data practices

## Comparison

| vs | Gemini Advantage | Trade-off |
|----|------------------|-----------|
| **OpenAI** | 2M context, native multimodal | Smaller ecosystem |
| **Anthropic** | 10x context, multimodal video | Less steerable |
| **Meta** | Long context, Google integration | Not open weights |

## Unique Capabilities

### Video Understanding

```python
# Upload video file
video_file = genai.upload_file(path="video.mp4")

# Ask about any part
response = model.generate_content([
    video_file,
    "What happens at timestamp 5:23?"
])
```

### PDF Analysis

Can process entire documents with layouts, charts, tables preserved.

### Audio Understanding

Process podcasts, meetings, lectures end-to-end.

## Resources

- **DeepMind**: https://deepmind.google
- **Gemini**: https://gemini.google.com
- **AI Studio**: https://aistudio.google.com
- **API Docs**: https://ai.google.dev
- **Gemini API**: https://ai.google.dev/gemini-api

## Related

- [[openai|OpenAI]] — Alternative frontier provider
- [[anthropic|Anthropic]] — Safety-focused alternative
- [[moonshot-ai|Moonshot AI]] — Another 2M context provider
- [[20-knowledge/ai/concepts/multimodal-ai|Multimodal AI Patterns]]

---

*Last updated: 2026-04-05*
