---
name: quick-backup
description: Quickly backup specific directories or files with compression and verification
allowed-tools: Bash(tar *), Bash(rsync *), Bash(cp *), Bash(gzip *), Bash(zip *), Bash(du *), Bash(df *), Bash(sha256sum *), Bash(find *)
argument-hint: [source-path] [destination-path]
---

# Quick Backup Tool

Create quick backups of directories or files with compression and verification.

## Arguments:
- `$0` - Source path to backup (required)
- `$1` - Destination path (optional, defaults to ~/backups/)

## Backup Methods:

### 1. Tar Archive Backup (Recommended)

```bash
SOURCE="$0"
DEST="${1:-$HOME/backups}"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME=$(basename "$SOURCE")_backup_$TIMESTAMP.tar.gz

mkdir -p "$DEST"
tar -czf "$DEST/$BACKUP_NAME" -C "$(dirname "$SOURCE")" "$(basename "$SOURCE")"
```

### 2. Rsync Backup (Incremental)

```bash
rsync -av --delete --link-dest="$DEST/latest" "$SOURCE/" "$DEST/$TIMESTAMP/"
ln -nsf "$DEST/$TIMESTAMP" "$DEST/latest"
```

### 3. Simple Copy Backup

```bash
cp -r "$SOURCE" "$DEST/$(basename $SOURCE)_backup_$TIMESTAMP"
```

## Verification

```bash
tar -tzf "$DEST/$BACKUP_NAME" > /dev/null
sha256sum "$DEST/$BACKUP_NAME" > "$DEST/$BACKUP_NAME.sha256"
```

## Vault Backup

For backing up the vault itself:

```bash
tar -czf ~/backups/vault_backup_$(date +%Y%m%d).tar.gz \
  --exclude='node_modules' \
  --exclude='.git' \
  --exclude='__pycache__' \
  --exclude='.DS_Store' \
  --exclude='50-system/conversations/sessions/' \
  -C ~/path/to/vault .
```

## Safety Features:

- Always verify before overwriting
- Confirm destructive operations
- Check available disk space
- Verify backup integrity
- Generate checksums
- Never delete source until backup verified