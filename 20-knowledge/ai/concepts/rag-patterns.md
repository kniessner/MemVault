---
title: RAG Patterns
created: 2026-04-05
tags: [ai, concept, rag, architecture]
---

# RAG (Retrieval-Augmented Generation) Patterns

> Patterns for connecting LLMs to external knowledge sources — the dominant architecture for knowledge-heavy AI applications.

## Overview

RAG combines retrieval systems with generative models to:
- Ground responses in factual data
- Reduce hallucinations
- Access domain-specific knowledge
- Work with private/recent data

---

## Core Architecture

```
User Query
    ↓
[Embedding] → Vector DB Search → Relevant Chunks
    ↓                    ↓
[Query] + [Context] → LLM → Response
```

---

## Pattern 1: Basic RAG

Simplest implementation — single retrieval pass.

```python
from openai import OpenAI
import chromadb

client = OpenAI()
chroma = chromadb.Client()
collection = chroma.get_collection("docs")

# Embed query
query_embedding = client.embeddings.create(
    model="text-embedding-3-small",
    input=user_query
).data[0].embedding

# Retrieve
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5
)

# Generate
context = "\n\n".join(results["documents"][0])
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role": "system",
        "content": f"Answer using this context:\n{context}"
    }, {
        "role": "user", 
        "content": user_query
    }]
)
```

**Best for:** Simple Q&A over documents

---

## Pattern 2: Query Expansion

Improve retrieval by expanding the query.

### HyDE (Hypothetical Document Embedding)

```python
# Generate hypothetical answer
hypothetical = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "user",
        "content": f"Write a brief answer to: {query}"
    }]
).choices[0].message.content

# Embed hypothetical answer
query_embedding = embed(hypothetical)

# Retrieve
results = collection.query(query_embeddings=[query_embedding])
```

### Multi-Query

```python
# Generate variations
variations = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "user",
        "content": f"Generate 3 different ways to ask: {query}"
    }]
).choices[0].message.content

# Retrieve with all variations
queries = parse_variations(variations)
all_results = []
for q in queries:
    results = collection.query(query_embeddings=[embed(q)])
    all_results.extend(results)

# Deduplicate and rerank
```

**Best for:** Queries with domain-specific vocabulary, user queries don't match document language

---

## Pattern 3: Re-ranking

Retrieve more, then rank by relevance.

```python
# Step 1: Retrieve many
initial_results = collection.query(
    query_embeddings=[query_embedding],
    n_results=20  # More than needed
)

# Step 2: Re-rank with cross-encoder
from sentence_transformers import CrossEncoder
reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

pairs = [(query, doc) for doc in initial_results["documents"][0]]
scores = reranker.predict(pairs)

# Step 3: Take top-k
sorted_results = sorted(
    zip(initial_results["documents"][0], scores),
    key=lambda x: x[1],
    reverse=True
)[:5]
```

**Best for:** High-stakes applications where precision matters

---

## Pattern 4: Hierarchical Retrieval

Retrieve at different granularities.

```python
# Level 1: Document-level summaries
doc_results = doc_summaries.query(
    query_embeddings=[query_embedding],
    n_results=3
)

# Level 2: Section-level within top documents
for doc_id in doc_results["ids"][0]:
    section_results = sections.query(
        query_embeddings=[query_embedding],
        where={"doc_id": doc_id},
        n_results=5
    )
```

**Best for:** Large documents, books, reports

---

## Pattern 5: Contextual Chunking

Add context to each chunk.

```python
def create_contextual_chunks(document):
    chunks = chunk_text(document, size=500, overlap=50)
    contextualized = []
    
    for i, chunk in enumerate(chunks):
        # Get context
        context_prompt = f"""
        Document: {document[:1000]}...
        
        This chunk is from that document:
        {chunk}
        
        Summarize the context this chunk sits within (1 sentence):
        """
        
        context = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": context_prompt}]
        ).choices[0].message.content
        
        contextualized.append({
            "text": f"Context: {context}\n\nChunk: {chunk}",
            "metadata": {"index": i}
        })
    
    return contextualized
```

**Best for:** Documents where chunk meaning depends on surrounding context

---

## Pattern 6: Iterative / Self-RAG

LLM decides when to retrieve more.

```python
messages = [{"role": "user", "content": query}]
max_iterations = 3

for i in range(max_iterations):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=[{
            "type": "function",
            "function": {
                "name": "retrieve",
                "description": "Get more information",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "search_query": {"type": "string"}
                    }
                }
            }
        }]
    )
    
    if not response.choices[0].message.tool_calls:
        break  # Model is satisfied
    
    # Execute retrieval
    tool_call = response.choices[0].message.tool_calls[0]
    search_query = json.loads(tool_call.function.arguments)["search_query"]
    
    results = retrieve(search_query)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": str(results)
    })
```

**Best for:** Complex research questions, multi-hop reasoning

---

## Pattern 7: Graph RAG

Use knowledge graphs for structured retrieval.

```python
# Query knowledge graph
entities = extract_entities(query)
graph_results = graph.query("""
    MATCH (e:Entity)-[:RELATES_TO]->(related)
    WHERE e.name IN $entities
    RETURN e, related
"", entities=entities)

# Combine with vector search
vector_results = collection.query(query_embeddings=[query_embedding])

# Merge and deduplicate
combined = merge_results(graph_results, vector_results)
```

**Best for:** Relationship-heavy domains (biomedical, legal, enterprise)

---

## Chunking Strategies

| Strategy | Best For | Size |
|----------|----------|------|
| **Fixed** | Uniform documents | 256-512 tokens |
| **Sentence** | Preserves meaning | Variable |
| **Paragraph** | Natural boundaries | Variable |
| **Semantic** | ML-based splits | Dynamic |
| **Hierarchical** | Multi-level access | Levels |

---

## Embedding Selection

| Model | Dim | Languages | Best For |
|-------|-----|-----------|----------|
| **text-embedding-3-small** | 1536 | EN | General, cheap |
| **text-embedding-3-large** | 3072 | EN | Quality |
| **bge-m3** | 1024 | Multi | Multilingual |
| **nomic-embed-text** | 768 | EN | Open |
| **e5-mistral** | 4096 | Multi | Long docs |

---

## Vector Database Comparison

| Database | Type | Best For |
|----------|------|----------|
| **Pinecone** | Managed | Production, scale |
| **Weaviate** | OSS/Cloud | Semantic search |
| **Chroma** | Local | Development |
| **Qdrant** | OSS/Cloud | Filtering, hybrid |
| **pgvector** | Postgres | SQL-native |
| **Milvus** | OSS | Enterprise scale |

---

## When to Use What

| Use Case | Pattern |
|----------|---------|
| Simple docs Q&A | Basic RAG |
| User queries ≠ doc language | Query expansion |
| High precision needed | Re-ranking |
| Books, long reports | Hierarchical |
| Complex dependencies | Contextual chunks |
| Research, investigation | Self-RAG |
| Relationship-heavy | Graph RAG |

---

## Anti-Patterns

❌ **Too small chunks** — Lose context
❌ **No overlap** — Miss boundaries
❌ **Single embedding** — No re-ranking
❌ **No metadata filtering** — Can't narrow
❌ **Retrieving 1 result** — No room for error
❌ **No source attribution** — Can't verify

---

## Resources

- **OpenAI Cookbook**: https://github.com/openai/openai-cookbook
- **LangChain RAG**: https://python.langchain.com/docs/use_cases/question_answering/
- **LlamaIndex**: https://docs.llamaindex.ai/en/stable/

---

## Related

- [[20-knowledge/ai/concepts/prompt-engineering|Prompt Engineering]]
- [[20-knowledge/ai/concepts/agent-patterns|Agent Patterns]]
- [[20-knowledge/ai/tools/llamaindex|LlamaIndex]]

---

*Last updated: 2026-04-05*
