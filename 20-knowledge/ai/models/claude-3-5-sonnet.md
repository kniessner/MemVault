---
title: Claude 3.5 Sonnet
provider: Anthropic
release_date: 2024-06-21
context: 200000
status: active
tags: [model, anthropic, coding, reasoning, agentic]
---

# Claude 3.5 Sonnet

> Anthropic's most intelligent model — excels at coding, agentic tasks, and complex reasoning with exceptional reliability.

## Overview

Claude 3.5 Sonnet is Anthropic's flagship model, offering an optimal balance of intelligence, speed, and cost. It outperforms Claude 3 Opus on most benchmarks while being significantly faster and cheaper.

| Attribute | Value |
|-----------|-------|
| **Provider** | Anthropic |
| **Release** | June 2024 |
| **Parameters** | Undisclosed (estimated ~175B) |
| **Context** | 200K tokens |
| **Knowledge Cutoff** | April 2024 |
| **API Model String** | `claude-3-5-sonnet-20241022` |

---

## Specifications

| Capability | Description |
|------------|-------------|
| **Text** | ✅ Native — frontier quality |
| **Vision** | ✅ Native — image analysis |
| **Audio** | ❌ Not native (TTS available) |
| **Computer Use** | ✅ Beta — control interface |
| **Artifacts** | ✅ Workspace environment |
| **Extended Thinking** | ✅ Available in 3.7 |

---

## Performance Benchmarks

| Benchmark | Claude 3.5 Sonnet | Claude 3 Opus | GPT-4o |
|-----------|-------------------|---------------|--------|
| MMLU | 88.7% | 86.8% | 88.7% |
| HumanEval | 92.0% | 84.9% | 90.2% |
| MATH | 71.1% | 60.1% | 76.6% |
| GPQA | 62.0% | 50.4% | 53.6% |

**Coding is a particular strength** — often rated best-in-class for software engineering tasks.

---

## Pricing

| Tier | Input | Output |
|------|-------|--------|
| **API** | $3.00/M tokens | $15.00/M tokens |
| **Prompt Caching** | $3.75/M (write) / $0.30/M (read) | — |
| **Batched** | 50% discount | 50% discount |

### Claude.ai Plans

| Plan | Price | Features |
|------|-------|----------|
| Free | $0 | Limited messages |
| Pro | $20/mo | 5x more usage, all models |
| Team | $25/user | Shared workspaces |
| Enterprise | Custom | SSO, audit logs |

---

## API Example

```python
import anthropic

client = anthropic.Anthropic(api_key="your-key")

# Basic completion
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": "Write a Python function to calculate fibonacci"
    }]
)

# With vision
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/png",
                    "data": image_data
                }
            },
            {
                "type": "text",
                "text": "Describe this UI mockup"
            }
        ]
    }]
)

# Tool use
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=4096,
    tools=[{
        "name": "get_weather",
        "description": "Get weather for location",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            }
        }
    }],
    messages=[{"role": "user", "content": "What's the weather in Berlin?"}]
)
```

---

## Use Cases

### Best For
- ✅ **Software engineering** — Best-in-class coding ability
- ✅ **Code review** — Understands large codebases
- ✅ **Agentic workflows** — Reliable tool use, computer control
- ✅ **Long-form analysis** — 200K context for documents
- ✅ **Creative writing** — Natural, nuanced output
- ✅ **Safety-critical apps** — Less likely to hallucinate

### Competitive vs
- **GPT-4o**: Better at coding, more natural writing, smaller ecosystem
- **Claude 3.7 Sonnet**: Earlier version, less reasoning capability
- **o3/o1**: Less reasoning depth, but faster and cheaper

---

## Extended Thinking (3.7)

Claude 3.7 Sonnet can use "extended thinking" for complex problems:
- Shows reasoning process
- Better at math, logic puzzles
- Self-correction before answering
- Higher cost, longer latency

---

## Computer Use (Beta)

Claude can control a computer:
- Screenshot → Action loop
- Move cursor, click, type
- Navigate interfaces
- Automate workflows

```python
# Enable computer use
response = client.beta.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=4096,
    tools=[{
        "type": "computer_20241022",
        "name": "computer",
        "display_width_px": 1024,
        "display_height_px": 768
    }],
    messages=[{"role": "user", "content": "Open Chrome and search for..."}]
)
```

---

## Limitations

1. **Knowledge cutoff** — April 2024
2. **No audio** — Text/image only (no native voice)
3. **No image generation** — Cannot create images
4. **Rate limits** — Strict quotas on API tiers
5. **No built-in search** — Can't browse web natively

---

## Variants

| Variant | Strengths |
|---------|-----------|
| **Claude 3.7 Sonnet** | Extended thinking, latest |
| **Claude 3.5 Sonnet** | Balanced, reliable |
| **Claude 3.5 Haiku** | Speed, cost-efficiency |

---

## Comparison: Claude 3.5 Sonnet vs Alternatives

| Model | Context | Coding | Reliability | Price |
|-------|---------|--------|-------------|-------|
| **Claude 3.5 Sonnet** | 200K | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | $3/$15 |
| **Claude 3.7 Sonnet** | 200K | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | $3/$15 |
| **GPT-4o** | 128K | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | $2.50/$10 |
| **Gemini 1.5 Pro** | 2M | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | $3.50/$10.50 |

---

## Resources

- **Anthropic Docs**: https://docs.anthropic.com
- **Claude.ai**: https://claude.ai
- **API Reference**: https://docs.anthropic.com/en/api/getting-started
- **Computer Use**: https://docs.anthropic.com/en/docs/build-with-claude/computer-use

---

## Related

- [[20-knowledge/ai/providers/anthropic|Anthropic Provider]]
- [[gpt-4o|GPT-4o]] — OpenAI alternative
- [[gemini-1-5-pro|Gemini 1.5 Pro]] — Google alternative
- [[20-knowledge/ai/concepts/constitutional-ai|Constitutional AI]]

---

*Last updated: 2026-04-05*
