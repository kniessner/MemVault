---
template: ai-tool
title: 'Claude Code LSP Setup Guide'
source: https://karanbansal.in/blog/claude-code-lsp/
author: Karan Bansal
published: ''
archived: '2026-04-08'
date-created: '2026-04-08'
date-updated: '2026-04-08'
description: Every Claude Code user is running without LSP. That means 30-60s grep
  searches instead of 50ms precise answers. Here's how to enable it — setup, real
  debug data, and undocumented discoveries.
category: ai-tool
tool_type: coding-assistant
tags:
- claude-code
- lsp
- language-server-protocol
- coding-assistant
- ai-tools
- setup-guide
- productivity
- developer-tools
- bookmark
domain: karanbansal.in
site: karanbansal
image: https://karanbansal.in/og-image.jpg
favicon: https://karanbansal.in/favicon.ico
---

# The 2-Minute Claude Code Upgrade You're Probably Missing: LSP - Karan Bansal

> **Source:** [karanbansal.in](https://karanbansal.in/blog/claude-code-lsp/)
> **Author:** Karan Bansal
> **Scraped:** 2026-04-08 16:06

## Summary

Every Claude Code user is running without LSP. That means 30-60s grep searches instead of 50ms precise answers. Here's how to enable it — setup, real debug data, and undocumented discoveries.

## Overview

Every Claude Code user is running without LSP. That means 30-60s grep searches instead of 50ms precise answers. Here's how to enable it — setup, real debug data, and undocumented discoveries.

## Key Points

1. Right now, every Claude Code user is running without LSP. That means every time you ask "where is processPayment defined?", Claude Code does what you'd do with a terminal. It greps. It searches text patterns across your entire codebase, reads through dozens of files, and tries to figure out which ma...
2. It works. But it's slow, it's fuzzy, and on large codebases it regularly misses or gets confused. Search for User in a real project and you get 847 matches across 203 files: class definitions, variable names, comments, imports, CSS classes, SQL columns. The thing you actually wanted? Buried somewher...
3. There's a feature that changes this entirely. It's called LSP, the Language Server Protocol. It's not enabled by default. It's not prominently documented. The setup requires a flag discovered through a GitHub issue, not the official docs. But once it's on, the same query ("where is processPayment de...
4. That's not an incremental improvement. That's a category change in how Claude Code navigates your code...
5. Claude Code ships without LSP enabled. Enabling it gives Claude the same code intelligence your IDE has: go-to-definition, find references, type info, real-time error detection. From my debug logs: ~50ms per query vs 30-60s with grep. Two minutes of setup. Jump to setup →...
6. By default, Claude Code navigates your codebase with text search tools: Grep, Glob, and Read. It's the same as having a very fast developer with grep and find at a terminal. Smart pattern matching, but fundamentally just matching text...
7. The core problem: grep treats code as text. But code is not text. It has structure, meaning, and relationships. When you ask "where is getUserById defined?", you want the one function definition, not the 50 places that call it plus the 12 comments that mention it. Grep can't tell the difference. LSP...
8. Before 2016, every code editor had to build its own language support from scratch. VS Code needed a Python plugin. Vim needed a separate Python plugin. Emacs, Sublime, Atom — each one reinventing the same work. Twenty editors times fifty languages meant a thousand separate implementations, most of t...

## Table of Contents

- [What You're Currently Running](#what-you're-currently-running)
- [What LSP Actually Is](#what-lsp-actually-is)
- [The Performance Gap](#the-performance-gap)
- [What Claude Code Gets from LSP](#what-claude-code-gets-from-lsp)
- [Passive: Self-Correcting Edits](#passive:-self-correcting-edits)
- [Active: On-Demand Code Intelligence](#active:-on-demand-code-intelligence)
- [Setting It Up](#setting-it-up)
- [Prerequisites](#prerequisites)
- [Step 1: Enable the LSP Tool](#step-1:-enable-the-lsp-tool)

---

# Content

Right now, every Claude Code user is running without LSP. That means every time you ask "where is processPayment defined?", Claude Code does what you'd do with a terminal. It greps. It searches text patterns across your entire codebase, reads through dozens of files, and tries to figure out which match is the actual definition.

It works. But it's slow, it's fuzzy, and on large codebases it regularly misses or gets confused. Search for User in a real project and you get 847 matches across 203 files: class definitions, variable names, comments, imports, CSS classes, SQL columns. The thing you actually wanted? Buried somewhere in the middle. Claude Code has to read through each match to narrow it down. That takes 30-60 seconds. Sometimes longer.

There's a feature that changes this entirely. It's called LSP, the Language Server Protocol. It's not enabled by default. It's not prominently documented. The setup requires a flag discovered through a GitHub issue, not the official docs. But once it's on, the same query ("where is processPayment defined?") returns the exact file and line number in 50 milliseconds. Not 30 seconds. Fifty milliseconds. With 100% accuracy.

That's not an incremental improvement. That's a category change in how Claude Code navigates your code.

Claude Code ships without LSP enabled. Enabling it gives Claude the same code intelligence your IDE has: go-to-definition, find references, type info, real-time error detection. From my debug logs: ~50ms per query vs 30-60s with grep. Two minutes of setup. Jump to setup →

## What You're Currently Running {#what-you're-currently-running}

By default, Claude Code navigates your codebase with text search tools: Grep, Glob, and Read. It's the same as having a very fast developer with grep and find at a terminal. Smart pattern matching, but fundamentally just matching text.

The core problem: grep treats code as text. But code is not text. It has structure, meaning, and relationships. When you ask "where is getUserById defined?", you want the one function definition, not the 50 places that call it plus the 12 comments that mention it. Grep can't tell the difference. LSP can.

## What LSP Actually Is {#what-lsp-actually-is}

Before 2016, every code editor had to build its own language support from scratch. VS Code needed a Python plugin. Vim needed a separate Python plugin. Emacs, Sublime, Atom — each one reinventing the same work. Twenty editors times fifty languages meant a thousand separate implementations, most of them incomplete.

In 2016, Microsoft had an insight: separate the language intelligence from the editor. Create a protocol, a standard way for any editor to talk to any language server. The editor says "where is this symbol defined?" in JSON-RPC. The language server (a separate process that deeply understands one language) answers.

That's LSP. It turned a thousand-implementation problem into a seventy-implementation one. And it's why your VS Code Python experience is exactly as good as your Neovim Python experience — they're both talking to Pyright.

## The Performance Gap {#the-performance-gap}

Here's the thing nobody talks about: AI coding assistants had the exact same problem that editors had before LSP. Without it, Claude Code does text search. Grep, Glob, Read. It works. But the cost is measured in seconds per query, multiplied by dozens of queries per task. It adds up fast.

## What Claude Code Gets from LSP {#what-claude-code-gets-from-lsp}

LSP gives Claude Code two categories of superpowers: things that happen automatically and things it can actively request.

## Passive: Self-Correcting Edits {#passive:-self-correcting-edits}

This is the most valuable part, and most people don't even realize it's happening. After every file edit, the language server pushes diagnostics: type errors, missing imports, undefined variables. Claude Code sees these immediately and fixes them in the same turn, before you ever see the error.

Think about what this means in practice. You ask Claude to add an email parameter to createUser(). Claude edits the function signature. The language server instantly reports 3 errors at three call sites that now have the wrong number of arguments. Claude sees the errors, finds all three call sites, and fixes them. You get the result with zero errors on the first try.

Without LSP, Claude would edit the function, hand you the result, you'd try to compile, see 3 errors, paste them back to Claude, and iterate. With LSP, that entire loop collapses into one step.

## Active: On-Demand Code Intelligence {#active:-on-demand-code-intelligence}

Beyond automatic diagnostics, Claude Code can explicitly ask the language server questions:

goToDefinition — "Where is processOrder defined?" → exact file and line

findReferences — "Find all places that call validateUser" → every call site with location

hover — "What type is the config variable?" → full type signature and docs

## Setting It Up {#setting-it-up}

Here's the full setup. It takes about 2 minutes, and you only do it once.

## Prerequisites {#prerequisites}

Claude Code version 2.0.74 or later (run claude --version to check)

The language server binary for your language(s) installed and in $PATH

## Step 1: Enable the LSP Tool {#step-1:-enable-the-lsp-tool}

This is the part that trips people up. You need to add a flag to your Claude Code settings:

Add this to your ~/.claude/settings.json:

~/.claude/settings.json

"env": { "ENABLE_LSP_TOOL": "1" }

ENABLE_LSP_TOOL is not officially documented as of February 2026. It was discovered via GitHub Issue #15619 as a community workaround. It may change or become unnecessary in future versions. I also recommend adding export ENABLE_LSP_TOOL=1 to your shell profile (~/.zshrc on macOS, ~/.bashrc on Linux) as a fallback.

## Step 2: Install the Language Server {#step-2:-install-the-language-server}

Install the binary for each language you work with. These are the same language servers your IDE uses. LSP is universal.

Language Plugin Install Command Python pyright-lsp npm i -g pyright TypeScript/JS typescript-lsp npm i -g typescript-language-server typescript Go gopls-lsp go install golang.org/x/tools/gopls@latest Rust rust-analyzer-lsp rustup component add rust-analyzer Java jdtls-lsp brew install jdtls C/C++ clangd-lsp brew install llvm C# csharp-lsp dotnet tool install -g csharp-ls PHP php-lsp npm i -g intelephense Kotlin kotlin-lsp GitHub releases Swift swift-lsp Included with Xcode Lua lua-lsp GitHub releases

npm i -g typescript-language-server typescript

go install golang.org/x/tools/gopls@latest

rustup component add rust-analyzer

## Step 3: Install and Enable the Plugin {#step-3:-install-and-enable-the-plugin}

First, update the marketplace catalog:

claude plugin marketplace update claude-plugins-official

Then install the plugin for your language:

claude plugin install pyright-lsp

claude plugin install typescript-lsp

## Step 4: Restart Claude Code {#step-4:-restart-claude-code}

LSP servers initialize at startup. After installing plugins, you need a full restart. Then verify by asking Claude: "What type is [some variable]?" — if it uses the LSP hover operation instead of reading the file, you're good.

## What Happens at Startup {#what-happens-at-startup}

Here's something I found interesting while digging through debug logs. When Claude Code starts, all enabled LSP servers launch simultaneously. They don't wait for you to open a file.

From my actual debug logs (4 language servers enabled):

# From ~/.claude/debug/ — session on Feb 23, 2026 05:53:56.216 [LSP MANAGER] Starting async initialization 05:53:56.573 Total LSP servers loaded: 4 05:53:56.757 gopls initialized (+0.5s) 05:53:56.762 typescript initialized (+0.5s) 05:53:56.819 pyright initialized (+0.6s) 05:54:04.791 jdtls initialized (+8.6s) Index is warm — all LSP operations now ~50ms

# From ~/.claude/debug/ — session on Feb 23, 2026 05:53:56.216 [LSP MANAGER] Starting async initialization 05:53:56.573 Total LSP servers loaded: 4 05:53:56.757 gopls initialized (+0.5s) 05:53:56.762 typescript initialized (+0.5s) 05:53:56.819 pyright initialized (+0.6s) 05:54:04.791 jdtls initialized (+8.6s) Index is warm — all LSP operations now ~50ms

Two things stand out. First, the Java server takes ~8 seconds because of JVM warmup — this is normal, not a bug. Second, servers start indexing your entire project immediately. They scan all files of their language type, build symbol tables, and resolve dependencies. By the time you ask your first question, the index is already warm.

## Using It in Practice {#using-it-in-practice}

You don't need to learn any new commands. Just talk to Claude Code the way you normally would:

You say... Claude uses... "Where is authenticate defined?" goToDefinition "Find all usages of UserService" findReferences "What type is response?" hover "What functions are in auth.ts?" documentSymbol "Find the PaymentService class" workspaceSymbol "What implements AuthProvider?" goToImplementation "What calls processPayment?" incomingCalls "What does handleOrder call?" outgoingCalls

The real power shows up in refactoring sessions. When you're renaming a method, adding a parameter, or changing a return type, LSP ensures Claude finds every reference and updates them correctly — not the "grep found 47 out of 52 actual usages" situation.

You can also press Ctrl+O to see diagnostics pushed by LSP servers. This shows you what the language servers are seeing in real time.

## The Gotchas {#the-gotchas}

I hit most of these so you don't have to.

Issue Cause Fix LSP tool not available at all ENABLE_LSP_TOOL not set Add under "env" in settings.json, restart "Plugin not found in any marketplace" Stale marketplace catalog claude plugin marketplace update claude-plugins-official Plugin installed but disabled Not enabled after install claude plugin enable <name> + restart "Executable not found in $PATH" Binary not installed or not in PATH Install binary, verify with which <binary> "No server available" Race condition during startup Restart Claude Code, wait for servers to initialize "Total LSP servers loaded: 0" in logs Plugins installed but all disabled Enable plugins, restart

claude plugin marketplace update claude-plugins-official

claude plugin enable <name>

## Debug Checklist {#debug-checklist}

When things aren't working:

Check the binary is installed: which pyright-langserver (or whatever binary your language needs)

which pyright-langserver

Check plugin status: claude plugin list — look for Status: enabled

## Nudging Claude to Actually Use LSP {#nudging-claude-to-actually-use-lsp}

Even with LSP fully set up, Claude Code may default to its familiar tools (Grep, Read, Glob) instead of LSP. This is the most common complaint after setup. The fix: add explicit instructions telling Claude to prefer LSP for code navigation.

CLAUDE.md — add the snippet below to ~/.claude/CLAUDE.md so it applies globally across all your projects. Or add it to your project's CLAUDE.md if you only want it for one repo.

Auto memory — tell Claude in conversation: "remember to always prefer LSP over Grep for code navigation." Claude saves it to auto memory and follows it in future sessions. Note: auto memory is per working tree, so you'd need to do this in each repo.

### Code Intelligence Prefer LSP over Grep/Glob/Read for code navigation: - `goToDefinition` / `goToImplementation` to jump to source - `findReferences` to see all usages across the codebase - `workspaceSymbol` to find where something is defined - `documentSymbol` to list all symbols in a file - `hover` for type info without reading the file - `incomingCalls` / `outgoingCalls` for call hierarchy Before renaming or changing a function signature, use `findReferences` to find all call sites first. Use Grep/Glob only for text/pattern searches (comments, strings, config values) where LSP doesn't help. After writing or editing code, check LSP diagnostics before moving on. Fix any type errors or missing imports immediately.

---

## Code Examples

```
{
  "env": {
    "ENABLE_LSP_TOOL": "1"
  },
  "enabledPlugins": {
    "pyright-lsp@claude-plugins-official": true,
    "typescript-lsp@claude-plugins-official": true,
    "gopls-lsp@claude-plugins-official": true
  }
}
```

```
# From ~/.claude/debug/ — session on Feb 23, 2026

05:53:56.216  [LSP MANAGER] Starting async initialization
05:53:56.573  Total LSP servers loaded: 4
05:53:56.757  gopls initialized          (+0.5s)
05:53:56.762  typescript initialized     (+0.5s)
05:53:56.819  pyright initialized        (+0.6s)
05:54:04.791  jdtls initialized          (+8.6s)
              Index is warm — all LSP operations now ~50ms
```

```
### Code Intelligence

Prefer LSP over Grep/Glob/Read for code navigation:
- `goToDefinition` / `goToImplementation` to jump to source
- `findReferences` to see all usages across the codebase
- `workspaceSymbol` to find where something is defined
- `documentSymbol` to list all symbols in a file
- `hover` for type info without reading the file
- `incomingCalls` / `outgoingCalls` for call hierarchy

Before renaming or changing a function signature, use
`findReferences` to find all call sites first.

Use Grep/Glob only for text/pattern searches (comments,
strings, config values) where LSP doesn't help.

After writing or editing code, check LSP diagnostics before
moving on. Fix any type errors or missing imports immediately.
```

---

## Lists

### UL List

- goToDefinition — "Where is processOrder defined?" → exact file and line
- findReferences — "Find all places that call validateUser" → every call site with location
- hover — "What type is the config variable?" → full type signature and docs
- documentSymbol — "List all functions in this file" → every symbol with location
- workspaceSymbol — "Find the PaymentService class" → search symbols across the entire project
- goToImplementation — "What classes implement AuthProvider?" → concrete implementations of interfaces
- incomingCalls / outgoingCalls — "What calls processPayment?" → full call hierarchy tracing

### UL List

- Claude Code version 2.0.74 or later (run claude --version to check)
- The language server binary for your language(s) installed and in $PATH

### OL List

- Check the binary is installed: which pyright-langserver (or whatever binary your language needs)
- Check plugin status: claude plugin list — look for Status: enabled
- Check debug logs at ~/.claude/debug/latest — search for "Total LSP servers loaded: N" where N should be > 0

---

## Related

- [[claude-code-skills-guide|Claude Code Skills and Commands Guide]]
- [GitHub Issue #15619](https://github.com/anthropics/claude-code/issues/15619)
- [auto memory](https://code.claude.com/docs/en/memory#auto-memory)
- [LinkedIn](https://linkedin.com/in/karanb192)
- [RSS](https://karanbansal.in/blog/feed.xml)

---

## Raw Content

> ⚠️ *Auto-extracted content, may contain noise*

Right now, every Claude Code user is running without LSP. That means every time you ask "where is processPayment defined?", Claude Code does what you'd do with a terminal. It greps. It searches text patterns across your entire codebase, reads through dozens of files, and tries to figure out which match is the actual definition.

It works. But it's slow, it's fuzzy, and on large codebases it regularly misses or gets confused. Search for User in a real project and you get 847 matches across 203 files: class definitions, variable names, comments, imports, CSS classes, SQL columns. The thing you actually wanted? Buried somewhere in the middle. Claude Code has to read through each match to narrow it down. That takes 30-60 seconds. Sometimes longer.

There's a feature that changes this entirely. It's called LSP, the Language Server Protocol. It's not enabled by default. It's not prominently documented. The setup requires a flag discovered through a GitHub issue, not the official docs. But once it's on, the same query ("where is processPayment defined?") returns the exact file and line number in 50 milliseconds. Not 30 seconds. Fifty milliseconds. With 100% accuracy.

That's not an incremental improvement. That's a category change in how Claude Code navigates your code.

Claude Code ships without LSP enabled. Enabling it gives Claude the same code intelligence your IDE has: go-to-definition, find references, type info, real-time error detection. From my debug logs: ~50ms per query vs 30-60s with grep. Two minutes of setup. Jump to setup →

By default, Claude Code navigates your codebase with text search tools: Grep, Glob, and Read. It's the same as having a very fast developer with grep and find at a terminal. Smart pattern matching, but fundamentally just matching text.

The core problem: grep treats code as text. But code is not text. It has structure, meaning, and relationships. When you ask "where is getUserById defined?", you want the one function definition, not the 50 places that call it plus the 12 comments that mention it. Grep can't tell the difference. LSP can.

Before 2016, every code editor had to build its own language support from scratch. VS Code needed a Python plugin. Vim needed a separate Python plugin. Emacs, Sublime, Atom — each one reinventing the same work. Twenty editors times fifty languages meant a thousand separate implementations, most of them incomplete.

In 2016, Microsoft had an insight: separate the language intelligence from the editor. Create a protocol, a standard way for any editor to talk to any language server. The editor says "where is this symbol defined?" in JSON-RPC. The language server (a separate process that deeply understands one language) answers.

That's LSP. It turned a thousand-implementation problem into a seventy-implementation one. And it's why your VS Code Python experience is exactly as good as your Neovim Python experience — they're both talking to Pyright.

Right now, every Claude Code user is running without LSP. That means every time you ask "where is processPayment defined?", Claude Code does what you'd do with a terminal. It greps. It searches text patterns across your entire codebase, reads through dozens of files, and tries to figure out which match is the actual definition.

It works. But it's slow, it's fuzzy, and on large codebases it regularly misses or gets confused. Search for User in a real project and you get 847 matches across 203 files: class definitions, variable names, comments, imports, CSS classes, SQL columns. The thing you actually wanted? Buried somewhere in the middle. Claude Code has to read through each match to narrow it down. That takes 30-60 seconds. Sometimes longer.

There's a feature that changes this entirely. It's called LSP, the Language Server Protocol. It's not enabled by default. It's not prominently documented. The setup requires a flag discovered through a GitHub issue, not the official docs. But once it's on, the same query ("where is processPayment defined?") returns the exact file and line number in 50 milliseconds. Not 30 seconds. Fifty milliseconds. With 100% accuracy.

That's not an incremental improvement. That's a category change in how Claude Code navigates your code.

Claude Code ships without LSP enabled. Enabling it gives Claude the same code intelligence your IDE has: go-to-definition, find references, type info, real-time error detection. From my debug logs: ~50ms per query vs 30-60s with grep. Two minutes of setup. Jump to setup →

By default, Claude Code navigates your codebase with text search tools: Grep, Glob, and Read. It's the same as having a very fast developer with grep and find at a terminal. Smart pattern matching, but fundamentally just matching text.

The core problem: grep treats code as text. But code is not text. It has structure, meaning, and relationships. When you ask "where is getUserById defined?", you want the one function definition, not the 50 places that call it plus the 12 comments that mention it. Grep can't tell the difference. LSP can.

Before 2016, every code editor had to build its own language support from scratch. VS Code needed a Python plugin. Vim needed a separate Python plugin. Emacs, Sublime, Atom — each one reinventing the same work. Twenty editors times fifty languages meant a thousand separate implementations, most of them incomplete.

In 2016, Microsoft had an insight: separate the language intelligence from the editor. Create a protocol, a standard way for any editor to talk to any language server. The editor says "where is this symbol defined?" in JSON-RPC. The language server (a separate process that deeply understands one language) answers.

That's LSP. It turned a thousand-implementation problem into a seventy-implementation one. And it's why your VS Code Python experience is exactly as good as your Neovim Python experience — they're both talking to Pyright.

Here's the thing nobody talks about: AI coding assistants had the exact same problem that editors had before LSP. Without it, Claude Code does text search. Grep, Glob, Read. It works. But the cost is measured in seconds per query, multiplied by dozens of queries per task. It adds up fast.

LSP gives Claude Code two categories of superpowers: things that happen automatically and things it can actively request.

This is the most valuable part, and most people don't even realize it's happening. After every file edit, the language server pushes diagnostics: type errors, missing imports, undefined variables. Claude Code sees these immediately and fixes them in the same turn, before you ever see the error.

Think about what this means in practice. You ask Claude to add an email parameter to createUser(). Claude edits the function signature. The language server instantly reports 3 errors at three call sites that now have the wrong number of arguments. Claude sees the errors, finds all three call sites, and fixes them. You get the result with zero errors on the first try.

Without LSP, Claude would edit the function, hand you the result, you'd try to compile, see 3 errors, paste them back to Claude, and iterate. With LSP, that entire loop collapses into one step.

Beyond automatic diagnostics, Claude Code can explicitly ask the language server questions:

goToDefinition — "Where is processOrder defined?" → exact file and line findReferences — "Find all places that call validateUser" → every call site with location hover — "What type is the config variable?" → full type signature and docs documentSymbol — "List all functions in this file" → every symbol with location workspaceSymbol — "Find the PaymentService class" → search symbols across the entire project goToImplementation — "What classes implement AuthProvider?" → concrete implementations of interfaces incomingCalls / outgoingCalls — "What calls processPayment?" → full call hierarchy tracing

goToDefinition — "Where is processOrder defined?" → exact file and line

findReferences — "Find all places that call validateUser" → every call site with location

hover — "What type is the config variable?" → full type signature and docs

