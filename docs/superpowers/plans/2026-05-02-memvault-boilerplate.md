# MemVault Boilerplate — Phase 1: Architecture Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a shareable, init-script-driven Obsidian vault boilerplate that lets non-technical users stand up an AI-agent-ready knowledge vault in under 5 minutes.

**Architecture:** A Python init script collects identity variables, scaffolds a canonical folder tree, and writes personalized agent configuration files (SOUL.md, USER.md, AGENTS.md, CLAUDE.md, VAULT_MANIFEST.json). The vault structure is derived from the VaultOS reference architecture with all personal data stripped and replaced with typed template variables.

**Tech Stack:** Python 3 (stdlib only), Markdown, YAML frontmatter, JSON, Obsidian (GUI), optional agent frameworks (Claude Code / Codex / opencode)

---

## 1. Architecture Extraction

### What to Port from VaultOS

**Folder structure** (all 12 top-level branches):
- `00-inbox/` through `90-archive/` numbered scheme
- `_meta/` for templates and tag taxonomy
- `assets/`, `skills/` as optional support directories

**Identity layer files** (templated, not copied verbatim):
- `SOUL.md` — agent values and hard vault rules
- `USER.md` — human profile
- `AGENTS.md` — session checklist and workspace rules
- `CLAUDE.md` — vault operating schema (routing, ingest, query workflows)
- `VAULT-ARCHITECTURE.md` — naming conventions, tag taxonomy, workflows
- `VAULT_MANIFEST.json` — canonical routing rules (machine-readable)
- `IDENTITY.md` — agent persona name and tone

**System layer** (generalized):
- `50-system/AGENTS/workflow.md` — every-session checklist
- `50-system/AGENTS/data-architecture.md` — canonical storage contract
- `50-system/AGENTS/security.md` — safety boundaries
- `_meta/templates/` — daily note, project, inbox capture, knowledge page, meeting note
- `_meta/tags.md` — controlled tag vocabulary
- `00-inbox/_process.md` — inbox triage ritual

**Conventions** (encoded into every example file):
- YAML frontmatter schema (title, created, tags minimum)
- kebab-case file naming
- Wikilink style `[[filename]]`
- Numbered folder prefix scheme
- Tag taxonomy (`status/*`, `type/*`, `#p0`–`#p3`)
- Atomic knowledge page format
- Append-only log pattern

### What Must NOT Ship

| File / Content | Reason |
|---|---|
| `USER.md` personal fields ("Commander", timezone) | Personal identity |
| `IDENTITY.md` persona name "Kit the Cat" | Personal agent persona |
| `TOOLS.md` SSH hosts, IPs, API keys | Infrastructure secrets |
| `.env` with real tokens | Credentials |
| `.obsidian/workspace.json` | User-specific workspace state |
| `MEMORY.md` with real project references | Personal content |
| `Home.md` with knssnr references | Personal dashboard |
| Real project folders in `30-projects/` | Proprietary work |
| `10-notes/10-daily/` actual daily notes | Personal logs |
| `40-library/bookmarks/` real bookmarks | Personal content |
| `50-system/openclaw/`, `50-system/hermes/` | Personal agent configs |
| File paths containing `darius.kniessner`, `knssnr` | Identifying info |
| References to `shore.com`, `knssnr.com` | Personal domains |

**Note on MemVault's existing files:** MemVault already has SOUL.md, USER.md, AGENTS.md, TOOLS.md, VAULT-ARCHITECTURE.md, IDENTITY.md, HOME.md, MEMORY.md, README.md with personal content from VaultOS. These will be **replaced entirely** by the boilerplate (not preserved as references). See Open Questions §1 for decision confirmation.

---

## 2. Target User Profile

**Assumed environment:**
- macOS 13+ (primary), Ubuntu 22+ (supported), Windows (deferred)
- Obsidian installed as a GUI app (free tier)
- Has opened Terminal at least once

**Technical floor:**
- Can copy-paste a command into Terminal and press Enter
- Can answer plain-English questions in a prompt
- Has or can obtain at least one LLM API key

**Technical ceiling (what we do NOT assume):**
- Cannot compile code or install Node.js manually
- Cannot configure YAML files by hand
- Cannot understand JSON routing manifests
- Will not debug shell errors

**The init script must:**
- Require no prerequisites beyond Python 3 (pre-installed on macOS/Linux)
- Never show a stack trace to the user (catch all errors, print plain English)
- Complete in under 3 minutes including scaffolding
- Never require the user to edit any file by hand to get a working vault

**The example files must:**
- Show what a finished entry looks like, not just the template
- Be short enough to read in 30 seconds
- Not assume the reader knows what frontmatter or wikilinks are (docs cover that)

---

## 3. Supported Agent Frameworks

openclaw is explicitly excluded — it is a personal tool without public install documentation.

### 3a. Claude Code (Primary Recommendation)

| | |
|---|---|
| **Install method** | `npm install -g @anthropic-ai/claude-code` |
| **Prereqs** | Node.js 18+, Anthropic API key |
| **Local vs API** | API (Anthropic) |
| **Vault integration** | Reads `CLAUDE.md` natively from vault root; supports `AGENTS.md` via instructions |
| **Conflicts** | None |
| **Rationale** | Best-in-class vault integration; `CLAUDE.md` is a first-class feature of Claude Code |

Init script action: Write `CLAUDE.md` with routing rules + vault schema; optionally run `npm install -g @anthropic-ai/claude-code` if user confirms.

### 3b. Codex (OpenAI)

| | |
|---|---|
| **Install method** | `npm install -g @openai/codex` |
| **Prereqs** | Node.js 18+, OpenAI API key |
| **Local vs API** | API (OpenAI) |
| **Vault integration** | Reads `AGENTS.md` by convention; can be pointed at vault root |
| **Conflicts** | None |
| **Rationale** | Large existing user base; straightforward CLI; broadens provider choice |

Init script action: Write Codex-specific section in `AGENTS.md`; optionally install.

### 3c. opencode (Optional / Advanced)

| | |
|---|---|
| **Install method** | `npm install -g opencode-ai` or system package |
| **Prereqs** | Any LLM API key (multi-provider) |
| **Local vs API** | Both (local models via Ollama, cloud via API) |
| **Vault integration** | Reads `AGENTS.md`; configurable workspace root; supports multiple providers |
| **Conflicts** | None |
| **Rationale** | Provider flexibility; supports users who don't want Anthropic or OpenAI |

Init script action: Write opencode config section; optionally install.

### 3d. Deferred

| Framework | Reason |
|---|---|
| **Hermes AI** | No public install documentation; unclear distribution channel |
| **openclaw** | Personal/internal tool; excluded by user request |

### Selection UX

The init script presents a numbered menu with no pre-selected default:

```
Which AI agent framework(s) do you already use or want to set up?
  1) Claude Code  (Anthropic API)
  2) Codex        (OpenAI API)
  3) opencode     (multi-provider)
  4) All of the above
  5) I'll set this up later

Enter your choice [5]:
```

If the user is already running an agent: they pick the matching option, and the init script writes the appropriate config without re-installing.

---

## 4. Identity Layer Schema

### Variables Collected

| Variable | Prompt | Default | Validates |
|---|---|---|---|
| `USER_NAME` | "Your name?" | `Human` | non-empty string |
| `USER_PRONOUNS` | "Your pronouns? (he/she/they/skip)" | `skip` | one of: he/she/they/skip |
| `USER_TIMEZONE` | "Your timezone?" | auto-detected | valid zoneinfo key |
| `USER_ROLE` | "Your primary role? (e.g. researcher, developer, writer)" | `Knowledge Worker` | non-empty string |
| `USER_LANGUAGE` | "Primary language?" | `English` | non-empty string |
| `AGENT_NAME` | "Name your AI assistant?" | `Sage` | 1-20 chars, no spaces |
| `AGENT_TONE` | "Preferred AI tone? (technical/friendly/balanced)" | `balanced` | one of 3 options |
| `VAULT_NAME` | "Name for your vault?" | `MemVault` | alphanumeric + hyphens, 3-50 chars |
| `ANTHROPIC_API_KEY` | "Anthropic API key? (paste or Enter to skip)" | `""` | starts with `sk-ant-` or empty |
| `OPENAI_API_KEY` | "OpenAI API key? (paste or Enter to skip)" | `""` | starts with `sk-` or empty |

### Files Populated

| File | Variables Used |
|---|---|
| `SOUL.md` | `AGENT_NAME`, `AGENT_TONE`, `USER_NAME`, `VAULT_NAME` |
| `USER.md` | `USER_NAME`, `USER_PRONOUNS`, `USER_TIMEZONE`, `USER_ROLE`, `USER_LANGUAGE` |
| `AGENTS.md` | `AGENT_NAME`, `VAULT_NAME`, `PREFERRED_FRAMEWORKS` |
| `IDENTITY.md` | `AGENT_NAME`, `AGENT_TONE` |
| `CLAUDE.md` | `VAULT_NAME` (static schema, vault name substituted) |
| `HOME.md` | `VAULT_NAME`, `USER_NAME` |
| `MEMORY.md` | `VAULT_NAME`, `USER_NAME` (index scaffold only) |
| `TOOLS.md` | `VAULT_NAME` (example structure, no real credentials) |
| `VAULT_MANIFEST.json` | `VAULT_NAME` |
| `.env` | `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `USER_TIMEZONE`, `VAULT_NAME` |

Keys are written to `.env` only — never embedded in markdown files.

---

## 5. Folder Architecture

```
MemVault/
├── 00-inbox/                   # Raw capture: drafts, links, unprocessed notes
│   ├── _process.md             # Triage ritual and decision tree
│   └── _template-capture.md   # Quick capture template
│
├── 10-notes/                   # Working memory: ephemeral, dated, personal
│   ├── 10-daily/               # YYYY-MM-DD.md daily logs
│   ├── 20-ideas/               # Fleeting brainstorms
│   ├── 30-meetings/            # Meeting notes
│   └── 50-personal/            # Private — not indexed by agents
│
├── 12-mocs/                    # Maps of Content: wayfinding between domains
│   └── _example-moc.md         # Example: AI landscape overview
│
├── 20-knowledge/               # Evergreen, atomic, interlinked knowledge pages
│   ├── ai/
│   │   ├── concepts/           # RAG, agents, prompting patterns
│   │   ├── models/             # Individual model pages
│   │   ├── providers/          # Anthropic, OpenAI, etc.
│   │   └── tools/              # LangChain, llama.cpp, etc.
│   ├── tech/                   # Platforms, frameworks, services
│   ├── business/               # Pricing models, strategy, ops
│   └── concepts/               # Domain-agnostic concepts
│
├── 30-projects/         # Living project docs: specs, decisions, logs
│   ├── _template/              # Copy this to start a new project
│   │   ├── README.md           # Project overview
│   │   ├── decisions.md        # Decision log (append-only)
│   │   └── log.md              # Progress log (append-only)
│   └── index.md                # Projects dashboard
│
├── 40-library/                 # External reference material
│   ├── bookmarks/              # Saved web pages
│   ├── books/                  # Book notes and reviews
│   ├── movies/                 # Film notes
│   └── index.md                # Library dashboard
│
├── 50-system/                  # Agent operating rules, state, scripts
│   ├── AGENTS/
│   │   ├── workflow.md         # Every-session checklist
│   │   ├── data-architecture.md # Canonical storage contract
│   │   └── security.md         # Safety rules and boundaries
│   ├── conversations/          # AI session artifacts (transient — distill within 48h)
│   │   └── index.md
│   ├── logs/                   # Operation logs
│   ├── state/                  # Runtime JSON state files
│   └── scripts/                # Utility scripts
│
├── 90-archive/                 # Cold storage: completed projects, old material
│   └── index.md
│
├── _meta/                      # Vault metadata and templates
│   ├── templates/
│   │   ├── daily-note.md       # Daily log template
│   │   ├── project.md          # Project overview template
│   │   ├── inbox-capture.md    # Quick capture template
│   │   ├── knowledge-page.md   # Evergreen knowledge template
│   │   └── meeting-note.md     # Meeting note template
│   └── tags.md                 # Controlled tag vocabulary
│
├── assets/                     # Shared images, PDFs, media
├── docs/                       # Boilerplate documentation (for humans)
│   ├── architecture.md         # How the vault works
│   ├── token-efficiency.md     # Conventions for lean AI context
│   ├── add-agent-framework.md  # How to add a new agent
│   └── troubleshooting.md      # Common problems and fixes
│
├── SOUL.md                     # Agent identity and values
├── USER.md                     # Human profile
├── AGENTS.md                   # Agent workspace rules and session checklist
├── CLAUDE.md                   # Vault operating schema (routing, workflows)
├── VAULT-ARCHITECTURE.md       # Naming conventions, tag taxonomy, principles
├── VAULT_MANIFEST.json         # Machine-readable routing rules
├── IDENTITY.md                 # Agent persona (name, tone)
├── HOME.md                     # Vault dashboard / entry point
├── MEMORY.md                   # Curated index and shortcuts
├── README.md                   # Human quickstart guide
├── TOOLS.md                    # Environment reference template
├── .env.example                # Environment variable template
├── .env                        # Created by init script (gitignored)
└── .gitignore                  # Ignores .env, .obsidian/workspace.json
```

### Example Entries (Token-Efficient Style)

**`00-inbox/_template-capture.md`**
```markdown
---
title: ""
created: YYYY-MM-DD
tags: [status/draft, type/note, "#agent-review"]
source: ""
---

## Raw Input

<!-- Paste content here -->

## Classify

- [ ] Trash
- [ ] Quick task (do it, delete this)
- [ ] Idea → `10-notes/20-ideas/`
- [ ] Project note → `30-projects/YYYY-name/`
- [ ] Evergreen knowledge → `20-knowledge/`
- [ ] Bookmark → `40-library/bookmarks/`
```

**`20-knowledge/ai/concepts/retrieval-augmented-generation.md`**
```markdown
---
title: "Retrieval-Augmented Generation (RAG)"
description: "Pattern for grounding LLM outputs in a private document corpus"
created: 2026-01-01
tags: [status/active, type/note, ai]
related: ["[[vector-databases]]", "[[embedding-models]]"]
---

## Definition

RAG retrieves relevant documents at query time and injects them into the LLM prompt, reducing hallucination and enabling knowledge cutoff bypass.

## Key Components

| Component | Role |
|---|---|
| Chunker | Splits docs into retrievable units |
| Embedder | Converts chunks to vector space |
| Vector DB | Stores and searches embeddings |
| Retriever | Fetches top-k relevant chunks |
| Generator | LLM that answers with retrieved context |

## When to Use

- Private knowledge not in training data
- Freshness required (news, docs, prices)
- Source attribution needed

## Related

[[vector-databases]] · [[embedding-models]] · [[llm-providers]]
```

**`30-projects/_template/README.md`**
```markdown
---
title: "Project Name"
description: "One-line summary"
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: active
tags: [status/active, type/project, "#p1-high"]
---

## Status

**Current:** What is happening right now  
**Priority:** p1-high  
**Deadline:** YYYY-MM-DD

## Goals

1. Primary goal
2. Secondary goal

## Notes

### YYYY-MM-DD — First entry

What happened.

## Decisions

| Date | Decision | Rationale |
|---|---|---|
| YYYY-MM-DD | Chose X over Y | Reason |

## Related

[[knowledge-page]] · [[other-project]]
```

**`_meta/templates/daily-note.md`**
```markdown
---
title: "YYYY-MM-DD"
created: YYYY-MM-DD
tags: [status/draft, type/daily]
focus: ""
---

## Focus

- Main priority today

## Log

- 09:00 Started X
- 10:30 Finished Y, blocked by Z

## Decisions

-

## Next Steps

- [ ] Action item
```

---

## 6. Token Efficiency Conventions

These are the enforceable rules every file in the vault must follow. They are documented in `docs/token-efficiency.md` and enforced by example in every template.

### File Naming

- `kebab-case-descriptive.md` — no spaces, no CamelCase, no underscores
- No date prefix unless the file is time-bound (daily notes, session logs)
- Name encodes the content: `rag.md` is wrong; `retrieval-augmented-generation.md` is right
- Template files prefix with `_` (underscore = hidden/meta): `_template-project.md`

### Frontmatter

- **Required:** `title`, `created`, `tags`
- **Recommended:** `description` (one sentence, ≤120 chars), `updated`, `related`
- **Forbidden in frontmatter:** multi-sentence descriptions, prose summaries, author fields, version fields
- `description` is a single indexable sentence — it is what the agent reads when scanning indices

### File Size Limits (enforced by convention, not code)

| File type | Soft limit | Hard limit |
|---|---|---|
| Agent config (SOUL.md, USER.md, AGENTS.md) | 200 lines | 500 lines |
| CLAUDE.md (operating schema) | 300 lines | 600 lines |
| Knowledge page | 150 lines | 400 lines |
| Daily note | no limit | — |
| Session artifact | no limit | — |
| Index file | 100 lines | 200 lines |

### Linking

- Always `[[filename]]` not a full path or URL to internal files
- `[[filename|Display Text]]` for human-readable aliases
- Link liberally in body text — connections compound value
- One "Related" line at the bottom of knowledge pages: `[[a]] · [[b]] · [[c]]`

### Content Rules

- No "Welcome to MemVault!" preamble in agent-readable files
- No redundant headings — the frontmatter `title` is the document title; don't repeat it as H1
- Tables over prose for comparisons, feature lists, decision matrices
- Status communicated via tag (`#status/active`) not a prose section
- Code blocks must have a language tag: ` ```python ` not ` ``` `

### What NOT to Put in Agent-Readable Files

- Lengthy onboarding explanations → those go in `docs/` (human-facing)
- Multiple examples of the same pattern (one is enough)
- Deprecated content without `#status/archived` tag
- Infrastructure details (SSH hosts, IPs, port numbers)
- API keys, tokens, secrets — always `.env` only
- Meeting transcripts — distill to decisions + action items only

### Context Window Strategy

- SOUL.md + USER.md + AGENTS.md combined ≤ 4K tokens (agent reads all three every session)
- CLAUDE.md is operational, not instructional — no onboarding narrative
- `VAULT_MANIFEST.json` is compact JSON, no comments
- Index files are tables of one-line summaries, never full content replicas
- Session artifacts in `50-system/conversations/` are transient — distill to `20-knowledge/` within 48h, then delete

---

## 7. Init Script UX Flow

### Language Recommendation: Python 3 (stdlib only)

**Rationale:**
- Pre-installed on macOS 12+ and Ubuntu 20+: zero install friction
- No `npm`, `pip install`, or `brew` required by the user
- `pathlib`, `string.Template`, `json`, `zoneinfo` cover all needs
- Readable error messages without stack traces
- Idempotency is easy to implement cleanly

Bash alternative was considered and rejected: harder to read for contributors, no built-in template substitution, error handling is messier.

### Invocation

```bash
python3 init.py              # Standard run
python3 init.py --dry-run    # Show what would happen, write nothing
python3 init.py --reconfigure  # Re-run identity questions, skip scaffolding
```

### Step-by-Step Flow

```
[1] Banner
    Print: "MemVault — AI-Agent Knowledge Vault Setup (v1.0)"

[2] Detect OS
    - macOS → proceed
    - Linux → proceed
    - Windows → print "Windows support coming soon. Exiting." → exit 0

[3] Check Python version
    - < 3.8 → print plain-English error + link to python.org → exit 1

[4] Idempotency check
    If SOUL.md exists AND contains non-template content (i.e., not "{{AGENT_NAME}}"):
      Print: "Vault already configured. What would you like to do?"
      1) Update identity files (re-run questions)
      2) Re-scaffold missing files only (safe, won't overwrite)
      3) Full reinitialize (overwrites identity files — YOUR NOTES ARE SAFE)
      4) Exit
      [Choice required, no default]

[5] Identity questions (with defaults in brackets)
    a. "Your name [Human]: "
    b. "Your pronouns — he/she/they/skip [skip]: "
    c. "Your timezone [auto-detected]: " (auto-detect via: date +%Z or /etc/timezone)
    d. "Your role, e.g. researcher, developer, writer [Knowledge Worker]: "
    e. "Primary language [English]: "
    f. "Name your AI assistant [Sage]: "
    g. "AI tone — technical/friendly/balanced [balanced]: "
    h. "Name this vault [MemVault]: "

[6] Agent framework selection
    Print: "Which AI agent framework do you use or want to set up?"
    Print: "(Already running one? Pick it — the script will configure without reinstalling.)"
      1) Claude Code  (Anthropic API, reads CLAUDE.md natively)
      2) Codex        (OpenAI API)
      3) opencode     (multi-provider: Anthropic, OpenAI, local models)
      4) All of the above
      5) Set up later
    [Default: 5]

[7] API key collection (only for chosen frameworks)
    For each framework selected:
      "Anthropic API key — paste or Enter to skip: "  (Claude Code / opencode)
      "OpenAI API key — paste or Enter to skip: "     (Codex / opencode)
    Keys validated by prefix (sk-ant-... / sk-...) but not by API call.
    Keys stored ONLY in .env. Message: "Key saved to .env (never committed to git)."

[8] Dry-run preview (always shown before writing)
    Print a file tree of what will be created or overwritten.
    If --dry-run flag: stop here, exit 0.

[9] Confirmation
    "Create vault at [path]? (Y/n): " [Default: Y]
    On N: exit 0

[10] Scaffolding (in order)
    a. Create all directories (mkdir -p, safe to repeat)
    b. Write identity files from templates (SOUL.md, USER.md, AGENTS.md, IDENTITY.md,
       CLAUDE.md, VAULT-ARCHITECTURE.md, VAULT_MANIFEST.json, HOME.md, MEMORY.md,
       README.md, TOOLS.md)
    c. Write all folder example files and templates
    d. Write .env (append new keys, never overwrite existing keys)
    e. Write .gitignore
    f. If agent frameworks selected AND user confirmed install:
       - Check if framework already installed (which claude-code, which codex, etc.)
       - If not installed: run npm install -g ... with live output
       - If already installed: skip with message "Claude Code already installed ✓"

[11] Success message
    "✓ Vault ready at [path]"
    "Next: Open [path] in Obsidian"
    "Then: Run 'claude' (or 'codex') from inside the vault directory"
    "Docs: [path]/docs/"
```

### Idempotency Contract

| Action | Safe to repeat? | Behavior on re-run |
|---|---|---|
| Create directories | Yes | `mkdir -p` is a no-op if exists |
| Write identity files | No (with confirmation) | Overwrites only after explicit user choice |
| Write example files | Yes | Skip if file exists (never overwrite user content) |
| Write .env | Partial | Append missing keys; never overwrite existing values |
| Write .gitignore | Yes | Merge new entries, never remove existing |
| npm install frameworks | Yes | Skip if already installed |

### Error Handling

All exceptions caught at top level. User sees:

```
Error: Python 3.8 or higher is required. You have Python 3.7.
Fix: Download Python from https://python.org/downloads
```

Never shows a traceback to the user unless `--debug` flag is passed.

---

## 8. Open Questions

**Require answers before Phase 2 begins.**

1. **MemVault existing files** — MemVault already contains SOUL.md, USER.md, AGENTS.md, TOOLS.md, VAULT-ARCHITECTURE.md, IDENTITY.md, HOME.md, MEMORY.md, README.md with personal VaultOS content (Commander, knssnr paths, etc.). Should I:
   - **A) Replace entirely** with clean boilerplate versions (recommended — cleanest result)
   - **B) Strip and template** in-place (preserves structure but risky with personal data)
   - **C) Archive to `reference/`** and build fresh alongside them

2. **Obsidian plugin config** — Should the boilerplate include a `.obsidian/` config with Dataview + Templater pre-enabled? This improves the dynamic index experience (DataviewJS tables in `30-projects/index.md`, etc.) but requires those plugins to be installed. Options:
   - **A) Include `.obsidian/` with recommended plugin config** (better UX, adds install step)
   - **B) No `.obsidian/` config** — purely static markdown, works out-of-box (recommended for non-technical users)
   - **C) Include `.obsidian/` but make DataviewJS optional** (static fallback index)

3. **CLAUDE.md scope** — The boilerplate's CLAUDE.md should guide agents operating in the new vault. Options:
   - **A) Generic copy of VaultOS CLAUDE.md** with personal details stripped (fast to build, well-tested)
   - **B) Lighter "starter" version** with simplified routing (easier for new users to understand)
   - **C) Full template filled by init script** (VAULT_NAME substituted, framework-specific sections added)

4. **Vault works offline?** — Should the init script require at least one API key to proceed, or should it scaffold everything and let the user add keys later? Options:
   - **A) Require at least one key** — ensures the vault is usable immediately
   - **B) Keys are optional** — scaffold fully, user adds keys when ready (recommended — lower friction)

5. **Git integration** — Should init.py run `git init` and create an initial commit? Options:
   - **A) Yes** — makes the vault git-trackable from day one (good practice, but unfamiliar to non-technical users)
   - **B) No** — omit git entirely, user can add later (recommended for non-technical north star)
   - **C) Optional** — ask "Set up git version history? (Y/n)"

6. **Hermes AI** — Include a placeholder/stub for Hermes AI setup in the agent selection menu (with a "coming soon" note), or omit it entirely?

7. **Windows deferral** — Is a hard exit with a plain-English message acceptable for Windows, or should we attempt a partial PowerShell scaffold?

---

*Plan authored: 2026-05-02. Awaiting approval before Phase 2 (build).*
