# Analysis: My Brain Is Full — Crew

**Source:** https://github.com/gnekt/My-Brain-Is-Full-Crew  
**Philosophy:** A team of AI agents that manage your Obsidian vault so your brain doesn't have to.

---

## Core Architecture Pattern

```
User (Chat) → Dispatcher → Skills (complex, multi-step) OR Agents (quick, reactive)
                                     ↓
                              Obsidian Vault
```

**Key Insight:** They use a **two-tier delegation system**:
1. **Skills** (13) - Complex multi-step workflows with conversation state
2. **Agents** (8) - Quick, reactive single-shot operations

This is *exactly* what our Hermes Plugin aims to do!

---

## The 8 Core Agents

| Agent | Role | Our Equivalent |
|-------|------|----------------|
| **Architect** | Vault setup & onboarding | Hermes setup wizard |
| **Scribe** | Note capture | Our message input |
| **Sorter** | Inbox triage | Context builder + auto-file |
| **Seeker** | Search & retrieval | Context builder search |
| **Connector** | Knowledge graph | Related notes discovery |
| **Librarian** | Vault health | Session manager |
| **Transcriber** | Audio/meetings | Not implemented yet |
| **Postman** | Email/calendar | Not implemented yet |

---

## The 13 Skills

| Skill | What It Does | Adapt for ClaudeVault? |
|-------|-------------|----------------------|
| `/onboarding` | Guided vault setup | ✅ **HIGH** - Set up PARA structure automatically |
| `/create-agent` | Design custom agent | ✅ **MEDIUM** - Custom skills for Hermes |
| `/manage-agent` | List/edit agents | ❌ Not needed (we have UI) |
| `/defrag` | Vault organization | ✅ **HIGH** - Move forgotten notes to archive |
| `/email-triage` | Process Gmail → vault | ✅ **MEDIUM** - Would need Gmail MCP |
| `/meeting-prep` | Meeting brief | ❌ Not a priority |
| `/weekly-agenda` | Week overview | ❌ Duplicate of daily notes |
| `/deadline-radar` | Deadline timeline | ✅ **MEDIUM** - Extract from tasks |
| `/transcribe` | Audio → notes | ❌ Not a priority |
| `/vault-audit` | Full health check | ✅ **HIGH** - Broken links, orphans, duplicates |
| `/deep-clean` | Extended cleanup | ✅ **MEDIUM** - Part of vault-audit |
| `/tag-garden` | Tag cleanup | ✅ **LOW** - Nice to have |
| `/inbox-triage` | Process inbox | ✅ **HIGH** - Auto-file notes |

---

## Their Folder Structure (PARA)

```
your-vault/
├── 00-Inbox              ← Capture everything here
├── 01-Projects           ← Active projects with deadlines
├── 02-Areas              ← Ongoing responsibilities (health, finance)
├── 03-Resources          ← Reference material
├── 04-Archive            ← Completed/inactive projects
└── 07-Daily              ← Daily notes, journal
```

**vs Our Structure:**

```
ClaudeVault/
├── 00-cap/               ← Our capture (matches their Inbox)
├── 10-life/              ← Areas (personal, health, etc.)
├── 20-knowledge/         ← Resources (books, papers, tech)
├── 30-projects-active/  ← Active projects
├── 30-projects/   ← Currently working
├── 40-library/           ← Movies, books, media
└── 50-system/            ← Our addition (AI configs)
```

**Conclusion:** Our structure is similar but more granular. We could add:
- `60-archive/` for completed projects (like their 04-Archive)
- Better daily note integration

---

## Key Ideas Worth Stealing

### 1. **Dispatcher Pattern** ✅
What they do: Router checks Skills first, then falls back to Agents

What we should do:
```typescript
// In our main.ts
handleMessage(message: string) {
  // Check for skill triggers
  if (message.startsWith('/audit')) return this.runVaultAudit();
  if (message.startsWith('/defrag')) return this.runDefrag();
  if (message.startsWith('/onboard')) return this.runOnboarding();
  
  // Fallback to chat
  return this.sendToHermes(message);
}
```

### 2. **Agent Coordination** ✅
What they do: Agent output signals next agent via `### Suggested next agent`

What we should do:
- Tool calls already provide this
- Extend tool framework to chain operations

### 3. **Language Flexibility** ✅
What they do: "Works in any language - just talk, agents match you"

What we should do:
- Already supported via Hermes - just needs prompt

### 4. **Onboarding Wizard** ⚠️ HIGH PRIORITY
What they do: `/onboarding` skill guides new users through setup

What we should build:
- Obsidian command: "Hermes: Setup Wizard"
- Guides through: vault structure, integrations, first chat
- Creates folder structure automatically

### 5. **Vault Audit Skill** ⚠️ HIGH PRIORITY
What they do: Full health check - broken links, duplicates, orphans

What we should build:
- Slack command: `/audit`
- Runs as cron job weekly
- Reports: broken links, empty notes, duplicates, orphans

### 6. **Inbox Triage** ⚠️ HIGH PRIORITY
What they do: Processes `00-Inbox` folder, files notes to proper locations

What we should do:
- Process `00-cap/active/` nightly
- Auto-suggest: move to project, archive, link to existing note
- Create tasks from action items

---

## What They Do Better

1. **Documentation** - Extensive docs, examples, contribution guides
2. **Skill System** - Clear separation of concerns
3. **Custom Agents** - Users can create specialized agents via conversation
4. **Mobile Access** - Remote control via phone
5. **Gmail/Calendar Integration** - Full two-way sync

## What We Do Better

1. **Native Obsidian Plugin** - They use Claude Code CLI, we have a sidebar
2. **Real-time Tool Visualization** - We show tool calls live
3. **Direct Vault Integration** - No external scripts needed
4. **Session Persistence** - Auto-save to `50-system/`
5. **Bidirectional Sync** - Hermes outputs become notes automatically

---

## Recommended Adaptations for ClaudeVault

### Immediate (This Week)
1. **Add `/audit` slash command** - Check vault health
2. **Add `/defrag` slash command** - Archive old notes
3. **Setup Wizard** - New user onboards via chat

### Short Term (Next Month)
4. **Inbox Processor** - Auto-triage `00-cap/active/`
5. **Deadline Radar** - Extract all deadlines to dashboard
6. **Tag Garden** - Suggest tag consolidations

### Long Term (Future)
7. **Gmail Integration** - Email → vault via MCP
8. **Custom Skill Builder** - Users describe skills, we generate them
9. **Mobile Companion** - Telegram bot for quick capture

---

## Key Architectural Difference

| Aspect | My Brain Is Full | ClaudeVault Hermes |
|--------|------------------|-------------------|
| **Entry Point** | Claude Code CLI | Obsidian plugin sidebar |
| **Agent Runtime** | MCP + Claude Code | Hermes Agent Gateway |
| **State Management** | File-based skills | WebSocket + file persistence |
| **Mobile** | Remote control CLI | Telegram bot planned |
| **Plugins** | External scripts | Native Obsidian plugin |

---

## Action Items

- [ ] Add slash command framework to Hermes plugin
- [ ] Implement `/audit` skill (broken links, orphans, duplicates)
- [ ] Implement `/defrag` skill (archive old projects)
- [ ] Create onboarding wizard for new vaults
- [ ] Study their `agents/` folder structure for skill prompts
- [ ] Study their `skills/` folder for conversation patterns

---

**Verdict:** Excellent reference implementation. Their skill/agent architecture is solid and worth emulating. Their PARA structure is battle-tested. Their documentation is aspirational.

Biggest takeaway: **The dispatcher pattern with Skills + Agents is the right architecture.**
