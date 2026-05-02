---
url: https://onyx.app/
title: Onyx
source_doc: https://docs.onyx.app/
description: Open-source AI enterprise search and chat platform for workplace knowledge
author: Onyx (formerly Danswer)
created: 2026-04-27
license: MIT
category: Enterprise Search / RAG
pricing: Free (self-hosted) / Cloud
tags:
  - bookmark
  - enterprise-search
  - ai-assistant
  - rag
  - self-hosted
  - open-source
  - internal-knowledge
  - knowledge-base
  - workplace-search
  - chatbot
---

# Onyx

> Open-source AI enterprise search. Ask questions across all your company data. Grounded, accurate, and self-hostable.

## Overview

**Onyx** (formerly *Danswer*) is a self-hosted, open-source AI search platform that connects to all your company data sources and lets employees ask questions in natural language. Think "ChatGPT for your company's knowledge."

| Attribute | Value |
|-----------|-------|
| **Website** | https://onyx.app |
| **Docs** | https://docs.onyx.app |
| **GitHub** | github.com/onyx-dot-app/onyx |
| **License** | MIT |
| **Pricing** | Free (self-hosted) / Cloud plans available |
| **Category** | Enterprise AI Search |

## Key Features

| Feature | Description |
|---------|-------------|
| **Grounded answers** | Responses cite actual sources; no hallucination on your data |
| **Hybrid search** | Combines hybrid search, advanced RAG, contextual retrieval, and LLM-based knowledge graphs |
| **Real-time sync** | Pulls in updates from connected sources automatically |
| **Access controls** | Respects fine-grained permissions from connected tools |
| **Multi-platform chat** | Deep research, MCP, code interpreter, web search, and advanced chat features |
| **Open source** | Fully MIT licensed; self-host on any infrastructure |
| **Plug-and-play connectors** | Connects to 25+ workplace tools |

## Supported Integrations (Connectors)

| Source | Status |
|--------|--------|
| Slack | ✅ |
| Confluence | ✅ |
| Notion | ✅ |
| Google Drive | ✅ |
| GitHub | ✅ |
| GitLab | ✅ |
| Jira | ✅ |
| Asana | ✅ |
| Microsoft SharePoint | ✅ |
| Salesforce | ✅ |
| Website crawling | ✅ |
| (25+ total connectors) | — |

## Architecture

| Component | Tech |
|-----------|------|
| **Search engine** | Hybrid search + RAG + contextual retrieval + knowledge graphs |
| **Embeddings** | Configurable (OpenAI, Cohere, local) |
| **LLM** | OpenAI, Anthropic, local, Azure, etc. |
| **Database** | PostgreSQL |
| **Vector store** | Qdrant / PgVector |
| **Deployment** | Docker Compose, Kubernetes, or cloud-managed |

## Deployment Options

| Option | Cost | Best For |
|--------|------|----------|
| **Self-hosted (Docker/K8s)** | Infrastructure only | Security/privacy-sensitive orgs |
| **Cloud managed** | Per-query/retainer | Teams without DevOps |

## Self-Hosted Quick Start

```bash
# Using Docker Compose
git clone https://github.com/onyx-dot-app/onyx.git
cd onyx/deployment/docker_compose
docker compose -f docker-compose.dev.yml -d up

# Access at http://localhost:3000
```

## Use Cases

| Use Case | How Onyx Helps |
|----------|---------------|
| **Onboarding** | New hires ask "How do I deploy?" and get contextual answers from docs, Slack, and Notion |
| **Support teams** | Find answers from past tickets and internal KB articles |
| **Engineering** | Search across PRs, issues, Confluence pages, and design docs |
| **Sales** | Find relevant case studies and competitive intel |
| **Compliance** | Maintain audit trail of all answers and sources |

## Why It Matters

1. **Privacy-first** — Self-hosted option means company data never leaves your infrastructure
2. **Source-verified** — Every answer is grounded in actual documents with citations
3. **Access-aware** — Respects permissions from connected tools (e.g., private Slack channels)
4. **Tested rigorously** — Evaluated on 99 real workplace questions across 220K+ documents

## Comparison

| | Onyx | Enterprise Bing / Copilot | Glean | Guru |
|---|------|--------------------------|-------|------|
| **Open source** | ✅ MIT | ❌ | ❌ | ❌ |
| **Self-hosted** | ✅ | ❌ | ❌ | ❌ |
| **Citations** | ✅ | ✅ | ✅ | ✅ |
| **Connectors** | 25+ | Microsoft | Proprietary | Proprietary |
| **Price** | Free / cloud | Enterprise | Enterprise | Enterprise |
| **LLM choice** | Any provider | Copilot only | Internal | Internal |

## Related

- [[rag]] — Retrieval-Augmented Generation concepts
- [[llamaindex]] — RAG framework alternative
- [[pinecone]] — Managed vector database option
- [[weaviate]] — Open-source vector search alternative

---

*Last updated: 2026-04-27*
