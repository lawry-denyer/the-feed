# -*- coding: utf-8 -*-
"""THE FEED — render spec.  Content lives in content.py; this file never changes."""

import base64
import html
import json
import re
import sys
from datetime import date, timedelta

from content import ISSUE, LEAD, SECTIONS, FORECAST, TLDR

try:                      # SHARE arrived 1 Sept 2026; issues before that have none
    from content import SHARE
except ImportError:
    SHARE = []

CSS = """
:root{
  --paper:#F1F0EA; --white:#FFFFFF; --ink:#141419; --ink-mid:#4A4A55;
  /* sampled from the THE FEED wordmark */
  --orange:#F85808; --lilac:#F8C0F8;
  --lime:#E0F860;   --blue:#0088B8; --blue-deep:#00688F; --green:#209058;
}
*{box-sizing:border-box;}
html{ -webkit-text-size-adjust:100%; }
body{
  margin:0; background:var(--paper); color:var(--ink);
  font-family:'Space Grotesk',system-ui,sans-serif; font-size:17px; line-height:1.62;
  overflow-x:hidden;
}
.wrap{ max-width:860px; margin:0 auto; padding:0 22px 90px; position:relative; z-index:1; }
a{ color:var(--blue-deep); }
mark{ background:var(--lime); mix-blend-mode:multiply; padding:0 .12em; color:inherit; }

/* progress */
#prog{
  position:fixed; top:0; left:0; height:5px; width:0%; z-index:9999;
  background:linear-gradient(90deg,var(--lime),var(--orange),var(--blue));
}

/* masthead */
header.mast{ padding:56px 0 6px; }
.kicker{
  font-family:'Space Mono',monospace; font-size:12px; letter-spacing:.16em;
  text-transform:uppercase; color:var(--ink-mid); margin:0 0 14px;
}
.logo{ margin:0 0 18px; }
.logomark{
  display:block; width:100%; max-width:640px; height:auto;
}
.subline{
  font-family:'Space Grotesk',sans-serif; font-weight:500; font-size:19px;
  margin:0 0 18px; max-width:44ch;
}
.stampline{ display:flex; flex-wrap:wrap; gap:8px; align-items:center; margin-bottom:10px; }
.tag{
  font-family:'Space Mono',monospace; font-size:11px; letter-spacing:.12em; text-transform:uppercase;
  border:2px solid var(--ink); padding:4px 9px; background:var(--white);
}
#copybtn{ /* wordmark blue */
  font-family:'Space Mono',monospace; font-size:11px; letter-spacing:.12em; text-transform:uppercase;
  border:2px solid var(--ink); padding:5px 11px; background:var(--blue-deep); color:var(--white);
  cursor:pointer;
}
#copybtn:hover{ background:var(--ink); }
.rule{ height:3px; background:var(--ink); margin:22px 0 0; }

/* chip nav */
nav.chips{
  position:sticky; top:0; z-index:60; background:var(--paper);
  border-bottom:3px solid var(--ink); padding:12px 0 14px; margin-bottom:30px;
  display:flex; gap:9px; overflow-x:auto; scrollbar-width:none;
}
nav.chips::-webkit-scrollbar{ display:none; }
.chip{
  flex:0 0 auto; font-family:'Space Mono',monospace; font-size:11px; letter-spacing:.1em;
  text-transform:uppercase; background:var(--white); border:2px solid var(--ink);
  padding:6px 11px; cursor:pointer; box-shadow:3px 3px 0 var(--ink); color:var(--ink);
}
.chip:hover{ background:var(--lime); }
.chip[aria-pressed="true"]{ background:var(--lime); box-shadow:0 0 0 var(--ink); transform:translate(3px,3px); }

/* sections */
section{ margin:0 0 54px; }
.sec-head{ display:flex; align-items:flex-end; justify-content:space-between; gap:14px; }
.sec-name{
  font-family:'Syne',sans-serif; font-weight:800; text-transform:uppercase;
  font-size:clamp(28px,6vw,44px); line-height:1.07; padding-bottom:10px; margin:0; letter-spacing:-.01em;
}
.sec-name.blue{ color:var(--blue); }
.sec-name.pink{ color:var(--orange); }
.pg{ font-family:'Space Mono',monospace; font-size:12px; color:var(--ink-mid); white-space:nowrap; padding-bottom:8px; }
.sec-rule{ height:3px; background:var(--ink); margin:6px 0 7px; }
.sec-note{ font-family:'Space Mono',monospace; font-size:14px; font-weight:700; color:var(--ink);
  letter-spacing:.01em; margin:0 0 24px; }

/* clippings */
.clip{
  background:var(--white); border:3px solid var(--ink); box-shadow:6px 6px 0 var(--ink);
  padding:20px 22px; margin:0 0 26px; transition:box-shadow .12s ease;
}
.clip:nth-of-type(odd){ transform:rotate(-.35deg); }
.clip:nth-of-type(even){ transform:rotate(.35deg); }
.clip:hover{ box-shadow:9px 9px 0 var(--ink); }
.clip.w{ border-top:11px solid var(--blue); }
.clip.l{ border-top:11px solid var(--orange); }
.clip-head{
  display:flex; align-items:flex-start; justify-content:space-between; gap:16px; width:100%;
  background:none; border:0; padding:0; text-align:left; cursor:pointer; font:inherit; color:inherit;
}
.clip-title{
  font-family:'Syne',sans-serif; font-weight:800; font-size:clamp(20px,3.4vw,27px);
  line-height:1.3; padding-bottom:9px; margin:0; letter-spacing:-.01em;
}
.plus{
  flex:0 0 auto; width:30px; height:30px; border:3px solid var(--ink); background:var(--white);
  display:grid; place-items:center; font-family:'Space Mono',monospace; font-size:17px; font-weight:700;
  line-height:1; transition:transform .16s ease, background .16s ease;
}
.clip.open .plus{ transform:rotate(45deg); background:var(--lime); }
.hook{
  font-family:'Space Grotesk',sans-serif; font-weight:500; font-size:17.5px;
  color:var(--ink-mid); margin:11px 0 0;
}
.clip-body{ display:none; margin-top:16px; }
.clip.open .clip-body{ display:block; }
.clip-body p{ margin:0 0 15px; }

/* stamps */
.stamps{ display:flex; flex-wrap:wrap; gap:7px; margin:0 0 17px !important; }
.stamps a{
  font-family:'Space Mono',monospace; font-size:10.5px; letter-spacing:.11em; text-transform:uppercase;
  border:2px solid var(--ink); padding:3px 8px; text-decoration:none; color:var(--ink); background:var(--white);
}
.stamps a:hover{ background:var(--blue); color:var(--white); border-color:var(--blue); }

/* flagnote */
.flagnote{
  border-left:6px solid var(--orange); background:var(--lilac); padding:9px 13px;
  font-family:'Space Mono',monospace; font-size:12px; line-height:1.5; margin:0 0 16px !important;
}

/* so what */
.sw{ border:3px solid var(--ink); background:var(--paper); padding:15px 17px; margin-top:20px; }
.sw .lab{
  display:inline-block; font-family:'Space Mono',monospace; font-size:10.5px; letter-spacing:.14em;
  text-transform:uppercase; background:var(--orange); color:var(--ink); font-weight:700;
  padding:2px 8px; margin:0 0 10px !important;
}
.sw .txt{ margin:0 !important; }
.sw .act{ border-top:3px solid var(--ink); margin:14px 0 0 !important; padding-top:13px; font-weight:700; }
.dochip{
  display:inline-block; font-family:'Space Mono',monospace; font-size:10.5px; letter-spacing:.12em;
  text-transform:uppercase; background:var(--orange); color:var(--ink); padding:2px 7px; margin-right:9px;
  font-weight:700; vertical-align:2px;
}

/* featured video */
.watch{ border:3px solid var(--ink); background:var(--lilac); padding:14px 16px; margin:0 0 18px; }
.watch .wl{
  font-family:'Space Mono',monospace; font-size:10.5px; letter-spacing:.16em; text-transform:uppercase;
  color:var(--blue-deep); margin:0 0 8px !important; font-weight:700;
}
.watch .wt{
  font-family:'Syne',sans-serif; font-weight:800; font-size:19px; line-height:1.3; padding-bottom:6px;
  margin:0 0 4px !important; display:block; color:var(--ink); text-decoration:none;
}
.watch a.wt:hover{ color:var(--blue); text-decoration:underline; }
.watch .wm{
  font-family:'Space Mono',monospace; font-size:11.5px; letter-spacing:.04em; color:var(--ink-mid);
  margin:0 0 9px !important;
}
.watch .wn{ margin:0 !important; font-size:15.5px; }

/* number blocks */
.nums{ display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin:22px 0; }
.num{ border:3px solid var(--ink); background:var(--white); padding:14px; }
.num b{
  display:block; font-family:'Syne',sans-serif; font-weight:800; font-size:clamp(28px,5.4vw,44px);
  line-height:1.14; padding-bottom:7px; letter-spacing:-.02em;
}
.num u{ font-family:'Space Mono',monospace; font-size:11px; letter-spacing:.08em; text-transform:uppercase;
  color:var(--ink-mid); text-decoration:none; line-height:1.4; display:block; }
.num.n1 b{ color:var(--ink); } .num.n2 b{ color:var(--orange); } .num.n3 b{ color:var(--blue-deep); }

/* lead */
.lead-head{
  font-family:'Syne',sans-serif; font-weight:800; text-transform:uppercase;
  font-size:clamp(34px,7.4vw,62px); line-height:1.08; padding-bottom:12px; margin:0 0 16px; letter-spacing:-.02em;
}
.deck{ font-size:20px; font-weight:500; margin:0 0 20px; }

/* forecast */
.forecast{
  background:var(--blue-deep); color:var(--white); border:3px solid var(--ink); box-shadow:6px 6px 0 var(--ink);
  list-style:none; counter-reset:f; margin:0; padding:8px 24px;
}
.forecast li{ counter-increment:f; padding:22px 0; border-top:2px solid rgba(255,255,255,.35); }
.forecast li:first-child{ border-top:0; }
.conf{
  display:inline-block; font-family:'Space Mono',monospace; font-size:10.5px; letter-spacing:.14em;
  text-transform:uppercase; background:var(--lime); color:var(--ink); padding:3px 8px; font-weight:700;
  margin-bottom:11px;
}
.conf .win{ color:var(--ink); opacity:.7; }
.forecast h4{
  font-family:'Syne',sans-serif; font-weight:800; font-size:clamp(21px,3.6vw,29px); line-height:1.3;
  padding-bottom:8px; margin:0 0 10px; color:var(--white);
}
.forecast p{ margin:0 0 12px; }
.forecast .fdo{ font-weight:700; margin:0; }

/* tldr */
.tldr{
  background:var(--lime); border:3px solid var(--ink); box-shadow:6px 6px 0 var(--ink);
  list-style:none; counter-reset:t; margin:0; padding:6px 24px;
}
.tldr li{
  counter-increment:t; display:flex; gap:18px; align-items:flex-start;
  padding:20px 0; border-top:2px solid var(--ink);
}
.tldr li:first-child{ border-top:0; }
.tldr li::before{
  content:counter(t); flex:0 0 auto; font-family:'Syne',sans-serif; font-weight:800;
  font-size:40px; line-height:1.0; color:var(--ink);
}
.tldr p{ margin:0; }

/* share */
.share{
  background:var(--lilac); border:3px solid var(--ink); box-shadow:6px 6px 0 var(--ink);
  list-style:none; margin:0; padding:8px 24px;
}
.share li{ padding:22px 0; border-top:2px solid var(--ink); }
.share li:first-child{ border-top:0; }
.who{
  display:inline-block; font-family:'Space Mono',monospace; font-size:10.5px; letter-spacing:.14em;
  text-transform:uppercase; background:var(--ink); color:var(--lime); padding:3px 8px; font-weight:700;
  margin-bottom:11px;
}
.share h4{
  font-family:'Syne',sans-serif; font-weight:800; font-size:clamp(20px,3.4vw,27px); line-height:1.3;
  margin:0 0 13px; color:var(--ink);
}
.post{
  background:var(--white); border:3px solid var(--ink); padding:18px 20px; margin:0 0 13px;
  white-space:pre-wrap; font-size:.97em;
}
.share .swhy{ margin:0; font-weight:700; }

.foot{
  margin-top:52px; border-top:3px solid var(--ink); padding-top:16px;
  font-family:'Space Mono',monospace; font-size:12px; letter-spacing:.1em;
  text-transform:uppercase; color:var(--ink-mid);
}

/* a11y + responsive */
:focus-visible{ outline:3px solid var(--blue); outline-offset:3px; }
@media (max-width:640px){
  body{ font-size:16px; }
  .wrap{ padding:0 15px 70px; }
  .nums{ grid-template-columns:1fr; }
  .clip, .clip:nth-of-type(odd), .clip:nth-of-type(even){ transform:none; }
  .logomark{ max-width:100%; }
  .clip{ padding:17px 16px; box-shadow:5px 5px 0 var(--ink); }
  .forecast, .tldr{ padding-left:17px; padding-right:17px; }
  .tldr li{ gap:13px; }
  .tldr li::before{ font-size:31px; }
}
@media (prefers-reduced-motion:reduce){
  *{ transition:none !important; animation:none !important; scroll-behavior:auto !important; }
}
"""

JS = """
(function(){
  var prog=document.getElementById('prog');
  function onScroll(){
    var h=document.documentElement.scrollHeight-window.innerHeight;
    prog.style.width=(h>0?(window.scrollY/h)*100:0)+'%';
  }
  window.addEventListener('scroll',onScroll,{passive:true});
  window.addEventListener('resize',onScroll); onScroll();

  document.querySelectorAll('.clip-head').forEach(function(btn){
    btn.addEventListener('click',function(){
      var clip=btn.closest('.clip');
      var open=clip.classList.toggle('open');
      btn.setAttribute('aria-expanded',open?'true':'false');
    });
  });

  var chips=document.querySelectorAll('.chip');
  chips.forEach(function(chip){
    chip.addEventListener('click',function(){
      var target=chip.dataset.target;
      chips.forEach(function(c){ c.setAttribute('aria-pressed', c===chip?'true':'false'); });
      document.querySelectorAll('section[data-sec]').forEach(function(sec){
        sec.style.display=(target==='all'||sec.dataset.sec===target)?'':'none';
      });
      window.scrollTo(0,0);
    });
  });

  var btn=document.getElementById('copybtn');
  var digest=DIGEST_JSON;
  var label=btn.textContent;
  btn.addEventListener('click',function(){
    navigator.clipboard.writeText(digest).then(function(){
      btn.textContent='\\u2713 copied \\u00b7 '+digest.length+' chars';
      setTimeout(function(){ btn.textContent=label; },2200);
    }).catch(function(){
      btn.textContent='copy failed';
      setTimeout(function(){ btn.textContent=label; },2200);
    });
  });
})();
"""


def esc(s):
    return html.escape(s, quote=False)


def stamps_html(stamps):
    links = "".join(
        '<a href="%s" target="_blank" rel="noopener">%s</a>' % (html.escape(u, quote=True), esc(t))
        for t, u in stamps
    )
    return '<p class="stamps">%s</p>' % links


def nums_html(nums):
    cells = "".join(
        '<div class="num n%d"><b>%s</b><u>%s</u></div>' % (i + 1, esc(n), esc(l))
        for i, (n, l) in enumerate(nums)
    )
    return '<div class="nums">%s</div>' % cells


def watch_html(w):
    if not w:
        return ""
    return (
        '<div class="watch"><p class="wl">%s</p>'
        '<a class="wt" href="%s" target="_blank" rel="noopener">%s</a>'
        '<p class="wm">%s</p><p class="wn">%s</p></div>'
    ) % (esc(w["label"]), html.escape(w["url"], quote=True), esc(w["title"]),
         esc(w["meta"]), esc(w["note"]))


def sw_html(so_what, do_this):
    return (
        '<div class="sw"><p class="lab">So what</p><p class="txt">%s</p>'
        '<p class="act"><span class="dochip">DO THIS</span>%s</p></div>'
    ) % (so_what, esc(do_this))


def flag_html(text):
    return '<p class="flagnote">%s</p>' % esc(text) if text else ""


def item_html(it, extra_class=""):
    open_cls = " open" if it.get("open") else ""
    body = watch_html(it.get("watch"))
    body += "".join("<p>%s</p>" % p for p in it["body"])
    body += nums_html(it["numbers"]) if it.get("numbers") else ""

    body += flag_html(it.get("flagnote"))
    body += sw_html(it["so_what"], it["do_this"])
    return (
        '<article class="clip %s%s">'
        '<button class="clip-head" aria-expanded="%s"><h3 class="clip-title">%s</h3>'
        '<span class="plus" aria-hidden="true">+</span></button>'
        '<p class="hook">%s</p>'
        '<div class="clip-body">%s%s</div></article>'
    ) % (
        extra_class,
        open_cls,
        "true" if it.get("open") else "false",
        esc(it["title"]),
        esc(it["hook"]),
        stamps_html(it["stamps"]),
        body,
    )


SITE = "https://lawry-denyer.github.io/the-feed"


def build_digest():
    """Discord message.  Webhook messages render [text](url) masked links."""
    d = "**[Read Full Edition Here](%s/%s.html)**\n\n" % (SITE, ISSUE["date_iso"])
    d += "**THE FEED** \u00b7 %s" % ISSUE["kicker"].split("// ")[-1]
    if ISSUE["pace"].upper() == "LIGHT":
        d += "  \u00b7 *light issue \u2014 quiet news day*"
    d += "\n\n**%s**\n%s\n\n" % (LEAD["headline"], LEAD["deck"])
    d += "\n".join("**%d.** %s" % (i + 1, t) for i, t in enumerate(TLDR))
    return None, d


def build():
    # ---- lead ----
    lead_body = "".join("<p>%s</p>" % p for p in LEAD["body"])
    lead = (
        '<section data-sec="lead"><div class="sec-head"><h2 class="sec-name">THE LEAD</h2>'
        '<span class="pg">pg. 01</span></div><div class="sec-rule"></div>'
        '<p class="sec-note">the story that changes how you read the rest</p>'
        '<article class="clip open">'
        '<button class="clip-head" aria-expanded="true"><h3 class="lead-head">%s</h3>'
        '<span class="plus" aria-hidden="true">+</span></button>'
        '<p class="deck">%s</p><div class="clip-body">%s%s%s%s%s</div></article></section>'
    ) % (
        esc(LEAD["headline"]),
        esc(LEAD["deck"]),
        stamps_html(LEAD["stamps"]),
        lead_body,
        nums_html(LEAD["numbers"]),
        flag_html(LEAD.get("flagnote")),
        sw_html(LEAD["so_what"], LEAD["do_this"]),
    )

    # ---- body sections ----
    secs = [lead]
    for s in SECTIONS:
        tint = (" " + s["tint"]) if s.get("tint") else ""
        extra = {"ws": "w", "ls": "l"}.get(s["id"], "")
        items = "".join(item_html(it, extra) for it in s["items"])
        secs.append(
            '<section data-sec="%s"><div class="sec-head"><h2 class="sec-name%s">%s</h2>'
            '<span class="pg">%s</span></div><div class="sec-rule"></div>'
            '<p class="sec-note">%s</p>%s</section>'
            % (s["id"], tint, esc(s["name"]), s["page"], esc(s["note"]), items)
        )

    # ---- forecast ----
    fitems = "".join(
        '<li><span class="conf">%s <span class="win">&middot; %s</span></span>'
        '<h4>%s</h4><p>%s</p><p class="fdo">%s</p></li>'
        % (esc(f["confidence"]), esc(f["window"]), esc(f["headline"]), f["body"], esc(f["do"]))
        for f in FORECAST
    )
    secs.append(
        '<section data-sec="forecast"><div class="sec-head"><h2 class="sec-name">FORECAST</h2>'
        '<span class="pg">pg. 09</span></div><div class="sec-rule"></div>'
        '<p class="sec-note">where this is heading, and what to get ahead of</p>'
        '<ol class="forecast">%s</ol></section>' % fitems
    )

    # ---- tldr ----
    titems = "".join("<li><p>%s</p></li>" % esc(t) for t in TLDR)
    secs.append(
        '<section data-sec="tldr"><div class="sec-head"><h2 class="sec-name">TL;DR</h2>'
        '<span class="pg">pg. 10</span></div><div class="sec-rule"></div>'
        '<p class="sec-note">the whole issue in seven lines</p>'
        '<ol class="tldr">%s</ol></section>' % titems
    )

    # ---- share ----
    if SHARE:
        shitems = "".join(
            '<li><span class="who">%s</span><h4>%s</h4>'
            '<div class="post">%s</div><p class="swhy">%s</p></li>'
            % (esc(sh["who"]), esc(sh["angle"]), esc(sh["post"]), esc(sh["why"]))
            for sh in SHARE
        )
        secs.append(
            '<section data-sec="share"><div class="sec-head"><h2 class="sec-name">SHARE</h2>'
            '<span class="pg">pg. 11</span></div><div class="sec-rule"></div>'
            '<p class="sec-note">one post each, ready to paste, from three different stories</p>'
            '<ol class="share">%s</ol></section>' % shitems
        )

    # ---- chips ----
    chip_defs = [("all", "EVERYTHING"), ("lead", "THE LEAD")]
    chip_defs += [(s["id"], s["name"]) for s in SECTIONS]
    chip_defs += [("forecast", "FORECAST"), ("tldr", "TL;DR")]
    if SHARE:
        chip_defs += [("share", "SHARE")]
    chips = "".join(
        '<button class="chip" data-target="%s" aria-pressed="%s">%s</button>'
        % (cid, "true" if cid == "all" else "false", esc(nm))
        for cid, nm in chip_defs
    )

    # ---- counts ----
    all_urls = {u for _, u in LEAD["stamps"]}
    for s in SECTIONS:
        for it in s["items"]:
            all_urls.update(u for _, u in it["stamps"])
    plain = re.sub(r"<[^>]+>", "", "".join(secs))
    words = len(plain.split())
    read = max(1, round(words / 220))

    # ---- digest ----
    digest = "THE FEED — %s\n\n%s\n%s\n%s\n\n" % (
        ISSUE["kicker"].split("// ")[-1],
        LEAD["headline"],
        LEAD["deck"],
        LEAD["stamps"][0][1],
    )
    digest += "\n".join("%d. %s" % (i + 1, t) for i, t in enumerate(TLDR))

    og_desc = "%s — %s — %s" % (
        LEAD["headline"],
        SECTIONS[0]["items"][0]["title"],
        SECTIONS[5]["items"][0]["title"],
    )

    js = JS.replace("DIGEST_JSON", json.dumps(digest))

    doc = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>THE FEED &mdash; %(kicker)s</title>
<meta name="theme-color" content="#FF3D8B">
<meta property="og:title" content="THE FEED &mdash; %(datestr)s">
<meta property="og:description" content="%(ogdesc)s">
<meta property="og:type" content="article">
<style>%(fonts)s</style>
<style>%(css)s</style>
</head><body>
<div id="prog"></div>
<div class="wrap">
<header class="mast">
  <p class="kicker">%(kicker)s</p>
  <div class="logo">
    <img class="logomark" src="data:image/png;base64,%(logo)s" alt="THE FEED" width="1600" height="687">
  </div>
  <p class="subline">%(tagline)s</p>
  <div class="stampline">
    <span class="tag">Pace: %(pace)s</span>
    <span class="tag">%(sources)d sources</span>
    <span class="tag">%(read)d min read</span>
    <button id="copybtn">&#8681; Copy digest</button>
  </div>
  <div class="rule"></div>
</header>
<nav class="chips" aria-label="Sections">%(chips)s</nav>
%(sections)s
<p class="foot">%(nextdrop)s</p>
</div>
<script>%(js)s</script>
</body></html>
""" % {
        "logo": base64.b64encode(open("logo.png", "rb").read()).decode("ascii"),
        "kicker": esc(ISSUE["kicker"]),
        "datestr": esc(ISSUE["kicker"].split("// ")[-1]),
        "ogdesc": html.escape(og_desc, quote=True),
        "fonts": open("fonts.css", encoding="utf-8").read(),
        "css": CSS,
        "tagline": esc(ISSUE["tagline"]),
        "pace": esc(ISSUE["pace"]),
        "sources": len(all_urls),
        "read": read,
        "chips": chips,
        "sections": "".join(secs),
        "nextdrop": esc(ISSUE["next_drop"]),
        "js": js,
    }
    return doc, len(all_urls), read, words, len(digest)


if __name__ == "__main__":
    doc, nsrc, read, words, dlen = build()
    out = "%s.html" % ISSUE["date_iso"]
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    with open("latest.html", "w", encoding="utf-8") as f:
        f.write(doc)
    _, digest = build_digest()
    with open("digest.json", "w", encoding="utf-8") as f:
        json.dump({"date": ISSUE["date_iso"], "pace": ISSUE["pace"],
                   "headline": LEAD["headline"], "deck": LEAD["deck"],
                   "lead_url": LEAD["stamps"][0][1], "tldr": TLDR,
                   "sources": nsrc, "read_minutes": read, "digest": digest}, f, indent=2)
    print("wrote %s  (%d bytes)" % (out, len(doc)))
    print("sources: %d | read: %d min | words: %d | digest: %d chars" % (nsrc, read, words, dlen))
