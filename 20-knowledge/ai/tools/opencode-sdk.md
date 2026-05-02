---
title: OpenCode SDK
author: Anomaly (OpenCode)
license: Open Source
url: https://opencode.ai/docs/de/sdk/
npm: "@opencode-ai/sdk"
github: https://github.com/opencode-ai/opencode
category: tool
type: sdk
tags:
  - opencode
  - sdk
  - typescript
  - coding-agent
  - server
  - api
status: active
platforms:
  - Node.js
  - TypeScript
  - JavaScript
date-added: 2026-05-02
description: TypeScript SDK for programmatic access to the OpenCode coding agent server API.
---

# OpenCode SDK

**OpenCode SDK** (`@opencode-ai/sdk`) ist ein typsicherer TypeScript/JavaScript-Client für die Server-API von [OpenCode](https://opencode.ai) — einem quelloffenen AI-Coding-Agenten, der über Terminal, Desktop-App und IDE-Extension nutzbar ist.

> OpenCode selbst ist ein Open-Source-Coding-Agent mit 150K+ GitHub Stars, 850+ Contributors und 6.5M+ monatlichen Nutzern. Die Desktop-App ist in Beta (macOS, Windows, Linux).

## Installation

```bash
npm install @opencode-ai/sdk
```

## Client erstellen

### Server + Client (beides starten)

```typescript
import { createOpencode } from "@opencode-ai/sdk"

const opencode = await createOpencode({
  hostname: "127.0.0.1",
  port: 4096,
  timeout: 5000,    // ms für Server-Start
  config: {
    model: "anthropic/claude-3-5-sonnet-20241022"
  }
})

// Server stoppen
opencode.server.close()
```

### Nur Client (Server läuft bereits)

```typescript
import { createOpencodeClient } from "@opencode-ai/sdk"

const client = createOpencodeClient({
  baseUrl: "http://localhost:4096",
  fetch: globalThis.fetch,         // Custom fetch
  parseAs: "auto",                 // auto | json | text | stream
  responseStyle: "fields",         // data | fields
  throwOnError: false
})
```

## Konfiguration

Das SDK lädt `opencode.json` automatisch. Inline-Konfiguration über `config`-Option überschreibt oder erweitert.

## Core APIs

### Sessions

| Methode | Beschreibung |
|---------|-------------|
| `client.session.list()` | Alle Sessions auflisten |
| `client.session.create()` | Neue Session erstellen |
| `client.session.get({ path: { id } })` | Session abrufen |
| `client.session.prompt({ path, body })` | Prompt an Session senden |
| `client.session.command({ path, body })` | Befehl an Session senden |
| `client.session.shell({ path, body })` | Shell-Befehl ausführen |
| `client.session.abort({ path })` | Laufende Session abbrechen |
| `client.session.revert({ path, body })` | Nachricht zurücksetzen |

**Prompt senden:**
```typescript
const result = await client.session.prompt({
  path: { id: session.id },
  body: {
    parts: [{ type: "text", text: "Hello!" }],
    model: { providerID: "anthropic", modelID: "claude-3-5-sonnet-20241022" }
  }
})
```

**Inject context only (noReply):**
```typescript
await client.session.prompt({
  path: { id: session.id },
  body: {
    noReply: true,
    parts: [{ type: "text", text: "You are a helpful assistant." }]
  }
})
```

### Files

| Methode | Beschreibung |
|---------|-------------|
| `client.find.text({ query: { pattern } })` | Text in Dateien suchen |
| `client.find.files({ query })` | Dateien/Verzeichnisse finden |
| `client.find.symbols({ query })` | Workspace-Symbole finden |
| `client.file.read({ query: { path } })` | Datei lesen (raw/patch) |
| `client.file.status({ query })` | Git-Status getrackter Dateien |

```typescript
// Text suchen
const textResults = await client.find.text({
  query: { pattern: "function.*opencode" }
})

// Dateien finden
const files = await client.find.files({
  query: { query: "*.ts", type: "file", limit: 50 }
})

// Datei lesen
const content = await client.file.read({
  query: { path: "src/index.ts" }
})
```

### TUI Control

| Methode | Beschreibung |
|---------|-------------|
| `client.tui.appendPrompt({ body })` | Text an Prompt anhängen |
| `client.tui.submitPrompt()` | Prompt absenden |
| `client.tui.clearPrompt()` | Prompt leeren |
| `client.tui.showToast({ body })` | Toast-Benachrichtigung |
| `client.tui.openHelp()` | Hilfe-Dialog |
| `client.tui.openSessions()` | Session-Auswahl |
| `client.tui.openModels()` | Modell-Auswahl |
| `client.tui.openThemes()` | Theme-Auswahl |

### App / Config

| Methode | Beschreibung |
|---------|-------------|
| `client.global.health()` | Server-Status prüfen |
| `client.app.log()` | Log-Eintrag schreiben |
| `client.app.agents()` | Verfügbare Agenten listen |
| `client.project.list()` | Alle Projekte listen |
| `client.project.current()` | Aktuelles Projekt |
| `client.config.get()` | Konfiguration abrufen |
| `client.config.providers()` | Provider + Default-Modelle |
| `client.auth.set()` | Auth-Daten setzen |

### Events (SSE)

```typescript
const events = await client.event.subscribe()
for await (const event of events.stream) {
  console.log("Event:", event.type, event.properties)
}
```

## Structured Output

Validiertes JSON über JSON-Schema:

```typescript
const result = await client.session.prompt({
  path: { id: sessionId },
  body: {
    parts: [{ type: "text", text: "Recherchiere Anthropic und gib Firmeninfos zurück" }],
    format: {
      type: "json_schema",
      retryCount: 2,  // Validierungsversuche (standard: 2)
      schema: {
        type: "object",
        properties: {
          company: { type: "string", description: "Firmenname" },
          founded: { type: "number", description: "Gründungsjahr" },
          products: { type: "array", items: { type: "string", description: "Hauptprodukte" } },
          required: ["company", "founded"]
        }
      }
    }
  }
})

// Zugriff auf strukturierte Ausgabe
console.log(result.data.info.structured_output)
```

### Output Formate

| Type | Beschreibung |
|------|-------------|
| `text` | Standard-Textantwort (keine Struktur) |
| `json_schema` | Validierbares JSON nach Schema |

### Fehler bei Structured Output

```typescript
if (result.data.info.error?.name === "StructuredOutputError") {
  console.error("Strukturierte Ausgabe fehlgeschlagen:", result.data.info.error.message)
  console.error("Versuche:", result.data.info.error.retries)
}
```

## Typen

TypeScript-Definitionen für alle API-Typen — importierbar direkt:

```typescript
import type { Session, Message, Part } from "@opencode-ai/sdk"
```

Typen werden aus der OpenAPI-Spezifikation generiert.

## Best Practices

1. **Klare Schema-Beschreibungen** — gibt Properties gute `description`, damit das Modell versteht, was zu extrahieren ist
2. **`required` nutzen** — definiere Pflichtfelder
3. **Schemas einfach halten** — tief verschachtelte Schemas sind schwer korrekt auszufüllen
4. **`retryCount` anpassen** — erhöhen bei komplexen Schemas, verringern bei einfachen

## Quellen

- [SDK Docs](https://opencode.ai/docs/de/sdk/)
- [OpenCode GitHub](https://github.com/opencode-ai/opencode)
- [Providers-Doku](https://opencode.ai/docs/providers/)
- [Ollama-Integration](https://docs.ollama.com/integrations/opencode)
