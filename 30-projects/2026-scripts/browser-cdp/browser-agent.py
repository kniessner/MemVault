#!/usr/bin/env python3
"""
Human-like browser agent — connects to your REAL Brave/Chrome via CDP.
All your logins, cookies and extensions are preserved.

Prerequisites:
  1. Launch Brave with CDP:  DISPLAY=:0 ./launch-brave-cdp.sh
  2. Run this script:        ~/.venv-whisper/bin/python3 browser-agent.py "your task"

LLM Priority:
  1. Anthropic Claude (claude-sonnet-4-6)  — requires ANTHROPIC_API_KEY or config.json
  2. Ollama Cloud (ollama/kimi-k2.6:cloud) — automatic fallback on credit exhaustion

Examples:
  python3 browser-agent.py "Go to shore.de and extract the pricing"
  python3 browser-agent.py "Open https://www.capterra.com/p/141463/Shore-com/ and get the rating"
  python3 browser-agent.py "Log into LinkedIn and export the first 10 job postings for 'Product Manager'"
  python3 browser-agent.py "Search Google for 'Treatwell alternatives 2025' and summarize the top 5 results"
  python3 browser-agent.py --screenshot "Take a screenshot of the current tab"
  python3 browser-agent.py --ollama "Use Ollama directly without trying Anthropic first"
"""

import asyncio
import argparse
import json
import sys
import os
from pathlib import Path

CDP_URL      = os.environ.get("CDP_URL", "http://localhost:9222")
CONFIG       = Path.home() / "ClaudeVault/30-projects-active/2026-scripts/telegram-claude/config.json"
OLLAMA_HOST  = os.environ.get("OLLAMA_HOST", "https://ollama.com/v1")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "ollama/kimi-k2.6:cloud")
OLLAMA_KEY   = os.environ.get("OLLAMA_API_KEY", "")


def get_config():
    try:
        return json.loads(CONFIG.read_text())
    except Exception:
        return {}


def get_anthropic_key():
    cfg = get_config()
    return os.environ.get("ANTHROPIC_API_KEY") or cfg.get("apiKey", "")


def get_ollama_key():
    """Read Ollama API key from env or .env.local in intel-agent."""
    if OLLAMA_KEY:
        return OLLAMA_KEY
    env_local = Path.home() / "ClaudeVault/30-projects-active/2026-shore-intel/agents/intel-agent/.env.local"
    try:
        for line in env_local.read_text().splitlines():
            if line.startswith("OLLAMA_API_KEY="):
                return line.split("=", 1)[1].strip()
    except Exception:
        pass
    return ""


def make_anthropic_llm(api_key: str):
    from browser_use.llm.anthropic.chat import ChatAnthropic
    return ChatAnthropic(model="claude-sonnet-4-6", api_key=api_key)


def make_ollama_llm():
    """OpenAI-compatible Ollama Cloud client."""
    key = get_ollama_key()
    if not key:
        print("⚠️  OLLAMA_API_KEY not set — Ollama Cloud may reject requests")
    from langchain_openai import ChatOpenAI
    return ChatOpenAI(
        model=OLLAMA_MODEL,
        base_url="https://ollama.com/v1",
        api_key=key or "no-key",
        temperature=0.1,
    )


def make_llm(prefer_anthropic: bool = True):
    """Return (llm, provider_name). Anthropic primary, Ollama Cloud fallback."""
    anthropic_key = get_anthropic_key()

    if prefer_anthropic and anthropic_key:
        return make_anthropic_llm(anthropic_key), "anthropic/claude-sonnet-4-6"

    print(f"⚡ Using Ollama Cloud fallback: {OLLAMA_MODEL}")
    return make_ollama_llm(), f"ollama-cloud/{OLLAMA_MODEL}"


def is_credit_error(e: Exception) -> bool:
    msg = str(e).lower()
    return any(kw in msg for kw in ["credit", "balance", "402", "quota", "billing", "overloaded"])


async def run_task(task: str, use_ollama: bool = False):
    import httpx

    # Check CDP is available
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{CDP_URL}/json/version", timeout=3)
            info = r.json()
            print(f"🌐 Connected to: {info.get('Browser', '?')}")
    except Exception:
        print(f"❌ No browser available at {CDP_URL}")
        print("   Run first:  DISPLAY=:0 ./launch-brave-cdp.sh")
        sys.exit(1)

    from browser_use import Agent, Browser
    from browser_use.browser.profile import BrowserProfile

    llm, provider = make_llm(prefer_anthropic=not use_ollama)
    browser = Browser(browser_profile=BrowserProfile(cdp_url=CDP_URL))

    print(f"🤖 Task: {task}  [{provider}]\n")

    async def _run(llm_instance):
        agent = Agent(
            task=task,
            llm=llm_instance,
            browser=browser,
            max_actions_per_step=10,
            use_thinking=False,
            generate_gif=False,
        )
        return await agent.run(max_steps=30)

    try:
        result = await _run(llm)
    except Exception as e:
        if provider.startswith("anthropic") and is_credit_error(e):
            print(f"⚠️  Anthropic limit reached — switching to Ollama Cloud: {OLLAMA_MODEL}")
            result = await _run(make_ollama_llm())
        else:
            raise

    final = result.final_result() if result else None
    if final:
        print(f"\n✅ Result:\n{final}")
    else:
        print("\n⚠️ No final result extracted.")

    await browser.close()
    return final


async def take_screenshot(output: str = "/tmp/brave-screenshot.png"):
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(CDP_URL)
        contexts = browser.contexts
        if not contexts:
            print("No open browser contexts found.")
            return
        pages = contexts[0].pages
        if not pages:
            print("No open tabs found.")
            return
        page = pages[0]
        await page.screenshot(path=output, full_page=False)
        print(f"📸 Screenshot saved: {output}")
        await browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Human-like browser agent via CDP")
    parser.add_argument("task", nargs="?", help="Natural language task for the agent")
    parser.add_argument("--screenshot", metavar="FILE", nargs="?", const="/tmp/brave-screenshot.png",
                        help="Take a screenshot of the current tab")
    parser.add_argument("--ollama", action="store_true",
                        help=f"Use Ollama Cloud ({OLLAMA_MODEL}) directly, skip Anthropic")
    parser.add_argument("--cdp", default=CDP_URL, help=f"CDP URL (default: {CDP_URL})")
    args = parser.parse_args()

    CDP_URL = args.cdp

    if args.screenshot:
        asyncio.run(take_screenshot(args.screenshot))
    elif args.task:
        asyncio.run(run_task(args.task, use_ollama=args.ollama))
    else:
        parser.print_help()
        print(f"\nCDP status: ", end="")
        import subprocess
        r = subprocess.run(["curl", "-sf", f"{CDP_URL}/json/version"], capture_output=True)
        print("✅ available" if r.returncode == 0 else "❌ not running (launch with: DISPLAY=:0 ./launch-brave-cdp.sh)")
