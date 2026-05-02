---
id: bookmark
name: bookmark
description: Web page archiver that scrapes URLs, summarizes content, takes screenshots, and organizes bookmarks with Obsidian-like frontmatter
---

# Bookmark Skill - Web Page Archiver

## Description
This skill automatically scrapes web pages, summarizes content, takes screenshots, and organizes them into a structured bookmark system with Obsidian-like frontmatter.

## Usage
When you send a message containing a URL, this skill will:
1. **Scrape** the web page content
2. **Summarize** the content using an AI model
3. **Take a screenshot** of the page
4. **Create a structured markdown file** with:
   - Frontmatter (YAML) with metadata
   - Summary of the content
   - Screenshot embedded
   - Organized in domain-based folders

## Requirements
- Python 3.x with `requests`, `beautifulsoup4`, `pyppeteer` (for screenshots)
- An AI model API key (OpenAI, Claude, etc.)

## Configuration
Create a `config.json` in the bookmark skill directory with:
```json
{
  "ai_model": "anthropic/claude-3-5-sonnet-20241022",
  "ai_api_key": "",
  "base_dir": ""
}
```

## Output Structure
```
40-library/bookmarks/
├── example.com/
│   ├── url-path.md
│   └── url-path.png
└── another-domain.com/
    ├── url-path.md
    └── url-path.png
```

## Installation
```bash
VAULT_ROOT="${VAULT_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
cd "$VAULT_ROOT/50-system/skills/bookmark"
pip install -r requirements.txt
```

## Domain-Aware Routing (Manual Override)

When processing URLs, check for existing vault taxonomy before defaulting to domain-based folders:

### AI Content Routing
For AI-related URLs (providers, models, tools):
1. **Check existing structure first**: Look in `20-knowledge/ai/` for established categories
2. **Route by content type**:
   - **Providers** → `20-knowledge/ai/providers/[name].md`
   - **Models** → `20-knowledge/ai/models/[name].md`
   - **Tools** → `20-knowledge/ai/tools/[name].md`
   - **Concepts** → `20-knowledge/ai/concepts/[name].md`
3. **Follow existing templates**: Copy structure from similar files
4. **Research thoroughly**: Check Wikipedia, official docs, pricing pages
5. **Comprehensive frontmatter**: Include `founded`, `url`, `category`, `tags`, `pricing`
6. **Embed screenshots**: Save to `_assets/` and reference in markdown

### Research Checklist for AI Providers
- [ ] Wikipedia page for company background/founding
- [ ] Official docs for model specs and API
- [ ] Pricing page for cost structure
- [ ] GitHub/community for developer resources
- [ ] Compare with similar providers in vault

This approach ensures knowledge is curated into the existing taxonomy rather than dumped into generic folders.

## Error Handling
- Network errors: Retry up to 3 times
- Unsupported content: Save raw HTML with warning
- Missing title: Use URL as fallback
- Screenshot failure: Save without image

## Privacy Considerations
- No personal data collected beyond page content
- Files saved locally only
- No external API calls except for AI summarization
- Configurable to skip certain domains