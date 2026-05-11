# vault-setup - ClaudeVault Agent Integration Tool

## Überblick

Dieses Tool verknüpft AI-Agenten (Codex, Claude Code, OpenClaw) mit dem ClaudeVault-Workspace. Skills und Configs werden zentral im Vault verwaltet.

## Funktionen

- **Agenten-Erkennung**: Findet automatisch installierte AI-Agenten
- **Vault-Struktur**: Erstellt die vollständige Vault-Verzeichnisstruktur
- **Skills-Verknüpfung**: Ersetzt Agent-Skill-Ordner durch Symlinks zum Vault
- **Backup**: Sichert bestehende Configs vor dem Verknüpfen
- **TUI**: Benutzerfreundliche Oberfläche mit `rich`

## Unterstützte Agenten

| Agent | Config-Pfad | Install-Check |
|-------|-------------|---------------|
| Codex (OpenAI) | `~/.codex/` | `codex --version` |
| Claude Code | `~/.claude/` | `claude --version` |
| OpenClaw | `~/.config/openclaw/` | `openclaw --version` |
| Claude CLI (opentool) | `~/.opentool/` | `opentool --version` |

## Verwendung

```bash
# Interaktiver Wizard (Standard)
./vault-setup

# Schnelles Setup (keine Fragen)
./vault-setup quick

# Status anzeigen
./vault-setup status

# Alle Verknüpfungen entfernen
./vault-setup unlink

# Hilfe anzeigen
./vault-setup help
```

## Symlinks

Das Tool erstellt folgende Verknüpfungen:

```
~/.codex/skills → ~/ClaudeVault/skills
~/.claude/skills → ~/ClaudeVault/skills
~/.config/openclaw/skills → ~/ClaudeVault/skills
```

## Dateien

| Datei | Beschreibung |
|-------|--------------|
| `vault-setup` | Shell-Wrapper |
| `vault-setup.py` | Python-Hauptscript |
| `vault-setup.md` | Diese Dokumentation |

## Fehlersuche

### Script nicht ausführbar

```bash
chmod +x ~/ClaudeVault/50-system/scripts/vault-setup
```

### Symlink existiert bereits als Ordner

```bash
# Manuelles Backup & Ersetzen
mv ~/.codex/skills ~/.codex/skills.backup.$(date +%s)
ln -s ~/ClaudeVault/skills ~/.codex/skills
```
