---
name: obsidian
description: Canonical skill for working with this Obsidian vault. Use for note creation, note retrieval, links, properties, templates, Bases, attachments, and Obsidian app/CLI automation.
allowed-tools: Read, Write, Edit, Bash(rg *), Bash(find *), Bash(ls *), Bash(obsidian *), Bash(xdg-open *), Glob, Grep
argument-hint: [action] [path-or-query]
---

# Obsidian Skill

This is the canonical Obsidian skill for this vault.

Use it when the task involves:
- finding or opening notes
- creating notes or logs
- updating note properties/frontmatter
- adding internal links, embeds, or references
- using templates
- organizing information into the correct vault branch
- working with Bases or Obsidian automation

## Vault-First Rules

Before writing anything, follow the vault data architecture:
- daily capture: `10-notes/10-daily/`
- reusable knowledge: `20-knowledge/`
- active project material: `30-projects/<project>/`
- library collections: `40-library/`
- system state, logs, scripts, agent rules, skills: `50-system/`
- templates: `_meta/templates/`
- vault docs: `_meta/docs/`
- media assets: `_assets/`

Do not create ad-hoc top-level folders for notes.

## Current Vault Capabilities

This vault currently has these core plugins enabled:
- Properties
- Daily notes
- Templates
- Search
- Graph view
- Backlinks
- Canvas
- Bookmarks
- Bases

This vault currently has this community plugin installed:
- `obsidian-git`

Treat community plugins carefully. Do not recommend adding plugins unless the core feature set is insufficient.

## Research Ingestion Workflow

When external research should become durable vault knowledge, use this pipeline:

1. Gather grounded results from a search/research system.
2. Store the first-pass result in the correct vault branch:
   - `10-notes/40-resources/` for source-oriented research capture
   - project folder for project-specific research
   - `20-knowledge/` only after distillation
   - `20-knowledge/ai/` for reusable AI knowledge
3. Preserve query, date, model/provider, and source links in properties.
4. Distill conclusions into reusable notes instead of leaving a giant raw answer as the only artifact.

### Preferred research split

- quick grounded answer with citations -> Perplexity Sonar or equivalent research API
- multi-step, exhaustive report -> Perplexity Deep Research or equivalent
- raw search result harvesting -> search API without LLM post-processing

### Research note frontmatter

Use a structure like:

```yaml
---
title: Human Readable Title
created: 2026-03-29
updated: 2026-03-29
tags:
  - type/resource
  - status/draft
source_type: research
query: original user or research query
provider: perplexity
model: sonar-deep-research
related:
  - "[[Related Project or Note]]"
---
```

Then add:
- short summary
- key findings
- decision-relevant takeaways
- source list
- follow-up links into project or knowledge notes

### AI research routing

If the research is about:
- models -> `20-knowledge/ai/models/`
- providers or APIs -> `20-knowledge/ai/providers/`
- AI products, SDKs, tooling -> `20-knowledge/ai/tools/`
- prompting, agents, memory, evaluation, architecture -> `20-knowledge/ai/concepts/`

If the note is only relevant to one active project, keep the working copy in the project folder and link the reusable part into `20-knowledge/ai/`.

## Prefer Official Obsidian CLI

Prefer the official `obsidian` CLI when it is available, because it can:
- open daily notes
- create notes from templates
- search the vault
- read notes
- append/prepend content
- query Bases

Check availability:

```bash
command -v obsidian >/dev/null 2>&1 && obsidian version
```

If the CLI is not available, use filesystem tools for note edits and `obsidian://` URIs or `xdg-open` only to hand off to the app.

## Resolve the Vault Dynamically

Use this pattern:

```bash
VAULT_ROOT="${VAULT_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
VAULT_NAME="${OBSIDIAN_VAULT_NAME:-$(basename "$VAULT_ROOT")}"
```

Never hardcode a vault name or device path.

## Canonical Obsidian Workflows

### 1. Find the right note before creating one

Always search first to avoid duplicates:

```bash
rg -n --glob '*.md' 'search term' "$VAULT_ROOT"
```

If `obsidian` CLI is available:

```bash
obsidian search query="search term"
```

### 2. Use templates from `_meta/templates/`

Use existing templates whenever the note type matches:
- `_meta/templates/project-template.md`
- `_meta/templates/session-log-template.md`
- `_meta/templates/skill-template.md`
- `_meta/templates/note-basic.md`

If the CLI is available, prefer:

```bash
obsidian create path="10-notes/20-ideas/example.md" template="note-basic" open
```

If not, copy the template structure manually and adapt it.

### 3. Use Properties for structured metadata

For notes that need structure, use YAML properties at the top of the file.

Preferred fields in this vault:

```yaml
---
title: Human Readable Title
created: 2026-03-29
updated: 2026-03-29
tags:
  - status/draft
  - type/note
---
```

Notes:
- keep values atomic
- use lists for `tags`, `aliases`, related items
- quote internal links inside properties, for example `"[[Note Name]]"`

### 4. Prefer wikilinks for internal navigation

Use Obsidian-style links:

```markdown
[[Note Name]]
[[Note Name|Custom Label]]
[[Note Name#Heading]]
[[Note Name#^block-id]]
```

Use Markdown links mainly for external URLs.

### 5. Use embeds deliberately

Useful patterns:

```markdown
![[Note Name]]
![[Note Name#Heading]]
![[Note Name#^block-id]]
![[image.png|400]]
![[Document.pdf#page=3]]
```

Only embed when inline context is useful. Otherwise link.

### 6. Use Daily Notes for running capture

Daily working context belongs in `10-notes/10-daily/`.

If the CLI is available:

```bash
obsidian daily
obsidian daily:path
obsidian daily:append content="- [ ] Follow up on X"
```

If not, edit today's note directly in `10-notes/10-daily/`.

### 7. Use Bases for structured collections

When a folder of notes is effectively a database, prefer a `.base` file over ad-hoc index notes.

Good candidates in this vault:
- project overviews
- media or reading lists
- curated references
- status dashboards based on note properties

If the CLI is available:

```bash
obsidian bases
obsidian base:query path="path/to/file.base" format=json
```

### 8. Use CLI move/rename when possible

If you rename or move notes and the CLI is available, prefer the Obsidian app/CLI path so internal links can stay consistent with vault settings:

```bash
obsidian move path="old/path.md" to="new/path.md"
obsidian rename path="path/to/file.md" name="New Name"
```

### 9. Keep attachments intentional

Do not dump random files at the root.

Use:
- note-local or project-local attachment folders when context matters
- `_assets/` for vault-wide shared assets
- collection-specific folders inside `40-library/` when assets belong to a library branch

Reference local attachments with wikilinks.

### 10. Convert research into knowledge deliberately

Do not stop at "saved a researched answer".

After storing source-oriented research:
- move stable conclusions into `20-knowledge/` if reusable
- move reusable AI conclusions into `20-knowledge/ai/`
- move execution-specific findings into the relevant project folder
- add links both ways between source capture and distilled notes
- prefer one distilled note per coherent topic instead of many overlapping summaries

## Recommended Actions

### Open something in Obsidian

Prefer CLI:

```bash
obsidian open path="10-notes/10-daily/2026-03-29.md"
```

URI fallback:

```bash
xdg-open "obsidian://open?vault=$VAULT_NAME&file=10-notes/10-daily/2026-03-29.md"
```

### Search the vault

```bash
obsidian search query="search term"
```

Fallback:

```bash
rg -n --glob '*.md' 'search term' "$VAULT_ROOT"
```

### Create a note

```bash
obsidian create path="10-notes/20-ideas/example.md" content="# Example"
```

Or from template:

```bash
obsidian create path="30-projects/2026-example/README.md" template="project-template" open
```

### Read or append

```bash
obsidian read path="README.md"
obsidian append path="10-notes/10-daily/2026-03-29.md" content="- noted from session"
```

## What not to do

- do not hardcode a vault name
- do not assume `notes/`, `daily/`, `configs/`, or other legacy folders exist
- do not recommend new plugins before checking whether a core feature already solves it
- do not create duplicate notes when an existing canonical note should be updated
- do not use Obsidian Sync, iCloud, or Nextcloud as an assumption for this vault
- do not paste a full research transcript into `MEMORY.md`
- do not store raw research output at the vault root

## Best-Practice Output Style

When helping with Obsidian tasks in this vault:
- name the canonical folder you chose
- explain whether you created, updated, linked, or embedded
- mention template or property changes explicitly
- prefer small, high-signal note structures over giant generic boilerplate