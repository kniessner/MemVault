#!/usr/bin/env python3
"""
vault_artifact.py — Store conversation artifacts into ClaudeVault.

Usage:
    python vault_artifact.py --type research --content "$CONTENT" --title "$TITLE" --provenance "$PROV"
    python vault_artifact.py --type session --session-id abc123 --summary "$SUMMARY"
    python vault_artifact.py --type bookmark --url https://example.com --title "Page Title"

This is a prototype for the vault_artifact() tool described in the vault improvement plan.
Future: integrate as a native Hermes tool.

Environment:
    CLAUDE_VAULT  - Path to vault root (default: ~/ClaudeVault)
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path


def get_vault_root() -> Path:
    """Resolve vault root from env or default."""
    root = os.environ.get("CLAUDE_VAULT", str(Path.home() / "ClaudeVault"))
    path = Path(root).expanduser().resolve()
    if not path.exists():
        print(f"Error: Vault root does not exist: {path}", file=sys.stderr)
        sys.exit(1)
    manifest = path / "VAULT_MANIFEST.json"
    if not manifest.exists():
        print(f"Warning: No VAULT_MANIFEST.json found at {path}", file=sys.stderr)
    return path


def slugify(text: str) -> str:
    """Convert text to kebab-case slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def make_frontmatter(data: dict) -> str:
    """Generate YAML frontmatter block."""
    lines = ["---"]
    for key, value in data.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {item}")
        elif isinstance(value, bool):
            lines.append(f"{key}: {str(value).lower()}")
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines)


def route_artifact(vault: Path, artifact_type: str, title: str) -> Path:
    """Determine destination path based on artifact type."""
    date_prefix = today()
    slug = slugify(title)

    routes = {
        "session": vault / "50-system/conversations" / "sessions" / f"{date_prefix}-{slug}.md",
        "research": vault / "50-system/conversations" / "research" / f"{date_prefix}-{slug}.md",
        "bookmark": vault / "50-system/conversations" / "bookmarks" / f"{slug}.md",
        "decision": vault / "50-system/conversations" / "research" / f"{date_prefix}-{slug}-decision.md",
        "code": vault / "50-system/conversations" / "research" / f"{date_prefix}-{slug}-code.md",
        "draft": vault / "00-inbox" / f"{date_prefix}-{slug}-draft.md",
    }

    default = vault / "50-system/conversations" / "_pending" / f"{date_prefix}-{slug}.md"
    return routes.get(artifact_type, default)


def write_artifact(path: Path, frontmatter: dict, body: str):
    """Write artifact file with frontmatter + body."""
    path.parent.mkdir(parents=True, exist_ok=True)
    content = make_frontmatter(frontmatter) + "\n\n" + body + "\n"
    path.write_text(content, encoding="utf-8")
    return path


def save_research(title: str, content: str, provenance: str, tags: list = None):
    """Save a research artifact."""
    vault = get_vault_root()
    path = route_artifact(vault, "research", title)
    fm = {
        "title": title,
        "created": today(),
        "classification": "research",
        "provenance": provenance,
        "reviewed": False,
        "target_layer": "20-knowledge",
        "tags": list(tags or []) + ["agent-review"],
    }
    body = f"# {title}\n\n*Classification: research | Reviewed: no*\n\n{content}\n\n---\n\n*Provenance: {provenance}*\n"
    write_artifact(path, fm, body)
    print(f"Saved research artifact: {path}")
    return str(path)


def save_session(session_id: str, summary: str, topics: list = None, provenance: str = ""):
    """Save a session summary artifact."""
    vault = get_vault_root()
    path = route_artifact(vault, "session", session_id)
    fm = {
        "title": f"Session {session_id}",
        "created": today(),
        "classification": "session",
        "session_id": session_id,
        "provenance": provenance,
        "topics": topics or [],
        "tags": ["session", "agent-review"],
    }
    body = f"# Session {session_id}\n\n## Summary\n\n{summary}\n\n---\n\n"
    if topics:
        body += "## Topics\n\n" + "\n".join(f"- {t}" for t in topics) + "\n\n"
    write_artifact(path, fm, body)
    print(f"Saved session artifact: {path}")
    return str(path)


def save_bookmark(url: str, title: str, extracted_text: str = ""):
    """Save a discovered bookmark for later processing by the bookmark skill."""
    vault = get_vault_root()
    path = route_artifact(vault, "bookmark", title)
    fm = {
        "title": title,
        "url": url,
        "created": today(),
        "classification": "bookmark",
        "reviewed": False,
        "target_layer": "40-library/bookmarks",
        "tags": ["bookmark", "agent-review"],
    }
    body = f"# {title}\n\nURL: {url}\n\n"
    if extracted_text:
        body += f"## Extracted Text\n\n{extracted_text[:2000]}\n\n"
    body += "---\n\n*Route to 40-library/bookmarks/ after review.*\n"
    write_artifact(path, fm, body)
    print(f"Saved bookmark draft: {path}")
    return str(path)


def main():
    parser = argparse.ArgumentParser(description="Store conversation artifacts into ClaudeVault")
    parser.add_argument("--type", required=True, choices=["research", "session", "bookmark", "decision", "code", "draft"])
    parser.add_argument("--title", required=True, help="Artifact title")
    parser.add_argument("--content", default="", help="Body content (for research/code/decision)")
    parser.add_argument("--provenance", default="", help="Tool/API source (e.g., 'tool:browser, api:github')")
    parser.add_argument("--session-id", default="", help="Session ID (for type=session)")
    parser.add_argument("--url", default="", help="URL (for type=bookmark)")
    parser.add_argument("--tags", default="", help="Comma-separated tags")

    args = parser.parse_args()
    tags = [t.strip() for t in args.tags.split(",") if t.strip()]

    if args.type == "research":
        save_research(args.title, args.content, args.provenance, tags)
    elif args.type == "session":
        save_session(args.session_id or slugify(args.title), args.content, tags, args.provenance)
    elif args.type == "bookmark":
        save_bookmark(args.url, args.title, args.content)
    elif args.type == "draft":
        vault = get_vault_root()
        path = route_artifact(vault, "draft", args.title)
        fm = {
            "title": args.title,
            "created": today(),
            "classification": "draft",
            "provenance": args.provenance,
            "reviewed": False,
            "tags": list(tags) + ["agent-review"],
        }
        write_artifact(path, fm, f"# {args.title}\n\n{args.content}\n")
        print(f"Saved draft to inbox: {path}")
    else:
        # decision, code fall through to generic
        vault = get_vault_root()
        path = route_artifact(vault, args.type, args.title)
        fm = {
            "title": args.title,
            "created": today(),
            "classification": args.type,
            "provenance": args.provenance,
            "reviewed": False,
            "target_layer": "30-projects-active" if args.type == "decision" else "50-system/conversations",
            "tags": list(tags) + ["agent-review"],
        }
        write_artifact(path, fm, f"# {args.title}\n\n{args.content}\n")
        print(f"Saved {args.type} artifact: {path}")


if __name__ == "__main__":
    main()
