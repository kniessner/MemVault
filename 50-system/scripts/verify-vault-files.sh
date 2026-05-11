#!/bin/bash
# =============================================================================
# verify-vault-files.sh - Prüft Integrität wichtiger Vault-Dateien
# =============================================================================

set -e

VAULT_ROOT="${CLAUDE_VAULT:-$HOME/ClaudeVault}"
ERRORS=0

# Farben
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

check_file() {
    local file="$1"
    local min_size="${2:-10}"
    local desc="${3:-$file}"
    
    if [[ ! -f "$file" ]]; then
        echo -e "${RED}❌ Fehlt${NC}: $desc"
        ((ERRORS++))
        return 1
    fi
    
    local size
    size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null || echo "0")
    
    if [[ "$size" -lt "$min_size" ]]; then
        echo -e "${YELLOW}⚠️  Zu klein${NC} (${size}B): $desc"
        ((ERRORS++))
        return 1
    fi
    
    echo -e "${GREEN}✅ OK${NC}: $desc (${size}B)"
    return 0
}

echo "🔍 Prüfe Vault-Dateien in $VAULT_ROOT..."
echo ""

# Kern-Dateien
check_file "$VAULT_ROOT/SOUL.md" 100 "SOUL.md"
check_file "$VAULT_ROOT/USER.md" 50 "USER.md"
check_file "$VAULT_ROOT/MEMORY.md" 50 "MEMORY.md"
check_file "$VAULT_ROOT/HEARTBEAT.md" 10 "HEARTBEAT.md"
check_file "$VAULT_ROOT/AGENTS.md" 100 "AGENTS.md"

echo ""

# Scripts
check_file "$VAULT_ROOT/50-system/scripts/vault-setup" 50 "vault-setup Script"
check_file "$VAULT_ROOT/50-system/scripts/vault-setup.py" 1000 "vault-setup.py"
check_file "$VAULT_ROOT/50-system/scripts/vault-setup.md" 100 "vault-setup.md"

echo ""

# Projekte
check_file "$VAULT_ROOT/30-projects-active/2026-kamera-recherche/README.md" 1000 "Kamera Recherche Projekt"

# Ressourcen
check_file "$VAULT_ROOT/10-notes/40-resources/kameras/index.md" 500 "Kamera Index"
check_file "$VAULT_ROOT/10-notes/40-resources/kameras/olympus-superzoom-140s.md" 1000 "Olympus Superzoom 140S"
check_file "$VAULT_ROOT/10-notes/40-resources/kameras/konica-c35.md" 1000 "Konica C35"

echo ""

if [[ $ERRORS -eq 0 ]]; then
    echo -e "${GREEN}✅ Alle Dateien OK${NC}"
    exit 0
else
    echo -e "${RED}❌ $ERRORS Probleme gefunden${NC}"
    exit 1
fi
