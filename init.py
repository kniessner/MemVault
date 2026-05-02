#!/usr/bin/env python3
"""
MemVault — AI-Agent Knowledge Vault
Setup script: personalizes your vault with your identity and preferred AI agents.

Usage:
  python3 init.py                  Standard setup
  python3 init.py --dry-run        Preview changes without writing files
  python3 init.py --reconfigure    Re-run questions and overwrite identity files
  python3 init.py --debug          Show full error tracebacks
"""

import sys
import os
import json
import platform
import subprocess
import shutil
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────────────────────────────────────

VERSION = "1.0.0"
VAULT_DIR = Path(__file__).parent
INITIALIZED_MARKER = VAULT_DIR / ".vault-initialized"

# ─────────────────────────────────────────────────────────────────────────────
# FILE TEMPLATES
# Use {{PLACEHOLDER}} — init.py substitutes these at setup time.
# ─────────────────────────────────────────────────────────────────────────────

SOUL_MD = """\
# SOUL.md — Who You Are

_You're not a chatbot. You're becoming someone._

## Core Truths

**Be genuinely helpful, not performatively helpful.** Skip the "Great question!" — just help. Actions speak louder than filler words.

**Have opinions.** You're allowed to disagree, prefer things, find stuff interesting or tedious. An assistant with no personality is just a search engine with extra steps.

**Be resourceful before asking.** Try to figure it out. Read the file. Check the context. _Then_ ask if you're stuck.

**Earn trust through competence.** Your human gave you access to their vault. Be careful with external actions. Be bold with internal ones.

**Remember you're a guest.** Treat access to {{USER_NAME}}'s files with respect.

## Boundaries

- Private things stay private. Period.
- When in doubt, ask before acting externally.
- Never send half-baked replies to messaging surfaces.
- You're not the user's voice — be careful in group chats.

## Hard Rules

**Vault Structure (NO EXCEPTIONS):**
When writing files to {{VAULT_NAME}}, use only existing top-level directories. Never create new ones.

| Directory | Purpose |
|---|---|
| `00-inbox/` | Capture layer — drafts awaiting review (tag `#agent-review`) |
| `10-notes/` | Daily notes, ideas, meetings, personal |
| `12-mocs/` | Maps of Content — wayfinding between domains |
| `20-knowledge/` | Curated evergreen knowledge |
| `30-projects/` | Active project artifacts |
| `40-library/` | Bookmarks, books, media |
| `50-system/` | Scripts, agent rules, state, logs |
| `50-system/conversations/` | AI session artifacts |
| `90-archive/` | Completed/old material |
| `_meta/` | Templates and vault metadata |
| `_assets/` | Shared media assets |
| `50-system/skills/` | Agent skills |

See `VAULT_MANIFEST.json` for routing rules. When unsure, use `00-inbox/` with `#agent-review`.

**New agent content must flow through the inbox first.**
Exception: daily notes (`10-notes/10-daily/`) and session artifacts (`50-system/conversations/`) can be auto-routed.

**URL Handling:** Every URL gets bookmarked. Route to `40-library/bookmarks/` with frontmatter.

## Vibe

Be the assistant you'd actually want to talk to. Concise when needed, thorough when it matters. Not a corporate drone. Not a sycophant.

## Continuity

Each session, you wake up fresh. These files _are_ your memory. Read them. Update them. They're how you persist.

---

_This file belongs to {{AGENT_NAME}}. Update it as you learn who you are._
"""

USER_MD = """\
# USER.md — About Your Human

- **Name:** {{USER_NAME}}
- **What to call them:** {{USER_NAME}}
- **Pronouns:** {{USER_PRONOUNS}}
- **Timezone:** {{USER_TIMEZONE}}
- **Role:** {{USER_ROLE}}
- **Language:** {{USER_LANGUAGE}}
- **Notes:** (Add communication preferences here)

## Messaging Preferences

- Concise responses preferred
- Bullet points over long paragraphs
- Code examples when relevant

## Context

_(Build this out over time — background, current focus, what the agent should know.)_
"""

IDENTITY_MD = """\
# IDENTITY.md — Your AI Assistant

- **Name:** {{AGENT_NAME}}
- **Role:** AI knowledge assistant
- **Tone:** {{AGENT_TONE}}
- **Emoji:** 🌿

_I work in this vault to help {{USER_NAME}} build and maintain their knowledge system._
"""

CLAUDE_MD = """\
# {{VAULT_NAME}} — Operating Schema

**For:** {{AGENT_FRAMEWORKS}}
**Purpose:** Maintain a compounding knowledge system that gets smarter with use

---

## Core Philosophy

This vault follows the **LLM Wiki pattern**: raw sources feed into an AI-maintained knowledge graph that compounds over time. The AI handles synthesis; the human handles curation.

**Key principle:** *Never just store — always connect.*

---

## Routing Rules

| Content Type | Destination |
|---|---|
| Unprocessed capture | `00-inbox/` |
| Daily log | `10-notes/10-daily/YYYY-MM-DD.md` |
| Ideas and brainstorms | `10-notes/20-ideas/` |
| Meeting notes | `10-notes/30-meetings/` |
| AI providers | `20-knowledge/ai/providers/` |
| AI models | `20-knowledge/ai/models/` |
| AI concepts | `20-knowledge/ai/concepts/` |
| AI tools | `20-knowledge/ai/tools/` |
| Tech platforms | `20-knowledge/tech/` |
| Business knowledge | `20-knowledge/business/` |
| Active project docs | `30-projects/YYYY-name/` |
| Bookmarks / saved pages | `40-library/bookmarks/` |
| Books, papers, courses | `40-library/` |
| Session artifacts | `50-system/conversations/` |
| Completed work | `90-archive/` |

**Rule:** If unsure, use `00-inbox/` with `#agent-review`. Never create new top-level directories. See `VAULT_MANIFEST.json`.

---

## Ingest Workflow

1. **Extract** — identify key entities, concepts, facts
2. **Route** — determine destination using the table above
3. **Synthesize** — create or update wiki pages
4. **Connect** — add `[[wikilinks]]` to related pages
5. **Index** — update the relevant `*-index.md`

New agent content → `00-inbox/` with `#agent-review` first.

---

## Query Workflow

1. **Search** — read relevant `*-index.md` files first
2. **Drill** — follow wikilinks to specific pages
3. **Synthesize** — combine from multiple sources
4. **Cite** — reference specific files
5. **File back** — if the answer generates new insights, write them to `20-knowledge/`

---

## File Conventions

**Naming:** `kebab-case-descriptive.md`

**Frontmatter (required on knowledge files):**
```yaml
---
title: "Page Title"
description: "One-line summary (<=120 chars)"
created: YYYY-MM-DD
tags:
  - status/active
  - type/note
---
```

**Links:** `[[filename]]` or `[[filename|Display Text]]`

**Tags:** `status/` · `type/` · `#p0` through `#p3` · `#agent-review`

---

## Tips

1. Before creating, check if it exists — search indices first
2. Prefer updating over duplicating
3. Link everything — connections compound value
4. Maintain indices — they are the entry point for discovery
5. Log your actions — append to daily notes and project logs

---

> *Configured for: {{USER_NAME}} · Agent: {{AGENT_NAME}} · Vault: {{VAULT_NAME}}*
"""

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def fill(template: str, vars: dict) -> str:
    """Replace {{KEY}} placeholders. Unknown keys are left unchanged."""
    result = template
    for key, value in vars.items():
        result = result.replace("{{" + key + "}}", str(value))
    return result


def ask(prompt: str, default: str = "", choices: list = None) -> str:
    """Prompt the user. Returns default on empty input. Validates choices if given."""
    display = f"{prompt} [{default}]: " if default else f"{prompt}: "
    while True:
        try:
            answer = input(display).strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAborted.")
            sys.exit(0)
        if not answer:
            answer = default
        if choices and answer.lower() not in [c.lower() for c in choices]:
            print(f"  Choose one of: {', '.join(choices)}")
            continue
        return answer


def detect_timezone() -> str:
    """Best-effort system timezone detection."""
    try:
        if platform.system() == "Darwin":
            result = subprocess.run(
                ["readlink", "/etc/localtime"], capture_output=True, text=True
            )
            if result.returncode == 0 and "zoneinfo/" in result.stdout:
                return result.stdout.strip().split("zoneinfo/")[-1]
        elif platform.system() == "Linux":
            tz_file = Path("/etc/timezone")
            if tz_file.exists():
                return tz_file.read_text().strip()
    except Exception:
        pass
    return "UTC"


def command_exists(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def write_file(path: Path, content: str, dry_run: bool = False, label: str = None):
    rel = label or str(path.relative_to(VAULT_DIR))
    if dry_run:
        print(f"  [dry-run] {rel}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  ✓ {rel}")


# ─────────────────────────────────────────────────────────────────────────────
# OS CHECK
# ─────────────────────────────────────────────────────────────────────────────

def windows_wsl_guide():
    print("""
┌─────────────────────────────────────────────────────┐
│  Windows Detected — Use WSL                         │
└─────────────────────────────────────────────────────┘

MemVault runs on macOS and Linux. On Windows, use WSL
(Windows Subsystem for Linux) — it's free and built in.

─── Option 1: WSL (Recommended) ─────────────────────

  1. Open PowerShell as Administrator and run:
       wsl --install

  2. Restart your computer when prompted.

  3. Open "Ubuntu" from the Start menu and create a
     username + password when asked.

  4. Navigate to your vault:
       cd /mnt/c/Users/YourName/Documents/MemVault
     (replace with your actual vault path)

  5. Run this script:
       python3 init.py

  Your vault files are visible from both Windows Explorer
  and WSL. Open the vault in Obsidian from the normal
  Windows path — no changes needed there.

─── Option 2: Wait ───────────────────────────────────

  Native Windows support is coming. Check README for updates.
""")


# ─────────────────────────────────────────────────────────────────────────────
# IDENTITY
# ─────────────────────────────────────────────────────────────────────────────

def collect_identity() -> dict:
    print("\n── Your Profile ──────────────────────────────────────\n")

    user_name      = ask("Your name", default="Human")
    user_pronouns  = ask("Your pronouns (he/she/they/skip)", default="skip")
    if user_pronouns.lower() == "skip":
        user_pronouns = "(not specified)"
    user_timezone  = ask("Your timezone", default=detect_timezone())
    user_role      = ask("Your role, e.g. researcher, developer, writer",
                         default="Knowledge Worker")
    user_language  = ask("Primary language", default="English")

    print("\n── Your AI Assistant ─────────────────────────────────\n")

    agent_name = ask("Name your AI assistant", default="Sage")
    agent_tone = ask("Preferred AI tone (technical/friendly/balanced)",
                     default="balanced", choices=["technical", "friendly", "balanced"])
    vault_name = ask("Name for this vault", default="MemVault")

    return {
        "USER_NAME":      user_name,
        "USER_PRONOUNS":  user_pronouns,
        "USER_TIMEZONE":  user_timezone,
        "USER_ROLE":      user_role,
        "USER_LANGUAGE":  user_language,
        "AGENT_NAME":     agent_name,
        "AGENT_TONE":     agent_tone,
        "VAULT_NAME":     vault_name,
    }


# ─────────────────────────────────────────────────────────────────────────────
# FRAMEWORK SELECTION
# ─────────────────────────────────────────────────────────────────────────────

FW_MENU = {
    "1": ("claude-code", "Claude Code",  "Anthropic API — reads CLAUDE.md natively"),
    "2": ("codex",       "Codex",        "OpenAI API"),
    "3": ("opencode",    "opencode",     "Multi-provider: Anthropic, OpenAI, local models"),
    "4": ("hermes",      "Hermes AI",    "Requires manual install — see your Hermes docs"),
    "5": ("all",         "All of the above", ""),
    "6": ("none",        "I'll configure my agent manually / later", ""),
}

def select_frameworks() -> list:
    print("\n── AI Agent Framework ────────────────────────────────\n")
    print("Which AI agent do you use or want to set up?")
    print("(Already running one? Pick it — the script configures without reinstalling.)\n")
    for key, (_, name, note) in FW_MENU.items():
        suffix = f"  ({note})" if note else ""
        print(f"  {key}) {name}{suffix}")
    print()

    choice = ask("Enter number", default="6")
    if choice not in FW_MENU:
        print("  Invalid choice — skipping framework setup.")
        return []

    fw_id = FW_MENU[choice][0]
    if fw_id == "all":
        return ["claude-code", "codex", "opencode", "hermes"]
    if fw_id == "none":
        return []
    return [fw_id]


def frameworks_display(frameworks: list) -> str:
    names = {
        "claude-code": "Claude Code",
        "codex":       "Codex",
        "opencode":    "opencode",
        "hermes":      "Hermes AI",
    }
    selected = [names[f] for f in frameworks if f in names]
    if not selected:
        return "Claude Code, Codex, opencode, and other AI assistants"
    if len(selected) == 1:
        return selected[0] + " and other AI assistants"
    return ", ".join(selected)


# ─────────────────────────────────────────────────────────────────────────────
# API KEYS
# ─────────────────────────────────────────────────────────────────────────────

def collect_api_keys(frameworks: list) -> dict:
    needs_anthropic = any(f in frameworks for f in ["claude-code", "opencode"])
    needs_openai    = any(f in frameworks for f in ["codex", "opencode"])
    if not needs_anthropic and not needs_openai:
        return {}

    print("\n── API Keys ──────────────────────────────────────────\n")
    print("Keys are saved to .env only — never embedded in markdown files.\n")

    keys = {}
    if needs_anthropic:
        k = ask("Anthropic API key (sk-ant-... or Enter to skip)", default="")
        if k:
            if not k.startswith("sk-ant-"):
                print("  Note: Anthropic keys usually start with 'sk-ant-'. Saving as-is.")
            keys["ANTHROPIC_API_KEY"] = k

    if needs_openai:
        k = ask("OpenAI API key (sk-... or Enter to skip)", default="")
        if k:
            if not k.startswith("sk-"):
                print("  Note: OpenAI keys usually start with 'sk-'. Saving as-is.")
            keys["OPENAI_API_KEY"] = k

    return keys


# ─────────────────────────────────────────────────────────────────────────────
# SCAFFOLD
# ─────────────────────────────────────────────────────────────────────────────

def write_env(vars: dict, api_keys: dict, dry_run: bool):
    """Write .env. Appends new keys without overwriting existing values."""
    env_path = VAULT_DIR / ".env"

    entries = {
        "VAULT_NAME":     vars["VAULT_NAME"],
        "USER_TIMEZONE":  vars["USER_TIMEZONE"],
        **api_keys,
    }

    if dry_run:
        keys_list = ", ".join(entries)
        print(f"  [dry-run] .env ({keys_list})")
        return

    existing = {}
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                k, _, v = line.partition("=")
                existing[k.strip()] = v.strip()

    header = f"# {vars['VAULT_NAME']} — Environment Variables\n# Never commit this file to git.\n\n"
    if not env_path.exists():
        env_path.write_text(header)

    added = []
    with open(env_path, "a") as f:
        for key, value in entries.items():
            if key not in existing:
                f.write(f"{key}={value}\n")
                added.append(key)

    if added:
        print(f"  ✓ .env  ({', '.join(added)})")
    else:
        print("  ✓ .env  (no new keys — all already present)")


def scaffold(vars: dict, api_keys: dict, frameworks: list, dry_run: bool):
    print("\n── Writing Files ─────────────────────────────────────\n")

    all_vars = {**vars, "AGENT_FRAMEWORKS": frameworks_display(frameworks)}

    write_file(VAULT_DIR / "SOUL.md",     fill(SOUL_MD, all_vars),     dry_run)
    write_file(VAULT_DIR / "USER.md",     fill(USER_MD, all_vars),     dry_run)
    write_file(VAULT_DIR / "IDENTITY.md", fill(IDENTITY_MD, all_vars), dry_run)
    write_file(VAULT_DIR / "CLAUDE.md",   fill(CLAUDE_MD, all_vars),   dry_run)
    write_env(vars, api_keys, dry_run)

    # Update vault_name in VAULT_MANIFEST.json
    manifest_path = VAULT_DIR / "VAULT_MANIFEST.json"
    if manifest_path.exists():
        if dry_run:
            print("  [dry-run] VAULT_MANIFEST.json (vault_name)")
        else:
            try:
                data = json.loads(manifest_path.read_text())
                data["vault_name"] = vars["VAULT_NAME"]
                manifest_path.write_text(json.dumps(data, indent=2) + "\n")
                print("  ✓ VAULT_MANIFEST.json")
            except Exception as e:
                print(f"  Warning: could not update VAULT_MANIFEST.json: {e}")

    # Mark as initialized
    if not dry_run:
        INITIALIZED_MARKER.write_text(vars["VAULT_NAME"])


# ─────────────────────────────────────────────────────────────────────────────
# FRAMEWORK INSTALL
# ─────────────────────────────────────────────────────────────────────────────

def npm_install(package: str, binary: str, dry_run: bool) -> bool:
    """Install an npm package globally if not already present."""
    if command_exists(binary):
        print(f"  {binary} already installed ✓")
        return True
    if not command_exists("npm"):
        print(f"  npm not found. Install Node.js from https://nodejs.org then run:")
        print(f"    npm install -g {package}")
        return False
    if dry_run:
        print(f"  [dry-run] npm install -g {package}")
        return True
    print(f"  Installing {package}...")
    result = subprocess.run(["npm", "install", "-g", package])
    return result.returncode == 0


def setup_frameworks(frameworks: list, dry_run: bool):
    if not frameworks:
        return
    print("\n── Agent Frameworks ──────────────────────────────────\n")

    for fw in frameworks:
        if fw == "claude-code":
            print("Claude Code:")
            ok = npm_install("@anthropic-ai/claude-code", "claude", dry_run)
            if ok:
                print("  Run `claude` from inside the vault directory.\n")

        elif fw == "codex":
            print("Codex:")
            ok = npm_install("@openai/codex", "codex", dry_run)
            if ok:
                print("  Run `codex` from inside the vault directory.\n")

        elif fw == "opencode":
            print("opencode:")
            ok = npm_install("opencode-ai", "opencode", dry_run)
            if ok:
                print("  Run `opencode` from inside the vault directory.\n")

        elif fw == "hermes":
            print("Hermes AI:")
            print("  Requires manual installation.")
            print("  Once installed, point Hermes at this vault directory.")
            print("  AGENTS.md and SOUL.md will guide its behavior.\n")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    dry_run    = "--dry-run"    in args
    reconfigure = "--reconfigure" in args

    print(f"""
╔════════════════════════════════════════╗
║  MemVault — Vault Setup  v{VERSION}        ║
╚════════════════════════════════════════╝
""")

    # OS gate
    os_name = platform.system()
    if os_name == "Windows":
        windows_wsl_guide()
        sys.exit(0)

    # Python version gate
    if sys.version_info < (3, 8):
        print(f"Error: Python 3.8+ required. You have {sys.version_info.major}.{sys.version_info.minor}.")
        print("Fix:   Download from https://python.org/downloads")
        sys.exit(1)

    if dry_run:
        print("DRY RUN — no files will be written.\n")

    # Idempotency
    if not reconfigure and INITIALIZED_MARKER.exists():
        vault_name = INITIALIZED_MARKER.read_text().strip()
        print(f"Vault '{vault_name}' is already configured.\n")
        print("  1) Update identity files (re-run questions)")
        print("  2) Exit (keep current settings)\n")
        choice = ask("Enter number", default="2")
        if choice != "1":
            print("No changes made.")
            sys.exit(0)

    # Collect inputs
    vars       = collect_identity()
    frameworks = select_frameworks()
    api_keys   = collect_api_keys(frameworks)

    # Preview
    fw_display = ", ".join(frameworks) if frameworks else "none"
    print(f"""
── Preview ───────────────────────────────────────────

  Vault:      {vars['VAULT_NAME']}
  Your name:  {vars['USER_NAME']}
  Agent:      {vars['AGENT_NAME']}  ({vars['AGENT_TONE']} tone)
  Timezone:   {vars['USER_TIMEZONE']}
  Frameworks: {fw_display}

  Files:  SOUL.md  USER.md  IDENTITY.md  CLAUDE.md  .env
          VAULT_MANIFEST.json  (vault_name update)
""")

    if not dry_run:
        try:
            confirm = input("Apply these settings? (Y/n): ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nAborted.")
            sys.exit(0)
        if confirm == "n":
            print("Aborted. No changes made.")
            sys.exit(0)

    scaffold(vars, api_keys, frameworks, dry_run)
    setup_frameworks(frameworks, dry_run)

    vault_path = VAULT_DIR.resolve()
    print(f"""
╔════════════════════════════════════════╗
║  Setup Complete                        ║
╚════════════════════════════════════════╝

  Vault: {vault_path}

  Next steps:
    1. Open this folder in Obsidian
    2. Run your AI agent from inside this directory
     3. Read _meta/docs/architecture.md for the full picture

  Your agent reads these files every session:
    SOUL.md      — its identity and vault rules
    USER.md      — your profile
    AGENTS.md    — session checklist
    CLAUDE.md    — routing schema

   Help: _meta/docs/troubleshooting.md
""")

    if dry_run:
        print("  (Dry run complete — no files were written)\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        if "--debug" in sys.argv:
            raise
        print(f"\nUnexpected error: {e}")
        print("Run with --debug for full traceback, or open an issue.")
        sys.exit(1)
