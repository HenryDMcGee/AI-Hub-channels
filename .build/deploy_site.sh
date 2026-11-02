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
rm -rf "$SITE/public"
mkdir -p "$SITE/public"
cp "$HUB/index.html" "$SITE/public/"
cp -r "$HUB/demo" "$SITE/public/"
( cd "$HUB" && git rev-parse --short HEAD ) > "$SITE/public/version.txt"
echo "staged $(du -sh "$SITE/public" | cut -f1) into $SITE/public"
if [ "${2:-}" = "--push" ]; then
  cd "$SITE"
  git add -A public
  git commit -m "Deploy AI-HUB $(cat public/version.txt) from AI-Hub-channels" || { echo "nothing to deploy"; exit 0; }
  git push origin HEAD:main
fi
