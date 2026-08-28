# -*- coding: utf-8 -*-
"""Content for THE FEED — issue data only.  The render spec lives in build_feed.py."""

ISSUE = {
    "date_iso": "2026-08-28",
    "kicker": "Crux Media // Friday 28 August 2026",
    "tagline": "What brands did on YouTube yesterday, and whether it worked.",
    "pace": "STEADY",
    "next_drop": "Next drop: Monday, 06:30 MT",
}

LEAD = {
    "headline": "NEARLY HALF OF BRANDS HAVE MISPRICED A CREATOR DEAL, BECAUSE NOBODY CAN LOOK UP WHAT THE LAST ONE SOLD FOR",
    "deck": "Digiday put the question to the industry this morning and the answer was blunter than anyone expected.  Creator pricing is not a market.  It is a thousand private guesses, and a survey of a thousand brand-side buyers found nearly half of them guessed wrong.",
    "stamps": [
        ("DIGIDAY · 28 AUG", "https://digiday.com/media/creator-industry-admits-that-fee-pricing-is-out-of-control-but-cant-agree-on-a-fix/"),
        ("CENSUSWIDE SURVEY · 31 JUL", "https://www.netinfluencer.com/nearly-half-of-brands-have-mispriced-creator-deals-survey-finds/"),
    ],
    "body": [
        "Digiday published a piece this morning in which the people who buy and sell creator video said out loud what they normally say off the record.  Harley Block, chief executive and co-founder of IF7, called creator pricing <mark>\"out of control.\"</mark>  James Nord, who founded the creator platform Fohr, gave the cleanest description of why: <mark>\"Imagine the real estate market where you could never look up what a house on your street sold for.\"</mark>",
        "Hold that image, because it is the whole story.  When you buy a house you can see what every comparable house nearby actually sold for, and that public record is the thing that stops either side taking you.  There is no such record for creator deals.  Every price is negotiated privately, nothing is published, and no two people in the room have the same information.",
        "Now the number.  A survey of <mark>1,000 marketing and procurement decision-makers</mark> at brands in the US and UK, run by the research firm Censuswide for the creator agency Billion Dollar Boy and fielded 10 to 16 July, found that <mark>45% had mispriced a creator partnership</mark> — paid meaningfully above or below what it was worth.  The split by market is stark: <mark>58% of UK brands against 33% of US brands</mark>.  Among the brands that got it wrong, 40% overpaid and 36% underpaid, so this is not a story about creators fleecing anyone.  It is a story about nobody knowing the number.",
        "Nord names the consequence precisely.  <mark>\"This is not a functioning market.  Prices never go down.  There's no clearinghouse, there's no transparency, so it creates this information asymmetry.\"</mark>  Jamie Gutfreund, who founded Creator Vision, puts the same thing from the buyer's chair: <mark>\"They have no historical benchmarking, which means they can't do anything predictive.\"</mark>  If you cannot see what you paid last time, you cannot tell whether this quote is good.  So you accept it, and the accepted price becomes the new floor.",
        "The plumbing is worse than you think.  In the same survey, <mark>73% of brands manage creator spend manually</mark> — 49% on spreadsheets, 24% on email and shared files — and only <mark>21% use software built for the job</mark>.  Becky Owen, chief marketing officer at Billion Dollar Boy: <mark>\"The problem isn't what creators cost.  It's that creator investment has scaled faster than the systems built to price and govern it.\"</mark>  Confidence tracks the plumbing.  Just <mark>44%</mark> of decision-makers say they are fully confident negotiating a fair rate, and they trust an outside agency's numbers far more than their own — 60% are very confident in agency-negotiated rates against 40% for their in-house team.",
        "The creators feel it too, from the other side of the same fog.  Osman Badat, who advises creators as The Social Accountant, wants exactly what Nord wants: <mark>\"There needs to be a place where people could go and say, 'Wait a second, this was the benchmark.  Why are you only offering me this?'\"</mark>  Both sides are asking for the same public record.  Nobody has built it, and the three companies racing to build it all sell something else.",
    ],
    "numbers": [
        ("45%", "of brands say they have mispriced a creator partnership"),
        ("58% v 33%", "UK brands mispricing against US brands, same survey"),
        ("21%", "who price creator deals on purpose-built software rather than spreadsheets and email"),
    ],
    "flagnote": "Digiday's write-up states that 50% of marketers misprice creator fees and 40% feel they overpaid.  The primary release from the same survey reports 45% mispriced, and that among those who mispriced, 40% overpaid and 36% underpaid.  The primary figures are the ones used here.  The survey was run by Censuswide for Billion Dollar Boy, which launched a creator pricing and governance product alongside the research, so the sponsor sells the fix for the problem it measured.",
    "so_what": "A price only means something when you can compare it to another price.  Creator deals have no comparison set, so every negotiation starts from zero and the number that gets agreed is whatever the more confident person in the room says first.  That is why rates only ever ratchet upward, and it is why the fix is not a better negotiator — it is a record of what you actually paid.",
    "do_this": "Build your own price book this week.  Pull every creator deal your team has signed in the last eighteen months into one sheet with four columns: the fee, the deliverables, the views the content actually got, and the cost per thousand views that works out to.  Take it into your next negotiation and quote from it.",
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
                "title": "Carhartt built its NFL campaign around the people who poured the concrete, and trade-school traffic went up five times",
                "hook": "Every other brand at that stadium bought a player.  Carhartt bought the crew who built it, and the only number that mattered to Carhartt went up 5x.",
                "open": True,
                "stamps": [
                    ("MODERN RETAIL · 27 AUG", "https://www.modernretail.co/retailers/carhartt-is-aligning-with-the-nfl-through-the-tradespeople-building-highmark-stadium/"),
                ],
                "body": [
                    "The Buffalo Bills' new Highmark Stadium is the only NFL stadium opening this year, which made it the most contested sponsorship object in American sport this summer.  Carhartt did not buy a player, a naming right or a halftime slot.  It spent <mark>two years filming the construction</mark> and built a campaign called Made Possible around the tradespeople doing the building.",
                    "The assets are unglamorous and specific.  A 30-second spot on the workers who built the stadium.  A two-minute film in which Bills alumnus Thurman Thomas tours the finished building with current running back James Cook III — and Thomas is in it because his own company, 34 Group, installed the seats.  Social cutdowns, in-stadium advertising from the first preseason game on 15 August, and rally towels printed with the names of the construction crew.",
                    "Here is the number that makes it a W rather than a nice story.  Traffic to Carhartt's <mark>Join the Trades landing page ran 5x higher</mark> than the same period a year earlier.  Not impressions.  Not followers.  Traffic to the page where someone who watched the ad goes to find out how to do the job the ad is about.  Carhartt also put <mark>$300,000</mark> into vocational programmes in Western New York, which is the same argument with a cheque attached.",
                    "Norma Delaney, Carhartt's vice president of marketing and creative, explains the discipline behind it: <mark>\"There's a lot of marketplace interest in the stadium.  This is the only stadium that is opening this year.\"</mark>  And on the temptation to do what everyone else was doing: <mark>\"It would be easy to follow a trend and go in that direction, but that's not why we're Carhartt.\"</mark>",
                    "The mechanism is that the subject of the film and the goal of the campaign are the same thing.  Carhartt sells workwear and needs more people to enter the trades, so it made a film about people in the trades, and the call to action is join the trades.  There is no leap for the viewer to make.  An athlete would have been a bigger name and a longer leap.",
                ],
                "so_what": "The reason this converted is that Carhartt did not borrow an audience and then try to bend it toward the product.  It filmed the exact people its product is for, doing the exact thing it wants more people to do, at an event those people built with their hands.  When the subject of your video and the action you want are the same, you do not need a clever bridge between them, and the drop-off that normally happens at the bridge does not happen.",
                "do_this": "Before your next big sponsorship, write down the one action you want a viewer to take, then cast the film with people already doing that action rather than with the most famous person available.  Measure it on traffic to the page where that action happens, not on impressions.",
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
                "title": "Wrong owner: the brand signed off on the ad, and the creator lost a tournament worth at least $6 million a year",
                "hook": "Callaway approved it.  Good Good made it.  Yesterday Callaway walked, four retailers cleared the shelves, and Good Good gave up title sponsorship of its own PGA Tour event.",
                "open": True,
                "stamps": [
                    ("FRONT OFFICE SPORTS · 27 AUG", "https://frontofficesports.com/callaway-good-good-golf-breakup/"),
                    ("GOLF.COM · 27 AUG", "https://golf.com/news/good-good-callaway-mistake-amends/"),
                    ("PGA TOUR · 27 AUG", "https://www.pgatour.com/article/news/latest/2026/08/27/good-good-golf-statement-press-release-2026"),
                ],
                "body": [
                    "We covered the ad itself on Wednesday.  Yesterday the bill arrived, and the size of it is the story.  Callaway ended its relationship with the golf creator company Good Good <mark>effective immediately</mark>, in a single line: <mark>\"Callaway has ended its relationship with Good Good, effective immediately.\"</mark>  It also committed <mark>$1 million</mark> to organisations working to prevent violence against women.",
                    "Then the rest went.  <mark>Dick's Sporting Goods, Golf Galaxy, PGA Tour Superstore and Target</mark> pulled Good Good merchandise.  Golf Channel pushed back the premiere of its Big Break series with the company.  And Good Good stepped away as title sponsor of its own PGA Tour tournament — a multi-year deal that Front Office Sports reports was worth <mark>at least $6 million a year</mark>.  The event still runs 12 to 15 November at Omni Barton Creek; the Tour will find another name for it.",
                    "Good Good is not a small operation.  <mark>2.1 million YouTube subscribers</mark>, founded in 2020, and <mark>$45 million raised</mark> last year from a group that includes Peyton Manning.  Callaway is a forty-four-year-old equipment company.  Between them they had a full approvals process, and the ad went out anyway.  Chip Brewer, Callaway's chief executive, on that: <mark>\"That approval should never have happened.\"</mark>",
                    "The failure mode is ownership, and it is worth being precise about it.  The creator made the ad.  The brand approved the ad.  When it went wrong, the brand could exit in one line and the creator could not — Good Good lost the equipment partner, the retail distribution and the tournament, while Callaway lost a sponsorship and gained a $1 million donation to talk about.  Both parties signed the same thing and only one of them was structurally exposed to it.",
                    "PGA Tour chief executive Brian Rolapp put the second failure on the record too, which is the part every brand should read twice.  On Good Good's first response: <mark>\"I think initially, no.  Their initial response was disappointing.  It was a bit defensive and late.\"</mark>  A three-sentence Saturday post and a two-sentence partner statement bought five days of escalation.  The ad did the damage.  The pace of the reply decided how far it spread.",
                ],
                "flagnote": "The $6 million annual sponsorship value is reported by Front Office Sports as \"at least $6 million annually\" and has not been confirmed by Good Good or the PGA Tour.  Target's removal of Good Good merchandise is reported second-hand.  No replacement title sponsor for the November event has been named — treat any \"renamed\" claim as unconfirmed.",
                "so_what": "When you co-sign a creator's creative, you are buying two things you may not have priced: the approval and the exposure.  The approval means you cannot later call it their video, because your own sign-off is on the record.  The exposure is asymmetric — you can terminate in a sentence, and the creator cannot terminate their own audience, their retail listings or their tournament.  That imbalance is exactly why creators will start asking for indemnities and cure periods in the next round of contracts.",
                "do_this": "Find out today who in your organisation holds final sign-off on creator-produced assets, and put a named second reviewer on anything involving physical contact, conflict or a joke at someone's expense.  Then write a 24-hour response rule into your creator contracts so nobody is drafting a statement on a Saturday afternoon.",
            },
            {
                "title": "Wrong economics: Messi has 516 million followers and his drink is dead in under two years",
                "hook": "Two celebrity beverage brands folded this month in a category growing 29% a year.  Followers got them onto the shelf.  Nothing got them off it fast enough.",
                "stamps": [
                    ("DIGIDAY · 26 AUG", "https://digiday.com/marketing/why-more-celebrity-led-brands-are-shutting-down/"),
                ],
                "body": [
                    "Lionel Messi's hydration drink Mas+ shut down <mark>less than two years</mark> after launch.  The podcaster Alex Cooper's functional drink Unwell is being discontinued this autumn.  Both landed in a category that is <mark>growing 29% year on year</mark>, and both had serious distribution behind them — Mas+ launched with Mark Anthony Group, the company behind White Claw.  Messi has <mark>516 million Instagram followers</mark>.",
                    "That is not the only recent list.  Kim Kardashian's Skkn folded into Skims in 2025.  Gwen Stefani's Gxve Beauty closed earlier this year.  Drew Barrymore's Flower Beauty was discontinued in 2025.  The pattern is now long enough to be a pattern.",
                    "Sunny Bonnell, founder and chief executive of the branding firm Motto, names the gap between an audience and a customer: a huge following <mark>\"does not automatically equate to the audience wanting to buy a beverage.\"</mark>  Mark Gallo, a beverage distribution manager, gives the mechanical version: <mark>\"Retail is a velocity business.  Those are not the same currency.\"</mark>",
                    "Velocity is the whole thing.  A retailer measures a drink by how many units leave that shelf per store per week, and it re-decides your listing on that number every few months.  A famous founder gets you the first order because the buyer believes the announcement will move product.  If the second and third purchase does not come from ordinary shoppers who liked the drink, the velocity number sags and the listing goes to someone else — no matter how many people follow the founder.",
                ],
                "so_what": "A creator or celebrity audience is a launch mechanism, not a retention mechanism.  It compresses your first wave of demand into a moment, which is genuinely valuable, but the shelf does not care about the moment — it cares about the twelfth week.  If the product does not earn a repeat purchase from people who have no relationship with the founder, fame just makes the failure faster and more public.",
                "do_this": "If you are being pitched a creator-founded product line, ask for the repeat purchase rate and the units per store per week before you ask about the founder's reach, and make the second-quarter velocity number the gate that releases the marketing budget.",
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
                "title": "Sony Music is suing Kroger for up to $58.8 million over songs in social posts, and the creator posts count too",
                "hook": "392 videos.  Up to $150,000 each.  The complaint singles out a creator post the brand's own marketing arm approved before it went live.",
                "stamps": [
                    ("MUSIC BUSINESS WORLDWIDE · 24 AUG", "https://www.musicbusinessworldwide.com/sony-music-sues-kroger-over-392-alleged-unauthorized-uses-of-its-recordings-in-social-media-ads/"),
                ],
                "body": [
                    "Sony Music and nine affiliated labels sued Kroger and <mark>19 Kroger entities</mark> on 21 August in the federal court for the Central District of California, over <mark>at least 392 unauthorised uses</mark> of Sony recordings across the supermarket group's social accounts and its creator-promoted content.  Statutory damages run to <mark>$150,000 per work</mark>, which puts the theoretical exposure near <mark>$58.8 million</mark>.  The recordings named include Mariah Carey's All I Want for Christmas Is You and OutKast's Hey Ya!, each alleged more than a dozen times.",
                    "The reason this one is dangerous rather than routine is the paper trail.  Sony and Kroger had <mark>at least 14 licensing agreements between 2017 and 2025</mark>, so the complaint argues Kroger cannot claim it did not know: <mark>\"Having previously negotiated and paid for such licenses, the Kroger Parties cannot claim ignorance of the licensing requirement.\"</mark>  Sony says it sent notice on 30 June 2025 and that new infringing posts appeared as recently as 12 August 2026.  Kroger spent <mark>$1.18 billion on advertising in 2025</mark>, a figure the complaint includes to make the point that this was affordable.",
                    "Now the part that lands on your desk.  The filing highlights a 2022 creator video promoting Home Chef, tagged #ad with a discount code, and argues that Kroger's own retail media arm formally approves creative before it posts.  In other words, a creator's post stops being the creator's problem the moment your team signs it off.  The audio library inside TikTok or Instagram is licensed for people posting personally.  It is not a commercial music licence, and a paid or boosted brand post is commercial use.",
                ],
                "flagnote": "These are allegations in a complaint that Kroger has not answered publicly.  The $58.8 million figure is the theoretical statutory maximum, not a claimed or awarded sum.",
                "so_what": "Every brand running creator content is carrying this risk right now and most do not know it, because the music was chosen inside an app that made it feel free.  The exposure is worst on whitelisted and boosted creator posts, where a personal-use track becomes paid brand media with your approval on it.  Sony has already settled similar cases against Marriott and USC, so the playbook is proven and the next defendant is whoever is easiest to document.",
                "do_this": "Pull a list of every live brand and creator post you have paid to boost in the last three years, check what audio each one uses, and take down or re-cut anything using commercial music you cannot produce a licence for.  Add a music-clearance line to your creator contract template this week.",
            },
            {
                "title": "YouTube and Amazon just made creator shopping links automatic, and you do not decide whether your products are in it",
                "hook": "A curated catalogue that Amazon controls now sits inside creator videos.  Your products are either in it or they are not, and nobody asked you.",
                "stamps": [
                    ("TUBEFILTER · 27 AUG", "https://www.tubefilter.com/2026/08/27/youtube-amazon-creator-product-selling-affiliate-marketing-shopping/"),
                ],
                "body": [
                    "YouTube and Amazon opened a shopping tie-up to US creators who are in both the YouTube Partner Programme and Amazon's influencer or associate programme.  Creators tag products in their videos and earn standard Amazon commissions, <mark>roughly 2% to 4% of the sale price</mark>, paid out through YouTube alongside their ad money.  If a viewer returns the item, the commission comes back off the next payout.",
                    "The control point is the catalogue.  YouTube's creator liaison Rene Ritchie says Amazon <mark>\"provides YouTube with a curated catalog of highly requested and trending products\"</mark> that creators can link.  Creators cannot pick anything they like, and brands are not asked.  A creator can request an addition through support, and approval is not guaranteed.",
                    "Scale, for context: <mark>more than a million creators</mark> have signed up for YouTube Shopping, and its gross merchandise value grew <mark>13x between the first quarter of 2024 and the first quarter of 2026</mark>.",
                ],
                "so_what": "This quietly changes what a creator affiliate deal is worth to you.  If your products are in the catalogue, creators can already earn on them without signing anything with you, which weakens the case for paying a separate affiliate fee on YouTube.  If your products are not in it, your competitors are getting free tagged placement inside videos you would have had to buy.  Either way the decision sits with Amazon and not with you.",
                "do_this": "Ask your Amazon account team this week whether your best-selling items are in the YouTube-linkable catalogue, and if they are not, start the request.  Then re-check any creator affiliate rate you are paying on YouTube against what the same creator now earns automatically.",
            },
            {
                "title": "A creator agency is now selling videos built to be quoted by chatbots",
                "hook": "Creator content shows up in a quarter of chatbot answers.  So an agency started commissioning videos aimed at the machine rather than the feed.",
                "stamps": [
                    ("TUBEFILTER · 27 AUG", "https://www.tubefilter.com/2026/08/27/answer-engine-optimization-aeo-influencer-creator-marketing-agency/"),
                ],
                "body": [
                    "The creator agency Influencer has partnered with the artificial-intelligence visibility firm Profound to sell what the trade is calling answer engine optimisation — commissioning creator videos specifically so that chatbots cite them when someone asks a question.  Research from the agency Jellyfish, cited in the piece, puts creator content in <mark>25% of chatbot responses</mark>, with YouTube having overtaken Reddit as the source these systems reach for most.",
                    "Ben Jeffries, Influencer's co-founder and chief executive: <mark>\"Creator marketing has entered a new era.  It now shapes what people think, trust and buy, as well as what AI understands and recommends.\"</mark>  Zoom has already commissioned creator videos designed to be cited this way, and the social platform Later has launched a competing offer.",
                ],
                "flagnote": "The 25% figure comes from Jellyfish research cited by an agency that sells the service it supports, and was not independently verified.  Treat it as directional.",
                "so_what": "This gives a creator video a second job with a second lifespan.  A sponsored video is normally worth whatever it earns in its first two weeks in the feed, and then it is archive.  If chatbots are pulling answers out of YouTube, that same video keeps answering buying questions for years, which changes how you value it and which questions you brief a creator to answer on camera.",
                "do_this": "Pick the five questions customers ask before they buy from you, and brief your next creator video to answer one of them out loud and clearly in the first minute, with the answer also written into the title and description.",
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
                "title": "The Esports World Cup missed last year's peak and grew 36.9% anyway, because the growth was never in the finals",
                "hook": "2.89 million at once, which is 32 sold-out Wembleys.  But the number that tells you the event is healthy is the boring one in the middle.",
                "open": True,
                "stamps": [
                    ("ESPORTS CHARTS · 28 AUG", "https://escharts.com/news/esports-world-cup-2026-viewership-recap"),
                ],
                "body": [
                    "Esports Charts published the full recap of this year's Esports World Cup this morning.  Twenty-five tournaments, the first edition relocated to Paris, and a set of numbers that pull in two directions if you only read the headline.",
                    "The peak: <mark>more than 2.89 million people watching at the same moment</mark>, during a Mobile Legends playoff, which came in <mark>6% below last year's record</mark>.  The total: <mark>more than 237 million hours watched, up 29.5%</mark>.  Those two facts together are usually a warning sign, because hours watched inflates whenever an event simply runs longer or adds more broadcasts, and nearly half the tournaments expanded their fields this year.",
                    "Which is why the third number is the one that matters.  Average live viewers ran <mark>145,100, up 36.9% year on year</mark>.  Average concurrents is the honest measure — it is how many people were watching at a typical moment, so it does not reward you for staying on air longer.  It went up faster than the total did.  That means the extra airtime was not empty airtime.  The event genuinely got bigger in the middle, and merely failed to beat one exceptional final.",
                    "Put the scale in something you can picture.  2.89 million watching at once is about <mark>32 sold-out Wembley Stadiums</mark>.  The average of 145,100 is bigger than a full Michigan Stadium, the largest stadium in the United States, sustained across the whole run.  The distribution shifted too: <mark>YouTube took 42% of hours watched and Twitch 30.2%</mark>, Kick doubled year on year, and the fastest-growing languages were <mark>Hindi at +300% and French at +124%</mark>.",
                ],
                "numbers": [
                    ("2.89M", "peak viewers at once, 6% short of last year's record"),
                    ("145.1K", "average live viewers, up 36.9% — the number that is not inflated by airtime"),
                    ("237M", "total hours watched, up 29.5% on a longer, wider event"),
                ],
                "so_what": "Peak tells you how big your single best moment was.  Hours watched tells you how long you were on air, which you control.  Average concurrents tells you how many people were actually there on a normal day, and it is the only one of the three that a seller cannot inflate by scheduling more content.  When average grows faster than total hours, the audience is real.  When total hours grows and average falls, you are being sold airtime.",
                "do_this": "Make average concurrent viewers a required line on every livestream proposal you receive, alongside peak and total hours, and refuse to price against hours watched on its own.  If a seller will not give you the average, assume it went down.",
            },
            {
                "title": "Bang Energy bought a month of a 24-hour stream and got a room in the house",
                "hook": "5.16 million hours watched in 26 days, and the sponsor was not a mid-roll read.  It was part of the set.",
                "stamps": [
                    ("STREAMS CHARTS · 27 AUG", "https://streamscharts.com/news/cinna-twitch-subs-august-subathon"),
                    ("BEVNET · 2 AUG", "https://www.bevnet.com/pr/2026/08/02/twitch-phenom-cinna-declares-for-bang-energy-during-recordbreaking-subathon-attempt"),
                ],
                "body": [
                    "The Twitch streamer Cinna ran a subathon through August — a continuous broadcast that keeps going as long as viewers keep subscribing.  Between 1 and 26 August it drew <mark>5.16 million hours watched</mark>, peaking at <mark>46,600 concurrent viewers</mark> on 21 August.  Her subscriber count went from around <mark>5,000 to 83,478</mark>, which made her the second most-subscribed streamer on the platform, and she gained <mark>114,968 followers</mark>.",
                    "Bang Energy signed her as a brand ambassador for it and did something more interesting than buying ad reads.  It kitted out a dedicated weight room inside the subathon house.  For a month of round-the-clock broadcast, the brand was not an interruption between segments — it was a location the stream kept walking into.",
                ],
                "flagnote": "Subscriber counts are sourced by Streams Charts to Twitch Tracker rather than to Twitch itself.  The Bang Energy ambassador deal was announced via a company press release; no financial terms were disclosed.",
                "so_what": "A 24-hour format has a problem no normal stream has: there is nothing to do for hours at a time, and the audience is still there.  A sponsor that supplies a physical thing to do fills that hole, which means the brand earns screen time by being useful to the broadcast rather than by buying a gap in it.  That is a far better trade than thirty seconds of read, and it only works if you give the creator something to actually use.",
                "do_this": "If you sponsor a long-form or endurance stream, replace one scheduled ad read with a physical object or space the creator will use unprompted — equipment, a setup, a game, food — and count the minutes it appears on camera against what the ad read would have cost.",
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
                "title": "The best-paid job in creator marketing right now is running a shop, not running a campaign",
                "hook": "A head of TikTok Shop is advertised at up to $240,000.  A campaign manager at one of the biggest talent agencies in the world tops out at $100,000.",
                "open": True,
                "stamps": [
                    ("NET INFLUENCER · 25 AUG", "https://www.netinfluencer.com/creator-economy-job-radar-august-25-2026-amazon-epic-games-twitch-and-more/"),
                ],
                "body": [
                    "Job adverts are a slow but honest indicator, because a published salary band is a company saying out loud what a skill is worth to it.  This week's open roles in creator marketing, with their disclosed bands, sort into a clear shape.",
                    "The commerce roles: Flamingo, part of Mammoth Brands, is hiring a <mark>Head of TikTok Shop at $195,000 to $240,000</mark>.  Kiss Beauty Group wants a senior manager for TikTok Shop and marketplace at <mark>$91,000 to $172,000</mark>.  The campaign roles: WME, one of the largest talent agencies on earth, is advertising a campaign manager for creator partnerships at <mark>$75,000 to $100,000</mark>, and Porter Novelli a senior influencer account executive at <mark>$70,000 to $78,000</mark>.  Amazon's brand creator marketing manager sits at <mark>$78,800 to $137,900</mark>.",
                    "Two outliers show where the ceiling actually is.  Epic Games will pay an influencer marketing director <mark>up to $261,381 in New York</mark>, and the creator ad platform Agentio is advertising a senior sales director at <mark>$280,000 to $400,000</mark> on target.  One is a games company that treats creators as its main distribution.  The other sells the software.",
                    "The gap between a head of shop and a campaign manager is not about seniority.  It is about what the job is measured on.  A shop is judged on revenue that lands in a system you can read at the end of the day.  A campaign is judged on reach, which nobody can convert into money without an argument.  Companies pay more for the job whose result they can see.",
                ],
                "so_what": "Follow the salary bands and you can see the industry quietly repricing itself around outcomes.  The roles attached to a cash register are being bid up, and the roles attached to reach are flat.  If you are building a creator team, that tells you where the scarce skill is — and if you sit in one of the flat roles, it tells you exactly which number to start reporting.",
                "do_this": "Benchmark your own creator roles against these bands before your next hiring round, and if you want the budget to grow, attach at least one person on your team to a revenue number rather than an audience number this quarter.",
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
                "title": "Rockstar put its own trailer behind a Netflix paywall, and 1.8 million people watched it on Twitch anyway",
                "hook": "Twenty-six minutes of gameplay, exclusive to Netflix for six hours.  The audience routed around it in real time and made the window worth more, not less.",
                "open": True,
                "stamps": [
                    ("PC GAMER · 28 AUG", "https://www.pcgamer.com/games/action/gta-6-netflix-extended-look-youtube/"),
                    ("PLAYTOEARN · 28 AUG", "https://playtoearn.com/news/gta-6-extended-look-breaks-twitch-as-1-8-million-watch-on-netflix"),
                ],
                "body": [
                    "At noon Pacific yesterday, Rockstar premiered a <mark>26-minute</mark> Extended Look at Grand Theft Auto VI.  Not a trailer.  A long, quiet gameplay presentation.  And it went out exclusively on Netflix, behind a subscription, for <mark>six hours</mark> before Rockstar posted it free on YouTube.",
                    "Read that again, because it is genuinely odd.  A company took its single most valuable piece of marketing material — the thing it wants the maximum number of humans to see — and put a paywall in front of it on purpose.",
                    "Here is what happened.  Twitch concurrent viewership hit <mark>1.8 million during the presentation, up from 881,000 across the same streamers beforehand</mark>, as people watched streamers watching Netflix.  Twitch fell over: Downdetector logged <mark>more than 17,000 outage reports</mark> and StatusGator recorded roughly eleven minutes of core downtime.  Netflix threw its own errors at people trying to load the stream.  Then, six hours later, the free version landed on YouTube and swept up everyone who had missed it.",
                    "The window is the whole design.  A video anyone can watch at any time is a video with no reason to watch it now, and no reason to watch it with other people.  Putting it behind one door at one time forced everyone to arrive at the same moment, and because most of them could not get through that door, they gathered somewhere else and watched it together.  The co-streamers did the distribution for free and generated a second, bigger audience out of the friction.",
                    "And six hours is the number to notice.  Long enough that the event was over before the free version arrived, so nobody waited.  Short enough that the clips, the reactions and the arguments were all still live when the real thing went up, so the free release landed into a conversation that was already at full volume rather than starting one from cold.",
                ],
                "flagnote": "The Twitch viewership and outage figures come from PlayToEarn citing Twitch data, Downdetector and StatusGator, all crowd-reported rather than official.  Rockstar, Netflix and Take-Two have not released viewership figures for the event.",
                "so_what": "Scarcity and simultaneity are free, and almost nobody uses them on owned video.  A timed exclusive does not shrink your audience if the free release follows quickly — it converts a piece of content into an appointment, and appointments produce the reactions, clips and arguments that a quiet upload never gets.  The restriction is not the cost of the strategy.  It is the engine of it.",
                "do_this": "For your next big owned video, pick a single premiere time, put it in one place only, and release it everywhere else the same day rather than the same minute.  Tell your creator partners the time in advance so they can watch it live with their audiences.",
            },
        ],
    },
]

FORECAST = [
    {
        "confidence": "LIKELY",
        "window": "by 30 June 2027",
        "headline": "A creator rate benchmark becomes a line item in RFPs, and the first one to publish real numbers wins the market",
        "body": "Fohr, Billion Dollar Boy and Nutcake are all building pricing tools right now, and every one of them has the same problem: the people building the tools do not set the prices, and no brand wants to hand over its deal history first.  Somebody will break that deadlock by publishing anonymised comparable deals rather than a calculator, the way property listing sites did.  The moment one credible set of comparables exists in public, procurement teams will start requiring it in briefs, and the agencies sitting on private benchmarking data lose their best advantage.",
        "do": "Start logging your own deals in a consistent format now so you can contribute to, and benefit from, whichever benchmark wins.",
    },
    {
        "confidence": "LIKELY",
        "window": "next 6 months",
        "headline": "Music licensing becomes a standard clause in creator contracts after another large brand gets sued",
        "body": "Sony has now settled with Marriott and USC and is suing Kroger, and the pattern in each is the same: a large advertiser with a documented history of licensing, a long tail of social posts, and creator content the brand approved.  That is a repeatable target profile, and there are thousands of brands matching it who have never once asked a creator where the audio came from.  Expect at least one more suit against a household advertiser, and expect creator contract templates to grow a music warranty in response.",
        "do": "Add a music-clearance warranty to your creator template before your legal team is asked to add one under pressure.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "next 9 months",
        "headline": "Brands start lobbying to get into Amazon's YouTube-linkable catalogue, and a paid tier appears",
        "body": "Amazon now controls which products a million-plus creators can tag inside YouTube videos, and it decides that on what is trending rather than on what any brand wants.  A gatekept list that drives sales is a list people will pay to be on.  The obvious next step is a paid or negotiated route into the catalogue, sold through Amazon's advertising business rather than granted on merit.  Watch for the first brand publicly complaining about being left out, because that is usually the quarter before a paid option quietly appears.",
        "do": "Get your catalogue status confirmed now, while inclusion is still free and based on demand rather than spend.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "by 31 March 2027",
        "headline": "Another two celebrity or creator drinks brands close, and investors start asking for velocity before reach",
        "body": "Mas+ and Unwell both died inside a category growing 29% a year, with elite distribution partners and enormous founder audiences.  That combination failing twice in one month is a signal, not a coincidence, and there is a queue of similar brands launched in 2024 and 2025 now hitting their second full year on shelf, which is exactly when listings get re-decided.  Expect more closures, and expect the diligence question in the next funding round to be units per store per week rather than follower count.",
        "do": "If you advise a creator-founded consumer brand, get its repeat-purchase and shelf-velocity numbers into presentable shape before the next raise.",
    },
    {
        "confidence": "LONG SHOT",
        "window": "next 12 months",
        "headline": "A major advertiser publishes what it actually pays creators, and resets the whole negotiation",
        "body": "Everyone in this market says they want transparency and nobody wants to go first, because the first mover hands its competitors a price list and hands its creators a floor.  But a brand confident that it pays fairly has an unusual recruiting pitch to creators, and one large advertiser deciding that openness is cheaper than a permanent information war would end the guessing overnight for everyone who follows.  It is unlikely because the incentives point the other way, and it would be the single fastest fix to the problem in today's lead.",
        "do": "Decide now what your rates would look like if they were public, and fix anything you would be embarrassed to defend.",
    },
]

TLDR = [
    "A survey of 1,000 brand-side buyers found 45% had mispriced a creator deal, 58% in the UK against 33% in the US, and only 21% price on purpose-built software rather than spreadsheets and email — because there is no public record of what any creator deal ever sold for.  Build your own price book this week from every deal your team signed in the last eighteen months, with fee, deliverables, actual views and cost per thousand views in four columns.",
    "Callaway ended its Good Good partnership outright, four retailers pulled the merchandise, and Good Good gave up title sponsorship of its own PGA Tour event reported at least $6 million a year — after the brand had approved the ad that caused it.  Name today who holds final sign-off on creator-produced assets, add a second reviewer for anything involving physical contact or conflict, and write a 24-hour response rule into your creator contracts.",
    "Carhartt cast the tradespeople who built the new Buffalo Bills stadium instead of the players who play in it, and traffic to its Join the Trades page ran five times higher than the same period last year.  Cast your next campaign with people already doing the action you want viewers to take, and measure it on traffic to the page where that action happens.",
    "Sony Music is suing Kroger over at least 392 unauthorised song uses in social and creator posts, with statutory damages up to $150,000 each, and the complaint points to a creator video the brand's own marketing arm approved.  Audit every boosted brand and creator post for its audio, take down anything you cannot produce a licence for, and add a music-clearance clause to your creator contract template.",
    "YouTube and Amazon now let creators tag products from a catalogue Amazon curates and brands do not control, paying creators 2% to 4% commissions automatically, on a shopping business whose sales grew 13x in two years.  Ask your Amazon account team whether your best sellers are in the linkable catalogue, and re-check any YouTube affiliate rate you pay against what creators now earn without you.",
    "The Esports World Cup peaked 6% below last year at 2.89 million but grew average live viewers 36.9% to 145,100 — the measure a seller cannot inflate by simply staying on air longer.  Require average concurrent viewers on every livestream proposal alongside peak and total hours, and price against the average rather than hours watched.",
    "Job adverts show a Head of TikTok Shop advertised at up to $240,000 while a campaign manager at WME tops out at $100,000, because commerce roles are judged on revenue and campaign roles are judged on reach.  Benchmark your creator roles against those bands, and attach at least one person on your team to a revenue number this quarter.",
]
