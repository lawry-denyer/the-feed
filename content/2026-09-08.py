# -*- coding: utf-8 -*-
"""Content for THE FEED — issue data only.  The render spec lives in build_feed.py."""

ISSUE = {
    "date_iso": "2026-09-08",
    "kicker": "Crux Media // Tuesday 8 September 2026",
    "tagline": "What brands did on YouTube yesterday, and whether it worked.",
    "pace": "STEADY",
    "next_drop": "Next drop: Wednesday, 06:30 MT",
}

LEAD = {
    "headline": "HALF OF EVERY WEB REQUEST IS NOW A MACHINE, AND YOUR RETARGETING LIST HAS BEEN LEARNING FROM IT",
    "deck": "Cloudflare puts bots and AI agents past half of all web traffic.  One agency's online retail clients saw bot traffic rise 80% in a year, and cleaning it out of their audience lists pushed the cost of reaching a thousand people up 20%.  The budget is not going back to the open web.  It is moving to places where people log in — which is the actual reason your social and creator video money is about to grow.",
    "stamps": [
        ("DIGIDAY · 8 SEP", "https://digiday.com/media-buying/marketers-face-dilemma-around-rising-bot-and-ai-web-traffic/"),
        ("PPC LAND · 8 SEP", "https://ppc.land/half-of-web-requests-are-bots-as-agency-cpms-climb-20/"),
    ],
    "body": [
        "Retargeting is the thing where you visit a website, then that brand's ads follow you around for a fortnight.  It works by recording who visited which page and building a list out of it.  Digiday reported this morning that the list has stopped describing people.  Cloudflare's figure is that automated agents and bots now account for <mark>more than half of all web requests</mark>.",
        "David Dweck, president at the media agency GoFish, gave Digiday the shape of it on the ground.  His online retail clients saw bot traffic rise <mark>80% year on year</mark> on average.  His words for what that did to the audience lists: those actions got muddied, or poisoned, with a lot of bot traffic.  Cost per customer briefly spiked.  We saw a degradation in performance starting in Q4 last year and dragging into this year.",
        "The fix has a price attached, and this is the number to carry into a meeting.  GoFish narrowed the rules on who lands in a retargeting pool, which shrank the pool, which pushed the <mark>average cost of reaching a thousand people up 20%</mark>.  Nothing got better.  The same money now buys fewer people, because the extra people were never there.",
        "The reason old bot filters do not catch this is the interesting part.  A classic bot visits a page and leaves, which is easy to spot.  An AI agent shopping on somebody's behalf adds things to a basket and signs up to a newsletter.  It behaves like your best customer.  John Lewis told Reuters that agent-driven searches went from 0.3% to 2.5% of all its web visits in a single year, and it is actively trying to attract more of them.",
        "So the money moves.  Nola Ladd, brand media supervisor at Collective Measures, said the bot problem was the final nail in the coffin for retargeting at one client, which shifted spend into retail media and social platforms instead.  Her line on where it goes: first party data is king.  Dweck said the same thing more bluntly — since 2023 they have seen a big shift out of automated open-web buying and back into places where people are more comfortable, like Google, Amazon and Meta.",
        "Not everyone is blocking.  Chad Keller, co-founder of the pillow brand Mellow Sleep, told Digiday he is less interested in blocking automated traffic than in classifying it, because AI assistants are already sending traffic that converts several times better than his site average.  Both positions are consistent.  The web is filling up with software that behaves like a customer, and some of it is standing in for one.",
    ],
    "numbers": [
        ("50%", "of all web requests now come from bots or automated agents — Cloudflare"),
        ("80%", "year-on-year rise in bot traffic across one agency's online retail clients"),
        ("20%", "rise in the cost to reach a thousand people once those bots are filtered out"),
    ],
    "flagnote": "The 80% and the 20% are one agency president's account of his own client base.  GoFish gave Digiday no sample size, no client names and no financial specifics, and seven other named practitioners in the piece describe the problem without quantifying it.  The Cloudflare figure counts web requests, not people or sessions.  Treat the direction as solid and the two percentages as one shop's experience.",
    "so_what": "Your retargeting audience is a list of things that visited a page, and a growing share of those things are software.  Cleaning the list makes it smaller and therefore dearer, so performance looks worse either way — before you clean it because it is fake, after you clean it because it costs more.  That is why buyers are rotating into environments where a real person had to log in, and video on those platforms is the biggest thing you can buy there.",
    "do_this": "Ask your buyers this week for the split between logged-in inventory and open-web inventory on your last quarter, and move the retargeting line specifically into places with a login behind it — YouTube, Meta, or a retail media network — rather than trying to filter your way back to a clean audience.",
}

SECTIONS = [
    {
        "id": "ws", "name": "W'S", "page": "pg. 02",
        "note": "what worked, and the exact reason it worked",
        "tint": "blue",
        "items": [
            {
                "title": "Buyers think viewers hate AI-made ads.  Only 10 percent of viewers said they did",
                "hook": "A 38-point gap between what the industry assumes and what the audience reported.",
                "open": True,
                "stamps": [("PPC LAND · 5 SEP", "https://ppc.land/freewheel-finds-48-of-buyers-overrate-viewer-dislike-of-ai-ads/")],
                "body": [
                    "FreeWheel, the advertising arm of Comcast, published a report on Friday called AI in TV Advertising: The Buyer, Seller, and Viewer Perspectives.  It asked three separate groups the same question from three sides.  <mark>48% of media buyers and 39% of media sellers said they assume viewers find AI-generated creative off-putting.  10% of viewers said they disliked the AI-made advertising they had seen.</mark>  That is a 38 point gap on the buyer side and 29 on the seller side.",
                    "The samples are worth naming because they are unusually specific.  226 media buyers and 50 media sellers, fielded by AdExchanger in April 2026.  2,496 American adults with access to traditional TV, paid streaming or free ad-supported streaming, fielded by Dynata in the same month.  A separate November 2025 survey of 216 marketers and agencies sits underneath the attribution findings.",
                    "Read the mechanism carefully, because it is not the one the headline invites.  The viewers were asked about advertising they had seen and identified as AI-made.  The 10% is a reaction to AI creative people noticed.  That says nothing at all about work good enough that nobody clocked it, and it says nothing about the much larger group who never registered a question either way.",
                    "There is real counter-evidence in the same piece and it deserves the space.  Raptive surveyed 3,000 American adults and found that suspecting content was AI-made cut reader trust by close to half and reduced brand ad effectiveness by <mark>14% in purchase consideration</mark>.  The IAB found a generational split: 39% negative sentiment among Gen Z against 20% among millennials.  Those findings and FreeWheel's fit together if the variable is detection rather than production.",
                    "The viewers were also warmer than expected on AI doing scheduling work rather than creative work: 89% were open to it reducing how often the same ad repeats inside one episode, and 89% to it choosing when breaks fall to minimise disruption.  76% were open to personalised advertising made with it.",
                ],
                "flagnote": "FreeWheel is Comcast-owned advertising technology that has spent the past year building AI-assisted buying tools, so a finding that audiences mind AI creative less than buyers fear flatters its own roadmap.  The fieldwork is April 2026 and November 2025, which makes the report new and the data roughly five months old.  Fielding was outsourced to AdExchanger and Dynata.",
                "so_what": "The industry has been pricing in an audience backlash that the audience did not report, and the cost of that is work not made and tests not run.  But the honest reading is narrower than the headline: what viewers reacted badly to was AI they could spot.  The variable under all of this is whether the seams show, not whether a model touched it.",
                "do_this": "Run one blind test this month — put an AI-assisted cut and a conventionally made cut of the same spot in front of the same audience without labelling either, and measure whether anyone identifies which is which before you measure whether they liked it.",
            },
            {
                "title": "A schedule announcement became a 15-minute heist film, and the film is how they book next year's guests",
                "hook": "Two years of production on a piece of promotion.  Roughly 40 cameos.  The promo is the recruiting department.",
                "stamps": [("HOLLYWOOD REPORTER · 8 SEP", "https://www.hollywoodreporter.com/tv/tv-news/2026-espn-manningcast-schedule-release-video-heist-1236691008/")],
                "body": [
                    "Peyton and Eli Manning's Omaha Productions released Manningcast: Heist this morning, a <mark>15-minute short film with roughly 40 cameos</mark> whose entire payload is announcing which games the ESPN Manningcast will call this season, the Super Bowl included.  Glen Powell, Anne Hathaway, Paul Rudd, Larry David, Jon Hamm, Jason and Travis Kelce.  NFL commissioner Roger Goodell has a starring role.",
                    "The production timeline is the number that should stop you.  Therese Andrews, head of production at Omaha, told The Hollywood Reporter that planning began in <mark>late 2024 and shooting started at the 2025 Pro Bowl</mark>, chosen because it puts a season's worth of gettable famous people in one building for a weekend.  A schedule announcement with a two-year runway.",
                    "The script is built to bend around whoever says yes.  Andrews: we map out the cameo roles early on when we do the script, thinking about what kind of people we want, and then we chip away throughout the entirety of the year.  As we book certain people, we're reshaping the creative based on who we think is gettable, who might be interested in it, and then we rework every time we film with somebody.",
                    "Then Omaha president Jamie Horowitz says the quiet part.  I think part of the reason that Paul Rudd, Kevin Hart, or David Letterman appears on the Manningcast is because we do things like this.  If the Manningcast was just a football show, Peyton and Eli probably could still recruit lots of great people.  But the more you see these types of projects from Omaha outside of Monday night, the more likely creative people want to be part of our little world.",
                    "So the film is not advertising the show.  It is the thing that stocks the show.  The cameo list is simultaneously the creative and the proof that appearing in an Omaha production is a nice place to be, which is what gets next season's bookings answered.",
                ],
                "flagnote": "The Hollywood Reporter piece is an exclusive in which the only sources are two Omaha executives.  The film went live the same morning, so no view count or performance data exists yet.",
                "so_what": "Most brand video is built to be watched once and then measured.  This one is built to be shown to the next person you want to book, which means the audience that matters is about forty people with agents.  A film with that job justifies a budget and a timeline that a view count never would, because what it buys is a cast list you could not otherwise afford.",
                "do_this": "Take the most boring announcement on your calendar for next year — a schedule, a range refresh, a partnership renewal — and brief it as a piece of entertainment with a guest list, then start booking the guests now rather than when the announcement is due.",
            },
        ],
    },
    {
        "id": "ls", "name": "L'S", "page": "pg. 03",
        "note": "what broke, and the failure mode behind it",
        "tint": "pink",
        "items": [
            {
                "title": "Wrong economics: streaming ad breaks got 18 percent longer in eight months, and nobody told the subscriber",
                "hook": "Paramount+ now runs nine minutes of ads an hour.  Fifteen percent of the time you spend watching.",
                "open": True,
                "stamps": [("BUSINESS INSIDER · 8 SEP", "https://www.businessinsider.com/streaming-ad-loads-rise-streamer-price-increases-inflation-advertising-hollywood-2026-9")],
                "body": [
                    "Ampere Analysis measured how many minutes of advertising the big American streaming services show per hour, and gave the numbers to Business Insider this morning.  Across the top services, ad minutes per hour rose <mark>18% between January and August this year</mark>.  The average in August was just over five minutes.  Of the nine most-watched services by Nielsen's ratings, only Prime Video was showing fewer ads in August than in January.",
                    "The spread is enormous and it should change which environments you rate.  Paramount+ went from 7.87 minutes an hour in January to <mark>9.01 in August</mark>, which Business Insider points out is about 15% of the time a viewer spends watching.  Hulu went 6.78 to 8.23.  Disney+ 6.69 to 7.54.  Pluto TV 4.80 to 6.53.  HBO Max 2.80 to 3.79.  Netflix had the largest proportional increase of the lot, 1.40 to 2.44, and still runs the least advertising of any major service.",
                    "Business Insider checked whether cheaper ad tiers carry heavier loads and found no significant correlation between an ad tier's price and the number of minutes in it.  So the length of the break is not tracking what the subscriber paid.  It is tracking what the business needs.",
                    "Brandon Katz, an analyst at Greenlight Analytics, gave the reason plainly: everyone is trying to squeeze more value out of existing subscribers, because it has become so much harder and more expensive to keep growing.  And once you reach scale, ad-supported tiers are more lucrative than ad-free tiers.  Antenna's numbers show the funnel that creates: <mark>nearly 60% of streaming sign-ups now choose an ad plan</mark>, ad plans took four million net sign-ups in the first quarter while ad-free plans had more cancellations than sign-ups, and 11% of ad-tier subscribers had traded down from an ad-free plan, up from 7% in 2024.",
                    "One absence worth noticing.  YouTube is not in the dataset at all.  The biggest television app in America by watch time does not appear in the ad-load league table, so nobody is publishing a comparable clutter figure for the place a lot of your video already runs.",
                ],
                "flagnote": "Ampere changed its ad-load tracking method at the start of 2026, so this is a January to August 2026 comparison only and cannot be read against earlier years.  The per-service figures are averages for viewers on ad-supported tiers.",
                "so_what": "When the break stretches from just under eight minutes to just over nine, your spot does not get worse, it gets buried deeper in a queue.  The service is lengthening the break to hit a margin target, not because the audience agreed to more advertising, and the people absorbing it are disproportionately those who traded down from ad-free to save money.  Clutter is now a property of the environment you buy, and it is moving fast enough that a rate negotiated in January describes a different product by August.",
                "do_this": "Add two lines to your next streaming negotiation: the average break length on the service you are buying, and your position inside the pod.  Price the back half of a nine-minute break differently from the front of a two-minute one, and put the clutter figure in the deal so it can be checked in six months.",
            },
        ],
    },
    {
        "id": "moves", "name": "MOVES", "page": "pg. 04",
        "note": "deals, launches and rule changes worth knowing about",
        "tint": None,
        "items": [
            {
                "title": "Brad Pitt argues with 16 dogs, Spike Jonze directs, and the creators come in behind it",
                "hook": "A thousand-dollar espresso machine, an auteur film, and an influencer layer doing the demonstrating.",
                "stamps": [("VARIETY · 8 SEP", "https://variety.com/2026/biz/columns/brad-pitt-talk-dogs-delonghi-espresso-maker-ad-1236853440/")],
                "body": [
                    "De'Longhi launches Hot or Cold, Always Perfetto globally tomorrow, 9 September, for the Magnifica Duo espresso maker at 999 dollars 95.  Brad Pitt shares a house with 16 dogs whose barks are subtitled; they berate him about the washing up and withhold his coffee.  Spike Jonze directs.  Created with LOLAMadrid.  It runs across broadcast, digital and social, with a Perfetto Barista influencer campaign behind it.",
                    "The creative device is doing product work rather than decoration.  Global chief marketing officer Aparna Sundaresh frames the whole thing on duality, because the Duo makes both hot and cold espresso, and the dogs swing between adoring him and telling him off.  The idea is the specification.",
                    "The structure is the bit to note.  One expensive film to buy cultural permission and reach, then a layer of creators to do repetition and demonstration.  On a thousand-dollar appliance, somebody still has to show the machine working, and Spike Jonze is not going to be the one doing it.",
                ],
                "flagnote": "Variety exclusive, and the only quoted source is De'Longhi's own chief marketing officer.  The campaign has not launched, so there is no performance data of any kind.  Read it as a launch, not a result.",
                "so_what": "The barbell is now the default shape for a considered purchase: one asset that earns attention and a roster of creators that earns understanding.  The film cannot demonstrate a two-temperature espresso machine to somebody about to spend a thousand dollars, and the creators cannot get themselves talked about.  Neither half works alone, which is why the budget split between them matters more than either brief.",
                "do_this": "On your next launch, write the hero film brief and the creator brief in the same session and hand them to the same person to sign off, so the film sets up the exact demonstration the creators are being paid to deliver.",
            },
            {
                "title": "Duolingo gatecrashed New York Fashion Week with a jacket that says zhee-vahn-shee",
                "hook": "It found the one thing it sells that luxury fashion happens to need.",
                "stamps": [("ADWEEK · 8 SEP", "https://www.adweek.com/creativity/duolingo-creates-a-fashion-line-for-the-brands-you-cant-pronounce/")],
                "body": [
                    "Duolingo released The Phonetic Collection this morning: garments and bags printed with the phonetic spelling of luxury brand names.  A lime-green bag reading air-mess.  A jacket reading zhee-vahn-shee.  Designed by Megan O'Cain from the second season of Netflix's Next in Fashion, with outdoor advertising running across New York City this week.",
                    "Chief marketing officer Manu Orssaud gave the logic in one line: some of the most recognisable names in fashion are also some of the hardest to pronounce.  That is a genuine overlap between what the company sells and an event it was not invited to, which is what buys it the right to turn up at all.",
                    "The objects are the media buy.  A bag that reads air-mess only works if somebody photographs it and somebody else gets the joke, and the person who gets the joke is by definition someone who knows the brand and cannot say it — which is the download.",
                ],
                "flagnote": "No spend, units or engagement figures disclosed, and it launched the morning the piece ran.  It also trades on luxury trademarks Duolingo has no relationship with, which is worth flagging before anyone copies the mechanic.",
                "so_what": "Borrowing an event you were not invited to only works when you own something the event actually contains.  Duolingo did not buy a presence at fashion week, it found a problem inside fashion week that it is already in the business of solving, and made the solution photographable.  That is a cheaper route in than sponsorship and a much harder one to fake.",
                "do_this": "List the three biggest cultural events your customers attend that you have no budget for, then find the one small problem inside each that your product already solves, and make a physical object out of it.",
            },
            {
                "title": "TikTok Shop banned the note in the box asking for five stars",
                "hook": "Ten packing rules, no stated effective date, and no penalty schedule.",
                "stamps": [("PPC LAND · 6 SEP", "https://ppc.land/tiktok-shop-bans-review-bait-inserts-in-10-packing-rules/")],
                "body": [
                    "TikTok Shop published ten packing standards in its United States seller academy on 3 September.  Sellers may no longer enclose messages that request or incentivise positive reviews, or materials designed to draw them.  Also banned: shipping direct from another retailer, unauthorised marketing pamphlets, and price tags from elsewhere.",
                    "Two things are missing from the policy as published, and both matter if you advise a brand selling there.  There is no stated effective date and no penalty schedule.  TikTok Shop's account health system blocks new listings and campaigns at 150 points, but nothing in this document says what a breach of these rules costs.",
                ],
                "flagnote": "PPC Land reports an unresolved internal editorial note left inside the live policy text attached to the size and weight cutoffs, which suggests the document was published before it was finished.  Check the seller academy directly before advising anyone.",
                "so_what": "The insert card asking for a five-star review is one of the quietest ways brands have been buying their own ratings, and it has been standard in the box for years.  Removing it means the rating on your TikTok Shop listing starts reflecting what people thought rather than what you asked them to think, which will move some listings down before it moves any up.",
                "do_this": "Open the last three parcels your brand shipped and pull any insert that mentions reviews, then replace that ask with a post-purchase message that solves a problem — setup, sizing, returns — because a review you earn survives a policy change.",
            },
        ],
    },
    {
        "id": "onstream", "name": "ON STREAM", "page": "pg. 05",
        "note": "the live numbers, and what they are actually worth",
        "tint": None,
        "items": [
            {
                "title": "Sony's own broadcast peaked at 982,400.  Sony's own channel carried under a third of it",
                "hook": "You can own the event, the announcements and the trailers, and still watch other people's rooms take the audience.",
                "open": True,
                "stamps": [
                    ("STREAMS CHARTS · 4 SEP", "https://streamscharts.com/news/state-play-september-2026-viewership"),
                    ("ESPORTS CHARTS · 7 SEP", "https://escharts.com/news/blast-open-fall-2026-viewership"),
                ],
                "body": [
                    "Sony ran a State of Play showcase on 3 September, followed straight away by a State of Play Japan broadcast, covering more than thirty games.  Streams Charts has the two broadcasts reaching a <mark>peak of 982,400 viewers with more than 1.6 million hours watched</mark>.  The headline announcements were Final Fantasy VII Revelation, Metro 2039 and Until Dawn 2.",
                    "Now the number a brand should actually read.  <mark>The official PlayStation YouTube channel peaked at 304,500</mark>.  That is the company's own channel, showing the company's own event, and it accounts for about 31% of the total.  The other two thirds were watching somebody else's face in the corner of the screen, reacting.  Streams Charts named the British streamer Caedrel as the leading community caster and the top channel on Twitch.",
                    "For a sense of scale: 304,500 people on the official feed is about three and a half times a full Wembley Stadium, all watching at the same moment.  The 982,400 total is a little above the 849,574 that the entire BLAST Open Fall counter-strike tournament peaked at when it finished on Sunday, and that was a multi-day event across every channel and language showing it.",
                    "Streams Charts published no average concurrent figure, which is the number that would tell you whether people stayed.  Do the arithmetic and it does not settle cleanly either — 1.6 million hours across a stated two hours implies an average near 800,000, which would mean the audience sat at four fifths of its peak for the entire run.  The likelier explanation is that the combined broadcast ran considerably longer than two hours, not that the audience was that steady.  Ask for the average before you quote the peak.",
                ],
                "numbers": [
                    ("982.4K", "peak viewers across every channel showing State of Play — Streams Charts"),
                    ("304.5K", "peak on PlayStation's own YouTube channel, about 31% of that total"),
                    ("1.6M", "hours watched across the two broadcasts"),
                ],
                "flagnote": "The 982,400 is an aggregate across Sony's own channels plus every Twitch and YouTube creator co-streaming it, and is not comparable to a single-channel record.  The 304,500 is the one clean single-channel figure in the set.  Streams Charts did not publish the number of channels in the aggregate or any average concurrent viewers.",
                "so_what": "Sony owns the announcements, the trailers and the broadcast, and two thirds of the live audience still chose to receive all of it through somebody else.  That is not a failure, it is the distribution working — but it means the version of your launch that most people see has a stranger talking over it and cutting away to their own face.  If you plan an owned livestream and measure only your own channel, you will under-report your reach and over-estimate your control.",
                "do_this": "Before your next owned livestream, write a co-streaming permission into the plan on purpose — clear the footage for reaction, brief a handful of creators on timings and embargo, and measure your own channel and the creator channels as one number rather than two.",
            },
        ],
    },
    {
        "id": "watch", "name": "ONE TO WATCH", "page": "pg. 06",
        "note": "one creator with momentum, and who should be calling them",
        "tint": None,
        "items": [
            {
                "title": "ProjectAir turned an aerodynamics question into four million views, and sells his own kit off the back of it",
                "hook": "906,000 subscribers, a 4.0 million view breakout, and the sponsors on it are remote desktop software and a web browser.",
                "open": True,
                "stamps": [("YOUTUBE CHANNEL", "https://www.youtube.com/@Project-Air")],
                "body": [
                    "ProjectAir is James Whomsley, a British engineer who builds radio-controlled aircraft on camera.  906,000 subscribers.  The median across his last ten long-form uploads is <mark>785,966 views</mark>, which is already a serious channel rather than a promising one.  What makes him worth a call this week is what happened on 14 August.",
                    "For years the format was a superlative — the fastest, the biggest, the most powerful.  Then he posted Giant Circle Plane, which asks whether a circular wing flies better than a straight one.  It has done <mark>4,035,700 views</mark>, roughly five times his own median and his biggest video in over a year.  He followed it on 28 August with I made a Circle Plane, a second bite at the same question.  The shift is from stunt to a counter-intuitive engineering question with an answer at the end, and the answer is what people came for.",
                    "The commercial detail that matters more than the view count: he sells physical radio-controlled aircraft kits through his own shop, and the Circle Plane kit went on sale off the back of that video.  A creator who can move his own hardware to his own audience has already proved the thing every brand is trying to find out before it signs.",
                    "And look at what is currently sponsoring him.  AnyDesk, a remote desktop tool, on the Circle Plane video.  Opera, a web browser, on the monorail build.  Those are generic software reads on an audience that is disproportionately practising engineers, makers and people who own a 3D printer.  He already uses Bambu Lab printers, Easy Composites materials and Polymaker filament in the builds without those being the deal.",
                ],
                "watch": {
                    "label": "TOP VIDEO, LAST 3 MONTHS",
                    "title": "Giant Circle Plane",
                    "url": "https://www.youtube.com/watch?v=mohqFopl2uM",
                    "meta": "4,035,700 views · published 14 August 2026 · 23m 50s",
                    "note": "The circular-wing build that took a 785,000-view channel to four million, and sold a kit off the ending.",
                },
                "flagnote": "No publication has covered this channel.  The subscriber count, the view counts and the median across his last ten long-form uploads were read from YouTube's public video data on 8 September, not from a third-party tracker.  Upload dates were confirmed against the channel's own feed.",
                "so_what": "The tools in his builds are load-bearing — you cannot make the video without the printer, the composite and the design software, so the product is inside the engineering rather than read out over a title card.  He is currently selling that inventory to companies who would take any audience with a pulse, which means the right hardware brand can outbid the incumbent without paying a premium.  A creator who already sells his own physical product to this audience is the cheapest proof of conversion you will ever get before signing.",
                "do_this": "If you sell desktop 3D printers, design or simulation software, composites, test equipment or cordless tools, email him this week and buy a build where your product is the reason the thing flies — plus a co-branded kit through his own shop, so you can see the conversion rather than be told about it.",
            },
        ],
    },
    {
        "id": "money", "name": "THE MONEY", "page": "pg. 07",
        "note": "where the budget actually moved",
        "tint": None,
        "items": [
            {
                "title": "Anthropologie is spending on trainers to buy a better customer, not a bigger shoe business",
                "hook": "Sneaker customers up nearly 30 percent, in a market growing 1 percent.",
                "stamps": [("DIGIDAY · 7 SEP", "https://digiday.com/marketing/anthropologie-is-launching-nike-as-sneaker-shoppers-increase-nearly-30/")],
                "body": [
                    "Anthropologie started selling Nike yesterday — the first of nine styles landed on Monday, with the rest rolling out by 21 September behind a full digital campaign.  The reason is a cohort number rather than a category one.  The count of customers coming to Anthropologie specifically for trainers is up <mark>nearly 30% year over year</mark>, according to Jessica Irick Peek, its general merchandise manager for footwear and accessories.",
                    "Set that against the market.  Circana has American footwear sales up just 1% in the first half of 2026, with trainers and performance shoes up 6%.  So Anthropologie is growing its shoe customer roughly five times faster than the fastest-growing part of a flat market.",
                    "The build behind it took five years: footwear went from 8 stores to about 200 of roughly 250, and 40% of the trainer range is exclusive to the United States.  Its own-brand footwear customer count is up 23%, and its spun-off label Maeve is up 32%.  The company does over two billion dollars of revenue, around 70% of it from brands it owns.",
                    "The line that explains the whole spend: the shoe customer is the most valuable customer.  One in five apparel buyers also bought shoes, and one in ten new customers bought shoes in their first year.  Footwear is being funded as a way of acquiring a high-value shopper, which is also why the campaign sells outfits rather than shoes — Irick Peek says they have the most success with footwear when they tie it back to apparel.",
                ],
                "flagnote": "Single-source: every figure except the Circana market data comes from Anthropologie's own general merchandise manager.  Digiday has published a correction on this piece — the near-30% is the number of customers buying trainers, not trainer sales.  Quote it the corrected way.",
                "so_what": "A category can be worth funding because of who it brings through the door rather than what it sells, and that changes the creative brief completely.  If shoes are the acquisition route into a customer who then buys clothes, the film should never be a shoe film.  The metric that justified the budget is a customer count, so the work should be judged on new customers rather than units of footwear.",
                "do_this": "Ask your client which product line brings in their most valuable customers rather than their most revenue, then build this quarter's video around that line and agree up front that new customer count, not that product's sales, is how the work gets marked.",
            },
        ],
    },
    {
        "id": "format", "name": "FORMAT LAB", "page": "pg. 08",
        "note": "one format worth stealing this week",
        "tint": None,
        "items": [
            {
                "title": "Rothy's spent its biggest campaign ever on deliberately not casting creators",
                "hook": "Sixteen women, none of them influencers, and five paid Substack essays instead of a creator roster.",
                "open": True,
                "stamps": [("GLOSSY · 8 SEP", "https://www.glossy.co/fashion/at-its-10th-anniversary-rothys-is-launching-its-biggest-campaign-ever/")],
                "body": [
                    "Rothy's launched Point of View today for its tenth anniversary, its most expensive and widest campaign to date, across video, social, print and outdoor, tied to a third-generation relaunch of its Point shoe.  The company does over 225 million dollars a year, runs 40 stores, and takes just under a third of revenue through wholesale.",
                    "The casting is the format.  Glossy reports the team <mark>intentionally shied away from traditional influencers and content creators</mark>, casting 16 women who are artists, photographers, writers, ceramicists and journalists — ESPN's Malika Andrews, the artist Jane Moseley, the actress Nathalie Love, the producer Julianne Jordan — specifically to look different from every other creator-led campaign in the category.",
                    "Anna Doré, vice president of brand, ties the spend directly to shelf space: when you're on shelves all over the place, you need a strong brand identity more than ever.  Wholesale means your product sits next to competitors with nothing but the brand doing the arguing.",
                    "And the channel choice follows the casting.  Rothy's has no Substack of its own, so it sponsored five Substack writers, including Emily Sundberg of Feed Me and Erika Veurink of Long Live, for reflective sponsored essays.  It bought a register — considered, written, slow — that a creator video cannot produce, from people whose readers turn up for exactly that.",
                ],
                "flagnote": "Single-source: Doré is the only named voice in the piece, and the campaign launched the day it ran.  No budget figure, no impressions and no performance data exist yet.  This is a strategy worth examining, not a proven result.",
                "so_what": "When everybody in your category casts creators, casting a creator stops being a differentiator and becomes the cost of entry.  Rothy's paid a premium for people whose credibility comes from a craft rather than an audience, which is a bet that recognisability is now worth less than being unmistakable.  The Substack half is the same bet in a different medium — buying a reading pace rather than a reach figure.",
                "do_this": "On your next campaign, cast one person from outside the creator economy who is genuinely excellent at the thing your product is for — a chef, a mechanic, a climber, a restorer — and put them in the same slot you were going to fill with a creator, then compare the two on brand recall rather than views.",
            },
        ],
    },
]

FORECAST = [
    {
        "confidence": "LIKELY",
        "window": "by 31 January 2027",
        "headline": "Break length becomes a line item in streaming deals",
        "body": "Ampere has now put a public number on how many minutes of advertising each service runs, and the gap between Paramount+ at nine minutes an hour and Netflix at under two and a half is too large for buyers to keep ignoring.  Once a clutter figure exists in the open, it gets negotiated.  Expect break length and position inside the break to start appearing in written terms alongside price, the same way viewability did a decade ago.",
        "do": "Put the clutter figure into your next streaming contract as a stated condition now, while nobody is defending it.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "by 30 June 2027",
        "headline": "A major advertiser labels its own AI-made ad, and the label becomes the story",
        "body": "FreeWheel's numbers say viewers minded AI creative far less than buyers assumed.  Raptive's say trust falls by close to half when people suspect it.  Both can be true if the variable is whether it is detected, which makes voluntary disclosure the single most interesting untested move in the category.  The first large brand to put a label on the work will run the experiment that everybody else is currently avoiding, in public.",
        "do": "Decide your own disclosure position on AI-assisted creative this quarter, in writing, before a client asks you in a meeting.",
    },
    {
        "confidence": "LIKELY",
        "window": "by 31 March 2027",
        "headline": "Retargeting budgets keep draining into logged-in environments, and bots get the blame",
        "body": "Two agencies have now said publicly that bot contamination pushed clients out of open-web retargeting and into retail media and social.  The economics only run one way: filtering makes the audience smaller and dearer, while a login makes it verifiable.  The interesting part is that the money moving into social and creator video will be described as a performance decision when it is really a data hygiene one.",
        "do": "Get your own quarterly split of logged-in versus open-web spend on record now, so you can tell the difference later between a budget that grew and a budget that fled.",
    },
    {
        "confidence": "LONG SHOT",
        "window": "by 31 December 2026",
        "headline": "A brand buys the co-stream roster rather than the broadcast",
        "body": "Sony's own channel took under a third of its own showcase audience, and that split is now normal for anything gaming-adjacent.  The obvious response is to stop treating co-streamers as free distribution and start buying them as the primary placement, with the official feed as the source rather than the product.  Nobody has done it properly yet, mostly because the buying and the production sit in different departments.",
        "do": "Ask whoever runs your owned livestreams what the creator channels did last time, and if nobody measured it, measure it next time.",
    },
]

TLDR = [
    "Bots and AI agents now make up more than half of all web requests, and one agency saw the cost of reaching a thousand people rise 20% once it filtered them out of its retargeting lists.  Move that budget into places where people log in — YouTube, Meta, retail media — instead of trying to clean the list.",
    "Streaming ad loads rose 18% between January and August, with Paramount+ at nine minutes an hour and Netflix under two and a half, and no correlation between what a tier costs and how much advertising it carries.  Write break length and your position in the break into your next streaming deal.",
    "48% of media buyers assume viewers dislike AI-made ads while only 10% of viewers said they did, though a separate study found trust halves when people suspect it.  Run one blind test this month to find out whether your audience can tell before you decide what the audience thinks.",
    "Sony's State of Play peaked at 982,400 viewers, but its own PlayStation channel carried only 304,500 of them.  Plan your next owned livestream with co-streamers briefed in advance, and report your channel and theirs as a single reach number.",
    "Omaha Productions spent two years making a 15-minute film to announce a broadcast schedule, and its president says the film is why famous people agree to appear on the show.  Brief your most boring announcement of next year as entertainment with a guest list, and start booking the guests now.",
    "Anthropologie added Nike because the number of customers coming to it for trainers rose nearly 30% in a market growing 1%, and it treats footwear as a way to acquire high-value shoppers.  Find the product line that brings your client their best customers and build this quarter's video around that, judged on new customers rather than units.",
    "Rothy's cast 16 non-creators and sponsored five Substack essays for its biggest campaign ever, on the view that creator casting no longer differentiates anyone.  Cast one genuine practitioner from outside the creator economy in your next campaign and compare it on brand recall.",
]

SHARE = [
    {
        "who": "JARED · CEO",
        "angle": "The two-year promo is a recruiting tool, and the cameo list is the product it buys.",
        "post": "Peyton and Eli Manning spent roughly two years making a 15-minute film whose only job is to announce which football games they are commentating on this season.\n\nAbout 40 cameos. Glen Powell, Anne Hathaway, Paul Rudd, Larry David, Jon Hamm. The NFL commissioner has a starring role.\n\nThe Hollywood Reporter ran it this morning. Their head of production, Therese Andrews, says planning started in late 2024 and shooting began at the 2025 Pro Bowl, because that weekend puts a year's worth of gettable famous people in one building.\n\nThen the company president, Jamie Horowitz, says the thing I keep turning over. Part of the reason Paul Rudd or Kevin Hart appears on the Manningcast, he says, is because we do things like this.\n\nSo the film is not advertising the show. The film is how they book the show.\n\nThat inverts how most of us budget. We fund the thing, then fund a smaller thing to tell people about it. Here the smaller thing is the recruitment department, and its audience is about forty people with agents.\n\nI don't know how many brands have a guest list worth building a two-year asset around. Probably fewer than think they do.\n\nBut if the promo is what gets next year's cast to answer the phone, it stopped being marketing spend a while ago.",
        "why": "It reframes a promotional film as a recruiting cost, which gives a client a reason to fund owned video that has nothing to do with reach.",
    },
    {
        "who": "JAMES · CREATIVE DIRECTOR",
        "angle": "The industry's fear of AI creative is 38 points larger than the audience's, and the real variable is whether the seams show.",
        "post": "48% of media buyers say they assume viewers find AI-generated advertising off-putting. 10% of viewers said they disliked the AI-made advertising they had actually seen.\n\nThat is a 38 point gap between what my side of the table believes and what the audience reported.\n\nThe figures are from a FreeWheel report published Friday. 226 media buyers and 50 sellers surveyed by AdExchanger, and 2,496 US adults surveyed by Dynata, all in April.\n\nI want to be careful with this, because the easy read is wrong and it flatters people who sell AI tools, FreeWheel included.\n\nThe viewers were asked about AI advertising they had seen and clocked as AI. So the 10% measures reactions to work where the seams showed. It says nothing about work good enough that nobody noticed.\n\nAnd in the same piece, Raptive surveyed 3,000 adults and found that suspecting content was AI-made cut trust by close to half, and cut ad effectiveness 14% in purchase consideration.\n\nPut those together and the variable is not the tool. It's detection.\n\nWhich is a craft problem, and craft problems are the ones I'm supposed to be good at. I've spent a year treating this as an ethics argument. It might have been a finishing argument the whole time.",
        "why": "A creative director admitting the industry's caution outran the audience's, then landing on detection rather than ethics, is specific and uncomfortable in a way a summary is not.",
    },
    {
        "who": "LAWRY · LEAD VIDEO EDITOR",
        "angle": "Two thirds of a launch audience watched the trailer with someone talking over it, and nobody mixes for that.",
        "post": "Sony's State of Play peaked at 982,400 viewers last week. Its own PlayStation YouTube channel carried 304,500 of them.\n\nThat's 31%. The other two thirds watched Sony's trailers inside somebody else's stream, with a face in the corner and a person talking over the top.\n\nFigures from Streams Charts.\n\nI think about this more than is healthy, because of what it does to a mix. You spend days on a trailer's sound. The low end under the logo. The half-second of silence before the title card, which is the whole reason the title card works.\n\nThat silence is where a co-streamer says something. Every time. It is the most reliable place in the edit for someone to talk, because it's the only gap.\n\nAnd the picture gets squeezed into a box with a webcam over one corner, usually the bottom right, which is where a lot of us like to put the date.\n\nI'm not arguing you should cut for that. A trailer built for a reaction stream is a worse trailer.\n\nBut I've never once been briefed on it, and two thirds of the audience is a strange thing to have never been briefed on.",
        "why": "It is a specific edit-suite observation about mixing and framing that turns a viewership split into a technical brief nobody writes.",
    },
]
