# -*- coding: utf-8 -*-
"""Regenerate docs/index.html — the archive list."""
import os, re, html, datetime

DOCS = "docs"
rows = []
for fn in sorted(os.listdir(DOCS), reverse=True):
    m = re.fullmatch(r"(\d{4}-\d{2}-\d{2})\.html", fn)
    if not m:
        continue
    d = datetime.date.fromisoformat(m.group(1))
    t = ""
    try:
        src = open(os.path.join(DOCS, fn), encoding="utf-8").read()
        h = re.search(r'class="lead-head">([^<]+)', src)
        if h:
            t = html.escape(h.group(1).strip(), quote=False)
    except Exception:
        pass
    rows.append((d, fn, t))

items = "".join(
    '<li><a href="%s"><span class="d">%s</span><span class="t">%s</span></a></li>'
    % (fn, d.strftime("%a %-d %b %Y"), t or "&mdash;")
    for d, fn, t in rows
)

open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8").write("""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>THE FEED &mdash; archive</title><meta name="theme-color" content="#FF3D8B">
<style>
:root{--paper:#F1F0EA;--white:#fff;--ink:#141419;--ink-mid:#4A4A55;--pink:#FF3D8B;--blue:#0B57C4;--yellow:#FFD400}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);
font-family:ui-monospace,'Space Mono',Menlo,monospace;font-size:15px;line-height:1.6}
body::before{content:'';position:fixed;inset:0;z-index:0;pointer-events:none;opacity:.5;
background-image:radial-gradient(var(--ink) .5px,transparent .5px);background-size:4px 4px}
.wrap{max-width:860px;margin:0 auto;padding:56px 22px 80px;position:relative;z-index:1}
h1{font-family:Impact,'Syne',sans-serif;font-size:clamp(46px,12vw,104px);text-transform:uppercase;
line-height:1.04;padding-bottom:12px;margin:0 0 10px;letter-spacing:-.02em}
.sub{color:var(--ink-mid);margin:0 0 8px}
.rule{height:3px;background:var(--ink);margin:22px 0 26px}
ul{list-style:none;margin:0;padding:0}
li{border:3px solid var(--ink);background:var(--white);box-shadow:6px 6px 0 var(--ink);margin:0 0 16px}
li a{display:flex;gap:18px;align-items:baseline;padding:15px 17px;text-decoration:none;color:var(--ink)}
li a:hover{background:var(--yellow)}
.d{flex:0 0 auto;color:var(--blue);font-weight:700;letter-spacing:.04em}
.t{font-family:system-ui,sans-serif;font-weight:600}
.latest{display:inline-block;border:2px solid var(--ink);background:var(--pink);color:#fff;
padding:5px 11px;text-decoration:none;letter-spacing:.1em;text-transform:uppercase;font-size:12px}
:focus-visible{outline:3px solid var(--blue);outline-offset:3px}
@media(max-width:640px){li a{flex-direction:column;gap:4px}}
</style></head><body><div class="wrap">
<h1>The Feed</h1>
<p class="sub">What brands did on YouTube yesterday, and whether it worked.</p>
<p><a class="latest" href="latest.html">&rarr; Read the latest issue</a></p>
<div class="rule"></div>
<ul>%s</ul>
</div></body></html>""" % items)
print("index: %d issues" % len(rows))
