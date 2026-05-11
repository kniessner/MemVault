---
title: "Pascal Editor – 3D Architectural Project Editor"
url: https://github.com/pascalorg/editor
created: 2026-04-20
tags:
  - 3d
  - architecture
  - webgpu
  - react-three-fiber
  - typescript
  - open-source
  - monorepo
  - nextjs
  - bookmark
type: code-reference
---

# Pascal Editor

> **Create and share 3D architectural projects** — an open-source, browser-based 3D building editor built on React Three Fiber and WebGPU.

| Detail              | Value                                                      |
| ------------------- | ---------------------------------------------------------- |
| **Repository**      | [pascalorg/editor](https://github.com/pascalorg/editor)    |
| **Live App**        | [editor.pascal.app](https://editor.pascal.app)             |
| **License**         | MIT                                                        |
| **Stars**           | ⭐ 13,658                                                  |
| **Forks**           | 🍴 1,698                                                   |
| **Primary Language**| TypeScript (98.8%)                                         |

---

## Overview

Pascal Editor is a fully browser-based 3D architectural design tool. Users can model buildings, compose scenes through a node-based graph, and share finished projects — all without installing native software. The renderer targets **WebGPU** with a WebGL fallback, making it one of the more ambitious open-source projects pushing next-generation browser graphics for a production use case.

Three reasons this project matters:

1. **Democratizes architectural visualization.** No Revit or SketchUp license required — just a modern browser.
2. **Proves WebGPU is production-viable** for complex, interactive 3D editors — not just demos.
3. **Serves as a reference architecture** for large-scale React Three Fiber applications structured as a Turborepo monorepo.

---

## Key Features

- **3D Building Editor** — Walls, floors, roofs, and object placement with snapping, measurement overlays, and orthographic/perspective camera modes.
- **Node-Based Scene Graph** — Visual graph editor for composing and parameterizing scene hierarchies (conceptually similar to Blender's geometry nodes, scoped to architectural elements).
- **IndexedDB Persistence** — Projects save locally in the browser. No account required. Enables offline-first workflows that survive browser restarts.
- **Undo / Redo** — Full command-history stack with granular state diffing, powered by Zustand middleware.
- **Shareable Projects** — Export project files or publish to a hosted URL for sharing with collaborators or clients.
- **Responsive Design** — Works across desktop and tablet devices.

---

## Tech Stack & Architecture

### Stack

| Layer         | Technology              | Role                                          |
| ------------- | ----------------------- | --------------------------------------------- |
| **Rendering** | React Three Fiber + WebGPU | 3D scene rendering and interaction          |
| **Framework** | Next.js                 | App shell, routing, SSR for non-3D pages      |
| **State**     | Zustand                 | Global state management with undo/redo middleware |
| **Storage**   | IndexedDB               | Client-side project persistence               |
| **Language**  | TypeScript              | End-to-end type safety                        |
| **Build**     | Turborepo               | Monorepo orchestration, caching, task pipeline|

### Monorepo Structure

```
pascalorg/editor/
├── apps/
│   └── editor/                # Next.js app — the main editor UI
│       ├── app/               # Next.js App Router pages
│       └── components/        # Editor-specific React components
├── packages/
│   ├── @pascal-app/core/      # Domain logic: scene graph, state, commands
│   │   └── src/
│   │       ├── nodes/         # Node type definitions (walls, floors, etc.)
│   │       ├── commands/      # Undo/redo command implementations
│   │       └── store/         # Zustand stores and middleware
│   └── @pascal-app/viewer/    # Embeddable read-only 3D viewer
│       └── src/
│           ├── Viewer.tsx     # Main viewer entry point
│           └── controls/      # Camera and interaction controls
├── turbo.json
└── package.json
```

### Dependency Flow

```
apps/editor ──▶ @pascal-app/core
apps/editor ──▶ @pascal-app/viewer
@pascal-app/viewer ──▶ @pascal-app/core
```

### Package Responsibilities

- **`@pascal-app/core`** — Framework-agnostic domain layer. Contains the scene graph data model, node type registry, serialization/deserialization, the command pattern for undo/redo, and Zustand store definitions. Designed to be consumed by both the editor and the viewer.

- **`@pascal-app/viewer`** — Lightweight, embeddable React component for rendering Pascal projects in read-only mode. Target use case: embedding a finished architectural visualization on a portfolio site, in documentation, or in a real estate listing.

- **`apps/editor`** — The full Next.js application: toolbar, inspector panels, node graph editor, and all interactive editing capabilities. Composes `core` and `viewer` into the complete authoring experience.

---

## Code Examples

> **Note:** These are conceptual patterns inferred from the project's documented architecture and dependency choices, not verbatim source extracts.

### Zustand Store with Undo/Redo

```typescript
// @pascal-app/core/src/store/editorStore.ts (conceptual)
import { create } from 'zustand';
import { temporal } from 'zundo';

interface SceneNode {
  id: string;
  type: 'wall' | 'floor' | 'roof' | 'object';
  position: [number, number, number];
  rotation: [number, number, number];
  properties: Record<string, unknown>;
  children: string[];
}

interface EditorState {
  nodes: Record<string, SceneNode>;
  selectedNodeIds: string[];
  addNode: (node: SceneNode) => void;
  removeNode: (id: string) => void;
  updateNode: (id: string, patch: Partial<SceneNode>) => void;
  selectNodes: (ids: string[]) => void;
}

export const useEditorStore = create<EditorState>()(
  temporal(
    (set) => ({
      nodes: {},
      selectedNodeIds: [],

      addNode: (node) =>
        set((state) => ({
          nodes: { ...state.nodes, [node.id]: node },
        })),

      removeNode: (id) =>
        set((state) => {
          const { [id]: _, ...rest } = state.nodes;
          return { nodes: rest };
        }),

      updateNode: (id, patch) =>
        set((state) => ({
          nodes: {
            ...state.nodes,
            [id]: { ...state.nodes[id], ...patch },
          },
        })),

      selectNodes: (ids) => set({ selectedNodeIds: ids }),
    }),
    { limit: 100 }
  )
);
```

### Embedding the Viewer

```tsx
// Embedding a Pascal project on an external site (conceptual)
import { PascalViewer } from '@pascal-app/viewer';

export default function PortfolioPage() {
  return (
    <div style={{ width: '100%', height: '600px' }}>
      <PascalViewer
        projectUrl="https://editor.pascal.app/api/projects/abc123"
        cameraPosition={[10, 8, 10]}
        enableOrbitControls
        background="#f5f5f5"
      />
    </div>
  );
}
```

### IndexedDB Persistence

```typescript
// @pascal-app/core/src/persistence/indexedDb.ts (conceptual)
import { openDB } from 'idb';

const DB_NAME = 'pascal-editor';
const STORE_NAME = 'projects';

export async function saveProject(id: string, data: ProjectData) {
  const db = await openDB(DB_NAME, 1, {
    upgrade(db) {
      db.createObjectStore(STORE_NAME);
    },
  });
  await db.put(STORE_NAME, data, id);
}

export async function loadProject(id: string): Promise<ProjectData | undefined> {
  const db = await openDB(DB_NAME, 1);
  return db.get(STORE_NAME, id);
}
```

---

## Use Cases

| Audience                      | Use Case                                                                                                      |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Architects & Designers**    | Rapid prototyping of building layouts without heavyweight CAD software                                        |
| **Real Estate / PropTech**    | Embed interactive 3D floor plans and building visualizations in listings via `@pascal-app/viewer`             |
| **Educators**                 | Teach architectural concepts with a free, accessible tool that runs in any modern browser                     |
| **Developers**                | Reference architecture for complex R3F + WebGPU applications; fork and extend for domain-specific 3D editors |
| **Homeowners & DIY Planners** | Home renovation planning and space layout exploration                                                         |
| **Open Source Contributors**  | Well-structured monorepo with clear package boundaries — approachable for first-time large project contributions |

---

## Why This Stands Out

- **WebGPU-first in production.** Most open-source 3D editors still target WebGL exclusively. Pascal bets on the next generation of browser graphics APIs while maintaining a fallback.
- **Clean separation of concerns.** The `core` → `viewer` → `editor` layering is textbook monorepo architecture. Domain logic is fully decoupled from rendering and UI.
- **Offline-first by default.** IndexedDB persistence means projects survive browser restarts with no backend required — a meaningful UX choice for users in low-connectivity environments.
- **Community traction.** 13.6k+ stars signals significant validation. Active enough to watch for evolving R3F and WebGPU patterns.

---

## Resources & Links

| Resource            | URL                                                                 |
| ------------------- | ------------------------------------------------------------------- |
| **Repository**      | <https://github.com/pascalorg/editor>                               |
| **Live Editor**     | <https://editor.pascal.app>                                         |
| **License**         | [MIT](https://github.com/pascalorg/editor/blob/main/LICENSE)        |
| **React Three Fiber** | <https://docs.pmnd.rs/react-three-fiber>                         |
| **WebGPU Spec**     | <https://www.w3.org/TR/webgpu/>                                     |
| **Next.js**         | <https://nextjs.org>                                                |
| **Zustand**         | <https://github.com/pmndrs/zustand>                                 |
| **Turborepo**       | <https://turbo.build/repo>                                          |

---

*Bookmarked for: R3F architecture reference · WebGPU production example · Turborepo monorepo patterns · offline-first state management · embeddable 3D viewer design.*

*Last updated: 2026-04-20*
