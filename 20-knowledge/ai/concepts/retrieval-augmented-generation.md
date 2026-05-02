---
title: "Retrieval-Augmented Generation (RAG)"
description: "Pattern for grounding LLM outputs in a private document corpus at query time"
created: 2026-01-01
tags:
  - status/active
  - type/note
  - ai
related:
  - "[[embeddings]]"
  - "[[vector-databases]]"
---

## Definition

RAG retrieves relevant documents at query time and injects them into the LLM prompt, reducing hallucination and enabling knowledge that post-dates training.

## Key Components

| Component | Role |
|---|---|
| Chunker | Splits documents into retrievable units |
| Embedder | Converts chunks to vector space |
| Vector DB | Stores and searches embeddings |
| Retriever | Fetches top-k relevant chunks |
| Generator | LLM that answers with retrieved context |

## When to Use

- Private knowledge not in training data
- Freshness required (news, prices, live docs)
- Source attribution is required

## Variants

- **Naive RAG** — single retrieval pass, no post-processing
- **Advanced RAG** — re-ranking, query rewriting, iterative retrieval
- **Modular RAG** — composable pipeline stages (routing, fusion, summarization)
- **Graph RAG** — retrieval over a knowledge graph instead of flat vector store

## Related

[[embeddings]] · [[vector-databases]] · [[agents]]
