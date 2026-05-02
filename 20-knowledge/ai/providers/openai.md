---
title: OpenAI
url: https://openai.com
founded: 2015
category: provider
tags: [ai, api, llm, gpt, frontier, chatgpt]
pricing: pay-per-token
free_tier: yes
---

# OpenAI

> "ChatGPT and GPT-4 for developers and consumers" — Pioneer of large language models and conversational AI.

## Overview

OpenAI is an AI research and deployment company founded in 2015. They developed the GPT series and ChatGPT, bringing conversational AI to mainstream adoption. The company operates as a capped-profit subsidiary of the non-profit OpenAI Inc.

| Attribute | Value |
|-----------|-------|
| **Founded** | 2015 (Research lab: Greg Brockman, Ilya Sutskever, Sam Altman) |
| **CEO** | Sam Altman |
| **HQ** | San Francisco, USA |
| **Funding** | $6.6B+ raised, valued at $80B+ |
| **Key Differentiator** | Frontier models, ecosystem dominance, ChatGPT |
| **API Format** | OpenAI API (industry standard) |
| **Free Tier** | ✅ ChatGPT Free, API trial credits |

## GPT Model Family

### GPT-4 Series (Current)

| Model | Released | Context | Best For |
|-------|----------|---------|----------|
| **GPT-4o** | May 2024 | 128K | Multimodal, fast, cost-effective |
| **GPT-4o mini** | July 2024 | 128K | Lightweight, cheap, fast |
| **GPT-4 Turbo** | Nov 2023 | 128K | Long context, reliable |
| **GPT-4** | Mar 2023 | 8K/32K | Legacy, stable |

### o-Series (Reasoning)

| Model | Released | Context | Best For |
|-------|----------|---------|----------|
| **o3** | Jan 2025 | 200K | Most advanced reasoning |
| **o3 mini** | Jan 2025 | 200K | Fast reasoning, cheap |
| **o1** | Sep 2024 | 128K | Complex problem solving |
| **o1 mini** | Sep 2024 | 128K | Quick reasoning |

### Specialty Models

| Model | Type | Use Case |
|-------|------|----------|
| **DALL-E 3** | Image gen | High-quality images from text |
| **Whisper** | Speech | Transcription and translation |
| **TTS** | Voice | Text-to-speech |
| **Embeddings** | Vector | Text similarity, search |
| **GPT-4o Realtime** | Audio | Low-latency voice conversations |

## Key Features

### Multimodal Capabilities

- **Vision**: Analyze images, charts, diagrams
- **Audio**: Speech-to-text, text-to-speech
- **Image Generation**: DALL-E API integration

### Function Calling

```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    tools=[{
        "type": "function",
        "function": {
            "name": "get_weather",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                }
            }
        }
    }]
)
```

### Structured Output

JSON Schema adherence:
```python
response = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=messages,
    response_format=PydanticModel
)
```

### Assistants API

Stateful AI assistants with:
- Thread management
- File attachments
- Code interpreter
- Function calling

## API Quick Start

```python
from openai import OpenAI

client = OpenAI(api_key="your-api-key")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role": "user",
        "content": "Hello!"
    }]
)
```

## Products

### ChatGPT

| Tier | Price | Features |
|------|-------|----------|
| Free | $0 | GPT-4o mini, limited messages |
| Plus | $20/mo | GPT-4o, DALL-E, browsing, GPTs |
| Team | $25/user/mo | Shared workspaces, admin |
| Enterprise | Custom | SSO, analytics, custom models |

### OpenAI API

- Platform: https://platform.openai.com
- Usage-based billing
- Rate limits by tier
- Organization management

### Developer Tools

- **OpenAI Playground**: Test prompts
- **OpenAI Evals**: Model evaluation
- **Fine-tuning API**: Custom models
- **Batch API**: Async processing

## Pricing (Per 1M Tokens)

### Chat Models

| Model | Input | Output | Cached Input |
|-------|-------|--------|--------------|
| **GPT-4o** | $2.50 | $10.00 | $1.25 |
| **GPT-4o mini** | $0.15 | $0.60 | $0.075 |
| **o3** | $10.00 | $40.00 | $2.50 |
| **o3 mini** | $1.10 | $4.40 | $0.275 |
| **o1** | $15.00 | $60.00 | $7.50 |
| **o1 mini** | $1.10 | $4.40 | $0.55 |
| **GPT-4 Turbo** | $10.00 | $30.00 | $5.00 |

### Other Models

| Model | Price |
|-------|-------|
| **DALL-E 3 (1024x1024)** | $0.04/image |
| **Whisper** | $0.006/minute |
| **TTS** | $15.00/1M chars |

## Use Cases

- ✅ **Chatbots** — Industry standard conversational AI
- ✅ **Content generation** — Writing, editing, brainstorming
- ✅ **Code assistance** — Copilot competitor via API
- ✅ **Analysis** — Data extraction, summarization
- ✅ **Creative tools** — Image generation, concept art
- ✅ **Voice apps** — Transcription, voice interfaces

## Limitations

1. **Knowledge cutoff** — Models trained up to specific dates
2. **Hallucinations** — Can generate plausible but false info
3. **Safety filters** — May over-refuse certain prompts
4. **Cost** — More expensive than some competitors
5. **Rate limits** — Strict tiers restrict high-volume usage

## Comparison

| vs | OpenAI Advantage | Trade-off |
|----|------------------|-----------|
| **Anthropic** | More multimodal, bigger ecosystem | Less safety focus |
| **Google** | Better developer experience, ChatGPT mindshare | Smaller context |
| **Meta** | API ecosystem, reliability | Not open weights |

## Resources

- **Main**: https://openai.com
- **API Platform**: https://platform.openai.com
- **ChatGPT**: https://chat.openai.com
- **Documentation**: https://platform.openai.com/docs
- **Status**: https://status.openai.com

## Related

- [[anthropic|Anthropic]] — Safety-focused alternative
- [[groq|Groq]] — Fast GPT-4 inference
- [[openrouter|OpenRouter]] — Route to multiple providers
- [[20-knowledge/ai/concepts/prompt-engineering|Prompt Engineering]]

---

*Last updated: 2026-04-05*
