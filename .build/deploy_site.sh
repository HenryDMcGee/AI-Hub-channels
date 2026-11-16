#!/usr/bin/env bash
# Stage the hosted (demo) hub into the Resume-Website repo, whose Cloudflare Worker
# ("resume-website", Workers Static Assets from ./public) serves mcgeehenry.com.
# Pushing that repo's main branch is what deploys.
#
#   .build/deploy_site.sh /path/to/resume-website          stage only (review with git diff)
#   .build/deploy_site.sh /path/to/resume-website --push   stage, commit and push
set -euo pipefail
HUB="$(cd "$(dirname "$0")/.." && pwd)"
SITE="${1:?path to a resume-website clone}"
[ -f "$SITE/wrangler.jsonc" ] || { echo "no wrangler.jsonc in $SITE"; exit 1; }
python3 -I "$HUB/.build/build.py" >/dev/null
# replace only what the hub owns; site-only pages (public/feedback/) stay
mkdir -p "$SITE/public"
rm -rf "$SITE/public/index.html" "$SITE/public/demo" "$SITE/public/version.txt"
cp "$HUB/index.html" "$SITE/public/"
cp -r "$HUB/demo" "$SITE/public/"
( cd "$HUB" && git rev-parse --short HEAD ) > "$SITE/public/version.txt"
# Microsoft Clarity (heatmaps + recordings) on the hosted copy only. The project id lives in .build/clarity_id or
# $CLARITY_ID; with neither, nothing is added. The tag stays off for Global Privacy Control and for Henry's own
# browsers (?notrack=1 or a visit to /insights/ sets mh-notrack), and loads only while recording is switched on
# (/api/t/on, the switch on /insights/). The demo pages get it too, since they open in frames.
CLARITY_ID="${CLARITY_ID:-$(cat "$HUB/.build/clarity_id" 2>/dev/null || true)}"
CLARITY_ID="$(printf '%s' "$CLARITY_ID" | tr -cd 'a-z0-9')"
if [ -n "$CLARITY_ID" ]; then
  python3 -I - "$SITE/public" "$CLARITY_ID" <<'PY'
import sys, pathlib
root, cid = pathlib.Path(sys.argv[1]), sys.argv[2]
tag = ('<script>(function(){try{if(navigator.globalPrivacyControl||/[?&](notrack=1|view=)/.test(location.search)||localStorage.getItem("mh-notrack")==="1")return}catch(e){}'
       'window.clarity=window.clarity||function(){(window.clarity.q=window.clarity.q||[]).push(arguments)};'
       'fetch("/api/t/on",{cache:"no-store"}).then(function(r){return r.json()}).then(function(j){if(!j||j.on===false)return;'
       'var t=document.createElement("script");t.async=1;t.src="https://www.clarity.ms/tag/' + cid + '";document.head.appendChild(t)}).catch(function(){})})();</script>')
pages = [root / 'index.html'] + sorted((root / 'demo').rglob('*.html'))
for p in pages:
    s = p.read_text()
    if 'clarity.ms/tag' in s or '<head>' not in s: continue
    p.write_text(s.replace('<head>', '<head>\n' + tag, 1))
print('clarity tag added to', len(pages), 'pages')
PY
else
  echo "no Clarity id (.build/clarity_id): skipping the Clarity tag"
fi
# Grafana Cloud Frontend Observability (Faro): page speed, JavaScript errors, and the hub's decisions as custom events
# for the Grafana dashboard "mcgeehenry.com: visits vs. the happy path". Home page only (not the demo frames or the
# private pages). The SDK is served from this site (demo/vendor/faro, Apache-2.0), and the tag follows the same rules
# as Clarity's: off for Global Privacy Control, Henry's own browsers and previews, and while recording is switched off.
FARO_URL="${FARO_URL:-$(cat "$HUB/.build/faro_url" 2>/dev/null || true)}"
FARO_URL="$(printf '%s' "$FARO_URL" | tr -cd 'a-zA-Z0-9:/._-')"
if [ -n "$FARO_URL" ]; then
  python3 -I - "$SITE/public/index.html" "$FARO_URL" "$(cd "$HUB" && git rev-parse --short HEAD)" <<'PY'
import sys, pathlib
p, url, ver = pathlib.Path(sys.argv[1]), sys.argv[2], sys.argv[3]
tag = ('<script>(function(){try{if(navigator.globalPrivacyControl||/[?&](notrack=1|view=)/.test(location.search)||localStorage.getItem("mh-notrack")==="1")return}catch(e){}'
       'fetch("/api/t/on",{cache:"no-store"}).then(function(r){return r.json()}).then(function(j){if(!j||j.on===false)return;'
       'var s=document.createElement("script");s.src="/demo/vendor/faro/faro-web-sdk.iife.js";'
       's.onload=function(){var F=window.GrafanaFaroWebSdk;if(!F)return;try{F.initializeFaro({url:"' + url + '",'
       'app:{name:"mcgeehenry-com",version:"' + ver + '",environment:"production"},'
       'instrumentations:F.getWebInstrumentations({captureConsole:false})});window.dispatchEvent(new Event("faro-ready"))}catch(e){}};'
       'document.head.appendChild(s)}).catch(function(){})})();</script>')
s = p.read_text()
if 'faro-web-sdk.iife.js' not in s:
    p.write_text(s.replace('<head>', '<head>\n' + tag, 1))
print('faro tag added')
PY
else
  echo "no Faro collector URL (.build/faro_url): skipping the Grafana tag"
fi
echo "staged $(du -sh "$SITE/public" | cut -f1) into $SITE/public"
if [ "${2:-}" = "--push" ]; then
  cd "$SITE"
  git add -A public
  git commit -m "Deploy AI-HUB $(cat public/version.txt) from AI-Hub-channels" || { echo "nothing to deploy"; exit 0; }
  git push origin HEAD:main
fi
