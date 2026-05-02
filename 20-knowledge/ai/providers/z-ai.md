---
title: Z.ai (Zhipu AI)
url: https://z.ai
chinese_website: https://zhipuai.cn
founded: 2019
category: provider
tags: [ai, api, llm, glm, chinese, agentic, reasoning]
pricing: pay-per-token
free_tier: yes
stock: SEHK:2513 (public company)
---

# Z.ai (Zhipu AI / 智谱AI)

> "Inspiring AGI to Benefit Humanity" — Chinese AI company developing the GLM (General Language Model) family and agentic AI systems.

## Overview

Z.ai (Knowledge Atlas Technology Joint Stock Co., Ltd.) is a leading Chinese AI provider developing the GLM model family. Founded in 2019 by researchers from Tsinghua University, the company went public on the Hong Kong Stock Exchange (SEHK:2513) in 2024.

| Attribute | Value |
|-----------|-------|
| **Full Name** | Knowledge Atlas Technology Joint Stock Co., Ltd. |
| **Chinese Name** | 北京智谱华章科技有限公司 (Zhipu AI) |
| **Founded** | 2019 |
| **CEO** | Zhang Peng |
| **Founders** | Tang Jie, Li Juanzi (Tsinghua researchers) |
| **Employees** | 800+ (2024) |
| **IPO** | 2024 (SEHK:2513) |
| **HQ** | Beijing, China |
| **API Format** | OpenAI-compatible |
| **Free Tier** | ✅ Yes (limited credits) |
| **Key Differentiator** | GLM architecture, Agentic Engineering focus |

## Screenshot

![Z.ai Logo](assets/z-ai-logo.svg)

## Products

| Product | URL | Description |
|---------|-----|-------------|
| **Z.ai Chat** | https://chat.z.ai | Free web chatbot powered by GLM-5.1 & GLM-5 |
| **AutoClaw** | https://autoglm.z.ai/autoclaw | Desktop agent for iMessage/Telegram (macOS/Windows) |
| **Developer Platform** | https://z.ai | API keys, billing, docs |
| **Docs** | https://docs.z.ai | Developer documentation and guides |

## Z.ai Chat (Free Web Interface)

- **URL**: https://chat.z.ai
- **Powered by**: GLM-5.1 & GLM-5
- **Free tier**: Yes, with credit limits
- **Features**: Web search, code execution, file upload, image generation

## GLM Architecture

**General Language Model (GLM)** — Z.ai's proprietary base architecture designed for:
- Autoregressive blank infilling
- Bidirectional context understanding
- Unified pre-training for NLU and generation
- Native support for tool use and agentic workflows

## Models

### Language Models

| Model | Type | Context | Focus |
|-------|------|---------|-------|
| **GLM-5** | Reasoning | Undisclosed | Flagship base model for Agentic Engineering |
| **GLM-5-Turbo** | Language | Undisclosed | Optimized for OpenClaw scenario |
| **GLM-4.7** | Reasoning | Undisclosed | Programming, multi-step reasoning |
| **GLM-4.7-Flash** | Reasoning | Undisclosed | 30B params, lightweight, efficient |
| **GLM-4.5-Air** | Reasoning | Undisclosed | Cost-effective, lightweight |
| **GLM-4-32B-0414-128K** | Language | 128K | General purpose, coding, Q&A |

### Vision Models

- **GLM-4.6V** - Multimodal vision+language
- **GLM-4.6V Flash** - Lightweight vision model

### Other Capabilities

- Image Models
- Video Generation Models
- Voice Models

## Agents

Z.ai provides pre-built agents for specific workflows:

| Agent | Purpose |
|-------|---------|
| **Translation Agent** | Intelligent translation engine based on LLM |
| **GLM Slide/Poster Agent** | Slide & poster creation assistant |
| **Video Effect Template Agent** | Video templates for short video creation |

## AutoClaw — Desktop Agent for IM

**AutoClaw** is Z.ai's macOS/Windows desktop agent that integrates AI assistants into your existing chat workflows (iMessage, Telegram, etc.).

| Feature | Description |
|---------|-------------|
| **Setup** | One-click OpenClaw configuration |
| **Integration** | Works inside your chat app — no separate dashboard |
| **Execution** | Agent performs tasks with real tools, keeps conversation moving |
| **Privacy** | Runs locally, tasks executed on-device |
| **Pricing** | 4,000 free credits/month; top-up available |
| **Platforms** | macOS (Apple Silicon + Intel), Windows |
| **Download** | https://autoglm.z.ai/autoclaw |

Usage flow:
1. Describe what you need in your chat app
2. AutoClaw executes using real tools
3. See the outcome + next steps inline without leaving the conversation

---

## GLM Coding Plan

Dedicated subscription for AI-powered coding workflows, compatible with popular agent tools.

| Attribute | Value |
|-----------|-------|
| **Price** | Starting at ~$18/month |
| **Compatibility** | Claude Code, Cline, Roo Code, Cursor, Windsurf, and 20+ other AI coding tools |
| **Endpoint** | `https://api.z.ai/api/coding/paas/v4` (dedicated, not the general endpoint) |
| **Quota** | High token quotas; unlimited for some tools |
| **Best for** | IDE agents and code-specific workflows |

> **Note:** The coding endpoint is intended for supported AI coding tools only. For general use cases, use the standard API endpoint.

---

## API Quick Start

```python
import os
import openai

client = openai.OpenAI(
    base_url="https://api.z.ai/v1",
    api_key=os.environ["ZAI_API_KEY"]
)

response = client.chat.completions.create(
    model="glm-5",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

## Key Features

- ✅ OpenAI-compatible API (drop-in replacement)
- ✅ Agentic Engineering paradigm support
- ✅ Native tool use and function calling
- ✅ Multimodal capabilities (vision, image, video, voice)
- ✅ Web search integration
- ✅ Long context support (up to 128K on some models)
- ✅ Web-based chat interface at z.ai/chat

## Comparison

| Provider | Origin | Architecture | Focus |
|----------|--------|--------------|-------|
| **Z.ai** | China | GLM | Agentic Engineering, Reasoning |
| **Moonshot AI** | China | - | Long-context (1M+ tokens) |
| **OpenAI** | USA | GPT | Frontier models, multimodal |
| **Anthropic** | USA | Claude | Safety, agentic systems |
| **Google** | USA | Gemini | Native multimodal, long context |

## Use Cases

- ✅ **Agentic workflows** — Complex multi-step task automation
- ✅ **Coding assistants** — IDE integrations, code generation
- ✅ **Reasoning tasks** — Multi-step reasoning, problem solving
- ✅ **Chinese language** — Native Mandarin capabilities
- ✅ **System engineering** — Complex system design tasks

## Limitations

1. **Geographic restrictions** — Primary focus on China market
2. **English performance** — Good but optimized for Chinese
3. **Documentation** — Some resources primarily in Chinese
4. **Transparency** — Limited technical details on model specs vs Western providers
5. **Compliance** — Enterprise deployment may require navigating international data regulations

## Pricing Notes

- Pay-per-token model (exact rates not publicly disclosed in docs)
- Free tier available for testing
- Developer-friendly commercial plans
- GLM Coding Plan: $10/mo starting price

## Resources

- **Main Website**: https://z.ai
- **Chinese Website**: https://zhipuai.cn
- **Developer Docs**: https://docs.z.ai
- **API Keys**: https://z.ai/manage-apikey/apikey-list
- **Chat Interface**: https://z.ai/chat
- **Community**: https://discord.com/invite/QR7SARHRxK

## Related

- [[moonshot-ai|Moonshot AI]] — Another major Chinese AI provider
- [[openrouter|OpenRouter]] — Can route to Z.ai models
- [[20-knowledge/ai/concepts/agentic-engineering|Agentic Engineering Concept]]

---

*Last updated: 2026-04-27*
