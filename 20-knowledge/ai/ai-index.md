---
title: AI Knowledge Base
created: 2026-03-30
updated: 2026-04-07
tags:
  - type/index
  - topic/ai
  - status/active
---

# 🤖 AI Knowledge Base

*Curated information about AI providers, models, tools, and concepts.*

## Structure

```
ai/
├── providers/     # AI providers & platforms
├── models/        # Specific model documentation
├── tools/         # AI tools, SDKs, frameworks
└── concepts/      # AI concepts, patterns, techniques
```

---

## 🗂️ Ordner-Struktur

```
20-knowledge/ai/
├── models/         # Modell-Spezifikationen & Vergleiche
├── providers/      # API-Provider & Plattformen
├── tools/          # AI-Tools & Frameworks
├── concepts/       # Patterns, Memory, Prompting, Architektur
├── alternatives-*.md  # Vergleiche
└── ai-index.md     # This overview
```

**Nutzen:**
- Modell-Vergleiche und Preise
- Provider-Analysen
- Architektur-Patterns
- Prompting-Techniken

---

## 🧠 Modelle

→ **[[models/models-index|All Models & Comparison Matrix]]**

| Modell | Provider | Kontext | Best For |
|--------|----------|---------|----------|
| Claude 3.7 Sonnet | [[providers/anthropic|Anthropic]] | 200K | Coding, reliability |
| GPT-4o | [[providers/openai|OpenAI]] | 128K | Multimodal, general |
| Gemini 2.0 Pro | [[providers/google|Google]] | 2M | Long context, video |
| Kimi K2.5 | [[providers/moonshot-ai|Moonshot]] | 256K-2M | Ultra-long docs |

---

## 🌐 Provider

→ **[[providers/providers-index|All 10 Providers & Comparison Matrix]]**

| Provider | Besonderheit | Modelle |
|----------|--------------|---------|
| [[providers/anthropic|Anthropic]] | Safety, Claude 3.7 | Sonnet, Haiku |
| [[providers/fal-ai|fal.ai]] | 1,000+ generative media models | FLUX, Kling, Seedance |
| [[providers/google|Google]] | 2M context, multimodal | Gemini 2.0 Pro/Flash |
| [[providers/groq|Groq]] | Ultra-fast inference | Llama, Mixtral |
| [[providers/lm-studio|LM Studio]] | GUI for local LLMs | Any GGUF |
| [[providers/moonshot-ai|Moonshot AI]] | Ultra-long context (2M) | Kimi Modelle |
| [[providers/ollama|Ollama]] | Simple local deployment | Llama, DeepSeek |
| [[providers/openai|OpenAI]] | GPT-4, DALL-E, Whisper | API & ChatGPT |
| [[providers/openrouter|OpenRouter]] | Multi-provider routing | 300+ models |
| [[providers/perplexity|Perplexity]] | Research, citations | Sonar |
| [[providers/z-ai|Z.ai]] | Agentic Engineering | GLM-5 |

---

## 🛠️ Tools

→ **[[tools/tools-index|All Tools & Frameworks]]**

### Coding Agents

| Tool | Category | Best For |
|------|----------|----------|
| [[tools/oh-my-codex|oh-my-codex]] | Codex Enhancement | Workflow layer for OpenAI Codex |
| [[tools/claw-code|claw-code]] | Coding Agent | Clean-room Claude Code rewrite |

### RAG & Document AI

| Tool | Category | Best For |
|------|----------|----------|
| [[tools/pageindex|PageIndex]] | Reasoning RAG | Vectorless document retrieval |

### Local Inference

| Tool | Category | Best For |
|------|----------|----------|
| [[tools/omlx|oMLX]] | macOS Inference | Apple Silicon with SSD KV caching |
| [[tools/llama-cpp|llama.cpp]] | Local Inference | Cross-platform performance |
| [[tools/local-llm-tools|Local LLM Tools]] | Comparison | Choosing tools |
| [[tools/ollama|Ollama]] | Local Deployment | Simple setup |

### Knowledge Management

| Tool | Category | Best For |
|------|----------|----------|
| [[tools/obsidian|Obsidian]] | Knowledge | AI-powered notes |

**Categories:** Coding Agents • RAG/Document AI • Local Inference • Cloud Platforms • Frameworks • Vector DBs

---

## 💡 Konzepte

→ **[[concepts/concepts-index|All Concepts & Patterns]]**

| Konzept | Category | Beschreibung |
|---------|----------|--------------|
| [[concepts/socius-memory-architecture|Socius Memory]] | Memory | Biologisch inspirierte Architektur |
| [[concepts/agentic-research-knowledge-workflows|Agentic Research]] | Agents | Systematic research workflows |

---

## 🔄 Alternativen

- [[alternatives-gemini|Gemini API Alternatives]] — OpenAI, Claude, Mistral...

---

## 📚 Ressourcen

- **Bookmarks:** [[40-library/bookmarks/_example-bookmark|Archivierte AI-Webseiten]]
- **Papers:** `40-library/papers/`
- **News:** [[10-notes/20-ideas/_example-idea|AI News & Updates]]

---

## ➕ Neue Einträge

### Provider hinzufügen:
```markdown
---
title: Provider Name
url: https://provider.com
tags: [ai, provider]
---
```
→ In `20-knowledge/ai/providers/`

### Konzept hinzufügen:
```markdown
---
title: Concept Name
tags: [ai, concept]
---
```
→ In `20-knowledge/ai/concepts/`

---

*Letzte Aktualisierung: 2026-04-05*
