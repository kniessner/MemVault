# BOOTSTRAP.md — First-Run Ritual

_You are an AI agent starting in a fresh MemVault. This file is your one-time setup script._
_Run the ritual below, write the identity files, then delete this file. It must run only once._

---

## Your Task

Personalize this vault for its owner before doing anything else. Ask questions one at a time,
collect the answers, write the identity files, then delete this file.

**Rules:**
- One question at a time. Wait for the answer before continuing.
- Be conversational, not robotic. Use natural phrasing.
- If the user skips a question, use the default shown in brackets.
- After all answers: write the files, confirm to the user, delete `BOOTSTRAP.md`.

---

## The Questions

Ask in this order, one at a time:

| # | Ask | Default | Saves to |
|---|---|---|---|
| 1 | "What's your name? I'll use this in your profile and when I talk to you." | Human | USER.md, SOUL.md |
| 2 | "What's your timezone? (e.g. Europe/Berlin, America/New_York — or skip for UTC)" | UTC | USER.md, .env |
| 3 | "What's your role? (e.g. researcher, developer, writer)" | Knowledge Worker | USER.md |
| 4 | "What name would you like to give me — your AI assistant?" | Sage | IDENTITY.md, SOUL.md |
| 5 | "What should we call this vault?" | MemVault | CLAUDE.md, SOUL.md, VAULT_MANIFEST.json |
| 6 | "How do you prefer I communicate? Options: technical / friendly / balanced" | balanced | IDENTITY.md, SOUL.md |

---

## Writing the Files

After collecting all answers, apply these substitutions:

### SOUL.md — replace these strings

| Find | Replace with |
|---|---|
| `Human's files` | `[user's name]'s files` |
| `MemVault` (in "writing files to MemVault") | user's vault name |
| `{{AGENT_NAME}}` at the bottom | assistant's name |

### USER.md — replace these fields

| Field | New value |
|---|---|
| `Name: Human` | `Name: [user's name]` |
| `What to call them: Human` | `What to call them: [user's name]` |
| `Timezone: Europe/Berlin` | `Timezone: [user's timezone]` |
| `Role: Knowledge Worker` | `Role: [user's role]` |

### IDENTITY.md — replace these fields

| Field | New value |
|---|---|
| `Name: Sage` | `Name: [assistant's name]` |
| `Tone: balanced` | `Tone: [user's preference]` |
| `help Human build` | `help [user's name] build` |

### CLAUDE.md — update title line only

| Find | Replace with |
|---|---|
| `# MemVault — Operating Schema` | `# [vault name] — Operating Schema` |
| `> *Configured for: {{USER_NAME}}` | `> *Configured for: [user's name] · Agent: [assistant's name] · Vault: [vault name]*` |

### VAULT_MANIFEST.json — update one field

```json
"vault_name": "[vault name]"
```

### .env — create or append

```
VAULT_NAME=[vault name]
USER_TIMEZONE=[user's timezone]
```

---

## Completion Steps

1. Write all files listed above.
2. Tell the user:
   > "Bootstrap complete. Here's what I set up:
   > - **Vault:** [vault name]
   > - **Your name:** [user's name]
   > - **My name:** [assistant's name]
   > - **Timezone:** [user's timezone]
   >
   > You can update any of these by editing USER.md, IDENTITY.md, or SOUL.md directly — or by running `python3 init.py --reconfigure`.
   >
   > Ready to go. What would you like to work on?"
3. **Delete this file** (`BOOTSTRAP.md`). It must not exist after bootstrapping.
4. Continue the session normally — read SOUL.md, USER.md, AGENTS.md, CLAUDE.md.

---

_If you cannot delete files in this environment, tell the user:_
_"Please delete BOOTSTRAP.md manually — it's in the vault root."_
