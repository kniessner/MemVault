---
name: file-finder
description: Advanced file search with filters for name, size, date, type, and content
allowed-tools: Bash(find *), Bash(locate *), Bash(grep *), Bash(du *), Bash(file *), Bash(stat *), Glob, Grep
argument-hint: [search-criteria]
---

# File Finder Tool

Advanced file search capabilities with multiple filter options.

## Arguments:
- `$ARGUMENTS` - Search query (filename pattern, content, or criteria)

## Search Methods:

### 1. Find by Name

```bash
find /search/path -name "$ARGUMENTS"
find /search/path -iname "$ARGUMENTS"  # case-insensitive
```

### 2. Find by Size

```bash
find . -size +100M                      # Larger than 100MB
find . -size -1k                        # Smaller than 1KB
```

### 3. Find by Date

```bash
find . -mtime -7                        # Modified in last 7 days
find . -mtime +30                       # Modified more than 30 days ago
find . -mmin -60                        # Modified in last 60 minutes
```

### 4. Find by Type

```bash
find . -type f                          # Regular files
find . -type d                          # Directories
find . -name "*.jpg" -o -name "*.png"   # Images
```

### 5. Find by Content

```bash
grep -r "$ARGUMENTS" .                  # Search content
grep -r -l "$ARGUMENTS" .               # Show only filenames
```

### 6. Find Duplicates

```bash
find . -type f -exec md5sum {} + | sort | uniq -w32 -d
```

### 7. Execute Actions on Found Files

```bash
find . -name "*.tmp" -delete
find . -name "*.bak" -exec mv {} /backup/ \;
```

## Vault-Aware Search

When searching within the vault, prefer these scoped searches:

```bash
# Search knowledge base
rg -n --glob '*.md' 'query' "$VAULT_ROOT/20-knowledge/"

# Search project files
rg -n --glob '*.md' 'query' "$VAULT_ROOT/30-projects/"

# Search daily notes
rg -n --glob '*.md' 'query' "$VAULT_ROOT/10-notes/"
```

## Search Tips:

1. **Limit search depth:** `find . -maxdepth 2 -name "*.js"`
2. **Exclude directories:** `find . -name node_modules -prune -o -name "*.js" -print`
3. **Safe file listing:** `find . -name "*.txt" -print0 | xargs -0 ls -l`

## Example Usage:
- `/file-finder config.json` - Find config files
- `/file-finder "*.log"` - Find all log files
- `/file-finder TODO` - Find files containing TODO
- Find large files consuming disk space
- Find recently modified files