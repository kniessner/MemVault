#!/usr/bin/env python3
"""
Bookmark Skill - Web Page Archiver

Automatically scrapes web pages, summarizes content, takes screenshots, and organizes them into a structured bookmark system with enhanced layout and content extraction.
"""

import os
import re
import json
import shutil
import datetime
import base64
from pathlib import Path
from urllib.parse import urlparse, quote, urljoin
from html import unescape

import requests
from bs4 import BeautifulSoup
import yaml
from dateutil import parser as date_parser
from dateutil.tz import tzlocal

try:
    import asyncio
    import aiohttp
    from pyppeteer import launch
    HAS_PYPPETEER = True
except ImportError:
    HAS_PYPPETEER = False


class BookmarkSkill:
    """Bookmark skill implementation."""

    def __init__(self):
        self.config = self.load_config()
        vault_root = Path(os.environ.get("VAULT_ROOT") or Path(__file__).resolve().parents[3])
        base_dir = self.config.get("base_dir")
        self.base_dir = Path(base_dir).expanduser() if base_dir else vault_root / "40-library" / "bookmarks"
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.ai_model = self.config.get("ai_model", "anthropic/claude-3-5-sonnet-20241022")
        self.ai_api_key = self.config.get("ai_api_key")
        self.screenshot_quality = self.config.get("screenshot_quality", 80)
        self.max_content_length = self.config.get("max_content_length", 15000)
        
    def load_config(self):
        """Load configuration from config.json."""
        config_path = Path(__file__).parent / "config.json"
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def detect_urls(self, text):
        """Detect URLs in text using regex."""
        url_pattern = re.compile(r'https?://(?:[\w-]+\.)+[\w-]+(?:/[\w- .,&?=%+#-]*)?')
        return url_pattern.findall(text)

    def get_domain(self, url):
        """Extract domain from URL."""
        parsed = urlparse(url)
        domain = parsed.netloc
        # Remove www. prefix if present
        if domain.startswith("www."):
            domain = domain[4:]
        return domain

    def create_domain_folder(self, domain):
        """Create domain folder if it doesn't exist."""
        domain_dir = self.base_dir / domain
        domain_dir.mkdir(exist_ok=True)
        return domain_dir

    def clean_text(self, text):
        """Clean and normalize text."""
        if not text:
            return ""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove control characters
        text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', text)
        return text.strip()

    def extract_metadata(self, soup, url):
        """Extract comprehensive metadata from the page."""
        metadata = {
            'title': '',
            'description': '',
            'author': '',
            'published': '',
            'modified': '',
            'image': '',
            'favicon': '',
            'site_name': '',
            'keywords': '',
            'language': ''
        }
        
        # Title
        if soup.title:
            metadata['title'] = self.clean_text(soup.title.string)
        
        # Meta tags
        meta_tags = {
            'description': 'name',
            'author': 'name',
            'keywords': 'name',
            'language': 'name',
            'published': 'property',  # og:article:published_time
            'modified': 'property',  # og:article:modified_time
            'image': 'property',  # og:image
            'site_name': 'property',  # og:site_name
        }
        
        for key, attr_type in meta_tags.items():
            if attr_type == 'name':
                tag = soup.find('meta', attrs={'name': key})
            else:
                tag = soup.find('meta', attrs={'property': f'og:{key}'})
            
            if tag and tag.get('content'):
                metadata[key] = self.clean_text(tag.get('content'))
        
        # Twitter cards
        twitter_title = soup.find('meta', attrs={'name': 'twitter:title'})
        if twitter_title and not metadata['title']:
            metadata['title'] = self.clean_text(twitter_title.get('content'))
        
        twitter_desc = soup.find('meta', attrs={'name': 'twitter:description'})
        if twitter_desc and not metadata['description']:
            metadata['description'] = self.clean_text(twitter_desc.get('content'))
        
        twitter_image = soup.find('meta', attrs={'name': 'twitter:image'})
        if twitter_image and not metadata['image']:
            metadata['image'] = twitter_image.get('content')
        
        # Favicon
        favicon = soup.find('link', rel=re.compile(r'icon', re.I))
        if favicon and favicon.get('href'):
            favicon_href = favicon.get('href')
            if not favicon_href.startswith('http'):
                favicon_href = urljoin(url, favicon_href)
            metadata['favicon'] = favicon_href
        
        # Fallback title from h1
        if not metadata['title']:
            h1 = soup.find('h1')
            if h1:
                metadata['title'] = self.clean_text(h1.get_text())
        
        # Fallback description from first paragraph
        if not metadata['description']:
            first_p = soup.find('p')
            if first_p:
                metadata['description'] = self.clean_text(first_p.get_text())[:200]
        
        return metadata

    def extract_content(self, soup):
        """Extract main content from the page with better structure."""
        content_sections = {}
        
        # Remove unwanted elements
        for unwanted in soup(['script', 'style', 'nav', 'header', 'footer', 'aside', 'iframe', 'noscript', 'form', 'button']):
            unwanted.decompose()
        
        # Try to find main content areas
        main_content = soup.find('main') or soup.find('article') or soup.find('div', class_=re.compile(r'content|article|post|entry', re.I)) or soup.body
        
        if not main_content:
            main_content = soup
        
        # Extract headings and their content
        headings = {}
        current_heading = 'Introduction'
        headings[current_heading] = []
        
        for element in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'li', 'blockquote', 'pre', 'code', 'table']):
            if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                heading_text = self.clean_text(element.get_text())
                if heading_text:
                    current_heading = heading_text
                    headings[current_heading] = []
            else:
                text = self.clean_text(element.get_text())
                if text and len(text) > 20:  # Skip very short texts
                    headings[current_heading].append({
                        'type': element.name,
                        'text': text
                    })
        
        # Flatten into structured content
        content_sections['headings'] = headings
        content_sections['main'] = []
        
        # Extract key points (first few meaningful paragraphs)
        for p in main_content.find_all('p'):
            text = self.clean_text(p.get_text())
            if text and len(text) > 50:
                content_sections['main'].append(text)
                if len(content_sections['main']) >= 10:
                    break
        
        # Extract lists
        content_sections['lists'] = []
        for ul in main_content.find_all(['ul', 'ol'])[:5]:
            items = []
            for li in ul.find_all('li')[:10]:
                text = self.clean_text(li.get_text())
                if text:
                    items.append(text)
            if items:
                content_sections['lists'].append({
                    'type': ul.name,
                    'items': items
                })
        
        # Extract code blocks
        content_sections['code'] = []
        for pre in main_content.find_all('pre')[:5]:
            code = pre.get_text()
            if code and len(code) > 20:
                content_sections['code'].append(code[:1000])  # Limit code length
        
        return content_sections

    def extract_links(self, soup, base_url):
        """Extract relevant links from the page."""
        links = []
        seen_urls = set()
        
        for a in soup.find_all('a', href=True):
            href = a.get('href')
            text = self.clean_text(a.get_text())
            
            if not text or len(text) < 3:
                continue
            
            # Skip anchor links and empty hrefs
            if href.startswith('#') or href.startswith('javascript:'):
                continue
            
            # Resolve relative URLs
            if not href.startswith('http'):
                href = urljoin(base_url, href)
            
            # Skip if already seen
            if href in seen_urls:
                continue
            
            seen_urls.add(href)
            
            # Only keep internal or related links (same domain)
            if self.get_domain(href) == self.get_domain(base_url) or len(links) < 10:
                links.append({
                    'text': text[:100],
                    'url': href
                })
            
            if len(links) >= 20:
                break
        
        return links

    def scrape_page(self, url):
        """Scrape web page content with enhanced extraction."""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
            }
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            # Handle encoding
            encoding = response.encoding or 'utf-8'
            if 'charset' not in response.headers.get('Content-Type', ''):
                # Try to detect encoding from content
                if response.content:
                    try:
                        from chardet import detect
                        detected = detect(response.content)
                        if detected and detected.get('encoding'):
                            encoding = detected['encoding']
                    except ImportError:
                        pass
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract metadata
            metadata = self.extract_metadata(soup, url)
            
            # Extract content
            content = self.extract_content(soup)
            
            # Extract links
            links = self.extract_links(soup, url)
            
            # Get full text content for summary
            full_text = ""
            for section_text in content['main']:
                full_text += section_text + "\n"
            
            # Also get heading content
            for heading, texts in content['headings'].items():
                for item in texts:
                    full_text += item['text'] + "\n"
            
            return {
                'url': url,
                'title': metadata['title'] or url,
                'description': metadata['description'],
                'author': metadata['author'],
                'published': metadata['published'],
                'modified': metadata['modified'],
                'image': metadata['image'],
                'favicon': metadata['favicon'],
                'site_name': metadata['site_name'] or self.get_domain(url).split('.')[0],
                'keywords': metadata['keywords'],
                'content': content,
                'links': links,
                'full_text': full_text.strip()[:self.max_content_length],
                'html': str(soup)
            }
            
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return None

    async def take_screenshot(self, url, output_path):
        """Take screenshot of web page."""
        if not HAS_PYPPETEER:
            print("Pyppeteer not available, skipping screenshot")
            return False
            
        try:
            browser = await launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])
            page = await browser.newPage()
            
            await page.setViewport({
                'width': 1280,
                'height': 720,
                'deviceScaleFactor': 1,
            })
            
            await page.goto(url, waitUntil='networkidle2')
            
            # Wait a bit for dynamic content
            await asyncio.sleep(2)
            
            await page.screenshot({
                'path': str(output_path),
                'quality': self.screenshot_quality,
                'type': 'jpeg'
            })
            
            await browser.close()
            return True
            
        except Exception as e:
            print(f"Error taking screenshot: {e}")
            return False

    def generate_tags(self, data):
        """Generate relevant tags from content."""
        tags = ['bookmark']
        
        # Add domain as tag (replace dots with hyphens)
        domain = self.get_domain(data['url'])
        tags.append(domain.replace('.', '-'))
        
        # Content-based tagging
        content_lower = data.get('full_text', '').lower()
        title_lower = data.get('title', '').lower()
        desc_lower = data.get('description', '').lower()
        combined = content_lower + title_lower + desc_lower
        
        # Tech/Development tags
        tech_keywords = {
            'python': 'python',
            'javascript': 'javascript',
            'typescript': 'typescript',
            'react': 'react',
            'vue': 'vue',
            'angular': 'angular',
            'nodejs': 'nodejs',
            'docker': 'docker',
            'kubernetes': 'kubernetes',
            'aws': 'aws',
            'azure': 'azure',
            'gcp': 'gcp',
            'linux': 'linux',
            'ubuntu': 'ubuntu',
            'debian': 'debian',
            'bash': 'bash',
            'shell': 'shell',
            'git': 'git',
            'api': 'api',
            'rest': 'rest',
            'graphql': 'graphql',
            'database': 'database',
            'sql': 'sql',
            'postgres': 'postgresql',
            'mysql': 'mysql',
            'mongodb': 'mongodb',
            'redis': 'redis',
            'machine learning': 'machine-learning',
            'deep learning': 'deep-learning',
            'ai': 'ai',
            'llm': 'llm',
            'gpt': 'gpt',
            'cloud': 'cloud',
            'devops': 'devops',
            'cicd': 'cicd',
            'security': 'security',
            'authentication': 'authentication',
            'oauth': 'oauth',
            'encryption': 'encryption',
            'tutorial': 'tutorial',
            'guide': 'guide',
            'documentation': 'documentation',
            'reference': 'reference',
            'cheat sheet': 'cheatsheet',
        }
        
        for keyword, tag in tech_keywords.items():
            if keyword in combined and tag not in tags:
                tags.append(tag)
        
        # Topic-based tagging
        topics = {
            'server': 'server',
            'network': 'network',
            'monitoring': 'monitoring',
            'backup': 'backup',
            'storage': 'storage',
            'virtualization': 'virtualization',
            'automation': 'automation',
            'configuration': 'configuration',
            'installation': 'installation',
            'setup': 'setup',
            'troubleshooting': 'troubleshooting',
            'optimization': 'optimization',
            'performance': 'performance',
            'debugging': 'debugging',
            'testing': 'testing',
            'deployment': 'deployment',
            'architecture': 'architecture',
            'design pattern': 'design-pattern',
        }
        
        for keyword, tag in topics.items():
            if keyword in combined and tag not in tags:
                tags.append(tag)
        
        return list(set([tag.replace('.', '-') for tag in tags]))[:15]  # Limit to 15 tags, replace dots with hyphens

    def generate_summary(self, data):
        """Generate a better summary from the content."""
        # Try to use description first
        if data.get('description'):
            return data['description']
        
        # Otherwise, generate from content
        content = data.get('full_text', '')
        if not content:
            return data.get('title', 'No content available')
        
        # Get first few meaningful sentences
        sentences = content.split('. ')
        summary = ""
        for sentence in sentences[:5]:
            if len(summary + sentence) < 300:
                summary += sentence + ". "
            else:
                break
        
        return summary.strip() or data.get('title', 'No summary available')

    def generate_frontmatter(self, data):
        """Generate YAML frontmatter."""
        now = datetime.datetime.now(tzlocal())
        scraping_time = now.isoformat()
        
        domain = self.get_domain(data['url'])
        site = data.get('site_name') or domain.split('.')[0].capitalize()
        
        # Generate tags
        tags = self.generate_tags(data)
        
        # Handle image URL
        image = data.get('image', '')
        if image and not image.startswith('http'):
            image = urljoin(data['url'], image)
        
        # Handle favicon
        favicon = data.get('favicon', '')
        if favicon and not favicon.startswith('http'):
            favicon = urljoin(data['url'], favicon)
        
        # Parse published date if available
        published = data.get('published', '')
        if published:
            try:
                dt = date_parser.parse(published)
                published = dt.isoformat()
            except:
                pass
        
        # Build frontmatter
        now = datetime.datetime.now(tzlocal())
        date_str = now.strftime('%Y-%m-%d')
        
        frontmatter = {
            'template': 'bookmark',
            'title': data['title'][:200],
            'source': data['url'],
            'author': data['author'] if data.get('author') else site,
            'published': published,
            'scraped': scraping_time,
            'date-created': date_str,
            'date-updated': date_str,
            'description': (data['description'] or '')[:500],
            'tags': tags,
            'domain': domain,
            'site': site,
            'image': image,
            'favicon': favicon,
        }
        
        return frontmatter

    def generate_filename_from_url(self, url):
        """Generate filename from URL path with query hash for uniqueness."""
        import hashlib
        parsed = urlparse(url)
        path = parsed.path.strip('/')
        query = parsed.query
        
        # Get the last part of the path (file or slug)
        if '/' in path:
            # Use the full path structure, e.g., "cheahjs/free-llm-api-resources"
            filename = path.replace('/', '-')
        elif path:
            filename = path
        else:
            # Use domain if no path
            filename = parsed.netloc.replace('www.', '')
        
        # Clean the filename
        filename = re.sub(r'[^\w\-]', '', filename)
        filename = filename[:100]  # Leave room for hash
        
        # Add hash of full URL to handle query parameters uniquely
        # This prevents overwrites for URLs like page?id=123 vs page?id=456
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        filename = f"{filename}-{url_hash}"
        
        if not filename:
            filename = f"index-{url_hash}"
        
        return filename + '.md'

    def save_bookmark(self, data):
        """Save bookmark to file with enhanced layout."""
        domain = self.get_domain(data['url'])
        domain_dir = self.create_domain_folder(domain)
        
        # Generate filename from URL path (new format)
        filename = self.generate_filename_from_url(data['url'])
        
        # Generate frontmatter
        frontmatter = self.generate_frontmatter(data)
        
        # Generate summary
        summary = self.generate_summary(data)
        
        # Build markdown content
        content_parts = []
        
        # Frontmatter
        content_parts.append("---\n")
        content_parts.append(yaml.dump(frontmatter, sort_keys=False, allow_unicode=True))
        content_parts.append("---\n\n")
        
        # Title and metadata
        content_parts.append(f"# {data['title']}\n\n")
        
        # Quick info
        content_parts.append(f"> **Source:** [{domain}]({data['url']})\n")
        if data.get('author'):
            content_parts.append(f"> **Author:** {data['author']}\n")
        if data.get('published'):
            content_parts.append(f"> **Published:** {data['published'][:10]}\n")
        content_parts.append(f"> **Scraped:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        
        # Description/Summary
        if data.get('description'):
            content_parts.append(f"## Summary\n\n{data['description']}\n\n")
        
        # AI Summary (if available, otherwise use generated)
        content_parts.append(f"## Overview\n\n{summary}\n\n")
        
        # Key Points (from content)
        if data.get('content', {}).get('main'):
            content_parts.append("## Key Points\n\n")
            for i, point in enumerate(data['content']['main'][:8], 1):
                # Clean and shorten points
                point = point[:300]
                if point.endswith('.'):
                    point = point[:-1]
                content_parts.append(f"{i}. {point}...\n")
            content_parts.append("\n")
        
        # Table of Contents (from headings)
        headings = data.get('content', {}).get('headings', {})
        if len(headings) > 1:
            content_parts.append("## Table of Contents\n\n")
            for heading in list(headings.keys())[:10]:
                if heading != 'Introduction':
                    anchor = heading.lower().replace(' ', '-').replace('.', '')
                    content_parts.append(f"- [{heading}](#{anchor})\n")
            content_parts.append("\n")
        
        # Content sections
        content_parts.append("---\n\n")
        content_parts.append("# Content\n\n")
        
        for heading, items in headings.items():
            if heading != 'Introduction' and items:
                # Create anchor
                anchor = heading.lower().replace(' ', '-').replace('.', '')
                content_parts.append(f"## {heading} {{#{anchor}}}\n\n")
            
            for item in items[:5]:  # Limit items per heading
                if item['type'] == 'p':
                    content_parts.append(f"{item['text']}\n\n")
                elif item['type'] in ['ul', 'ol']:
                    # This would be handled in lists section
                    pass
                elif item['type'] in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    pass  # Already handled by heading
                else:
                    content_parts.append(f"{item['text']}\n\n")
        
        # Code blocks
        code_blocks = data.get('content', {}).get('code', [])
        if code_blocks:
            content_parts.append("---\n\n")
            content_parts.append("## Code Examples\n\n")
            for i, code in enumerate(code_blocks[:3], 1):
                content_parts.append(f"```\n{code}\n```\n\n")
        
        # Lists
        lists = data.get('content', {}).get('lists', [])
        if lists:
            content_parts.append("---\n\n")
            content_parts.append("## Lists\n\n")
            for lst in lists[:3]:
                content_parts.append(f"### {lst['type'].upper()} List\n\n")
                for item in lst['items'][:10]:
                    content_parts.append(f"- {item}\n")
                content_parts.append("\n")
        
        # Related Links
        links = data.get('links', [])
        if links:
            content_parts.append("---\n\n")
            content_parts.append("## Related Links\n\n")
            for link in links[:10]:
                content_parts.append(f"- [{link['text']}]({link['url']})\n")
            content_parts.append("\n")
        
        # Raw content (truncated)
        content_parts.append("---\n\n")
        content_parts.append("## Raw Content\n\n")
        content_parts.append(f"> ⚠️ *Auto-extracted content, may contain noise*\n\n")
        
        full_text = data.get('full_text', '')
        if full_text:
            # Split into paragraphs
            paragraphs = full_text.split('\n')
            for para in paragraphs[:30]:
                if para.strip():
                    content_parts.append(f"{para.strip()}\n\n")
        
        # Join and save
        content = ''.join(content_parts)
        
        filepath = domain_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Saved bookmark: {filepath}")
        
        return filepath

    def process_url(self, url):
        """Process a single URL."""
        print(f"Processing URL: {url}")
        
        # Scrape the page
        data = self.scrape_page(url)
        if not data:
            print(f"Failed to scrape {url}")
            return None
        
        # Take screenshot
        screenshot_path = None
        if HAS_PYPPETEER:
            timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            screenshot_filename = f"{timestamp}.jpg"
            screenshot_path = Path(f"/tmp/{screenshot_filename}")
            asyncio.run(self.take_screenshot(url, screenshot_path))
            
            # Copy screenshot to bookmark folder
            if screenshot_path and screenshot_path.exists():
                domain = self.get_domain(url)
                domain_dir = self.create_domain_folder(domain)
                screenshot_dest = domain_dir / screenshot_path.name
                shutil.copy(screenshot_path, screenshot_dest)
                print(f"Saved screenshot: {screenshot_dest}")
        
        # Save bookmark
        filepath = self.save_bookmark(data)
        
        return filepath

    def process_message(self, message):
        """Process a message containing URLs."""
        urls = self.detect_urls(message)
        if not urls:
            print("No URLs found in message")
            return
        
        results = []
        for url in urls:
            try:
                result = self.process_url(url)
                if result:
                    results.append(result)
            except Exception as e:
                print(f"Error processing {url}: {e}")
        
        return results


# Main entry point
if __name__ == "__main__":
    import sys
    
    skill = BookmarkSkill()
    
    if len(sys.argv) > 1:
        # Process command line arguments
        for arg in sys.argv[1:]:
            skill.process_url(arg)
    else:
        # Read from stdin
        try:
            message = input("Enter message with URLs: ")
            skill.process_message(message)
        except EOFError:
            pass
