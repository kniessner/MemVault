# MemVault

A structured Obsidian vault that turns an AI agent into a knowledge curator. The agent reads sources, synthesizes insights, maintains cross-references, and grows a knowledge graph that gets more useful every time you use it. You direct; the agent maintains.

## The Compounding Knowledge Pattern

Most people use LLMs with documents like this: upload files, the LLM retrieves relevant chunks, generate an answer, done. Next question, same process from scratch. Nothing accumulates. The LLM rediscovers knowledge fresh every time.

MemVault does something different. The agent doesn't just retrieve — it **builds and maintains a persistent wiki**. When you add a source, the agent reads it, extracts key information, and integrates it across existing pages: updating entity pages, adding cross-references, noting contradictions with older claims, strengthening the evolving synthesis. When you ask a question, the agent draws on pages that already reflect everything you've read before.

The wiki is the persistent artifact. Conversations are ephemeral; the knowledge base compounds.

### How it works

**Ingest.** You bring sources — articles, papers, URLs, meeting notes, book chapters. The agent reads each source, writes summary pages, updates related pages across the wiki, and appends to the daily log. A single source might touch 5-10 wiki pages.

**Query.** You ask questions. The agent searches the wiki, synthesizes answers with citations, and files any valuable new insights back as new pages. Good answers become new knowledge — they don't disappear into chat history.

**Lint.** Periodically, the agent checks for orphans, stale claims, missing links, and contradictions. The wiki stays healthy because maintenance is cheap for an LLM and expensive for a human.

### Three layers

| Layer | Folders | What happens here |
|---|---|---|
| **Capture** | `00-inbox/`, `10-notes/` | Raw, ephemeral — drafts, daily logs, unprocessed notes |
| **Knowledge** | `20-knowledge/`, `12-mocs/`, `30-projects/` | Curated — agent-maintained, interlinked, evergreen |
| **Reference** | `40-library/`, `_assets/` | Immutable — sources as-is, never modified |

Raw sources stay untouched in `40-library/bookmarks/`. Knowledge pages in `20-knowledge/` evolve over time. This separation is what makes compounding work: sources stay clean, synthesis pages grow richer.

### Why this works

The tedious part of maintaining a knowledge base isn't reading or thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, flagging contradictions, maintaining consistency across dozens of pages. Humans abandon wikis because maintenance burden grows faster than value. An LLM doesn't get bored, doesn't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost is near zero.

Your job is to curate sources, direct analysis, and ask good questions. The agent handles everything else.

## Quickstart

### Path A — Agent setup (no terminal needed)

1. **Clone or download** this repository into a folder of your choice
2. **Open the folder in Obsidian** — File → Open Vault → select the folder
3. **Enable JavaScript in Dataview** — Settings → Community Plugins → Dataview → toggle "Enable JavaScript Queries"
4. **Start your AI agent** from inside the vault directory
5. The agent reads `BOOTSTRAP.md` and guides you through a short Q&A to personalize the vault
6. Done — `BOOTSTRAP.md` is deleted when setup is complete

### Path B — CLI setup

```bash
python3 init.py        # guided setup
python3 init.py --dry-run   # preview without writing
```

Requires Python 3.8+ (pre-installed on macOS and Linux). Windows users: use WSL.

---

## Folder Structure

```
MemVault/
├── 00-inbox/                 # Quick-capture landing zone
├── 10-notes/                 # Daily notes, ideas, meetings, personal
│   ├── 10-daily/             # YYYY-MM-DD.md daily logs
│   ├── 20-ideas/             # Fleeting brainstorms
│   ├── 30-meetings/          # Meeting notes and decisions
│   └── 50-personal/         # Private — not indexed by agents
├── 12-mocs/                  # Maps of Content — wayfinding between domains
├── 20-knowledge/             # Curated, interlinked, evergreen knowledge
│   ├── ai/                   # AI providers, models, concepts, tools
│   ├── tech/                 # Platforms, frameworks, services
│   ├── business/             # Pricing, strategy, operations
│   └── concepts/             # Domain-agnostic concepts
├── 30-projects/       # Active project docs, specs, decisions
├── 40-library/               # Immutable sources — bookmarks, books, papers
│   ├── bookmarks/            # Archived web pages (domain-organized)
│   ├── books/                # Book notes
│   ├── movies/               # Film notes
│   └── papers/               # Research papers
├── 50-system/                # Agent infrastructure
│   ├── agents/               # Operating rules, checklists, boundaries
│   ├── conversations/        # Session artifacts (transient — distill within 48h)
│   ├── logs/                 # Operation logs
│   ├── scripts/              # Utility scripts
│   ├── skills/               # Extensible agent skill definitions
│   └── state/                # Runtime JSON state files
├── 90-archive/               # Completed projects, cold storage
├── _assets/                  # Shared media (images, PDFs, attachments)
├── _meta/                    # Vault metadata and docs
│   ├── docs/                 # Architecture, efficiency, troubleshooting
│   ├── claude-versions/      # Alternative CLAUDE.md variants
│   ├── superpowers/          # Dev plans
│   └── templates/            # Note templates (_template-*.md)
├── AGENTS.md                 # Session protocol — what to read, in order
├── CLAUDE.md                 # Operating schema — routing, workflows, conventions
├── SOUL.md                   # Agent identity, values, hard rules
├── USER.md                   # Your profile — name, timezone, preferences
├── MEMORY.md                 # Long-term index linking vault branches
└── home.md                   # Dashboard (Dataview-powered)
```

Each folder has a single purpose. The agent never creates new top-level directories — it routes content to the right branch.

## Key Files

| File | What it does |
|---|---|
| `SOUL.md` | Agent identity and hard rules — who the agent is |
| `CLAUDE.md` | Operating schema — how the vault works, where things go |
| `AGENTS.md` | Session protocol — what to read first, how to behave |
| `USER.md` | Your profile — name, timezone, role, preferences |
| `MEMORY.md` | Curated index linking all vault branches |
| `TOOLS.md` | Environment reference — SSH, API keys, web research |
| `VAULT_MANIFEST.json` | Machine-readable routing rules |

## CLAUDE.md Variants

Three versions of the operating schema — pick what fits:

| Version | File | Best for |
|---|---|---|
| Starter (default) | `CLAUDE.md` | New users — clean, minimal, everything you need |
| Full | `_meta/claude-versions/claude-a-full.md` | Power users — lint workflow and quality checklists |
| Template | `_meta/claude-versions/claude-c-template.md` | Used by `init.py` for personalized generation |

See `_meta/claude-versions/README.md` for how to swap versions.

## Naming Conventions

| Type | Pattern | Examples |
|---|---|---|
| Root identity files | `UPPERCASE.md` | `SOUL.md`, `USER.md`, `AGENTS.md` |
| Templates | `_template-{name}.md` | `_template-project.md`, `_template-daily-note.md` |
| Examples | `_example-{name}.md` | `_example-daily.md`, `_example-bookmark.md` |
| Everything else | `kebab-case.md` | `retrieval-augmented-generation.md`, `add-agent-framework.md` |
| Content folders | `NN-name/` | `10-notes/`, `20-knowledge/`, `30-projects/` |
| Infrastructure folders | `_name/` | `_meta/`, `_assets/` |
| Sub-folders | `kebab-case/` | `agents/`, `conversations/`, `skills/` |

## Further Reading

- [`_meta/docs/architecture.md`](_meta/docs/architecture.md) — how the vault works, layer model, quality standards
- [`_meta/docs/token-efficiency.md`](_meta/docs/token-efficiency.md) — conventions for lean AI context
- [`vault-architecture.md`](vault-architecture.md) — naming, tags, frontmatter, workflows

## License

MIT — use it, modify it, share it.