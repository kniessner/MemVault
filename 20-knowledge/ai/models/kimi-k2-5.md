---
title: Kimi K2.5
provider: Moonshot AI
release_date: 2025-07-11
context: 256000
status: active
tags: [model, moonshot, chinese, long-context]
---

# Kimi K2.5

> Moonshot AI's flagship with exceptional long-context capabilities — up to 2M tokens for massive document and codebase processing.

## Overview

Kimi K2.5 is Moonshot AI's primary model, designed for ultra-long context understanding. It excels at processing massive documents, analyzing large codebases, and maintaining coherence across extremely long conversations.

| Attribute | Value |
|-----------|-------|
| **Provider** | Moonshot AI (月之暗面) |
| **Release** | July 2025 |
| **Parameters** | Undisclosed |
| **Standard Context** | 256K tokens |
| **Extended Context** | 1M tokens (K2.5 1M variant) |
| **Knowledge Cutoff** | Unknown |
| **API Model String** | `moonshotai/kimi-k2.5` |

---

## Specifications

| Capability | Description |
|------------|-------------|
| **Text** | ✅ Native — strong multilingual |
| **Chinese** | ✅ Excellent (native optimization) |
| **English** | ✅ Very good |
| **Vision** | ✅ Multimodal (K2.5 Vision) |
| **Long Context** | ✅ Up to 1M tokens |
| **Reasoning** | ✅ Strong |
| **Tool Use** | ✅ Available |

---

## Performance Benchmarks

| Benchmark | Kimi K2.5 | GPT-4o | Claude 3.5 |
|-----------|-----------|--------|------------|
| MMLU | ~85% | 88.7% | 88.7% |
| HumanEval | ~85% | 90.2% | 92.0% |
| Long-context QA | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Chinese Understanding | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |

---

## Pricing

| Model | Input | Output | Context |
|-------|-------|--------|---------|
| **Kimi K2.5** | ~$0.50/M tokens | ~$2.00/M tokens | 256K |
| **Kimi K2.5 1M** | ~$1.00/M tokens | ~$3.00/M tokens | 1M |
| **Kimi K1.6** | Premium pricing | Premium pricing | 2M+ |

*Prices estimated based on OpenRouter rates*

---

## API Example

```python
import openai

client = openai.OpenAI(
    base_url="https://api.moonshot.cn/v1",
    api_key="your-moonshot-key"
)

# Standard context
response = client.chat.completions.create(
    model="kimi-k2.5",
    messages=[{
        "role": "user",
        "content": "Summarize this document"
    }]
)

# Via OpenRouter
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="your-openrouter-key"
)

response = client.chat.completions.create(
    model="moonshotai/kimi-k2.5",
    messages=[{
        "role": "user", 
        "content": "Analyze this entire codebase..."
    }]
)
```

---

## Use Cases

### Best For
- ✅ **Ultra-long documents** — Books, legal docs, research
- ✅ **Large codebases** — Full repo analysis
- ✅ **Chinese language tasks** — Native-level understanding
- ✅ **Multi-hour conversations** — Maintains context
- ✅ **Literature review** — Process hundreds of papers
- ✅ **Document comparison** — Compare multiple long docs

### Not For
- ❌ Speed-sensitive real-time (latency higher)
- ❌ Simple Q&A (overkill)
- ❌ Native English superiority (Claude/GPT better)
- ❌ Maximum coding perf (Claude 3.5 better)

---

## What 1M Context Enables

| Content Type | Size |
|--------------|------|
| Novels | 3-4 full books |
| Codebase | Large project (100K+ lines) |
| Research | 50-100 papers |
| Legal | Complete case files |
| Conversation | Multi-day chat history |

---

## Kimi Model Family

| Model | Context | Focus |
|-------|---------|-------|
| **Kimi K2.5** | 256K | General purpose |
| **Kimi K2.5 1M** | 1M | Extended documents |
| **Kimi K1.6** | 2M+ | Maximum context |
| **Kimi-VL** | 256K | Vision-language |

---

## Comparison: Kimi vs Alternatives

| Model | Context | Chinese | Coding | Price |
|-------|---------|---------|--------|-------|
| **Kimi K2.5** | 256K-1M | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | $0.50/$2.00 |
| **Kimi K1.6** | 2M+ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Premium |
| **Gemini 1.5 Pro** | 2M | ⭐⭐⭐ | ⭐⭐⭐⭐ | $1.25/$5.00 |
| **Claude 3.5 Sonnet** | 200K | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | $3.00/$15.00 |

---

## Access

| Platform | Availability |
|----------|--------------|
| **Moonshot API** | Direct (China) |
| **OpenRouter** | Global access |
| **Kimi Chat** | Web interface |

---

## Resources

- **Moonshot AI**: https://www.moonshot.ai
- **Kimi Chat**: https://www.kimi.com
- **OpenRouter**: https://openrouter.ai/moonshotai
- **Platform Docs**: https://platform.moonshot.cn (Chinese)

---

## Related

- [[20-knowledge/ai/providers/moonshot-ai|Moonshot AI Provider]]
- [[gemini-1-5-pro|Gemini 1.5 Pro]] — Alternative 2M context
- [[20-knowledge/ai/models/gpt-4o|GPT-4o]] — General-purpose alternative

---

*Last updated: 2026-04-05*
