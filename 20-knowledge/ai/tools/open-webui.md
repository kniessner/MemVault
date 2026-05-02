---
title: "Open WebUI"
source: https://docs.openwebui.com/
date-created: 2026-04-05
date-updated: 2026-04-05
description: "Self-hosted Web-Frontend fuer LLMs mit Tool-Integration, Multi-Provider-Support und Open Terminal"
tags:
- ai-tool
- web-ui
- self-hosted
- llm-frontend
- docker
---

# Open WebUI

## Summary

Open WebUI ist ein self-hosted Web-Frontend fuer LLMs. Laeuft als Docker-Container und verbindet sich mit mehreren Providern gleichzeitig: Ollama, OpenAI-kompatible APIs, und Anthropic.

## Lokales Setup

### Container

```bash
# Image: ghcr.io/open-webui/open-webui:main
# Port: 3008 -> 8080
# Volume: openwebui_data:/app/backend/data
# Restart: unless-stopped
# Zugriff: http://localhost:3008
```

### Verbundene Provider

| Provider | Endpoint | Details |
|----------|----------|---------|
| **Hermes Agent** | `http://host.docker.internal:8642/v1` | OpenAI-kompatibler API-Server, eigener API-Key |
| **OpenRouter** | `https://openrouter.ai/api/v1` | 349+ Modelle (Claude, Codex, Gemini, Llama, etc.) |
| **Lokales Ollama** | `http://host.docker.internal:11434` | Modelle auf dieser Maschine |
| **Remote Ollama** | `http://knssnr.com:11434` | 13 Modelle auf dem Remote-Server |

### Environment Variables

```bash
# Mehrere OpenAI-Endpunkte (Semikolon-getrennt)
OPENAI_API_BASE_URLS="http://host.docker.internal:8642/v1;https://openrouter.ai/api/v1"
OPENAI_API_KEYS="<hermes-key>;<openrouter-key>"

# Mehrere Ollama-Instanzen (Semikolon-getrennt)
OLLAMA_BASE_URLS="http://host.docker.internal:11434;http://knssnr.com:11434"

# Linux Docker: Host-Gateway-Mapping noetig
--add-host=host.docker.internal:host-gateway
```

### Docker-Befehl (komplett)

```bash
DOCKER_HOST=unix:///var/run/docker.sock docker run -d \
  --name openwebui \
  -p 3008:8080 \
  -e OPENAI_API_BASE_URLS="http://host.docker.internal:8642/v1;https://openrouter.ai/api/v1" \
  -e OPENAI_API_KEYS="<hermes-api-key>;<openrouter-api-key>" \
  -e OLLAMA_BASE_URLS="http://host.docker.internal:11434;http://knssnr.com:11434" \
  --add-host=host.docker.internal:host-gateway \
  -v openwebui_data:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

> **Wichtig:** Auf dieser Maschine laeuft Docker Engine via systemd, NICHT Docker Desktop. Bei Problemen: `DOCKER_HOST=unix:///var/run/docker.sock` oder `docker context use default`

---

## Open Terminal

### Was ist Open Terminal?

Open Terminal gibt KI-Modellen in Open WebUI Zugriff auf eine echte Ausfuehrungsumgebung: Shell-Befehle, Dateiverwaltung, Code-Ausfuehrung — alles innerhalb des Chat-Interfaces.

**Faehigkeiten:**
- Datenanalyse (CSV, Spreadsheets, Datenbanken)
- Dokumentenverarbeitung (PDF, Word, Excel, EPUB)
- Web-Entwicklung mit Live-Preview
- Software-Entwicklung (Git, Tests, Debugging)
- Systemautomation (Dateien, Backups, Batch-Prozesse)

### Installation

```bash
DOCKER_HOST=unix:///var/run/docker.sock docker run -d \
  --name open-terminal \
  --restart unless-stopped \
  -p 8000:8000 \
  -v open-terminal-data:/home/user \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -e OPEN_TERMINAL_API_KEY=open-terminal-key-2024 \
  -e OPEN_TERMINAL_PIP_PACKAGES="httpx polars pandas matplotlib" \
  ghcr.io/open-webui/open-terminal
```

### Image-Varianten

| Variante | Groesse | Inhalt |
|----------|---------|--------|
| `latest` | ~4 GB | Node.js, gcc, ffmpeg, LaTeX, Docker CLI, Data-Science-Libs, sudo, Multi-User |
| `slim` | ~430 MB | git, curl, jq (Debian) |
| `alpine` | ~230 MB | git, curl, jq (Alpine, minimal) |

### Environment Variables

| Variable | Beschreibung |
|----------|-------------|
| `OPEN_TERMINAL_API_KEY` | Auth-Key (wird auto-generiert wenn nicht gesetzt) |
| `OPEN_TERMINAL_PACKAGES` | APT-Pakete (Space-getrennt) |
| `OPEN_TERMINAL_PIP_PACKAGES` | Python-Pakete (Space-getrennt) |
| `OPEN_TERMINAL_NPM_PACKAGES` | NPM-Pakete (Space-getrennt) |
| `OPEN_TERMINAL_MULTI_USER` | `true` fuer User-Isolation |

### Verbindung mit Open WebUI

**Option 1: Admin-Level (fuer alle User)**
1. Admin Settings > Integrations > Open Terminal
2. URL: `http://host.docker.internal:8000`
3. API Key: `open-terminal-key-2024`
4. Aktivieren

**Option 2: User-Level (pro User)**
1. User Settings > Integrations > Open Terminal
2. Gleiche URL + Key

### Sicherheit

- Docker-Socket-Mount (`/var/run/docker.sock`) gibt vollen Zugriff auf den Host-Docker-Daemon
- Bare-Metal-Modus fuehrt Befehle mit den Rechten des ausfuehrenden Users aus
- Multi-User-Modus bietet nur Basis-Isolation (shared Kernel + Netzwerk)
- Nur in vertrauenswuerdigen Umgebungen einsetzen

---

## Konfiguration via Admin-UI

### Connections (Admin Settings > Connections)

Zusaetzliche Provider koennen auch ueber die UI hinzugefuegt werden:
1. **OpenAI API** > Zahnrad > **+ Add New Connection**
2. URL eingeben (mit `/v1` Suffix)
3. API Key eingeben
4. Verifizieren und speichern

### Modell-Sichtbarkeit

Alle verbundenen Provider werden automatisch zusammengefuehrt. Modelle erscheinen im Modell-Dropdown sortiert nach Provider.

### Weitere Features

| Feature | Beschreibung |
|---------|-------------|
| **RAG** | Document-Upload fuer Retrieval-Augmented Generation |
| **Web Search** | Integrierte Web-Suche (konfigurierbar) |
| **Image Generation** | Verbindung zu DALL-E, Stable Diffusion, etc. |
| **Voice** | STT/TTS mit Whisper und anderen Backends |
| **Tools/Functions** | Custom Python-Tools die Modelle aufrufen koennen |
| **Pipelines** | Request/Response-Middleware-System |

---

## Troubleshooting

| Problem | Loesung |
|---------|---------|
| Modelle erscheinen nicht | URL muss `/v1` enthalten, `curl http://localhost:8642/v1/models` testen |
| Connection refused | `host.docker.internal` statt `localhost` in Docker verwenden |
| Container nicht sichtbar | Docker-Context pruefen: `docker context use default` |
| Langsame Antworten via Hermes | Normal — Agent fuehrt Tools aus bevor er antwortet |
| Auth-Fehler | API-Keys muessen exakt uebereinstimmen |

---

## Referenzen

- Docs: https://docs.openwebui.com/
- GitHub: https://github.com/open-webui/open-webui
- Open Terminal: https://github.com/open-webui/open-terminal
- Hermes-Integration: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/open-webui
