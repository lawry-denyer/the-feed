# -*- coding: utf-8 -*-
"""Content for THE FEED — issue data only.  The render spec lives in build_feed.py."""

ISSUE = {
    "date_iso": "2026-08-17",
    "kicker": "Crux Media // Monday 17 August 2026",
    "tagline": "What brands did on YouTube yesterday, and whether it worked.",
    "pace": "STEADY",
    "next_drop": "Next drop: Tuesday, 06:30 MT",
}

LEAD = {
    "headline": "YOUR VIEW COUNT IS ABOUT TO JUMP AND IT MEANS NOTHING",
    "deck": "YouTube announced this morning that from August 24, a view counts from the very first frame.  Every channel's numbers go up.  Nobody is watching more.",
    "stamps": [
        ("YOUTUBE SUPPORT", "https://support.google.com/youtube/thread/433409976?hl=en"),
        ("9TO5GOOGLE", "https://9to5google.com/2026/08/17/youtube-view-counts-change/"),
        ("ENGADGET", "https://www.engadget.com/2238611/youtube-public-view-counts-will-likely-get-higher-starting-next-week/"),
        ("DEXERTO", "https://www.dexerto.com/entertainment/youtube-is-making-a-major-change-to-how-long-form-video-views-are-counted-3399287/"),
    ],
    "body": [
        "Here is the change, in one line.  Right now a view on a long video means somebody watched a meaningful chunk of it.  <mark>From August 24, a view means the video started playing.</mark>  First frame.  That is the whole bar.",
        "It covers long-form video, podcasts and live streams.  Shorts already worked this way — YouTube switched them over in 2025 — so this is the rest of the platform catching up to the vertical feed.",
        "What this does to your numbers is obvious once you say it out loud.  Somebody who clicks, watches two seconds, decides it is not for them and bounces?  That is a view now.  Public counts across basically every channel are going to step up overnight, and not one extra human will have watched anything.",
        "Three things did not change, and they are the ones that matter.  Money is untouched — creators still get paid on Engaged Watch Hours and Engaged Shorts views, the old stricter measure, which YouTube is keeping and reporting separately.  Monetization thresholds are untouched.  And old videos are not being recounted, so your back catalogue keeps its real numbers while everything from the 24th onward runs on the new inflated ones.",
        "That last detail is the trap.  <mark>Your archive and your new uploads are about to be measured with two different rulers</mark>, and every year-on-year chart anyone builds in September is going to show a jump that is pure accounting.",
        "YouTube's own framing is worth reading closely.  It says the change helps creators show brand partners their \"true scale and value.\"  Translated: the number you put in a sponsorship deck gets bigger next Monday.  Whether it should is a different question.",
    ],
    "numbers": [
        ("AUG 24", "the day everyone's numbers jump"),
        ("FRAME 1", "where a view now starts counting"),
        ("$0", "extra revenue this actually creates"),
    ],
    "so_what": "Views were already a soft currency and they just got softer.  The mechanism is simple — YouTube moved the counter from \"watched a while\" to \"pressed play,\" so the number now measures exposure instead of attention.  Anything you price, benchmark or report against raw views breaks on August 24, and the only number still tied to real watching is the one labelled Engaged.",
    "do_this": "Rewrite every live creator contract to say Engaged Views before the 24th, and screenshot your current dashboards this week so you have a clean before-and-after.",
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
                "title": "Ads posted from the creator's own account beat ads that borrow their footage",
                "hook": "Same creator.  Same footage.  A 19% gap in whether anybody clicks.",
                "stamps": [
                    ("TUBEFILTER", "https://www.tubefilter.com/2026/08/13/agentio-study-meta-partnership-ads-creator-marketing/"),
                    ("NET INFLUENCER", "https://www.netinfluencer.com/meta-partnership-ads-outperform-licensed-ugc-across-130m-usd-in-ad-spend-report-finds/"),
                    ("PR NEWSWIRE", "https://www.prnewswire.com/news-releases/new-report-by-agentio-reveals-how-brands-can-build-an-infinite-creative-engine-with-creator-led-advertising-302849831.html"),
                ],
                "body": [
                    "Agentio ran the numbers on 65,000 Meta partnership ads — $130 million of spending, 137 brands.  Partnership ads run from the creator's own handle with the brand paying to push them.  The comparison group: the brand takes that same creator's video, recuts it, runs it from the brand account.",
                    "Same person.  Same face.  Same product.  <mark>The version with the creator's name on it got 19% more clicks, converted 10% better, and cost 5% less per customer.</mark>  It also cost 19% more to reach the same thousand people, so you are paying for the lift.",
                    "The reason is not complicated and it is worth saying plainly: the handle is the endorsement.  Take the creator's account off the post and you still have their face, but you no longer have them vouching for it.  Audiences clock that instantly.  They do not need to think about it.",
                ],
                "so_what": "Brands buy footage rights because it is cheaper and you get to control everything.  Turns out that control costs you a fifth of your clicks.  The trust lives in whose name is on the post — not in the pixels — which is exactly why a recut performs worse even when it is literally the same edit.",
                "do_this": "Put creator-handle posting rights in your next contract, and build the higher media cost into the plan on day one instead of arguing about it later.",
            },
            {
                "title": "Gamescom's audience grew because other people rebroadcast it",
                "hook": "The show did not get better.  Four hundred more channels carried it.",
                "stamps": [
                    ("STREAMS CHARTS", "https://streamscharts.com/news/gamescom-opening-night-2025-recap"),
                    ("GAMESPOT", "https://www.gamespot.com/articles/gamescom-opening-night-live-was-watched-by-way-more-people-than-last-year/1100-6534239/"),
                ],
                "body": [
                    "Gamescom Opening Night Live is two hours of trailers.  That should have a ceiling.  In 2025 it pulled more than 2 million people watching at once, 1.8 million average, 4.6 million hours watched, 72 million total views — up 60%, 67%, 79% and 80% on the year before.",
                    "The production barely changed.  <mark>Channels rebroadcasting it went from about 700 to more than 1,100</mark>, and the viewership climbed right alongside that count.",
                    "This is the cleanest proof going that for an event like this, letting other people carry your stream beats making your own stream better.  The official channel is not the destination anymore.  It is the seed.",
                ],
                "so_what": "How far a launch travels now depends on how many other channels are legally allowed to carry it live, not on what you spent producing it.  Most brand launch content is still built and licensed like the brand's own channel is where everybody shows up.  The growth is sitting in the permission, not the production budget.",
                "do_this": "Clear co-streaming rights on your next launch video so other channels can legally rebroadcast it live.",
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
                "title": "Brands kill their best creator ads early, then ride the survivors a month too long",
                "hook": "Wrong economics — at $100 of testing, nearly half your future winners still look like duds.",
                "stamps": [
                    ("TUBEFILTER", "https://www.tubefilter.com/2026/08/13/agentio-study-meta-partnership-ads-creator-marketing/"),
                    ("NET INFLUENCER", "https://www.netinfluencer.com/meta-partnership-ads-outperform-licensed-ugc-across-130m-usd-in-ad-spend-report-finds/"),
                ],
                "body": [
                    "Same $130 million study, two mistakes sitting on opposite ends of the same campaign.  At the $100 mark — roughly where every team makes the keep-or-kill call — <mark>45% of the ads that went on to win still looked like losers.</mark>  You have to get to about $1,000 before that misread drops to a quarter.",
                    "So the discipline everyone is proud of, cutting weak performers fast, is quietly binning close to half the stuff that would have paid.  At $100 you are not reading signal.  You are reading noise and calling it a decision.",
                    "The other end costs actual money.  A winning creator ad decays after about 36 days, and running it past that pushes your cost per customer up around 1.8 times.  Median campaign finds a winner roughly one time in five.  Which is why the recommendation lands at about 40 new spots a month.",
                    "Put it together: this is a production line, not a talent show.  Almost nobody runs it that way.",
                ],
                "so_what": "The two mistakes feed each other.  Killing early means fewer winners survive, which means you cling harder to the ones that did, which means you run them straight past the point where they still work.  A team doing both ends the campaign paying more per customer than they did at the start and genuinely cannot tell you why.",
                "do_this": "Set a hard $1,000 no-kill floor on every creator ad test, and diary a 36-day retirement date the day each winner goes live.",
            },
            {
                "title": "The market pays for subscriber counts while buyers swear they are buying engagement",
                "hook": "Wrong audience — 5,095 creators surveyed, and follower count still predicts income better than anything else.",
                "stamps": [
                    ("BUSINESSWIRE", "https://www.businesswire.com/news/home/20260811188612/en/CreatorIQ-Study-Reveals-a-Growing-Authenticity-Gap-Brands-Value-Engagement-but-the-Market-Still-Rewards-Reach"),
                    ("MARKETING BREW", "https://www.marketingbrew.com/stories/creator-income-follower-count-importance-creator-iq"),
                    ("THEWRAP", "https://www.thewrap.com/media-platforms/tv/creators-annual-salary-2026-study/"),
                    ("TUBEFILTER", "https://www.tubefilter.com/2026/08/16/creators-rely-on-brand-deals-but-worry-about-the-tension-between-sponsors-and-viewers-and-just-15-say-they-fully-trust-sponsored-content-from-other-creators/"),
                ],
                "body": [
                    "CreatorIQ surveyed 5,095 creators across 100 regions.  Buried under the friendlier stats: <mark>subscriber count is still the strongest predictor of what a creator earns</mark>, even though every buyer will tell you they select on engagement and fit.",
                    "The decks and the purchase orders are saying different things.  If you actually believe engagement drives results, then you are overpaying at the top and underpaying the mid-size creators who are doing the work.",
                    "The rest of the picture: 67% of creators make under $10,000 a year from content, just under 5% clear $100,000.  Only 15% fully trust sponsored content made by other creators — that is people inside the industry, not sceptical viewers.  And 42% feel a pull between what their audience wants and what brands ask for, climbing to 53% once you pass 500,000 followers.",
                    "That 53% is the one to sit with.  The bigger the creator, the more likely your brief is fighting the exact relationship you are paying to borrow.",
                ],
                "so_what": "There is a pricing gap sitting in the open between what the market rewards and what buyers claim to value.  Reach is easy to verify and easy to defend in a meeting, so reach is what gets paid for.  Engagement is harder to prove, so it is harder to charge for — which makes the mid-tier creator with a tight audience the most underpriced thing in this market right now.",
                "do_this": "Build your next campaign entirely from creators in the 50,000 to 250,000 range and run it head to head against your last big-name buy.",
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
                "title": "YouTube is doubling the bar to get monetized",
                "hook": "First change to the entry rules in eight years, and both routes just got twice as hard.",
                "stamps": [
                    ("YOUTUBE BLOG", "https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/"),
                    ("YOUTUBE HELP", "https://support.google.com/youtube/answer/12843009"),
                    ("BARRETT MEDIA", "https://barrettmedia.com/2026/08/14/youtube-monetization-rules-for-creators/"),
                    ("BUSINESS STANDARD", "https://www.business-standard.com/technology/tech-news/technology-tech-news-youtube-partner-program-monetisation-rules-2027-watch-hours-shorts-views-126081100708_1.html"),
                ],
                "body": [
                    "From February 1, 2027, a new creator needs 1,000 subscribers plus either 8,000 watch hours in a year or 20 million Shorts views in 90 days.  Both of those performance numbers are exactly double what they are today.  Subscriber count did not move.",
                    "Already in the program?  You are fine on entry.  But there is a second change that does reach you: <mark>if you take a share of Shorts revenue you now have to hold 10 million qualified Shorts views every rolling 90 days.</mark>  Drop below and the Shorts money switches off while everything else keeps running.",
                    "Look at the asymmetry.  8,000 watch hours is very doable with a small loyal audience.  20 million Shorts views in 90 days needs you to actually go viral, repeatedly.  YouTube has quietly made long video the easy door — a few years after spending enormous money pulling everyone toward the short vertical one.",
                    "Creator liaison Rene Ritchie tightened the definitions on the 14th: only public long videos, podcasts and archived livestreams count toward watch hours, and Shorts views have to be engaged ones.  How many seconds makes a view engaged?  Still unpublished.  That is the number everyone actually needs.",
                ],
                "flagnote": "The August 14 definitions come from a single write-up of Rene Ritchie's remarks, not from YouTube's own documentation.",
                "so_what": "YouTube is rationing who gets onto its payroll and steering the ones who make it toward long video.  Doubling the bar roughly halves how many new creators it has to start paying.  For anyone buying, the pool of freshly monetized small channels is about to thin out, and the survivors will be long-form.",
                "do_this": "Ask every creator you are about to sign whether they clear 10 million Shorts views a quarter — the ones who do not are staring at an income hole and will negotiate.",
            },
            {
                "title": "The film studios just cut a deal with ByteDance over AI video",
                "hook": "Six months ago it was a cease and desist.  Today it is a signed agreement.",
                "stamps": [
                    ("TIKTOK NEWSROOM", "https://newsroom.tiktok.com/mpa-and-bytedance-announce-global-agreement-to-protect-intellectual-property-on-ai-video-and-image-generation-models?lang=en"),
                    ("HOLLYWOOD REPORTER", "https://www.hollywoodreporter.com/business/digital/mpa-inks-ai-video-ip-protection-bytedance-1236675016/"),
                    ("DEADLINE", "https://deadline.com/2026/08/mpa-tiktok-bytedance-deepfakes-1237042847/"),
                    ("VARIETY", "https://variety.com/2026/biz/news/motion-picture-association-deal-bytedance-ip-ai-seedance-1236836240/"),
                ],
                "body": [
                    "Announced this morning.  The Motion Picture Association and ByteDance signed a global agreement putting copyright guardrails on the Seedance and Seedream generative models — across TikTok, the TikTok USDS joint venture, CapCut and Dreamina.",
                    "The backstory is the interesting part.  In February the MPA sent ByteDance a cease and desist over those exact models.  <mark>Six months later it is a cooperation framework instead of a lawsuit</mark> — the same road the music labels went down with AI audio.",
                    "Practical read for anyone editing: expect new blocks on prompting recognizable film and TV characters inside CapCut and Dreamina.  Those tools sit right where people actually make content, which is precisely why the studios cared enough to move.",
                ],
                "so_what": "Generative video lives inside the editing apps now, not in some separate research tool, so studio-owned characters were one prompt away from mass reproduction.  The studios picked negotiated limits over years of litigation.  If you build workflows on CapCut or Dreamina, the guardrails are arriving and it is better to find out now than mid-project.",
                "do_this": "Audit any CapCut or Dreamina step in your workflow this week and flag anything that leans on recognizable film or TV characters.",
            },
            {
                "title": "KSI is now the broadcaster for a football club he part-owns",
                "hook": "A top-20 YouTube channel just turned itself into a sports rights holder.",
                "stamps": [
                    ("TUBEFILTER", "https://www.tubefilter.com/2026/08/14/ksi-dazn-stream-dagenham-redbridge-soccer-match/"),
                    ("DAZN", "https://dazngroup.com/press-room/ksi-dazn-and-dagenham-redbridge-announce-landmark-broadcast-partnership-to-redefine-non-league-football-coverage/"),
                    ("DAGGERS", "https://daggers.co.uk/ksi-dazn-and-dagenham-redbridge-announce-landmark-broadcast-partnership-to-redefine-non-league-football-coverage/"),
                    ("YAHOO SPORTS", "https://sports.yahoo.com/articles/ksi-showcase-dagenham-redbridge-fixtures-155354179.html"),
                ],
                "body": [
                    "KSI, 18.9 million subscribers, is livestreaming Dagenham and Redbridge fixtures on his own channel this season alongside DAZN.  Sixth tier of English football.  He bought into the club in March.",
                    "<mark>The audience, the broadcast rights and the equity are all on the same side of the table now.</mark>  Normally that is three separate parties — a league sells rights to a broadcaster, broadcaster sells sponsorship to brands.  Here it is one guy holding all three.",
                    "Precedents: Wrexham, where Ryan Reynolds and Rob McElhenney turned a documentary into money that went back into the club.  And CazéTV in Brazil, a creator channel that held official World Cup rights this year and broke viewership records with them.",
                    "What nobody has said: how many matches, when the first one is, what any of it costs, or the size of his stake.",
                ],
                "flagnote": "No match count, first fixture date, or financial terms were disclosed by KSI, DAZN or the club.",
                "so_what": "Live sport sponsorship is starting to show up inside creator channels instead of only inside broadcast deals.  That means sixth-tier football pricing attached to a top-20 global audience, which has not been a thing you could buy before.  It also means the person selling you the sponsorship owns the team, so there is no rights holder in the middle taking a cut.",
                "do_this": "Ask your sports sponsorship contacts what creator-channel rights cost this season, while the comparable deals are still being written.",
            },
            {
                "title": "YouTube is premiering creator films at the Toronto film festival",
                "hook": "Nobody is discovering a YouTube show at TIFF.  That is not what it is for.",
                "stamps": [
                    ("TUBEFILTER", "https://www.tubefilter.com/2026/08/13/tiff-toronto-international-film-festival-youtube-variety-creator-premieres/"),
                    ("THE PUBLISH PRESS", "https://news.thepublishpress.com/p/youtube-tiff"),
                ],
                "body": [
                    "September 10, opening day at TIFF, YouTube and Variety host an event launching the festival's content marketplace.  Mark Vins of Brave Wilderness screens a Galapagos documentary.  Ziwe premieres two episodes.  Both go YouTube-exclusive afterwards.",
                    "YouTube's global head of creators called it proof that creators are leading the industry's future.  The sharper reading: <mark>YouTube is renting a prestige film festival's credibility</mark> so that when it sells creator-led series to advertisers, buyers compare them to television instead of to influencer posts.",
                    "Same play as the Sundance creator day in 2025, the Cannes summit this year, and the Emmy campaign.  It is working, which is why they keep doing it.",
                ],
                "so_what": "The format YouTube is actively pushing money and attention behind right now is premium, long, single-subject documentary — the stuff that looks most like TV.  That is where brand-funded series money moves next, because it is the format that holds the highest prices.  A festival premiere is a pricing strategy wearing a tuxedo.",
                "do_this": "Pitch your next brand-funded series as a single-subject documentary and take it to a festival before it goes to YouTube.",
            },
            {
                "title": "A creator media company just got priced at half a billion dollars",
                "hook": "The number is not the story.  What is inside it is.",
                "stamps": [
                    ("AXIOS", "https://www.axios.com/2026/08/12/alex-cooper-unwell-500-million-valuation-investment"),
                    ("BLOOMBERG", "https://www.bloomberg.com/news/articles/2026-08-12/-call-her-daddy-host-raises-money-at-500-million-valuation"),
                    ("FORTUNE", "https://fortune.com/2026/08/12/call-her-daddy-host-alex-cooper-raises-money-at-a-500-million-valuation/"),
                ],
                "body": [
                    "WTSL, Patrick Whitesell and Jason Lublin's firm, invested in Alex Cooper's Unwell at a $500 million valuation.  First outside money the company has ever taken.  Cheque size undisclosed.",
                    "The structure is the lesson.  Unwell is a podcast network of a dozen-plus shows, a film and TV production arm, a live events business, a creative agency, and a drinks line — with a SiriusXM distribution deal on top.",
                    "<mark>Nobody valued that as a podcast.  They valued it as a bundle</mark> where the creator owns the products and the agency, and therefore keeps margin that would otherwise have gone to a brand partner and the people booking her.",
                ],
                "flagnote": "Cooper's claim of 70 million women reached monthly is a company statement, not an audited measurement.",
                "so_what": "A half-billion mark sets the price the next creator-founded company quotes at you in a negotiation.  More useful day to day: it tells you what creators at this level now want.  A share of the thing, not a fee for the post.  Once a creator can build and sell the product themselves, your flat sponsorship fee starts looking like the worse offer.",
                "do_this": "Offer product or equity terms to your top three creator partners this month and find out which ones would take that over a fee.",
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
                "title": "Kai Cenat and IShowSpeed played Minecraft for 121 hours and out-watched most of the esports calendar",
                "hook": "Two guys, one world, five straight days — more total watch time than nearly every pro esports event this year.",
                "open": True,
                "stamps": [
                    ("STREAMS CHARTS", "https://streamscharts.com/news/kai-cenat-ishowspeed-2026-minecraft-marathon-recap"),
                    ("WIN.GG", "https://win.gg/kai-cenat-and-ishowspeed-minecraft-marathon-completed/"),
                    ("ESPORTS CHARTS", "https://escharts.com/news/t1-makes-history-winning-worlds-2025-event-reached-over-67m-peak-viewers"),
                ],
                "body": [
                    "August 7 to 12.  Five days and an hour, four channels, both of them live on Twitch and YouTube at once.  <mark>Over 30 million total hours watched.</mark>  IShowSpeed's YouTube stream alone did 13.5 million of them.  Kai Cenat's Twitch added 7.77 million and peaked near 198,000 concurrent.  IShowSpeed's Twitch peak of 128,726 was a personal record.  Average across all four: about 61,800.  42 deaths.  All four bosses down.",
                    "Reality check on peak, though: the League of Legends world final last November hit 6.7 million concurrent.  That is roughly fifteen times bigger.  Esports still owns the single biggest moment by a mile.",
                    "Where the marathon wins is accumulated time.  Streams Charts has it beating Ludwig's Streamer Games 2026, LEC spring, VALORANT Masters Santiago and the Kings World Cup Nations.  Gamescom's opening showcase did 4.6 million hours in 2025 — the marathon did about six and a half times that.",
                    "The 2024 run of the same bit did 18.88 million hours.  This one did 30 million plus.  <mark>That is 59% growth in two years on a format that is literally just staying awake.</mark>",
                ],
                "so_what": "Endurance formats convert time into reach in a way scheduled broadcasts structurally cannot.  A tournament sells you a series of appointments; a marathon sells continuous presence and lets the audience rotate through it for five days.  No rights deal, no crew, no league — which is why the cost side looks nothing like the number it produced.",
                "do_this": "Budget one endurance format into your next creator campaign and grade it on total hours watched instead of peak viewers.",
            },
            {
                "title": "The next big number lands August 25",
                "hook": "Gamescom's opening show is the most predictable large audience on your calendar.",
                "stamps": [
                    ("GAMESRADAR", "https://www.gamesradar.com/games/events-conferences/gamescom-2026-schedule/"),
                    ("NINTENDO LIFE", "https://www.nintendolife.com/guides/gamescom-2026-opening-night-live-time-date-and-how-to-watch"),
                    ("STREAMS CHARTS", "https://streamscharts.com/news/gamescom-opening-night-2025-recap"),
                ],
                "body": [
                    "Opening Night Live, Tuesday August 25, 11am Pacific, Geoff Keighley and Eefje Depoortere hosting, on YouTube and Twitch.  Show floor in Cologne runs the 26th to the 30th — 357,000 people through the doors last year.",
                    "Marks to beat from 2025: 2 million plus concurrent, 1.8 million average, 4.6 million hours, 72 million total views, 1,100 plus channels carrying it.",
                    "<mark>Watch the channel count, not the viewer count.</mark>  That is the number that moved first last year and everything else followed it.",
                ],
                "so_what": "This is the cleanest annual test of whether creator redistribution still beats first-party broadcast, and it runs on a fixed date with published history — so it is unusually easy to learn something real from.  If channel count climbs and viewership does not follow, the effect has hit its ceiling and you want to know that before planning a launch around it.",
                "do_this": "Block out August 25 and log the co-streaming channel count next to the viewer figures, so you have your own baseline for next year.",
            },
            {
                "title": "Ludwig's Streamer Games grew its audience faster than it grew its runtime",
                "hook": "Watch time up 72%, airtime up 31%.  The gap is the whole point.",
                "stamps": [
                    ("STREAMS CHARTS", "https://streamscharts.com/news/ludwigs-streamer-games-2026-recap"),
                    ("STREAMS CHARTS INFO", "https://streamscharts.com/news/ludwigs-streamer-games-2026-info"),
                ],
                "body": [
                    "August 1 to 2, a USC track stadium in Los Angeles, records across the board: hours watched up 72% year on year, peak up 37%, average up 31%, airtime up 31%.  Against 2024 the peak nearly tripled and hours watched grew about 3.7 times.",
                    "For an actual anchor number, 2025 peaked at 374,674 concurrent and did 3.74 million hours, carried by 90-plus channels against 24 the year before.",
                    "<mark>Watch time grew more than twice as fast as airtime.</mark>  That is the difference between an audience that genuinely got bigger and an event that just ran longer.",
                ],
                "flagnote": "Streams Charts published percentage changes for 2026 rather than absolute figures, so the 2026 totals cannot be stated directly.",
                "so_what": "Any time a show reports record watch time, the first question is whether it simply ran longer.  Here it did not — airtime and watch time separated by more than a factor of two, so that is real audience growth.  It is the check worth running on every event a partner brings you with the word record attached.",
                "do_this": "Ask for airtime alongside hours watched whenever an event pitches you a record, and compare the two growth rates before committing.",
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
                "title": "Kinigra Deon",
                "hook": "She calls herself the Tyler Perry of YouTube.  She is now selling episodes to a streaming service.",
                "open": True,
                "stamps": [
                    ("THEWRAP", "https://www.thewrap.com/media-platforms/tv/kinigra-deon-speed-tubi-series/"),
                    ("TIME100 CREATORS", "https://time.com/collection/time100-creators/2026/kinigra-deon/"),
                    ("CHANNEL", "https://www.youtube.com/@KinigraDeon"),
                ],
                "watch": {
                    "label": "TOP VIDEO, LAST 3 MONTHS",
                    "title": "The GROUP CHAT Was ROBBED!!! | Messy Group Chat Season 5",
                    "url": "https://www.youtube.com/watch?v=XdW7YgcrUTE",
                    "meta": "1,673,726 views · published 26 May 2026 · 2h 45m",
                    "note": "A feature-length season premiere of her scripted teen drama, told through a friend group's text thread and live-action scenes.  Watch ten minutes and you will understand the whole business.",
                },
                "body": [
                    "She writes, directs and stars in scripted series — supernatural drama, horror, romance, family comedy — three episodes a week, out of Birmingham, Alabama.  Channel started in 2018.",
                    "5.6 million subscribers last December, 5.9 million by July, 14 million plus across her platforms.  Roughly 300,000 added in seven months on a channel that already had size.",
                    "Here is the part that should get your attention.  <mark>Her top video in the last three months is a 2 hour 45 minute season premiere with 1.67 million views.</mark>  Her top upload full stop is a Kohl's-sponsored Short about a kid ruining her clothes on the first day of kindergarten — 11.4 million views in July.  A second Kohl's Short did 10.2 million.  She is already running branded work at scale and nobody in the trades is writing about it.",
                    "The last eight months: TIME's 2026 creators list in July.  Tubi launched her scripted series Speed with Spotter financing it.  Two supernatural films with Kevin Hart's Hartbeat.  A physical production studio going up in Alabama.  <mark>She did not get bigger.  She changed what she is</mark> — a channel became a scripted studio that supplies a streamer and still owns its audience outright.",
                    "She is invisible on the creator-economy circuit.  No podcast tour, no conference keynote.  The trades file her under streaming programming instead of creators, which is exactly why she is not already on every list you have read.",
                ],
                "so_what": "She sells something almost nobody else can: episodic scripted inventory, recurring characters, on a schedule, watched on TV screens in multi-episode sittings.  That is the living-room inventory brands keep saying they want and keep failing to find.  And the Kohl's numbers prove she can already run a brand integration without it feeling bolted on.",
                "do_this": "Watch ten minutes of the Messy Group Chat premiere and decide whether your product could sit inside a scene rather than in front of it.",
            },
        ],
    },
    {
        "id": "money",
        "name": "THE MONEY",
        "page": "pg. 07",
        "note": "numbers that should change somebody's plan",
        "tint": None,
        "items": [
            {
                "title": "Half of an influencer budget is now media, not talent",
                "hook": "By next year the money spent boosting creator posts equals the money paid to make them.",
                "open": True,
                "stamps": [
                    ("DIGIDAY", "https://digiday.com/media-buying/influencer-boost-budgets-are-throwing-gas-on-social-video-spending-fire/"),
                    ("DIGIDAY / RIGHTS", "https://digiday.com/future-of-tv/future-of-tv-briefing-brands-are-spending-more-to-advertise-creators-content-making-usage-rights-a-focal-point/"),
                    ("IAB", "https://www.iab.com/news/creator-economy-ad-spend-to-reach-37-billion-in-2025-growing-4x-faster-than-total-media-industry-according-to-iab/"),
                ],
                "body": [
                    "US spend on boosting creator content and US spend on creator production fees both land around $14.2 billion in 2027.  <mark>In 2028 the boosting side hits $16.1 billion and passes the fees entirely.</mark>",
                    "Agencies are reporting individual clients lifting boost budgets 79% and 253% inside a single year.  Individual campaign boost budgets now run from a few thousand dollars to $5 million.",
                    "The consequence is contractual, not creative.  Content you are not allowed to put money behind is worth a fraction of content you are — so the right to run somebody's face as paid media is becoming the sharpest thing in the negotiation.",
                    "And if you are quoting a creator campaign on production alone, you are understating what it actually needs by close to half.",
                ],
                "numbers": [
                    ("$14.2B", "paid amplification, 2027"),
                    ("$14.2B", "creator production fees, 2027"),
                    ("$16.1B", "amplification in 2028, overtaking fees"),
                ],
                "flagnote": "The parity forecast rests on a single set of projections, and the 79% and 253% figures come from unnamed clients at one agency.",
                "so_what": "The shape of an influencer budget is flipping from mostly-talent to half-media, and most planning templates have not noticed.  A brief that budgets the shoot and treats the boost as contingency runs out of money halfway through.  Rights are the pinch point because they used to be an afterthought clause written when nobody planned to spend real media money behind the thing.",
                "do_this": "Add a paid-usage clause with a defined term and territory to your standard creator contract this quarter, and quote the boost budget on the same line as the fee.",
            },
            {
                "title": "YouTube advertising grew 13%, making it the slowest major line at Google",
                "hook": "$11.1 billion in one quarter, and it is now Alphabet's laggard.",
                "stamps": [
                    ("ALPHABET Q2 2026", "https://www.marketscreener.com/news/alphabet-2026-q2-earnings-press-release-ce7f51d9df8cf425"),
                    ("HOLLYWOOD REPORTER", "https://www.hollywoodreporter.com/business/business-news/youtube-ad-revenue-reported-giant-alphabet-google-profits-1236654342/"),
                    ("VARIETY", "https://variety.com/2026/digital/news/youtube-q2-2026-ad-sales-alphabet-google-earnings-results-1236818132/"),
                ],
                "body": [
                    "$11.055 billion in advertising for the three months to June, against $9.796 billion a year earlier.  About 12.9% growth.",
                    "One thing to be careful about: that is advertising only.  YouTube TV, Premium, Music and Sunday Ticket sit in a separate Google line worth $12.9 billion in the quarter, so the real YouTube business is a lot bigger than $11.1 billion.  It is also global, not US.",
                    "<mark>Google search ads grew 17% and Alphabet overall grew 24%.</mark>  YouTube is now the slowest-growing major ad line in the company.",
                ],
                "so_what": "The runaway-growth framing for YouTube is a couple of years out of date, and anyone still pitching it that way is going to get corrected by a client who reads earnings releases.  Double-digit growth on an $11 billion base is a strong business — it just means moderate pricing pressure ahead and Google's product attention pointed elsewhere.",
                "do_this": "Lead your next YouTube pitch with the television viewing share number and let the size of the base do the work.",
            },
            {
                "title": "YouTube is 13.8% of all American television viewing",
                "hook": "On actual TV sets it out-draws about two-thirds of the cable bundle.",
                "stamps": [
                    ("NIELSEN", "https://www.nielsen.com/news-center/2026/streaming-embarks-on-annual-summer-ascent-in-nielsens-may-2026-gauge-reports/"),
                    ("PPC LAND", "https://ppc.land/youtube-gains-0-4-points-to-13-8-of-us-tv-as-cable-drops-to-20-4/"),
                    ("MEDIAPOST", "https://www.mediapost.com/publications/article/416872/streaming-viewing-share-hits-record-high-in-may-n.html"),
                ],
                "body": [
                    "Nielsen's May numbers put YouTube at 13.8% of total American TV watch time — a record, up 0.4 points in a month and 1.3 on the year.  Streaming overall hit 48.6%.  Cable fell to 20.4%, broadcast to 19.2%.",
                    "Read the definition properly, because this is the most misquoted stat on the beat.  <mark>It only counts time on a television set.</mark>  YouTube on phones, tablets and laptops is not in there at all, so the real share of video attention is higher.",
                    "Seasonal caveat: streaming share climbs every late spring and summer.  Part of that record is just the calendar.",
                ],
                "so_what": "Viewers stopped treating television and YouTube as different things a while ago and the measurement finally caught up.  If YouTube is still sitting in a social budget line at your company, it is being planned against the wrong competitors and judged on the wrong benchmarks.  It is competing with cable for the same room.",
                "do_this": "Move YouTube into your television budget line at the next planning cycle and benchmark it against cable instead of social.",
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
                "title": "Cut for the couch, not the feed",
                "hook": "The biggest screen watching your video is an actual television, and your edit is still built for a phone.",
                "open": True,
                "stamps": [
                    ("NIELSEN", "https://www.nielsen.com/news-center/2026/streaming-embarks-on-annual-summer-ascent-in-nielsens-may-2026-gauge-reports/"),
                    ("PPC LAND", "https://ppc.land/youtube-gains-0-4-points-to-13-8-of-us-tv-as-cable-drops-to-20-4/"),
                ],
                "body": [
                    "If YouTube is 13.8% of American TV watch time, a big chunk of your audience is sitting eight to ten feet back with the sound on.  Nearly every convention in a modern YouTube edit assumes the exact opposite — phone at arm's length, sound off, thumb hovering.",
                    "Four things change when you cut for a room instead of a hand.  <mark>Text has to read at ten feet, not ten inches</mark> — lower thirds sized for a phone straight up vanish on a couch.  Sound stops being decoration, because feed edits lean on captions to carry meaning and TV viewers are actually listening.  Wide shots work again; a face filling the frame is fine on a phone and feels like a confrontation on a 55-inch panel.  And your cold open can breathe, because a remote is a much slower weapon than a thumb.",
                    "On runtime, borrow the discipline from Ludwig's Streamer Games: watch time up 72%, airtime up 31%.  Longer is not the move.  The gap between those two numbers is the move.",
                ],
                "so_what": "Editing conventions follow where people watch, and where people watch moved without most edit suites noticing.  The failures are small and cheap to fix — undersized text, caption-dependent storytelling, shot sizes built for a six-inch screen — but they add up to a video that looks amateur on a TV and totally fine on a phone.  Your client is increasingly on the TV.",
                "do_this": "Play your last three videos on a TV from across the room and resize every piece of on-screen text you cannot read from the sofa.",
            },
        ],
    },
]

FORECAST = [
    {
        "confidence": "LIKELY",
        "window": "24 August onward",
        "headline": "Every view count chart in September becomes useless",
        "body": "New views count from frame one, old views do not get restated.  So from the 24th your archive and your new uploads are measured on two different rulers.  Anyone building a year-on-year comparison in September will see a jump that is entirely accounting, and at least a few of them will present it as growth.",
        "do": "Screenshot your channel and campaign dashboards this week so you have a clean pre-change baseline to argue from.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "next 3 months",
        "headline": "Sponsorship rates get renegotiated against Engaged Views",
        "body": "Once public view counts inflate and everyone can see it, the number stops working as a pricing input.  Engaged Views is the metric that still tracks actual watching, and it is reported separately.  Expect the sharper buyers to start writing deals against it and the rest to keep paying inflated rates for a while.",
        "do": "Rewrite your creator contract template to price against Engaged Views before the 24th.",
    },
    {
        "confidence": "LIKELY",
        "window": "by 31 January 2027",
        "headline": "A visible scramble to beat the monetization bar",
        "body": "Creators sitting just under 4,000 watch hours have about five months to clear the old threshold before it doubles.  Expect a surge in upload frequency through Q4, a wave of get-monetized-before-February content, and a lot of channels suddenly very interested in guaranteed money.",
        "do": "Lock rates now with creators in that band, while a guaranteed budget is worth more to them than a bigger fee.",
    },
    {
        "confidence": "LIKELY",
        "window": "through 2027",
        "headline": "Usage rights become the hardest part of a creator negotiation",
        "body": "Once the money spent boosting a post matches the money spent making it, the right to run somebody's face as paid media is worth as much as the shoot.  Rights clauses written back when nobody planned to spend real media money are about to get renegotiated, expensively, in the middle of live campaigns.",
        "do": "Rewrite your standard creator contract now with a defined usage term and territory, ahead of the campaigns that will need it.",
    },
    {
        "confidence": "LONG SHOT",
        "window": "next 18 months",
        "headline": "More creators buy the thing they broadcast",
        "body": "KSI holding equity and broadcast rights in the same club is a template, not a stunt.  If Dagenham puts up a watchable number this season, expect creators to start buying small sports properties and cultural events outright instead of sponsoring them.  The economics favour owning the thing whose audience you already are.",
        "do": "Work out which of your properties would be worth more with a creator on the ownership side, and open that conversation early.",
    },
]

TLDR = [
    "YouTube starts counting a view from the first frame on 24 August, so every channel's public numbers inflate overnight.  Rewrite live creator contracts to price against Engaged Views this week.",
    "Half of an influencer budget is becoming media rather than talent, hitting rough parity at $14.2 billion each in 2027.  Add a paid-usage clause with a defined term and territory to every creator contract from now on.",
    "Nearly half of eventually-winning creator ads still look like duds at $100 of spend, and winners decay after about 36 days.  Set a $1,000 no-kill floor and diary a 36-day retirement date for every winner.",
    "Ads posted from a creator's own handle beat recut licensed footage by 19% on clicks and 10% on conversion.  Write handle-posting rights into your next deal and budget the higher media cost up front.",
    "YouTube doubles its monetization entry bar on 1 February 2027, to 8,000 watch hours or 20 million Shorts views.  Sign your emerging creator partners this quarter while guaranteed budget still beats a bigger fee.",
    "YouTube is 13.8% of American television watch time, measured on TV sets alone.  Move it into your television budget line and cut your next video to read from across a room.",
    "Kinigra Deon is supplying scripted episodes to Tubi off a 5.9-million-subscriber channel she still owns, and her Kohl's Shorts are clearing 10 million views.  Watch ten minutes of her Messy Group Chat premiere and decide whether your product fits inside a scene.",
]
