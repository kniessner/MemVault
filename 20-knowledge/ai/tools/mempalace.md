---
url: https://github.com/milla-jovovich/mempalace
title: MemPalace
description: The highest-scoring AI memory system ever benchmarked. And it's free.
created: 2026-04-10
author: Milla Jovovich & Ben Sigman
license: Open Source
stars: "1200+ (trending)"
category: AI Memory Systems
tags:
  - bookmark
  - ai-memory
  - chromadb
  - local-first
  - mcp-server
  - claude-code
  - long-term-memory
  - rag
---

# MemPalace

![MemPalace Logo](https://raw.githubusercontent.com/milla-jovovich/mempalace/main/assets/mempalace_logo.png)

**The highest-scoring AI memory system ever benchmarked. And it's free.**

## What It Is

MemPalace is a local-first AI memory system that stores all your AI conversations, decisions, and knowledge without relying on cloud APIs or subscriptions. It's inspired by the ancient Greek "Method of Loci" (memory palace technique) where orators memorized speeches by placing ideas in rooms of an imaginary building.

## Key Innovation

Unlike other memory systems that use LLMs to extract and summarize what they think is important (losing context in the process), MemPalace **stores everything verbatim** and makes it findable through semantic search.

## Architecture: The Palace

| Level | Description |
|-------|-------------|
| **Wing** | A project, person, or topic you work with |
| **Rooms** | Subjects related to that wing (ideas, employees, decisions) |
| **Closets** | Storage for AAAK-compressed memories |
| **Drawers** | Individual memory chunks |

## Benchmarks

**96.6% R@5 on LongMemEval** — highest score ever published, free or paid.

| Mode | LongMemEval Score | Notes |
|------|-------------------|-------|
| **Raw (verbatim)** | **96.6%** | Default, zero API calls |
| AAAK | 84.2% | Experimental compression |
| Rooms | Lower | Metadata filtering |

- 500/500 questions independently reproduced
- Zero cloud API calls required
- Runs entirely on local hardware (tested on M2 Ultra)

## AAAK Dialect (Experimental)

AAAK (Name pending — "don't ask, it's a whole story") is a lossy abbreviation dialect that packs repeated entities into fewer tokens. It's readable by any LLM without a decoder.

**Status:** Currently regresses vs raw mode. The team is iterating on it.

## Integration Options

### Claude Code (Recommended)
```bash
claude plugin marketplace add milla-jovovich/mempalace
claude plugin install --scope user mempalace
```

### MCP-Compatible Tools (Claude, ChatGPT, Cursor, Gemini)
```bash
claude mcp add mempalace -- python -m mempalace.mcp_server
```

Provides **19 MCP tools** for AI to search and retrieve memories automatically.

### Local Models (Llama, Mistral)
```bash
# Wake-up command for context
mempalace wake-up > context.txt
# Paste into system prompt

# Or search on demand
mempalace search "auth decisions" > results.txt
```

## Quick Start

```bash
pip install mempalace

# Initialize
mempalace init ~/projects/myapp

# Mine your data
mempalace mine ~/projects/myapp                 # Projects (code, docs)
mempalace mine ~/chats/ --mode convos           # Conversations
mempalace mine ~/chats/ --mode general          # Auto-classified

# Search
mempalace search "why did we switch to GraphQL"
```

## Cost Comparison

| Approach | Annual Cost | Notes |
|----------|-------------|-------|
| Paste everything | Impossible | 19.5M tokens won't fit |
| LLM summaries | ~$507/yr | Loses context |
| **MemPalace wake-up** | **~$0.70/yr** | 170 tokens of critical facts |
| **MemPalace + 5 searches** | **~$10/yr** | Full memory access |

## Honest Assessment (Post-Launch)

The authors published a candid note acknowledging initial issues:

- AAAK token counts were initially miscalculated
- "30x lossless compression" was overstated (AAAK is lossy)
- "+34% palace boost" was misleading (standard metadata filtering)
- Contradiction detection not fully wired

**What remains true:** The 96.6% raw mode score is real and reproducible.

## Why It's Interesting

1. **Local-only** — No data leaves your machine
2. **No subscription** — Free, open source
3. **Verbatim storage** — No LLM decides what's "worth remembering"
4. **MCP-native** — Modern integration with AI tools
5. **Honest benchmarking** — Authors corrected their own claims publicly

## Related

- [[chromadb]] — Vector storage backend
- [[mcp-server]] — Model Context Protocol
- [[claude-code]] — Claude Code plugin system
- [[longmemeval]] — Benchmark dataset

---

*Source: GitHub — milla-jovovich/mempalace*
*Captured: 2026-04-10*
