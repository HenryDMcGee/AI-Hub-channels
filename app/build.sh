#!/usr/bin/env bash
# Builds app/AI-HUB.exe (Windows x64, GUI subsystem) from any OS with Go 1.22+.
# Icon + manifest are in rsrc_windows_amd64.syso; regenerate with:
#   go install github.com/akavel/rsrc@latest && rsrc -manifest app.manifest -ico ../launch/ai-hub.ico -arch amd64 -o rsrc_windows_amd64.syso
set -e
cd "$(dirname "$0")"
GOOS=windows GOARCH=amd64 CGO_ENABLED=0 go build -trimpath -ldflags "-H windowsgui -s -w" -o AI-HUB.exe .
echo "built $(pwd)/AI-HUB.exe"
