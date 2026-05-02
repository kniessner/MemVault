---
title: Agent Memory Systems Comparison
url: 
created: 2026-04-19
category: concepts
tags: [memory, agents, ai-architecture, mem0, hermes, comparison]
---

# Agent Memory Systems

Analysis of memory systems for AI agents - comparing approaches, providers, and integration strategies for our Hermes setup.

---

## Quick Overview Table

| System | Type | Hosting | Integration | Best For |
|--------|------|---------|-------------|----------|
| **Hermes Native Memory** | Built-in | Local | Native | Session persistence, user preferences |
| **Mem0** | External API | Cloud/Self-hosted | API | Cross-session learning, user history |
| **Agent37** | Managed Hosting | Cloud | Full stack | Non-technical users, quick deployment |
| **Hindsight** | Vector DB | Cloud | SDK | Long-term facts, entity extraction |
| **ByteRover** | Graph Memory | Cloud | SDK | Relationship tracking |
| **Supermemory** | Hybrid | Cloud | API | Task-oriented memory |

---

## 1. Hermes Native Memory System

### Current Implementation
Hermes Agent includes several memory layers:

**`~/.hermes/` Structure:**
```
~/.hermes/
├── config.yaml              # User preferences, themes, display settings
├── .env                     # API keys (provider credentials)
├── sessions/                # SQLite conversation persistence
│   └── ...
├── skills/                  # User-installed skills
│   └── ...
└── profiles/                # Multiple profile support
    └── ...
```

**Memory Types:**

| Type | File/API | Use Case |
|------|----------|----------|
| **`memory` tool** | `target: memory` | User notes, environment facts, learned conventions |
| **`user` profile** | `target: user` | User identity, preferences, communication style |
| **Session persistence** | `hermes_state.py` | Conversation history, context across restarts |
| **Skills** | `~/.hermes/skills/` | Reusable procedures, workflows |
| **Config** | `config.yaml` | Tool enablement, model preferences, display settings |

### How It Works
- **Store:** `memory(action="add", target="memory", content="fact...")`
- **Retrieve:** Auto-injected into system prompt every session
- **Search:** `session_search(query)` for conversation recall

### Limitations for Our Consideration
- ❌ No cross-user memory (single user per instance)
- ❌ No semantic search (keyword only via FTS5)
- ❌ No vector embeddings
- ✅ Privacy-first (local only)
- ✅ Works offline

---

## 2. Mem0 (mem0.ai)

> "The Memory Layer for your AI Apps"

### Overview
Mem0 is a **dedicated memory service** that adds persistent, self-improving memory to any AI application. It's provider-agnostic and can integrate with any LLM.

### Key Features
| Feature | Description |
|---------|-------------|
| **Multi-level Memory** | User, session, and agent-level memory scopes |
| **Self-improving** | Automatically extracts facts, preferences, relationships |
| **Vector Search** | Semantic retrieval, not just keyword |
| **Multi-tenant** | Supports multiple users with isolated memory |
| **API-first** | REST API with Python/JS SDKs |
| **Open Source** | Self-hostable (<github.com/mem0ai/mem0>) |

### Pricing (as of Apr 2026)
| Tier | Price | Limits |
|------|-------|--------|
| **Free** | $0 | 10K API calls/month |
| **Developer** | $15/mo | 100K calls |
| **Pro** | $75/mo | 500K calls |
| **Enterprise** | Custom | Unlimited |

### Architecture
```
User Input → Mem0 API → Vector DB (Pinecone/Weaviate/Qdrant)
                        ↓
              Fact Extraction (LLM-based)
                        ↓
              Memory Store + Semantic Index
                        ↓
Agent Context ← Relevant Memories Retrieved
```

### Integration for Hermes
```python
# New tool: mem0_memory.py
import mem0

m = mem0.Memory(api_key=os.getenv("MEM0_API_KEY"))

# Add memory
m.add("User prefers Python for scripting", user_id="darius")

# Retrieve for context
memories = m.search("scripting preferences", user_id="darius")
```

### Pros/Cons for Our Setup
| ✅ Pros | ❌ Cons |
|---------|---------|
| Semantic search vs keyword | Adds external dependency |
| Cross-session intelligence | Costs at scale |
| Can self-host (privacy) | Another infra component |
| Works with any LLM | Requires API integration |

---

## 3. Agent37 (agent37.com)

> "Managed OpenClaw Hosting & Skill Monetization"

### What It Actually Is
**NOT a memory system** - it's a **managed hosting service** for OpenClaw (similar agent framework).

### Offering
| Feature | Description |
|---------|-------------|
| **Price** | $9.99/mo |
| **Includes** | Pre-configured OpenClaw instance |
| **Setup** | "Live in ~30s" |
| **Extras** | Skill marketplace, monetization |

### Relevance to Us
- **Low** - This is a competitor/alternative hosting model
- Might be interesting for comparison re: managed Hermes offerings
- Not relevant for memory architecture decisions

---

## 4. Hermes WebUI (hermes-webui)

> "Web interface for Hermes Agent — full CLI parity"

### GitHub
`github.com/nesquena/hermes-webui`

### Features
| Feature | Description |
|---------|-------------|
| **Layout** | Three-panel (sessions, chat, workspace) |
| **Controls** | Model switcher, profile selector, token ring |
| **Workspace** | File browser with inline preview |
| **Sessions** | Projects, tags, tool call cards |
| **Stack** | Python + vanilla JS (no build step) |
| **Auth** | Password protection, SSH tunnel access |

### Memory Integration
- Uses same `~/.hermes/` storage as CLI
- No additional memory layer
- Just a **different interface** to same Hermes instance

### Suitability for Us
✅ **Good** if we want browser-based access to our Hermes instance
❌ **Not a memory enhancement** - just a UI alternative

---

## 5. Hermes Desktop (hermes-desktop)

> "Native desktop app for Hermes Agent"

### GitHub
`github.com/fathah/hermes-desktop`

### Features
- **Guided install** with dependency resolution
- **Multi-provider support** (OpenRouter, Anthropic, OpenAI, etc.)
- **Streaming chat** with markdown, syntax highlighting
- **22 slash commands** (`/memory`, `/tools`, `/skills`, etc.)
- **Token tracking** with live cost display
- **Session management** with projects/tags

### Memory Integration
- Same as CLI - uses native Hermes memory
- Has `/memory` slash command for user memory management
- No external memory provider integration (yet)

### Suitability for Us
✅ Good for non-technical users who want GUI
❌ Still limited to Hermes native memory

---

## 6. Other Memory Providers (from get-hermes.ai guide)

Based on the memory provider comparison guide at get-hermes.ai:

### Hindsight
| Attribute | Value |
|-----------|-------|
| **Type** | Vector-based fact storage |
| **Focus** | Long-term factual memory |
| **Extraction** | Automatic entity/relationship extraction |
| **Use Case** | Knowledge bases, research agents |

### ByteRover
| Attribute | Value |
|-----------|-------|
| **Type** | Graph-based memory |
| **Focus** | Relationship mapping |
| **Query** | Graph traversal for context |
| **Use Case** | Multi-hop reasoning, connected data |

### Supermemory
| Attribute | Value |
|-----------|-------|
| **Type** | Hybrid (vector + structured) |
| **Focus** | Task completion history |
| **Features** | Goal tracking, action consequences |
| **Use Case** | Task-oriented agents |

---

## Our Recommendation

### For Current Hermes Setup

**Keep native memory for:**
- User preferences (`target: user`)
- Environment facts (`target: memory`)
- Session persistence (SQLite)

**Consider adding Mem0 for:**
- Semantic memory retrieval (current system is keyword-only)
- Cross-session intelligence beyond simple preference storage
- If we add multi-user support later

### Implementation Path

1. **Short-term:** Enhance native memory usage
   - Better structured templates for `memory` tool
   - Automatic categorization (e.g., `category: workflow`, `category: preference`)
   - Periodic memory consolidation

2. **Medium-term:** Evaluate Mem0 integration
   ```python
   # Potential new tool: semantic_memory.py
   if os.getenv("MEM0_API_KEY"):
       # Use Mem0 for semantic retrieval
   else:
       # Fallback to native memory
   ```

3. **Long-term:** Hybrid approach
   - Native: Fast, offline, preferences
   - Mem0: Semantic search, cross-session learning
   - Configurable per profile

### Key Files to Create
- `~/.hermes/skills/memory-management/` - Enhanced memory workflows
- Document: `20-knowledge/ai/concepts/memory-design-patterns.md`
- Comparison: `20-knowledge/ai/tools/mem0-integration-guide.md`

---

## Related Resources

| Resource | URL | Notes |
|----------|-----|-------|
| Mem0 GitHub | github.com/mem0ai/mem0 | Self-hostable |
| Hermes WebUI | github.com/nesquena/hermes-webui | Browser UI |
| Hermes Desktop | github.com/fathah/hermes-desktop | Native GUI |
| Agent37 | agent37.com | Managed hosting |
| Memory Guide | get-hermes.ai/memory/ | Provider comparison |

---

*Last updated: 2026-04-19*
*Analysis for: Hermes Agent memory architecture decisions*
