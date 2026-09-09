# -*- coding: utf-8 -*-
"""Content for THE FEED — issue data only.  The render spec lives in build_feed.py."""

ISSUE = {
    "date_iso": "2026-09-09",
    "kicker": "Crux Media // Wednesday 9 September 2026",
    "tagline": "What brands did on YouTube yesterday, and whether it worked.",
    "pace": "STEADY",
    "next_drop": "Next drop: Thursday, 06:30 MT",
}

LEAD = {
    "headline": "TWO BRANDS ENROLLED 21,365 CREATORS ON TIKTOK SHOP, SPENT MORE THAN TWO DOLLARS TO MAKE ONE, AND PUBLISHED THE RECEIPTS",
    "deck": "Swoveralls and DudeRobe ran the maximum-aggression TikTok Shop affiliate playbook for four months, then wrote up their own post-mortem with the ledger in it.  They spent 2.25 to 2.65 dollars for every dollar of sales the channel returned, before the cost of making the clothes.  Of 21,365 creators who joined, 38 produced 80% of the sales.  The genuinely useful part is what they say they kept.",
    "stamps": [
        ("NET INFLUENCER · 8 SEP", "https://www.netinfluencer.com/swoveralls-duderobe-spent-more-than-2-usd-for-every-1-usd-in-tiktok-shop-gmv-during-four-month-affiliate-push/"),
        ("THE GREAT FANTASTIC — FIELD REPORT", "https://thegreatfantastic.vercel.app/tiktok-shop-white-paper"),
        ("MARKETPLACE PULSE · 11 JUN", "https://www.marketplacepulse.com/articles/on-tiktok-shop-1-of-sellers-drive-60-of-gmv"),
    ],
    "body": [
        "Kyle Bergman, founder of Swoveralls and managing director of DudeRobe, and David Silverander, founder of the agency Kelson which runs growth and media for both brands, published a document called We Spent Six Figures on TikTok Shop.  Here Is What We Learned.  Net Influencer wrote it up yesterday.  It is the most detailed public account anyone has given of what a creator affiliate programme actually costs, and it was written by the people who lost the money.",
        "The ledger first.  Between April and July they shipped <mark>4,752 samples</mark> to creators and enrolled <mark>21,365 of them</mark>, on commissions of 12% to 20%, with five-figure incentive programmes and paid Shop Ads stacked on top.  Money out against money in: <mark>2.25 to 2.65 dollars spent for every 1.00 dollar of sales</mark>, before the cost of goods.  Roughly 5.6 million views.  Several thousand videos.  Just under 1,200 new customers, at a cost to acquire each one that ran about double their average order value.  The paid ads on top returned between 0.4 and 1.6 times their spend against a breakeven above 2.  Their best combined month reached about a quarter of the sales the model needed to wash its face.",
        "Now the shape of it, which is the part to carry into a meeting.  Of those 21,365 enrolled creators, <mark>38 accounted for 80% of affiliate sales and a single creator did roughly 30%</mark>.  About 99% generated no sales at all, and only around one in eight ever posted a shoppable video.  Every sample cost the low-to-high twenties in dollars to make and ship, and every sample returned less than that in sales.  So the recruiting was not building a salesforce.  It was buying lottery tickets at a fixed unit price and finding out which thirty-eight of twenty-one thousand were winners.",
        "There was a month that looked like it was working, and their write-up of it is the most honest paragraph in the document.  One brand posted roughly four times the previous month.  Then they looked closer — the spike was almost entirely ad-driven at a return still below breakeven, and the following month gave back about 70% of it the moment spend normalised.  Their words: it is a channel that hands you revenue at a loss while you pay for it and takes most of it back the moment you stop.",
        "Their own diagnosis is about price, and it is checkable.  TikTok Shop converts on things people buy mid-scroll without thinking, which they put at well under sixty dollars.  Swoveralls sell at 99 dollars, DudeRobe at 128.  They name their own error plainly: the brand that inspired the swing was Crocs, and that was the wrong comparison.  They also flag the other gap — the brands winning here subsidise the loss-making phase with nine-figure revenue or venture money, and these two are, by their own description, eight-figure and bootstrapped.  Across the four months the push consumed about a quarter of their total contribution margin, and twice it flipped an otherwise profitable brand-month into a loss.",
        "And this is the finding worth more than the loss.  The agency's verdict is that the strongest use of TikTok Shop for a brand like theirs is getting a large volume of creator content made, not chasing direct affiliate sales.  Their line on what they are keeping: creator content, licensed and run as paid media, consistently outperformed most of what they produce in-house.  They are shutting the volume sampling, holding a minimal storefront, and moving the thirty-eight who worked into direct deals with content licensing written in.",
        "One independent check on whether this is just two brands having a bad run.  Marketplace Pulse tracked nearly 100,000 American TikTok Shop sellers in June and found the <mark>top 1% take 60% of all sales while the bottom half take 0.1%</mark>.  Different measurement — sellers, not affiliates — but the same shape.  The platform does not flatten outcomes.  It sharpens them.",
    ],
    "numbers": [
        ("$2.25", "spent for every dollar of TikTok Shop sales, before the cost of goods"),
        ("38", "creators out of 21,365 who produced 80% of the affiliate sales"),
        ("79%", "higher combined operating profit the two brands say they would have made without it"),
    ],
    "flagnote": "This is a self-published field report by interested parties, and Net Influencer is the only outlet carrying it — no second publication, no analyst, no platform data.  Silverander's agency is the paid agency for both brands, so the operator is a co-author of the audit.  The authors state that the sample and creator counts are exact and everything else is a ratio or approximation from internal reporting.  The creator concentration table covers May to July while the spend figures cover April to July, so the two are not the same window.  They ran no controlled holdout, so the finding of no Amazon halo is a before-and-after comparison rather than a test, and they say so themselves.  The eight-figure revenue description is theirs and is not verifiable.",
    "so_what": "Almost every creator programme is bought as a sales channel and marked against sales, so when the sales do not arrive the whole line gets cut — including the part that was working.  These two separated the two jobs and found the content was worth paying for while the selling was not, at their price point.  That separation is the transferable finding, not the loss.  And the concentration number tells you the recruiting model is the wrong instinct: thirty-eight relationships you chose beat twenty-one thousand you enrolled.",
    "do_this": "Split your creator budget into two lines this week — one for content you license and run as paid media, one for sales attributed to creator links — and report them separately from the next campaign onward, so a failure in one cannot quietly kill the other.",
}

SECTIONS = [
    {
        "id": "ws", "name": "W'S", "page": "pg. 02",
        "note": "what worked, and the exact reason it worked",
        "tint": "blue",
        "items": [
            {
                "title": "Twitch's reward button pulled 1.6 billion hours, and the campaign count only rose a fifth",
                "hook": "40 million people claimed a Drop this year.  The hours grew more than twice as fast as the number of brands buying them.",
                "open": True,
                "stamps": [("TWITCH BLOG · 9 SEP", "https://blog.twitch.tv/en/2026/09/09/twitch-state-of-gaming-2026/")],
                "body": [
                    "Twitch published its State of Gaming report this morning.  Headline scale: <mark>8.6 billion hours of gaming watched between 1 January and 1 September</mark>, with the top five games accounting for about 1.7 billion of it.  Channels tagged indie were up 51% to more than 348 million hours.",
                    "The number a brand should read is further down.  Streams with Drops switched on generated <mark>1.6 billion hours, up 46% year on year</mark>.  That is close to a fifth of all gaming watch time on the platform.  A Drop, for anyone who has never bought one, is an in-game item a viewer earns by keeping a stream open for a set number of minutes — you buy the reward, not the ad slot.",
                    "Here is why the growth is interesting rather than just large.  <mark>More than 7,500 Drops campaigns ran, up only 20%</mark>, while channel participation rose 40% and the number of people claiming Drops rose 15% to 40 million.  So hours grew more than twice as fast as the number of brands buying in, because each campaign is now being carried by far more channels than it was last year.  The same money is reaching further, not because Twitch got bigger, but because more streamers opted in.",
                    "Mike Minton, chief product officer at Twitch, on the top line: 8.6 billion hours of gaming content watched in just eight months — and the GTA VI community showing up so big it broke the site — are powerful testaments to the strength of Twitch's gaming community.",
                    "One honest caveat before you buy on this.  Hours watched on a Drops-enabled stream credits the whole stream to the Drop.  It does not tell you how many minutes anyone spent looking at your brand, or whether they would have watched anyway.  It tells you the reward kept the tab open, which is a real thing to buy and a different thing from attention.",
                ],
                "flagnote": "These are Twitch's own first-party numbers with no third-party verification, published by the company that sells the inventory they make look attractive.  No average concurrent viewers, no per-campaign performance and no methodology beyond a stated global window of 1 January to 1 September 2026 against the same period last year.",
                "so_what": "Every other thing you can buy on a livestream interrupts the reason the viewer is there.  A Drop is the only one that gives them a reason to stay, which is why the hours grow faster than the number of buyers.  It also means your competitor's campaign is not competing with you for attention in the same stream — it is competing for the streamer's willingness to run it at all, and that queue is now 40% longer than last year.",
                "do_this": "If you sell anything with a digital counterpart — a skin, a code, a trial, a physical item with a claim number — brief a Drops campaign for Q4 now rather than a sponsorship, and book the channels early, because the number of streamers carrying Drops grew faster than the number of slots.",
            },
            {
                "title": "A machine is about to summarise your creator video, and the person it trusts most is the least polished one in your casting deck",
                "hook": "Everyday consumers 52%.  Professional reviewers 43.  Subject-matter experts 37.",
                "stamps": [("IAB · 9 SEP", "https://www.iab.com/news/consumers-want-ai-shopping-recommendations-to-include-trusted-creator-perspectives")],
                "body": [
                    "The IAB published research this morning on how people use AI assistants to decide what to buy.  <mark>72% use a general-purpose AI assistant for shopping decisions.  56% prefer recommendations that include creator perspectives, and 65% say they feel more confident when the answer draws on credible creator reviews.</mark>",
                    "The ranking underneath is the uncomfortable one for anyone who casts talent.  Asked which creators they trust in this context, people picked <mark>everyday consumers at 52%, professional reviewers at 43% and subject-matter experts at 37%</mark>.  The stated reasons run credibility 46%, consistency 40%, expertise 36%, and independence from brands with clear sponsorship disclosure 34%.",
                    "Among Gen Z, creator reviews inside an AI answer sit almost level with brand and advertiser information — 27% against 29%.  Half of Gen Z and millennials say they have found a creator through an AI tool in the first place.  By market, India and Mexico are the most receptive to creator input, the United States is the most receptive Western market and the United Kingdom the most cautious.",
                    "Jack Koch, senior vice president of research and insights at the IAB, gives the mechanism in one line: with AI shopping, consumers don't just want the recommendation.  They want real-world experience and expertise behind the guidance.",
                    "Think about what an assistant can actually lift out of a fourteen-minute review.  It can lift a sentence.  If nobody in your video ever says plainly whether the thing is good, and why, and who it is for, there is nothing for the summariser to quote — and the summariser is increasingly the last thing the buyer reads before deciding.",
                ],
                "flagnote": "The IAB released this in the week before it convenes its own first CreatorFronts, an event it is selling to the industry, so a finding that creator content is essential to AI shopping flatters what the IAB is convening.  Fieldwork was May 2026 through Attest — 2,200 people who had used an AI tool for shopping research in the previous three months, 1,000 in the United States and 300 each in the United Kingdom, Australia, Mexico and India.  All self-reported intent, not observed purchasing.",
                "so_what": "Casting for authority is the safe choice in a client room, and this says the audience discounts it — the ordinary person testing the thing outranks the credentialled expert by fifteen points.  Layered on top of that, an assistant now sits between your video and the buyer, and it can only pass along a verdict somebody actually stated.  A beautifully made review with no clear sentence in it survives the edit and dies in the summary.",
                "do_this": "Add one mandatory line to every creator brief this week — the creator states a plain verdict out loud, naming the product, saying whether it is good and who it is for — and put that same sentence in the video description and the pinned comment so a summariser has something to lift.",
            },
        ],
    },
    {
        "id": "ls", "name": "L'S", "page": "pg. 03",
        "note": "what broke, and the failure mode behind it",
        "tint": "pink",
        "items": [
            {
                "title": "Wrong owner: a golf YouTuber is owed 1.4 million dollars by a tour that filed for bankruptcy yesterday",
                "hook": "Sixteenth on the creditor list, ahead of two of the players.",
                "open": True,
                "stamps": [("DEXERTO · 9 SEP", "https://www.dexerto.com/youtube/liv-golf-bankruptcy-reveals-they-owe-1-4m-to-youtuber-rick-shiels-3407169/")],
                "body": [
                    "LIV Golf filed for bankruptcy protection in the United States on 8 September, with at least 45 million dollars owed to players including Jon Rahm, Bryson DeChambeau and Dustin Johnson.  Buried in the creditor list is <mark>Rick Shiels Media LTD, owed approximately 1.4 million dollars for a brand partnership agreement</mark>.",
                    "Shiels is a British golf coach with over three million YouTube subscribers, signed as a LIV ambassador in May 2025.  He sits <mark>16th on the list of the tour's largest creditors, ahead of the players Caleb Surratt and Joaquin Niemann</mark> — and Niemann won five times in the 2025 season.",
                    "The part that makes this a lesson rather than a misfortune is the sequencing.  Shiels took real audience damage when he signed; Dexerto reports fans walked away over it at the time.  He paid the reputational cost on day one, in public, in full.  The money was to arrive later, and the Saudi Public Investment Fund confirmed at the end of April that it would stop funding the tour after this season.",
                    "So a creator ambassadorship, structured this way, is an unsecured trade debt with a reputation posted as collateral up front.  There is no security, no escrow and no seniority.  Scott O'Neill, the tour's chief executive, says its future will be built around a sustainable business model and deeper alignment, which is the language of a restructuring, not of a payment.",
                ],
                "flagnote": "Dexerto is the only outlet to have pulled the creator line out of the filing.  Shiels has not commented publicly on the money owed, and the 1.4 million dollar figure is the amount listed in the filing rather than an amount confirmed by either party.",
                "so_what": "Every long ambassador deal you write asks a creator to spend their audience's goodwill now and trust you for the money later.  That trade only holds while the buyer is solvent, and creators have just watched what happens when it is not.  Expect the next round of negotiations to be about when you pay, not how much — and the brands that can pay early will start winning creators they could not previously afford.",
                "do_this": "Look at your own creator contracts this week and find out whether you pay in arrears.  Move the next ambassador deal to paying a meaningful chunk before the first post goes live, and use it in the pitch — it is a real advantage right now and it costs you nothing but timing.",
            },
            {
                "title": "Wrong sponsor: the copy was not the problem, the product was the copy",
                "hook": "A prediction-market ad has to turn whatever is in the news into a betting line.  Sometimes the news is a mistrial about two dead children.",
                "stamps": [("NET INFLUENCER · 8 SEP", "https://www.netinfluencer.com/podcaster-amanda-hirsch-apologizes-for-polymarket-ad-tied-to-lindsay-clancy-mistrial/")],
                "body": [
                    "On 4 September, the day a mistrial was declared in the Lindsay Clancy case, the podcaster Amanda Hirsch posted a paid Polymarket promotion noting the market had predicted a not-guilty verdict and asking her followers whether they were surprised, tagged as a partnership.  More than 161,000 dollars had been wagered on the outcome.",
                    "She deleted it.  Screenshots circulated.  She disabled comments on the post and on her stories, and on 6 September apologised, calling the content completely insensitive, wrong, and out of character for me, and adding that she became so consumed by the trial that she completely lost perspective.",
                    "The failure mode here is not judgment on one post, and treating it that way will lead you to the wrong fix.  A prediction market sells a wager on an outcome.  Its promotional copy therefore has to convert something currently in the news into a line you can bet on.  When the thing in the news is a trial concerning the deaths of two children, there is no version of that sentence that lands.  The brief was impossible before anyone wrote a word of it.",
                    "Prediction-market sponsorships are multiplying fast across podcasts and creator channels because the money is good and the read is short.  This is the first one to break in public in a way that names the structural problem rather than the execution.",
                ],
                "flagnote": "Single publication.  Polymarket is not quoted, no deal value is disclosed, and there is no audience or unfollow data.",
                "so_what": "Some sponsor categories carry a brief that cannot be made safe by good creative, because the product requires the copy to be about whatever is happening.  Betting, prediction markets and rapid-response news formats all sit there.  You cannot brief your way out of it, and the creator who signed is the one whose name is on the apology.",
                "do_this": "Before signing any prediction-market, betting or news-reactive sponsorship, agree a written exclusion list — criminal trials, deaths, disasters, health emergencies — and give the creator a standing right to skip a scheduled post without losing the fee.",
            },
        ],
    },
    {
        "id": "moves", "name": "MOVES", "page": "pg. 04",
        "note": "deals, launches and rule changes worth knowing about",
        "tint": None,
        "items": [
            {
                "title": "Weight Watchers is launching a podcast because most people do not know what it sells now",
                "hook": "63 years old, eight episodes, and the chief admission is an awareness problem.",
                "stamps": [("GLOSSY · 9 SEP", "https://www.glossy.co/beauty/wellness/wellness-briefing-weight-watchers-launches-the-weigh-in-podcast-with-dear-media-to-crush-glp-1-stigma-plus-news/")],
                "body": [
                    "Weight Watchers launches The Weigh In on 16 September with Dear Media — eight episodes of 45 to 60 minutes, hosted by Samhita Mukhopadhyay, its head of content and impact, who joined in March 2025 from The Meteor after editorial roles at Teen Vogue and Mic.  Guests include the stylist Erin Walsh, The Cut's editor-in-chief Lindsay Peoples and Julie Rice, the SoulCycle founder now on the Weight Watchers executive team.",
                    "Mukhopadhyay's stated reason for making it: when she arrived, a lot of media outlets were not sure how to cover the moment, and a big motivation was to insert the company into the wider conversation.  Glossy states plainly that the show is a marketing exercise for the company's telehealth, coaching and body-scanning products.",
                    "The line that explains the whole commission is her own: most people don't even know that we sell these.  This is not a brand building affection.  It is a 63-year-old company using a podcast to tell people what its product currently is, because its name says something it stopped only being years ago.",
                    "Mark Mullett, president of global entertainment and business development at Dear Media, on why it fits their slate: a lot of our wellness content does really, really well.  Our audience is leaning in.",
                ],
                "flagnote": "Announced the morning it ran, with the company's own content head as the only substantive source.  No budget, no episode-one date beyond 16 September, and no performance data of any kind exists yet.",
                "so_what": "A long-format show is a bad awareness tool and an excellent explanation tool, which makes it the right buy when your problem is that people have an out-of-date idea of what you sell.  The awareness gap here is the entire brief, and it is a gap a thirty-second spot cannot close because the thing that needs saying takes longer than thirty seconds.",
                "do_this": "Ask your client one question this week: what do customers think you sell that you no longer sell, or do not yet sell?  If the answer is substantial, brief a long-format series rather than a campaign, and judge it on whether people can correctly describe the product afterwards.",
            },
            {
                "title": "Modelo put 18 percent more behind college football, and the reason is an awareness number",
                "hook": "The chief executive's own words are that unaided awareness is remarkably low.",
                "stamps": [("MARKETING DIVE · 8 SEP", "https://www.marketingdive.com/news/modelo-hikes-marketing-spend-on-college-football-for-new-platform/829785/")],
                "body": [
                    "Modelo launched a new college football platform yesterday, It's Not Just Game Day.  It's Tradition, with a <mark>stated 18% year-on-year increase in media investment</mark>.  Three brand spots, distribution across Fox including Big Noon Kickoff and across ESPN, a presenting sponsorship of Barstool Sports' Mostly Sports, and co-branded merchandise with Homefield.  It is already the official beer of the College Football Playoff.",
                    "The pressure behind it is Michelob Ultra, and the diagnosis comes from the top.  Nicholas Fink, chief executive of Constellation Brands, has said unaided awareness is remarkably low — meaning that when you ask people to name beers without prompting, Modelo often is not one of them, despite the shelf position.",
                    "Worth noting where the money went inside the buy.  Broadcast for reach, then a presenting sponsorship of a podcast for the part broadcast cannot do — repeated, hours-long, in-jokes-and-all presence with the same audience week after week.  That is two different jobs bought in one platform.",
                ],
                "flagnote": "The 18% is a company-stated increase against an undisclosed base.  No spend figure, no impressions and no results — the season has just started.",
                "so_what": "Unaided awareness is the metric that separates a brand people buy from a brand people ask for, and it is one of the few problems where volume genuinely is the answer.  What is more interesting is the split: the broadcast buy gets them named, and the season-long podcast sponsorship gets them familiar.  Familiarity is the expensive half and it cannot be bought in a burst.",
                "do_this": "Find out your client's unaided awareness figure before your next brief — not aided, unaided — and if it is low, argue for one season-long presence with a single show rather than three short bursts across many.",
            },
            {
                "title": "Piers Morgan is spinning up a third show off one interview format, and the ad money is now someone else's problem",
                "hook": "11.5 million monthly podcast listens, 230 million monthly YouTube views, and a 27 million dollar round in June.",
                "stamps": [("NET INFLUENCER · 8 SEP", "https://www.netinfluencer.com/piers-morgan-launches-weekly-soccer-show-as-his-uncensored-youtube-slate-keeps-growing/")],
                "body": [
                    "Morgan announced Football Uncensored, a weekly debate show with Simon Jordan, the former Crystal Palace owner and TalkSPORT pundit.  It follows a summer run of World Cup Uncensored with John Terry which did a reported 60 million streams across social over 12 episodes, with close to a million views on the finale.",
                    "The network numbers behind it: <mark>11.5 million monthly podcast listens and 230 million monthly YouTube views</mark>, a chief executive in Rashida Jones, backers including Elisabeth Murdoch, and a 27 million dollar round in June.  In July, Acast bought Backyard Ventures for 20 million dollars, folding the network into an established advertising sales operation.",
                    "The structure is the thing to read, not the personality.  One proven interview format, then vertical spin-offs, each fronted by a co-host who brings a credentialled audience of his own — so the new show does not have to build an audience, it borrows two.  And the money comes through an acquired sales pipe rather than through platform revenue sharing.",
                ],
                "flagnote": "The 60 million streams figure is a company-supplied cross-platform aggregate rather than YouTube views, and the launch date for the new show is not stated.  Net Influencer is the only outlet carrying the announcement.",
                "so_what": "This is what a creator-owned network looks like once it stops being a channel: a format, a repeatable spin-off template, and an advertising sales team it does not have to build.  For anyone buying, it means the unit you negotiate for is increasingly a show inside a network rather than a person, which changes who you are actually talking to and what they can guarantee.",
                "do_this": "When you next buy a podcast or creator show, ask whether the sales rights sit with the creator or with a network, and get the answer in writing before you negotiate — it determines whether you can buy a season, a slot or nothing at all.",
            },
        ],
    },
    {
        "id": "onstream", "name": "ON STREAM", "page": "pg. 05",
        "note": "the live numbers, and what they are actually worth",
        "tint": None,
        "items": [
            {
                "title": "Z Event peaked at 1.3 million people across 354 channels, and the biggest single room held 28 percent of it",
                "hook": "Nearly 33 million euros raised in a weekend.  And a second event this week where hours watched went up while the audience went down.",
                "open": True,
                "stamps": [
                    ("STREAMS CHARTS · 7 SEP", "https://streamscharts.com/news/z-event-2026-recap"),
                    ("ESPORTS CHARTS · 8 SEP", "https://escharts.com/news/vct-2026-americas-stage-2-viewership"),
                ],
                "body": [
                    "Z Event, the French charity streaming marathon, ran its final edition from 3 to 6 September.  Streams Charts has it <mark>peaking at 1.3 million viewers with 26.18 million hours watched across 354 unique channels</mark>, raising 32,891,874 euros for 22 associations.  It is the second-highest peak in the event's history, 4,600 concurrent viewers short of the record.",
                    "The single-channel numbers are the ones that behave like something you could buy.  Mastu peaked around 477,000.  <mark>ZeratoR, who founded the event, peaked at 370,400 on his own channel</mark> — his best of the year, and about 28% of the aggregate.  Same pattern as every large distributed broadcast now: the event is enormous and no individual room holds much of it.",
                    "For scale against something recognisable: The International, Dota 2's world championship, peaked at 1,796,267 last month with an average of 590,958 across 109 hours of play.  Z Event reached roughly 72% of that peak over a single weekend.  Its 26.18 million hours is about 1.7% of everything watched on the whole of Twitch during August, which was 1.56 billion hours.",
                    "Streams Charts published no average concurrent viewers for Z Event.  Do not let anyone infer one from the hours — a marathon runs for days, so hours watched rises for reasons that have nothing to do with how many people were in the room.",
                    "Which brings us to a clean demonstration of that trap, published yesterday.  Esports Charts reported the VCT Americas Stage 2 finals: <mark>hours watched up 27.6% to 24.4 million, while average concurrent viewers fell 10.8%</mark>.  Peak was 522,800.  The event ran 165 hours and 40 minutes across 224 channels, itself up 27.2%.  So the hours grew because the broadcast got longer and wider, and the audience present at any given moment got smaller.  One metric, two events, opposite stories.",
                ],
                "numbers": [
                    ("1.3M", "peak viewers across the 354 channels showing Z Event 2026 — Streams Charts"),
                    ("370.4K", "peak on ZeratoR's own channel, about 28% of that total"),
                    ("26.18M", "hours watched, roughly 1.7% of everything watched on Twitch in August"),
                ],
                "flagnote": "Every peak here is aggregated across hundreds of channels and is not comparable to a single-channel record.  Streams Charts published no average concurrent viewers for Z Event, and Esports Charts gave only a percentage change for VCT rather than an absolute average, so neither audience figure can be independently reconstructed.",
                "so_what": "Hours watched is the number every rights holder leads with because it is the one that grows when you simply run longer or add more channels.  VCT proves that exactly: more airtime, more channels, more hours, fewer people actually watching.  Peak tells you how big the moment got, average tells you whether anyone stayed, and you need both before a livestream number means anything to you.",
                "do_this": "On every livestream figure you are shown this week, ask three questions before you react to it — peak, average concurrent, and how many channels it aggregates.  If the seller cannot give you the average, price the deal as if the audience left.",
            },
        ],
    },
    {
        "id": "watch", "name": "ONE TO WATCH", "page": "pg. 06",
        "note": "one creator with momentum, and who should be calling them",
        "tint": None,
        "items": [
            {
                "title": "Repair Geek tore an engine down twice over 20,000 miles, and gave Valvoline the best product demonstration of its year for nothing",
                "hook": "325,000 subscribers, a 1.25 million view breakout at six and a half times his median, and not a single sponsor on the channel.",
                "open": True,
                "stamps": [("YOUTUBE CHANNEL", "https://www.youtube.com/@RepairGeek")],
                "body": [
                    "Repair Geek is a one-man automotive testing channel with <mark>325,000 subscribers</mark>, read from YouTube this morning.  He buys competing products with his own money and settles arguments the aftermarket has been having for decades — brake pads, rust treatments, headlight bulbs, diesel additives, dash cameras, engine oil.  The median across his last ten long-form uploads is <mark>196,128 views</mark>.",
                    "On 28 August he posted a test of Valvoline Restore and Protect run over 20,000 miles.  He tore the engine down at the start to document a baseline, reassembled it, ran four oil changes on the product, sent used oil out for lab analysis, then tore the same engine down again to compare.  It has done <mark>1,249,634 views</mark> in twelve days — six and a half times his own median, and comfortably his biggest video ever against a previous ceiling of 735,624 in May.",
                    "The commercial detail that should make a brand pick up the phone: there is no sponsor.  Not on that video and not on the three before it.  He funds the tests himself and monetises through Amazon affiliate links and a paid consultation service.  He is also willing to be brutal — the description on his dash camera test names one major brand and tells you not to buy it.  That bluntness is the entire reason his verdict is worth anything, and it is why the format cannot be bought in the normal way.",
                    "Be honest about what the momentum is and is not.  His two biggest videos of all time are both from the last four months, so the format is proven and repeatable.  But his baseline is not rising — the median of his ten most recent long-form uploads sits slightly below the ten before them.  This is a record-breaking spike on a proven format, not a channel compounding.  That is exactly the moment to buy, and it will not read that way on a dashboard.",
                ],
                "watch": {
                    "label": "TOP VIDEO, LAST 3 MONTHS",
                    "title": "I Ran Valvoline Restore & Protect for 20,000 Miles, Then Tore Down the Engine",
                    "url": "https://www.youtube.com/watch?v=qe-ULbMuvJ4",
                    "meta": "1,249,634 views · published 28 August 2026 · 46m 14s",
                    "note": "A 16-month, 20,000-mile test with a teardown at both ends and lab analysis in the middle, carrying no sponsor at all.",
                },
                "flagnote": "No publication has covered this channel.  The subscriber count, the view counts and the median across his last ten long-form uploads were read from YouTube's own public data on 9 September rather than from a third-party tracker, and Shorts were excluded from the median.  The featured video link was confirmed to resolve.  Subscriber growth history could not be verified from any source, so no growth rate is claimed here.",
                "so_what": "Valvoline just received a million-view, lab-corroborated, teardown-proven demonstration of its product from someone with no relationship to it, which is the single most persuasive thing that exists in that category and cannot be produced by an agency.  The buyable version is not an advertisement.  It is funding the test — the vehicle time, the lab work, the teardown labour — with editorial independence written in, so the verdict stays worth reading.  A brand that will not risk a bad result should not call.",
                "do_this": "If you sell engine oil, additives, filtration, brake components, lighting or 12-volt accessories, email him this week and offer to fund a controlled test of your product against two named competitors, with the result published whatever it says and no approval rights — then buy the media behind whichever way it lands.",
            },
        ],
    },
    {
        "id": "money", "name": "THE MONEY", "page": "pg. 07",
        "note": "where the budget actually moved",
        "tint": None,
        "items": [
            {
                "title": "TikTok took the back-to-school money and YouTube still grew, because it is not the same money",
                "hook": "TikTok spend up 20% at one agency and 41% at another.  YouTube up 6%.  Nothing moved between them.",
                "open": True,
                "stamps": [("DIGIDAY · 7 SEP", "https://digiday.com/media-buying/media-buying-briefing-back-to-school-brand-spending-on-tiktok-rises/")],
                "body": [
                    "Three agencies gave Digiday their own client numbers for July and August.  Jack Johnston, vice president of social innovation and growth at Tinuiti: <mark>TikTok spend up about 20% year on year</mark>, and TikTok's share of his clients' total social spending up 55% between July and August alone.  David Dweck, president at Go Fish Digital: <mark>TikTok spend up 41% year on year, and the number of advertisers using it during back-to-school up 160%</mark>.  Aynsley Moffitt at Open Influence: YouTube spending rose 6% over the summer.",
                    "The obvious reading is that TikTok is taking YouTube's money, and Dweck's own explanation says otherwise.  His words: once they max spend on Amazon and Google, they want to start going into TikTok Shop, and a lot of our advertisers are trying to find white space.  This is the budget that appears after the two big performance channels are full, not budget moving out of video.",
                    "The scale underneath it is real.  NielsenIQ has TikTok Shop sales up 84% between March 2025 and February 2026, which makes it the fourth largest American retailer of health and beauty products by annual sales.  eMarketer estimates 48% sales growth across 2026.  Search spend rose 16% in August with Google search costs up 20%, which Dweck attributes partly to AI summaries shrinking the space available for advertising.",
                    "Hold this next to today's lead.  That is the tide the two brands in the lead were swimming in — a channel growing at 84% a year, an advertiser count up 160%, and a maximum-aggression affiliate model that still returned less than half of what they put into it.  Both things are true at once, and the second one is the one nobody publishes.",
                ],
                "flagnote": "Every percentage here describes one agency's own client base.  No sample sizes, no client names and no spend figures were given, and three agencies with different client mixes produced three different numbers.  Treat the direction as solid and the magnitudes as illustrative.",
                "so_what": "A channel growing this fast pulls budget in by looking like an opportunity rather than by beating anything on results, and the money arriving is incremental — the last money, spent by advertisers who have run out of room elsewhere.  Incremental money is the least disciplined money in the building, which is exactly why a public teardown of what it actually returns is worth more than another growth chart.",
                "do_this": "Before your next TikTok budget increase, write down which channel the money would otherwise have gone to.  If the honest answer is none, set the success measure at the start and a date to kill it, because incremental money never gets reviewed as hard as reallocated money.",
            },
            {
                "title": "YouTube gaming creators are charging 23 percent more than Twitch streamers, and nobody has explained why",
                "hook": "203 dollars against 165, from the same pool of buyers.",
                "stamps": [("TUBEFILTER · 8 SEP", "https://www.tubefilter.com/2026/09/08/collabstr-youtube-gaming-twitch-brand-deal-data/")],
                "body": [
                    "Collabstr, a marketplace that matches brands with creators, gave Tubefilter its deal pricing across both gaming platforms.  <mark>YouTube gaming creators averaged about 203 dollars per deal against about 165 for Twitch streamers</mark> — a 23% premium, drawn from what Collabstr says is the same population of brand buyers on both sides.",
                    "Two things stop this being a finding.  Collabstr's own book contains 15 times more YouTube deals than Twitch deals, so the two averages are not built on comparable volume.  And nobody at Collabstr is quoted explaining the gap at all — there is no mechanism in the piece, just the price.",
                    "The traffic data does not settle it either, and Tubefilter says so directly: Stream Hatchet shows Twitch declining year on year while YouTube gaming grows, but the piece notes that view-inflating bots and the countermeasures against them make all such counting too compromised to trust.",
                    "Collabstr's own read is the practical one.  Twitch partnerships are potential savings for brands, top streamers such as Kai Cenat now work across both platforms anyway, and Kick is arriving as a third option with advertising of its own.  Note the deal sizes: these are two hundred dollar marketplace bookings with small creators, not the mid-tier deals most of this brief covers.",
                ],
                "flagnote": "Marketplace data from a company that sells access to these creators, with 15 times more YouTube deals than Twitch deals in the underlying set and no stated methodology.  The article offers no explanation for the gap, so this is a price observation and nothing more.",
                "so_what": "A 23% gap between two platforms serving the same buyers is either a real difference in what you get or a habit that nobody has priced properly, and the reporting cannot tell you which.  What it does tell you is that the same creator population is cheaper on one side, and at small deal sizes that is a testable question rather than a strategic one.",
                "do_this": "On your next gaming buy, ask one creator who works on both platforms to quote you separately for a YouTube integration and a Twitch stream, and compare the gap in your own pipeline against 23% before you accept either price as normal.",
            },
        ],
    },
    {
        "id": "format", "name": "FORMAT LAB", "page": "pg. 08",
        "note": "one format worth stealing this week",
        "tint": None,
        "items": [
            {
                "title": "The ghost creator: a real person, a pseudonym, and 2,500 videos a week",
                "hook": "Brands have started buying a creator's ability to make things without buying their following.",
                "open": True,
                "stamps": [("DIGIDAY · 9 SEP", "https://digiday.com/media/wtf-is-a-ghost-creator/")],
                "body": [
                    "Digiday published a plain explainer this morning of a practice that has been growing quietly.  A ghost creator is a real human hired to make content to a brand's brief, posting under a pseudonym or under the brand's own accounts.  Not an anonymous account — a paid performer with no audience of their own attached to the work.",
                    "The trigger was a Semafor report on 2 September about Virelox, a content company which, per alleged posts from its co-founder, was releasing <mark>2,500 organic videos every week for businesses</mark> and running more than 106 YouTube accounts by April.  In July it posted a casting call on Backstage for a reliable and professional on-camera spokesperson for a news-related YouTube channel.",
                    "Julian Ivaldy, who runs a farm of 60 TikTok accounts, prefers content operators: you're paying for their ability to create content and reach people, rather than for an existing audience.  Ghost describes the arrangement, not whether you see a face.  Jeremy Carrasco, a director at Riddance, is blunter — they're pretty replaceable.  You can spin up a bunch, and hope that one hits, and if it hits, you did your job, and you might kill the campaign once it's done.",
                    "Joseph Perello, founder and chief executive of Props, gives both halves of the argument.  For it: a creator can be highly credible and persuasive without having millions of followers.  Those are two different assets, credibility and distribution, and brands no longer need to buy them as a bundle.  Against it: if you make the creator completely interchangeable or anonymous, you risk removing the very thing that makes creator media powerful.",
                    "Carrasco also names the reason volume is exploding.  He calls it a human carrying out an automation because they're effectively doing the last mile — a route around platform crackdowns on machine-made content.  YouTube removed several artificially generated political channels in August.",
                ],
                "flagnote": "The Virelox figures are attributed by Digiday to alleged posts from a co-founder rather than to the company, and neither TikTok nor YouTube responded before publication.  Every practitioner quoted operates in this market.",
                "so_what": "Creator marketing has sold credibility and distribution as one bundle for a decade, and this unbundles them — you buy the ability to make a convincing thing, and you supply the reach yourself with paid media.  It is also exactly what the two brands in today's lead concluded they should have bought.  The open question, and it is a real one, is whether credibility survives being detached from a person the viewer can look up.",
                "do_this": "Hire one on-camera person on retainer this quarter to make video for your own brand channel, brief them like a creator rather than a presenter, and compare their cost per finished video against what you last paid for a sponsored integration.",
            },
        ],
    },
]

FORECAST = [
    {
        "confidence": "LIKELY",
        "window": "by 31 March 2027",
        "headline": "More brands publish their own losses, because the post-mortem outperforms the case study",
        "body": "Two small apparel brands published a six-figure failure with the ledger attached and got picked up inside a day, which no case study of theirs would have managed.  The incentive is now visible to everyone in the category: a written loss buys credibility that a written win cannot, and it costs nothing but the embarrassment.  Expect the format to spread first among founder-led brands with nothing to protect, then into agencies looking to prove they measure honestly.",
        "do": "Write up one channel that did not work for you this year, with the actual numbers, and decide before you start whether you would publish it.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "by 30 June 2027",
        "headline": "Payment timing becomes the hardest term in creator contracts",
        "body": "A YouTuber with three million subscribers is sitting 16th on a bankrupt tour's creditor list for 1.4 million dollars, having already spent his audience's goodwill on the deal a year ago.  Every creator agent in the market has read that.  The negotiation that follows is not about fee size, it is about when the money lands and what happens if a sponsor's funding disappears mid-term, and the brands that can pay in advance are about to find creators cheaper than the ones that cannot.",
        "do": "Get your finance team to confirm this quarter whether you can pay a creator before publication, so you know the answer before the question is asked in a negotiation.",
    },
    {
        "confidence": "LIKELY",
        "window": "by 31 December 2026",
        "headline": "TikTok Shop budgets split into a content line and a sales line",
        "body": "The teardown in today's lead ends with a specific conclusion — the affiliate sales did not pay, the content it generated did, and the only reason they know is that they measured them separately.  Everyone running this playbook at a similar price point is about to reach the same crossroads with the same single budget line and no way to tell which half is working.  The split is the cheapest fix available and it requires no new spend.",
        "do": "Separate your creator content costs from your creator sales attribution in this quarter's reporting, even if it means two lines in a spreadsheet nobody asked for.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "by 31 December 2026",
        "headline": "A major studio signs creators to make brand campaigns rather than shows",
        "body": "Disney is convening 350-plus creators at the El Capitan Theatre next week, and the session run by its chief marketing and brand officer is billed around scripted series, features and brand campaigns together.  The first two are the story everyone expects.  The third is the one that changes who your agency competes with, because a studio that can offer a creator both a film deal and a brand campaign is offering something no agency can match.",
        "do": "Find out what your biggest client would pay for access to a creator roster, then work out honestly whether you or a studio is better placed to sell it.",
    },
]

TLDR = [
    "Two apparel brands ran a full TikTok Shop affiliate programme for four months, spent 2.25 to 2.65 dollars for every dollar of sales, and found that 38 of 21,365 enrolled creators produced 80% of it.  Split your creator budget into a content line and a sales line this week, so a failure in one cannot quietly kill the other.",
    "Twitch streams with a Drop attached generated 1.6 billion hours this year, up 46%, while the number of campaigns rose only 20% and channel participation rose 40%.  Brief a Drops campaign for Q4 if you have anything digital to give away, and book channels early.",
    "Z Event peaked at 1.3 million viewers across 354 channels but the biggest single channel held only 370,400 of it, and a separate esports final posted hours watched up 27.6% while average viewers fell 10.8%.  Ask for peak, average and channel count on every livestream number you are shown before you react to it.",
    "IAB research says 72% of people now use an AI assistant for shopping decisions, and that they trust everyday consumers at 52% against subject-matter experts at 37%.  Add a plain spoken verdict to your creator brief so a summariser has a sentence it can actually lift.",
    "LIV Golf filed for bankruptcy owing a golf YouTuber roughly 1.4 million dollars, placing him 16th on the creditor list ahead of two players.  Check whether your own creator contracts pay in arrears and move the next one to paying before publication.",
    "TikTok spend rose 20% at one agency and 41% at another over the summer while YouTube grew 6%, and the agencies say it is incremental budget rather than money leaving video.  Write down which channel your next TikTok increase would otherwise have come from, and set a kill date if the honest answer is none.",
    "A one-man automotive channel with 325,000 subscribers did 1.25 million views on an unsponsored 20,000-mile engine oil test, six and a half times his own median.  If you sell anything that goes into a car, fund a controlled test with no approval rights and buy the media behind whatever it concludes.",
]

SHARE = [
    {
        "who": "JARED · CEO",
        "angle": "The failed sales channel produced their best-performing creative, and most brands never find out because both live on one budget line.",
        "post": "Two apparel brands spent six figures on TikTok Shop over four months, made back less than half of it, and then published the entire ledger under their own names.\n\n$2.25 to $2.65 spent for every $1 of sales. 21,365 creators enrolled. 38 of them produced 80% of the revenue, and one produced about 30% on his own.\n\nThe report is by Kyle Bergman, who runs Swoveralls and DudeRobe, and David Silverander, whose agency ran the media for both.\n\nThe loss is not the interesting part. This is: they say the highest-return thing the exercise produced was the video. Creator content, licensed and run as paid media, outperformed most of what they were making in-house.\n\nSo they bought a sales channel and what they got was a content operation, and the only reason they know is that they measured the two things separately.\n\nMost companies do not. The creator budget is one line. It gets judged on sales. When the sales do not come, the whole line gets cut — including the half that was working.\n\nThey are clear this is not a verdict on the platform. Their products are $99 and $128; the thing converts well under $60.\n\nContent and distribution have always been two separate decisions. This is the first time I have seen someone pay six figures to prove it and then publish the working.",
        "why": "It turns a channel failure into an argument for funding content separately from sales, which is a budgeting decision a chief executive can actually make.",
    },
    {
        "who": "JAMES · CREATIVE DIRECTOR",
        "angle": "Audiences trust everyday consumers 15 points more than subject-matter experts, and a summariser is now the last thing they read.",
        "post": "52% of people say they trust product recommendations from everyday consumers. 37% say the same about subject-matter experts.\n\nI have spent my career casting the expert.\n\nThe figures are from IAB research out this morning. 2,200 people across five markets who had used an AI assistant to research a purchase in the previous three months. 72% of them now use one for shopping decisions. 56% want creator perspectives inside the answer they get back.\n\nCasting for authority is the defensible choice in a client room. You bring the dermatologist, the mechanic, the chef, and nobody argues with you. The research says the audience discounts exactly that.\n\nAnd now there is a machine standing between the film and the buyer, pulling out whatever reads like a real person's verdict.\n\nWhich means the things I have been treating as production value — the lighting, the credentials on screen, the clean delivery — may be the first things stripped out.\n\nI do not know how to brief for that yet. Say something a machine can quote is a horrible line to put in a creative brief and I am not going to put it in one.\n\nBut I would rather admit I have not solved it than keep making beautiful work that gets summarised into nothing.",
        "why": "A creative director conceding that casting for authority is the wrong instinct, and that he has no answer yet, is uncomfortable and specific in a way a news summary is not.",
    },
    {
        "who": "LAWRY · LEAD VIDEO EDITOR",
        "angle": "The most persuasive product demonstration of the year works because nobody cut it, and tightening a demo is how you make it less true.",
        "post": "A 46-minute video about engine oil has done 1.25 million views in twelve days. The reason it works is that almost nothing in it is cut.\n\nRepair Geek ran Valvoline Restore & Protect for 20,000 miles. Tore the engine down at the start to document a baseline. Reassembled it. Four oil changes. Sent used oil out for lab analysis. Tore the same engine down again at the end.\n\nHis channel median is about 196,000 views. This is six and a half times that. There is no sponsor in the description.\n\nWhat I keep thinking about is the edit, or the deliberate lack of one. When the whole claim is that this is the same engine and here is what changed, every cut is a place a viewer can decide you swapped something. So he holds. Moves the camera instead of cutting. Keeps his hands in frame.\n\nThat is the opposite of my job. My job is usually to find the boring forty seconds and take them out.\n\nHere the boring forty seconds is the evidence.\n\nI have sat in sessions where we tightened a product demo because it dragged, and that demo was the only thing in the film anyone needed to believe. We made it shorter. We also made it less true, and nobody in the room said so, me included.",
        "why": "It is an edit-suite observation about when cutting destroys the only load-bearing part of a film, written from inside the work and ending on an admission rather than a lesson.",
    },
]
