# -*- coding: utf-8 -*-
"""Content for THE FEED — issue data only.  The render spec lives in build_feed.py."""

ISSUE = {
    "date_iso": "2026-08-19",
    "kicker": "Crux Media // Wednesday 19 August 2026",
    "tagline": "What brands did on YouTube yesterday, and whether it worked.",
    "pace": "STEADY",
    "next_drop": "Next drop: Thursday, 06:30 MT",
}

LEAD = {
    "headline": "SHORTS IS THE CHEAPEST VIDEO INVENTORY IN SOCIAL AND ALMOST NOBODY IS BUYING IT",
    "deck": "Agency buyers say Shorts costs $4 to $6 to reach a thousand people.  Reels and TikTok cost $7 to $8.  The reason nobody is moving money is not performance — it is which budget line the buy sits in.",
    "stamps": [
        ("DIGIDAY · 19 AUG", "https://digiday.com/future-of-tv/future-of-tv-briefing-youtube-shorts-gains-ad-dollars-but-needs-to-crack-social-budgets/"),
    ],
    "body": [
        "Digiday put the question to buyers at Digitas, Tinuiti and Wpromote this morning.  <mark>Shorts runs $4 to $6 to put an ad in front of a thousand people.  Reels and TikTok run $7 to $8.</mark>  That is a 30 to 45% discount on the two platforms it competes with directly.",
        "So why is the money not moving?  Because of where the buy lives.  Shorts is sold inside bundled YouTube campaigns, which means it sits in the television and video budget rather than the social budget.  And once it is inside a bundle, the optimisation pushes delivery toward in-stream — the ads that run before and during regular videos — because that is where the system finds the cheapest results.  Your Shorts money quietly becomes in-stream money.",
        "One buyer put the scale of it plainly: if Meta and TikTok are taking 60% of a social budget, Shorts is not getting to 10%.",
        "The fix is boring and it is one line in a media plan.  Break Shorts out as its own line item and it has to compete on its own numbers instead of being absorbed by the rest of the buy.",
        "Now the caution, because this is buyer chatter rather than measurement.  These are ranges agency executives quoted for their own books.  No survey, no sample, no audited market average.  <mark>YouTube declined to comment.</mark>  A price gap that big usually reflects a performance gap, and nobody in the piece sizes it — so the honest read is that Shorts is cheap and untested at scale, not that it is free money.",
    ],
    "numbers": [
        ("$4–6", "shorts, per thousand people reached"),
        ("$7–8", "reels and tiktok, same measure"),
        ("<10%", "share of social budget shorts gets"),
    ],
    "flagnote": "All pricing here is self-reported by named and unnamed agency executives at three shops.  It is not audited or vendor-measured data, and YouTube declined to comment.",
    "so_what": "Shorts is cheap because it is bought in the wrong pocket, not because it underperforms.  Bundled buys let the system spend your short-form money on in-stream, so the inventory never gets a fair test and the price never gets bid up.  That gap is available to anyone willing to split the line item and actually measure it.",
    "do_this": "Ask your media team this week whether Shorts is a separate line item or sitting inside a bundled YouTube buy, and split it out if it is bundled.",
}

SECTIONS = [
    {
        "id": "ws",
        "name": "W'S",
        "page": "pg. 02",
        "note": "what worked, and the exact reason it worked",
        "tint": "blue",
        "items": [
            {
                "title": "PUBG Mobile's biggest audience in five years came from Hindi and Turkish, not English",
                "hook": "The main broadcast grew 29%.  The Hindi feed grew 248%.",
                "stamps": [
                    ("ESPORTS CHARTS · 17 AUG", "https://escharts.com/news/pmwc-2026-ewc-viewership"),
                ],
                "body": [
                    "The PUBG Mobile World Cup peaked at roughly 1.78 million people watching at the same moment during the grand finals — its best in five years and up about 29% on last year.  For scale, that is close to a strong US cable news primetime audience, and just under what Gamescom's opening show drew in 2025.",
                    "The interesting number is underneath.  <mark>Hindi-language broadcasts grew 248% in hours watched.  Turkish peak viewers grew 249%.</mark>  The overall event grew 29%.  So essentially all of the growth came from two language feeds, while the English broadcast sat roughly flat.",
                    "Two things to hold onto about the measurement.  The figure is reported inconsistently in the source — 1.79 million in one place, 1.78 in another — so treat the precision as soft.  And it explicitly excludes Chinese streaming platforms, which are not counted as comparable.",
                    "Language feeds are still sold as secondary inventory at secondary prices.  They are the only part of this event that is actually growing.",
                ],
                "so_what": "Mobile esports audiences are concentrating in South Asia and Turkey while Western viewership flattens, and the rate card has not caught up.  Rights packages price the English broadcast as the main event and treat everything else as an add-on, which means the fastest-growing audience in the tournament is also the cheapest thing in the deal.",
                "do_this": "Price the Hindi feed separately on your next mobile esports buy and compare its growth rate against the main broadcast before you accept a bundled rate.",
            },
        ],
    },
    {
        "id": "ls",
        "name": "L'S",
        "page": "pg. 03",
        "note": "not dunking, figuring out what actually broke",
        "tint": "pink",
        "items": [
            {
                "title": "Rainbow Six set a watch-time record while its live audience fell 60%",
                "hook": "Wrong owner — one co-streamer stayed home and took most of the audience with him.",
                "stamps": [
                    ("ESPORTS CHARTS · 17 AUG", "https://escharts.com/news/rainbow-six-ewc-2026-recap"),
                ],
                "body": [
                    "Rainbow Six at the Esports World Cup posted 3.7 to 3.8 million hours watched — a record for the game.  The press release writes itself.",
                    "Then the other number: <mark>peak viewers fell 60.1% year on year, to 99,200.</mark>  Last year it was around 250,000.  Esports Charts attributes the English-language collapse largely to the absence of one co-streamer, Jynxzi.",
                    "Both numbers are true and they describe the same event.  Hours watched is viewers multiplied by minutes, summed across every channel carrying the broadcast.  It rises when a tournament runs longer or adds feeds.  Broadcasting channels went from 111 to 319 here — nearly triple.  So the record is substantially a function of more airtime across more channels, not more people.",
                    "The uncomfortable version: <mark>a single creator was worth roughly 60% of this event's peak live audience</mark>, and he was not part of the rights package anyone signed.",
                ],
                "flagnote": "Esports Charts is both the source and the measurement provider here, and the piece does not state whether co-streams and Chinese platforms are inside the watch-time total.  Treat the 3.7 to 3.8 million as directional.",
                "so_what": "When you sponsor a tournament you are often really buying access to two or three co-streamers, and their attendance is not guaranteed anywhere in your contract.  Hours watched is the metric a rights holder reaches for when the audience number is bad, because airtime and channel count can carry it upward on their own.  Peak and average concurrent viewers are the ones that track actual humans.",
                "do_this": "Get your event partner to name their committed co-streamers in writing before you value the buy, and grade the result on peak and average concurrents rather than hours watched.",
            },
        ],
    },
    {
        "id": "moves",
        "name": "MOVES",
        "page": "pg. 04",
        "note": "what changed, and what it means if you are buying",
        "tint": None,
        "items": [
            {
                "title": "State Farm is buying 100,000 gifted Twitch subs instead of pre-roll",
                "hook": "A mainstream insurance brand just demonstrated the community-perk buy at scale.",
                "stamps": [
                    ("TWITCH BLOG · 18 AUG", "https://blog.twitch.tv/en/2026/08/18/subtember-2026/"),
                ],
                "body": [
                    "SUBtember runs 28 August to 1 October.  Subscriptions are 25% off for one and three months, 30% off for six, and Twitch absorbs the discount so streamers are paid at full rate.",
                    "The part worth copying: <mark>State Farm is funding 100,000 gifted subscriptions across participating channels.</mark>  Minecraft Dungeons II sponsors bonus gift subs in the finale.",
                    "That is a non-endemic brand — insurance, no gaming connection — buying its way into a community mechanic rather than an ad break.  Attribution lands across many channels at once, and the thing being given away is something the audience already wants.  There is a fixed five-week window when Twitch viewers are paying unusual attention to subscriptions, and it opens in nine days.",
                ],
                "so_what": "Gifted subs put a brand inside the moment a viewer gets something for free from a creator they like, which is a different emotional slot from an ad roll.  State Farm has now priced and executed that at six-figure volume, which gives you a public comparable to negotiate against instead of guessing.",
                "do_this": "Price a gifted-sub package against your usual streamer buy before 28 August and see which one costs less per engaged viewer.",
            },
            {
                "title": "Kick's founders took their creator community platform out of beta",
                "hook": "Another walled garden where your creator's most engaged audience goes and you cannot follow.",
                "stamps": [
                    ("TUBEFILTER · 18 AUG", "https://www.tubefilter.com/2026/08/18/club-kick-stake-founders-creator-monetization-platform/"),
                ],
                "body": [
                    "Bijan Tehrani and Ed Craven — the Kick and Stake.com founders — fully launched Club, a superfan platform with subscriptions, tipping, paywalls and an in-app currency.  They paid $10 million for the domain.",
                    "The claimed numbers: 100,000 members accumulated during beta, with one creator's page above 30,000.  <mark>All of it is company-supplied, and members is undefined</mark> — it does not mean paying subscribers.",
                    "Most new creator platforms die quietly.  This one has founders with a working platform and real capital behind them, which makes it likelier to still exist in a year.",
                ],
                "flagnote": "Every figure here comes from the company's own launch release.  Nothing is audited and members is not defined.",
                "so_what": "Each of these platforms moves a slice of a creator's most committed audience somewhere you cannot buy media against or measure.  That does not make the creator less valuable, but it does mean the audience you can reach through a public post is increasingly the less-engaged half.",
                "do_this": "Ask your top creator partners which off-platform community they are building on, and get that audience named in your next brief.",
            },
            {
                "title": "The Esports Nations Cup slipped to November 2027",
                "hook": "If you had budget parked against it, it just freed up.",
                "stamps": [
                    ("ESPORTS CHARTS · 18 AUG", "https://escharts.com/news/esports-nations-cup-postponed"),
                ],
                "body": [
                    "The inaugural Esports Nations Cup has moved from 2026 to November 2027.  Riyadh remains the host.  No viewership history exists because the event has never happened.",
                    "Short item, but a real one: a tentpole some 2026 plans were built around has moved by more than a year.",
                ],
                "so_what": "Money earmarked against an event that no longer happens this year does not reallocate itself, and the later you notice the fewer good options remain in the calendar.  The back half of 2026 still has Gamescom and the usual autumn tournaments to absorb it.",
                "do_this": "Check whether any of your 2026 esports budget was allocated against this event and move it to a Q4 property this week.",
            },
        ],
    },
    {
        "id": "onstream",
        "name": "ON STREAM",
        "page": "pg. 05",
        "note": "big live events, just finished and coming up",
        "tint": None,
        "items": [
            {
                "title": "Gamescom Opening Night Live is six days out",
                "hook": "The most predictable large audience on your calendar, and the one number that predicts the rest.",
                "open": True,
                "stamps": [
                    ("STREAMS CHARTS", "https://streamscharts.com/news/gamescom-opening-night-2025-recap"),
                    ("GAMESRADAR", "https://www.gamesradar.com/games/events-conferences/gamescom-2026-schedule/"),
                ],
                "body": [
                    "Tuesday 25 August, 11am Pacific, on YouTube and Twitch.  The Cologne show floor follows from the 26th to the 30th — 357,000 people through the doors last year.",
                    "The 2025 marks to beat: more than 2 million watching at once, 1.8 million average, 4.6 million hours watched, 72 million total views, and more than 1,100 channels carrying it.",
                    "<mark>Watch the channel count, not the viewer count.</mark>  Co-streaming channels went from about 700 to over 1,100 last year and viewership climbed with them.  It is the number that moved first.",
                    "No credible pre-show forecasts exist.  Everything currently ranking for this is scheduling filler with no data in it, so the 2025 figures are the only real reference point you have.",
                ],
                "so_what": "This is the cleanest annual test of whether letting other people rebroadcast your event beats making your own broadcast better, and it runs on a fixed date with published history.  If channel count climbs and viewership does not follow this year, the redistribution effect has found its ceiling — which is worth knowing before you plan a launch around it.",
                "do_this": "Block out 25 August and record the co-streaming channel count next to the viewer figures, so you have your own baseline for next year.",
            },
        ],
    },
    {
        "id": "watch",
        "name": "ONE TO WATCH",
        "page": "pg. 06",
        "note": "one creator worth knowing early",
        "tint": None,
        "items": [
            {
                "title": "Cullen Honohan — All Hail Bball",
                "hook": "He did not sponsor a college basketball team.  He became its broadcaster.",
                "open": True,
                "stamps": [
                    ("TUBEFILTER · 17 AUG", "https://www.tubefilter.com/2026/08/17/all-hail-bball-cullen-honohan-robert-morris-university-sponsorship/"),
                    ("CHANNEL", "https://www.youtube.com/@AllHailCullen"),
                ],
                "watch": {
                    "label": "TOP VIDEO, LAST 3 MONTHS",
                    "title": "24 Hours w/ Arkansas's #1 Recruiting Class",
                    "url": "https://www.youtube.com/watch?v=r3eW_sgvRRg",
                    "meta": "339,110 views · published 12 July 2026 · 28:20",
                    "note": "A day inside John Calipari's Arkansas program with the top-ranked recruiting class in the country.  Watch five minutes and you will see exactly what he is selling.",
                },
                "body": [
                    "He makes half-hour documentary films about basketball recruiting — embedding with high-school prospects, touring $200 million athletic facilities, running a stunt where he tries to get an unranked kid nationally ranked.",
                    "372,488 YouTube subscribers and 218 million lifetime views, plus a million on TikTok and 462,000 on Instagram.  His last fifteen uploads have done at least 3.6 million views between them.",
                    "On Monday, Tubefilter reported that All Hail Bball is sponsoring Robert Morris University's Division I men's basketball team.  <mark>It is not a jersey patch.  He becomes the program's official media partner</mark>, embedded with the team for the 2026-27 season, producing on-court and behind-the-scenes content.  First game is 2 November.  He has said he wants to run the same structure across other sports.",
                    "Every creator-buys-a-team story you already know involves a mega-name — KSI and Logan Paul at Arsenal, MrBeast with the Hornets, John Green at AFC Wimbledon.  <mark>This is the first time someone at 372,000 subscribers has taken media rights instead of a logo</mark>, and that is the version other creators can actually copy.",
                ],
                "flagnote": "No third-party growth-rate data was available for this channel — Social Blade and ViewStats both refused automated access.  Subscriber and view figures come from a live public counter and YouTube's own channel feed, observed 19 August.",
                "so_what": "From November he controls the only continuous camera inside a Division I program being set up as a Cinderella story.  That is a rights-holder position wearing a creator's clothes, and it means season-long presenting sponsorship of an episodic series rather than a sixty-second read.  The buyer is a basketball apparel brand, a sports nutrition or hydration brand, or a regional Pittsburgh advertiser — and the same shoot yields Shorts cutdowns that routinely clear 100,000 to 1.9 million views.",
                "do_this": "Watch the Arkansas film this week, then have someone contact his agent about presenting sponsorship before the season tips off on 2 November.",
            },
        ],
    },
    {
        "id": "format",
        "name": "FORMAT LAB",
        "page": "pg. 08",
        "note": "one thing about how to actually make the video",
        "tint": None,
        "items": [
            {
                "title": "Stop feeding TV cutdowns into Shorts",
                "hook": "The cheapest inventory in social has the least tolerance for repurposed footage.",
                "open": True,
                "stamps": [
                    ("DIGIDAY · 19 AUG", "https://digiday.com/future-of-tv/future-of-tv-briefing-youtube-shorts-gains-ad-dollars-but-needs-to-crack-social-budgets/"),
                ],
                "body": [
                    "The same buyers quoting the Shorts discount are explicit about why brands are not getting results there: they are running cutdowns of television spots.  <mark>The format punishes repurposed footage harder than any other placement you buy.</mark>",
                    "The reason is structural, not aesthetic.  A TV spot is built to be watched by someone already sitting still, with a slow open that earns attention over thirty seconds.  A vertical feed gives you under two seconds before a thumb moves, and it is watched by someone who did not choose your video.  Cutting the same footage shorter does not fix a wrong opening — it just gets to the wrong opening faster.",
                    "What works instead is shot for the placement: vertical framing rather than a cropped sixteen-by-nine, the payoff at the front instead of the end, a person talking to camera rather than a voiceover over b-roll, and a creator's face rather than a brand's logo doing the first two seconds.",
                    "The practical version for a production schedule: if you are already shooting a hero spot, add half a day and a vertical rig, and come away with eight to twelve native assets from the same setup and talent.  That is far cheaper than commissioning them separately later, which is what most brands end up doing.",
                ],
                "so_what": "Cheap inventory only stays cheap while it underperforms, and right now it underperforms mostly because of what brands put in it.  Native vertical assets cost a fraction of a hero spot when they are shot on the same day, and they are the thing that decides whether the price gap is an opportunity or an accurate reflection of results.",
                "do_this": "Add a vertical shoot block to your next production day and come away with eight native assets from the same setup, instead of cropping the hero spot later.",
            },
        ],
    },
]

FORECAST = [
    {
        "confidence": "LIKELY",
        "window": "next 2 quarters",
        "headline": "The Shorts price gap closes as soon as buyers split the line item",
        "body": "A 30 to 45% discount on directly comparable inventory does not survive contact with a competitive auction.  The only thing holding it open is that Shorts money keeps getting absorbed into bundled YouTube buys before it can bid.  Once enough advertisers break it out and prove the numbers, the price moves toward Reels and TikTok.",
        "do": "Run your Shorts test now, while the inventory is still priced as an afterthought.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "25 August",
        "headline": "Gamescom's channel count tells you whether redistribution has peaked",
        "body": "Co-streaming channels went from roughly 700 to more than 1,100 in a year and viewership rose in step.  If the count climbs again and viewership follows, letting other people carry your stream is still the cheapest reach in the business.  If it climbs and viewership stalls, the effect has hit its ceiling and launch plans built on it need rethinking.",
        "do": "Record the channel count on the day, not just the headline viewer figure, so you can answer this yourself next year.",
    },
    {
        "confidence": "LIKELY",
        "window": "this season",
        "headline": "Named co-streamers start appearing in sponsorship contracts",
        "body": "Rainbow Six lost 60% of its peak audience because one person did not stream.  Once a brand has eaten that outcome, the obvious response is to stop treating co-streamers as a happy accident and start naming them as deliverables.  Expect rights holders to resist, because they mostly cannot guarantee it.",
        "do": "Put a named co-streamer clause in your next event sponsorship draft and see how the rights holder reacts — their answer tells you what the audience number is really worth.",
    },
    {
        "confidence": "LONG SHOT",
        "window": "next 12 months",
        "headline": "Mid-size creators start taking media rights instead of sponsorships",
        "body": "Cullen Honohan at 372,000 subscribers took official media-partner status with a Division I program rather than a logo placement.  If that produces a watchable season, the model is copyable by any creator with a vertical audience and a small property willing to trade access for coverage.  The economics favour it — the creator gets inventory to sell rather than a one-off fee.",
        "do": "Work out which small property in your category would trade camera access for coverage, and find the creator who already covers it.",
    },
]

TLDR = [
    "YouTube Shorts costs $4 to $6 per thousand people reached against $7 to $8 for Reels and TikTok, because it is bought inside bundled YouTube campaigns.  Split Shorts into its own line item this week and make it compete on its own numbers.",
    "Rainbow Six posted record hours watched while its peak live audience fell 60%, because one co-streamer did not show up.  Name your committed co-streamers in the contract and grade events on peak concurrents instead.",
    "Brands are pushing TV cutdowns into Shorts and it is the placement least tolerant of repurposed footage.  Add a vertical shoot block to your next production day and leave with eight native assets from the same setup.",
    "State Farm is funding 100,000 gifted Twitch subs from 28 August, a non-endemic brand buying a community mechanic rather than an ad break.  Price a gifted-sub package against your usual streamer buy before the window opens.",
    "PUBG Mobile's five-year audience high came almost entirely from Hindi and Turkish feeds growing about 248%, while English stayed flat.  Price language feeds separately on your next mobile esports buy.",
    "Cullen Honohan took official media-partner rights with a Division I basketball program at 372,000 subscribers, not a jersey patch.  Contact his agent about presenting sponsorship before the season starts on 2 November.",
]
