#!/usr/bin/env python3
"""
Agent Monitor Server — serves dashboard HTML + JSON API + actions.
"""
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

DIR = Path(__file__).parent.resolve()
DATA_FILE = DIR / "data.json"

def load_data():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text())
        except Exception:
            pass
    return {"error": "No data yet — collector is running"}


def run(cmd: str, timeout: int = 15) -> tuple[int, str, str]:
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except subprocess.TimeoutExpired:
        return 1, "", "timeout"
    except Exception as e:
        return 1, "", str(e)


def handle_action(action: str, target: str):
    """Execute safe system actions."""
    home = str(Path.home())
    result = {"success": False, "output": "", "error": ""}

    # Systemd service actions
    if action in ("restart", "stop", "start", "status", "logs"):
        svc = target
        if not svc.endswith(".service"):
            svc += ".service"
        if action == "logs":
            rc, out, err = run(f"journalctl --user -u {svc} -n 100 --no-pager", timeout=10)
        else:
            rc, out, err = run(f"systemctl --user {action} {svc} 2>&1", timeout=20)
        result["success"] = rc == 0
        result["output"] = out or err
        return result

    # Agent start actions
    if action == "start_agent":
        if target == "opencode":
            rc, out, err = run(f"cd /mnt/newhome/knssnr/CVault && opencode serve --port 39023 >/dev/null 2>&1 &", timeout=3)
        elif target == "codex":
            rc, out, err = run(f"cd /mnt/newhome/knssnr/CVault && codex >/dev/null 2>&1 &", timeout=3)
        else:
            rc, out, err = 1, "", f"Unknown agent: {target}"
        result["success"] = rc == 0
        result["output"] = out or err
        return result

    # Read log file
    if action == "read_logs":
        if os.path.exists(target):
            try:
                with open(target) as f:
                    lines = f.readlines()[-200:]
                    result["success"] = True
                    result["output"] = "".join(lines)
            except Exception as e:
                result["error"] = str(e)
        else:
            result["error"] = f"Log file not found: {target}"
        return result

    # Tail log file
    if action == "tail_logs":
        if os.path.exists(target):
            rc, out, err = run(f"tail -n 50 '{target}'", timeout=5)
            result["success"] = rc == 0
            result["output"] = out or err
        else:
            result["error"] = f"Log file not found: {target}"
        return result

    if action == "kill_pid":
        rc, out, err = run(f"kill {target} 2>&1", timeout=5)
        result["success"] = rc == 0
        result["output"] = out or err
        return result

    if action == "docker_restart":
        rc, out, err = run(f"docker restart {target} 2>&1", timeout=30)
        result["success"] = rc == 0
        result["output"] = out or err
        return result

    if action == "docker_logs":
        rc, out, err = run(f"docker logs --tail 50 {target} 2>&1", timeout=10)
        result["success"] = rc == 0
        result["output"] = out or err
        return result

    result["error"] = f"Unknown action: {action}"
    return result


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/api/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(load_data()).encode())
            return

        if path == "/api/action":
            qs = parse_qs(parsed.query)
            action = qs.get("action", [""])[0]
            target = qs.get("target", [""])[0]
            result = handle_action(action, target)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
            return

        if path == "/" or path == "/index.html":
            html_file = DIR / "index.html"
            if html_file.exists():
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(html_file.read_bytes())
                return

        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"Not found")

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.end_headers()


def run_server(port=39999):
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"Agent Monitor running at http://0.0.0.0:{port}/")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 39999
    run_server(port)
