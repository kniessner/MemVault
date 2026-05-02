---
title: Agentic Research Knowledge Workflows
created: 2026-03-29
updated: 2026-03-29
tags:
  - ai/concept
  - ai
  - agents
  - knowledge-management
---

# Agentic Research Knowledge Workflows

This note describes how research-oriented agents should write into the vault without creating messy, overlapping knowledge artifacts.

## Core pattern

### 1. Retrieve

Gather live sources with a search or research system.

### 2. Capture

Write the first-pass evidence to a resource note under `10-notes/40-resources/` or to a project-local research note when the task is strictly project-bound.

### 3. Distill

Promote reusable knowledge into `20-knowledge/ai/`:

- providers -> `providers/`
- models -> `models/`
- tools -> `tools/`
- methods, patterns, architecture -> `concepts/`

### 4. Link

Connect the resource note, distilled note, and any project note with wikilinks.

### 5. Maintain

Update the distilled note when better evidence arrives. Do not create a fresh canonical note every time.

## Why this matters

- prevents source notes from pretending to be the canonical knowledge base
- keeps project context separate from reusable AI knowledge
- makes later agent retrieval more accurate
- supports clean branching for providers, models, tools, and concepts

## Anti-patterns

- dumping everything into one giant `MEMORY.md`
- storing the only useful insight in a session log
- creating a new root-level note for every research run
- mixing provider, model, and project facts into one undifferentiated file

## Related

- [[20-knowledge/ai/providers/perplexity]]
- [[20-knowledge/ai/providers/openrouter]]
- [[20-knowledge/ai/tools/obsidian]]
- [[20-knowledge/ai/models/perplexity-sonar-deep-research]]
- [[10-notes/40-resources/ai/2026-03-29-agentic-ai-source-pack]]

