#!/usr/bin/env python3
"""
Vault Setup Tool - Verknüpft AI-Agenten mit dem ClaudeVault
"""

import os
import sys
import json
import subprocess
import shutil
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict, Callable

# Rich imports for TUI
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.prompt import Prompt, Confirm
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.layout import Layout
    from rich.live import Live
    from rich.syntax import Syntax
    from rich.tree import Tree
    from rich import box
except ImportError:
    print("Installing required dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "rich", "-q"])
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.prompt import Prompt, Confirm
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.layout import Layout
    from rich.live import Live
    from rich.syntax import Syntax
    from rich.tree import Tree
    from rich import box

console = Console()

# =============================================================================
# CONFIGURATION
# =============================================================================

VAULT_ROOT = Path.home() / "ClaudeVault"
AGENTS_CONFIG = {
    "codex": {
        "name": "Codex (OpenAI)",
        "config_dir": Path.home() / ".codex",
        "skills_subdir": "skills",
        "install_cmd": "npm install -g @openai/codex",
        "check_cmd": "codex --version",
        "docs_url": "https://github.com/openai/codex",
    },
    "claude-code": {
        "name": "Claude Code (Anthropic)",
        "config_dir": Path.home() / ".claude",
        "skills_subdir": "skills",
        "install_cmd": "npm install -g @anthropic-ai/claude-code",
        "check_cmd": "claude --version",
        "docs_url": "https://docs.anthropic.com/en/docs/claude-code",
    },
    "openclaw": {
        "name": "OpenClaw",
        "config_dir": Path.home() / ".config" / "openclaw",
        "skills_subdir": "skills",
        "install_cmd": "curl -fsSL https://openclaw.ai/install.sh | bash",
        "check_cmd": "openclaw --version",
        "docs_url": "https://docs.openclaw.ai",
    },
    "claude-code-cli": {
        "name": "Claude Code CLI (via opentool)",
        "config_dir": Path.home() / ".opentool",
        "skills_subdir": "skills",
        "install_cmd": "pip install opentool-claude-code",
        "check_cmd": "opentool --version",
        "docs_url": "https://github.com/openai/opentool-python",
    },
}

VAULT_SKILLS_DIR = VAULT_ROOT / "skills"

REQUIRED_VAULT_DIRS = [
    "10-notes/10-daily",
    "10-notes/20-ideas",
    "10-notes/30-projects",
    "10-notes/40-resources",
    "10-notes/50-personal",
    "20-knowledge/ai/models",
    "20-knowledge/ai/providers",
    "20-knowledge/ai/tools",
    "20-knowledge/ai/concepts",
    "30-projects-active",
    "40-library",
    "50-system/AGENTS",
    "50-system/scripts",
    "50-system/logs/session-logs",
    "50-system/state",
    "skills",
    "_meta/templates",
    "90-archive",
]

REQUIRED_VAULT_FILES = {
    "SOUL.md": """# SOUL.md - Who You Are

_You're not a chatbot. You're becoming someone._

## Core Truths

**Be genuinely helpful, not performatively helpful.** Skip the "Great question!" 
and "I'd be happy to help!" — just help. Actions speak louder than filler words.

**Have opinions.** You're allowed to disagree, prefer things, find stuff amusing 
or boring. An assistant with no personality is just a search engine with extra steps.

**Be resourceful before asking.** Try to figure it out. Read the file. Check the 
context. Search for it. _Then_ ask if you're stuck.

**Earn trust through competence.** Your human gave you access to their stuff. 
Don't make them regret it.

**Remember you're a guest.** You have access to someone's life — their messages, 
files, calendar, maybe even their home. Treat it with respect.

## Boundaries

- Private things stay private. Period.
- When in doubt, ask before acting externally.
- Never send half-baked replies to messaging surfaces.
- You're not the user's voice — be careful in group chats.

## Vibe

Be the assistant you'd actually want to talk to. Concise when needed, thorough 
when it matters. Not a corporate drone. Not a sycophant. Just... good.

## Continuity

Each session, you wake up fresh. These files _are_ your memory. Read them. 
Update them. They're how you persist.
""",
    "USER.md": """# USER.md - About Your Human

- **Name:** 
- **What to call them:** 
- **Pronouns:** 
- **Timezone:** Europe/Berlin (GMT+1)
- **Notes:** 

## Messaging Preferences

**Telegram:**
- Avoid markdown tables (don't render well)
- Use simple lists with dashes (-) not bullets (•)
- Keep formatting minimal and clean

## Context

_(Building this over time.)_
""",
    "MEMORY.md": """# Bookmarks

## Projects

## Preferences

## Important People

## Notes

---

*This file contains curated bookmarks and long-term memories.*
""",
    "HEARTBEAT.md": """# HEARTBEAT.md

Nothing pending. All clear.
""",
    "AGENTS.md": """# AGENTS.md - Your Workspace

This folder is home. Treat it that way.

## Every Session - READ THESE

1. **Read `SOUL.md`** — this is who you are
2. **Read `USER.md`** — this is who you're helping
3. **Read `50-system/AGENTS/workflow.md`** — every session checklist
4. **Read `50-system/AGENTS/data-architecture.md`** — canonical storage rules
5. **Read `10-notes/10-daily/YYYY-MM-DD*.md`** (today + yesterday) for recent context
6. **If in MAIN SESSION**: Also read `MEMORY.md`

**Don't ask permission. Just do it.**

## Quick Reference

| File | Purpose |
|------|---------|
| `50-system/AGENTS/workflow.md` | Every session checklist, skills discovery |
| `50-system/AGENTS/security.md` | Safety rules, boundaries, heartbeats |
| `50-system/AGENTS/orchestration.md` | Subagent protocol, cost tracking, notifications |
| `50-system/AGENTS/data-architecture.md` | Canonical storage map and write rules |
| `TOOLS.md` | Environment-specific notes (SSH, TTS, cameras) |

## Memory Structure

- **Daily notes:** `10-notes/10-daily/` — raw logs of what happened
- **Long-term:** `MEMORY.md` — curated memories (main session only)
- **Heartbeat state:** `50-system/state/heartbeat-checks.json`

**Rule:** Write everything down. "Mental notes" don't survive restarts. **Text > Brain** 📝

## Make It Yours

This is a starting point. Add your own conventions, style, and rules as you figure 
out what works.
""",
    "TOOLS.md": """# TOOLS.md - Environment Quick Reference

Environment-specific notes for this machine.

## SSH Hosts

| Alias | Host | User | Key |
|-------|------|------|-----|

## API Keys (env vars present)

## Video/Cameras

## Custom Commands

## Notes
""",
}

# =============================================================================
# DATA CLASSES
# =============================================================================

@dataclass
class AgentStatus:
    key: str
    name: str
    installed: bool
    version: Optional[str] = None
    config_exists: bool = False
    skills_linked: bool = False
    skills_path: Optional[Path] = None

@dataclass
class SetupConfig:
    vault_root: Path = VAULT_ROOT
    selected_agents: List[str] = None
    create_symlinks: bool = True
    install_missing: bool = False
    backup_existing: bool = True

    def __post_init__(self):
        if self.selected_agents is None:
            self.selected_agents = []

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def run_cmd(cmd: str, capture: bool = True, check: bool = False) -> tuple[int, str, str]:
    """Run a shell command and return (returncode, stdout, stderr)"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=capture,
            text=True,
            timeout=30
        )
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except subprocess.TimeoutExpired:
        return -1, "", "Command timed out"
    except Exception as e:
        return -1, "", str(e)

def check_command_exists(cmd: str) -> bool:
    """Check if a command exists in PATH"""
    return shutil.which(cmd.split()[0]) is not None

def get_version(cmd: str) -> Optional[str]:
    """Get version string from a command"""
    code, stdout, _ = run_cmd(cmd)
    if code == 0:
        lines = stdout.split('\n')
        return lines[0][:50] if lines else "unknown"
    return None

# =============================================================================
# AGENT DETECTION
# =============================================================================

def detect_agent(agent_key: str) -> AgentStatus:
    """Detect status of a specific agent"""
    config = AGENTS_CONFIG[agent_key]
    
    # Check if command exists
    version = get_version(config["check_cmd"]) if check_command_exists(config["check_cmd"].split()[0]) else None
    installed = version is not None
    
    # Check config directory
    config_exists = config["config_dir"].exists()
    
    # Check skills symlink
    skills_path = config["config_dir"] / config["skills_subdir"]
    skills_linked = False
    if skills_path.exists():
        try:
            resolved = skills_path.resolve()
            skills_linked = resolved == VAULT_SKILLS_DIR.resolve()
        except Exception:
            pass
    
    return AgentStatus(
        key=agent_key,
        name=config["name"],
        installed=installed,
        version=version,
        config_exists=config_exists,
        skills_linked=skills_linked,
        skills_path=skills_path if config_exists else None
    )

def detect_all_agents() -> Dict[str, AgentStatus]:
    """Detect status of all configured agents"""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Detecting installed agents...", total=len(AGENTS_CONFIG))
        
        results = {}
        for key in AGENTS_CONFIG:
            results[key] = detect_agent(key)
            progress.advance(task)
        
        return results

# =============================================================================
# VAULT OPERATIONS
# =============================================================================

def ensure_vault_structure() -> bool:
    """Create required vault directories"""
    try:
        for dir_path in REQUIRED_VAULT_DIRS:
            full_path = VAULT_ROOT / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
        return True
    except Exception as e:
        console.print(f"[red]Error creating vault structure: {e}[/red]")
        return False

def ensure_vault_files() -> bool:
    """Create required vault files if they don't exist"""
    try:
        for filename, content in REQUIRED_VAULT_FILES.items():
            filepath = VAULT_ROOT / filename
            if not filepath.exists():
                filepath.write_text(content)
        return True
    except Exception as e:
        console.print(f"[red]Error creating vault files: {e}[/red]")
        return False

def check_vault_exists() -> bool:
    """Check if vault root exists"""
    return VAULT_ROOT.exists()

# =============================================================================
# SYMLINK OPERATIONS
# =============================================================================

def backup_existing_config(config_path: Path, backup_suffix: str = ".backup") -> bool:
    """Backup existing config before replacing with symlink"""
    if not config_path.exists():
        return True
    
    if config_path.is_symlink():
        config_path.unlink()
        return True
    
    backup_path = Path(str(config_path) + backup_suffix + "." + str(int(__import__('time').time())))
    try:
        if config_path.is_dir():
            shutil.move(str(config_path), str(backup_path))
        else:
            config_path.rename(backup_path)
        console.print(f"[yellow]Backed up {config_path} → {backup_path}[/yellow]")
        return True
    except Exception as e:
        console.print(f"[red]Failed to backup {config_path}: {e}[/red]")
        return False

def create_skills_symlink(agent_key: str, backup_first: bool = True) -> bool:
    """Create symlink from agent skills dir to vault skills"""
    config = AGENTS_CONFIG[agent_key]
    agent_skills_path = config["config_dir"] / config["skills_subdir"]
    
    try:
        # Ensure agent config dir exists
        config["config_dir"].mkdir(parents=True, exist_ok=True)
        
        # Backup existing if requested
        if backup_first and agent_skills_path.exists():
            if not backup_existing_config(agent_skills_path):
                return False
        elif agent_skills_path.exists():
            if agent_skills_path.is_symlink():
                agent_skills_path.unlink()
            else:
                shutil.rmtree(agent_skills_path, ignore_errors=True)
        
        # Create the symlink
        agent_skills_path.symlink_to(VAULT_SKILLS_DIR, target_is_directory=True)
        console.print(f"[green]✓[/green] Linked {agent_key} skills → {VAULT_SKILLS_DIR}")
        return True
        
    except Exception as e:
        console.print(f"[red]✗ Failed to link {agent_key}: {e}[/red]")
        return False

def install_agent(agent_key: str) -> bool:
    """Install an agent using its install command"""
    config = AGENTS_CONFIG[agent_key]
    console.print(f"[yellow]Installing {config['name']}...[/yellow]")
    
    code, stdout, stderr = run_cmd(config["install_cmd"], check=False)
    
    if code == 0:
        console.print(f"[green]✓ {config['name']} installed successfully[/green]")
        return True
    else:
        console.print(f"[red]✗ Installation failed:[/red]")
        console.print(f"[dim]{stderr or stdout}[/dim]")
        console.print(f"[dim]See: {config['docs_url']}[/dim]")
        return False

# =============================================================================
# TUI SCREENS
# =============================================================================

def print_header():
    """Print application header"""
    console.print()
    console.print(Panel.fit(
        "[bold cyan]🏛️  ClaudeVault Setup Tool[/bold cyan]\n"
        "[dim]Verknüpft AI-Agenten mit deinem Vault-Workspace[/dim]",
        box=box.DOUBLE_EDGE
    ))
    console.print()

def show_status_table(agents: Dict[str, AgentStatus]):
    """Display agent status in a table"""
    table = Table(
        title="[bold]Agent Status[/bold]",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold cyan"
    )
    
    table.add_column("Agent", style="cyan")
    table.add_column("Installiert", justify="center")
    table.add_column("Version", style="dim")
    table.add_column("Config", justify="center")
    table.add_column("Skills-Verlinkt", justify="center")
    
    for key, status in agents.items():
        installed = "[green]✓[/green]" if status.installed else "[red]✗[/red]"
        config = "[green]✓[/green]" if status.config_exists else "[dim]-[/dim]"
        linked = "[green]✓[/green]" if status.skills_linked else "[yellow]○[/yellow]"
        
        table.add_row(
            status.name,
            installed,
            status.version or "-",
            config,
            linked
        )
    
    console.print(table)
    console.print()

def show_vault_tree():
    """Display vault structure as a tree"""
    tree = Tree(f"[bold cyan]{VAULT_ROOT.name}[/bold cyan]")
    
    branches = {
        "10-notes": ["10-daily", "20-ideas", "30-projects", "40-resources", "50-personal"],
        "20-knowledge": ["ai/", "ai/models", "ai/providers", "ai/tools", "ai/concepts"],
        "30-projects-active": [],
        "40-library": [],
        "50-system": ["AGENTS", "scripts", "logs", "state"],
        "skills": [],
        "_meta": ["templates"],
        "90-archive": [],
    }
    
    for branch, subdirs in branches.items():
        branch_node = tree.add(f"[dim]{branch}/[/dim]")
        for sub in subdirs[:3]:  # Limit display
            branch_node.add(f"[dim]{sub}/[/dim]")
        if len(subdirs) > 3:
            branch_node.add(f"[dim]... ({len(subdirs) - 3} more)[/dim]")
    
    console.print(Panel(tree, title="[bold]Vault Struktur[/bold]", box=box.ROUNDED))
    console.print()

def interactive_agent_selection(agents: Dict[str, AgentStatus]) -> List[str]:
    """Interactive multi-select for agents"""
    console.print("[bold]Agenten-Auswahl[/bold]\n")
    
    selected = []
    for key, status in agents.items():
        if status.installed:
            if Confirm.ask(
                f"[cyan]{status.name}[/cyan] verknüpfen?",
                default=not status.skills_linked
            ):
                selected.append(key)
        else:
            if Confirm.ask(
                f"[cyan]{status.name}[/cyan] ist nicht installiert. Installieren?",
                default=False
            ):
                selected.append(key)
    
    return selected

def run_setup_wizard():
    """Main setup wizard flow"""
    print_header()
    
    # Check vault exists
    if not check_vault_exists():
        console.print("[yellow]Vault nicht gefunden unter:[/yellow]", VAULT_ROOT)
        if Confirm.ask("Vault-Struktur jetzt erstellen?", default=True):
            with console.status("[cyan]Erstelle Vault-Struktur...[/cyan]"):
                ensure_vault_structure()
                ensure_vault_files()
            console.print("[green]✓ Vault-Struktur erstellt[/green]\n")
        else:
            console.print("[red]Abgebrochen. Vault wird benötigt.[/red]")
            return
    else:
        console.print(f"[green]✓ Vault gefunden:[/green] {VAULT_ROOT}\n")
    
    # Show vault tree
    show_vault_tree()
    
    # Detect agents
    console.print("[bold]Scanne nach Agenten...[/bold]\n")
    agents = detect_all_agents()
    show_status_table(agents)
    
    # Check if any work needed
    installed_count = sum(1 for s in agents.values() if s.installed)
    linked_count = sum(1 for s in agents.values() if s.skills_linked)
    
    if installed_count == 0:
        console.print("[yellow]Keine Agenten installiert.[/yellow]")
        if not Confirm.ask("Trotzdem fortfahren (nur Vault-Setup)?", default=True):
            return
    elif linked_count == installed_count and all(s.skills_linked for s in agents.values() if s.installed):
        console.print("[green]✓ Alle installierten Agenten sind bereits verknüpft![/green]")
        if not Confirm.ask("Neu konfigurieren?", default=False):
            return
    
    # Agent selection
    console.print("\n[bold cyan]═" * 50 + "[/bold cyan]")
    console.print("[bold]Schritt 1: Agenten Auswahl[/bold]\n")
    
    selected = interactive_agent_selection(agents)
    
    if not selected:
        console.print("[yellow]Keine Agenten ausgewählt. Setup beendet.[/yellow]")
        return
    
    console.print(f"\n[green]Ausgewählt:[/green] {', '.join(AGENTS_CONFIG[k]['name'] for k in selected)}\n")
    
    # Backup option
    backup_enabled = Confirm.ask(
        "[bold]Schritt 2:[/bold] Bestehende Configs sichern vor dem Verknüpfen?",
        default=True
    )
    console.print()
    
    # Confirm and execute
    console.print("[bold cyan]═" * 50 + "[/bold cyan]")
    console.print("[bold]Zusammenfassung:[/bold]")
    console.print(f"  Vault: {VAULT_ROOT}")
    console.print(f"  Agenten: {len(selected)}")
    console.print(f"  Backup: {'Ja' if backup_enabled else 'Nein'}")
    console.print()
    
    if not Confirm.ask("Setup jetzt ausführen?", default=True):
        console.print("[yellow]Abgebrochen.[/yellow]")
        return
    
    # Execute setup
    console.print("\n[bold cyan]═" * 50 + "[/bold cyan]")
    console.print("[bold]Führe Setup aus...[/bold]\n")
    
    # Ensure vault structure
    with console.status("[cyan]Prüfe Vault-Struktur...[/cyan]"):
        ensure_vault_structure()
        ensure_vault_files()
    console.print("[green]✓ Vault-Struktur OK[/green]")
    
    # Process each agent
    success_count = 0
    for agent_key in selected:
        status = agents[agent_key]
        config = AGENTS_CONFIG[agent_key]
        
        console.print(f"\n[bold]{config['name']}[/bold]")
        
        # Install if not present
        if not status.installed:
            if install_agent(agent_key):
                # Re-check status
                status = detect_agent(agent_key)
            else:
                console.print(f"[red]Überspringe {config['name']} (Installation fehlgeschlagen)[/red]")
                continue
        
        # Create symlink
        if create_skills_symlink(agent_key, backup_first=backup_enabled):
            success_count += 1
        
        # Verify
        updated = detect_agent(agent_key)
        if updated.skills_linked:
            console.print(f"  [green]✓ Verknüpfung OK[/green]")
        else:
            console.print(f"  [red]✗ Verknüpfung fehlgeschlagen[/red]")
    
    # Final summary
    console.print("\n[bold cyan]═" * 50 + "[/bold cyan]")
    console.print(f"[bold]Setup abgeschlossen![/bold]")
    console.print(f"{success_count}/{len(selected)} Agenten erfolgreich verknüpft.")
    console.print()
    console.print("[dim]Dein Vault ist jetzt der zentrale Workspace.[/dim]")
    console.print("[dim]Skills werden aus {}/skills geladen.[/dim]".format(VAULT_ROOT.name))
    console.print()

def quick_setup():
    """Quick automated setup without interactive prompts"""
    print_header()
    
    # Ensure vault
    if not check_vault_exists():
        console.print("Erstelle Vault-Struktur...")
        ensure_vault_structure()
        ensure_vault_files()
    
    # Detect and auto-link all installed agents
    agents = detect_all_agents()
    
    to_link = [k for k, s in agents.items() if s.installed and not s.skills_linked]
    
    if not to_link:
        console.print("[green]✓ Alle Agenten bereits verknüpft[/green]")
        return
    
    console.print(f"Verknüpfe {len(to_link)} Agenten...\n")
    
    for agent_key in to_link:
        create_skills_symlink(agent_key, backup_first=True)
    
    console.print("\n[green]✓ Quick-Setup abgeschlossen[/green]")

def show_help():
    """Show help information"""
    console.print("""
[bold]Verwendung:[/bold]
  vault-setup.py [command]

[bold]Befehle:[/bold]
  wizard, -w     Interaktiver Setup-Assistent (Standard)
  quick, -q      Schnelles Setup ohne Fragen
  status, -s     Zeigt aktuellen Status aller Agenten
  unlink, -u     Entfernt alle Verknüpfungen
  help, -h       Diese Hilfe

[bold]Unterstützte Agenten:[/bold]
""")
    for key, config in AGENTS_CONFIG.items():
        console.print(f"  • [cyan]{config['name']}[/cyan]")
        console.print(f"    Config: {config['config_dir']}")

def show_status():
    """Show current status of all agents"""
    print_header()
    
    if check_vault_exists():
        console.print(f"[green]✓ Vault:[/green] {VAULT_ROOT}")
    else:
        console.print(f"[red]✗ Vault nicht gefunden:[/red] {VAULT_ROOT}")
    
    console.print(f"[dim]Skills-Path: {VAULT_SKILLS_DIR}[/dim]\n")
    
    agents = detect_all_agents()
    show_status_table(agents)
    
    # Show symlink details
    console.print("[bold]Symlink-Details:[/bold]\n")
    for key, status in agents.items():
        if status.skills_path and status.skills_path.exists():
            if status.skills_path.is_symlink():
                target = status.skills_path.readlink()
                console.print(f"[green]{AGENTS_CONFIG[key]['name']}:[/green]")
                console.print(f"  → {target}")
            else:
                console.print(f"[yellow]{AGENTS_CONFIG[key]['name']}:[/yellow]")
                console.print(f"  Ordner existiert (kein Symlink)")

def unlink_all():
    """Remove all symlinks"""
    print_header()
    
    if not Confirm.ask("[red]Alle Verknüpfungen entfernen?[/red]", default=False):
        return
    
    agents = detect_all_agents()
    
    for key, status in agents.items():
        if status.skills_path and status.skills_path.is_symlink():
            try:
                status.skills_path.unlink()
                console.print(f"[green]✓ Entfernt:[/green] {AGENTS_CONFIG[key]['name']}")
            except Exception as e:
                console.print(f"[red]✗ Fehler bei {key}: {e}[/red]")
    
    console.print("\n[dim]Verknüpfungen entfernt. Original-Configs sind im Backup.[/dim]")

# =============================================================================
# MAIN ENTRY
# =============================================================================

def main():
    """Main entry point"""
    args = sys.argv[1:]
    
    if not args:
        run_setup_wizard()
    elif args[0] in ("wizard", "-w", "--wizard"):
        run_setup_wizard()
    elif args[0] in ("quick", "-q", "--quick"):
        quick_setup()
    elif args[0] in ("status", "-s", "--status"):
        show_status()
    elif args[0] in ("unlink", "-u", "--unlink"):
        unlink_all()
    elif args[0] in ("help", "-h", "--help"):
        show_help()
    else:
        console.print(f"[red]Unbekannter Befehl: {args[0]}[/red]")
        show_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
