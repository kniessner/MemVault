#!/usr/bin/env python3
"""
Agent Monitor — wrapper that runs collector + serves dashboard.
Usage: python monitor.py [port]
"""
import os
import sys
import time
import threading
from pathlib import Path

DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(DIR))

from collector import collect
from server import run_server

DATA = DIR / "data.json"
INTERVAL = 5  # seconds


def collector_loop():
    while True:
        try:
            data = collect()
            DATA.write_text(__import__("json").dumps(data, indent=2, default=str))
        except Exception as e:
            print("[collector error]", e)
        time.sleep(INTERVAL)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 39999
    # Start collector in background
    t = threading.Thread(target=collector_loop, daemon=True)
    t.start()
    # Start server (blocks)
    run_server(port)
