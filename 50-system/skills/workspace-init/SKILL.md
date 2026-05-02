---
name: workspace-init
description: Initialize your terminal session to use MemVault as the default workspace
allowed-tools: Bash(cd *), Bash(pwd), Bash(export *), Bash(echo *)
---

# Workspace Init

Set up your shell session to use the vault as the default workspace.

## Core Function:

This skill sets up environment variables and changes to the vault directory, making it the default location for all your work.

## What It Does:

### 1. Set Environment Variables

```bash
export VAULT_ROOT="${VAULT_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
export VAULT_PROJECTS="$VAULT_ROOT/30-projects-active"
export VAULT_SKILLS="$VAULT_ROOT/50-system/skills"
export VAULT_LOGS="$VAULT_ROOT/50-system/logs"
export VAULT_SESSIONS="$VAULT_LOGS/session-logs"
```

### 2. Change to Projects Directory

```bash
cd "$VAULT_PROJECTS"
```

### 3. Show Workspace Info

Display:
- Current workspace location
- Available project categories
- Recent projects
- Quick commands

## Setup Instructions:

To make the vault your default workspace automatically, add this to your shell configuration:

### For Bash (~/.bashrc):
```bash
# Vault Workspace
export VAULT_ROOT="${VAULT_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
export VAULT_PROJECTS="$VAULT_ROOT/30-projects-active"
export VAULT_SKILLS="$VAULT_ROOT/50-system/skills"
export VAULT_LOGS="$VAULT_ROOT/50-system/logs"
export VAULT_SESSIONS="$VAULT_LOGS/session-logs"

# Aliases for quick navigation
alias vault="cd $VAULT_ROOT"
alias projects="cd $VAULT_PROJECTS"
alias skills="cd $VAULT_SKILLS"

# Start in projects directory
cd $VAULT_PROJECTS 2>/dev/null || true
```

### For Zsh (~/.zshrc):
```zsh
# Vault Workspace
export VAULT_ROOT="${VAULT_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
export VAULT_PROJECTS="$VAULT_ROOT/30-projects-active"
export VAULT_SKILLS="$VAULT_ROOT/50-system/skills"
export VAULT_LOGS="$VAULT_ROOT/50-system/logs"
export VAULT_SESSIONS="$VAULT_LOGS/session-logs"

# Aliases
alias vault="cd $VAULT_ROOT"
alias projects="cd $VAULT_PROJECTS"
alias skills="cd $VAULT_SKILLS"

# Start in projects directory
cd $VAULT_PROJECTS 2>/dev/null || true
```

## Usage:

When you invoke this skill, it will:
1. Set all environment variables
2. Change to the projects directory
3. Display workspace status

## Shell Functions:

Add these to your shell config for enhanced project management:

```bash
# Quick project creation
mkproject() {
  mkdir -p "$VAULT_PROJECTS/$1"
  cd "$VAULT_PROJECTS/$1"
  git init
  echo "# $1" > README.md
  echo "Created project: $1"
}

# List all projects
lsprojects() {
  echo "Projects in vault:"
  tree -L 2 "$VAULT_PROJECTS"
}

# Jump to project
goto() {
  if [ -d "$VAULT_PROJECTS/$1" ]; then
    cd "$VAULT_PROJECTS/$1"
  else
    echo "Project not found: $1"
    echo "Available projects:"
    ls "$VAULT_PROJECTS"
  fi
}
```

## Integration:

This skill works seamlessly with:
- `50-system/skills/project-manager/` - Project creation and management
- `50-system/skills/obsidian/` - Open notes and docs

## Benefits:

- Consistent location - Always work in the same place
- Quick access - Environment variables for fast navigation
- Organized - All projects in one vault
- Integrated - Works with Obsidian and other skills
- Backed Up - Everything in one vault for easy backup