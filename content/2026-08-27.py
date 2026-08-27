# -*- coding: utf-8 -*-
"""Content for THE FEED — issue data only.  The render spec lives in build_feed.py."""

ISSUE = {
    "date_iso": "2026-08-27",
    "kicker": "Crux Media // Thursday 27 August 2026",
    "tagline": "What brands did on YouTube yesterday, and whether it worked.",
    "pace": "STEADY",
    "next_drop": "Next drop: Friday, 06:30 MT",
}

LEAD = {
    "headline": "META JUST PAID BILLIONS TO CAP HOW LONG TEENS CAN WATCH, AND WANTS YOUTUBE AND TIKTOK TO DO THE SAME",
    "deck": "Meta settled the big state lawsuit over teen harm yesterday and agreed to put hard limits on how long under-18s can use its apps.  Then it took out full-page newspaper ads daring YouTube and TikTok to accept the same limits.  If they do, the largest teen video audiences you buy get a time cap and an overnight blackout.",
    "stamps": [
        ("TECHCRUNCH · 26 AUG", "https://techcrunch.com/2026/08/26/meta-settles-for-18-billion-in-lawsuit-brought-by-29-states-over-social-media-harms-to-children/"),
        ("NPR · 27 AUG", "https://www.npr.org/2026/08/27/nx-s1-5945278/meta-settlement-child-safety-big-tech"),
        ("AXIOS · 26 AUG", "https://www.axios.com/2026/08/26/meta-lawsuit-settlement-states-facebook"),
        ("FORTUNE · 26 AUG", "https://fortune.com/2026/08/26/meta-contingency-settlement-18-billion-tiktok-youtube/"),
    ],
    "body": [
        "Here is what happened, plainly.  Yesterday Meta settled a lawsuit brought by a coalition of state attorneys general who argued Facebook and Instagram were built to hook children.  The deal was filed before Judge Yvonne Gonzalez Rogers in the federal court in Oakland, it runs over ten years, and Meta will take a <mark>$10 billion charge this quarter</mark> to pay for it.  The exact headline price depends on who you read: the wire services put it around <mark>$16.7 billion</mark>, while TechCrunch, the Wall Street Journal and Fortune put it at <mark>$18 billion</mark>.  Meta shares rose about 4% before the market opened.",
        "The part that touches your job is the product changes Meta agreed to.  For users under 18, a combined cap of <mark>two hours a day</mark> across Facebook and Instagram, a lockout from midnight to 6am, muted notifications during school hours, like counts hidden by default, and cosmetic-surgery filters restricted.  Children 12 and under are to be blocked from accounts entirely.  An outside auditor checks compliance for five years and the restrictions run for up to ten.  Read that as one sentence: the biggest social platform just agreed to ration how much time teenagers spend inside it.",
        "Then Meta did something unusual.  It took out full-page ads in the Washington Post, the Los Angeles Times and the New York Times under the headline \"An Open Letter to TikTok and YouTube to Join Us in Supporting Teens.\"  Chief legal officer C.J. Mahoney called for an industry-wide standard and asked the other platforms to adopt the same framework right away — a <mark>one-hour daily cap</mark> and an overnight lockout.  And Meta backed the ask with money: it structured roughly <mark>$5.3 billion of the deal, about 30% of it</mark>, around whether TikTok and YouTube fall in line.",
        "Be honest about the one thing the reporting does not agree on, because it matters.  Outlets describe that $5.3 billion three different ways — Meta holding back its own money until rivals match, the rivals paying in themselves, or the teen limits simply getting stricter and lasting longer if everyone signs up.  So do not quote the mechanics as settled.  What is not in dispute is the intent.  Meta wants every big platform bound to the same teen curfew, and it is willing to spend billions to drag them there.",
        "As of this morning, <mark>TikTok, YouTube and Snap have all stayed silent</mark>.  None of them has said yes and none has said no.  Two of them already have their own reasons to move slowly: TikTok and Snap quietly settled the same underlying case back in January.  And the legal pressure is not letting up — Pennsylvania's attorney general filed a fresh addictive-design suit against Snapchat yesterday, a near-copy of the one it aimed at TikTok two weeks ago.  The direction of travel is one way.",
        "So here is the stake for anyone who buys teen reach.  If YouTube and TikTok match Meta, then the three platforms that carry almost all of your under-18 video audience get a one-hour daily ceiling and go dark overnight.  The audience does not vanish, but the hours you can reach it shrink and the times you can reach it move.  The plan you signed off six months ago assumed that inventory was effectively uncapped.  Very soon it may not be, and the deal still needs the judge's final sign-off before any of it is locked in.",
    ],
    "numbers": [
        ("$5.3B", "structured around whether TikTok and YouTube match the teen limits"),
        ("2 hrs", "the daily cap Meta accepted for its under-18 users"),
        ("$10B", "the charge Meta takes this quarter to pay for the deal"),
    ],
    "flagnote": "Settlement totals vary by outlet: wire services (Reuters, AP) report roughly $16.7 to $16.8 billion; TechCrunch, WSJ, CNN and Fortune report $18 billion; the gap is whether contingent amounts are counted.  The exact mechanism of the $5.3 billion contingency is reported three different ways across TechCrunch, Fortune, WSJ and Platformer, so it is described here as intent rather than settled mechanics.  The deal still requires the judge's final approval.",
    "so_what": "A settlement is normally a story for the legal team, not the media team.  This one is different because it changes the product, and the product is your inventory.  A time cap and an overnight lockout on under-18s is a direct cut to how many hours of teen attention exist to buy, and Meta is trying to make that cut the industry standard rather than its own handicap.",
    "do_this": "Before your next teen-facing plan, model the reach twice: once as it is today, and once assuming a one-hour daily cap and a midnight-to-morning blackout on Meta, YouTube and TikTok.  Bring both numbers to the meeting so nobody is planning against an audience that may be about to get smaller.",
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
                "title": "Rhode sold $27 million in a single day, and the number that explains it is the repeat rate",
                "hook": "One creator-founded brand did more skincare revenue in one day on its own site than 98% of tracked brands do in a year.  Here is the mechanism, and it is repeatable.",
                "open": True,
                "stamps": [
                    ("E.L.F. BEAUTY Q1 CALL · 5 AUG", "https://www.marketbeat.com/earnings/reports/2026-8-5-elf-beauty-inc-stock/"),
                ],
                "body": [
                    "On e.l.f. Beauty's earnings call, chairman and chief executive Tarang Amin gave the cleanest creator-commerce number of the month.  Rhode, the brand Hailey Bieber founded and e.l.f. bought this year, ran a summer launch it calls Summer of Rhode.  Amin's words: <mark>\"Rhode's latest summer product launch drove $27 million of DTC sales in a single day.  Yes, $27 million of sales on rhodeskin.com in a single day.\"</mark>  DTC means direct to consumer — the brand's own website, no retailer in the middle.",
                    "Then he put it in scale.  <mark>\"To put that in perspective, we often talk about Nielsen tracking 1,800 cosmetics and skincare brands.  Rhode did in one day more than what 98% of those brands do in an entire year.\"</mark>  That is the headline, but it is not the number that should change how you plan.",
                    "This is the one.  Rhode acquired <mark>90,000 new customers that day</mark>, and <mark>over 70% of the day's sales came from existing customers</mark>.  Both things at once.  A launch big enough to pull in ninety thousand first-timers, on the back of a base loyal enough to still make up most of the revenue.  That is not a viral spike.  That is a brand with a standing audience it can call on demand, topped up by newcomers the moment pulls in.",
                    "The mechanism is the founder's audience acting as the distribution.  A creator-founded brand does not rent attention for a launch, it already owns it, so it can compress a year's worth of demand into one announced day.  The drop is the event.  Scarcity and a fixed date do the rest — everyone shows up at once because they were told exactly when to.  Rhode's total contribution to the quarter was around <mark>$160 million</mark>, so the single day is a spike on top of a real business, not the whole business.",
                    "The reason this is a W and not just a big number is that repeat rate.  A one-day sales record built on strangers is a sugar high.  A one-day record where seven of every ten dollars come from people who already bought before is a machine you can run again next quarter.  That is the difference between a lucky launch and a launch calendar.",
                ],
                "so_what": "The lesson is not \"get a famous founder.\"  It is that a concentrated, dated drop beats always-on selling when you have an audience that already trusts you, because it stacks all the demand into one measurable moment instead of smearing it across a quarter.  And the number that tells you whether it worked is the share of sales from returning customers, not the total.  A big day from new buyers only is a warning, not a win.",
                "do_this": "If you run or advise a brand with a real owned audience, plan one concentrated launch day this quarter with a fixed date and limited stock, and judge it on two numbers: new customers acquired and the share of the day's revenue that came from existing ones.",
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
                "title": "Wrong metric: a brand reported 615 million impressions for its big creator launch and not one sales number",
                "hook": "The launch reportedly did well.  So why did the company only tell investors the number that means the least?  Because it is the number everyone accepts.",
                "open": True,
                "stamps": [
                    ("BATH & BODY WORKS Q2 CALL · 26 AUG", "https://www.marketbeat.com/earnings/reports/2026-8-26-bath-body-works-inc-stock/"),
                ],
                "body": [
                    "On Bath & Body Works' earnings call yesterday, chief executive Daniel Heaf described the brand's first celebrity-scale creator launch — a line called Fruit Fusion, with Hilary Duff as ambassador and creative partner.  His words: <mark>\"The campaign generated approximately 615 million impressions and contributed to over 50,000 new social followers, bringing Bath & Body Works into the cultural conversation with new audiences.\"</mark>",
                    "Now notice what is not there.  An impression is a video appearing on a screen.  A follower is someone tapping a button.  Neither is a sale, a customer, or a dollar.  Heaf said elsewhere on the call that the launch <mark>\"exceeded our sales expectations\"</mark> and carried a higher price per item than the core range, with some products selling out — but he attached <mark>no sales figure, no unit figure and no revenue figure</mark> to the campaign itself.  The only hard numbers he gave were the two that measure reach, not results.",
                    "Hold this next to the item above it in this issue.  Rhode told you it did $27 million in a day and that 70% came from repeat buyers.  Bath & Body Works, in the very same week, on the very same kind of launch, told you about impressions and followers.  One brand reported the outcome.  The other reported the audience.  The launch may well have worked — that is not the failure.",
                    "The failure mode is the metric, and it is contagious.  When a public company stands up and reports 615 million impressions for a creator campaign, it tells every marketer watching that impressions are the acceptable currency for this kind of work.  <mark>Impressions are the number you show when you would rather not show the number that matters.</mark>  They are big, they are flattering, and they cannot be checked against a cash register.  The more that becomes the norm, the harder it gets for the person in your building who wants to buy on outcomes to win the argument.",
                ],
                "flagnote": "Bath & Body Works stated the Fruit Fusion launch exceeded internal sales expectations and achieved a higher average price per item than its core range; it simply did not attach a specific sales, unit or revenue figure to the campaign.  This item is about the choice of what to report, not a claim that the launch failed.",
                "so_what": "Reach numbers and outcome numbers answer different questions, and the gap between them is where budgets get wasted.  Impressions tell you the video was served.  They tell you nothing about whether anyone bought, and a brand that only reports reach is either not measuring outcomes or not willing to show them.  Either way, do not let a nine-figure impression count stand in for proof that a campaign worked.",
                "do_this": "For your next creator campaign, decide the one outcome number you will report before it launches — new customers, repeat rate, or revenue — and put it at the top of the recap, with impressions underneath as context rather than the headline.",
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
                "title": "The BBC is now paying £50,000 for a YouTube-first documentary, and it does not want your TV repurposed",
                "hook": "A national broadcaster just became a direct buyer of creator production, with a rate card and a rule about what it will not commission.",
                "stamps": [
                    ("BBC COMMISSIONING", "https://www.bbc.co.uk/commissioning/youtube-commissioning/"),
                    ("PPC LAND · 25 AUG", "https://ppc.land/bbc-offers-50-000-per-youtube-documentary-for-16-24-year-olds/"),
                ],
                "body": [
                    "The BBC's own commissioning page, live this morning, sets out a strand called deepwatch: <mark>\"the BBC's YouTube-first documentary destination for 16-24 year-olds.\"</mark>  The tariff is stated plainly: <mark>\"We expect films to be at least 25 minutes in length, with an indicative tariff of £50,000 per documentary for production and delivery.\"</mark>  Ideas go in through the BBC's commissioning platform, to named editors including Adam MacDonald, Editor of BBC Factual YouTube.",
                    "The rule underneath it is the interesting part.  The BBC writes: <mark>\"We're less interested in television ideas repackaged for digital, companion content or promotional extensions of existing programmes.\"</mark>  In other words, a broadcaster is now telling producers that YouTube-native beats broadcast-warmed-over, and it is putting a fixed price on the native version.",
                ],
                "flagnote": "A widely cited comparison that YouTube reached 51.9 million UK viewers in December 2025 against the BBC's 50.8 million, attributed to BARB, appears in ppc.land's report and was not independently corroborated in second sourcing; treat it as single-sourced.",
                "so_what": "For a decade the money flowed one way: creators hiring TV people to look professional.  A broadcaster setting a public rate for YouTube-first films is the flow reversing, and it puts a new, well-funded buyer into the same production market your creator partners work in.  That competes for the same makers and it sets a reference price other commissioners will quote.",
                "do_this": "If you commission short documentary or factual video, benchmark your own rate against the BBC's £50,000 for 25-plus minutes before your next negotiation, and use its \"not repackaged TV\" line as the brief for anyone pitching you digital-first work.",
            },
            {
                "title": "Flipboard bought a two-person startup that pays people to build feeds, for the model rather than the size",
                "hook": "Graze splits ad money 70/30 in the feed-builder's favour.  Flipboard bought it to prove creators can be paid for curation, not just creation.",
                "stamps": [
                    ("TECHCRUNCH · 26 AUG", "https://techcrunch.com/2026/08/26/flipboard-acquires-graze-the-feed-builder-working-to-monetize-the-open-social-web/"),
                ],
                "body": [
                    "Flipboard acquired Graze, a startup that lets people build and run custom feeds on Bluesky and pays them for it.  The mechanism is a <mark>70/30 ad revenue split with the majority going to the feed's builder</mark>.  Graze is tiny — <mark>two staff, $1 million raised</mark>, terms undisclosed — but it has moved <mark>over 41 billion posts to some 12 million people</mark> across <mark>more than 7,000 feeds</mark>, with around <mark>60% of its traffic monetized</mark>, in 21 months.",
                    "Flipboard chief executive Mike McCue framed the point: <mark>\"The ad revenue is being shared with the feed builder.\"</mark>  The bet is that the next paid creator job is not making the video, it is assembling and curating the stream other people watch — and that whoever builds the audience should get most of the money.",
                ],
                "so_what": "This is a small deal that names a big idea: curation as a paid creator role, on open platforms nobody has locked down yet.  If it works, brands get a new kind of partner — the person who owns a feed rather than a channel — and a new, cheaper surface to reach a built-in audience before everyone else notices it exists.",
                "do_this": "Spend twenty minutes this week looking at who runs the biggest custom feeds in your category on Bluesky, and treat feed-builders as a partner type worth testing before the rates on them harden.",
            },
            {
                "title": "YouTube stood up in front of British TV and argued against being forced to promote the BBC",
                "hook": "The UK wants to guarantee broadcasters top billing on YouTube.  YouTube says that means burying the creators who actually live there.",
                "stamps": [
                    ("DEADLINE · 27 AUG", "https://deadline.com/2026/08/youtube-argues-against-prominence-1237059305/"),
                ],
                "body": [
                    "At the Edinburgh TV Festival, YouTube's most senior European executive Pedro Pina used the industry's marquee lecture to fight a proposed UK rule that would force platforms to give public broadcasters prominence — guaranteed visibility — in their apps.  His argument: <mark>\"A lot of independent creators, producers and publishers, who have spent a lot making sure their content is discoverable and make a living from it, will be pushed down.  We are endangering a creator economy that has been burgeoning in this country.\"</mark>",
                    "The UK government has this among the options in a coming policy paper, so it is a live fight rather than a done deal.  Strip away the national politics and the mechanism is simple: prominence is a fixed shelf, and every slot you promise a broadcaster is a slot taken from whoever the algorithm would have ranked there — often a smaller creator or a brand channel.",
                ],
                "so_what": "If a government can mandate who gets ranked highly on YouTube, then ranking stops being purely a performance question and becomes partly a policy question, market by market.  For anyone buying UK creator inventory, that is a new variable: the visibility you are paying a creator for could be reshuffled by law rather than by the algorithm.",
                "do_this": "If you run brand or creator video in the UK, add the prominence proposal to your watch list and ask your YouTube rep directly how any mandated broadcaster placement would affect ranking for the channels you buy.",
            },
        ],
    },
    {
        "id": "onstream",
        "name": "ON STREAM",
        "page": "pg. 05",
        "note": "the live numbers, and what they actually measure",
        "tint": None,
        "items": [
            {
                "title": "Gamescom's opening show drew 1.74 million people at once, and the peak fell even as the hours watched jumped",
                "hook": "More channels carried it, more hours got watched, and the actual live crowd got smaller.  This is the exact trap in livestream numbers, live on stage.",
                "open": True,
                "stamps": [
                    ("STREAMS CHARTS · 26 AUG", "https://streamscharts.com/news/gamescom-opening-night-live-2026-viewership"),
                    ("ESPORTS CHARTS · 27 AUG", "https://escharts.com/news/overwatch-world-cup-2026-group-stage"),
                    ("ESPORTS CHARTS · 26 AUG", "https://escharts.com/news/ewc-2026-tournament-viewership"),
                ],
                "body": [
                    "Gamescom's Opening Night Live ran in Cologne on Monday.  Streams Charts put the <mark>peak at 1.74 million concurrent viewers</mark> across official channels and community co-streams, with <mark>hours watched over 5.8 million, up 27% on last year</mark>.  Sounds like a straight win.  It is not, and the reason is one line down.",
                    "The number of channels broadcasting the show went from <mark>about 1,150 last year to 7,800 this year</mark> — nearly seven times as many.  And against all that, the <mark>peak concurrent audience actually fell 13.3%</mark>.  Read those together.  Hours watched rose because far more channels carried the stream for longer, while the real measure of the live crowd — how many people were watching at the same moment — went down.  Average concurrents and airtime were not published, which are exactly the figures that would settle it.",
                    "For scale on the peak: 1.74 million people watching at once is roughly <mark>nineteen sold-out Wembley Stadiums</mark>, all full, all watching one show.  That is a genuinely enormous live audience.  It is just not a bigger one than last year, whatever the hours-watched line implies.",
                    "The same trap showed up cleanly at the Overwatch World Cup, whose group stage this year switched matches from best-of-three to best-of-five.  Esports Charts reported <mark>hours watched up 90%</mark> — and said the jump came largely from the longer format, not a bigger audience.  The honest figures sit right beside it: <mark>peak up 5.8% to 159,300</mark>, average viewers up 14.6%.  Longer matches, more hours, roughly the same crowd watching a little more attentively.",
                    "One more for perspective on how top-heavy this all is.  Across the seven-week Esports World Cup in Paris, Esports Charts counted <mark>only 4 of 25 tournaments that topped a million peak viewers</mark>.  Mobile game Mobile Legends led at 2.89 million, down from about 3 million last year.  PUBG Mobile set a record at 1.79 million.  And Counter-Strike's hours watched rose 93.7% — on a field that doubled from 16 teams to 32 and airtime that more than doubled from 41 hours to 90.5.  Same pattern, every time: add teams or add match length and the hours climb on their own.",
                ],
                "numbers": [
                    ("1.74M", "peak concurrent viewers at Gamescom's opening show"),
                    ("7,800", "channels that carried it, up from about 1,150 last year"),
                    ("-13.3%", "the peak audience's actual change year on year"),
                ],
                "flagnote": "Gamescom's peak includes community co-streams; average concurrent viewers and airtime were not published by Streams Charts, and no official organiser figure for 2026 had been released as of this morning.  Overwatch World Cup average-viewer and hours-watched figures were published only as percentage changes, not absolute numbers.",
                "so_what": "Hours watched is the number event organisers love because it rises whenever the event gets bigger, longer, or carried in more places — none of which means more people showed up.  Peak concurrent viewers is the crowd.  Average concurrent viewers is the crowd that stayed.  When an organiser hands you a giant hours-watched figure and leaves out the peak and the channel count, that omission is the story.",
                "do_this": "Before you price any livestream sponsorship, ask the seller for peak and average concurrent viewers plus the channel count and airtime for this year and last, and if they will only give you hours watched, treat the gap as a red flag and price down.",
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
                "title": "Wemmbu",
                "hook": "4.5 million subscribers, and his last big video pulled 8.2 million views — nearly twice his whole subscriber base.  He builds Minecraft civilizations for a thousand players, then blows them up.",
                "open": True,
                "stamps": [
                    ("YOUTUBE CHANNEL", "https://www.youtube.com/@wemmbumc"),
                ],
                "body": [
                    "Wemmbu makes long, heavily scripted Minecraft films — the format is a giant social experiment.  He and three credited collaborators drop a thousand players into a custom modded world, let a civilization form, then infiltrate it, betray it or destroy it across a running storyline with recurring characters and arcs.  Episodes run <mark>90 minutes to two hours</mark>, in English, made by a small team with composed music and custom mechanics, not one person with a phone.  He flags in his own descriptions that it is staged for storytelling, which keeps the trust intact.",
                    "The momentum is in the trajectory.  The channel sat around <mark>900,000 subscribers in June 2025</mark> and reads <mark>4.47 million this morning</mark> against about <mark>659 million lifetime views across 90 videos</mark>, having relaunched in October 2023.  That is roughly a million and a half subscribers added in the last six months, on a channel that posts only about <mark>once every two weeks</mark> — the opposite of the upload-flooding you see from content farms.",
                    "What changed is that one sub-format broke out.  His \"1,000 players simulate\" episodes have been climbing release over release through this year, and the audience now outruns the subscriber count by a wide margin — the standout video did 8.2 million views against a 4.5 million base, and rival creators are posting their own reaction videos to his uploads, which is the clearest sign a format has escaped its own channel.",
                    "The honest caveats.  The universe is shared among four creators, so some of this momentum belongs to the ensemble, not to him alone — if the group splits or the current story arc ends flat, growth can stall.  The audience skews young, male and gaming-forum adjacent, which rules out whole categories.  And two-hour episodes mean a single ad has to be placed with care or it gets skipped.  But the flip side is scarcity: at one upload a fortnight, there is very little sponsor inventory here, which makes each slot premium rather than diluted.",
                ],
                "watch": {
                    "label": "TOP VIDEO, LAST 3 MONTHS",
                    "title": "1000 Players Simulate THE PURGE in Minecraft",
                    "url": "https://www.youtube.com/watch?v=4v_jk0w7wR0",
                    "meta": "8,243,497 views · published 6 June 2026 · 1:57:41",
                    "note": "A thousand players, one modded world, and a night where the rules come off — a two-hour build-and-destroy episode that pulled nearly twice his subscriber count in views.",
                },
                "so_what": "This is a scarce, high-completion channel in a category that reliably sells hardware and games.  His audience over-indexes for exactly the things a gaming-peripherals or PC-software brand wants to reach, and because he posts so rarely, a single integration is not fighting ten others in the same week.  The buy is attention and completion, not raw frequency.",
                "do_this": "If you sell gaming headsets, controllers, capture cards, a VPN or a strategy game, get a quote for one 60-to-90-second scripted mid-roll inside a flagship Wemmbu episode this quarter, before his rate card catches up with reach that already runs ahead of his subscriber count.",
            },
        ],
    },
    {
        "id": "money",
        "name": "THE MONEY",
        "page": "pg. 07",
        "note": "where the spend is going, and what the market data actually says",
        "tint": None,
        "items": [
            {
                "title": "Creator buying is being handed to the machines, and the people who sell trust are nervous",
                "hook": "One retail platform now runs creator campaigns off 100 billion shopping signals.  One agency boss says that automates away the exact thing brands are paying for.",
                "open": True,
                "stamps": [
                    ("DIGIDAY · 27 AUG", "https://digiday.com/marketing/the-case-for-and-against-the-programmatic-ification-of-the-creator-economy/"),
                ],
                "body": [
                    "Digiday reported this morning on creator budgets shifting from relationship-based buying to automated, data-driven matching.  The shopping platform LTK rolled out an artificial-intelligence campaign tool it says is built on <mark>more than 100 billion commerce signals</mark> gathered over 15 years.  Unilever, on the other end of the scale, now says it manages an <mark>army of 300,000 creators</mark>.  The pitch is speed and measurement: pick and price creators by data, at a scale no human team could handle by hand.",
                    "The pushback names the risk exactly.  Gabe Gordon, chief executive of Reach Agency: <mark>\"Creators are not interchangeable media inventory, and the industry risks automating away the very thing brands are buying: human trust and creative judgment.\"</mark>  Natalie Silverstein of Collectively put the tension more gently — creator buying is <mark>\"some combination of art and science... but the art is what makes it work.\"</mark>",
                ],
                "so_what": "Automating creator selection makes it faster and cheaper to buy at scale, and it quietly changes what you are buying.  The reason a creator outperforms a normal ad is that their audience trusts them, and trust is the one input a matching model handles worst.  Buy creators like raw audience and you get the price of a creator with the results of a banner.",
                "do_this": "If your agency or platform is moving creator buying onto an automated system, keep a human veto on the final shortlist and test the two approaches head to head on one campaign — machine-picked against hand-picked — before you let the system run unsupervised.",
            },
            {
                "title": "Twitch just made the gifted subscription the unit brands buy, and the streamer keeps the full cut",
                "hook": "State Farm is handing out 100,000 subscriptions to kick off a month of discounts.  The brand pays, the viewer gets in cheap, and the creator loses nothing.",
                "stamps": [
                    ("TWITCH BLOG · 18 AUG", "https://blog.twitch.tv/en/2026/08/18/subtember-2026/"),
                ],
                "body": [
                    "Twitch's month-long SUBtember discount runs <mark>28 August to 1 October</mark>: 25% off one and three-month subscriptions, 30% off six-month ones.  The key line is who eats the discount — <mark>\"Twitch covers the difference so streamers will still get the same payout as a full-priced sub.\"</mark>  The viewer pays less, the creator is paid in full, and the platform absorbs the gap.",
                    "Brands are bolted straight onto it.  State Farm kicks the month off by <mark>gifting nearly 100,000 subscriptions</mark> across channels in its Gamerhood series, and a Minecraft game launch sponsors a bonus-sub week to close it out.  The sponsorship unit here is not a banner or a pre-roll — it is the subscription itself, bought in bulk and handed to viewers as the brand's gift.",
                ],
                "so_what": "A gifted subscription is a cleaner brand buy than an ad read, because it does something the viewer actually wants and it credits the brand for the favour every time that sub shows up in chat.  It also aligns everyone: the fan gets access, the creator gets paid in full, and the brand gets goodwill instead of an interruption.  That is a very different trade from renting thirty seconds of a stream.",
                "do_this": "If you sponsor streamers, price a block of gifted subscriptions against your usual mid-stream ad spend for the same creators, and test which one moves sentiment and watch time more over a month.",
            },
        ],
    },
    {
        "id": "format",
        "name": "FORMAT LAB",
        "page": "pg. 08",
        "note": "one production or format idea, taken apart",
        "tint": None,
        "items": [
            {
                "title": "Chris Hansen turned a movie about himself into an ad slot for his own network",
                "hook": "A24 made a film starring Robert Pattinson as Chris Hansen.  Hansen bought the ad space in front of it and pointed the audience at his own streaming service.",
                "open": True,
                "stamps": [
                    ("THEWRAP · 26 AUG", "https://www.thewrap.com/creative-content/movies/chris-hansen-primetime-trublu-theatrical-ad-purchase/"),
                    ("TMZ · 26 AUG", "https://www.tmz.com/2026/08/26/chris-hansen-buys-ad-space-before-primetime-showings/"),
                ],
                "body": [
                    "A24's film Primetime, out in select theatres 25 September, stars Robert Pattinson as the TV host Chris Hansen.  Hansen did not authorise it — he says he walked away rather than sign A24's non-disclosure agreement, and A24 says it was a standard spoiler NDA he chose not to negotiate.  So Hansen did something else.  He <mark>bought the pre-show cinema advertising that runs in front of Primetime</mark>, set to play ahead of the film for at least its <mark>first four weeks</mark>, promoting his own true-crime streaming network, TruBlu.",
                    "Look at the structure, because the money is almost beside the point — no figure was disclosed and it does not need to be.  A24 spent a studio budget to make a film about Hansen and to fill theatres with people interested in Hansen.  Hansen bought the ninety seconds right before that film and used them to send that exact audience to the real thing.  The studio built the audience.  He rented the doorway.",
                    "The frame that makes it hold together is that the movie and the ad are about the same person.  There is no mismatch to paper over — anyone in that seat is already interested in the subject, so an ad pointing them to the subject's own network is the most relevant thing that could play.  He even considered ad copy calling the film \"a Hollywood fantasy version\" and dropped it, which is the right call: the move works better as a straight invitation than as a swipe.",
                ],
                "flagnote": "The NDA backstory is reported by TheWrap and TMZ, with A24's position that the agreement was a standard anti-spoiler NDA; no dollar figure for the ad buy has been disclosed.",
                "so_what": "When someone else builds an audience around your subject, the cheapest way to reach that audience is to stand in the doorway they already built rather than build your own.  The scarce asset is not attention in general, it is attention that has already been gathered and pointed at your exact topic.  Buying the slot in front of it is a fraction of the cost of assembling it yourself.",
                "do_this": "When a film, show, event or piece of press is about to gather your exact audience — even one you did not create and do not control — price the advertising, sponsorship or content slot that sits right next to it before you spend a cent building reach from scratch.",
            },
        ],
    },
]

FORECAST = [
    {
        "confidence": "LIKELY",
        "window": "by 31 December 2026",
        "headline": "Neither YouTube nor TikTok agrees to Meta's teen curfew, and the $5.3 billion lever fizzles",
        "body": "Meta wants rivals to accept a one-hour teen cap and an overnight lockout, and structured billions around it.  But matching would mean voluntarily capping their own most-watched young audiences, with no lawsuit forcing them to — and TikTok already settled the underlying case on its own terms in January.  Silence from all three this week is the tell.  Expect the pressure campaign to make headlines and the actual matching to not happen, leaving Meta with tighter teen limits than its competitors rather than an industry standard.",
        "do": "Plan teen reach on the assumption that Meta tightens and the others do not, which means Meta's under-18 inventory gets scarcer while YouTube and TikTok stay open, at least for now.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "next 6 months",
        "headline": "A state attorney general aims the same addictive-design case squarely at YouTube",
        "body": "Meta has settled, TikTok and Snap have settled, and Pennsylvania just filed fresh against Snap.  YouTube is the largest teen video platform not yet at the centre of one of these suits, which makes it the obvious next target rather than a safe bystander.  When it happens, expect the same menu of demands — time caps, overnight lockouts, age checks — pointed at the platform where most of your teen video actually runs.",
        "do": "Assume teen product restrictions are coming to YouTube too, and start the conversation now about what your teen plans look like under a daily cap there.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "next 9 months",
        "headline": "Broadcaster money becomes a real bidder for the creator production market",
        "body": "The BBC setting a public £50,000 rate for YouTube-first films is one signal, and it will not be the last — legacy broadcasters across markets are watching their young audiences move and will follow with their own commissioning budgets.  That puts well-funded, standards-heavy buyers into the same pool of makers your creator partners use, which pushes up both rates and lead times.  The talent gets more expensive and slower to book as the bidders multiply.",
        "do": "Lock in your key creator production partners on longer terms now, before broadcaster commissioning pulls their rates and their calendars away from you.",
    },
    {
        "confidence": "LIKELY",
        "window": "next 3 months",
        "headline": "The concentrated founder drop becomes the template other creator brands copy",
        "body": "Rhode's $27 million single day, built mostly on repeat buyers, is the kind of number that gets screenshotted into every creator-brand board deck.  The move is simple and repeatable for anyone with an owned audience: stop selling always-on, pick a date, limit the stock, and stack the demand.  Expect a run of creator-founded brands to announce dated drops this quarter and to start reporting single-day revenue as their headline metric.",
        "do": "If you run or advise a creator-founded brand, design one concentrated drop this quarter and instrument it to capture new-customer count and repeat share, so you have the real numbers when the copycats arrive.",
    },
    {
        "confidence": "LONG SHOT",
        "window": "next 12 months",
        "headline": "A major brand reports a creator campaign with repeat purchase, not impressions, as the headline",
        "body": "Right now the norm is what Bath & Body Works did this week: report 615 million impressions and leave the sales line blank.  It would take one big advertiser deciding that outcome numbers are a competitive brag rather than a risk to break the pattern — leading a campaign recap with new customers acquired and repeat rate, the way rhode's owner did on an earnings call.  The first one to do it publicly resets what \"good\" looks like for everyone else.",
        "do": "Get ahead of it by making an outcome number the headline of your own next recap, so you are setting the standard rather than scrambling to match it.",
    },
]

TLDR = [
    "Meta settled the state teen-harm case for somewhere between $16.7 and $18 billion, agreed to a two-hour daily cap and an overnight lockout for under-18s, and is spending roughly $5.3 billion trying to force YouTube and TikTok to match — which would cap and black out the teen video audiences you buy.  Model your next teen plan twice, once as it is today and once under a one-hour cap and an overnight blackout across all three platforms.",
    "Rhode did $27 million in DTC sales in a single day with 90,000 new customers and over 70% of revenue from repeat buyers, proving a concentrated founder drop beats always-on selling when you own the audience.  Plan one dated, limited-stock launch this quarter and judge it on new customers and repeat share, not the total.",
    "Bath & Body Works reported 615 million impressions and 50,000 followers for its Hilary Duff creator launch and gave investors no sales number at all, which trains the whole market to buy on reach instead of results.  Decide the one outcome number you will report before your next campaign launches, and put it above impressions in the recap.",
    "Gamescom's opening show hit a 1.74 million peak but its live crowd actually fell 13.3% year on year even as hours watched rose 27%, because the channels carrying it jumped from about 1,150 to 7,800.  Demand peak and average concurrent viewers plus channel count from any livestream seller, and treat an hours-watched-only pitch as a reason to price down.",
    "The BBC set a public £50,000 rate for 25-minute YouTube-first documentaries and said it does not want repackaged TV, making a national broadcaster a direct bidder for creator production.  Benchmark your own digital-first rates against it and expect talent to get more expensive as broadcaster money enters the market.",
    "Twitch's SUBtember makes the gifted subscription the brand-buying unit — State Farm is gifting nearly 100,000 subs — with Twitch eating the discount so streamers keep their full payout.  Price a block of gifted subs against your usual stream ad spend and test which one moves watch time and sentiment more.",
    "Creator buying is shifting to automated systems built on billions of shopping signals, and agency leaders warn it automates away the trust brands are actually paying creators for.  Keep a human veto on final creator selection and run machine-picked against hand-picked on one campaign before letting the system run alone.",
]
