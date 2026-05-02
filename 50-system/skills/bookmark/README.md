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
  "ai_api_key": "your_api_key_here",
  "base_dir": ""
}
```

## Output Structure
```
bookmarks/
├── example.com/
│   ├── 2025-09-03-example-title.md
│   └── 2025-09-03-example-title.png
└── another-domain.com/
    ├── 2025-09-03-another-title.md
    └── 2025-09-03-another-title.png
```

## Example Output
```markdown
---
template: default
image: "/api/dynamic-og?title=Coder+Desktop&description=Transform+remote+workspaces+into+seamless+local+development+environments+with+no+port+forwarding+required&badge=User+Guides+%3E+Coder+Desktop&header=Coder+Docs"
favicon: "/favicon-192x192-light.svg"
title: Coder Desktop | Coder Docs
source: https://coder.com/docs/user-guides/desktop
author: - Coder
published: created:
scraping_time: 2025-09-03T14:40:42+02:00
description: Coder is an innovative remote-first company specializing in the management of software development environments. It offers an enterprise platform and open-source tools focused on enhancing security and configuration. Backed by leading VC firms, Coder aims to simplify cloud software development processes.
tags: - bookmark - Coder - software development - enterprise platform - open-source tools - cloud environments - configuration - security - management - VC-backed
OpenAI GPT-3.5
domain: coder.com
site: Coder
provider: "OpenAI "
model: "GPT-3.5 "
---

![Coder Desktop](/api/dynamic-og?title=Coder+Desktop&description=Transform+remote+workspaces+into+seamless+local+development+environments+with+no+port+forwarding+required&badge=User+Guides+%3E+Coder+Desktop&header=Coder+Docs)

# Coder Desktop | Coder Docs

Coder is a remote-first company that provides an enterprise platform along with open-source tools designed to streamline the configuration, security, and management of software development environments in the cloud.

## Main

Transform remote workspaces into seamless local development environments with no port forwarding required

Troubleshooting
```

## Files
- `bookmark.py` - Main skill implementation
- `config.json` - Configuration file
- `README.md` - This documentation
- `requirements.txt` - Python dependencies

## Installation
```bash
VAULT_ROOT="${CLAUDE_VAULT:-$(git rev-parse --show-toplevel 2>/dev/null || find /Volumes /Users /home -type d -path '*/skills/bookmark' -prune 2>/dev/null | head -n1)}"
VAULT_ROOT="${VAULT_ROOT%/skills/bookmark}"
cd "$VAULT_ROOT/skills/bookmark"
pip install -r requirements.txt
```

## Usage Example
```
User: Check out this article: https://example.com/article
Skill: Processing... (scrapes, summarizes, takes screenshot, saves to bookmarks/example.com/)
Skill: Saved: bookmarks/example.com/2025-09-03-article-title.md
```

## Dependencies
- `requests` - for HTTP requests
- `beautifulsoup4` - for HTML parsing
- `pyppeteer` - for taking screenshots
- `pyyaml` - for YAML frontmatter
- `python-dateutil` - for date parsing
- An AI model API (OpenAI, Anthropic, etc.)

## Installation
```bash
VAULT_ROOT="${CLAUDE_VAULT:-$(git rev-parse --show-toplevel 2>/dev/null || find /Volumes /Users /home -type d -path '*/skills/bookmark' -prune 2>/dev/null | head -n1)}"
VAULT_ROOT="${VAULT_ROOT%/skills/bookmark}"
cd "$VAULT_ROOT/skills/bookmark"
pip install -r requirements.txt
```

## Usage

### From Command Line
```bash
VAULT_ROOT="${CLAUDE_VAULT:-$(git rev-parse --show-toplevel 2>/dev/null || find /Volumes /Users /home -type d -path '*/skills/bookmark' -prune 2>/dev/null | head -n1)}"
VAULT_ROOT="${VAULT_ROOT%/skills/bookmark}"
cd "$VAULT_ROOT/skills/bookmark"
python bookmark.py https://example.com/article
```

### From Within OpenClaw
When you send a message containing a URL, the skill will automatically:
1. Detect the URL
2. Scrape the page
3. Generate summary
4. Take screenshot
5. Save to bookmarks folder with proper structure

### Example
```
User: Check out this article: https://example.com/article
Skill: Processing... (scrapes, summarizes, takes screenshot, saves to bookmarks/example.com/)
Skill: Saved: bookmarks/example.com/2025-09-03-article-title.md
```

## Dependencies Installation
```bash
pip install requests beautifulsoup4 pyppeteer pyyaml python-dateutil
```

## Requirements Check
```bash
python -c "
import sys
try:
    import requests, bs4, pyppeteer, yaml, dateutil
    print('All dependencies installed')
except ImportError as e:
    print(f'Missing dependency: {e}')
"
```

## Testing
```bash
# Test URL detection
python -c "from bookmark import BookmarkSkill; skill = BookmarkSkill(); print(skill.detect_urls('Check https://example.com and http://test.com'))"

# Test scraping
python -c "from bookmark import BookmarkSkill; skill = BookmarkSkill(); print(skill.scrape_page('https://example.com'))"
```

## Error Handling
- Network errors: Retry up to 3 times
- Unsupported content: Save raw HTML with warning
- Missing title: Use URL as fallback
- Screenshot failure: Save without image
- AI API errors: Use simple summary

## Performance
- Screenshots optimized for web (JPEG, quality 80)
- Content truncated to first 10,000 characters for summarization
- Async operations where possible
- Caching of recent results (configurable TTL)

## Privacy Considerations
- No personal data collected beyond page content
- Files saved locally only
- No external API calls except for AI summarization
- Configurable to skip certain domains

## Extensibility
- Add custom templates via frontmatter
- Support for additional output formats (JSON, HTML)
- Plugin system for additional processors
- Custom AI model selection per domain

## License
MIT License - feel free to modify and use.
```

## Implementation

The skill works by:
1. Detecting URLs in messages
2. Creating the appropriate domain folder if it doesn't exist
3. Scraping the page content using `requests` + `BeautifulSoup`
4. Taking a screenshot using `pyppeteer`
5. Generating a summary using the configured AI model
6. Creating a markdown file with Obsidian-compatible frontmatter
7. Saving the screenshot alongside the markdown file

All files are organized by domain to keep the bookmark collection structured and searchable.
