---
name: project-manager
description: Create and manage development projects in the vault - initialize, list, open, and organize projects
allowed-tools: Read, Write, Edit, Bash(mkdir *), Bash(ls *), Bash(cd *), Bash(git *), Bash(tree *), Glob
argument-hint: [action] [project-name]
---

# Project Manager

Create and manage all your development projects within the vault.

## Default Workspace:
**All projects live in:** `$VAULT_ROOT/30-projects/`

## Arguments:
- `$0` - Action (new, list, open, info, init)
- `$1` - Project name or category

## Core Functions:

### 1. Create New Project

**Interactive project creation:**
```bash
VAULT_ROOT="${VAULT_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
PROJECTS_DIR="$VAULT_ROOT/30-projects"
PROJECT_NAME="$1"
CATEGORY="${2:-2026-experiments}"
PROJECT_PATH="$PROJECTS_DIR/$CATEGORY/$PROJECT_NAME"

mkdir -p "$PROJECT_PATH"/{src,tests,docs}
```

**Ask for project type:**
- Web application (React, Vue, Next.js, etc.)
- Backend API (Node, Python, Go, etc.)
- Script/Tool
- Experiment/POC
- Learning project

### 2. List Projects

**All projects:**
```bash
tree -L 2 "$PROJECTS_DIR"
```

**Recently modified:**
```bash
find "$PROJECTS_DIR" -type d -maxdepth 2 -mindepth 2 -mtime -7
```

### 3. Open Project

**Open in current shell:**
```bash
cd "$PROJECTS_DIR/$CATEGORY/$PROJECT_NAME"
```

**Show project info:**
- Path, Size, File count, Git status, Tech stack

### 4. Project Categories

**Default categories:**
- **web/** - Frontend and full-stack web applications
- **backend/** - Backend APIs and services
- **scripts/** - Utility scripts and tools
- **experiments/** - POCs and experiments
- **learning/** - Learning projects and tutorials

### 5. Project Templates

#### Minimal
```
project/
├── README.md
├── src/
└── .gitignore
```

#### Web App
```
project/
├── README.md
├── package.json
├── src/
│   ├── components/
│   ├── pages/
│   └── utils/
├── public/
└── .gitignore
```

#### Python Project
```
project/
├── README.md
├── requirements.txt
├── setup.py
├── src/
│   └── __init__.py
├── tests/
└── .gitignore
```

### 6. Project Workspace Setup

```bash
cd "$PROJECT_PATH"

if [ -f "package.json" ]; then
  npm install
elif [ -f "requirements.txt" ]; then
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
fi
```

## Integration with Other Skills:

- `50-system/skills/obsidian/` - Open notes and docs
- `50-system/skills/file-organizer/` - Organize project files

## Usage Examples:

**Create new project:**
```
/project-manager new my-app web
```

**List projects:**
```
/project-manager list
```

**Open project:**
```
/project-manager open my-app
```