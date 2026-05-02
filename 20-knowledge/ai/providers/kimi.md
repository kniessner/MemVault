---
title: Kimi
url: https://www.kimi.com
founded: 2023
category: ai-platform
tags: [ai-platform, moonshot-ai, coding, agent-swarms, multimodal, chinese]
pricing: subscription + usage-based
free_tier: yes
status: active
creator: Moonshot AI (月之暗面)
---

# Kimi

> The platform layer for Moonshot AI's Kimi models — featuring agent swarms, coding tools, document processing, and visual UI generation.

## Overview

Kimi is Moonshot AI's consumer platform built around the **K2.6** open-source model family. It provides a web interface, CLI, and API for accessing state-of-the-art coding, agentic, and multimodal capabilities.

| Attribute | Value |
|-----------|-------|
| **Parent Company** | Moonshot AI (月之暗面) |
| **Founded** | 2023 |
| **Headquarters** | China |
| **Key Model** | Kimi K2.6 (1T params, MoE, 262K context) |
| **Free Tier** | ✅ Yes (via kimi.com and API) |
| **License** | Apache 2.0 (weights) |

---

## Architecture: Kimi K2.6

| Spec | Value |
|------|-------|
| **Parameters** | 1T total / 32B active |
| **Experts** | 384 (8 activated per token) |
| **Architecture** | Mixture-of-Experts (MoE) |
| **Attention** | MLA (Multi-head Latent Attention) |
| **Context Window** | 262,144 tokens |
| **Training** | MuonClip-stabilized |
| **Availability** | Open-source weights, Apache 2.0 |

**K2.6 GA: April 21, 2026** — graduated from Code Preview (Apr 13) in just 8 days.

---

## Features

### Agent Swarm
- Up to **300 sub-agents** in parallel
- **4,000 coordinated steps** per swarm
- Supervisor + workers topology with Agent Relay
- Proactive autonomy — runs 24/7 against task queues

### Coding (Kimi Code)
- **12-hour autonomous coding sessions**
- Built-in context compression when approaching window limits
- Native tool-calling, file-system access, swarm supervisor
- Anthropic-compatible API base URL swapping

### Visual Tools
| Tool | What It Does |
|------|-------------|
| **Website Builder** | Full-stack website generation from prompts |
| **Slides** | AI-generated presentations/PPTs |
| **Sheets** | AI spreadsheets and data analysis |
| **Deep Research** | Document analysis and research synthesis |
| **Claw Groups** | Agent teamwork/collaboration preview |

### API
- OpenAI-compatible API format
- Default: `temperature=1.0`, `top_p=1.0`
- Available at: `api.moonshot.cn/v1`

---

## Benchmarks

| Benchmark | Score |
|-----------|-------|
| **Terminal-Bench 2.0** | 66.7% |
| **SWE-Bench Pro** | 58.6% |
| **MathVision (with Python)** | 93.2% |

**Partner Results vs K2.5:**
| Partner | Improvement |
|---------|------------|
| CodeBuddy | +12% accuracy, +18% long-context stability |
| Vercel | >50% on internal Next.js benchmark |
| Factory.ai | +15% on both benchmarks |

---

## Platform Surfaces

1. **kimi.com** — Web chat and agent swarm interface
2. **Kimi App** — Mobile companion
3. **Kimi Code CLI** — Terminal coding agent
4. **Open Platform API** — Programmatic access

---

## Pricing

| Tier | Access |
|------|--------|
| Free | kimi.com interface, limited API |
| Paid | Higher rate limits, priority inference |

*Weights available free on Hugging Face. Usage based per 1M tokens.*

---

## Notable Achievements

- **Zig inference engine**: Deployed Qwen3.5-0.8B locally at ~193 tokens/sec (20% faster than LM Studio)
- **exchange-core optimization**: 185% throughput improvement on real Java financial matching engine
- **Full-stack generation**: Complete App Router/Servers Component Next.js apps with auth + DB
- **Open-source Apache 2.0**: Weights freely available, no commercial restrictions

---

## Related

- [[moonshot-ai|Moonshot AI Provider Analysis]]
- [[models/kimi-k2.6|Kimi K2.6 Model Deep Dive]]
- [[concepts/agent-swarms|Agent Swarms Concept]]
- [[providers/openrouter|OpenRouter Integration]]

---

*Last updated: 2026-04-28*
