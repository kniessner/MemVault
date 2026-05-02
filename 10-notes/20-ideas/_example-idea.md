---
title: "Idea: Automated Knowledge Graph from Meeting Notes"
description: "Use AI to extract entities and links from meetings into 20-knowledge"
created: 2026-01-01
tags:
  - status/idea
  - type/note
  - ai
---

Meeting notes contain dense signal — decisions, people, projects, dependencies — but that signal gets buried in prose. An AI agent could parse each meeting note on ingest, extract named entities (projects, people, tools, decisions), and automatically create or update wiki pages in `20-knowledge/`. Links between pages would surface organically rather than requiring manual curation. Over time this would turn raw meeting logs into a queryable knowledge graph with minimal human overhead. The main challenge is avoiding noise: not every mention warrants a new page, so the agent needs a confidence threshold and a Human review step.

## Related

- [[retrieval-augmented-generation]]
- [[agents]]
- [[10-notes/30-meetings/_example-meeting|Example Meeting Note]]
