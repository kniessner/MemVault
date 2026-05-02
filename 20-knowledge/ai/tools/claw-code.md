---
title: claw-code
description: Clean-room Python rewrite of Claude Code's agent harness
url: https://wavespeed.ai/blog/posts/what-is-claw-code/
author: WaveSpeedAI
published: 2026-04-01
category: tool
tags:
  - claude-code
  - coding-agent
  - python
  - agent-harness
  - open-source
  - clean-room
status: emerging
---

# claw-code

**claw-code** is a clean-room Python rewrite of Claude Code's agent harness that emerged after the Claude Code source code was accidentally exposed in March 2026. It represents a community effort to create an open, auditable alternative to Anthropic's proprietary coding agent.

## Background: The Claude Code Source Exposure

In March 2026, Claude Code's source code was accidentally made publicly accessible, revealing the internal implementation details of Anthropic's coding agent. While Anthropic quickly fixed the issue, the exposure sparked significant community interest in understanding and potentially recreating the agent architecture.

**claw-code** was developed as a clean-room implementation — written from scratch based on publicly observable behavior and the architectural insights gained from the exposure, without directly copying proprietary code.

## What claw-code Is

A Python-based coding agent framework that replicates the core functionality of Claude Code:

- **Agent harness** — Orchestrates LLM interactions with file system and shell
- **Tool system** — Extensible tool calling architecture
- **Context management** — Handles large codebases efficiently
- **Multi-turn reasoning** — Stateful conversation with the agent

## Architecture Highlights

Based on the leaked source analysis, Claude Code (and by extension, claw-code's target architecture) consists of:

### 1. Core Agent Loop
- Synchronous message processing
- Tool call dispatch and result handling
- Conversation state management

### 2. Tool Registry
- Dynamic tool discovery
- Schema-based validation
- Environment-aware availability checking

### 3. Context Management
- Sliding window conversation history
- Smart context compression
- File content caching

### 4. Terminal Integration
- Pseudo-terminal (PTY) support for interactive programs
- Process lifecycle management
- Output streaming

## Should Builders Pay Attention?

**Reasons to consider claw-code:**
- Open, auditable codebase
- Python ecosystem integration
- Community-driven development
- Not tied to Anthropic's product roadmap

**Reasons to stay with Claude Code:**
- Official Anthropic support
- Tight Claude model integration
- Continuous updates and improvements
- Established reliability

## Current Status

As of April 2026, claw-code is an emerging project. Key considerations:

- **Early stage** — Not yet feature-complete compared to Claude Code
- **Community-driven** — Development pace depends on contributor interest
- **Clean-room** — Legally distinct implementation
- **Educational value** — Useful for understanding agent architectures

## Comparison

| Aspect | Claude Code | claw-code |
|--------|-------------|-----------|
| Language | TypeScript | Python |
| Official | Yes (Anthropic) | No (community) |
| Support | Commercial | Community |
| Integration | Best with Claude | Model-agnostic potential |
| Source | Proprietary | Open |

## Related Developments

The Claude Code source exposure also revealed:
- Hidden features and capabilities
- Internal tool implementations
- Context window management strategies
- Multi-agent coordination patterns

## Resources

- **Article**: [What Is Claw Code? The Claude Code Rewrite Explained](https://wavespeed.ai/blog/posts/what-is-claw-code/)
- **Related**: [Claude Code Hidden Features](https://wavespeed.ai/blog/posts/claude-code-hidden-features-leaked-source-2026/)
- **Related**: [claw-code Pricing and Access](https://wavespeed.ai/blog/posts/claw-code-pricing-2026/)

## See Also

- [[tools/claude-code|Claude Code]]
- [[tools/oh-my-codex|oh-my-codex]]
- [[providers/anthropic|Anthropic]]
- [[../concepts/agents|AI Agents]]

## Note

This is a rapidly evolving situation. The claw-code project may merge with or be superseded by other community efforts to create open coding agents. The key takeaway is the emergence of open alternatives to proprietary coding assistants.
