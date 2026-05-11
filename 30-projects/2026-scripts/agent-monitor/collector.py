#!/usr/bin/env python3
"""
Agent Monitor Collector — gathers live system state for the dashboard.
Includes health checks, rolling history, and log tailing.
"""
import json
import os
import re
import subprocess
import time
import urllib.request
import urllib.error
from dataclasses import dataclass, asdict, field
from pathlib import Path
from typing import Any
from collections import deque

HOME = Path.home()
VAULT = Path("/mnt/newhome/knssnr/CVault")
HISTORY_FILE = Path(__file__).parent / "history.json"
MAX_HISTORY = 120  # 120 * 5s = 10 minutes


def run(cmd: str, timeout: int = 10) -> str:
    try:
        return subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=timeout
        ).stdout.strip()
    except Exception:
        return ""


def get_ip() -> str:
    return run("ip route get 1.1.1.1 | awk '{print $7; exit}'", timeout=3) or "localhost"


def check_health(url: str, timeout: int = 3) -> dict:
    """Ping a URL and return health status."""
    if not url:
        return {"status": "unknown", "latency_ms": None, "code": None}
    start = time.time()
    try:
        req = urllib.request.Request(url, method="HEAD")
        req.add_header("User-Agent", "AgentMonitor/1.0")
        resp = urllib.request.urlopen(req, timeout=timeout)
        latency = int((time.time() - start) * 1000)
        return {"status": "online", "latency_ms": latency, "code": resp.status}
    except urllib.error.HTTPError as e:
        latency = int((time.time() - start) * 1000)
        return {"status": "online", "latency_ms": latency, "code": e.code}
    except Exception:
        return {"status": "offline", "latency_ms": None, "code": None}


def load_history() -> dict:
    if HISTORY_FILE.exists():
        try:
            return json.loads(HISTORY_FILE.read_text())
        except Exception:
            pass
    return {
        "timestamps": [],
        "total_cpu": [],
        "total_mem": [],
        "agent_cpu": {},
        "agent_mem": {},
    }


def save_history(hist: dict, agents: list[dict]):
    # Append current point
    now = time.strftime("%H:%M:%S")
    hist["timestamps"].append(now)
    total_cpu = sum(a.get("cpu_percent", 0) for a in agents)
    total_mem = sum(a.get("mem_percent", 0) for a in agents)
    hist["total_cpu"].append(round(total_cpu, 1))
    hist["total_mem"].append(round(total_mem, 1))

    for a in agents:
        name = a["name"]
        hist.setdefault("agent_cpu", {}).setdefault(name, []).append(a.get("cpu_percent", 0))
        hist.setdefault("agent_mem", {}).setdefault(name, []).append(a.get("mem_percent", 0))

    # Trim to MAX_HISTORY
    for key in ["timestamps", "total_cpu", "total_mem"]:
        if len(hist[key]) > MAX_HISTORY:
            hist[key] = hist[key][-MAX_HISTORY:]
    for cat in ["agent_cpu", "agent_mem"]:
        for name in hist.get(cat, {}):
            if len(hist[cat][name]) > MAX_HISTORY:
                hist[cat][name] = hist[cat][name][-MAX_HISTORY:]

    HISTORY_FILE.write_text(json.dumps(hist, indent=2, default=str))
    return hist


def tail_file(path: str, lines: int = 50) -> list[str]:
    try:
        p = Path(path)
        if not p.exists():
            return []
        out = run(f"tail -n {lines} '{path}'", timeout=3)
        return out.splitlines()[-lines:]
    except Exception:
        return []


@dataclass
class AgentInfo:
    name: str
    display_name: str
    installed: bool
    version: str = ""
    running: bool = False
    pids: list[int] | None = None
    cpu_percent: float = 0.0
    mem_percent: float = 0.0
    config_dir: str = ""
    sessions: list[str] | None = None
    last_activity: str | None = None
    log_tail: list[str] | None = None
    model: str = ""
    provider: str = ""
    port: int | None = None
    url: str = ""
    health: dict = field(default_factory=lambda: {"status": "unknown", "latency_ms": None, "code": None})
    log_file: str = ""


@dataclass
class ServiceInfo:
    name: str
    description: str = ""
    state: str = "unknown"
    sub_state: str = ""
    enabled: bool = False
    pid: int | None = None
    uptime: str = ""


@dataclass
class CronJob:
    source: str
    schedule: str
    command: str
    user: str = ""
    enabled: bool = True


@dataclass
class Listener:
    protocol: str
    local_address: str
    port: int
    pid: int | None
    process: str
    container: str = ""


@dataclass
class DockerContainer:
    name: str
    image: str
    ports: str
    status: str
    uptime: str


@dataclass
class AgentTask:
    agent: str
    command: str
    pid: int
    cpu: float
    mem: float
    start_time: str


def get_agent_processes() -> dict[str, list[dict]]:
    procs: dict[str, list[dict]] = {}
    patterns = {
        "opencode": r"opencode(?!-telegram)",
        "opencode-telegram": r"opencode-telegram|opencode telegram",
        "claude-code": r"\bclaude\b(?!-telegram| .*--version| .*-msg| .*bridge)",
        "codex": r"\bcodex\b",
        "hermes": r"hermes_cli|hermes-agent",
        "telegram-claude-bot": r"telegram-claude.*bot\.js|bot\.js.*telegram",
        "telegram-cli-bridge": r"telegram-cli-bridge",
        "whisper-server": r"whisper-server",
        "chroma": r"chromadb",
        "open-webui": r"open_webui|openwebui",
        "searxng": r"searxng",
        "homepage": r"next-server.*homepage|homepage.*next",
        "caddy": r"\bcaddy\b",
        "camofox": r"camoufox|camofox",
    }
    ps_output = run("ps aux", timeout=5)
    for line in ps_output.splitlines()[1:]:
        parts = line.split()
        if len(parts) < 11:
            continue
        try:
            pid = int(parts[1])
            cpu = float(parts[2])
            mem = float(parts[3])
            cmdline = " ".join(parts[10:])
        except (ValueError, IndexError):
            continue
        for name, pat in patterns.items():
            if re.search(pat, cmdline, re.I):
                procs.setdefault(name, []).append(
                    {"pid": pid, "cpu": cpu, "mem": mem, "cmd": cmdline[:120]}
                )
    return procs


def get_version(cmd: str) -> str:
    for flag in ["--version", "-v", "version"]:
        out = run(f"{cmd} {flag} 2>&1", timeout=3)
        if out and "not found" not in out.lower() and "error" not in out.lower() and "EACCES" not in out and len(out) < 100:
            first = out.splitlines()[0][:80]
            if first and not first.startswith("/") and not first.startswith("mkdir"):
                return first
    return ""


def get_installed_agents(procs: dict, ip: str) -> list[AgentInfo]:
    agents = []

    # OpenCode
    opencode_bin = HOME / ".opencode/bin/opencode"
    oc_installed = opencode_bin.exists() or run("which opencode")
    oc_version = ""
    if opencode_bin.exists():
        oc_version = get_version(str(opencode_bin))
        if not oc_version or "EACCES" in oc_version or "mkdir" in oc_version:
            pkg = HOME / ".opencode/package.json"
            if pkg.exists():
                try:
                    oc_version = "opencode " + json.loads(pkg.read_text()).get("dependencies", {}).get("@opencode-ai/plugin", "")
                except Exception:
                    pass
    oc_pids = [p["pid"] for p in procs.get("opencode", [])]
    oc_port = None
    oc_url = ""
    oc_model = ""
    if oc_installed:
        for p in procs.get("opencode", []):
            m = re.search(r"--port\s+(\d+)", p["cmd"])
            if m:
                oc_port = int(m.group(1))
                break
        if not oc_port:
            ss = run("ss -tlnp | grep opencode")
            m = re.search(r":(\d+)", ss)
            if m:
                oc_port = int(m.group(1))
        if oc_port:
            oc_url = f"http://{ip}:{oc_port}/"
        cfg = HOME / ".opencode/config.toml"
        if cfg.exists():
            txt = cfg.read_text()
            m = re.search(r'^model\s*=\s*"([^"]+)"', txt, re.M)
            if m:
                oc_model = m.group(1)
    agents.append(
        AgentInfo(
            name="opencode", display_name="OpenCode", installed=bool(oc_installed),
            version=oc_version, running=bool(oc_pids), pids=oc_pids or [],
            config_dir=str(HOME / ".opencode"), port=oc_port, url=oc_url, model=oc_model,
            log_file=str(HOME / ".opencode/log"),
        )
    )

    # Claude Code
    cc_bin = HOME / ".local/bin/claude"
    cc_installed = cc_bin.exists() or run("which claude")
    cc_pids = [p["pid"] for p in procs.get("claude-code", [])]
    cc_sessions = []
    sess_dir = HOME / ".claude/sessions"
    if sess_dir.exists():
        cc_sessions = sorted([f.name for f in sess_dir.iterdir() if f.suffix == ".json"])
    agents.append(
        AgentInfo(
            name="claude-code", display_name="Claude Code", installed=bool(cc_installed),
            version=get_version(str(cc_bin)) if cc_bin.exists() else "",
            running=bool(cc_pids), pids=cc_pids or [], config_dir=str(HOME / ".claude"),
            sessions=cc_sessions, model="gpt-5.4", provider="OpenAI",
        )
    )

    # Codex
    codex_installed = run("which codex")
    codex_pids = [p["pid"] for p in procs.get("codex", [])]
    agents.append(
        AgentInfo(
            name="codex", display_name="Codex (OpenAI)", installed=bool(codex_installed),
            version=get_version("codex") if codex_installed else "",
            running=bool(codex_pids), pids=codex_pids or [], config_dir=str(HOME / ".codex"),
            model="gpt-5.4", provider="OpenAI",
        )
    )

    # Hermes
    hermes_dir = HOME / ".hermes"
    hermes_installed = (hermes_dir / "hermes-agent").exists()
    hermes_pids = [p["pid"] for p in procs.get("hermes", [])]
    hermes_model = "kimi-k2.6"
    hermes_provider = "ollama-cloud"
    cfg_yaml = hermes_dir / "config.yaml"
    if cfg_yaml.exists():
        try:
            import yaml
            cfg = yaml.safe_load(cfg_yaml.read_text())
            hermes_model = cfg.get("model", {}).get("default", hermes_model)
            hermes_provider = cfg.get("model", {}).get("provider", hermes_provider)
        except Exception:
            pass
    gw_port = 8642
    gw_url = f"http://{ip}:{gw_port}/"
    agents.append(
        AgentInfo(
            name="hermes", display_name="Hermes Agent", installed=hermes_installed,
            version="", running=bool(hermes_pids), pids=hermes_pids or [],
            config_dir=str(hermes_dir), port=gw_port, url=gw_url,
            model=hermes_model, provider=hermes_provider,
            log_file=str(HOME / ".hermes/logs"),
        )
    )

    # OpenCode Telegram Bot
    oc_tg_pids = [p["pid"] for p in procs.get("opencode-telegram", [])]
    agents.append(
        AgentInfo(
            name="opencode-telegram", display_name="OpenCode Telegram Bot",
            installed=(HOME / ".opencode-telegram-bot").exists() or bool(oc_tg_pids),
            running=bool(oc_tg_pids), pids=oc_tg_pids or [],
            config_dir=str(HOME / ".opencode-telegram-bot"),
        )
    )

    # Telegram ↔ Claude Bot
    tg_claude_dir = VAULT / "30-projects-active/2026-scripts/telegram-claude"
    tg_claude_pids = [p["pid"] for p in procs.get("telegram-claude-bot", [])]
    log_tail = []
    log_file = tg_claude_dir / "bot.log"
    if log_file.exists():
        log_tail = tail_file(str(log_file), 20)
    agents.append(
        AgentInfo(
            name="telegram-claude", display_name="Telegram ↔ Claude Bot",
            installed=tg_claude_dir.exists(), running=bool(tg_claude_pids),
            pids=tg_claude_pids or [], config_dir=str(tg_claude_dir), log_tail=log_tail,
            log_file=str(log_file),
        )
    )

    # Telegram CLI Bridge
    tg_bridge_pids = [p["pid"] for p in procs.get("telegram-cli-bridge", [])]
    agents.append(
        AgentInfo(
            name="telegram-cli-bridge", display_name="Telegram CLI Bridge",
            installed=(VAULT / "50-system/scripts/telegram-cli-bridge.py").exists() or bool(tg_bridge_pids),
            running=bool(tg_bridge_pids), pids=tg_bridge_pids or [],
            config_dir=str(VAULT / "50-system/scripts"),
        )
    )

    # Whisper Server
    ws_dir = VAULT / "30-projects-active/2026-scripts/whisper-server"
    ws_pids = [p["pid"] for p in procs.get("whisper-server", [])]
    ws_log = str(ws_dir / "whisper.log")
    agents.append(
        AgentInfo(
            name="whisper-server", display_name="Whisper Transcription Server",
            installed=ws_dir.exists(), running=bool(ws_pids), pids=ws_pids or [],
            config_dir=str(ws_dir), log_file=ws_log,
        )
    )

    # ChromaDB
    chroma_pids = [p["pid"] for p in procs.get("chroma", [])]
    chroma_port = 8000
    chroma_url = f"http://{ip}:{chroma_port}/"
    agents.append(
        AgentInfo(
            name="chroma", display_name="ChromaDB Vector Store",
            installed=(HOME / ".openclaw/chromadb-venv").exists() or bool(chroma_pids),
            running=bool(chroma_pids), pids=chroma_pids or [],
            config_dir=str(HOME / ".openclaw/chromadb-venv"),
            port=chroma_port, url=chroma_url,
        )
    )

    # Open WebUI
    ow_pids = [p["pid"] for p in procs.get("open-webui", [])]
    ow_port = 3008
    ow_url = f"http://{ip}:{ow_port}/"
    agents.append(
        AgentInfo(
            name="open-webui", display_name="Open WebUI",
            installed=bool(ow_pids), running=bool(ow_pids), pids=ow_pids or [],
            port=ow_port, url=ow_url,
        )
    )

    # SearXNG
    sx_pids = [p["pid"] for p in procs.get("searxng", [])]
    sx_port = 8088
    sx_url = f"http://{ip}:{sx_port}/"
    agents.append(
        AgentInfo(
            name="searxng", display_name="SearXNG Search",
            installed=bool(sx_pids), running=bool(sx_pids), pids=sx_pids or [],
            port=sx_port, url=sx_url,
        )
    )

    # Homepage Dashboard
    hp_pid_str = run("systemctl --user show homepage.service -p MainPID", timeout=3)
    hp_pid = None
    if hp_pid_str.startswith("MainPID="):
        v = hp_pid_str.split("=", 1)[1]
        if v and v != "0":
            hp_pid = int(v)
    hp_pids = [hp_pid] if hp_pid else []
    hp_port = 3000
    hp_url = f"http://{ip}:{hp_port}/"
    agents.append(
        AgentInfo(
            name="homepage", display_name="Homepage Dashboard",
            installed=(Path("/mnt/newhome/knssnr/CVault/30-projects-active/homepage")).exists(), running=bool(hp_pids),
            pids=hp_pids or [], port=hp_port, url=hp_url,
            config_dir=str(Path("/mnt/newhome/knssnr/CVault/30-projects-active/homepage")),
        )
    )

    # Caddy
    caddy_pids = [p["pid"] for p in procs.get("caddy", [])]
    agents.append(
        AgentInfo(
            name="caddy", display_name="Caddy Reverse Proxy",
            installed=bool(run("which caddy")), running=bool(caddy_pids),
            pids=caddy_pids or [], config_dir=str(HOME / ".config/caddy"),
        )
    )

    # Camofox Browser
    cf_pids = [p["pid"] for p in procs.get("camofox", [])]
    agents.append(
        AgentInfo(
            name="camofox", display_name="Camofox Browser (Playwright)",
            installed=(HOME / ".cache/camoufox").exists() or bool(cf_pids),
            running=bool(cf_pids), pids=cf_pids or [],
            config_dir=str(HOME / ".cache/camoufox"),
            port=9377, url=f"http://localhost:9377/",
        )
    )

    # Enrich with health checks and totals
    for a in agents:
        total_cpu = sum(p.get("cpu", 0) for p in procs.get(a.name, []))
        total_mem = sum(p.get("mem", 0) for p in procs.get(a.name, []))
        a.cpu_percent = round(total_cpu, 1)
        a.mem_percent = round(total_mem, 1)
        if a.url:
            a.health = check_health(a.url)

    return agents


def get_services() -> list[ServiceInfo]:
    services = []
    names = [
        "telegram-claude.service",
        "telegram-cli-bridge.service",
        "hermes-gateway.service",
        "homepage.service",
        "whisper-server.service",
        "caddy.service",
        "agent-monitor.service",
    ]
    for svc in names:
        out = run(f"systemctl --user show {svc} -p ActiveState -p SubState -p Description -p MainPID -p UnitFileState", timeout=5)
        state = "unknown"; sub = ""; desc = ""; pid = None; enabled = False
        for line in out.splitlines():
            if line.startswith("ActiveState="):
                state = line.split("=", 1)[1]
            elif line.startswith("SubState="):
                sub = line.split("=", 1)[1]
            elif line.startswith("Description="):
                desc = line.split("=", 1)[1]
            elif line.startswith("MainPID="):
                v = line.split("=", 1)[1]
                if v and v != "0": pid = int(v)
            elif line.startswith("UnitFileState="):
                enabled = line.split("=", 1)[1] == "enabled"
        services.append(ServiceInfo(name=svc, description=desc, state=state, sub_state=sub, enabled=enabled, pid=pid))

    system_svcs = ["docker.service", "containerd.service", "ssh.service"]
    for svc in system_svcs:
        out = run(f"systemctl show {svc} -p ActiveState -p SubState -p Description -p MainPID -p UnitFileState", timeout=5)
        state = "unknown"; sub = ""; desc = ""; pid = None; enabled = False
        for line in out.splitlines():
            if line.startswith("ActiveState="):
                state = line.split("=", 1)[1]
            elif line.startswith("SubState="):
                sub = line.split("=", 1)[1]
            elif line.startswith("Description="):
                desc = line.split("=", 1)[1]
            elif line.startswith("MainPID="):
                v = line.split("=", 1)[1]
                if v and v != "0": pid = int(v)
            elif line.startswith("UnitFileState="):
                enabled = line.split("=", 1)[1] == "enabled"
        services.append(ServiceInfo(name=svc, description=desc, state=state, sub_state=sub, enabled=enabled, pid=pid))
    return services


def get_cronjobs() -> list[CronJob]:
    jobs = []
    user_crontab = run("crontab -l 2>/dev/null", timeout=3)
    for line in user_crontab.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 5)
        if len(parts) >= 6:
            jobs.append(CronJob(source="user crontab", schedule=" ".join(parts[:5]), command=parts[5], user=str(HOME.name)))

    for f in sorted(Path("/etc/cron.d").iterdir()):
        if f.is_file():
            for line in f.read_text().splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split(None, 5)
                if len(parts) >= 6:
                    user = parts[5].split()[0] if len(parts[5].split()) > 0 else "root"
                    cmd = " ".join(parts[5].split()[1:]) if len(parts[5].split()) > 1 else parts[5]
                    jobs.append(CronJob(source=f"/etc/cron.d/{f.name}", schedule=" ".join(parts[:5]), command=cmd, user=user))

    hermes_cron = HOME / ".hermes/cron/jobs.json"
    if hermes_cron.exists():
        try:
            data = json.loads(hermes_cron.read_text())
            for job in data.get("jobs", []):
                sched = job.get("schedule_display", job.get("schedule", {}).get("display", "unknown"))
                state = job.get("state", "unknown")
                enabled = job.get("enabled", True)
                jobs.append(CronJob(
                    source="hermes cron", schedule=sched,
                    command=job.get("name", "") + ": " + job.get("prompt", "")[:100],
                    user="hermes", enabled=enabled and state != "completed"))
        except Exception:
            pass
    return jobs


def get_listeners() -> list[Listener]:
    listeners = []
    ss_out = run("ss -tlnp 2>/dev/null || netstat -tlnp 2>/dev/null", timeout=5)
    for line in ss_out.splitlines():
        if "LISTEN" not in line:
            continue
        parts = line.split()
        if len(parts) < 6:
            continue
        proto = "tcp"
        local = parts[3]  # Local Address:Port
        pid_proc = parts[-1]
        pid = None
        proc_name = ""
        m = re.search(r'users:\(\("([^"]+)",pid=(\d+)', pid_proc)
        if m:
            proc_name = m.group(1)
            pid = int(m.group(2))
        else:
            m = re.search(r"pid=(\d+)", pid_proc)
            if m:
                pid = int(m.group(1))
        m2 = re.match(r"(.+):(\d+)", local)
        if m2:
            addr = m2.group(1)
            port = int(m2.group(2))
            listeners.append(Listener(protocol=proto, local_address=addr, port=port, pid=pid, process=proc_name))
    return listeners


def get_docker() -> list[DockerContainer]:
    containers = []
    out = run("docker ps --format '{{.Names}}\t{{.Ports}}\t{{.Status}}\t{{.Image}}'", timeout=5)
    for line in out.splitlines():
        parts = line.split("\t")
        if len(parts) >= 4:
            containers.append(DockerContainer(name=parts[0], ports=parts[1], status=parts[2], image=parts[3], uptime=parts[2]))
    return containers


def get_agent_tasks(procs: dict) -> list[AgentTask]:
    tasks = []
    ps_out = run("ps aux | grep -E 'run-agent|batch_runner|intel-agent|shore-intel' | grep -v grep", timeout=3)
    for line in ps_out.splitlines():
        parts = line.split()
        if len(parts) < 11:
            continue
        try:
            pid = int(parts[1])
            cpu = float(parts[2])
            mem = float(parts[3])
            cmd = " ".join(parts[10:])[:120]
        except (ValueError, IndexError):
            continue
        agent = "unknown"
        if "shore-intel" in cmd or "intel-agent" in cmd:
            agent = "shore-intel"
        elif "run-agent" in cmd:
            agent = "hermes-agent"
        tasks.append(AgentTask(agent=agent, command=cmd, pid=pid, cpu=cpu, mem=mem, start_time=parts[8]))
    return tasks


def get_system_info() -> dict:
    return {
        "hostname": run("hostname"),
        "uptime": run("uptime -p"),
        "load": run("cat /proc/loadavg | awk '{print $1, $2, $3}'"),
        "memory": run("free -h | grep Mem"),
        "disk": run("df -h /home | tail -1"),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
    }


def collect() -> dict:
    procs = get_agent_processes()
    ip = get_ip()
    agents = get_installed_agents(procs, ip)
    services = get_services()
    cronjobs = get_cronjobs()
    listeners = get_listeners()
    docker = get_docker()
    tasks = get_agent_tasks(procs)
    system = get_system_info()
    history = save_history(load_history(), [asdict(a) for a in agents])

    return {
        "system": system,
        "agents": [asdict(a) for a in agents],
        "services": [asdict(s) for s in services],
        "cronjobs": [asdict(c) for c in cronjobs],
        "listeners": [asdict(l) for l in listeners],
        "docker": [asdict(d) for d in docker],
        "tasks": [asdict(t) for t in tasks],
        "history": history,
    }


if __name__ == "__main__":
    print(json.dumps(collect(), indent=2, default=str))
