#!/bin/bash
# Build today's issue from content/$DATE.py and publish it.
set -euo pipefail
DATE="${1:-$(date -u +%F)}"
[ -f "content/$DATE.py" ] || { echo "FATAL: content/$DATE.py missing"; exit 1; }

cp "content/$DATE.py" content.py
python3 build_feed.py
mv "$DATE.html" docs/
mv latest.html docs/latest.html
mv digest.json docs/digest.json
python3 make_index.py

# hard verification — never publish or announce a broken page
python3 - "$DATE" <<'PY'
import sys, re, os
d = sys.argv[1]; p = "docs/%s.html" % d
src = open(p, encoding="utf-8").read()
def need(cond, msg):
    if not cond: print("VERIFY FAIL:", msg); sys.exit(1)
need(os.path.getsize(p) > 150_000, "page suspiciously small (%d bytes)" % os.path.getsize(p))
need(src.count("data:font/woff2") >= 7, "fonts not embedded")
need("logomark" in src and "data:image/png;base64," in src, "wordmark logo missing")
need("mix-blend-mode" in src, "blend mode missing")
need(re.search(r'class="lead-head">[A-Z0-9 ,.\'&;-]{10,}<', src), "lead headline missing or not uppercase")
need(src.count("DO THIS") >= 3, "closing boxes missing")
need("<em" not in src and "<i " not in src, "italics present")
for w in ["programmatic","flywheel","sponcon","mid-funnel","ideate"]:
    need(not re.search(r"\b%s\b" % w, re.sub(r"<[^>]+>"," ",src), re.I), "banned word: %s" % w)
need(os.path.getsize("docs/digest.json") > 200, "digest.json empty")
print("VERIFY OK — %d bytes" % os.path.getsize(p))
PY

git add -A
git -c user.name="THE FEED" -c user.email="feed@cruxmedia.local" \
    commit -m "issue: $DATE" --allow-empty-message || echo "nothing to commit"
git push origin HEAD
echo "PUBLISHED $DATE"
