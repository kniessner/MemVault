---
title: Mem0
category: tools
url: https://mem0.ai/
founded: 2024
tags: [memory, vector-db, ai-memory, semantic-search, embedding]
pricing: freemium
free_tier: yes
api: yes
self_hostable: yes
---

# Mem0

> The Memory Layer for your AI Apps — self-improving memory for any LLM.

![Mem0 Logo](https://framerusercontent.com/images/LSW9rnFnG91ayf102rTo996iAS8.png)

## Overview

Mem0 is a **dedicated memory service** that adds persistent, self-improving memory capabilities to AI applications. Unlike simple conversation history, Mem0 extracts facts, learns preferences, and enables semantic retrieval across sessions.

| Attribute | Value |
|-----------|-------|
| **Company** | Mem0 Inc. |
| **Founded** | 2024 |
| **Type** | Memory-as-a-Service |
| **Open Source** | ✅ Yes (<github.com/mem0ai/mem0>) |
| **API** | REST + Python/Node.js SDKs |

## Key Capabilities

| Feature | Description |
|---------|-------------|
| **Multi-level Memory** | User, session, and agent-level scopes |
| **Semantic Search** | Vector-based retrieval (not keyword) |
| **Self-Improving** | Automatic fact extraction from conversations |
| **Multi-tenant** | Isolated memory per user |
| **Provider Agnostic** | Works with any LLM |
| **Hybrid Storage** | Vector DB + structured metadata |

## Architecture

```
User Input
    ↓
Mem0 API
    ↓
├─→ Vector DB (Pinecone/Weaviate/Qdrant)
├─→ Fact Extraction (LLM-based NLP)
└─→ Memory Store (versioned, timestamped)
    ↓
Agent Context ← Retrieved via semantic similarity
```

## Pricing (April 2026)

| Tier | Price | Included | Best For |
|------|-------|----------|----------|
| **Free** | $0 | 10K API calls/mo | Prototyping |
| **Developer** | $15/mo | 100K calls | Individual devs |
| **Pro** | $75/mo | 500K calls | Small teams |
| **Enterprise** | Custom | Unlimited | Production scale |

## Quick Start

```python
import mem0

# Initialize
m = mem0.Memory(api_key="m0-xxxxx")

# Add memory
m.add(
    "User prefers Python over JavaScript for automation",
    user_id="darius",
    metadata={"category": "preference", "confidence": 0.95}
)

# Retrieve relevant memories
memories = m.search(
    "What language should I use for scripting?",
    user_id="darius",
    limit=5
)

# Results include semantic matches even if keywords differ
```

## Memory Types

| Type | Use Case | Example |
|------|----------|---------|
| **Facts** | User information | "Works at Acme Corp" |
| **Preferences** | Style choices | "Prefers terse responses" |
| **Relationships** | Connected entities | "Manager is Sarah" |
| **Events** | Temporal data | "Met with team on Monday" |
| **Procedures** | Learned workflows | "Always runs tests before commit" |

## Integration Patterns

### With Hermes Agent

```python
# tools/mem0_memory.py
def store_user_fact(fact: str, user_id: str = None):
    """Store a fact about the user."""
    if not os.getenv("MEM0_API_KEY"):
        # Fallback to native memory
        return memory(action="add", target="memory", content=fact)
    
    m = mem0.Memory()
    return m.add(fact, user_id=user_id or get_current_user())

def get_relevant_context(query: str, user_id: str = None):
    """Retrieve memories relevant to current context."""
    if not os.getenv("MEM0_API_KEY"):
        # Fallback to session_search
        return session_search(query)
    
    m = mem0.Memory()
    return m.search(query, user_id=user_id or get_current_user())
```

### Configuration

```yaml
# ~/.hermes/config.yaml
memory:
  provider: mem0  # or "native"
  api_key: ${MEM0_API_KEY}
  vector_store: pinecone  # pinecone|weaviate|qdrant
  embedding_model: text-embedding-3-small
```

## Self-Hosting

```bash
# Clone and run locally
git clone https://github.com/mem0ai/mem0.git
cd mem0
docker-compose up -d

# Uses:
# - Qdrant (vector DB)
# - PostgreSQL (metadata)
# - Redis (caching)
```

## Comparison to Native Memory

| Capability | Hermes Native | Mem0 |
|------------|---------------|------|
| Persistence | ✅ SQLite | ✅ Cloud/self-hosted |
| Semantic search | ❌ Keyword only | ✅ Vector similarity |
| Fact extraction | ❌ Manual | ✅ Automatic |
| Multi-user | ❌ Single user | ✅ Multi-tenant |
| Offline use | ✅ Fully local | ❌ Requires network |
| Cost | Free | Free tier → Paid |
| Privacy | Absolute | Configurable |

## When to Use

### Use Mem0 When:
- ✅ Need semantic search across sessions
- ✅ Building multi-user applications
- ✅ Want automatic fact extraction
- ✅ Scale requires managed infrastructure

### Stick with Native When:
- ✅ Privacy requirements are strict
- ✅ Offline/air-gapped operation
- ✅ Simple use cases (preferences, notes)
- ✅ Minimizing external dependencies

## Competitors

| Provider | Type | Differentiator |
|----------|------|----------------|
| **Hindsight** | Vector DB | Automatic entity extraction |
| **ByteRover** | Graph memory | Relationship mapping |
| **Supermemory** | Hybrid | Task-oriented tracking |
| **Zep** | Memory | Long-term conversation recall |

## Resources

| Resource | URL |
|----------|-----|
| Website | https://mem0.ai |
| GitHub | https://github.com/mem0ai/mem0 |
| Docs | https://docs.mem0.ai |
| Discord | discord.gg/mem0 |

## Related

- [Agent Memory Systems](../concepts/agent-memory-systems.md) — Full comparison
- [Vector Databases](../../databases/vector-databases.md) — Storage options
- [Hermes Agent](../providers/hermes-agent.md) — Integration target

---

*Archived: 2026-04-19*  
*Source: mem0.ai website, GitHub repository*
