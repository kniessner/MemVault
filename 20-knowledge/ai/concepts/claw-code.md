---
title: What Is Claw Code? The Claude Code Rewrite Explained | WaveSpeedAI Blog
source: https://wavespeed.ai/blog/posts/what-is-claw-code/
domain: wavespeed.ai
site: WaveSpeedAI
author: WaveSpeed
date-created: 2026-04-08
date-updated: 2026-04-08
scraped: 2026-04-08T16:08:09.728997
tags: ['code-generation', 'claw', 'generative-ai', 'ai', 'wavespeed', 'coding-assistant', 'bookmark', 'wavespeed-ai']
---

# What Is Claw Code? The Claude Code Rewrite Explained | WaveSpeedAI Blog

> **Source:** [wavespeed.ai](https://wavespeed.ai/blog/posts/what-is-claw-code/)
> **Scraped:** 2026-04-08

## Summary

claw-code is a clean-room Python rewrite of Claude Code

## Content

claw-code is a clean-room Python rewrite of Claude Code&#39;s agent harness. Here&#39;s what it is, how it happened, and what builders need to know.

Hey, guys. I’m Dora. Can you imagine? I’ve been watching the claw-code repository since the morning it appeared. Not because I expected to use it — but because the circumstances around its creation clarify how the agentic coding ecosystem actually works, underneath all the noise.

Let me walk through what happened, ​what claw-code is​, and who should actually care.

On March 31, 2026, security researcher Chaofan Shou noticed something odd in the npm registry. Version 2.1.88 of @anthropic-ai/claude-code had shipped with a 59.8 MB JavaScript source map file attached.

Source maps are debugging artifacts — they translate minified production code back into readable TypeScript so developers can make sense of stack traces. They are not supposed to ship in public packages.

The mechanism isn’t exotic. Bun’s bundler, which Claude Code uses internally, generates source maps by default unless you explicitly disable them. There’s an open Bun bug (oven-sh/bun#28001, filed March 11) reporting that source maps appear in production builds even when they shouldn’t. If that’s what caused the leak, then Anthropic’s own build toolchain shipped a known issue that exposed their own product. Nobody had to hack anything. The file was just there, pointing to a zip archive sitting on ​Anthropic’s own Cloudflare R2 storage bucket​.

Anthropic confirmed the incident as “​a release packaging issue caused by human error, not a security breach​.” Worth noting: this is the second time it’s happened — a nearly identical source map leak occurred with an earlier version in February 2025.

One more thing for anyone who updated Claude Code via npm that morning: a separate supply-chain attack on the axios package was active between 00:21 and 03:49 UTC the same day. Axios is a Claude Code dependency. If you updated during that window, audit your dependencies and rotate credentials.

No customer data, no API credentials, no model weights. What was exposed: approximately 512,000 lines of TypeScript across ~1,900 files — the query engine, tool system, multi-agent orchestration logic, context compaction, and 44 feature flags covering functionality that’s built but not yet shipped.

Those feature flags are the most strategically sensitive part. Compiled code sitting behind flags that evaluate to false in the external build isn’t just implementation detail — it’s a product roadmap. Competitors can now see what Anthropic has built and is considering shipping. That strategic surprise can’t be un-leaked.

Within hours of the exposure, mirrored repositories appeared on GitHub. Anthropic began issuing DMCA takedowns. The internet did not wait.

Sigrid Jin (@instructkr) — a Korean developer who had attended Claude Code’s first birthday party in San Francisco in February — published what became claw-code. The repo reached ​50,000 stars in two hours​, one of the fastest accumulation rates GitHub has recorded.

The important distinction:​ ​claw-code​​ is not an archive of the leaked TypeScript. It’s a clean-room Python rewrite, built from scratch by reading the original harness structure and reimplementing the architectural patterns without copying Anthropic’s proprietary source. Jin built it overnight using oh-my-codex, an orchestration layer on top of OpenAI’s Codex, with parallel code review and persistent execution loops.

Whether clean-room reimplementation fully sidesteps copyright exposure is a legal question, not a technical one. That answer isn’t settled. The repo is explicit: “This repository does not claim ownership of ​**the original Claude Code source material.**​” But framing and legal outcome aren’t the same thing.

As of April 2026, the main source tree is Python-first. ​The structure mirrors Claude Code’s core modules: CLI entry, query engine, runtime session management, tool execution, permission context, session persistence, and a parity_audit.py that explicitly tracks gaps from the original implementation.

