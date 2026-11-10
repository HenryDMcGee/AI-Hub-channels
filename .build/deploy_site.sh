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
echo "staged $(du -sh "$SITE/public" | cut -f1) into $SITE/public"
if [ "${2:-}" = "--push" ]; then
  cd "$SITE"
  git add -A public
  git commit -m "Deploy AI-HUB $(cat public/version.txt) from AI-Hub-channels" || { echo "nothing to deploy"; exit 0; }
  git push origin HEAD:main
fi
