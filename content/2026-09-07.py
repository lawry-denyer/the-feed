# -*- coding: utf-8 -*-
"""Content for THE FEED — issue data only.  The render spec lives in build_feed.py."""

ISSUE = {
    "date_iso": "2026-09-07",
    "kicker": "Crux Media // Monday 7 September 2026",
    "tagline": "What brands did on YouTube yesterday, and whether it worked.",
    "pace": "STEADY",
    "next_drop": "Next drop: Tuesday, 06:30 MT",
}

LEAD = {
    "headline": "YOUTUBE PUBLISHES ONE VIEW COUNT AND PAYS ON ANOTHER, AND THE GAP IS 40 PERCENT",
    "deck": "Agentio measured more than 75,000 videos and found that six in ten public views also counted as engaged views.  The number under the video is not the number YouTube pays creators on, and only the creator can see the second one.  If you price a sponsorship off the public count, you are buying a number that has been quietly redefined.",
    "stamps": [
        ("TUBEFILTER · 4 SEP", "https://www.tubefilter.com/2026/09/04/youtubes-new-public-viewcounts-over-report-actual-engagement-by-40/"),
        ("AGENTIO · 4 SEP", "https://www.agentio.com/blog/youtube-new-view-count-60-engaged-view-rate"),
    ],
    "body": [
        "In August YouTube changed what makes a public view.  The counter now ticks the instant the first frame loads, rather than after roughly thirty seconds of somebody actually watching.  The number under the video went up.  Nothing about the watching changed.",
        "The creator advertising platform Agentio has now put a size on the gap.  Across more than 75,000 videos in its network, those videos pulled around <mark>549 million public views and 330 million engaged views</mark> — the metric YouTube itself uses for revenue sharing and Partner Programme eligibility.  Six in ten.  Agentio's framing is that public viewership overstates meaningful engagement by an average of 1.67x, or 40%.",
        "The interesting part is where the gap comes from, because it is not people clicking the wrong thing.  Feed surfaces — the homepage hover preview, autoplay, the recommended shelf — generate <mark>38% of all public views but only 20% of those become engaged views</mark>, and that single behaviour accounts for 77% of the entire gap.  Misclicks are about 15%.  So the missing views are mostly a video starting itself at somebody who never asked for it.",
        "It is not spread evenly, and this is the line that should change what you pay.  On channels under 50,000 subscribers the public count is overstated by <mark>85%</mark>.  On channels over 300,000 it is 49%.  The smaller the creator, the more inflated the number you are negotiating against — which is precisely backwards from how most brands assume the risk sits.  By subject, education holds up best at a 63% engaged rate and technology worst at 46%.",
        "Agentio's own conclusion is blunt: a brand pricing a creator partnership off public views is likely overpaying by 67%, and a thirty dollar cost to reach a thousand people becomes an effective fifty once you count only engaged views.  That is a vendor talking its book, and you should read it that way.  The direction of the finding is still hard to argue with.",
        "Here is the structural problem underneath all of it.  Engaged views live inside the creator's own analytics.  You cannot look them up, your agency cannot look them up, and no third party audits them.  The only two ways to see the real number are to ask the creator to show you, or to buy through a platform with permissioned access to their channel.  Everything else is you pricing off a figure that YouTube redefined in August without telling the people spending the money.",
    ],
    "numbers": [
        ("40%", "average gap between public and engaged views — Agentio, 75,000+ videos"),
        ("85%", "overstatement on channels under 50,000 subs, against 49% over 300,000"),
        ("77%", "of the gap comes from autoplay and feed surfaces, not misclicks"),
    ],
    "flagnote": "Agentio sells brands access to creator ad inventory using permissioned channel data, so a finding that public view counts are unreliable flatters its own product.  The sample is its own network, not a YouTube disclosure, and YouTube has published no engaged-view benchmark of its own.",
    "so_what": "The number you negotiate on and the number YouTube pays on have quietly separated, and only one side of the table can see both.  Autoplay is doing most of the damage, which means the inflation is worst on channels whose videos get pushed at people rather than chosen by them.  Small creators are the most overstated, so the cheap end of your roster is where you are overpaying hardest.",
    "do_this": "Add one line to every creator proposal you are reviewing this week: ask for a screen recording of the engaged views figure from their own analytics on their last five sponsored videos, and price the deal off that.  Any creator who will not show you the number has told you what it says.",
}

SECTIONS = [
    {
        "id": "ws", "name": "W'S", "page": "pg. 02",
        "note": "what worked, and the exact reason it worked",
        "tint": "blue",
        "items": [
            {
                "title": "Agencies started picking creators on whether a chatbot will quote them, and long-form is winning",
                "hook": "The asset everyone is defunding is the one the machines actually read.",
                "open": True,
                "stamps": [("DIGIDAY · 4 SEP", "https://digiday.com/marketing/future-of-marketing-brands-want-creators-who-can-win-over-humans-and-machines-at-once/")],
                "body": [
                    "Something moved in the creator brief over the summer and almost nobody announced it.  Agencies are now scoring creators partly on whether an AI assistant will cite them when somebody asks it what to buy.  Tinuiti told Digiday that six to eight months ago AI visibility was maybe a tenth of what it weighed when building a creator strategy.  It is now closer to a quarter, and clients raise it across <mark>about 60% of the agency's roster</mark>.",
                    "The finding that matters is which format gets quoted.  Lauren Lyster, who heads social at Go Fish Digital, put it plainly: what gets cited is a lot more long-form information, and that outperforms Shorts, which do not often get cited very often in AI data.  Long, spoken, indexable video is what the models can read.  Nine seconds of vertical with a trending sound is not.",
                    "Ogilvy already has a handful of clients setting explicit targets around discoverability and credibility rather than views.  Nobody is charging for it yet — Digiday reports rate cards have not moved, and creators are folding citations into media kits to stand out rather than to raise their price.",
                    "Keep the scale honest, though.  Digiday's own numbers put OpenAI's advertising at a one billion dollar annualised run rate, but only 23% of American shoppers currently rank AI assistants among their trusted sources for shopping.  This is not a settled buying surface.  It is a cheap option on one.",
                ],
                "so_what": "For two years the whole industry has been shovelling creator money into short vertical video.  If AI answers become a real discovery route, the thing that shows up in them is the long-form video everyone stopped funding, and right now nobody is charging a premium for it.  That is a rare window where the useful asset is also the cheap one.",
                "do_this": "Put one long-form asset back into every creator brief you write this month — a full spoken review or explainer, not a cutdown — and ask your agency to check what ChatGPT and Gemini currently say about your brand and which sources they name.",
            },
            {
                "title": "E.l.f. held 64,000 people for eight minutes each with a ten-foot pickle jar at a state fair",
                "hook": "Eight minutes of attention.  No media buy behind it.",
                "stamps": [("MODERN RETAIL · 3 SEP", "https://www.modernretail.co/marketing/state-fairs-are-the-hot-new-spot-for-pop-ups-by-brands-like-e-l-f-and-levis/")],
                "body": [
                    "E.l.f. ran a pop-up at the Minnesota State Fair from 27 to 30 August built around three pickle-flavoured lip balm shades, with a ten-foot-tall pickle jar in the middle of it.  Nearly <mark>64,000 attendees passed through over four days, with an average dwell time of eight minutes</mark>.  Over 200 influencers turned up across the four days.  Organisers say it was the first time in at least twenty years a beauty brand had shown up at the fair.",
                    "The product proof came earlier: E.l.f. first released a pickle lip balm as a limited edition in February and it sold out within eight minutes.",
                    "The reason a state fair works is footfall nobody is bidding against.  Jennifer Schuder, senior vice president of customer engagement for the State Fair of Texas, gave Modern Retail the maths: between 2.3 and 2.5 million visitors a year, and if you average that over 24 days, you can think about it as a Super Bowl a day.  Minnesota drew 1,940,869 visitors over twelve days last year.  Texas drew 2,020,064 in 2025.",
                    "And the flavour was not a creative flourish.  Nearly 2.1 million pickle chips get eaten at the Minnesota fair each year, according to the fair itself.  The brand built its object out of the thing the audience was already queueing for.  Levi's is doing the same trick in Texas from 25 September, making a custom pair of jeans for Big Tex, the 55-foot cowboy statue that is the fair's mascot.",
                ],
                "flagnote": "The 64,000 attendees and the eight-minute dwell time carry no attribution in Modern Retail's piece and are figures only E.l.f. could have measured.  Treat them as brand-supplied.  The fair attendance and pickle chip numbers come from the fair organisers, who sell the sponsorships.",
                "so_what": "Eight minutes is not a comparable number to a video view and you should not pretend it is.  But it is eight minutes of a person standing in front of your product because they chose to walk over, on a day they had already decided to spend taking photographs.  The expensive part of most campaigns is renting attention.  This one bought a location where the attention was already assembled and pointing a camera.",
                "do_this": "Look at your next twelve months and find the one dated event where your customers already gather and already film — a fair, a race, a move-in week, a convention — and move the budget for one social burst into building a physical object there that is worth photographing.",
            },
        ],
    },
    {
        "id": "ls", "name": "L'S", "page": "pg. 03",
        "note": "what broke, and the failure mode behind it",
        "tint": "pink",
        "items": [
            {
                "title": "Wrong diagnosis: leggings fell 20 percent, and the answer is more marketing",
                "hook": "The chief financial officer named social commentary as the cause.  The analysts did not buy it.",
                "stamps": [("MODERN RETAIL · 3 SEP", "https://www.modernretail.co/operations/lululemons-identity-crisis-continues-with-comp-sales-down-9-as-it-prepares-to-welcome-new-ceo/")],
                "body": [
                    "Lululemon's second quarter: net revenue down 4% year over year, comparable sales down 9%, comparable sales in the Americas down 12%, gross profit 1.5 billion dollars and down 1%.  The number that tells you what is actually wrong is that <mark>sales of leggings were down 20%</mark>.  That is the core product.  That is the thing the company is for.",
                    "Meghan Frank, the chief financial officer and interim co-chief executive, told the call that as they moved into the second quarter they faced negative commentary in the media and social channels.  In the first quarter revenue had been 2.47 billion dollars and up 4%.  So the story is that a good quarter met a bad conversation.",
                    "The response is to increase marketing investment in the second half of the year and push harder on the styles that are working.  Which is a media answer to a question the analysts think is about product.  Neil Saunders at GlobalData: things have gone from bad to worse, and an incredibly boring assortment, too much non-core product that misses on both fashionability and style, and an absence of good technical innovation have all contributed to a rapid loss of brand heat.",
                    "Wells Fargo's Ike Borochuw pushed on the cost side and said the underperformance does not feel like it has been fully diagnosed yet.  Heidi O'Neill, who ran the direct-to-consumer business at Nike, takes over as chief executive tomorrow.",
                ],
                "so_what": "When the core product falls a fifth and the plan is to spend more on marketing, the marketing has been handed a job it cannot do.  No film fixes an assortment.  What it does is buy reach for the thing that is not selling, which is how a bad quarter turns into a bad year with a bigger invoice attached.",
                "do_this": "Before you accept your next brief, ask the person signing it what changed in the product or the price in the last two quarters.  If the honest answer is nothing, put that sentence in writing at the top of the plan so the campaign is not later blamed for a problem it was never given the tools to solve.",
            },
            {
                "title": "Wrong owner: the machines wrote this brand's story out of its sponsorship deals",
                "hook": "Twenty orders from ChatGPT in thirty days, and a brand description nobody at the company approved.",
                "stamps": [("GLOSSY · 7 SEP", "https://www.glossy.co/fashion/aviator-nation-shopify-ai-shopping-shop-app/")],
                "body": [
                    "Aviator Nation went looking for what AI shopping was actually delivering and came back with a number worth reading before anybody signs a plan built on it.  Over the last thirty days the brand saw <mark>around 20 orders come through ChatGPT</mark>, according to Curtis Ulrich, its director of e-commerce.  Against total volume he called that fairly insignificant.  His position is still to prepare for a future where it is dominant, which is the sane read.",
                    "The genuinely useful finding is what happened when they audited how the models described them.  Much of the public information the AI tools had picked up centred on the brand's partnerships, including its Major League Baseball and music festival collaborations.  Ulrich's line: what we uncovered was that it was not telling the brand's story exactly as we felt it in our hearts and minds.",
                    "Meanwhile the channel that is working is unglamorous.  Shopify's Shop app is 3 to 5% of the brand's total revenue but its fastest-growing channel, up around 30% year to date.  Shop's head of growth Jess Jacobs says almost 50% of the time a purchase in the app is a user buying from a brand for the first time.",
                    "Shopify's own platform-wide figures are the ones getting quoted in every deck right now: AI-referred traffic to its stores grew more than eight times year over year in the first quarter of 2026, and AI-referred orders carried 14% higher average order values than organic search.  Eight times a very small number is still a small number, and Aviator Nation's twenty orders is what that looks like on the ground.",
                ],
                "so_what": "A model describing your brand is summarising whatever you published most of.  Aviator Nation made a lot of content about its partnerships, so the machines decided the partnerships are the brand.  You do not get to write that description directly, and nobody at the company noticed it had been written until they went and looked.",
                "do_this": "Ask ChatGPT, Gemini and Perplexity to describe your brand and to name their sources, then compare the answer to your own positioning line.  Wherever it is wrong, the fix is publishing long-form text and spoken video that says the true thing plainly, because that is what these systems read.",
            },
        ],
    },
    {
        "id": "moves", "name": "MOVES", "page": "pg. 04",
        "note": "deals, launches and rule changes worth knowing about",
        "tint": None,
        "items": [
            {
                "title": "YouTube now estimates how many people are on the sofa, and only the creator can see it",
                "hook": "A new metric that multiplies your reach, invented by a model, audited by nobody.",
                "stamps": [("PPC LAND · 5 SEP", "https://ppc.land/youtube-estimates-three-tv-viewers-where-analytics-counted-one-device/")],
                "body": [
                    "YouTube has added a metric called views (co-viewed) that estimates the total number of people watching on a TV set rather than counting each television as one view.  Three people on a sofa can now register as three.  Rene Ritchie announced it on Creator Insider on Friday.  It sits in the advanced mode of the creator's own analytics.",
                    "Two things to hold onto.  It is modelled, not observed — YouTube uses statistical modelling based on demographic patterns, video genre and viewing times to predict when people are watching together, and it has not said what else goes into that.  And it changes no money at all: revenue sharing, AdSense payouts and Partner Programme eligibility all still run on engaged views and qualified views.  The rationale is scale, with YouTube reporting over one billion hours of viewing on television screens every day.",
                ],
                "so_what": "In one week you got a study showing public view counts overstate engagement by 40%, and a new private metric that multiplies the TV portion of a creator's audience by household size.  Both numbers live where the buyer cannot check them.  Expect the second one to start appearing in rate cards long before anyone agrees how to audit it.",
                "do_this": "Write one sentence into your creator contract template this week: fees are set on engaged views, and modelled or estimated audience figures are not an accepted basis for pricing.  Do it before the first co-viewed screenshot lands in a negotiation.",
            },
            {
                "title": "Google is switching on personalised targeting for alcohol ads on YouTube",
                "hook": "A whole category that treated YouTube as inefficient gets an eight-week runway.",
                "stamps": [
                    ("GOOGLE ADS POLICY · 3 SEP", "https://support.google.com/adspolicy/answer/17598957?hl=en"),
                    ("TUBEFILTER · 4 SEP", "https://www.tubefilter.com/2026/09/04/google-ads-youtube-alcohol-content-personalization/"),
                ],
                "body": [
                    "From <mark>30 October</mark> Google will allow personalised ads on YouTube inventory for alcohol advertising, including alcohol-related products and alcohol alternative beverages.  Personalisation for those categories had been switched off on YouTube entirely.  Egypt, India, Indonesia and Poland are carved out at launch.",
                    "The guardrails stay: age restrictions to keep the ads away from minors, the user's own ad controls, and a continuing ban on using health-related data to target alcohol.  Google's stated reasoning is customer interest, emerging categories and improved controls.  Tubefilter reads it partly as a response to TikTok, where age verification has already let drinks brands run creator campaigns.",
                ],
                "so_what": "Drinks brands have spent years treating YouTube as a place you buy blunt reach because you could not do anything else.  That constraint lifts in eight weeks, which means audience lists, exclusions and creative variants that were pointless in September become the whole plan in November.",
                "do_this": "If you work with a drinks brand, book the planning session this month rather than in late October — build the audience segments and the creative variants now, and get responsible-marketing sign-off on personalised targeting before the switch flips.",
            },
            {
                "title": "X shut its creator revenue share today and opens a replacement tomorrow",
                "hook": "The subsidy under a lot of talent's X output ended this morning.",
                "stamps": [("X HELP CENTRE", "https://help.x.com/en/using-x/creator-revenue-sharing")],
                "body": [
                    "Creator Revenue Sharing, the ad-revenue split, closes today, 7 September.  Existing members get a final payout for earnings through today and can apply from tomorrow to the Original Content Rewards Program if they clear its bar.  The new scheme pays on qualified impressions from Premium subscribers rather than on ad revenue, and explicitly excludes content that is copied, reuploaded without authorship, automated, or reposted with only minor edits.  Payouts run fortnightly with a thirty dollar minimum.",
                    "Worth knowing before you advise anyone: X's own help page and the secondary coverage give different eligibility thresholds.  Check the help page, not the write-ups.",
                ],
                "so_what": "A slice of what creators earned on X was ad revenue share, and that stopped this morning.  The replacement pays only for original work, which kills the repost-and-lightly-edit economy that a lot of branded content quietly relied on for distribution there.",
                "do_this": "If any of your talent was posting to X partly because the platform paid them, ask them this week what their rate becomes without it, and brief X-native original cuts rather than reposting the same asset you ran everywhere else.",
            },
            {
                "title": "A second lawsuit argues that the sponsor read in a video is an ad",
                "hook": "Two suits in weeks, both aimed at the format most brand money on YouTube actually buys.",
                "stamps": [("DEXERTO · 4 SEP", "https://www.dexerto.com/youtube/youtube-faces-second-class-action-lawsuit-over-ad-free-premium-claims-sponsored-content-3405920/")],
                "body": [
                    "Three Canadian subscribers filed a proposed class action in the Supreme Court of British Columbia on 21 August against Google and YouTube, arguing that Premium is not ad-free because creator-embedded sponsorships are functionally advertising.  Their line, reported via Courthouse News: although the source and delivery mechanism of the advertisements changed, the commercial interruption experienced by subscribers remained substantially the same.",
                    "They want restitution and an injunction against marketing Premium as ad-free without disclosing creator sponsorships.  It follows a July suit in California that cited sponsored segments in videos from Theo Von, Kallmekris and Markiplier.",
                ],
                "flagnote": "Single-source reporting: Dexerto, citing Courthouse News.  No ruling has been made and neither suit has been certified as a class action.",
                "so_what": "Nobody is going to lose Premium over this.  What is being tested is whether the in-video sponsor read has to be labelled and disclosed to a subscriber who paid to avoid ads — and that read is the single most common thing a brand buys on YouTube.  Combine it with Friday's automated disclosure labelling and the direction is one way.",
                "do_this": "Make sure every sponsor segment you commission is declared as paid promotion at upload, without exception and including gifted product, so a future disclosure rule finds your back catalogue already compliant.",
            },
        ],
    },
    {
        "id": "onstream", "name": "ON STREAM", "page": "pg. 05",
        "note": "the live numbers, and what they are actually worth",
        "tint": None,
        "items": [
            {
                "title": "The biggest live audience of the weekend had no sponsor on it at all",
                "hook": "1.3 million viewers, 33 million euros, 354 channels, zero brands.",
                "open": True,
                "stamps": [
                    ("STREAMS CHARTS · 7 SEP", "https://streamscharts.com/news/z-event-2026-recap"),
                    ("TEAM AAA · 7 SEP", "https://www.team-aaa.com/fr/actualite/zevent-2026-la-10eme-et-ultime-edition-sacheve-sur-une-cagnotte-de-32-8-millions-deuros_137039"),
                ],
                "body": [
                    "ZEvent, the French charity marathon, ran its tenth and final edition from Thursday to Sunday night.  Streams Charts has it peaking at <mark>1.3 million viewers</mark> across 354 broadcasting channels, the second-highest in the event's history and short of its own record by 4,600 concurrent viewers, with 26.18 million hours watched, which is a series record.  It raised 32,891,874 euros, more than double last year's 16,658,660.  Ten editions have now raised 90,984,628 euros.",
                    "Now the part that matters if you are thinking about buying anything like this.  That 1.3 million is a sum of 354 channels at one moment, not one broadcast.  The largest single stream in it was Mastu at almost 477,000 peak, with ZeratoR at 370,400.  So the headline audience is roughly three times the biggest individual channel in it.",
                    "For a sense of what a single feed does: the Dota 2 International grand final peaked at 1,796,267 in August, on one broadcast, on one night.  Last year's ZEvent peaked at 784,599 with over 330 channels.  The audience grew about 66% year on year while the money doubled.",
                    "There was no title sponsor and no product placement.  Revenue was donations and merchandise.  The most-watched thing on the internet this weekend was assembled out of 354 people turning their own cameras on for the same cause, and nobody bought a logo on it.",
                ],
                "numbers": [
                    ("1.3M", "peak viewers across 354 channels — Streams Charts"),
                    ("26.18M", "hours watched, a record across ten editions"),
                    ("477K", "peak on the single biggest channel in it"),
                ],
                "flagnote": "The peak is an aggregate across 354 simultaneous channels and is not comparable to a single-channel record.  Streams Charts published no average concurrent figure; the community tracker zevent-stats puts the cumulative peak at 1,180,767 and the average at 284,679, roughly 10% below the Streams Charts peak on a different method.  Do not mix the two.",
                "so_what": "A multi-streamer event manufactures a number no single channel can reach, by adding up small simultaneous audiences.  That is a real audience, but it is 354 rooms rather than one, so a logo on the main feed reaches a fraction of what the headline implies.  The value in this shape of event is the roster, not the hero.",
                "do_this": "When you next price a multi-streamer event, ask for the peak on the individual channels you would actually appear on rather than the event total, and buy a spread of mid-sized streamers instead of the top one.",
            },
        ],
    },
    {
        "id": "watch", "name": "ONE TO WATCH", "page": "pg. 06",
        "note": "one creator with momentum, and who should be calling them",
        "tint": None,
        "items": [
            {
                "title": "Adam Stew bought an island, and did three times his career best in eleven days",
                "hook": "221,000 subscribers.  2.46 million views.  A camping channel that just became a build series.",
                "open": True,
                "stamps": [("YOUTUBE CHANNEL", "https://www.youtube.com/@AdamStew")],
                "body": [
                    "Adam Stew is a Canadian outdoors channel with 221,000 subscribers, built on winter camping at temperatures down to minus forty, an off-grid cabin and a 1,300 dollar camper he bought off Facebook Marketplace.  For most of this year it did between 30,000 and 150,000 views a video.  The median of his last ten long-form uploads is 53,363.",
                    "Then the format changed on a date you can point at.  On 31 July he posted a video about finding a tiny island for sale and asking whether to buy it, which did 326,256.  On 27 August he posted the answer.  <mark>I Bought a Tiny Off-Grid Cabin on a Remote Island has done 2,465,043 views in eleven days</mark> — three times his previous best ever, which took seven months to get there, and roughly forty-six times his own median.",
                    "The mechanic is not complicated and it is the whole reason this is worth a call.  A camping channel makes one trip per video and each one starts from zero.  A property build makes a story with an unfinished middle, so every upload has a reason to exist and an audience that has to come back to see it.  He has just turned a series of episodes into a serial.",
                    "He already runs gear deals — his videos have carried dog food, outdoor clothing, portable power and watches.  What he does not appear to have is an agent, a press profile or a rate card that has caught up with a 2.4 million view video.",
                ],
                "watch": {
                    "label": "TOP VIDEO, LAST 3 MONTHS",
                    "title": "I Bought a Tiny Off-Grid Cabin on a Remote Island",
                    "url": "https://www.youtube.com/watch?v=KmORyWp1G4A",
                    "meta": "2,465,043 views · published 27 August 2026 · 35m 09s",
                    "note": "The purchase video that pays off the island he scouted a month earlier, and the moment his channel stopped being about trips.",
                },
                "flagnote": "No publication has covered this channel.  The subscriber count, view counts and the comparison against his own back catalogue were read from the channel's public feed and YouTube's own video data on 7 September, not from a third-party tracker.",
                "so_what": "An island build is months of episodes where the gear is not a mention, it is the thing making the story possible.  Nobody can construct a cabin on a remote island without power, tools, boats and warm clothing on camera, so the products carry narrative weight rather than sitting in a thirty-second read.  And he is priced against a channel that was doing 50,000 views a month ago.",
                "do_this": "If you sell portable power, satellite internet, workwear, cordless tools or boat kit, email him this week and buy the series rather than a video — a multi-episode build integration signed before the next upload, at rates set against his back catalogue rather than that 2.4 million.",
            },
        ],
    },
    {
        "id": "money", "name": "THE MONEY", "page": "pg. 07",
        "note": "where the budget actually moved",
        "tint": None,
        "items": [
            {
                "title": "TikTok took the back-to-school money, and the lift is new advertisers rather than bigger budgets",
                "hook": "TikTok up as much as 41 percent.  YouTube up 6.",
                "stamps": [("DIGIDAY · 7 SEP", "https://digiday.com/media-buying/media-buying-briefing-back-to-school-brand-spending-on-tiktok-rises/")],
                "body": [
                    "Digiday's Monday briefing has the numbers with an agency attached to each one, which is what makes them usable.  Tinuiti says TikTok spend across July and August was up about 20% year over year, and TikTok's share of its clients' overall social spending rose 55% between July and August.  Go Fish Digital reports TikTok spending up 41% year on year among its brand clients.",
                    "The number that explains the shape of it: the count of advertisers using TikTok during back-to-school rose <mark>160%</mark>.  That is not incumbents bidding harder.  That is new companies arriving.",
                    "And they arrived because search got expensive.  Go Fish puts search ad spend up 16% in August with Google search costs up around 20%, so budget rotated sideways into cheaper inventory.  Over the same summer months, YouTube spending rose 6%, according to Open Influence.",
                    "The commerce demand underneath it is real enough: NielsenIQ has TikTok Shop sales up 84% between March 2025 and February 2026, making it the fourth largest American health and beauty retailer by annual sales, and eMarketer forecasts a further 48% rise across 2026.  PwC puts typical back-to-school spending at 922 dollars with 47% of households expecting to spend more.",
                ],
                "so_what": "Six percent against twenty to forty-one is a gap worth understanding before somebody in a meeting uses it as evidence that YouTube is losing.  A lot of this money moved because search prices went up, not because TikTok outperformed.  Price-driven migration comes back when the price changes.",
                "do_this": "Ask your buyers to split the last quarter's social increases into what moved for measured performance and what moved because search inflated, and hold the performance-driven share as the only number worth planning next year against.",
            },
        ],
    },
    {
        "id": "format", "name": "FORMAT LAB", "page": "pg. 08",
        "note": "one format worth stealing this week",
        "tint": None,
        "items": [
            {
                "title": "Sheetz did not build a channel.  It rented the mechanics of one that already works",
                "hook": "Three episodes on First We Feast, and the winning dish goes on the menu.",
                "open": True,
                "stamps": [("AXIOS PITTSBURGH · 4 SEP", "https://www.axios.com/local/pittsburgh/2026/09/04/sheetz-first-we-feast-show-youtube")],
                "body": [
                    "The convenience chain Sheetz premiered a three-part series called Fuel Stop Feast on First We Feast, the channel that makes Hot Ones, on Friday, with weekly episodes through 18 September.  Adam Richman hosts.  Two chefs, Christian Alquiza and Ian Fujimoto, compete to build absurd dishes out of the ingredients already behind a Sheetz counter — a Lumberjack Breakfast Sandwich between waffles, a burger using pizza bagels as buns, tater bomb nachos.",
                    "Here is the part worth stealing.  The winning dishes go on sale in actual Sheetz stores.  So the video does not end when the view count stops.  It ends on a menu board, where the people who never watched it still meet the outcome, and the people who did watch it have a reason to drive somewhere.",
                    "Compare that with building a brand channel from zero, where you spend the first eighteen months teaching an audience that your channel exists.  First We Feast already has the format, the host language, the thumbnail grammar and the habit.  Sheetz bought the machine rather than the media.",
                ],
                "so_what": "The expensive part of brand-owned video is not the production, it is manufacturing the reason anyone returns.  An established creator franchise sells you that habit fully built, and a competition format sells you a result the business can act on.  A dish on a menu is a campaign with a physical ending.",
                "do_this": "Sketch one three-episode competition on a creator channel your customers already watch, where the winning entry becomes something you actually ship — a menu item, a colourway, a bundle — and price it against what a brand channel launch would cost you for the same year.",
            },
        ],
    },
]

FORECAST = [
    {
        "confidence": "LIKELY",
        "window": "by 31 October 2026",
        "headline": "Co-viewed numbers start showing up in rate cards",
        "body": "YouTube handed creators a metric that multiplies their television audience by an estimated household size, put it only in their own analytics, and attached no audit to it.  Creators are commercially rational.  Within weeks somebody will send you a deck with a co-viewed figure in it, presented as reach, and there will be no way for you to check it or for them to prove it.",
        "do": "Set your contract language on engaged views now, while nobody has an incentive to argue about it.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "by 31 December 2026",
        "headline": "Somebody publishes an engaged-view benchmark by subject and channel size",
        "body": "Agentio has just shown there is a 40% gap and that it varies from 46% to 63% depending on the subject and from 49% to 85% depending on channel size.  That is the first cut of a pricing table, published by a company that sells against it.  A measurement firm or a large agency with a wide enough view of the market has an obvious reason to publish a neutral version, and buyers now have an obvious reason to demand one.",
        "do": "Ask your measurement partner today whether they can report engaged views across your roster, so you are ready to use a benchmark the day one exists.",
    },
    {
        "confidence": "LIKELY",
        "window": "by 31 January 2027",
        "headline": "A drinks brand draws the first complaint over personalised alcohol targeting on YouTube",
        "body": "Personalisation switches on for alcohol on 30 October, in a category that regulators watch more closely than almost any other and where the whole objection has always been about who sees the ad rather than what it says.  The first campaign that gets a targeting choice wrong in public will set the tone for how cautiously everyone else builds their audiences.",
        "do": "If you plan alcohol campaigns, write your audience exclusion rules before your targeting rules, and get them signed off by someone who does not report to the marketing team.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "by 30 June 2027",
        "headline": "Creator rate cards grow a line for AI citation",
        "body": "Agencies told Digiday they expect pricing to reflect citation value in another six to twelve months, and that creators are already putting citations in their media kits without charging for them.  That is exactly what a metric looks like just before it gets priced.  The creators who can show they get quoted will move first, and long-form channels are the ones holding that card.",
        "do": "Lock multi-video deals with your best long-form creators now, at today's prices, with usage terms that run past the point where this gets priced.",
    },
]

TLDR = [
    "Public YouTube view counts overstate engaged views by 40% on average, and by 85% on channels under 50,000 subscribers.  Reprice every open creator proposal on engaged views and ask the creator to show you the figure from their own analytics.",
    "YouTube added a private, modelled metric that estimates how many people share a sofa in front of a TV.  Write into your contract template that fees are set on engaged views and estimated audience figures are not a pricing basis.",
    "Agencies now weigh whether AI assistants will quote a creator, and long-form gets cited where Shorts do not.  Keep one long-form asset in every creator brief this month and check what the chatbots currently say about your brand and who they cite.",
    "Lululemon's leggings sales fell 20% and the company is answering with more marketing spend in the second half.  Ask what changed in the product before you accept a brief that asks a campaign to fix a shelf.",
    "TikTok back-to-school spend rose 20 to 41% while YouTube rose 6%, and the lift came from a 160% increase in the number of advertisers pushed sideways by search inflation.  Split your own social increases into performance-driven and price-driven before planning next year.",
    "ZEvent's final edition peaked at 1.3 million viewers across 354 channels with no sponsor attached, while its biggest single channel peaked at 477,000.  Price multi-streamer events on the channels you would actually appear on, and buy the roster rather than the hero.",
    "Google switches on personalised targeting for alcohol ads on YouTube on 30 October, excluding Egypt, India, Indonesia and Poland.  Build the audience lists, exclusions and creative variants this month rather than in late October.",
]

SHARE = [
    {
        "who": "JARED · CEO",
        "angle": "The video format everyone is defunding is the one AI assistants actually quote.",
        "post": "Agencies have started picking creators on whether a chatbot will quote them. The format that gets quoted is long-form video. Shorts barely register.\n\nDigiday reported this on Friday. Tinuiti said that six to eight months ago, AI visibility was maybe a tenth of what it weighed when building a creator strategy. It's now closer to a quarter, and clients raise it across about 60% of its roster.\n\nLauren Lyster, who runs social at Go Fish Digital, put it plainly: what gets cited is long-form information, and it outperforms Shorts, which don't often get cited at all.\n\nSit with that for a second. The industry has spent two years moving creator money into short vertical video. If AI answers become a place people decide what to buy, the asset that turns up in them is the long one that everybody defunded.\n\nAnd nobody is charging for it yet. Digiday says rate cards haven't moved. Creators are putting citations in their media kits to stand out, not to raise their price.\n\nI'm not sure this becomes a real buying surface. Only 23% of American shoppers currently rank AI assistants among their trusted shopping sources, which is not a mandate.\n\nBut a long-form video works today regardless. If it also gets quoted in two years, you bought that for nothing.",
        "why": "It gives a sceptical client a concrete reason to fund long-form owned video that has nothing to do with view counts, and it is currently free.",
    },
    {
        "who": "JAMES · CREATIVE DIRECTOR",
        "angle": "The variable was the location, not the film — and the creative team was not in that meeting.",
        "post": "E.l.f. put 64,000 people through a pop-up in four days and held them for an average of eight minutes each. The creative was a ten-foot pickle jar at the Minnesota State Fair.\n\nEight minutes. I have spent weeks of my life arguing about whether a cut lands better at three seconds or five, and a jar held people for eight minutes.\n\nModern Retail ran the numbers on Wednesday. Jennifer Schuder at the State Fair of Texas describes her event as between 2.3 and 2.5 million visitors across 24 days — a Super Bowl a day, as she puts it.\n\nThe uncomfortable part for someone in my job: the decision that made this work was made before any creative brief existed. Somebody chose a place where people already gather with cameras out and already spend money on food. The pickle flavour wasn't a flourish either. Nearly 2.1 million pickle chips get eaten at that fair every year.\n\nThe idea followed the venue. Not the other way round.\n\nI'd rather tell you the concept did it. Over 200 influencers turned up, and the attendance and dwell figures are E.l.f.'s own, so treat them accordingly.\n\nBut nobody had to be paid to point a camera at that jar. That's the bit I can't argue with.",
        "why": "A creative director conceding that the media decision outperformed the creative one is unusual, specific and reads as honest.",
    },
    {
        "who": "LAWRY · LEAD VIDEO EDITOR",
        "angle": "YouTube just told editors the room has three people in it, and we are still cutting for one phone.",
        "post": "YouTube started estimating how many people are on the sofa rather than how many televisions are switched on. Three people watching together can now count as three.\n\nI have spent this year cutting everything for one person holding a phone about thirty centimetres from their face.\n\nThat assumption is baked into everything I do. Lower-third text sized for a six-inch screen, which turns into a smear across a living room. Dialogue mixed for earbuds, which vanishes the moment there's a kettle on and someone talking over the top of it. Cuts every two seconds, which reads as energetic on a phone and frantic on a 55-inch screen at the other end of a room.\n\nYouTube says people watch over a billion hours a day on television screens. I've known that number for a while. I hadn't changed a single technical habit because of it.\n\nWorth saying what the metric actually is. It's modelled, not measured — YouTube predicts co-viewing from demographics, genre and viewing time. Only the creator sees it. It doesn't change anyone's payment.\n\nSo I don't fully trust the number.\n\nI do believe the room. And I've been mixing for the wrong one.",
        "why": "It is a craft observation only someone in an edit suite would make, and it turns a metrics announcement into a technical brief.",
    },
]
