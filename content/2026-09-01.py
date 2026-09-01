# -*- coding: utf-8 -*-
"""Content for THE FEED — issue data only.  The render spec lives in build_feed.py."""

ISSUE = {
    "date_iso": "2026-09-01",
    "kicker": "Crux Media // Tuesday 1 September 2026",
    "tagline": "What brands did on YouTube yesterday, and whether it worked.",
    "pace": "STEADY",
    "next_drop": "Next drop: Wednesday, 06:30 MT",
}

LEAD = {
    "headline": "GOOGLE JUST PUT A NUMBER ON THE MOST VALUABLE THING IN A YOUTUBE AD, AND IT IS A HUMAN VOICE",
    "deck": "Google quietly updated its creative guidance for YouTube advertisers with three numbers from its own campaign data.  A human voice in the ad is worth 12 percent more conversions.  Text on screen is worth 3 percent.  The brand appearing in the first five seconds is worth 4 percent.  Voice beats the other two combined, and voice is the thing everybody cuts first.",
    "stamps": [
        ("GOOGLE ADS HELP CENTRE", "https://support.google.com/google-ads/answer/18061165?hl=en"),
        ("SEARCH ENGINE LAND · 28 AUG", "https://searchengineland.com/google-says-better-youtube-creative-can-more-than-double-roi-486180"),
        ("TUBEFILTER · 31 AUG", "https://www.tubefilter.com/2026/08/31/google-youtube-guidelines-for-advertisers-human-voices/"),
    ],
    "body": [
        "The page is called Creative guidance on YouTube and it reads like housekeeping.  It is not.  Buried in it are the first hard figures Google has published on which parts of an ad actually move a sale, taken from its own Demand Gen skippable in-stream ads.  The wording is exact: <mark>including a human voice drives 12% higher conversions on average.  Having supers or a text overlay drives 3% higher conversions on average.  Having the brand visualized in the first 5 seconds drives 4% higher conversions on average.</mark>  All three are marked US, July 2026.",
        "Read the ranking rather than the headline.  Voice is worth roughly twice the two visual levers put together.  And the two visual levers are the ones every brand already does, because they are free.  You add a caption in the edit.  You slide the logo earlier on the timeline.  Neither costs anything, which is exactly why neither is worth much.",
        "Voice costs.  A read means a booth, a performer, a round of notes, and a lock that has to be broken and redone for every language and every regional variant.  Music beds and captions scale for free.  So when a brand needs forty versions of one ad by Friday, the voice track is the first thing to go.  Google has now priced that decision at 12 percent of your conversions.",
        "Note precisely what the number measures.  It measures the presence of a human voice, not the quality of the performance.  Nobody has published a figure saying a great read beats an adequate one.  The finding is binary — there is a voice, or there is not — and the gap between those two states is bigger than anything else Google chose to publish.",
        "The framing around the figures matters too.  Google opens the page by citing Nielsen, that <mark>creative accounts for 49% of all campaign ROI</mark>, and Ekimetrics, that improving your creative can more than double your return on YouTube.  That is Google telling advertisers where their remaining control lives.  Targeting is automated now.  Bidding is automated now.  The creative is the last part of the buy you still own, so Google would very much like you to spend more attention on it.  That is self-interested and it is also true.",
        "One more line on the same page is worth stealing.  Google tells advertisers to strip out any button, arrow or overlay in an image that looks clickable but is not, because that fake interface competes with YouTube's real buttons and confuses people.  Every brand doing fake-play-button thumbnails on paid placements is paying for confusion.",
    ],
    "numbers": [
        ("12%", "more conversions when a human voice is present in the ad"),
        ("4%", "more conversions when the brand is visible in the first five seconds"),
        ("49%", "of campaign return that Nielsen attributes to creative"),
    ],
    "flagnote": "Google sells the inventory this study flatters, and publishes no sample size, campaign count or margin of error for the three figures.  The Nielsen and Ekimetrics numbers are cited by name with no link to either study.  Treat the ranking as directional and the exact percentages as unaudited.",
    "so_what": "Voice is the only element that keeps working when the viewer is not looking at the screen, and an enormous share of YouTube gets consumed that way — second screen, phone on the counter, sound on, eyes elsewhere.  Captions and an early logo only pay when someone is watching the picture.  A voice reaches the people who are only listening, which is why it outperforms the things that cost nothing.",
    "do_this": "Pull every YouTube ad variant you have running this week and sort them into two piles: has a voice track, does not.  Put a human read on the top three performers in the silent pile and run them against their own originals for two weeks.  Then price a voice session into every future edit brief as a line item, not an optional extra.",
}

SECTIONS = [
    {
        "id": "ws", "name": "W'S", "page": "pg. 02",
        "note": "what worked, and the exact reason it worked",
        "tint": "blue",
        "items": [
            {
                "title": "Factor signed Serena Williams in June.  She announced her US Open comeback afterwards.",
                "hook": "The decision that made this campaign possible was made months before anyone knew there was a moment to campaign around.",
                "stamps": [("ADWEEK · 31 AUG", "https://www.adweek.com/brand-marketing/factor-serves-up-a-glp-1-meal-plan-in-new-serena-williams-ad-spot/")],
                "body": [
                    "Meal-kit brand Factor launched a campaign called Let's Eat Real with Serena Williams as global ambassador, running through the US Open.  The spots play off her return to tennis.  One opens on a tense meeting about her career and reveals she is choosing a meal.  Another has her up against a microwave timer.",
                    "The interesting part is the calendar.  Factor started courting Williams in January and signed her in June, on a multi-year deal with a rotating monthly menu she curates.  Her comeback announcement came later.  When it landed, Factor already owned the asset instead of bidding against everyone else for it.",
                    "Then the production numbers.  From her announcement to finished spots took one week of planning plus a half-day shoot near her home in Palm Beach, working with Maximum Effort.  Out of that half day came two full ads, thirty stills and an hour of usable behind-the-scenes footage.  CMO Christopher Stadler calls it the fastest turnaround the brand has attempted.",
                    "That output ratio is the actual craft lesson.  You cannot move at the speed of a news cycle if your production model needs a full crew day per deliverable.  A half-day that yields two cut spots and thirty stills is a shoot that was planned as a content harvest, not as an ad shoot with pickups.",
                ],
                "so_what": "Two separate things did the work, and neither of them was the creative.  Signing talent before the cultural moment exists turns a bidding war into a phone call.  And structuring a shoot to produce many deliverables from one setup is what makes a one-week turnaround physically possible.  The ad is fine.  The ad is not why this worked.",
                "do_this": "Take your next talent or creator shoot and rebuild the schedule around asset count rather than hero deliverable — block time for stills, verticals and unscripted footage inside the same setup.  And ask your talent team which of your current partners has something coming in the next six months that nobody has announced yet.",
            },
            {
                "title": "Dr. Squatch put a million dollars into a game with IShowSpeed and barely shot any ads",
                "hook": "The brand's own chief says most of the money went to the community making content, not to the campaign.",
                "stamps": [("MARKETING DIVE · 31 AUG", "https://www.marketingdive.com/news/why-dr-squatch-is-investing-in-experiences-not-ads-with-ishowspeed/829009/")],
                "body": [
                    "Unilever-owned Dr. Squatch launched Speedrun: Million Dollar Mission with IShowSpeed on Monday.  A nine-week, 25-challenge contest across the US, Canada, UK and Australia running to 31 October.  A briefcase holding a gold bar of soap is hidden in a city each week, GPS coordinates get progressively more readable across the week on stream, and fans post their own challenge attempts to TikTok, Instagram and YouTube for prizes.",
                    "The scale: a one million dollar prize pool, 25 scratch tickets worth ten thousand dollars each, a two hundred and fifty thousand dollar briefcase finale, and more than 4,000 Walmart stores acting as physical hubs with displays and QR codes.  Built with Applied MSCHF, the agency arm behind the big red boots.",
                    "Chief brand officer John Ludeke says the quiet part plainly.  The brand shot only a basic set of ads.  The majority of the marketing money supports the community making hundreds of pieces of content instead.  He contrasts it directly with brands that use streamers the top-down way they used to use celebrities.",
                    "The other number nobody will put on a slide: partnership development started in April 2025.  Sixteen months from first conversation to launch.",
                ],
                "so_what": "The design principle is participation instead of impressions.  Every challenge a fan films is a piece of media the brand did not pay to produce and did not have to buy distribution for, and the escalating prize values are engineered so the noise compounds week over week rather than peaking on day one.  The Walmart codes are what turns the game into footfall.",
                "do_this": "Before your next creator deal, calculate what share of the budget produces content the audience makes versus content you make.  If it is under a quarter, redesign the deal around a repeatable action fans can film in under a minute, and give it a prize ladder that gets bigger each week.",
            },
        ],
    },
    {
        "id": "ls", "name": "L'S", "page": "pg. 03",
        "note": "what broke, and the failure mode behind it",
        "tint": "pink",
        "items": [
            {
                "title": "Wrong owner: the Callaway ad failed a test that takes minutes, because nobody ran one",
                "hook": "A third of viewers found it offensive.  Shock scored eight times the norm.  A synthetic panel gave it one out of five in minutes.",
                "open": True,
                "stamps": [
                    ("ADWEEK · 31 AUG", "https://www.adweek.com/brand-marketing/callaway-and-good-goods-ad-was-so-bad-even-ai-audiences-sounded-the-alarm/"),
                    ("TUBEFILTER · 30 AUG", "https://www.tubefilter.com/2026/08/30/good-good-callaway-driver-ad-controversy/"),
                ],
                "body": [
                    "You already know the ad.  Golf channel Good Good, 2.1 million subscribers, produced a spot in which co-founder Garrett Clark shoves creator Alexis Miestowski to the ground and stands over her telling her not to touch his driver.  Callaway approved it.  It went out.  It came down.",
                    "This week the fallout hardened and the useful data arrived.  Callaway dissolved a three-year deal.  Retailers pulled Good Good merchandise.  Good Good withdrew from a six million dollar PGA Tour title sponsorship.  Golf Channel cancelled an already-filmed season of Big Break x Good Good.  Callaway pledged one million dollars to organisations preventing violence against women.  Good Good chief executive Matt Kendrick says he has removed the people responsible, says he never saw the ad before it went live, and when asked whether he would sue Callaway replied that he was not opposed.",
                    "Then Zappi tested the pulled ad after the fact.  With US consumers it scored significantly below advertising norms on appeal, likelihood to drive behaviour, brand fit, relevance, believability and attention.  <mark>Nearly one-third said there was something offensive, unpleasant or disturbing about the ad.  Shock was eight times higher than the norm.</mark>  Run past 150 AI synthetic respondents trained on real consumer response data, it came back in minutes with the lowest possible score, one out of five, and a note recommending they soften the physical moment so it read as playful rather than awkward.",
                    "Both chief executives are now arguing about who approved it.  That is the wrong argument.  Approval rights existed and were used — Callaway had them and signed off.  What did not exist was a screen.  The premise was legible as a problem to the cheapest possible check, and no cheap check was in the workflow.",
                    "The structural reason is worth naming.  Brands now ship hundreds of small creator assets a month through a process that was designed to research three big campaigns a year.  Creator content moves faster than brand content because it looks like a post rather than a spot, so it routes around the research gate entirely.",
                ],
                "flagnote": "The Adweek piece is a bylined column by Nataly Kelly, chief marketing officer of Zappi, which sells the creative testing product the article concludes brands should be using.  The test figures are single-sourced to the vendor.  The consequences — the dissolved deal, the six million dollar sponsorship, the cancelled season — are independently reported.",
                "so_what": "The failure mode is ownership, not taste.  Somebody has to own the go or no-go on every creator asset, and right now that job is split between a brand that assumes the creator screened it and a creator who assumes the brand did.  A screen that takes minutes and costs less than the club being advertised was never in anyone's job description.",
                "do_this": "Name one person as the pre-publication reviewer on every creator-made asset this week, brand side, with the power to stop it.  Write into your next creator contract who owns the takedown and who speaks publicly if something goes wrong, because that ambiguity is what turned one bad ad into a two-party public fight.",
            },
            {
                "title": "Wrong fit: Old Navy bought the biggest branded video of the week and it is set in a house being destroyed",
                "hook": "104 million views, and the comment section hates what is happening on screen.",
                "stamps": [("TUBEFILTER · 31 AUG", "https://www.tubefilter.com/2026/08/31/top-5-branded-videos-mrbeast-alans-universe-amanda-pulitano-cyra-riley/")],
                "body": [
                    "The most-watched branded video of the week was MrBeast's Last To Leave Mansion, Keeps It, at 103,995,201 views, carrying Feastables, Lowe's and Old Navy.  It is a classic last-to-do-X challenge and the house gets wrecked.",
                    "The top comments are not about the brands.  They are hostile to the contestants and to the destruction — one of the most-liked reads them destroying the house pisses me off, none of them deserve it.  That is 104 million views attached to irritation rather than delight, which is a different asset than 104 million friendly views, and no dashboard will tell you which one you bought.",
                    "Lowe's lands it.  A home-improvement brand standing in a wrecked house is in on the joke and the joke points at the product.  Old Navy is running a back-to-school message in the same wreckage with no such connection.  Same footage, same reach, two completely different outcomes.",
                ],
                "so_what": "Reach was never the variable here.  Both brands got the same hundred million impressions.  What differs is whether the thing happening on screen makes the brand make sense, and in a destruction format only the brands that repair, sell or clean things get that for free.  Everyone else is renting proximity to an audience that is currently annoyed.",
                "do_this": "For your next creator integration, write down in one sentence why the format makes your product make sense.  If the sentence only works because the audience is large, buy a different video.",
            },
        ],
    },
    {
        "id": "moves", "name": "MOVES", "page": "pg. 04",
        "note": "who did what, and what it changes",
        "tint": None,
        "items": [
            {
                "title": "Markiplier bought 8.5 percent of GoPro because it would not show him a camera, then reviewed the camera",
                "hook": "The stock went up 33 percent.  He is now the largest shareholder and a paid sponsor of the same company.",
                "stamps": [("TUBEFILTER · 31 AUG", "https://www.tubefilter.com/2026/08/31/markiplier-gopro-mission-1-ils-accessible-filmmaking-shareholder/")],
                "body": [
                    "GoPro refused to let Mark Fischbach look at its first interchangeable-lens cinema camera at NAB in April.  So he bought the company instead.  An SEC filing dated 20 August shows 13.5 million shares, an 8.5 percent passive stake, making him GoPro's single largest shareholder.  Shares surged 33 percent to $1.39 on the news, from a stock that had been trading under a dollar and hit an all-time low of $0.57.",
                    "GoPro then handed him the camera and agreed to sponsor his channel.  The Mission 1 Pro ILS ships tomorrow at $699.99.  His fourteen-minute video argues it out-shoots the seven thousand dollar RED Komodo-X he shot Iron Lung on, and he tells Bloomberg the entry point into cinema cannot be seven thousand dollars because people cannot afford seven thousand dollars.",
                    "For a brand, the lesson is which endorsement carried weight.  Fischbach is known for turning brands down and being hard on the ones he takes.  That is precisely why a market moved on his opinion.  The endorsement was not purchased — the equity came first and the sponsorship followed — and that sequence is the whole reason anyone believed it.",
                ],
                "so_what": "The partners who are hardest to sign are the ones whose word is load-bearing, and the reason they are hard to sign is the same reason their word works.  Notice too what gave him something to advocate for: a price that breaks a category open.  A critical creator will not read your script, but they will argue for a genuine price disruption without being asked.",
                "do_this": "List the three creators in your category who have publicly turned down sponsors, and brief a pitch that gives them a position to argue rather than copy to read.  If your product has no argument in it, do not send the pitch — fix the product claim first.",
            },
            {
                "title": "Instagram will cut the reach of AI-generated profiles that do not say so",
                "hook": "Labelling is free.  Not labelling now costs you distribution.",
                "stamps": [("TECHCRUNCH · 31 AUG", "https://techcrunch.com/2026/08/31/instagram-puts-new-limits-on-undisclosed-ai-profiles/")],
                "body": [
                    "Instagram is renaming its AI creator label to AI-generated profile and will reduce the reach of accounts featuring AI-generated people that do not carry it.  Correctly labelled accounts are not penalised at all.",
                    "The scope is narrow and worth getting right.  The label applies where the person featured is generated or substantially created with AI.  It explicitly does not apply to AI used for photo editing, caption writing or graphics, so do not over-disclose ordinary post-production and confuse the signal.",
                    "The exposure for brands is second-hand.  If a creator you have hired runs an undisclosed AI persona, your paid post inherits the distribution penalty and you find out from a flat delivery report rather than a warning.",
                ],
                "so_what": "This is a disclosure regime with a price attached rather than a ban, which means the compliant answer is also the cheap answer.  The risk sits with partners rather than with your own account, and nobody is going to volunteer that their face is synthetic unless you ask.",
                "do_this": "Add one question to your creator vetting form: is any person appearing on this account generated or substantially created with AI.  Then check the label is applied on any campaign using a synthetic spokesperson before the first post goes live.",
            },
        ],
    },
    {
        "id": "onstream", "name": "ON STREAM", "page": "pg. 05",
        "note": "live audiences, and what the numbers actually mean",
        "tint": None,
        "items": [
            {
                "title": "Gamescom's audience got 27 percent bigger and 13 percent smaller at the same time",
                "hook": "The exact trick to watch for when someone sells you an audience number.",
                "open": True,
                "stamps": [
                    ("STREAMS CHARTS · 26 AUG", "https://streamscharts.com/news/gamescom-opening-night-live-2026-viewership"),
                    ("STREAMS CHARTS · 14 JUN", "https://streamscharts.com/news/youtube-sets-new-platform-record"),
                ],
                "body": [
                    "Gamescom Opening Night Live is the biggest games showcase of the European calendar, and the Streams Charts numbers for this year's edition are a masterclass in how one event produces two opposite headlines.  Hours watched: more than 5.8 million, up 27 percent on last year.  Peak concurrent viewers: 1.74 million, down 13.3 percent.",
                    "Both are true.  The reason they diverge is that the number of channels broadcasting the show went from just over 1,150 last year to 7,800 this year.  Spread the same show across seven times as many streams, with each of those streams running longer, and total hours watched climbs while the number of people watching at any one moment falls.  The audience got thinner and wider, not bigger.",
                    "So when a press release quotes only the 27 percent, it is telling you about the distribution footprint and calling it demand.  Twitch took over 62 percent of hours watched and YouTube 34.6 percent.  Average concurrent viewers were not published, which is the number that would settle it.",
                    "Give the peak some scale.  1.74 million people watching simultaneously is about nineteen Wembley Stadiums, which sounds enormous until you set it against YouTube's own platform record from June — 21.7 million concurrent viewers for Brazil against Morocco at the World Cup, with a single Brazilian streamer channel, CazéTV, taking 12.4 million of them on its own.  The biggest games showcase in Europe is about one twelfth of one group-stage football match on a free platform.",
                    "One live thing to diary: ZEvent runs Thursday 3 September to Sunday 6 September and has been announced as its final edition.  The French charity stream raised over sixteen million euros in 2025.  It is the last chance any brand gets to be associated with it.",
                ],
                "numbers": [
                    ("1.74M", "peak concurrent viewers, down 13.3 percent year on year"),
                    ("5.8M", "hours watched, up 27 percent year on year"),
                    ("7,800", "channels broadcasting it, against 1,150 last year"),
                ],
                "flagnote": "Streams Charts does not include audiences from Chinese livestreaming services, so any global comparison understates events with large Chinese audiences.",
                "so_what": "Hours watched is a volume metric and it rises whenever an event runs longer, adds channels or adds days.  It can go up while fewer people are actually there.  Peak and average concurrent viewers are the two that tell you how many humans were in the room, and average is the honest one because a peak can be a single minute.",
                "do_this": "Write peak and average concurrent viewers into your next livestream sponsorship reporting requirement alongside hours watched, and make it a condition of the deal.  When a partner can only supply hours watched, ask how many channels carried the stream this year versus last before you compare anything.",
            },
        ],
    },
    {
        "id": "watch", "name": "ONE TO WATCH", "page": "pg. 06",
        "note": "one creator with momentum, and what to buy from them",
        "tint": None,
        "items": [
            {
                "title": "Elevated Fabworks",
                "hook": "A truck fabrication channel was given a free abandoned yacht.  Two episodes have done a quarter of its entire five-year view count.",
                "open": True,
                "stamps": [("YOUTUBE CHANNEL", "https://www.youtube.com/@ElevatedFabworks")],
                "body": [
                    "210,000 subscribers.  11,404,483 views across the channel's whole life since September 2020.  Then in late July somebody gave the guy a free 45-foot yacht and the channel changed shape.",
                    "Episode one landed on 31 July and has done 1,916,958 views.  The ten uploads before it ranged from 47,000 to 461,000, with a median around 110,000.  That is roughly seventeen times the channel's normal video.  Episode two arrived on 22 August and held at 924,288 views in nine days, which is the part that matters — the first one could have been an accident, the second one is a series.  Between them the two yacht episodes account for about a quarter of everything the channel has ever done.",
                    "He is not a beginner.  The channel started as a spinoff after he left Grind Hard Plumbing Co, so the production standard was already there when the format found him.  Episodes run long — the two yacht ones are 1 hour 23 and 1 hour 20 — documentary-style builds for a gearhead, overland and DIY audience that buys tools.",
                    "Here is the number a media buyer should care about most.  Episode one already carried a paid Ridge integration.  A brand paid a 210,000-subscriber rate card and collected 1.9 million views.  That gap is open right now and it closes the moment his subscriber count catches up to his view count.",
                ],
                "watch": {
                    "label": "TOP VIDEO, LAST 3 MONTHS",
                    "title": "This FREE Abandoned Yacht Was Too Good to Pass Up - MY FIRST BOAT!",
                    "url": "https://www.youtube.com/watch?v=LHf4iX8R-ng",
                    "meta": "1,916,958 views · published 31 July 2026 · 1h 23m",
                    "note": "The pivot episode: he collects a derelict 45-foot yacht he was given for nothing and starts pulling it apart.",
                },
                "so_what": "A derelict-to-launch restoration is one of the few formats on YouTube with a guaranteed payoff episode built into it, and everyone who starts watching knows there is a day the boat goes in the water.  That gives a sponsor a narrative arc with a scheduled finale, which is exactly what you cannot buy in a normal upload calendar.  Pricing still reflects the subscriber count, not the series.",
                "do_this": "If you sell tools, welding gear, marine paint, portable power, parts or specialty insurance, approach him this week about presenting the whole restoration arc rather than buying a single read — title billing across the run plus your product genuinely being the one used on the boat on camera.  Price it against the two episodes already published, not against the subscriber count.",
            },
        ],
    },
    {
        "id": "money", "name": "THE MONEY", "page": "pg. 07",
        "note": "where the spend is going, and what the numbers exclude",
        "tint": None,
        "items": [
            {
                "title": "The FTC says Amazon charged advertisers their own full bid close to 80 percent of the time",
                "hook": "Over a million brands and sellers had complete dashboards and still could not see the rule they were bidding under.",
                "open": True,
                "stamps": [
                    ("FTC PRESS RELEASE · 31 AUG", "https://www.ftc.gov/news-events/news/press-releases/2026/08/ftc-states-sue-amazon-over-secret-ad-surcharge-scheme"),
                    ("TECHCRUNCH · 31 AUG", "https://techcrunch.com/2026/08/31/ftc-accuses-amazon-of-running-a-secret-ad-surcharge-scheme-in-new-lawsuit/"),
                ],
                "body": [
                    "The Federal Trade Commission and 22 state attorneys general sued Amazon on Monday in the Western District of Washington over what the FTC calls a secret ad surcharge scheme.  The allegation is that Amazon quietly stopped running its ad auctions the way advertisers understood them to work.",
                    "The numbers in the complaint, as published by the FTC: the share of Sponsored Products clicks where the winner was charged their own full bid rather than a runner-up price went from <mark>between 30% and 40% in 2021, to 70% in 2022, and to approximately 80% in 2024</mark>.  The FTC says the scheme has likely extracted tens of billions of dollars from unwitting advertising customers, affecting over one million brands and sellers, more than 500,000 of them small and medium-sized businesses.",
                    "The mechanism, in Amazon's own internal words as quoted by the FTC, was a surcharge hidden inside what it called a soft reserve price, alongside what the complaint describes as an invented auction participant producing proxy second-price bids that the FTC characterises as essentially shill bids.",
                    "Amazon calls the suit misguided, says it fundamentally misunderstands how advertisers operate, and says advertisers are properly informed about pricing.  None of this is proven — it is a regulator's complaint, and a deception case rather than an antitrust one.",
                    "The part that should travel beyond Amazon: every one of those advertisers had a working dashboard the whole time.  Spend, clicks, cost per click and return on ad spend were all reported accurately.  The reporting was complete and the pricing rule was still invisible.",
                ],
                "flagnote": "These are allegations in a complaint filed by a regulator, not audited figures or an Amazon disclosure.  Amazon denies them.",
                "so_what": "Stop modelling Amazon Sponsored Products as an auction where you pay one cent more than the next bidder.  For planning purposes, assume you pay what you bid.  The wider point is that complete reporting and understood pricing are two different things, and a platform that runs the auction and grades the results can deliver the first without the second.",
                "do_this": "Pull your 2021 to 2024 Amazon cost-per-click history this week and re-baseline your Q4 blended assumptions on a pay-your-bid model.  Check whether dynamic bid adjustments are switched on across your accounts, and add an auction-mechanics disclosure clause to your next retail media contract.",
            },
            {
                "title": "Ask which population a streaming share is measured on before you believe it",
                "hook": "Streaming is 48.2 percent of US viewing, or 44.4 percent, depending on who you count.",
                "stamps": [
                    ("PPC LAND · 31 AUG", "https://ppc.land/nielsen-changes-tv-currency-today-as-ad-supported-viewing-falls-to-71-5/"),
                    ("NIELSEN", "https://www.nielsen.com/news-center/2026/major-live-sports-events-bolster-broadcast-in-nielsens-q2-2026-ad-supported-gauge/"),
                ],
                "body": [
                    "Nielsen's Q2 Ad-Supported Gauge has ad-funded television at 71.5 percent of total US viewing for April to June, down 1.3 points from 72.8 percent in Q1.  On persons aged two and up, streaming takes 48.2 percent of that, broadcast 26.6 percent and cable 25.2 percent.",
                    "Change the base to adults 18 and over — the population most guarantees are actually written against — and it reads differently.  Streaming 44.4 percent, broadcast 28.6 percent, cable 27.0 percent.  The gap between streaming and broadcast narrows from 21.6 points to 15.8.  Same quarter, same data, one footnote apart.",
                    "Two more things to hold.  Streaming gained share of a bloc that is itself shrinking.  And Nielsen deployed seven separate methodology changes to its national measurement on 31 August at once, including new co-viewing capture and a new universe estimate, so August delivery will not be cleanly comparable to July and you will not be able to attribute any shift to a single cause.",
                    "Separately, TVision's panel of 5,000 US households puts about 24 minutes of daily advertising opportunity inside more than 200 minutes of daily video, of which roughly nine minutes qualify as attentive advertising time.",
                ],
                "so_what": "Population base is the cheapest trick in a media deck and almost nobody asks about it.  A seller quoting streaming at 48.2 percent is using a base that includes children, which flatters streaming.  Neither number is wrong and only one of them matches what you buy against.",
                "do_this": "When any seller quotes a share of viewing this week, ask two questions before you use it: which population base, and which quarter.  Then re-check your August delivery against plan rather than assuming it runs on from July, because the measurement changed underneath it on Monday.",
            },
            {
                "title": "July's ad market growth is the World Cup fading, not a pullback",
                "hook": "Up 11.9 percent, after June was up 19.3 percent.  Do not build Q4 on either.",
                "stamps": [("MEDIAPOST · 31 AUG", "https://www.mediapost.com/publications/article/417567/ad-market-continues-world-cup-related-surge-expan.html")],
                "body": [
                    "Guideline's Standard Media Index has the US ad market up 11.9 percent in July year on year, following June at 19.3 percent — the best month of 2026, with national television up 36 percent.  First-half growth overall was around 4 percent.",
                    "What the tracker measures matters here.  It is built from actual media dollars processed through Guideline's agency pool, representing roughly 70 percent of the major agency holding companies.  That means it largely misses money booked directly with platforms, which is where a great deal of social, retail media and creator spend now lives.",
                ],
                "so_what": "The step down from 19.3 to 11.9 percent is the World Cup comparison starting to wear off, not demand softening.  The tournament pulled national television money forward and none of it repeats.  The 4 percent first-half figure is the honest baseline.",
                "do_this": "Set your Q4 growth assumptions off the 4 percent first-half number rather than the summer prints, and label any use of this figure as agency-booked spend only when you put it in front of a client.",
            },
        ],
    },
    {
        "id": "format", "name": "FORMAT LAB", "page": "pg. 08",
        "note": "how the work is actually being made",
        "tint": None,
        "items": [
            {
                "title": "One brand bought 104 million views.  Another bought sixteen videos and 75,000.",
                "hook": "Two opposite bets landed in the same weekly chart, and the small one is the more interesting experiment.",
                "open": True,
                "stamps": [("TUBEFILTER · 31 AUG", "https://www.tubefilter.com/2026/08/31/top-5-branded-videos-mrbeast-alans-universe-amanda-pulitano-cyra-riley/")],
                "body": [
                    "The weekly branded video chart is worth reading sideways.  At the top, MrBeast at 103,995,201 views with three brands attached.  Second, Alan's Universe doing Back to School with Walmart at 24,412,144.  Walmart also hedged across three much smaller creators in the same week.",
                    "Then the interesting one.  Rocket Money paid for sixteen videos in a single week across a spread of unrelated niches, and shows up in the chart at rank 2,163 with 75,007 views.  That is the exact opposite bet to the blockbuster: many small, cheap, audience-diverse integrations instead of one enormous one.  Neither approach is obviously right, but only one of them lets you find out which niches convert.",
                    "Third and fourth in the chart are worth a note for anyone briefing beauty creators this autumn.  Amanda Pulitano for OUAI at 19,240,198 and Cyra Riley for Dermstore at 11,487,656 won on the identical pitch — this saves you time, you do not need a ten-product routine.  Two unrelated companies, same message, same week, both in the top five.  Time saved is now a crowded lane rather than a difference.",
                ],
                "flagnote": "Chart data is from Gospel Stats, a single commercial provider, republished by Tubefilter as a snippet of its paid weekly report.",
                "so_what": "The blockbuster buys certainty about reach and nothing else.  Sixteen small integrations across different niches buys you a map — which audience actually clicks, at what cost, for a product like yours — and that map is worth more in the second quarter of doing it than any single big placement.  You cannot learn anything from one video.",
                "do_this": "Take ten percent of your next big creator budget and split it across eight to twelve small creators in genuinely different niches with identical creative direction, then compare cost per action by niche.  And if you are briefing beauty this autumn, change the message off time saved, because two of the top four videos last week already own it.",
            },
        ],
    },
]

FORECAST = [
    {
        "confidence": "LIKELY",
        "window": "by 31 October 2026",
        "headline": "Legacy sports bodies quietly slow down on creator tie-ups",
        "body": "The Callaway and Good Good collapse did not just cost one brand a partnership.  It cost the PGA Tour a six million dollar title sponsor and cost Golf Channel a season it had already filmed.  Institutions that lose money on somebody else's mistake do not write a memo about it, they just stop returning calls for a quarter.  Expect creator-led programming to get harder to sell into traditional sports rights holders through the autumn, and expect the ones who do sign to demand approval rights that look like broadcast standards.",
        "do": "If you have a creator format in front of a league, federation or traditional sports broadcaster, send them your content review process before they ask for it.",
    },
    {
        "confidence": "LIKELY",
        "window": "by 31 December 2026",
        "headline": "Google publishes more creative benchmarks in exactly this shape",
        "body": "The creative guidance page is a template: presence-based findings, clean percentages, no sample sizes, and a framing that puts creative at the centre of what an advertiser still controls.  That is a deliberate position, not an accident, and it follows from Google automating targeting and bidding.  Expect more of these — sound, pacing, faces, formats — with the same generosity about the numbers and the same silence about the method.",
        "do": "Start a running file of platform-published creative benchmarks with the date, the exact wording and what each one omits, so your team can cite them without over-claiming.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "by 31 March 2027",
        "headline": "Auction mechanics become a standard contract question in retail media",
        "body": "Whatever happens to the FTC case itself, a million advertisers have just learned that a complete dashboard and an understood pricing rule are different things.  Retail media networks are numerous, young and largely self-reported, and the ones that can answer plainly how their auction prices a winning bid will start saying so in pitches.  The rest will get asked.",
        "do": "Add a single line to your next media contract requiring the seller to state in writing how a winning bid is priced.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "by 30 November 2026",
        "headline": "Instagram's AI disclosure moves from profiles to individual posts",
        "body": "Labelling the account is the easy version, and it leaves an obvious hole: a real person's account posting fully synthetic content carries no label at all.  Meta has built the enforcement mechanism now — reduced reach for non-disclosure — and mechanisms of that kind get pointed at more things.  Post-level labelling is the natural next step and it lands directly on brand content.",
        "do": "Start recording, per asset, which parts of your output are AI-generated, so a post-level disclosure requirement is a lookup rather than an audit.",
    },
]

TLDR = [
    "Google published its own figures showing a human voice in a YouTube ad is worth 12 percent more conversions, against 3 percent for text overlay and 4 percent for an early brand appearance.  Put a voice track on your silent variants this week and price a voice session into every edit brief from now on.",
    "The FTC and 22 states allege Amazon charged advertisers their own full bid close to 80 percent of the time in 2024, up from 30 to 40 percent in 2021.  Re-baseline your Amazon cost-per-click assumptions on a pay-your-bid model before Q4 planning closes.",
    "The Callaway ad scored the lowest possible mark from a synthetic test panel in minutes, and nearly a third of human viewers found something offensive in it.  Name one brand-side person as pre-publication reviewer on every creator asset, and write takedown ownership into your next contract.",
    "Factor signed Serena Williams in June, before she announced her comeback, then turned the news into two ads, thirty stills and an hour of extra footage from a half-day shoot.  Rebuild your next shoot schedule around asset count rather than one hero deliverable.",
    "Gamescom's hours watched rose 27 percent while its peak audience fell 13.3 percent, because the number of channels carrying it went from 1,150 to 7,800.  Require peak and average concurrent viewers alongside hours watched in every livestream sponsorship report.",
    "Nielsen puts streaming at 48.2 percent of ad-supported US viewing on persons two and up, but 44.4 percent on adults 18 and over, the base most deals are written against.  Ask which population any share of viewing is measured on before you repeat it.",
    "Elevated Fabworks turned a free abandoned yacht into two videos worth a quarter of its five-year view count, and a sponsor already bought episode one at a 210,000-subscriber rate.  If you sell tools, marine gear or portable power, buy the whole restoration arc now rather than a single read.",
]

SHARE = [
    {
        "who": "JARED · CEO",
        "angle": "Complete reporting and understood pricing are two different things, and a million advertisers just found out the hard way.",
        "post": "The FTC says Amazon charged advertisers their own full winning bid close to 80% of the time in 2024. Not the runner-up price. Their own bid.\n\nAccording to the complaint filed Monday by the FTC and 22 state attorneys general, that went from 30-40% in 2021, to 70% in 2022, to roughly 80% in 2024. Over a million brands and sellers. Amazon calls the suit misguided and says advertisers were properly informed.\n\nWhat I keep coming back to is this. Every one of those advertisers had a dashboard the entire time. Spend, clicks, cost per click, return on ad spend, all reported accurately. None of the numbers were wrong.\n\nThe reporting was complete. The rule was invisible. Those turn out to be separate things, and most of us have spent a decade treating them as the same thing.\n\nIt is a fair argument for putting more money into video you own. Owned is slower, and in year one it costs more per view, and I am not going to pretend otherwise. But you can audit it. You know what a view cost because you paid for the thing that earned it.\n\nI do not think this ends the auction. Most of the industry's money will keep flowing through companies that run the auction and grade their own results. It just got harder to call that measurement.",
        "why": "It is the biggest number in the market this week and the reframe is one a sceptical client has not heard: their reporting was accurate the whole time and still told them nothing.",
    },
    {
        "who": "JAMES · CREATIVE DIRECTOR",
        "angle": "The Callaway ad was competently made.  Craft was never the variable, and admitting that is the uncomfortable part.",
        "post": "Nearly a third of people who saw the Callaway and Good Good ad said there was something offensive, unpleasant or disturbing about it. Shock scored eight times the testing norm.\n\nZappi ran the pulled ad past 150 AI synthetic respondents afterwards. It came back in minutes with the lowest possible score, one out of five, and a note recommending they soften the physical moment so it read as playful rather than awkward.\n\nI want to be honest about my own instinct here. If someone had proposed running a creator-made spot past a synthetic panel before it went live, I would have argued against it. Panels flatten things. They punish anything unfamiliar. I still believe that.\n\nIt is also not what happened here. This was not a brave idea that testing would have sanded down. It was a premise nobody stress-tested, going out under a brand that had approval rights and used them.\n\nZappi sells the testing product, so weigh the numbers accordingly. I cannot argue with the direction of them.\n\nThe uncomfortable version is that the ad is competently made. The lighting is fine. The edit is fine. The performances land the beat they were asked to land. And none of that was ever going to save it, because the thing that went wrong happened before anyone picked up a camera.",
        "why": "A creative director conceding that craft was not the variable, and naming the process instinct he would have got wrong, is a thing almost nobody posts.",
    },
    {
        "who": "LAWRY · LEAD VIDEO EDITOR",
        "angle": "Voice outperforms both visual levers combined, and it is the first thing stripped out of an edit for cost.",
        "post": "Google published its own numbers on YouTube ad creative this week. A human voice in the ad is worth 12% more conversions. Text overlay, 3%. Brand visible in the first five seconds, 4%.\n\nVoice beats the other two put together. Voice is also the first thing cut when a budget tightens.\n\nI understand why. A read means a booth, a performer, notes, and then a lock that has to be broken and redone for every language and every regional variant. Music beds and supers scale for nothing. Voice does not scale at all.\n\nBut watch what happens to a cut when the voice goes. With no read carrying the meaning, the picture has to carry it alone, so you start cutting faster to hold people. Six-frame shots. Two-frame flashes of the pack. It feels urgent on the timeline and it explains nothing. I have made that mistake and then watched it play in a room.\n\nThe other thing worth saying: the 12% is measuring presence, not performance. Nobody published a figure saying a great read beats an adequate one. A flat, unremarkable voice beats no voice.\n\n12% is not a huge number. It is also the cheapest of the three to fix, and half the time the audio is already sitting on a drive from the last shoot.",
        "why": "It is the lead story rewritten from inside the edit suite, with the specific mechanism nobody outside one would name — that removing the voiceover is what makes the cutting speed up.",
    },
]
