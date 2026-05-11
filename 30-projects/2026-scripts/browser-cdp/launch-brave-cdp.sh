#!/usr/bin/env bash
# Launch Brave with Chrome DevTools Protocol (CDP) enabled.
# This lets AI agents connect to YOUR real browser — with all logins, cookies, extensions.
#
# Usage:
#   ./launch-brave-cdp.sh          # uses your real Brave profile
#   ./launch-brave-cdp.sh --clean  # uses an isolated fresh profile (safer for automation)

set -e

PORT="${CDP_PORT:-9222}"
PROFILE_DIR="$HOME/.config/BraveSoftware/Brave-Browser"
CLEAN_PROFILE="/tmp/brave-cdp-profile"

# Check if CDP is already available
if curl -sf "http://localhost:${PORT}/json/version" > /dev/null 2>&1; then
  echo "✅ CDP already available at http://localhost:${PORT}"
  echo "   Browser: $(curl -s http://localhost:${PORT}/json/version | python3 -c "import sys,json;d=json.load(sys.stdin);print(d.get('Browser','?'))")"
  exit 0
fi

# Kill any existing Brave (can't add CDP to a running instance)
if pgrep -x "brave" > /dev/null || pgrep -f "brave-browser" > /dev/null; then
  echo "⚠️  Brave is already running WITHOUT CDP."
  echo "   Close Brave first, then run this script."
  echo ""
  echo "   Or run:  pkill -f brave-browser && sleep 1 && $0"
  exit 1
fi

# Export XAUTHORITY if running under Wayland + Xwayland (GNOME, etc.)
# Brave needs X11 auth to connect to the display.
if [ -z "${XAUTHORITY:-}" ] && [ -n "${WAYLAND_DISPLAY:-}" ]; then
  AUTH_FILE=$(find /run/user/$(id - u) -maxdepth 1 -name '.mutter-Xwaylandauth.*' -print -quit 2>/dev/null)
  if [ -n "$AUTH_FILE" ]; then
    export XAUTHORITY="$AUTH_FILE"
  fi
fi

if [[ "$1" == "--clean" ]]; then
  echo "🧹 Launching Brave with clean profile (no logins)…"
  PROFILE="$CLEAN_PROFILE"
else
  echo "🔐 Launching Brave with your real profile (all logins preserved)…"
  PROFILE="$PROFILE_DIR"
fi

brave-browser \
  --remote-debugging-port="${PORT}" \
  --remote-debugging-address=127.0.0.1 \
  --user-data-dir="${PROFILE}" \
  --no-first-run \
  --no-default-browser-check \
  --disable-background-networking \
  --disable-sync \
  --password-store=basic \
  "$@" &

# Wait for CDP to come up
echo -n "⏳ Waiting for CDP on port ${PORT}…"
for i in $(seq 1 20); do
  sleep 0.5
  if curl -sf "http://localhost:${PORT}/json/version" > /dev/null 2>&1; then
    echo " ready!"
    BROWSER=$(curl -s "http://localhost:${PORT}/json/version" | python3 -c "import sys,json;d=json.load(sys.stdin);print(d.get('Browser','?'))")
    echo "✅ CDP active: http://localhost:${PORT}"
    echo "   Browser: ${BROWSER}"
    echo ""
    echo "Connect with:"
    echo "  Python (browser-use): BrowserConfig(cdp_url='http://localhost:${PORT}')"
    echo "  Playwright:           chromium.connect_over_cdp('http://localhost:${PORT}')"
    echo "  Puppeteer:            puppeteer.connect({ browserURL: 'http://localhost:${PORT}' })"
    exit 0
  fi
done

echo " timeout. Check if Brave launched correctly."
exit 1
