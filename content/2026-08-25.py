# -*- coding: utf-8 -*-
"""Content for THE FEED — issue data only.  The render spec lives in build_feed.py."""

ISSUE = {
    "date_iso": "2026-08-25",
    "kicker": "Crux Media // Tuesday 25 August 2026",
    "tagline": "What brands did on YouTube yesterday, and whether it worked.",
    "pace": "STEADY",
    "next_drop": "Next drop: Wednesday, 06:30 MT",
}

LEAD = {
    "headline": "THE BEST BRANDED VIDEO ON YOUTUBE LAST WEEK CAME FROM A CHANNEL WITH 17,800 SUBSCRIBERS",
    "deck": "Tubefilter published the weekly branded video chart yesterday afternoon.  For the first time in the ranking's history, every creator in the top five was new to it.  The one at number one has fewer subscribers than a mid-sized office building has windows, and it did 29,130,708 views.",
    "stamps": [
        ("TUBEFILTER · 24 AUG", "https://www.tubefilter.com/2026/08/24/top-5-branded-videos-mrbeast-disney-quenlin-blackwell-manuel-enrique-alisha-marie-2/"),
        ("THE VIDEO ITSELF", "https://www.youtube.com/watch?v=gbc0asbK2aU"),
        ("ANC3 ON YOUTUBE", "https://www.youtube.com/@AnimeNightClub3"),
    ],
    "body": [
        "Here is the chart, straight.  Number one branded video on all of YouTube last week was a Short called \"Too far?\" from a channel called ANC3 — three brothers who make anime sketches — sponsored by Crunchyroll.  <mark>29,130,708 views.</mark>  The joke is that you can watch Crunchyroll anywhere, on any device, including on the toilet.  That is the whole video.",
        "Now the number that should stop you.  <mark>ANC3 has 17,800 subscribers.</mark>  Tubefilter says plainly it is the smallest subscriber count it has ever seen on a top five creator.  I checked the channel myself this morning and it still reads 17.8K.  A channel that would not clear the minimum threshold at most agencies just out-performed every sponsored video on the platform.",
        "It was not a fluke slot, either.  <mark>All five top creators were newcomers to the chart, and every sponsoring brand except Crunchyroll was new too.</mark>  The names you would expect got pushed down the list — WhistlinDiesel came in at 9, Dr Insanity at 11, Veritasium at 13.  Every video in the top slots was a Short.",
        "So why does subscriber count stop predicting anything here?  Because Shorts and long-form are two different distribution machines wearing the same logo.  A subscriber is a long-form asset — it puts your video in someone's subscription feed and fires a notification.  <mark>The Shorts feed does not work that way.  It serves videos to strangers, one at a time, and decides what to serve next based on how the last one performed, not on who follows the account.</mark>  Subscribers are almost irrelevant to that decision.",
        "Which means that when you pay a premium for subscriber count on a Shorts deal, you are paying for a distribution mechanism the format does not use.  You are buying a season ticket to a stadium the match is not being played in.",
        "Look at what the brands who figured this out are actually doing.  Trü Frü, the fruit snack company, took the number two slot with Thesisterz at 12,830,602 views — and it also sponsored the videos at number 22, number 72, number 865 and number 2,224 in the same week.  Medal.tv, in the top five for the first time ever, <mark>sponsored eight videos that week</mark>.  BetterHelp, still one of the most prolific sponsors on the platform, <mark>paid for 40 videos in a single week</mark>.  Nobody is placing one expensive bet.  They are placing forty cheap ones and letting the feed sort it out.",
        "One honest caveat before you rebuild your buying model around this.  A single week of one chart is a snapshot, and Shorts results swing hard.  But the direction is not new information — it is the arithmetic of how the feed works, and this week it is unusually legible.",
    ],
    "numbers": [
        ("17.8K", "subscribers on the number one branded video"),
        ("29,130,708", "views it did anyway"),
        ("5 of 5", "top creators new to the chart"),
    ],
    "flagnote": "All chart data comes from Gospel Stats via Tubefilter, which publishes a snippet of a larger paid brand report, so the full methodology is not public and the rankings cannot be independently reproduced.  The 17,800 subscriber figure is Tubefilter's and was confirmed against ANC3's own public channel page this morning.  View counts on this chart were recorded before YouTube's 24 August counting change took effect, which matters — see L'S.",
    "so_what": "Subscriber count tells you how many people asked to hear from someone.  On Shorts, nobody is asking — the feed decides, video by video, and it re-decides every time.  So the price you pay for a big subscriber number on a Shorts brief is a price for something the format never spends.  The brands winning this chart worked that out and switched from one hero placement to forty small ones.",
    "do_this": "Take your next Shorts brief and split the budget you would have spent on one large creator across eight to ten small ones, brief them identically, and rank them on views per pound at the end of the month.",
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
                "title": "KFC spent two years letting IShowSpeed advertise it for free, then finally paid him",
                "hook": "The affinity was already there.  The deal is just the paperwork catching up.",
                "open": True,
                "stamps": [
                    ("PR NEWSWIRE · 24 AUG", "https://www.prnewswire.com/news-releases/kfc-debuts-new-hot-ranch-big-dip-taps-ishowspeed-to-bring-big-dip-energy-nationwide-302858454.html"),
                    ("DEXERTO · 24 AUG", "https://www.dexerto.com/food/ishowspeeds-kfc-obsession-lands-him-a-commercial-for-new-hot-ranch-dip-3401669/"),
                ],
                "body": [
                    "KFC launched a product yesterday called the Hot Ranch Big Dip — a four-ounce tub of ranch with garlic, herb and chilli, four times the size of the standard dip — and put IShowSpeed in a sixty-second spot to sell it.  The joke in the ad is that he misreads the brief and turns up expecting an actual ranch.  It runs on YouTube and social.",
                    "Here is the part worth writing down.  <mark>Speed has been talking about KFC unprompted, on stream and on tour, for years before anybody paid him.</mark>  He visited KFC branches on his world tours and brought it up on his own.  KFC's Denmark arm publicly offered him a collaboration around 2024, roughly two years ago.  The company had already given him what it called KFC for life, and his reaction to that went viral on its own.",
                    "KFC's US marketing chief Melissa Cash said it out loud in the release — Speed <mark>\"has been part of the KFC story long before this partnership\"</mark>.  Speed's line was \"everybody knows I love KFC.\"  Neither of them is pretending this was a casting decision.",
                    "The mechanism is about where the credibility comes from.  A paid endorsement asks an audience to believe that this person likes this thing.  A paid endorsement of something the person has been shouting about for free for two years does not have to ask — the audience already watched it happen, unpaid, dozens of times.  The money did not buy the affinity.  It bought permission to put a camera on affinity that already existed and was already public.",
                    "More is coming.  KFC says further work with Speed lands in autumn, with fans involved.",
                ],
                "so_what": "Every brand of any size has creators talking about it for nothing right now, and almost nobody has a list of who they are.  That list is the cheapest talent shortlist in the building, because the hardest part of a creator deal — making the enthusiasm believable — is already done and already on the record.  KFC's only real skill here was noticing.",
                "do_this": "Run a search this week for unpaid mentions of your brand across YouTube, TikTok and Twitch over the last twelve months, rank the creators by how often they brought you up on their own, and take the top three to your next planning meeting.",
            },
        ],
    },
    {
        "id": "ls",
        "name": "L'S",
        "page": "pg. 03",
        "note": "what broke, and the failure mode that broke it",
        "tint": "pink",
        "items": [
            {
                "title": "Wrong economics: every view count on YouTube went up yesterday, and the smallest channels went up the most",
                "hook": "A study of 35,800 videos says the inflation is not even.  It is biggest exactly where you were about to start buying.",
                "open": True,
                "stamps": [
                    ("YOUTUBE HELP", "https://support.google.com/youtube/answer/2991785?hl=en"),
                    ("AGENTIO · 21 AUG", "https://www.agentio.com/blog/youtube-view-vs-engaged-view"),
                    ("FORBES · 17 AUG", "https://www.forbes.com/sites/gabrielalinzainescu/2026/08/17/youtube-changes-how-it-counts-views-handing-marketers-two-numbers-instead-of-one/"),
                ],
                "body": [
                    "We flagged this change when YouTube announced it on 17 August.  It went live yesterday, so this is the part that actually affects your budget.  YouTube's own help page now reads: <mark>\"Beginning August 24, 2026, views are counted the moment a video starts to play across all formats, including Shorts, long-form videos (VOD), and live streams.\"</mark>  First frame.  No minimum watch time.  The old stricter measure survives, renamed engaged views, and it only appears inside YouTube Studio.",
                    "Agentio has now put a size on the gap.  It looked at <mark>35,800 creator videos published in June and July</mark> and estimates public long-form view counts will run <mark>roughly 30% above engaged views</mark>.  On Shorts, which made this change back in 2025, it measured the gap directly at <mark>65%</mark>.",
                    "Now the number that connects this to today's lead.  <mark>The inflation is not evenly spread.  Micro channels — those doing 10,000 to 50,000 median views a month — inflate by 32.4%.  Macro channels doing 300,000 or more inflate by 26.6%.</mark>  Desktop-heavy channels rise most at 37.2%, television-heavy channels least at 28.9%.  By subject, technology and fitness rise 36.5%, gaming 27%.",
                    "Read those two paragraphs together.  The lead says go and buy small Shorts creators.  This says the public numbers of small creators just inflated by about a third, more than anyone else's, and their rate cards have not moved yet.  For a few weeks you are looking at a number that got bigger for free, on the exact tier you were about to negotiate against.",
                    "The failure mode is economics, and it is entirely avoidable.  Anyone who signs a deal this month priced against raw public views is paying roughly a third more per unit of actual attention than they did in July, and any chart comparing September against August will show a rise that is pure accounting.  The fix is one word in a contract.",
                ],
                "flagnote": "Agentio operates a YouTube creator advertising marketplace and prices its own product on engaged views, so a finding that public view counts are inflated flatters what Agentio sells.  Its 30% long-form figure is an estimate, not a measurement — YouTube has never published the engagement threshold, so Agentio assumed 30 seconds and modelled from early retention curves.  Only the 65% Shorts figure is directly measured.  This brief covered the announcement of this change on 17 August; what is new here is that it is now live and that the distortion has been sized by channel tier.",
                "so_what": "A metric changed definition overnight and every price in the market is still quoted in the old one.  That gap is temporary and it is currently pointing in the buyer's favour, but only if you say which number you mean.  Say views in a contract this month and you have agreed to a figure that measures whether a video started, not whether anyone watched it.",
                "do_this": "Write engaged views into every creator contract you sign from today, and screenshot the dashboards on your live campaigns now so you have a clean reading from before the change to compare against.",
            },
            {
                "title": "Wrong owner: the celebrity drinks brands are closing, and the best owned audience in podcasting could not save one",
                "hook": "Messi's brand is gone.  Alex Cooper's goes this autumn.  Fame sells the first bottle and nothing after it.",
                "stamps": [
                    ("MODERN RETAIL · 25 AUG", "https://www.modernretail.co/operations/why-more-celebrity-led-brands-are-shutting-down/"),
                ],
                "body": [
                    "Modern Retail ran the list this morning.  <mark>Lionel Messi's hydration drink Mas+ shut down less than two years after launch.  Alex Cooper's Unwell — electrolyte, energy and protein drinks — is being discontinued this autumn after its Halloween flavours.</mark>  Kim Kardashian's Skkn closed in 2025 after several relaunches.  Gwen Stefani's Gxve Beauty shut this year.  Drew Barrymore's Flower Beauty was discontinued last year.",
                    "Mas+ was not under-resourced.  It launched with Mark Anthony Group, the company behind White Claw, which gave it real distribution in year one, and it was positioned squarely against Logan Paul's Prime.  It still missed its sales goals in a category growing at over 29% a year, and it picked up trademark litigation from Prime along the way.",
                    "The Unwell case is the one that should worry anyone buying creator audiences.  Cooper has one of the most engaged owned audiences in podcasting — the exact asset this industry keeps telling brands is the real prize — and it did not convert into a beverage business.",
                    "Two quotes carry the whole mechanism.  Sunny Bonnell, who runs the branding agency Motto: <mark>\"There is a big difference between having attention and having permission to enter a category.\"</mark>  And Mark Gallo, a drinks distribution manager who has worked at Anheuser-Busch and Heineken: <mark>\"Retail is a velocity business.  Those are not the same currency.\"</mark>",
                    "Gallo's version of why is blunt and worth quoting in full.  The famous name converts the first purchase and drives trial.  Taste, effectiveness and price drive the second.  <mark>\"Most celebrity brands are a 'me too' formulation at a usually a premium price, so there is no second purchase.\"</mark>  An audience is a launch mechanism.  It is not a product.",
                    "The failure mode is ownership, and it runs the opposite way to how these deals are usually pitched.  Giving a creator equity does not transfer their credibility onto a product — it just puts their name on a thing that has to survive a supermarket shelf on its own merits, in a category where dozens of new drinks launched in the United States this year alone.",
                ],
                "so_what": "The pitch for creator-owned brands has always been that the audience comes with them.  It does, for exactly one purchase.  After that the product is competing on taste and price against companies that have been doing this for a century, and the audience is not standing in the aisle to help.  If you are being sold equity in a creator brand, the question is not how big their following is — it is what the product does that the incumbent does not.",
                "do_this": "Before you sign any creator-equity deal, ask the founder to show you repeat purchase rate rather than first purchase rate, and walk away if they will only show you launch week.",
            },
        ],
    },
    {
        "id": "moves",
        "name": "MOVES",
        "page": "pg. 04",
        "note": "deals, launches and rule changes you should know happened",
        "tint": None,
        "items": [
            {
                "title": "YouTube is building always-on channels out of creator back catalogues",
                "hook": "It started as a Coachella experiment.  It is now aimed at your television.",
                "stamps": [
                    ("TUBEFILTER · 24 AUG", "https://www.tubefilter.com/2026/08/24/youtube-expands-stations-beyond-music-and-into-the-realm-of-creator-content/"),
                    ("YOUTUBE COMMUNITY", "https://support.google.com/youtube/thread/18138167"),
                    ("SOCIAL MEDIA TODAY · 23 AUG", "https://www.socialmediatoday.com/news/youtube-expands-stations-experiment/828551/"),
                ],
                "body": [
                    "YouTube is expanding a feature called Stations beyond music artists and into <mark>creator content, media channels and podcasts</mark>.  A Station is a rolling, always-on channel assembled from an existing catalogue, with live chat running alongside it — YouTube's own words are \"an always-on, lean-back viewing experience.\"  It started as a Coachella test in April.  It now shows up in Home and Search on phone, desktop and television, everywhere except Portugal, Switzerland and Türkiye.",
                    "It is still an experiment with a limited number of creators, and YouTube has published no selection criteria.  More importantly for anyone with a budget, <mark>it has said nothing about whether Stations carry ads, sponsorships or any existing money-making tool.</mark>  So there is nothing to buy today.",
                    "What it tells you is where the platform thinks the fight is.  Netflix has been buying creator programmes hard, and YouTube has been paying some creators to stay away.  A channel that just runs, that you put on and leave on, is a television product, not a video-sharing product.  That is the shelf brands already buy free streaming channels on.",
                ],
                "so_what": "Lean-back inventory built from library content is a different buy from a video placement — it is closer to buying a slot on a small cable channel.  If YouTube opens this to brands, the creators worth talking to will be the ones with a deep back catalogue that still plays, not the ones with the best single upload.  That is a different shortlist to the one on your desk.",
                "do_this": "Ask your three biggest creator partners this week whether they have been offered a Station, and note which of them have enough evergreen back catalogue to fill one.",
            },
            {
                "title": "X is launching a creator payments scheme on 8 September and has published no rates",
                "hook": "Quality over quantity, they say.  No numbers, they also say.",
                "stamps": [
                    ("DIGIDAY · 25 AUG", "https://digiday.com/media/x-creates-a-new-revenue-model-for-creators-but-will-it-actually-win-them-over/"),
                ],
                "body": [
                    "X is replacing its 2023 revenue share with an Original Content Rewards Program, launching <mark>8 September</mark>.  The old scheme paid anyone with a Premium subscription, five million organic impressions across three months and 500 verified followers, which meant it paid aggregators and rage-bait accounts as readily as anyone else.  The new one says it rewards original, high-quality work.",
                    "<mark>X has published no rates, no percentages, no payout terms and no eligibility criteria.</mark>  That absence is the story.  Nobody can model whether this is worth showing up for.",
                    "The agencies Digiday spoke to were cold.  Viral Nation's chief executive said his creators have not mentioned X in multiple years.  A media buyer said she does not recommend it to finance or technology clients.  NowThis Media's representative said \"the risk was not worth the reward\" and the company does not even link an X account from its site.",
                    "One counterpoint worth keeping.  Doug Landers of Greenlight Group argues X is a poor payer but an unmatched place for organised fandoms — people who translate, archive and campaign for free, <mark>\"at a scale essentially no marketing budget can buy.\"</mark>  That is a real asset and it is not the same asset as reach.",
                ],
                "so_what": "A payments scheme with no published rate is a press release, not a market.  Until X puts a number on it there is nothing for a creator to plan against and nothing for a buyer to price.  If X matters to your brand at all right now it matters as a place where existing fans organise, which is a community job rather than a media buy.",
                "do_this": "Wait for the 8 September terms before committing anything to X, and in the meantime check whether your brand already has an organised fan community there that nobody on your team is talking to.",
            },
            {
                "title": "Roblox has banned reward-driven scrolling feeds for its youngest audiences, effective immediately",
                "hook": "If your branded world pays kids to keep watching, it comes down.",
                "stamps": [
                    ("ROBLOX DEVELOPER FORUM · 25 AUG", "https://devforum.roblox.com/t/roblox-kids-and-select-new-restrictions-on-reward-driven-media-feeds/4829188"),
                    ("DEXERTO · 25 AUG", "https://www.dexerto.com/roblox/roblox-bans-doomscrolling-games-for-kids-following-outcry-3401895/"),
                ],
                "body": [
                    "Roblox posted new restrictions this morning covering its Kids and Select maturity tiers.  An experience is banned if it combines all three of these: <mark>a media feed of short videos, images or story-style posts; a feed that autoplays, loops or scrolls on its own; and a reward, or an implied reward, for continued watching.</mark>",
                    "It is effective immediately and compliance reviews are already running.  Anything non-compliant comes out of the Kids and Select tiers until it is rebuilt and re-reviewed.  Rewarded video ads that the user starts themselves are explicitly exempt, and so are autoplay feeds with no reward attached.",
                    "The trigger is the reward loop bolted onto passive watching, not the feed itself.  If a brand has built a Roblox world for under-13s with a watch-to-earn mechanic in it, that is now a delisting risk from the two youngest tiers on the platform.",
                ],
                "so_what": "Platforms are starting to legislate against the specific pattern of paying children to keep watching, and the rule here is narrow and testable rather than vague.  Any brand build aimed at kids should be audited against those three conditions, because the removal happens at the platform's pace, not yours.",
                "do_this": "Audit any Roblox experience your brand runs for under-13s this week against the three conditions, and strip out any reward tied to continued watching before a compliance review finds it.",
            },
            {
                "title": "X shipped an advertiser tool for AI agents, and it is the last major platform to do so",
                "hook": "Meta, TikTok, Pinterest and Snapchat already had one.",
                "stamps": [
                    ("MEDIAPOST · 25 AUG", "https://www.mediapost.com/publications/article/417438/x-becomes-latest-social-app-to-launch-advertiser-m.html"),
                ],
                "body": [
                    "X launched a tool today that connects AI assistants directly to <mark>23 of its advertising tools</mark>, so a buyer can create, manage and report on campaigns by typing an instruction rather than clicking through a dashboard.  The example given is a plain sentence naming a budget, a duration, a country and a goal.",
                    "<mark>Meta, Pinterest, TikTok and Snapchat all shipped equivalents over the past year.</mark>  X is the last of the majors to arrive, which makes today less a launch than a completion.",
                    "The reason to care is not X.  It is that describing a campaign in a sentence is now the standard way to buy social media, across every large platform, and the skill that used to sit in a junior buyer's hands is moving into a text box.",
                ],
                "so_what": "Every major social platform can now be bought by an AI assistant reading plain English, which changes who on your team is capable of placing a campaign and how fast a bad instruction becomes live spend.  The controls that used to be enforced by the dashboard being fiddly are gone.  Whatever approval process you have needs to sit before the sentence gets typed, not after.",
                "do_this": "Write down who on your team is allowed to spend money through an AI assistant and what the per-campaign ceiling is, and circulate it before anyone connects one to a live ad account.",
            },
        ],
    },
    {
        "id": "onstream",
        "name": "ON STREAM",
        "page": "pg. 05",
        "note": "the live numbers, and what they are worth against something you recognise",
        "tint": None,
        "items": [
            {
                "title": "The biggest event in Dota grew 0.4% and is being reported as a record",
                "hook": "Same airtime as last year.  Which is the only reason you can tell.",
                "open": True,
                "stamps": [
                    ("ESPORTS CHARTS · 24 AUG", "https://escharts.com/news/team-spirit-makes-history-international-2026"),
                    ("ESPORTS CHARTS · CS AT EWC", "https://escharts.com/news/ewc-2026-cs-tops-1m-peak-viewers"),
                ],
                "body": [
                    "The International 2026 finished in Shanghai on Sunday, Team Spirit beating PVISION 3-2.  Esports Charts has the grand final at a <mark>peak of 1,792,174 concurrent viewers</mark>, an <mark>average of 588,564</mark> and <mark>64,349,633 hours watched</mark> across 109 hours and 20 minutes of airtime.",
                    "Make the big number mean something first.  1,792,174 people watching the same match at the same moment is about <mark>ninety sold-out Madison Square Gardens</mark>, all watching one screen.  And 64.3 million hours of viewing is <mark>a bit over seven thousand years</mark> of continuous human attention, spent on ten days of Dota.",
                    "Now the part everybody is skipping.  Against last year: <mark>peak up 0.4%, hours watched up 1.9%, average viewers up roughly 1.1%.</mark>  Esports Charts is explicit that the two editions had almost identical airtime.  Those are rounding errors.  This is not a record year, it is a flat year, and it sits third in the tournament's own history behind The International 10 at 2.74 million and The International 2019 at 1.97 million.",
                    "Compare that to the Counter-Strike event at the Esports World Cup, which finished a week ago.  <mark>Its hours watched nearly doubled year on year.</mark>  Sounds enormous.  Esports Charts says plainly the gain came from a format change — a group stage was added and the field expanded, so there were substantially more matches.  More airtime, more hours.  The audience did not double.",
                    "So here is the mechanism, and it is the single most useful thing on this page.  <mark>Hours watched is the product of how many people are watching and how long you broadcast for, and the organiser controls the second one entirely.</mark>  Adding a day costs an organiser almost nothing and adds hours watched for free.  The only way to read the number honestly is to hold airtime constant — which is exactly why the Dota figure is trustworthy and flat, and the Counter-Strike figure is impressive and meaningless.",
                    "Which is why average concurrent viewers is the number to negotiate on.  It already has the division done.  Peak tells you the size of the biggest moment, average tells you what a typical minute is worth, and hours watched tells you mostly how long the organiser decided to stay on air.",
                ],
                "numbers": [
                    ("1,792,174", "peak concurrents, dota grand final"),
                    ("588,564", "average across the tournament"),
                    ("0.4%", "growth on last year at peak"),
                ],
                "flagnote": "All figures are Esports Charts third-party estimates, sampled from public viewer counts on tracked channels rather than supplied by the platforms.  Esports Charts states that it excludes Chinese livestreaming services entirely, which matters a great deal here because The International 2026 was held in Shanghai — the true global audience is materially higher than 1,792,174 and nobody outside the organiser can say by how much.  The Madison Square Garden and seven thousand year comparisons are our own arithmetic, not published figures.",
                "so_what": "An organiser who adds a day to the schedule can grow hours watched without adding a single viewer, and every sales deck in this business leads with hours watched for exactly that reason.  Average concurrent viewers cannot be inflated that way, because lengthening the broadcast drags the average down.  When a rights holder shows you a big growth number, the first question is whether the event got longer.",
                "do_this": "Ask for last year's and this year's airtime alongside any hours watched figure you are quoted, and if airtime went up, price the deal off average concurrent viewers instead.",
            },
        ],
    },
    {
        "id": "watch",
        "name": "ONE TO WATCH",
        "page": "pg. 06",
        "note": "one creator with momentum, and what to buy from them",
        "tint": None,
        "items": [
            {
                "title": "kajal chouhan",
                "hook": "Two million subscribers.  Two point four billion views.  She went from rank 764 to rank 23 in a single week.",
                "open": True,
                "stamps": [
                    ("TUBEFILTER TOP 50 VIEWED · 24 AUG", "https://www.tubefilter.com/2026/08/24/top-50-most-viewed-youtube-channels-week-of-08-23-2026/"),
                    ("TUBEFILTER TOP 50 SUBBED · 24 AUG", "https://www.tubefilter.com/2026/08/24/top-50-most-subscribed-youtube-channels-week-of-08-23-2026/"),
                    ("YOUTUBE CHANNEL", "https://www.youtube.com/@KajalChouhan01"),
                ],
                "body": [
                    "If you read today's lead and want the extreme version of it, here she is.  In the week of 17 to 23 August, Tubefilter's global charts have kajal chouhan at <mark>number 23 for views with 437,839,041 in seven days — up 613%, from rank 764 the week before.</mark>  She also came in at number 31 for subscriber gain with 280,000, up 600%, from rank 780.  Two charts, both from outside the top 750, in one week.",
                    "Now the ratio that should make a buyer sit up.  Her channel this morning reads <mark>2.05 million subscribers against 2,417,936,416 lifetime views</mark> across 210 videos.  That is roughly <mark>1,180 views for every single subscriber she has.</mark>  Most channels her size run a tiny fraction of that.  She is a distribution machine with almost no audience relationship, which is precisely the shape today's lead says the Shorts feed rewards.",
                    "She is Hindi-language, based in India, and the channel opened in September 2023.  The format is two things on repeat, and both are built around a physical object.  One is prop-driven family and school comedy with recurring characters, where the gag is almost always food — who ate the cake, who hid chilli in it, whose chips went missing.  The other is craft and drawing challenges, mixing colours and making a rose or a giraffe out of paint and household bits.",
                    "The best-performing upload of the last three months is below, at just under sixty million views.  <mark>She is still accelerating right now</mark> — Tubefilter's chart snapshot recorded her lifetime views at 2,288,066,631, and the channel read 2,417,936,416 two days later.  That is about 130 million views in roughly forty-eight hours.",
                    "The honest caveat.  Her monster videos came in a May and June run, and her August uploads are running much smaller, which means a good part of this surge is YouTube resurfacing an old catalogue rather than new work breaking out.  That is genuinely good news if you care about a video still earning six months later.  It also means the timing of any single sponsored post is less predictable than 613% makes it sound.",
                ],
                "watch": {
                    "label": "TOP VIDEO, LAST 3 MONTHS",
                    "title": "Balloon drawing challenge part-2 #drawing #art #trending #foryou #youtubeshorts",
                    "url": "https://www.youtube.com/watch?v=boDHaHuHRMY",
                    "meta": "59,535,246 views · published roughly two months ago · YouTube Shorts",
                    "note": "A wordless craft challenge where the tools are the entire premise, which is exactly where a branded product would sit.",
                },
                "flagnote": "The weekly ranks, weekly gains and percentage changes are Tubefilter chart estimates built on Gospel Stats data and are already a day old.  The subscriber count, lifetime view total and video count were read from the channel's own public pages this morning.  YouTube's watch pages rate-limited us, so the publish date of the featured video is YouTube's own relative label rather than an exact date; the video ID was confirmed against YouTube's oembed service, which returned the matching title and author.",
                "so_what": "The buyers who should be calling are Indian snack, confectionery, instant-food, ice cream and craft or stationery brands, plus back-to-school retail.  What they are buying is the object, not a mention — in the comedy format your product becomes the thing that gets eaten or stolen, and in the craft format your paints or markers become the tools.  She already runs part-one, part-two, part-three series, so the right buy is a short series of Shorts rather than a single placement, and nobody has set a price on her yet.",
                "do_this": "Have someone who reads Hindi watch her last twenty Shorts this week and come back with a note on which of your products could physically replace the prop in the premise, then approach her with a three-video series and a specific object.",
            },
        ],
    },
    {
        "id": "money",
        "name": "THE MONEY",
        "page": "pg. 07",
        "note": "what things cost and who is getting paid",
        "tint": None,
        "items": [
            {
                "title": "Publicis and Travis Kelce are building an index over the $4.5 billion college athlete market",
                "hook": "Tens of thousands of athletes, 68 universities, and a claim that they engage four points better than influencers.",
                "open": True,
                "stamps": [
                    ("MARKETING DIVE · 24 AUG", "https://www.marketingdive.com/news/publicis-tackles-fragmented-nil-market-with-travis-kelce-3-arts-sports/828498/"),
                ],
                "body": [
                    "Publicis Sports, the Kansas City Chiefs tight end Travis Kelce, and Lionsgate-owned talent shop 3 Arts Sports announced a joint venture yesterday called Tekta.  It sells brands access to student athletes — <mark>tens of thousands across 68 Power Four universities</mark> — with the legal compliance handled and one measurement framework over the top.  The market it is aiming at is valued at <mark>$4.5 billion</mark> by the platform Opendorse.",
                    "The performance claim underneath it is the number to interrogate.  <mark>Opendorse found student athlete brand partners deliver an average engagement rate of 5.7%, nearly four percentage points higher than traditional influencers.</mark>",
                    "Take that seriously but understand what it is measuring.  Engagement rate is the share of an audience that reacts, and it runs high on small, local, tightly bound audiences almost by construction — a college quarterback's following is largely people who actually live near him and know who he is.  That is a real and useful property, but it is not evidence of better sales.  It is evidence of a smaller, denser audience, which is why the rate is high.",
                    "Publicis Sports chief executive Suzy Deering framed the problem as reach at a local level: clients want to connect locally while still adding up to something national, and doing that brand-side has been <mark>\"challenging — if not impossible — given all the pain points.\"</mark>  Tekta promises <mark>50% to 70% faster speed to market</mark> than current offerings.",
                    "The shape of this is worth noticing on its own.  College athlete deals, beauty creators through Ipsy, creators on X — the money is moving toward middlemen who sell the same promise, which is that a market is too fragmented to buy directly and they will index it for you.  Sometimes that is true.  It is always more expensive than buying direct.",
                ],
                "flagnote": "Opendorse is a college athlete deal platform and both the $4.5 billion market size and the 5.7% engagement figure come from it, so the company supplying the numbers sells into the market those numbers make attractive.  Neither figure has been independently audited.  Engagement rate is a ratio of reactions to audience size and says nothing about sales.  Tekta's speed and pricing claims are its own and are not yet demonstrated by any completed campaign.",
                "so_what": "A high engagement rate on a small local audience is a genuinely different product from reach, and it is the right buy if you have something to sell in a specific town.  What it is not is a cheaper way to buy national scale, and the joint venture selling it takes a margin for assembling it.  Before you pay for the index, work out whether three direct deals would do the job.",
                "do_this": "If you have regional sales targets, price one direct deal with an athlete at a single university against what an agency quotes for the same reach, and use the gap to decide whether the middleman is worth it.",
            },
        ],
    },
    {
        "id": "format",
        "name": "FORMAT LAB",
        "page": "pg. 08",
        "note": "one production decision, taken apart",
        "tint": None,
        "items": [
            {
                "title": "Shein ran two sponsored Shorts in the same week.  One placed third on YouTube.  The other placed 1,080th",
                "hook": "The polished one lost.  By about a thousand places.",
                "open": True,
                "stamps": [
                    ("TUBEFILTER · 24 AUG", "https://www.tubefilter.com/2026/08/24/top-5-branded-videos-mrbeast-disney-quenlin-blackwell-manuel-enrique-alisha-marie-2/"),
                ],
                "body": [
                    "This is the cleanest natural experiment on the chart, because the variable that changed is the format and nothing else.  Same brand, same week, same platform, same category of creator.",
                    "Video one.  Roya Destroyaa, 693,000 subscribers.  The entire video is <mark>two grown women screaming and crying like toddlers</mark>.  That is it.  There is no clothing shown, no styling, no product beat at all.  <mark>10,884,166 views, third-highest branded video on all of YouTube last week.</mark>",
                    "Video two.  Clara Afua, an elegant try-on montage — clothes, styling, the thing Shein actually sells, shot properly.  <mark>It came in at number 1,080.</mark>",
                    "Tubefilter's own read on the first one is that it says something about viewer taste, and it does.  But the production lesson is more specific than taste, and it is about the first second.",
                    "A Shorts viewer is not choosing your video.  They are being handed it, mid-scroll, with a thumb already in motion.  <mark>The only question that gets answered in frame one is whether this is an advert.</mark>  A try-on montage answers yes immediately — the lighting, the framing, the clothes on a rail, all of it reads as commercial before a word is spoken, and the thumb keeps moving.  Two people screaming answers no, or answers nothing at all, which is enough to buy the next two seconds.",
                    "Look at the number two video on the same chart and the pattern holds.  Thesisterz playing a fast maths game with a bag of Trü Frü sitting in shot — Tubefilter notes there is <mark>no product spot in it at all</mark> — did 12,830,602 views.  The product is furniture.  It is in the room while something else is happening.",
                    "The trap here is obvious and worth naming, because this is the part people get wrong.  This is not an argument that the product should be invisible.  It is an argument that the product cannot be the reason the video starts.  In the lead's number one video the Crunchyroll joke is the premise and it still won, because the joke is funny first and an advert second.  The order matters more than the presence.",
                ],
                "flagnote": "All rankings and view counts come from Gospel Stats via Tubefilter's weekly brand report, which publishes a partial extract, so the full ranked list cannot be independently checked.  Two videos from one brand in one week is an illustration, not a controlled test — the creators have different audiences and the videos were served to different people.",
                "so_what": "The brief you write decides this before anyone shoots anything.  Ask for a product showcase and you get a video that announces itself as an advert in frame one, and on Shorts frame one is the entire negotiation.  Ask for a premise that happens to contain your product and you buy yourself the two seconds you need.  Shein paid for both this week and one of them worked a thousand times harder.",
                "do_this": "On your next Shorts brief, delete the requirement for a product demonstration and replace it with one line — the product must be present in frame one and must not be what frame one is about — then judge the cuts on whether you would keep scrolling.",
            },
        ],
    },
]

FORECAST = [
    {
        "confidence": "LIKELY",
        "window": "next 3 months",
        "headline": "Creator rate cards reprice against the inflated view number, and the buyers who move first get a discount",
        "body": "Public view counts went up by roughly a quarter to a third yesterday and every rate card in the market was written against the old definition.  Rate cards do not move overnight — they move at renewal, which for most creator rosters means the next quarter.  In the gap, a buyer who signs against engaged views is paying July prices for July attention while everyone else's headline numbers drift upward.  Expect the larger talent agencies to reprice first because they have the analytics to notice, and the smaller independent creators to reprice last, which is the tier where the inflation is biggest.",
        "do": "Sign your next three creator deals against engaged views this month rather than waiting for a standard contract update.",
    },
    {
        "confidence": "LIKELY",
        "window": "next 6 months",
        "headline": "Volume buying across small Shorts creators becomes the default, not the experiment",
        "body": "Trü Frü sponsored five videos in one week, Medal.tv eight, BetterHelp forty, and the top of the branded chart went entirely to newcomers with small followings.  The economics are simple — Shorts distribution is decided per video, so spreading a budget across many creators is buying more lottery tickets rather than a bigger one.  What has been missing is a chart anyone can point at in a meeting, and now there is one.  Watch packaged goods and app companies move first, because they have the volume of creative and the least attachment to a single celebrity face.",
        "do": "Run one volume test this quarter against eight to ten small creators and record cost per thousand views so you have your own benchmark.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "by the end of Q1 2027",
        "headline": "The celebrity equity brand goes out of fashion and paid partnerships come back",
        "body": "Five celebrity-led brands closed inside two years, and the Unwell shutdown is the one that will change minds, because Alex Cooper had the exact asset this industry says matters most and it still did not produce repeat purchases.  Equity deals were sold on the theory that an audience transfers to a product.  The evidence says an audience transfers to a first purchase.  Expect the pitch to shift back toward paid partnerships with performance terms, which cost less and fail smaller, and expect at least two more celebrity drinks brands to announce closures before spring.",
        "do": "Move any creator-equity conversation you are in toward a paid partnership with a performance clause and see whether the creator still wants it.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "next 12 months",
        "headline": "YouTube opens Stations to advertisers and creates a television-shaped inventory nobody has priced",
        "body": "Stations exists because Netflix is buying creator programmes and YouTube wants the living room.  Right now there are no ads in it and no published rules for getting one.  The moment it carries advertising it becomes a lean-back channel built from library content, which is a completely different buy from a video placement and is priced closer to a small streaming channel.  The creators who win that are the ones with hundreds of hours that still play, not the ones with the best single upload, and almost nobody is currently valued on their back catalogue.",
        "do": "Start noting which of your creator partners have a deep evergreen back catalogue, because that is what gets valuable if this opens up.",
    },
    {
        "confidence": "LONG SHOT",
        "window": "next 12 months",
        "headline": "A brand publishes what it actually paid for a college athlete campaign and breaks the pricing fog",
        "body": "The college athlete market is worth $4.5 billion by its own vendors' reckoning and there is no public price for anything in it, which is exactly why an agency joint venture can promise to index it.  Every opaque market gets priced eventually, and it usually happens because one buyer publishes.  A brand with regional sales targets that runs a direct deal at a single university and puts the invoice next to the results would do more damage to the middleman layer than a year of trade coverage.  It is a long shot because nobody has an incentive to be first.",
        "do": "Run one direct college athlete deal and record what you paid, so you have a private benchmark even if nobody publishes a public one.",
    },
]

TLDR = [
    "The most-watched branded video on YouTube last week came from a channel with 17,800 subscribers and did 29,130,708 views, and all five top creators were new to the chart.  Split your next Shorts budget across eight to ten small creators instead of one large one and rank them on views per pound at month end.",
    "YouTube started counting a view from the first frame yesterday, and Agentio's study of 35,800 videos estimates public counts now run about 30% above the old measure, rising to 32.4% for the smallest channels and 65% on Shorts.  Write engaged views into every creator contract you sign from today.",
    "Shein ran two sponsored Shorts in the same week — a chaotic one with no product in it placed third on YouTube, and a polished try-on montage placed 1,080th.  Rewrite your next Shorts brief so the product must appear in frame one but must not be what frame one is about.",
    "KFC put IShowSpeed in a commercial yesterday after two years of him promoting the chain unpaid on stream and on tour, and its own marketing chief said he was part of the story long before the deal.  Search your unpaid brand mentions from the last twelve months and take the three most frequent creators to your next planning meeting.",
    "The International 2026 peaked at 1,792,174 concurrent viewers on Sunday against an average of 588,564, up just 0.4% on last year at identical airtime, while the Counter-Strike event that nearly doubled its hours watched did so by adding a group stage.  Ask for airtime alongside any hours watched figure and price off average concurrent viewers when the event got longer.",
    "Five celebrity-led brands have closed in two years, including Alex Cooper's Unwell despite one of the most engaged owned audiences in podcasting, because fame converts the first purchase and taste and price convert the second.  Ask for repeat purchase rate before you sign any creator-equity deal and walk if they will only show you launch week.",
    "Roblox banned reward-driven scrolling feeds in its Kids and Select tiers this morning, effective immediately, where a feed autoplays and pays users to keep watching.  Audit any Roblox build you run for under-13s against those three conditions this week and strip out watch-to-earn mechanics before a compliance review does.",
]
