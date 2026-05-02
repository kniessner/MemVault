---
name: file-organizer
description: Intelligently organizes your files and folders across your vault by understanding context, finding duplicates, suggesting better structures, and automating cleanup tasks. Reduces cognitive load and keeps your digital workspace tidy without manual effort.
allowed-tools: Bash(ls *), Bash(find *), Bash(du *), Bash(file *), Bash(stat *), Bash(md5 *), Bash(mkdir *), Bash(mv *), Bash(rm *), Glob, Grep, Read
argument-hint: [target-directory or task description]
---

# File Organizer

This skill acts as your personal organization assistant, helping you maintain a clean, logical file structure across your vault without the mental overhead of constant manual organization.

## When to Use This Skill

- Your Downloads folder is a chaotic mess
- You can't find files because they're scattered everywhere
- You have duplicate files taking up space
- Your folder structure doesn't make sense anymore
- You want to establish better organization habits
- You're starting a new project and need a good structure
- You're cleaning up before archiving old projects

## What This Skill Does

1. **Analyzes Current Structure**: Reviews your folders and files to understand what you have
2. **Finds Duplicates**: Identifies duplicate files across your system
3. **Suggests Organization**: Proposes logical folder structures based on your content
4. **Automates Cleanup**: Moves, renames, and organizes files with your approval
5. **Maintains Context**: Makes smart decisions based on file types, dates, and content
6. **Reduces Clutter**: Identifies old files you probably don't need anymore

## Vault-Aware Organization

When organizing files within the vault, always respect the vault structure:

| Content Type | Destination |
|---|---|
| Unknown files | `00-inbox/` with `#agent-review` |
| Daily notes | `10-notes/10-daily/` |
| Knowledge files | `20-knowledge/` according to domain |
| Project files | `30-projects/YYYY-name/` |
| Shared media | `_assets/` |

Never create new top-level directories.

## Instructions

When a user requests file organization help:

1. **Understand the Scope**

   Ask clarifying questions:
   - Which directory needs organization?
   - What's the main problem?
   - Any files or folders to avoid?
   - How aggressively to organize?

2. **Analyze Current State**

   ```bash
   ls -la [target_directory]
   find [target_directory] -type f -exec file {} \; | head -20
   du -sh [target_directory]/* | sort -rh | head -20
   ```

3. **Identify Organization Patterns**

   Group by type, purpose, or date as appropriate.

4. **Find Duplicates**

   ```bash
   find [directory] -type f -exec md5 {} \; | sort | uniq -d
   ```

5. **Propose Organization Plan** — Present a clear plan before making changes.

6. **Execute After Approval**

   **Important Rules**:
   - Always confirm before deleting anything
   - Log all moves for potential undo
   - Preserve original modification dates
   - Handle filename conflicts gracefully
   - Within the vault, always route to canonical branches

7. **Provide Summary and Maintenance Tips**

## Pro Tips

1. Start small — begin with one messy folder
2. Regular maintenance — run weekly cleanup on inbox
3. Consistent naming — use `YYYY-MM-DD-descriptive-slug.md` format
4. Archive aggressively — move old projects to `90-archive/`
5. Keep active separate — maintain clear boundaries between active and archived work