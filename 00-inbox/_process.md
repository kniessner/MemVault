# Inbox Triage Ritual

Process the inbox before starting new work.

---

## Quick Scan

Check item age before triaging. Items older than 7 days are a red flag — prioritize clearing them.

## Triage Decision Tree

| Item type | Destination |
|---|---|
| Actionable task (<5 min) | Do it now, delete this |
| Raw idea | `10-notes/20-ideas/` |
| Meeting notes | `10-notes/30-meetings/` |
| Durable knowledge | `20-knowledge/` |
| External reference/URL | `40-library/bookmarks/` |
| Active project note | `30-projects/YYYY-name/` |
| AI session artifact | `50-system/conversations/` |
| Unsure | Leave with `#status/draft`, revisit tomorrow |

## Process Checklist

- [ ] Read item
- [ ] Determine destination (see table above)
- [ ] Add frontmatter (title, created, tags minimum)
- [ ] Move to correct folder
- [ ] Update relevant index file
- [ ] Delete this inbox copy

## Age Escalation

| Age | Action |
|---|---|
| 0–2 days | Normal — process when ready |
| 3–7 days | Prioritize today |
| 8–30 days | Force triage before new captures |
| 30+ days | Archive or delete |

## Agent Rules

- Tag agent-created drafts with `#agent-review`
- Do not route directly to `20-knowledge/` — Human reviews first
- Use `[[_template-capture]]` for new agent captures
