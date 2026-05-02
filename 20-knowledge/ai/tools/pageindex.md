---
title: PageIndex
description: Vectorless, reasoning-based RAG engine that mirrors how humans read documents
url: https://pageindex.ai
github: https://github.com/VectifyAI/PageIndex
docs: https://docs.pageindex.ai
chat: https://chat.pageindex.ai
founded: 2025
company: Vectify AI
authors:
  - Mingtian Zhang
  - Yu Tang
category: tool
tags:
  - rag
  - retrieval
  - document-ai
  - vectorless
  - reasoning
  - mcp
  - api
status: active
pricing: Free tier available, premium enterprise plans
---

# PageIndex

**PageIndex** is a vectorless, reasoning-based retrieval framework that simulates how human experts extract knowledge from complex documents. Instead of relying on vector similarity search, it builds a tree-structured index from documents and enables LLMs to perform agentic reasoning over that structure for context-aware retrieval.

## Core Concept

Traditional RAG systems rely on vector similarity search and chunking, which often fail to capture the semantic structure of documents. PageIndex takes a different approach:

- **No vector databases required**
- **No arbitrary chunking**
- **Tree-structured document index** (PageIndex/ToC-based)
- **Agentic reasoning** over document structure
- **Traceable and interpretable** retrieval process

## How It Works

### 1. Document Indexing
Documents are parsed into a hierarchical tree structure based on:
- Table of Contents (ToC)
- Page structure
- Section hierarchy
- Natural document boundaries

### 2. Reasoning-Based Retrieval
Instead of vector similarity, PageIndex uses LLM reasoning to:
- Navigate the document tree
- Identify relevant sections
- Follow in-document references (e.g., "see Appendix G")
- Iteratively fetch neighboring sections when context is incomplete

### 3. Context-Aware Understanding
The system integrates:
- **Chat history** for multi-turn context
- **Cross-references** within documents
- **Semantic coherence** (full sections rather than arbitrary chunks)

## Key Advantages Over Vector RAG

| Limitation | Vector-based RAG | Reasoning-based RAG (PageIndex) |
|------------|-----------------|--------------------------------|
| Query–Knowledge Mismatch | Matches surface similarity; often misses context | Uses inference to identify relevant sections |
| Similarity ≠ Relevance | Retrieves semantically similar but irrelevant chunks | Retrieves contextually relevant information |
| Hard Chunking | Fixed-length chunks fragment meaning | Retrieves coherent sections dynamically |
| No Chat Context | Each query isolated | Multi-turn reasoning considers prior context |
| Cross-References | Fails to follow internal links | Follows references via ToC/PageIndex reasoning |

## Performance

- **98.7% accuracy** on FinanceBench benchmark
- Handles long documents effectively
- Exact page reference citations

## Integration Options

### 1. Chat Platform
Web interface at [chat.pageindex.ai](https://chat.pageindex.ai)

### 2. MCP (Model Context Protocol)
Integrate with MCP-compatible clients:
```json
{
  "mcpServers": {
    "pageindex": {
      "command": "npx",
      "args": ["-y", "@pageindex/mcp-server"],
      "env": {
        "PAGEINDEX_API_KEY": "your-api-key"
      }
    }
  }
}
```

### 3. REST API
Direct API access for custom integrations:
- Documentation: [docs.pageindex.ai/quickstart](https://docs.pageindex.ai/quickstart)

## Use Cases

- **Financial document analysis** (10-K, 10-Q reports)
- **Legal document review**
- **Research paper exploration**
- **Technical documentation Q&A**
- **Complex multi-document queries**

## Example: Following References

In the [PageIndex MCP example](https://claude.ai/share/b29bdfac-f22a-478d-ac1e-00e604c4f3fd), a query asked for the *total value of deferred assets*. The main section (pages 75–82) only reported the *increase* in value. On page 77, the text referenced "Appendix G" for more details. The reasoning-based retriever followed this cue to Appendix G, found the correct table, and returned the total deferred asset value — a task vector-based retrievers would likely fail.

## Resources

- **GitHub**: [github.com/VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)
- **Documentation**: [docs.pageindex.ai](https://docs.pageindex.ai)
- **Cookbooks**: [docs.pageindex.ai/cookbook](https://docs.pageindex.ai/cookbook)
- **Tutorials**: [docs.pageindex.ai/tutorials](https://docs.pageindex.ai/tutorials)

## Citation

```bibtex
@article{zhang2025pageindex,
  author = {Mingtian Zhang and Yu Tang and PageIndex Team},
  title = {PageIndex: Next-Generation Vectorless, Reasoning-based RAG},
  journal = {PageIndex Blog},
  year = {2025},
  month = {September},
  note = {https://pageindex.ai/blog/pageindex-intro}
}
```

## Related Concepts

- [[concepts/rag|RAG (Retrieval-Augmented Generation)]]
- [[concepts/agents|AI Agents]]
- [[providers/anthropic|Anthropic]] (Claude integration)
