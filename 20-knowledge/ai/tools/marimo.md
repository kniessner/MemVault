---
url: https://marimo.io/
title: marimo
description: A next-generation Python notebook — open source, reactive, and Git-friendly
source_doc: https://docs.marimo.io/
created: 2026-04-27
author: marimo team
license: Apache-2.0
category: Developer Tools
pricing: Free
open_source: true
tags:
  - bookmark
  - python
  - notebook
  - jupyter
  - data-science
  - reactive
  - open-source
  - git-friendly
  - web-app
  - dashboard
---

# marimo

> A next-generation Python notebook. Open source, reactive, and Git-friendly. Run as an app, share as a script.

## Overview

**marimo** reimagines Jupyter notebooks with native reactivity, reproducibility, and Git-friendliness. Built for data scientists, ML engineers, and Python developers who need interactive notebooks that don't break when re-run.

| Attribute | Value |
|-----------|-------|
| **Website** | https://marimo.io |
| **GitHub** | [github.com/marimo-team/marimo](https://github.com/marimo-team/marimo) |
| **License** | Apache-2.0 |
| **Pricing** | Free (open source) |
| **Platforms** | macOS, Linux, Windows |
| **Python** | 3.8+ |

## Key Features

| Feature | Description |
|---------|-------------|
| **Reactive cells** | Changing a cell automatically reruns all dependent cells |
| **Deterministic** | Runs top-to-bottom, no hidden state |
| **Git-friendly** | Pure Python `.py` files, readable diffs |
| **Interactive widgets** | Built-in UI elements (sliders, dropdowns, text inputs) |
| **Share as apps** | Export notebook as a standalone web app |
| **Run as scripts** | Execute notebooks without the UI |
| **SQL support** | First-class SQL cells (SQLite, DuckDB, etc.) |
| **AI editor** | Built-in AI assistant for code generation |

## Installation

```bash
pip install marimo

# Run the app
marimo edit

# Or open a specific notebook
marimo edit my_notebook.py

# Run as a script
python my_notebook.py
```

## Interactive Elements

Built-in widgets for building dashboards and apps:

```python
import marimo as mo

slider = mo.ui.slider(0, 10, step=1, label="Value")
dropdown = mo.ui.dropdown(["A", "B", "C"], label="Option")
text = mo.ui.text(label="Input")

mo.hstack([slider, dropdown, text])
```

## Reactive by Design

```python
# Cell 1
data = load_dataset("iris")

# Cell 2
filtered = data[data.label == selected_label]

# Cell 3
mo.hstack([
    mo.md(f"Rows: {len(filtered)}"),
    mo.as_html(filtered.plot()),
])
```

Changing `selected_label` automatically reruns Cell 2 and Cell 3.

## Export Options

| Format | Command | Use |
|--------|---------|-----|
| **Python script** | `marimo export my_notebook.py` | Run anywhere |
| **HTML** | `marimo export --format html` | Static viewing |
| **Web app** | `marimo run my_notebook.py` | Interactive deployment |
| **WASM** | Browser-based | No server needed |

## AI Features

marimo includes an AI-powered editor:
- Code generation from natural language
- Smart cell suggestions
- Error explanation and fix suggestions

## Cloud Deployment

```bash
# Deploy as a web app
marimo run notebook.py --port 3000

# Or use Marimo Cloud (managed hosting)
# See docs.marimo.io/cloud for details
```

## Comparison

| | marimo | Jupyter | Streamlit | Panel |
|---|--------|---------|-----------|-------|
| **Reactive** | ✅ Native | ❌ Manual | ✅ | ✅ |
| **Git-friendly** | ✅ Python files | ❌ JSON | ✅ | ✅ |
| **Run as script** | ✅ | ⚠️ (nbconvert) | ✅ | ✅ |
| **Widgets** | ✅ Built-in | Via ipywidgets | ✅ | ✅ |
| **Notebook** | Yes | Yes | No | No |
| **Open source** | ✅ | ✅ | ✅ | ✅ |

## Community

- **Twitter**: [@marimo_io](https://twitter.com/marimo_io)
- **GitHub**: [github.com/marimo-team/marimo](https://github.com/marimo-team/marimo)
- **LinkedIn**: [marimo-io](https://www.linkedin.com/company/marimo-io)
- **YouTube**: [@marimo-team](https://www.youtube.com/@marimo-team)
- **Reddit**: [r/marimo_notebook](https://reddit.com/r/marimo_notebook)

## Related

- [[jupyter-live-kernel]] — Traditional Jupyter notebooks
- [[streamlit]] — Python web apps
- [[panel]] — Python dashboard library

---

*Last updated: 2026-04-27*
