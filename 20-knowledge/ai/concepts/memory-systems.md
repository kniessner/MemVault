---
title: Memory Systems
created: 2026-04-05
tags: [ai, concept, memory, architecture]
---

# Memory Systems for AI

> Patterns for giving LLMs persistent, structured memory across conversations and sessions.

---

## The Problem

LLMs are **stateless** — each request starts fresh. Without memory:
- No context from previous messages (beyond context window)
- No learning from past interactions
- No user preferences or history
- Every conversation restarts from zero

---

## Types of Memory

### By Duration

| Type | Duration | Example |
|------|----------|---------|
| **Working** | Single conversation | Current chat history |
| **Short-term** | Session | Today's interactions |
| **Long-term** | Persistent | User preferences, facts |
| **Episodic** | Event-based | "Last week we discussed..." |
| **Semantic** | Concept-based | "User likes Python" |

### By Structure

| Type | Structure | Query Method |
|------|-----------|--------------|
| **Buffer** | Raw text | Direct inclusion |
| **Summary** | Condensed | Retrieve full or summary |
| **Vector** | Embeddings | Similarity search |
| **Knowledge Graph** | Entities/relations | Graph traversal |
| **Key-Value** | Structured | Direct lookup |

---

## Pattern 1: Conversation Buffer

Store raw conversation history.

```python
class BufferMemory:
    def __init__(self, max_tokens=4000):
        self.messages = []
        self.max_tokens = max_tokens
    
    def add(self, role, content):
        self.messages.append({"role": role, "content": content})
        self._trim_if_needed()
    
    def get(self):
        return self.messages
    
    def _trim_if_needed(self):
        # Remove oldest if over limit
        while self._token_count() > self.max_tokens:
            self.messages.pop(0)
```

**Pros:** Simple, chronological, transparent  
**Cons:** Context window limits, no prioritization

---

## Pattern 2: Rolling Summary

Summarize old messages, keep recent full.

```python
class SummaryMemory:
    def __init__(self, llm, buffer_size=6):
        self.llm = llm
        self.buffer = []
        self.summary = ""
        self.buffer_size = buffer_size
    
    def add(self, message):
        self.buffer.append(message)
        
        if len(self.buffer) > self.buffer_size:
            # Summarize old buffer
            to_summarize = self.buffer[:-self.buffer_size]
            new_summary = self.llm(f"""
            Current summary: {self.summary}
            
            New messages:
            {to_summarize}
            
            Create updated summary:
            """)
            self.summary = new_summary
            self.buffer = self.buffer[-self.buffer_size:]
    
    def get(self):
        return {
            "summary": self.summary,
            "recent": self.buffer
        }
```

**Pros:** Fits more history, prioritizes recent  
**Cons:** Summarization cost, loss of detail

---

## Pattern 3: Vector Memory

Store facts as embeddings, retrieve relevant.

```python
import chromadb

class VectorMemory:
    def __init__(self, embedding_fn):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("memory")
        self.embed = embedding_fn
    
    def add_fact(self, fact, category="general"):
        embedding = self.embed(fact)
        self.collection.add(
            documents=[fact],
            embeddings=[embedding],
            metadatas=[{"category": category}],
            ids=[str(hash(fact))]
        )
    
    def recall(self, query, k=5):
        query_embedding = self.embed(query)
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )
        return results["documents"][0]

# Usage
memory = VectorMemory(embed_fn)

# Store facts
memory.add_fact("User prefers Python over JavaScript", "preferences")
memory.add_fact("User works at Company X", "facts")
memory.add_fact("Last project was about RAG systems", "history")

# Query context
relevant = memory.recall("What language should I suggest?")
# Returns: ["User prefers Python over JavaScript", ...]
```

**Pros:** Semantic retrieval, scalable  
**Cons:** No chronology, embedding quality matters

---

## Pattern 4: Knowledge Graph Memory

Structured entity-relationship storage.

```python
class KnowledgeGraphMemory:
    def __init__(self):
        self.entities = {}  # name -> {type, attributes}
        self.relations = []  # (subject, predicate, object)
    
    def extract_and_store(self, text):
        # Use LLM to extract
        extraction = llm(f"""
        Extract entities and relations from:
        {text}
        
        Format:
        Entities: name (type)
        Relations: subject -predicate-> object
        """)
        
        # Parse and store
        entities, relations = parse_extraction(extraction)
        for e in entities:
            self.entities[e.name] = e
        self.relations.extend(relations)
    
    def query(self, entity_name):
        # Get entity and related
        entity = self.entities.get(entity_name)
        related = [r for r in self.relations 
                  if r[0] == entity_name or r[2] == entity_name]
        return entity, related

# Usage
memory.extract_and_store("Alice works at Google as an engineer")
# Entity: Alice (person), Google (company)
# Relation: Alice -works_at-> Google
# Relation: Alice -has_role-> engineer

entity, rels = memory.query("Alice")
```

**Pros:** Structured, relational reasoning  
**Cons:** Extraction complexity, graph maintenance

---

## Pattern 5: Entity Memory

Track specific entities mentioned.

```python
class EntityMemory:
    def __init__(self):
        self.entities = {}  # entity_name -> info
    
    def update(self, conversation):
        # Extract entities
        entities = llm(f"""
        Extract entities and what we learned about them:
        
        Conversation:
        {conversation}
        
        Format: entity | information learned
        """)
        
        for line in entities.split("\n"):
            entity, info = parse(line)
            if entity not in self.entities:
                self.entities[entity] = []
            self.entities[entity].append(info)
    
    def get_context(self, query):
        # Find mentioned entities
        mentioned = extract_entities(query)
        context = []
        for e in mentioned:
            if e in self.entities:
                context.append(f"{e}: {self.entities[e]}")
        return context
```

**Pros:** Focus on important entities  
**Cons:** Might miss implicit references

---

## Pattern 6: Hybrid Memory

Combine multiple memory types.

```python
class HybridMemory:
    def __init__(self, llm, embed_fn):
        self.buffer = BufferMemory(max_tokens=2000)
        self.summary = SummaryMemory(llm, buffer_size=4)
        self.vector = VectorMemory(embed_fn)
        self.entities = EntityMemory()
    
    def add(self, role, content):
        # All memory types update
        self.buffer.add(role, content)
        self.summary.add({"role": role, "content": content})
        self.vector.add_fact(content)
        self.entities.update(content)
    
    def get_context(self, query):
        # Gather from all sources
        recent = self.buffer.get()[-4:]  # Last 4 messages
        summary = self.summary.get()
        relevant_facts = self.vector.recall(query, k=3)
        entity_info = self.entities.get_context(query)
        
        # Combine
        return f"""
Summary of conversation: {summary['summary']}

Relevant facts: {relevant_facts}

Entity information: {entity_info}

Recent messages:
{recent}
"""
```

**Pros:** Best of all worlds  
**Cons:** Complexity, multiple failure modes

---

## Memory in Multi-Turn Conversations

```python
def conversation_with_memory():
    memory = HybridMemory(llm, embed_fn)
    
    while True:
        user_input = input("User: ")
        
        # Retrieve context
        context = memory.get_context(user_input)
        
        # Generate response
        response = llm(f"""
        {context}
        
        User: {user_input}
        Assistant:""")
        
        print(f"Assistant: {response}")
        
        # Update memory
        memory.add("user", user_input)
        memory.add("assistant", response)
```

---

## User Profile Memory

Persistent user preferences and facts.

```python
class UserProfile:
    def __init__(self, user_id):
        self.user_id = user_id
        self.profile = self.load(user_id)
    
    def extract_preferences(self, conversation):
        prefs = llm(f"""
        Extract user preferences and facts from this conversation.
        Format as key-value pairs.
        
        Conversation:
        {conversation}
        """)
        
        for line in prefs.split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                self.profile[key.strip()] = value.strip()
        
        self.save()
    
    def get_system_prompt(self):
        return f"""User preferences:
{self.format_profile()}

Adapt your responses accordingly."""
```

---

## Memory Storage Options

| Storage | Persistence | Scale | Latency |
|---------|-------------|-------|---------|
| **In-memory** | ❌ Session | Small | Instant |
| **JSON file** | ✅ Local | Medium | Fast |
| **Redis** | ✅ Server | Large | Fast |
| **Postgres** | ✅ Server | Large | Medium |
| **Vector DB** | ✅ Server | Very Large | Medium |

---

## Best Practices

1. **Prioritize recency** — Recent > old
2. **Summarize aggressively** — Compress history
3. **Extract facts** — Don't store raw text
4. **Tag/contextualize** — Metadata for filtering
5. **Allow forgetting** — Remove outdated info
6. **User control** — Let users edit/clear memory

---

## Resources

- **LangChain Memory**: https://python.langchain.com/docs/modules/memory/
- **MemGPT**: https://memgpt.ai/
- **Socius Memory**: [[socius-memory-architecture]]

---

## Related

- [[20-knowledge/ai/concepts/agent-patterns|Agent Patterns]]
- [[20-knowledge/ai/concepts/rag-patterns|RAG Patterns]]
- [[20-knowledge/ai/providers/anthropic|Anthropic]] — Context window focus

---

*Last updated: 2026-04-05*
