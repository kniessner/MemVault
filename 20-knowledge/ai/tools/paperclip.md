---
url: https://paperclip.ing/
title: Paperclip
description: The human control plane for AI labor — orchestrate autonomous companies of AI agents
source_doc: https://paperclip.ing/
git_repo: https://github.com/paperclip-labs/paperclip
created: 2026-04-27
author: Paperclip Labs
license: Open source
pricing: Free (self-hosted)
tags:
  - bookmark
  - agent-orchestration
  - autonomous-company
  - multi-agent
  - open-source
  - self-hosted
  - company-management
  - bot-management
  - ai-labor
  - goals-system
---

# Paperclip

> **The human control plane for AI labor.** Manage a team of AI agents to run your business. Org charts, budgets, governance, and goals — all in one deployment.

## Overview

**Paperclip** is an open-source platform for orchestrating autonomous companies of AI agents. Instead of managing individual bots, you define a **company** with roles, budgets, goals, and governance — then let the agents execute.

| Attribute | Value |
|-----------|-------|
| **Website** | https://paperclip.ing |
| **GitHub** | https://github.com/paperclip-labs/paperclip |
| **License** | Open source |
| **Pricing** | Free (self-hosted) |
| **Setup** | Interactive setup wizard — no Paperclip account required |

## Philosophy

Paperclip reframes AI agents from tools to **employees**:

| Analogy | Paperclip |
|---------|-----------|
| **Employees** | Your bots (Cursor, Codex, OpenClaw, custom, etc.) |
| **Org chart** | Roles, reporting, responsibilities |
| **Budget** | Monthly spending per agent |
| **Goals** | Company objectives the agents work toward |
| **Governance** | Approval workflows, limits, oversight |

## Core Concepts

| Concept | Description |
|---------|-------------|
| **Goal Alignment** | Define what the business needs; agents self-organize toward it |
| **Bring Your Own Agent** | Paperclip connects existing agents — no lock-in |
| **Heartbeats** | Regular check-ins so agents don't drift |
| **Cost Control** | Monthly budgets per agent; auto-stop when exceeded |
| **Ticket System** | Human oversight via approval tickets |
| **Multi-Company** | Run multiple businesses in one install |
| **Mobile Ready** | Manage your agents from your phone |
| **Org Chart** | Visual hierarchy of agent roles |

## Workflow

1. **Define the goal** → "Build a SaaS landing page with auth and Stripe"
2. **Hire the team** → Assign Cursor (code), Codex (QA), OpenClaw (infrastructure)
3. **Approve and run** → Review plans, set budgets, let them work

## Skills System

Paperclip uses **SKILLS.md** files so agents know how to:
- Follow company conventions
- Use internal tools
- Report progress
- Handle failures

## Cost Control

| Feature | Description |
|---------|-------------|
| **Per-agent budget** | Each agent has a monthly spending cap |
| **Auto-stop** | Budget exceeded → agent pauses |
| **Cost tracking** | See which agents are expensive per task/project/goal |
| **Forecasting** | Predict spending before approving |

## Setup

```bash
# Self-hosted, interactive setup
git clone https://github.com/paperclip-labs/paperclip.git
cd paperclip
./setup.sh
```

Setup walks you through:
1. Database setup
2. Authentication
3. First company configuration
4. Agent connections

## Agents Supported

- Cursor
- Codex
- OpenClaw
- Claude Code
- Claude 3/4 Sonnet
- Any custom agent via API
- ("Bring your own bot")

## Comparison

| | Paperclip | Factory | n8n | CrewAI |
|---|-----------|---------|-----|--------|
| **Concept** | AI company management | Industrial dev agents | Workflow automation | Agent teams |
| **Agents** | BYOA (bring your own) | Factory Droids | Pre-built nodes | Crew (roles) |
| **Budget control** | ✅ Per-agent | ✅ Usage-based | ⚠️ Basic | ❌ |
| **Self-hosted** | ✅ | ❌ | ✅ | ✅ |
| **Open source** | ✅ | ❌ | ✅ | ✅ |
| **Goal alignment** | ✅ Company goals | ✅ Ticket-driven | ❌ | ⚠️ Task-based |
| **Mobile** | ✅ | ❌ | ❌ | ❌ |

## Why It Matters

1. **Company-level orchestration** — Not just managing agents, but building an autonomous organization
2. **BYOA (Bring Your Own Agent)** — No lock-in; works with whatever tools your team already uses
3. **Financial guardrails** — Real budget controls prevent runaway AI spend
4. **Self-hosted privacy** — Your data never leaves your infrastructure
5. **Mobile management** — Approve tasks and monitor agents from your phone

## Community Quotes

- *"Great for orchestrating a bunch of agents to do dev, content, social, marketing, QA, research, outreach"*
- *"OpenClaw is an employee, Paperclip is the company"*
- *"This replaces my mission control dashboard"*
- *"This is gonna be the interface of the future"*

## Related

- [[factory-ai]] — Enterprise AI coding agents
- [[hermes-agent]] — Open-source multi-platform agent
- [[crewai]] — Framework for AI agent teams
- [[n8n]] — Workflow automation with AI nodes

---

*Last updated: 2026-04-27*
