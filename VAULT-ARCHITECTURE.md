# Vault Architecture

*An intelligent, human-centered data management system for MemVault*

> **Concept:** This vault implements the [LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — a compounding knowledge system where AI maintains interlinked markdown files that get richer with every source added.

Primary agent operating rules: `50-system/AGENTS/vault-operating-system.md`

---

## Core Principles

1. **The 3-Click Rule** — Any item should be findable within 3 clicks
2. **Single Source of Truth** — One place per type of information
3. **Convention over Configuration** — Clear rules reduce decision fatigue
4. **Archive, Don't Delete** — Old things go to `archive/`, never purged
5. **Obsidian-Native** — Works seamlessly with Obsidian, Dataview, Tasks
6. **Sync method is your choice** — Syncthing, iCloud, Dropbox, git, or manual

---

## Folder Structure

```
MemVault/
│
├── 00-inbox/                 # Temporary landing zone
│   └── README.md             # "Process me first" reminder
│
├── 10-notes/                 # Core personal notes
│   ├── 10-daily/             # Daily logs
│   ├── 20-ideas/             # Fleeting notes, thoughts
│   ├── 30-projects/          # Project support docs
│   ├── 40-resources/         # Bookmarks, articles, references
│   └── 50-personal/          # Private: health, finance, etc.
│
├── 20-knowledge/             # Curated knowledge bases
│   ├── ai/                   # AI provider/model docs
│   ├── tech/                 # Technical knowledge
│   ├── business/             # Business/marketing
│   └── concepts/             # Concepts, frameworks, methods
│
├── 30-projects/       # Active work
│   ├── YYYY-project-name/    # Naming: YEAR-descriptive-name
│   └── _template/            # Project starter template
│
├── 40-library/               # Static reference materials
│   ├── books/                # Book notes
│   ├── courses/              # Course materials
│   ├── papers/               # Research papers
│   ├── datasets/             # Data files
│   └── bookmarks/            # Archived web pages
│
├── 50-system/                # System & configuration
│   ├── AGENTS/               # Agent rules and checklists
│   ├── conversations/        # Session artifacts
│   ├── logs/                 # Operation logs
│   ├── scripts/              # Utility scripts
│   ├── skills/               # Agent skills
│   └── state/                # Runtime state files
│
├── 90-archive/               # Cold storage
│   ├── YYYY/                 # Archived by year
│   └── _graveyard/           # Deleted concepts (soft delete)
│
├── _assets/                # Media assets (images, PDFs, attachments)
│
├── _meta/                    # Metadata & docs
│   ├── tags.md               # Controlled vocabulary
│   ├── templates/            # Note templates
│   ├── docs/                 # Vault documentation
│   ├── claude-versions/      # CLAUDE.md variants
│   ├── superpowers/          # Dev plans
│   └── checklists/           # Process checklists
│
├── 50-system/                # System & configuration
│   ├── AGENTS/               # Agent rules and checklists
│   ├── conversations/        # Session artifacts
│   ├── logs/                 # Operation logs
│   ├── scripts/              # Utility scripts
│   ├── skills/               # Agent skills
│   └── state/                # Runtime state files
├── README.md                 # Entry point for humans
└── VAULT-ARCHITECTURE.md     # This file
```

---

## Naming Conventions

### Files
```
YYYY-MM-DD-descriptive-slug.md     # Daily notes
project-name-status-note.md        # Project docs (kebab-case)
Company-Name-Provider.md           # Knowledge base (Pascal-kebab)
README.md                          # Folder index (always UPPER)
_template.md                       # Hidden templates (underscore prefix)
```

### Folders
```
XX-category-name/                  # Numbered for sorting
YYYY-project-name/                 # Projects: year prefix
_hide-me/                          # Hidden folders (underscore)
```

### Media Attachments
```
YYYYMMDD-HHMMSS-context.ext        # Timestamped assets
project-name-diagram.png           # Project assets
```

---

## Tag Taxonomy (Controlled Vocabulary)

Use these consistently for Dataview queries:

### Status Tags
- `#status/idea` — Raw thought
- `#status/draft` — Work in progress
- `#status/review` — Needs review
- `#status/done` — Complete
- `#status/archived` — Moved to archive

### Type Tags
- `#type/note` — General note
- `#type/project` — Project documentation
- `#type/resource` — External reference
- `#type/person` — People/contacts
- `#type/meeting` — Meeting notes

### Priority Tags
- `#p0-critical` — Drop everything
- `#p1-high` — Do soon
- `#p2-medium` — Normal priority
- `#p3-low` — Backlog

### Domain Tags
- `#ai` `#tech` `#business` `#personal` `#health` `#finance`

### Time Tags
- `#now` — Active this week
- `#next` — Coming up
- `#later` — Eventually
- `#someday` — Maybe never

---

## Frontmatter Standard

Every note should have this YAML frontmatter:

```yaml
---
title: "Human-Readable Title"
description: "One-line summary of this note"
date-created: YYYY-MM-DD
date-modified: YYYY-MM-DD
tags: [status/draft, type/note, ai]
source: "URL or book reference if applicable"
related: [[Link to related note]]
---
```

---

## Workflows

### Daily Inbox Processing (Do This Daily)

1. Open `00-inbox/`
2. For each item:
   - **Trash?** → Move to `90-archive/_graveyard/`
   - **Quick task?** → Add to task manager, delete file
   - **Reference?** → Move to `10-notes/20-ideas/` or `40-resources/`
   - **Project-related?** → Move to `30-projects/PROJECT/`
   - **Knowledge?** → Move to `20-knowledge/` with proper structure
3. Inbox should be **empty** after processing

### Weekly Review (Every Sunday)

1. Review `10-notes/10-daily/` — summarize into weekly note
2. Check `30-projects/` — update status, archive completed
3. Update `MEMORY.md` with weekly insights

### Monthly Archive

1. Move completed projects to `90-archive/YYYY/`
2. Archive daily notes older than 90 days
3. Review tags for consistency

---

## Search Strategy

### Obsidian Quick Access

**Active Projects Dashboard:**
```dataview
TABLE status, priority, deadline
FROM "30-projects"
WHERE status != "archived"
SORT priority ASC, deadline ASC
```

**Recent Notes:**
```dataview
LIST
FROM !"90-archive" AND !"_meta"
SORT date-modified DESC
LIMIT 20
```

**Hot Items (tag #now):**
```dataview
TASK
FROM #now
WHERE !completed
```

---

## Quick Start Checklist

- [ ] Create folder structure
- [ ] Run `python3 init.py` to configure identity files
- [ ] Set up `_meta/templates/` with note templates
- [ ] Create dashboard notes (Active Projects, Recent, Hot)
- [ ] Process inbox to zero
- [ ] Configure Obsidian hotkeys

---

## Success Metrics

You know the system works when:

- Inbox stays near zero
- You find things in under 10 seconds
- No duplicate information exists
- Archive grows, deletions are rare
- You actually use the dashboard notes
