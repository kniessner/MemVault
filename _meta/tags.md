# Tag Taxonomy

## Status

| Tag | Meaning |
|---|---|
| #status/idea | Early concept, not validated |
| #status/draft | In progress, not ready to use |
| #status/active | Current, being used |
| #status/done | Completed |
| #status/archived | No longer active, kept for reference |

## Type

| Tag | Meaning |
|---|---|
| #type/note | Evergreen knowledge page |
| #type/index | Index or MOC page |
| #type/project | Project readme or doc |
| #type/log | Append-only log |
| #type/daily | Daily note |
| #type/meeting | Meeting notes |
| #type/resource | Bookmark, paper, or reference |

## Priority

| Tag | Meaning |
|---|---|
| #p0-critical | Must address immediately |
| #p1-high | Important, near-term |
| #p2-medium | Normal queue |
| #p3-low | Nice to have |

## Domain

| Tag | Meaning |
|---|---|
| #ai | Artificial intelligence, LLMs, agents |
| #tech | Software, infrastructure, platforms |
| #business | Strategy, operations, revenue |
| #personal | Private — not shared with agents |

## Special

| Tag | Meaning |
|---|---|
| #agent-review | Created by AI agent, awaiting human review |

## Anti-patterns

Avoid these tagging habits:

- **Too many unique tags** — if a tag appears on one note only, it's not a tag, it's a title word
- **Synonyms for the same concept** — pick one: `#ai` not both `#ai` and `#artificial-intelligence`
- **Spaces in tags** — Obsidian supports them but they break portability; use `/` or `-` instead
- **Single-use tags** — tags with one note provide no navigational value; use frontmatter fields instead
- **Status as content** — `#wip` and `#draft` mean the same thing; standardise on `#status/draft`
