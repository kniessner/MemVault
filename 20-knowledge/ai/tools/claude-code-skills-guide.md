---
template: ai-tool
title: "Claude Code: Essential Built-in Skills and Commands"
source: https://batsov.com/articles/2026/03/11/essential-claude-code-skills-and-commands/
author: Bozhidar Batsov
published: "2026-03-11"
archived: "2026-05-01"
date-created: "2026-05-01"
date-updated: "2026-05-01"
description: >
  Comprehensive guide to Claude Code's built-in skills (/simplify, /review, /batch, /loop, /debug, /claude-api)
  and slash commands (/compact, /diff, /btw, /memory, /plan, etc). Covers skills vs. commands distinction,
  creating custom skills, and practical workflow tips.
category: ai-tool
tool_type: coding-assistant
tags:
  - claude-code
  - skills
  - slash-commands
  - ai-tools
  - coding-assistant
  - productivity
  - bookmark
  - cli
domain: batsov.com
site: batsov.com
---

# Essential Claude Code Skills and Commands

> **Source:** [batsov.com](https://batsov.com/articles/2026/03/11/essential-claude-code-skills-and-commands/)  
> **Author:** Bozhidar Batsov  
> **Published:** 2026-03-11  
> **Scraped:** 2026-05-01

## Summary

Claude Code comes with powerful built-in capabilities that many users overlook in favor of building custom skills. This article covers the difference between **skills** (AI-driven workflow prompts) and **slash commands** (fixed CLI operations), the six built-in skills, useful slash commands, skill arguments/parameters, how to create custom skills, and practical workflow tips.

---

## Skills vs. Slash Commands: What's the Difference?

**Slash commands** are built-in fixed-logic operations: `/clear`, `/compact`, `/help`, `/model`, `/cost`. Hardcoded into the CLI — do one thing, no AI reasoning, not customizable.

**Skills** are prompt-based capabilities. When invoked, they load a markdown instruction file into context and Claude executes them. Skills can spawn subagents, accept arguments, use specific tools, and orchestrate complex multi-step workflows. Built-in skills: `/simplify`, `/review`, `/batch`, `/loop`, `/debug`, `/claude-api`.

Historically, Claude Code had separate **commands** (`.claude/commands/*.md`) and **skills** (`.claude/skills/*/SKILL.md`). These have merged — files in either location create the same `/slash-command` interface. The skills system is recommended going forward because it supports:

- Supporting files (templates, examples, scripts alongside SKILL.md)
- Frontmatter control (`disable-model-invocation`, `user-invocable`, `allowed-tools`, `context`, `agent`)
- Dynamic context injection via shell command output
- Subagent execution with `context: fork`

Existing `.claude/commands/` files still work, but new ones should go in `.claude/skills/`.

> List all available skills (built-in + custom) with `/skills`.

---

## The Built-in Skills

### /simplify — Code Quality Review

Reviews recently changed files for code reuse, quality issues, and efficiency improvements — then fixes them automatically. Spawns three parallel review agents, each from a different angle. Essentially a mini code review without leaving the terminal.

```
/simplify
/simplify memory efficiency
/simplify error handling
/simplify reduce duplication
```

Pass a focus area to narrow the review. Most valuable right after larger refactors or accepting AI-generated code — catches unused imports, redundant variables, missed extractions, overly complex conditionals.

### /review — Code Review

PR-style review of your changes. Examines for bugs, logic errors, edge cases, style issues.

```
/review
/review 123
/review https://github.com/org/repo/pull/123
```

Without arguments: reviews recent local changes. Pass a PR number/URL to review a pull request.

**Typical workflow:** Make changes → `/review` for correctness → fix flags → `/simplify` for cleanliness.

### /batch — Large-Scale Parallel Changes

Heavy hitter for repetitive, parallelizable changes. Decomposes work into 5–30 independent units and spawns isolated worktree agents.

```
/batch migrate all test files from Jest to Vitest
/batch add TypeScript types to all files in src/utils/
/batch update all API endpoints to use the new auth middleware
```

Each agent works in its own git worktree, implements its unit, runs tests, can open a PR. Ideal for pattern-based changes, not redesigns.

### /loop — Scheduled Recurring Prompts

Runs a prompt repeatedly on a schedule while session stays open.

```
/loop 5m check if the dev server has any new errors in the log
/loop 10m run the test suite and report any failures
/loop 1h check deployment status and summarize metrics
```

Useful for monitoring tasks — long-running builds, staging deployments, log watching.

### /debug — Session Troubleshooting

When something goes wrong — tool calls fail silently, context loss, inexplicable behavior — `/debug` reads session debug logs and helps diagnose. "Claude, diagnose yourself."

```
/debug
/debug why did the last edit fail
/debug tool calls are timing out
```

### /claude-api — API Reference Loader

Loads relevant Claude API reference material for your project's language (Python, TypeScript, Java, Go, Ruby, C#, PHP, cURL) + Agent SDK reference.

```
/claude-api
```

Activates automatically when Claude detects imports of `anthropic`, `@anthropic-ai/sdk`, or `claude_agent_sdk`.

---

## Useful Slash Commands

### Context & Session

| Command | Description |
|---------|-------------|
| `/compact [focus]` | Compress conversation history. Essential for long sessions — use proactively before new work phases. |
| `/diff` | Interactive diff viewer of all changes Claude made. Checkpoint before moving on. |
| `/rewind` | Reverts conversation + file changes to a previous checkpoint. Your safety net. |
| `/context` | Colored grid showing context window usage. |
| `/btw "question"` | Side question without polluting main context. |

### Model & Usage

| Command | Description |
|---------|-------------|
| `/model <name>` | Switch model mid-session (e.g., `/model sonnet`, `/model opus`). |
| `/fast on/off` | Toggle fast mode (optimize for speed over quality). |
| `/usage` | Plan-level limits and rate limit status. |
| `/cost` | Token usage + estimated dollar cost (API billing users). |
| `/stats` | Daily usage patterns, session history, model preferences. |

### Workflow

| Command | Description |
|---------|-------------|
| `/plan` | Plan mode — Claude designs strategy without making changes. Toggle with `Shift+Tab`. |
| `/memory` | View/edit Claude's persistent MEMORY.md for the project. |
| `/copy` | Copy last response to clipboard. Interactive picker for multiple code blocks. |

---

## Skill Arguments and Parameters

All skills support `$ARGUMENTS` placeholder (and indexed `$0`, `$1`).

| Skill | Arguments (optional → required) |
|-------|--------------------------------|
| `/simplify` | Optional focus area: `/simplify error handling` |
| `/review` | Optional PR number/URL: `/review 123` |
| `/batch` | Required: change description |
| `/loop` | Optional interval + required prompt: `/loop 5m check build` |
| `/debug` | Optional issue description: `/debug why did the edit fail` |
| `/claude-api` | None |

Custom SKILL.md example:

```yaml
---
name: fix-issue
description: Fix a GitHub issue
argument-hint: <issue-number>
---

Fix GitHub issue $ARGUMENTS following our project's standards.
```

Invoked as `/fix-issue 123`, `$ARGUMENTS` becomes `123`.

---

## Creating Your Own Skills

Skills live in one of three locations:

| Scope | Path | Use case |
|-------|------|----------|
| Personal | `~/.claude/skills/<name>/SKILL.md` | Your workflows, all projects |
| Project | `.claude/skills/<name>/SKILL.md` | Team conventions, commit to git |
| Plugin | `<plugin>/skills/<name>/SKILL.md` | Shared via plugin system |

A skill = SKILL.md file with optional frontmatter:

```yaml
---
name: deploy
description: Deploy the current branch to staging
disable-model-invocation: true
allowed-tools: Bash
---

1. Run the test suite: `npm test`
2. Build production bundle: `npm run build`
3. Deploy: `./scripts/deploy.sh staging`
4. Verify via health endpoint
```

**Frontmatter options:**

| Option | Description |
|--------|-------------|
| `disable-model-invocation: true` | Only user can invoke (for side-effect ops) |
| `user-invocable: false` | Only Claude invokes (background knowledge) |
| `allowed-tools` | Restrict which tools Claude can use |
| `context: fork` | Run in isolated subagent (won't pollute main conversation) |
| `agent` | Subagent type: Explore, Plan, general-purpose |

Supporting files (templates, examples, scripts) can live alongside SKILL.md. Dynamic context injection via `!`command`:shell syntax:

```markdown
---
name: pr-review
description: Review the current PR
---

Here's the PR diff:
!`gh pr diff`

Changed files:
!`gh pr diff --name-only`

Review these changes for correctness, style, and potential issues.
```

---

## Workflow Tips

1. **Chain /simplify after AI-generated changes.** AI output often has subtle redundancies a second pass catches.
2. **Use /batch for migrations, not redesigns.** Perfect for repetitive, parallelizable changes. "Add error handling to all 47 API endpoints" — yes. "Redesign the API layer" — no.
3. **Use /compact proactively.** Don't wait for context loss. Compact between logical work chunks.
4. **Start with /plan for complex tasks.** Think through the approach before a single line of code.
5. **Use /btw liberally.** Side questions are context-free — use them for lookups.

---

## Related

- [[claude-code-lsp|Claude Code LSP Setup Guide]]
- [[claude-code|Claude Code]]
- [[oh-my-codex|oh-my-codex (OMX) — Codex Workflow Layer]]
- [[../providers/anthropic|Anthropic]]
