#!/usr/bin/env bash
# AI-HUB laptop launcher (macOS / Linux): pull the latest build, then open the hub as an app window.
# CHANNEL=release ./ai-hub.sh follows tagged releases instead of main.
CHANNEL="${CHANNEL:-main}"
cd "$(dirname "$0")/.." || exit 1
if command -v git >/dev/null 2>&1; then
  if [ "$CHANNEL" = release ]; then
    git fetch --tags --quiet 2>/dev/null
    tag=$(git describe --tags --abbrev=0 origin/main 2>/dev/null) && git checkout --quiet "$tag" 2>/dev/null
  else
    git pull --ff-only --quiet 2>/dev/null || echo "AI-HUB: offline or local changes - running the copy you already have."
  fi
fi
URL="file://$PWD/index.html"
if [ "$(uname)" = Darwin ]; then
  for app in "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"; do
    [ -x "$app" ] && exec "$app" --app="$URL" --window-size=1280,860
  done
  exec open "$URL"
else
  for b in google-chrome google-chrome-stable chromium chromium-browser microsoft-edge brave-browser; do
    command -v "$b" >/dev/null 2>&1 && exec "$b" --app="$URL" --window-size=1280,860
  done
  exec xdg-open "$URL"
fi
