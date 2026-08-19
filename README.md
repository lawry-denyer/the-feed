# THE FEED

A daily brief on what brands did on YouTube, and whether it worked.
Built each weekday morning by a scheduled Claude task.

**Read it:** https://lawry-denyer.github.io/the-feed/

## How it works

The design and the content are deliberately separate, so the look cannot drift.

| file | role |
|---|---|
| `build_feed.py` | The entire render spec. Rarely changes. Change the design **here**, once. |
| `fonts.css` | Syne, Space Grotesk and Space Mono as base64 woff2, so pages work offline. |
| `content/YYYY-MM-DD.py` | One file per issue. Pure data — headlines, prose, sources, numbers. |
| `make_index.py` | Regenerates the archive at `docs/index.html`. |
| `publish.sh` | Build, verify, commit, push. Refuses to publish a broken page. |
| `docs/` | GitHub Pages root. `latest.html` always points at the newest issue. |

## Daily run

```bash
git clone https://github.com/lawry-denyer/the-feed.git && cd the-feed
# write content/$(date -u +%F).py
./publish.sh
# then POST docs/digest.json's "digest" field to the Discord webhook
```

`publish.sh` verifies the built page before committing: font embedding, masthead
misregistration, uppercase lead headline, closing boxes, no italics, no banned
vocabulary. A failed check exits non-zero and nothing is announced.

## Changing the design

Edit `build_feed.py`, then rebuild any issue to see the change:

```bash
cp content/2026-08-17.py content.py && python3 build_feed.py
```

Every past issue re-renders identically from its data file.
