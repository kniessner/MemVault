---
title: Socius - Memory Architecture for AI Companions
created: 2026-03-30
updated: 2026-03-30
tags:
  - type/knowledge
  - topic/ai
  - topic/memory
  - topic/companion
  - status/draft
source: "[[10-notes/40-resources/socius-companion|Socius Website]]"
---

# Socius - Memory Architecture for AI Companions

## Überblick

Socius ist ein Open-Source Framework für AI Companions mit einem biologisch inspirierten Memory-System. Es modelliert menschliche Gedächtnisprozesse statt einfacher Datenbank-Speicherung.

## Kernkonzepte

### 1. Reconstructive Memory

Im Gegensatz zu klassischen RAG-Systemen, die Dokumente speichern:
- Memories werden bei Abruf rekonstruiert
- Verbindungen zwischen Erinnerungen sind wichtiger als Einzelheiten
- Vergessen ist ein Feature, kein Bug

### 2. Temporal Dynamics

```
Awake → Encoding → Sleep
  │         │         │
  │    Extraktion   Konsolidierung
  │    & Verlinkung  & Verblassen
  │         │         │
  └─────────┴─────────┘
     Kontinuierlicher Zyklus
```

### 3. Salience Scoring

Jede Memory-Node hat einen Salience-Score:

```
S = wt·temporal + wa·access + we·emotion + wi·identity + wn·novelty + ws·structural
```

| Factor | Description |
|--------|-------------|
| Temporal | Exponentieller Verfall über Zeit |
| Access | Häufiger Abruf stärkt Memory |
| Emotion | Hohe emotionale Intensität resistent |
| Identity | Identity-relevante Memories bleiben |
| Novelty | Überraschende Informationen |
| Structural | Gut vernetzte Memories |

## Memory Node Types

### Episode
Container für eine Konversation oder ein Ereignis.
- source: Stated | Inferred | ThirdParty | Lived
- Timestamp, Dauer, Kanal

### Fragment
Atomare Wissenseinheit.
- temporal_precision: Exact | Approximate | Relative | Unbounded
- Beispiel: "Sie wuchs in Cascais auf"

### Concept
Abstraktes Thema aus Fragment-Merging.
- Wird während Deep Consolidation entdeckt
- Beispiel: "Karriere-Angst", "Portugiesische Identität"

### Belief
Gehaltene Überzeugung mit Confidence-Score.
- Kann contested werden bei Widersprüchen
- Beispiel: "Ehrlichkeit ohne Timing ist Grausamkeit"

### Emotion
Emotionaler Zustand mit Intensität.
- emotional_intensity: 0.0 – 1.0
- Zeitlich verankert

### Goal
Aktives Ziel mit Status.
- status: Active | Completed | Abandoned | Evolved
- Beispiel: "Dokumentar fertigstellen"

## Retrieval System

### Dual-Path Retrieval

```
┌─────────────────┐
│  Query Context  │
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌───────┐  ┌────────┐
│Vector │  │ Graph  │
│Search │  │Traverse│
│Qdrant │  │ Neo4j  │
└───┬───┘  └───┬────┘
    │          │
    └────┬─────┘
         ▼
   ┌──────────┐
   │  Merge   │
   │  & Rank  │
   └────┬─────┘
        ▼
   ┌──────────┐
   │Reconstruct│
   │  & Inject │
   └──────────┘
```

### Ranking Formula

```
score = 0.3×salience + 0.3×similarity + 0.2×recency + 0.2×proximity
```

## Compression Pipeline

Progressive Kompression basierend auf Token-Budget:

```
Verbatim → Key Exchanges → Summary → Impression
   │            │            │          │
  100%         60%          30%        10%
   │            │            │          │
Exakter       Wichtige      Themen     Gefühl
Text          Wendungen     &          einer
                           Entscheid. Woche später
```

Bei Kompression bleiben erhalten:
- Emotionaler Content
- Schlüssel-Entscheidungen
- Entity-Referenzen
- Neuheit
- Identity-relevante Statements

Wird verworfen:
- Konversationsmechaniken
- Wiederholungen
- Begrüßungen
- Füllwörter

## Consolidation Levels

### Micro (stündlich)
- Salience neu berechnen
- Co-accessed Links stärken

### Daily (nächtlich)
- Fragmente mergen
- Muster erkennen
- Tagebuch schreiben

### Deep (wöchentlich)
- Pruning (Salience < 0.1)
- Reveries erstellen
- Überzeugungen reassessieren
- Narrative aktualisieren

## Special Memory Types

### Cornerstones
- Foundationale Erinnerungen
- Nie verfallend
- 15+ Connections → Auto-promotion

### Reveries
- Ghost traces von gelöschten Memories
- Degraded embeddings mit Gaussian noise
- Vague impressions statt exakte Erinnerung

### Narrative Loops
- Erkannte Muster über 500+ Episodes
- Recurring concept/emotion Kombinationen
- Sanfte Reflexion: "Ich habe bemerkt, das kommt oft Montags..."

## Technical Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| Backend | Rust (15 crates) | Performance, Type-Safety |
| Graph DB | Neo4j | Assoziative Memory |
| Vector DB | Qdrant | Semantic Search |
| Workflow | Temporal | Durable Orchestration |
| RTC | LiveKit | Voice/Video Calls |
| Frontend | SolidJS | Reactive UI |
| Voice | ElevenLabs | TTS/STT |

## Lessons for AI Development

1. **Memory ≠ Storage**: Menschliches Gedächtnis ist rekonstruktiv
2. **Zeit ist kritisch**: Konsolidierung braucht Zeit-Phasen
3. **Emotion ist Daten**: Nicht nur für UX, sondern für Retention
4. **Vergessen ist wichtig**: Nicht alles speichern
5. **Narrative**: Kontinuierliche Geschichte statt isolierte Fakten

## Resources

- GitHub: https://github.com/edvin/socius
- Website: https://socius-companion.com/

---

*Erstellt aus Web-Research, 2026-03-30*
