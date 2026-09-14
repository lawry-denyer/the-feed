# -*- coding: utf-8 -*-
"""Content for THE FEED — issue data only.  The render spec lives in build_feed.py."""

ISSUE = {
    "date_iso": "2026-09-14",
    "kicker": "Crux Media // Monday 14 September 2026",
    "tagline": "What brands did on YouTube yesterday, and whether it worked.",
    "pace": "STEADY",
    "next_drop": "Next drop: Tuesday, 06:30 MT",
}

LEAD = {
    "headline": "CREATORS ADDED 55 PERCENT MORE PURCHASE TAGS TO THEIR TIKTOKS LAST QUARTER, AND THE TAGGED POSTS LOST 41 PERCENT OF THEIR STANDING AGAINST THE AVERAGE POST",
    "deck": "A benchmark across 58,037 US TikTok posts found supply and response moving in opposite directions.  More creators put a buy button on the video every month.  The tagged videos slid further behind everything else on the platform.  The typical purchase-tagged post earns a 1.4 percent engagement rate against 6.4 percent for the typical post across the whole sample, which means the tag is not a feature you add to a video.  It is a thing you trade the video for.",
    "stamps": [
        ("NET INFLUENCER · 12 SEP", "https://www.netinfluencer.com/tiktok-audiences-are-pulling-toward-six-formats-and-scrolling-past-the-ones-built-to-sell-q2-editing-format-index-finds/"),
    ],
    "body": [
        "Net Influencer published its Q2 2026 TikTok Editing Format Index on Saturday, built with data from the TikTok social listening firm dig.  It tracks <mark>20 editing formats across 58,037 US TikTok posts from the first half of 2026</mark>, and scores each format on two questions every quarter: are more creators making it, and are audiences responding to it more than to the average post.  Engagement rate here means likes plus comments as a share of views, which is the definition the index uses throughout.",
        "The finding that should change a budget this week is the one about purchase tags.  <mark>Shoppable Video Tagged — video with a visible purchase tag on it — grew 55 percent in post count, to 683 posts, while its engagement rate against the average post fell 41 percent.</mark>  Live Shopping shows the same shape from 46 posts — below the index's own 300-post reliability bar, so read it as a hint rather than a finding: share of posts up 27 percent, engagement rate down 73 percent.",
        "Now the absolute numbers, because the percentage changes on their own could describe a format falling from a great height.  They do not.  <mark>The typical purchase-tagged post in the sample earned a 1.4 percent engagement rate.  The typical post across the whole collection earned 6.4 percent.</mark>  So tagged video was already the weakest thing on the board, and it got weaker while more people made it.",
        "The index is careful about not letting a handful of viral posts carry a format, and that matters here.  Every format is rescored with the top one percent most-viewed posts removed, and formats under 300 posts in a quarter are marked directional rather than solid.  Shoppable Video Tagged has 683 posts, so it clears that bar.",
        "Here is the mechanism, and it is not that people hate shopping.  The purchase tag is the first thing a viewer reads about the video, before a single frame has made its case.  It answers the question every scroll is really asking — is this for me or is this for them — and it answers it the wrong way, instantly, on the thumbnail.  You have not added a way to buy.  You have added a label saying this is an advertisement, and you have put it in the one position where a person decides whether to keep watching.",
        "Which is why the honest read is not stop selling.  It is that the tag has to sit on top of something the audience already wants to watch, rather than being the reason the post exists.  The index says exactly this in its own recommendations: the question to ask of a brief is whether a tagged post is pure shopping, built around the tag alone, or a hybrid where the tag sits on a carousel or a fast-cut edit that people already respond to.  Same tag, different host.",
    ],
    "numbers": [
        ("58,037", "US TikTok posts across 20 editing formats in the index"),
        ("1.4%", "engagement rate on the typical tagged post, against 6.4% across the whole sample"),
        ("55%", "growth in tagged post count while their standing fell 41%"),
    ],
    "flagnote": "This is Net Influencer's own quarterly benchmark, produced with dig, a firm that sells TikTok social listening — the publication and its data partner both benefit from brands treating format analysis as a thing worth paying for, and the full board of all 20 formats sits behind a lead-capture form.  We could find no independent coverage or second source for the index, so every figure here traces to one publisher.  The sample is US posts only, engagement rate is likes plus comments over views rather than any measure of sales, and the index does not publish how the percentage changes were calculated against the raw rates.",
    "so_what": "Everyone has been treating commerce features as free upside — same video, one more button, more revenue.  This says the button is not free, and that it costs you at the only moment that matters, which is the half second before somebody keeps watching.  A tag tells a viewer what the video is for before the video gets to argue.  That is the whole finding, and it applies to any format where the sell is visible in the first frame rather than earned by the fourth.",
    "do_this": "Pull every purchase-tagged post your brand ran last quarter and judge it against the 1.4 percent benchmark for tagged posts rather than against your overall average, so you can see which ones actually beat their own format.  Then take one upcoming brief and rewrite it so the tag sits on a format people already watch — a carousel or a fast-cut edit — instead of commissioning a post whose only reason to exist is the tag.",
}

SECTIONS = [
    {
        "id": "ws", "name": "W'S", "page": "pg. 02",
        "note": "what worked, and the exact reason it worked",
        "tint": "blue",
        "items": [
            {
                "title": "The only format at scale gaining on both counts is still images, and a 208-follower account used it to pull 1.4 million views",
                "hook": "Photo carousel posts nearly doubled last quarter and gained on both measures — more creators making them, more people responding.  Fifty-nine percent came from accounts under ten thousand followers.",
                "open": True,
                "stamps": [
                    ("NET INFLUENCER · 12 SEP", "https://www.netinfluencer.com/tiktok-audiences-are-pulling-toward-six-formats-and-scrolling-past-the-ones-built-to-sell-q2-editing-format-index-finds/"),
                ],
                "body": [
                    "From the same index as the lead, the other end of the board.  <mark>Photo Carousels — a swipeable slideshow of still images — went from 717 posts in the first quarter to 1,317 in the second</mark>, a rise of 84 percent against 22 percent for the sample as a whole.  Their share of all posts collected each month rose 20 percent and their engagement rate against the average post rose 15 percent.  They were <mark>the only format with 300 or more posts to gain on both measures</mark>, and both gains held after the top one percent most-viewed posts were stripped out.",
                    "The distribution is the part worth staring at.  <mark>Fifty-nine percent of carousel posts in the sample came from accounts under 10,000 followers</mark>, and accounts under 1,000 were the single largest group.  The highest-reach small account in the sample had <mark>208 followers and drew 1.4 million views at a 28.4 percent engagement rate</mark>.  The index names a live example of the same shape: the account cupcakecowgirl6, 268 followers, 147,832 views, a 25.5 percent engagement rate.",
                    "Two things are true at once there, and only one of them is comfortable.  A format that rewards accounts with no audience is a format where the work is doing the reaching rather than the follower count, which is the thing every brand says it wants.  It is also a format with no production floor, which means your agency cannot charge for it and your competitor can make forty of them this week.",
                    "The mechanism is pacing, and it is the reverse of everything video craft is built on.  In a cut video the editor controls when each thing arrives.  In a carousel the viewer controls it — they swipe when they are ready, linger on the one that interests them, and leave when they are done.  Nobody is being held.  So the format that gives up the single lever an editor is paid to operate is the one gaining on both signals.",
                    "Worth noticing what that implies about why it works for small accounts specifically.  A carousel cannot be judged on production value, because there is barely any to judge.  It gets read on whether the thing in the pictures is interesting, which is the one contest a 208-follower account can win against a brand with a crew.",
                ],
                "flagnote": "Single-sourced to Net Influencer's own index, produced with the social listening firm dig, which sells the data the index demonstrates.  The 208-follower example is the highest-reach small account in their sample rather than a typical result, and no brand or campaign figures are attached to any of it — every number here is organic creator posting, not paid work.",
                "so_what": "The cheapest format on the platform is currently the one gaining fastest, and the reason is that it hands pacing to the viewer instead of taking it from them.  That is a real trade rather than a free win: you give up the ability to build to something, and you get back a format people finish because they set the speed.  For a brand it changes what a test costs — you can put ten carousels out for less than one edit, and find out which idea people actually want before you shoot anything.",
                "do_this": "Take the three best-performing videos your brand made this year and rebuild each one as a photo carousel this week, using frames you already own, then run them as ordinary organic posts.  Compare each against what a carousel usually earns rather than against your video average, and use whichever wins to decide what gets a full shoot next quarter.",
            },
            {
                "title": "Old Navy put its back-to-school campaign on one creator and got a 22 percent traffic lift, which is not the number the company most needs",
                "hook": "Over 100 million views, 1.4 billion impressions, and a 22 percent jump in traffic to the kids' range.  In the quarter before it launched, sales at stores open a year or more fell 4 percent.",
                "stamps": [
                    ("MARKETING DIVE · 11 SEP", "https://www.marketingdive.com/news/old-navys-mrbeast-deal-boosts-engagement-amid-bigger-bet-on-creators/830100/"),
                ],
                "body": [
                    "Peter Adams reported this at Marketing Dive on Friday.  Old Navy built its 2026 back-to-school campaign around MrBeast — the first time the brand has anchored a back-to-school push on a single creator — and says the result was <mark>an over 22 percent jump in traffic to its kids' range online in the days immediately following launch</mark>.  The videos have done <mark>over 100 million global views and 1.4 billion impressions on YouTube</mark>.  Damon Berger, senior vice president and head of shared marketing services at parent company Gap Inc: the numbers are staggering.",
                    "The structure is worth copying even if the numbers are not yet bankable.  A single creator as the anchor rather than a roster, comedic content rather than apparel photography, and participation built in — a sweepstakes, meme-themed trivia questions with cash and gift cards for correct answers, and free lunch for a year given to a middle school in Kansas.  Berger says the previous back-to-school campaigns were the more highly produced ideas, and that this one is about more storytelling from the authentic lens to the communities they are trying to reach.",
                    "Now the context the piece puts right next to it, which is why this sits here with a caveat rather than as a clean win.  <mark>The campaign follows a 4 percent decline in comparable sales — takings at stores open at least a year — at Old Navy in the second quarter</mark>, extending a slump at the largest brand in the Gap portfolio, after summer marketing failed to deliver an expected traffic bump.  Gap Inc chief executive Richard Dickson said on the earnings call that the impact of the MrBeast work and a Cardi B denim campaign on sales likely will not be clear until the next round of earnings.",
                    "So read the metric selection as information.  Traffic in the days immediately after launch is the fastest thing a big creator moves and the easiest thing to measure while you are waiting.  It is also the number a company reaches for when the slower one has not arrived.  That is not dishonest — Dickson said plainly that the sales read is a quarter away — but it does tell you what stage this is at.",
                    "One more figure in the piece that deserves less weight than it will get: 91 percent of surveyed parents report their teenage children influence their brand preferences, from research by HarrisX and Allison Worldwide.  No sample size, no field dates and no mechanism behind it.  It is a fine thing to believe and a poor thing to plan against.",
                ],
                "flagnote": "The 22 percent traffic figure, the view count and the impressions all come from data Old Navy gave Marketing Dive, with no measurement vendor, no methodology, no control group and no stated length for days immediately following launch.  Nothing in the reporting separates the creator effect from back-to-school seasonality or from the sweepstakes mechanic running alongside it, and Gap Inc's own chief executive says the sales impact will not be readable until the next earnings round.",
                "so_what": "A single-creator anchor with a giveaway attached will reliably move traffic within days, because that is what a very large audience arriving at once does.  Whether it moves the business is a different measurement on a different clock, and the gap between those two clocks is where most creator campaigns get declared a success or a failure prematurely.  Decide which number you are buying before you buy it, not after the first one arrives.",
                "do_this": "Before your next creator campaign goes live, write down the two numbers you will judge it on — the fast one and the slow one — with the date you will read each.  Put the slow one in the same document as the budget approval so nobody can quietly settle for the traffic spike when the quarter closes.",
            },
        ],
    },
    {
        "id": "ls", "name": "L'S", "page": "pg. 03",
        "note": "what broke, and the failure mode underneath it",
        "tint": "pink",
        "items": [
            {
                "title": "Wrong brief: a hundred creators went to the US Open, a few people nobody credentialed stopped play, and every creator wore it",
                "hook": "Brands briefed deliverables and talking points.  Nobody briefed the room.  Play halted during Naomi Osaka's opening match because of flash photography from a hospitality suite.",
                "open": True,
                "stamps": [
                    ("DIGIDAY · 14 SEP", "https://digiday.com/media/what-weve-learned-from-the-creator-snafus-at-this-years-us-open/"),
                ],
                "body": [
                    "Alyssa Mercante reported this at Digiday this morning, talking to six marketing executives and creator agents.  The United States Tennis Association invited <mark>around 100 credentialed creators</mark> to this year's US Open, <mark>nearly double the number in 2025</mark>, when it first built a formal cohort that gave creators credentials and gave brands a list of who was attending.  The USTA said last year that the 2025 cohort generated <mark>more than 5.5 million social engagements</mark>.  ESPN's opening-day coverage this year drew 13 percent more viewing than last year.",
                    "Then, during Naomi Osaka's opening match on 31 August, play was temporarily stopped because several people in a hospitality suite took flash photos during play.  A separate clip went round of a woman using a ring light to photograph herself mid-match, and did most of the reputational damage.  Osaka, asked about it afterwards, said people attending should respect the sport and read up on the etiquette.  The Daily Mail ran the line that influencers were killing the US Open.",
                    "Here is the detail that makes this a briefing failure rather than a creator failure.  <mark>ESPN reported that the people responsible were not USTA-credentialed at all</mark> — they were not part of the official cohort.  The backlash landed on the whole cohort anyway.  A hundred people who followed the rules absorbed the reputation cost of a handful who were never briefed on any.",
                    "Cayley Stonehouse, senior social media strategist at Gupta Media, names the gap exactly.  The relationship with a creator should go beyond just deliverables and talking points, she says: it should include the rules of the sport, etiquette, when and where they should be capturing content and what's expected of them while they're there.  Tennis is obviously not a sport like soccer or football where it's super rowdy all the time.  She adds that it is the brand's job to brief this, and that it does not always happen.",
                    "The rest of the panel splits the fix into two parts.  Becky Owen, chief marketing officer at Billion Dollar Boy, on the standard: we mandate strict etiquette protocols that protect the craft of the athletes and the experience of paying fans.  Gabby Gamad, chief operating officer and co-founder of LV8, warns against over-correcting into rules so restrictive the creator cannot work.  And Beni Brown, global director of strategy at Buttermilk, gives the one-line test: the backlash comes when it stops being about the game.  Emily Steele, chief executive and co-founder of Hummingbirds, on selection rather than volume: I don't think the solution is fewer influencers at events like this, it's the right influencers who have a relationship to what they're covering, not influencers who were dropped in for the weekend.",
                    "For contrast, Digiday points at the 2026 World Cup, where FIFA gave TikTok and YouTube creators unusually deep access to stadiums and matches and the content outperformed celebrity endorsements.  Same idea, different room, and the room is the variable.",
                ],
                "flagnote": "The creator count and the 5.5 million engagements figure both come from the USTA rather than from independent measurement, and the engagement number describes the 2025 cohort, not this year's.  No brand or creator responsible for the disruption has been named, the attribution that they were uncredentialed rests on ESPN's reporting, and the six executives Digiday spoke to all sell creator marketing services.  They also broadly agree the backlash was an overreaction, which is a view held by people with an interest in it being one.",
                "so_what": "A creator brief is usually a list of what to make and what to say, and it almost never covers how to behave in the physical space you have bought access to.  That is fine on a set you control and dangerous at somebody else's live event, where the etiquette is invisible to anyone who did not grow up in the sport and obvious to everyone who did.  The reputational damage does not stay with the person who broke the rule either — it attaches to the format, which means the next brand to buy event access pays for it.",
                "do_this": "Add an etiquette page to your event creator brief before your next live access deal: what is prohibited during play, where capture is allowed, what to do if an official approaches, and who at your company they call.  Then check whether anyone attending on your brand's tickets is outside the organiser's credential list, because those are the people no one has briefed.",
            },
            {
                "title": "Wrong platform: Meta made ads about its own safety standards and TikTok refused to run them as political content",
                "hook": "A 17 billion dollar settlement, five billion more promised if rivals follow, and the creative could not be placed on the rival it was aimed at.",
                "stamps": [
                    ("TUBEFILTER · 11 SEP", "https://www.tubefilter.com/2026/09/11/meta-tiktok-trust-safety-settlement-declined/"),
                ],
                "body": [
                    "Sam Gutelle wrote this up at Tubefilter on Friday, following Axios.  Last month Meta announced a <mark>17 billion dollar settlement</mark> with dozens of state attorneys general, agreeing to add safety features across its platforms — stricter time limits for underage users, silenced notifications during school hours, and a night mode limiting access in the predawn hours — and described those updates as a new industry standard.  <mark>Meta has pledged a further 5 billion dollars if other large technology firms adopt the same standard</mark> — it would rather spend that than be the only company carrying the cost, so it is buying hard for company.",
                    "Part of the persuasion was media.  Meta bought ads on rival platforms promoting the standard.  <mark>TikTok rejected them, classifying them as political content</mark>, which its guidelines do not permit as paid advertising.  TikTok's line: the nature of political ads is not something we believe fits the TikTok experience.  Meta's response, per Axios: it is disappointing that YouTube and TikTok have chosen not to engage.  That is the only mention in the reporting of YouTube also declining, and no reason for it is given.",
                    "Strip out the corporate feud and what is left is a placement lesson that applies to brands with no lobbying interest whatsoever.  Meta produced creative whose entire job was to be seen by a competitor's users, and discovered at the buying stage that the competitor's definition of political extends to industry-policy and child-safety messaging.  That is a much wider net than most planners assume political means.",
                    "The failure mode is that platform policy was treated as a distribution question rather than a creative one.  Policy decides what can be made, not just where it runs, and it is knowable before anyone writes a script.  Nobody checked, or somebody checked and shipped anyway.",
                    "Be fair about the read, though.  This was probably always partly a message aimed at regulators and press rather than only at TikTok's users, and a rejection is itself a story Meta can point at.  It still cost real production money to learn a rule that a pre-clearance conversation would have surfaced for nothing.",
                ],
                "so_what": "Any brand running purpose, safety, sustainability or policy-adjacent creative has a placement risk it has probably not priced, because platforms define political far more broadly than marketers do and they apply it at the ad review stage, after the work exists.  The cost is not the rejection.  It is that the campaign was built around a channel it turned out it could never run on, and you find out at the point where changing the plan is most expensive.",
                "do_this": "Before you brief any campaign that touches a social issue, industry standard or regulation, send the core message in writing to each platform's ad policy team and get the read back first.  Keep the answers in the brief so the creative team knows which platforms are already closed before they start.",
            },
        ],
    },
    {
        "id": "moves", "name": "MOVES", "page": "pg. 04",
        "note": "platform, policy and legal changes that alter what you can make and buy",
        "tint": None,
        "items": [
            {
                "title": "Roblox is opening daily cash payouts to US creators and retiring the system that paid them in batches",
                "hook": "1.7 billion dollars paid out in twelve months.  From December, US creators who opt in get dollars every business day as each payment clears a hold.",
                "stamps": [
                    ("ROBLOX NEWSROOM · 11 SEP", "https://about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play"),
                    ("ROBLOX DEVFORUM · 11 SEP", "https://devforum.roblox.com/t/introducing-roblox-wallet-and-card-get-paid-faster/4865505"),
                    ("TUBEFILTER · 11 SEP", "https://www.tubefilter.com/2026/09/11/roblox-developers-conference-2026-game-apps-creator-payouts-roblox-wallet-roblox-card/"),
                ],
                "body": [
                    "Announced at the Roblox Developers Conference on Friday.  Roblox is launching a Wallet and, in 2027, a card.  <mark>From December 2026, US-based independent creators aged 18 and over can opt in to receive earnings in dollars every business day</mark> as holds clear, with a hold period of up to 30 days, after identity verification.  The existing Developer Exchange programme, which converts Robux — the platform's internal currency — into cash in batches, <mark>sunsets in mid-2027</mark> in the United States and later elsewhere.  The conversion rate is unchanged at 0.0038 dollars per Robux.",
                    "The scale behind it: <mark>5 billion dollars paid to creators since the exchange launched in 2013, and about 1.7 billion of that in the twelve months to 30 June 2026</mark>.  Roblox reported 29 billion player hours last quarter across more than 180 countries.  A separate incentive programme generated more than 300 million Robux in creator earnings in its first four months, about 1.1 million dollars at that rate — our arithmetic.",
                    "Also announced, and arguably the bigger structural change: Roblox says developers will be able to release their experiences as standalone apps across PC, mobile and consoles, with a browser player by the end of 2026 and offline play in mid-2027.  A thing you built inside Roblox stops being only a thing inside Roblox.",
                    "For a brand funding a Roblox build, the payment change is a negotiating fact rather than a headline.  A developer paid daily has different cash flow from one paid in batches, which changes what a deposit is worth, how long a build can run before the first invoice, and how much of the risk the studio can carry.  The standalone app route changes something else — what you are commissioning may end up with a life outside the platform you commissioned it for, and nobody's current contract says who owns that.",
                ],
                "so_what": "Payment terms are the quietest part of any creator or developer deal and the part that moves fastest when a platform changes them.  When the people you commission get paid daily rather than in lumps, the advance you are offering is worth less to them and your hold over the schedule weakens with it.  The standalone app announcement is the one to actually think about, because it turns a platform build into a portable asset midway through a lot of contracts that never imagined one.",
                "do_this": "If you have a Roblox build in flight or in contract, ask your developer this week whether they intend to opt into daily payouts, and get the distribution rights for a standalone version written down before mid-2027 rather than after.",
            },
            {
                "title": "Raptive launched a creator community app and is splitting ad revenue down the middle",
                "hook": "Fifty-fifty, free for creators and for fans, no paid tier.  More than 150 communities joined since launch.",
                "stamps": [
                    ("PR NEWSWIRE · 9 SEP", "https://www.prnewswire.com/news-releases/raptive-launches-raptive-community-for-the-next-era-of-creator-growth-302872844.html"),
                    ("NET INFLUENCER · 14 SEP", "https://www.netinfluencer.com/raptive-launches-ad-supported-community-platform-giving-creators-a-50-50-revenue-split/"),
                ],
                "body": [
                    "Raptive, which represents more than 7,000 sites and reaches 224 million monthly unique visitors, has launched Raptive Community — an app where creators run their own community space, monetised by advertising from day one rather than by subscriptions.  <mark>Creators take a 50-50 share of the advertising revenue.</mark>  It is free for creators and free for fans, with no paywall and no paid tier.  <mark>More than 150 creator communities have joined since launch</mark>, including Melani Sanders of the We Do Not Care Club, Lourd Asprec, Sally's Baking and Skinnytaste.  Raptive says it has paid out more than 4 billion dollars to creators and publishers to date.",
                    "The interesting decision is the absence of a subscription.  Almost every community product of the last three years asked the audience to pay, which caps the community at the people willing to, and quietly turns the creator into a retention manager.  Advertising-funded means the community can be as big as it can get, and the creator's incentive is growth rather than churn management.",
                    "For a brand, this is a new place to buy that did not exist last week, and the pitch is context: people talking to each other about one subject, inside a space a creator owns and moderates.  Whether it is worth more than the same audience on a feed depends entirely on inventory and measurement that do not exist yet.",
                    "The obvious risk is the one every community product has.  Advertising-funded free communities grow until the advertising has to pay for the moderation, and the point where those two lines cross is where the experience usually changes.",
                ],
                "so_what": "A creator with a community app has a direct line to their audience that no feed ranking sits in front of, which makes it more durable than a follower count and harder to buy by the post.  The fifty-fifty split matters because it tells you the creator's incentives are aligned with keeping the space worth being in, rather than with squeezing it.  Treat it as an early test budget, not a channel.",
                "do_this": "Check this week whether any creator you already pay is standing up a community space, and ask what advertising inside it costs before it gets priced by a media seller.  Buy one small test and judge it on comments and repeat visits rather than reach.",
            },
            {
                "title": "OpenAI's next ad format keeps the click inside ChatGPT instead of sending it to your site",
                "hook": "The button opens a conversation with your own agent rather than a landing page.  Wayfair is trialling it.",
                "stamps": [
                    ("DIGIDAY · 14 SEP", "https://digiday.com/marketing/openais-next-chatgpt-ad-format-click-to-chat-not-to-site/"),
                ],
                "body": [
                    "Digiday reported this morning on the next format OpenAI is testing inside ChatGPT.  Instead of a call to action that sends someone to the advertiser's website, the button opens a branded chat interface with the brand's own agent, inside ChatGPT.  Chief financial officer Sarah Friar described the direction at the Goldman Sachs Communacopia conference on 8 September, calling the current ads a basic starting point with early indications of what formats built for this environment become.  It is roughly seven months since ChatGPT ads launched.",
                    "No pricing, no rates, no user or advertiser counts have been disclosed.  It is with select clients, and Wayfair has confirmed it is trialling.",
                    "The closest existing thing is a click-to-message ad, where the button opens a chat thread rather than a page.  Those have been around for years and the thing that decides whether they work has never been the ad.  It is whether there is a competent thing on the other end of the conversation at the moment somebody opens it.",
                    "So the requirement this creates is not creative.  It is that you need a conversational agent that knows your catalogue, your stock and your prices, and a route from that conversation to a human or a checkout.  A brand without one is buying a button that opens an empty room.",
                ],
                "so_what": "Every ad format that ends in a conversation moves the hard part from the media buy to operations, because the ad works exactly as well as the response behind it.  This is the same shift retailers went through with chat on their own sites, arriving in a place where the audience is much larger and far less patient.  The brands that win the first year of this will be the ones who already had the agent, not the ones with the better creative.",
                "do_this": "Work out this week whether your brand could answer a stranger's product question end to end without a human, and write down the three questions it would fail on.  Fix those before you buy any format that opens a conversation.",
            },
        ],
    },
    {
        "id": "onstream", "name": "ON STREAM", "page": "pg. 05",
        "note": "the live numbers, and what they are worth to a sponsor",
        "tint": None,
        "items": [
            {
                "title": "The Overwatch World Cup final peaked at 349,275, and the tournament put up 90 percent more hours watched than 2023 largely by making the matches longer",
                "hook": "Esports Charts says so itself.  Group matches moved from best-of-three to best-of-five, so there was more broadcast to watch.  Hours watched rose 90 percent.  Peak viewers rose 5.8 percent.",
                "open": True,
                "stamps": [
                    ("ESPORTS CHARTS · 27 AUG", "https://escharts.com/news/overwatch-world-cup-2026-group-stage"),
                    ("ESPORTS CHARTS · TOURNAMENT", "https://escharts.com/tournaments/ow/overwatch-world-cup-2026"),
                    ("DUST2", "https://www.dust2.in/news/77207/how-cs2s-viewership-numbers-fared-at-ewc-2026"),
                    ("STREAMS CHARTS", "https://streamscharts.com/news"),
                ],
                "body": [
                    "The Overwatch World Cup final, played inside BlizzCon at the Anaheim Convention Center on Sunday, <mark>peaked at 349,275 concurrent viewers</mark> — people watching at the same moment — as South Korea beat Saudi Arabia 4-1, with France third.  Across the whole tournament — and this is a 20 August to 14 September window, not a weekend — Esports Charts has <mark>9,791,512 hours watched, an average of 166,901 concurrent viewers and 59 hours of airtime, meaning hours of live broadcast</mark>, across Twitch, YouTube, SOOP Korea, CHZZK, TikTok Live and Kick.",
                    "Now the part that makes this issue's best teaching example, and the rare pleasure is that the measurement firm says it out loud rather than leaving you to work it out.  <mark>Esports Charts reports that group-stage matches were played as best-of-five instead of best-of-three, that this significantly increased the stage's airtime, and that it contributed to a 90 percent rise in hours watched compared with 2023.</mark>  Over the same comparison the group stage peaked at 159,300 viewers, <mark>up 5.8 percent</mark>.",
                    "Read those two numbers together.  Hours watched up 90 percent.  Peak up 5.8 percent.  Almost none of that ninety came from more people showing up.  It came from a rules change that made each series longer, which put more hours of broadcast in front of roughly the same crowd.  Hours watched is the product of how many people were watching and how long there was something to watch, and only one of those is an audience.  Esports Charts also reports average viewers up 14.6 percent on the previous edition, which is the honest measure of whether more people came.",
                    "Blizzard's own Twitch channel, over Streams Charts' trailing seven days, tells the run-of-show story.  <mark>Peak 233,206, average 73,803, 1,402,233 hours watched across 19 hours of airtime.</mark>  For every three people present at the top of that broadcast, about one was there on average.  That gap is not a failure — it is what happens to any show with reveals near the front — but it is the difference between what a sponsor is shown and what a sponsor gets.",
                    "Put 349,275 somewhere recognisable.  It is roughly twenty sold-out Honda Centers, the arena next door to the convention centre it was played in, on that venue's published capacity of about 17,000 — our arithmetic, not theirs.  Against the year's live benchmarks it is mid-table: the Esports World Cup Counter-Strike grand final in late August peaked at 1,037,179, and Z Event peaked at 1.3 million earlier this month.  A real audience, and about a third of the biggest esports final of the year.",
                    "One commercial note, carefully worded.  No title sponsor or presenting partner is named in any of the coverage of this event, and the viewer-reward mechanic was Twitch Drops — in-game items handed out for watching, which is Blizzard holding an audience with a currency it prints itself.  We have not seen the broadcast, so treat that as an absence in the reporting rather than a confirmed absence of a sponsor.  What we can say is that no brand partner is visible anywhere in the coverage of an event that put a third of a million people in front of one screen at the same second, which is worth knowing if you are pricing a livestream deal this quarter.",
                    "One thing that quietly got easier on Friday: Streams Charts extended its audience geography and demographics data to YouTube and Kick, having covered only Twitch before.  If you have been buying streaming sponsorship off Twitch and guessing at who was watching, you can stop guessing.",
                ],
                "numbers": [
                    ("349,275", "peak concurrent viewers, Overwatch World Cup final"),
                    ("90%", "rise in hours watched against 2023, on a 5.8% rise in peak viewers"),
                    ("166,901", "average concurrents across the whole 20 Aug to 14 Sep tournament"),
                ],
                "flagnote": "Esports Charts publishes hours watched, average concurrents and airtime as tournament totals spanning 20 August to 14 September across six platforms, so none of them can be read as weekend figures, and it does not publish a channel count or a per-platform split outside its paid tier.  The 90 percent and 5.8 percent figures describe the group stage against 2023; the 14.6 percent average-viewer rise is printed as an edition-wide figure rather than a group-stage one.  The Blizzard channel numbers are a rolling seven-day view of one Twitch channel with no calendar dates stated, and are not directly comparable with the multi-platform tournament peak.  The Honda Center comparison is our own arithmetic on a published capacity figure.",
                "so_what": "Hours watched is the number every livestream deck leads with and it is the one most easily inflated without a single extra viewer, because it rises whenever a broadcast runs longer or adds a channel.  This event is the cleanest proof you will get: a rules change lengthened the matches, hours watched went up 90 percent, and the number of people at the biggest moment barely moved.  Peak tells you the size of the largest moment, average concurrents against airtime tells you what you are actually renting, and you need both to know which one you bought.",
                "do_this": "Demand peak, average concurrents, hours watched and airtime on every livestream proposal you receive this quarter, and price the deal off average concurrents against airtime, which is the pair that tells you what you are actually renting.  When a seller shows you a year-on-year rise in hours watched, ask what changed about the format or the schedule before you read it as audience growth.",
            },
        ],
    },
    {
        "id": "watch", "name": "ONE TO WATCH", "page": "pg. 06",
        "note": "one creator with momentum, and the client who should be calling",
        "tint": None,
        "items": [
            {
                "title": "Silver Cymbal's videos do three times the views when no brand name is in the title, and the brands in his biggest videos have never paid him",
                "hook": "A million views on a video about duct seal putty.  The uploads with a manufacturer in the title are his worst performers, by our count of his last fifteen.",
                "open": True,
                "stamps": [
                    ("YOUTUBE · @SILVERCYMBAL", "https://www.youtube.com/@SilverCymbal"),
                ],
                "body": [
                    "Silver Cymbal is a home repair channel with <mark>1.08 million subscribers</mark> and 536 uploads, making five-minute videos that solve one expensive household problem cheaply.  Across his last fifteen uploads the median is <mark>72,110 views</mark>.  On 30 August he posted Spray Foam is Expensive.  Use THIS Instead! and it has done <mark>1,113,465 views — fifteen times his own median</mark>.  It is a five and a half minute video about duct seal putty.",
                    "That is not a one-off.  He ran the same title structure on 19 April with Mosquito Spraying is Expensive.  Do This Instead!, which is at 1,022,446.  A garage door sealing video from 17 May sits at 732,101 and a tick-prevention one from 24 May at 627,495.  The template is: name an expensive recurring household cost, then show the cheap thing that replaces it.  He posted a third instance yesterday, Lawn Care is Expensive.  Try THIS Instead! — 85,771 views at a day old, so the case on that one is open.  What it shows is intent.  He published it a fortnight after the spray foam video went up and while it was still climbing, which means he has worked out what he has.",
                    "Now the number that should interest a brand, and it is ours rather than his.  Split those fifteen uploads by whether the title names a manufacturer.  <mark>Titles naming a brand: median 48,815 views across six videos.  Titles that do not: median 160,330 across nine.</mark>  A 3.3 times gap, and every single video over half a million sits on the unnamed side.  The titles with a brand on the front are the worst-performing thing on the channel.",
                    "The spray foam video carries a line in its description, on its own: Nothing in this video is sponsored.  It also carries Amazon affiliate links, as everything on the channel does.  So he took no fee for it and he is not disinterested — both of those are true and a brand should know which is which.",
                    "Look at what he has actually sold and what he has not.  His sponsors are portable power stations and robot mowers — EcoFlow, Anker SOLIX, Jackery, Aiper, Worx.  Meanwhile his million-view videos are about duct seal putty, garage door weatherstripping, mosquito control and tick prevention.  <mark>Not one sealant, weatherstrip, pest control or plumbing fittings brand appears anywhere on his sponsor list</mark>, and those are the exact categories where his audience arrives with a problem and leaves with a product name.",
                    "The likeliest reason for the gap is the same mechanism as today's lead.  A brand name in the title tells the viewer what the video is for before the video argues for itself.  Whether it is the title doing that or the subject matter underneath it, fifteen videos cannot say.  What they do say is that his best-performing work is the work with no brand name on the front of it.",
                ],
                "watch": {
                    "label": "TOP VIDEO, LAST 3 MONTHS",
                    "title": "Spray Foam is Expensive.  Use THIS Instead!",
                    "url": "https://www.youtube.com/watch?v=sHL4lBAhklA",
                    "meta": "1,113,465 views · published 30 August 2026 · 5m 34s",
                    "note": "Five and a half minutes on sealing gaps around pipes and wiring with duct seal putty instead of expanding foam, with an unsponsored disclosure in the description.",
                },
                "flagnote": "The median figures and the brand-name split are our own calculation across his fifteen most recent uploads, not a published statistic, and fifteen videos is a small sample that cannot separate the effect of a brand in the title from the effect of the subject matter.  View counts and the subscriber figure were read from YouTube on 14 September and will have moved since.  We could not obtain an independent subscriber growth series — Social Blade and ViewStats were both unavailable — so every momentum claim here is view-based, measured against the channel's own median.",
                "so_what": "This channel is the clearest illustration you will see this month of the thing the lead is about: the signal that a post is selling gets read before the post does, and it appears to cost most of the audience.  On his own channel the videos with no manufacturer in the title do roughly three times the median of the ones that have one — across fifteen uploads, which cannot rule out the subject matter doing the work.  A brand that took the hint would buy the format rather than the mention.",
                "do_this": "If you sell sealants, weatherstripping, pest control, fasteners or plumbing fittings, contact Silver Cymbal this week and price a five-minute problem-solution video where your product is the cheap answer to an expensive recurring cost — not a review with your name in the title.  Agree the title stays generic and take the credit in the demonstration and the description instead.",
            },
        ],
    },
    {
        "id": "money", "name": "THE MONEY", "page": "pg. 07",
        "note": "the numbers that change what a thing is worth buying",
        "tint": None,
        "items": [
            {
                "title": "TikTok is where young shoppers find brands and one of the last places they take advice, and both facts come from the same survey",
                "hook": "27.8 percent discover new brands through TikTok's organic posts.  10.8 percent trust the creators they follow for style advice.  Friends get 34 percent.",
                "open": True,
                "stamps": [
                    ("NET INFLUENCER · 14 SEP", "https://www.netinfluencer.com/gen-z-discovers-brands-on-tiktok-but-trusts-influencers-less-than-friends-family-report-finds/"),
                ],
                "body": [
                    "Pacsun published its 2026 Youth Report this morning, compiled with GlobalData from <mark>6,126 US respondents aged 11 to 24</mark>.  On discovery, TikTok wins and it is not close: <mark>organic TikTok content is the single largest driver of new brand discovery at 27.8 percent</mark>, ahead of TikTok Shop at 18.6 percent, organic Instagram at 10.6 percent and Instagram ads and sponsored posts at 7.5 percent.  As a source of fashion inspiration overall TikTok is named by 61.6 percent, flat against 61.9 percent last year, with Instagram at 52.3 percent and falling from 57.7 percent.",
                    "Then the same respondents were asked who they trust for fashion and style information.  <mark>Influencers and creators they follow: 10.8 percent.  Friends: 34 percent.  Family: 27 percent.</mark>  Celebrities got 5.9 percent and social media generally got 3.9 percent.  The pattern repeats outside fashion — creators score 8.2 percent for financial advice, 10.2 percent for news and current events, 7.4 percent for emotional support, behind friends and family every time.",
                    "Hold those two findings next to each other, because the temptation is to pick the one that suits.  The biggest discovery engine in this age group is also one of the least trusted advice sources in it.  Both are true, and they are not in conflict.  They are describing two different jobs, and the industry has spent three years selling one while charging for the other.",
                    "The mechanism is that finding out something exists and being convinced to buy it are separate transactions with separate people attached.  A creator introduces the thing.  A friend ratifies it.  If your campaign ends at the creator post, you have paid for the first half and left the second to chance, and the second half is the one that closes.",
                    "That reframes what you should ask a creator post to do.  Not persuade — transfer.  The measure that matters is whether it gets sent to somebody, screenshotted into a group chat, or brought up in a conversation, because that is the step where trust is actually applied.  Sends and shares stop being vanity metrics under this reading and start being the only ones pointed at the mechanism.",
                    "One more finding worth knowing before it gets quoted at you.  Asked what would make them unfollow a creator, respondents put bullying at 49.5 percent, racist or discriminatory content at 47.9 percent and scamming followers at 46.7 percent.  <mark>Failing to disclose a paid partnership came in at 22.6 percent</mark>, roughly half the rate of the top three.  That is not permission to skip disclosure, which is a legal requirement in most of the markets you sell in.  It is a warning that your creators' own audiences will not police it for you.",
                ],
                "flagnote": "This is a retailer's own annual youth report, produced with GlobalData, and Pacsun sells to the demographic it surveyed.  Every figure is stated preference rather than observed behaviour, and respondents are notoriously poor at reporting what influences them.  The age band runs from 11 to 24, which mixes children and adults in one sample, and the report does not publish field dates or a margin of error.  Note also that it points the other way from the Precisify survey of affluent shoppers we covered on Friday, which put trust in creators at 38.4 percent — different populations, different questions, and not directly comparable.",
                "so_what": "Creators are the best introduction mechanism in this age group and a weak closing argument, which means paying for a creator post and measuring it on conversion is measuring the wrong half of the job.  The step you are actually buying is the one where a viewer passes it to somebody they trust, and almost no brief asks for anything that makes that easy.  Build the thing that gets forwarded and you get the friend's 34 percent working for free.",
                "do_this": "Add one requirement to your next creator brief: the post must contain something specific enough to be worth sending to one person — a price, a comparison, a result, a genuinely useful instruction.  Then report sends and shares alongside views, and judge the post on whether it travelled rather than on how many people saw it.",
            },
            {
                "title": "Kroger's advertising arm grew profit 24 percent, its best since 2021, and its shopper data is now buyable inside TikTok",
                "hook": "The grocery business guided sales down.  The ad business had its strongest quarter in five years.",
                "stamps": [
                    ("MODERN RETAIL · 11 SEP", "https://www.modernretail.co/marketing/krogers-ad-business-sees-most-profit-growth-since-2021/"),
                ],
                "body": [
                    "Kroger Precision Marketing, the retailer's advertising business, <mark>grew profit 24 percent in the second quarter — its strongest since 2021</mark> — with advertising rising as a share of sales by 88 basis points year on year — 0.88 of a percentage point.  Total company sales were 34.6 billion dollars against 33.9 billion in the same quarter last year, and operating profit 971 million against 863 million.  At the same time Kroger cut its full-year guidance for identical sales excluding fuel — takings at stores open at least a year, fuel stripped out — to a range of 0.2 to 0.8 percent, down from 1.0 to 2.0 percent.",
                    "Two directions in one earnings call.  Selling groceries got harder and selling access to grocery shoppers got considerably easier.",
                    "The growth is attributed to store traffic, new advertising formats inside its shopping assistant, and expanded inventory through partnerships with Google and TikTok.  That last one is the part that matters to anyone making video: a supermarket's shopper data is now buyable inside TikTok, which means a creator video and a retailer's purchase data can sit in the same buy.",
                    "Kroger has also put digital screens into roughly 600 stores, currently in wine and spirits departments, and intends to expand to end caps.  Worth reading against what we covered on Friday about Walgreens, where the previous generation of in-store screens sat in front of the product rather than beside it and cost 200 million dollars to learn that.",
                    "The structural point is the boring one.  Retail media — a retailer selling advertising against its own shopper data and shelf space — grows because it costs the retailer almost nothing to make, and it is now large enough to be the line a grocer leads with when the groceries disappoint.  That money comes out of the same budget your video is competing for.",
                ],
                "so_what": "Every quarter retail media outperforms, a little more of the brand budget moves toward the end of the journey where sales are easy to attribute, and video that builds demand loses the argument by default because its effect arrives later.  The TikTok partnership is the interesting wrinkle, because it puts a creator video and a retailer's purchase data in the same buy for the first time in that account.  That is where a credible case for video against retail media can actually be made, using the retailer's own numbers.",
                "do_this": "If you sell through Kroger, ask your rep this week what the TikTok inventory partnership lets you match — specifically whether creator-made video can be measured against in-store purchase data.  Run one creator video through it and take the result into the meeting where your video budget gets compared with retail media.",
            },
        ],
    },
    {
        "id": "format", "name": "FORMAT LAB", "page": "pg. 08",
        "note": "the format decision underneath the numbers",
        "tint": None,
        "items": [
            {
                "title": "Most creator briefs never say what the video should be, and the same format is the best in one category and the worst in another",
                "hook": "Briefs name the product, the message, the deliverables and the dates.  They leave the one decision that predicts the result to whoever is holding the phone.",
                "open": True,
                "stamps": [
                    ("NET INFLUENCER · 12 SEP", "https://www.netinfluencer.com/tiktok-audiences-are-pulling-toward-six-formats-and-scrolling-past-the-ones-built-to-sell-q2-editing-format-index-finds/"),
                ],
                "body": [
                    "The most quietly damning line in the index is not a number.  It is this: many creator briefs specify the product, the message, the deliverables and the dates, and leave the format of the post to the creator.  Everything else in the study says format is the variable with the widest spread of outcomes attached to it.",
                    "Two formats show why that matters.  <mark>Photo Carousels had the highest typical engagement rate of any format in Fashion and in Comedy, and the lowest in Food.</mark>  <mark>Raw phone footage had the highest in Business and the lowest in DIY.</mark>  Same format, opposite verdict, decided by which aisle you are selling in.  So a rule like carousels are working right now is true platform-wide and can be exactly wrong for your category.",
                    "It also breaks the way most campaign reports are read.  The typical post in the index earned a 6.4 percent engagement rate, and the typical post in each format lands somewhere else entirely — a carousel at 5 percent is below what carousels usually do, while a purchase-tagged video at 5 percent is well above what tagged posts usually do.  <mark>Judged against one platform average, the same 5 percent is a failure and a triumph.</mark>  Most campaign reports do not record which format each post used at all, so the question cannot even be asked afterwards.",
                    "Two other numbers make the case that format choice is where the movement is.  The two largest formats in the whole index — raw phone footage at 13,271 posts and talking head with cutaways at 8,701 — <mark>did not move more than 8 percent on either measure last quarter</mark>, below the 10 percent the index treats as real change.  The volume is sitting still.  Everything that moved, up or down, moved in the smaller formats.",
                    "The practical version is three questions the index suggests putting on every brief, and they take a minute each.  Which format is this post, and how did it do against the typical post in that format?  Which formats are gaining in our category right now, and does this brief include any of them?  And if the brief includes purchase-tagged posts, is the tag sitting on its own or on a format people already watch?",
                ],
                "flagnote": "Single-sourced to Net Influencer's own quarterly index, produced with the social listening firm dig, which sells the data underneath it, and the full category board sits behind a lead-capture form.  The category comparisons are stated by the index qualitatively rather than with published rates for every pairing, and are limited to formats with at least 100 posts in that category.  US TikTok posts only.",
                "so_what": "Format is the field on a brief that almost nobody fills in, which means the decision with the widest spread of outcomes gets made by default by whoever picks up the camera.  It is not that creators choose badly — they usually choose what works for them, which is not the same as what works for your category.  Writing the format down costs nothing and turns the biggest variable into a decision somebody owns.",
                "do_this": "Add two fields to your creator brief template this week: the editing format you want, and the benchmark that format usually earns in your category.  Then go back through last quarter's campaign report and label each post with the format it used, so the next round has something to compare against.",
            },
        ],
    },
]

FORECAST = [
    {
        "confidence": "LIKELY",
        "window": "by 31 March 2027",
        "headline": "Format becomes a named field in creator briefs and in the rate card that follows it",
        "body": "Once a benchmark exists showing a 1.4 percent typical engagement rate for purchase-tagged posts against 6.4 percent overall, a buyer has the arithmetic to argue that a tagged deliverable is a different product from an untagged one and should not cost the same.  Creators have the mirror image of that argument, which is that a tagged post costs them audience and should cost the brand more.  Both sides now have a number, and formats that were previously bundled as one post start getting priced separately.  Quarterly updates to the index are what turn this from an argument into a rate card.",
        "do": "Split your next creator rate negotiation into separate prices for tagged and untagged deliverables, so you find out what the tag is worth to them before it is worth it to you.",
    },
    {
        "confidence": "LIKELY",
        "window": "by 30 June 2027",
        "headline": "A major sports body publishes a written creator code of conduct after a second incident",
        "body": "The US Open produced the template failure — an event where the people who broke the etiquette were not on the organiser's list and the credentialed cohort took the damage anyway.  Creator access at live sport is expanding rather than contracting, because the audience arithmetic still works, so the same conditions will recur at the next big event with a tradition worth offending.  The cheapest institutional response is a published document that lets an organiser say the rules existed, which is why it usually arrives after the second incident rather than the first.",
        "do": "Write your own creator etiquette annexe now and attach it to every event access deal, so you are not adopting somebody else's version under pressure later.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "by 31 December 2026",
        "headline": "A platform publishes its own format benchmark to compete with a vendor's",
        "body": "A third-party index that tells brands purchase-tagged posts earn a fifth of the engagement of everything else is not a finding any platform selling commerce tools wants left unanswered.  Platforms have far better data than any listening firm and have historically published it exactly when an outside number starts shaping how buyers price their inventory.  The tell will be a benchmark post framed around what good looks like by format, with the commerce formats measured against each other rather than against the feed.",
        "do": "When a platform publishes format benchmarks, check whether tagged posts are compared with other tagged posts or with everything, because that choice decides the conclusion.",
    },
    {
        "confidence": "LONG SHOT",
        "window": "by 30 September 2027",
        "headline": "A brand buys a creator's format rather than a creator's audience, and says so publicly",
        "body": "Silver Cymbal's numbers point at something more transferable than a sponsorship: a title structure and a five-minute problem-solution shape that does three times the views without a brand name attached.  A brand that wanted that would license the format and run it on its own channel with the creator paid as a maker, rather than renting his audience for one video.  The reason it is a long shot is that nobody in a marketing structure gets promoted for buying a template, and the legal question of what a format even is stays genuinely unsettled.  The first company to do it will have found a way to describe it as a production deal.",
        "do": "Identify the one creator format in your category that consistently outperforms, and price what it would cost to commission its maker to run it on your channel for a year.",
    },
]

TLDR = [
    "Purchase-tagged TikTok posts grew 55 percent in count last quarter while response to them fell 41 percent, and the typical tagged post earns a 1.4 percent engagement rate against 6.4 percent for the typical post across the whole 58,037-post sample.  Judge your tagged posts against the 1.4 percent benchmark rather than your overall average, and rewrite one brief so the tag sits on a format people already watch instead of on a post that exists only to carry it.",
    "Photo carousels nearly doubled to 1,317 posts and were the only format at scale to gain on both creator supply and audience response, with 59 percent of them coming from accounts under 10,000 followers and one 208-follower account taking 1.4 million views.  Rebuild your three best videos of the year as carousels from footage you already own and use the winner to decide what gets a full shoot next quarter.",
    "Around 100 credentialed creators attended the US Open, roughly double last year, and play was halted during Naomi Osaka's opening match by people ESPN reports were not credentialed at all, with the backlash landing on the whole cohort.  Add an etiquette page to every event creator brief covering what is prohibited during play, where capture is allowed and who to call, and check who is attending on your tickets outside the organiser's list.",
    "Old Navy anchored back-to-school on MrBeast and reports a 22 percent traffic lift to its kids' range in the days after launch, from over 100 million views, after a quarter in which sales at stores open a year or more fell 4 percent, with the sales read on the campaign itself still a quarter away.  Write down the fast metric and the slow metric with the date you will read each before your next creator campaign goes live, and put the slow one in the budget approval.",
    "Pacsun and GlobalData asked 6,126 US 11- to 24-year-olds where they find brands and who they trust: TikTok's organic posts drive 27.8 percent of new brand discovery while only 10.8 percent trust the creators they follow for advice, against 34 percent for friends.  Brief your next creator post to contain something specific enough to be forwarded to one person, and report sends and shares alongside views.",
    "The Overwatch World Cup peaked at 349,275 concurrent viewers on Sunday's final, and Esports Charts says its 90 percent rise in hours watched against 2023 came largely from moving group matches to best-of-five, while peak viewers rose 5.8 percent.  Demand peak, average concurrents, hours watched and airtime together on every livestream proposal, and ask what changed about the format before you read a rise in hours watched as audience growth.",
    "Silver Cymbal has 1.08 million subscribers, a median of 72,110 views across his last fifteen uploads and 1.11 million on an unsponsored video about duct seal putty, and by our count his brand-named titles earn about a third of what his generic ones do.  If you sell sealants, weatherstripping, pest control or plumbing fittings, commission a five-minute problem-solution video from him with your product as the cheap answer and your name out of the title.",
]

SHARE = [
    {
        "who": "JARED · CEO",
        "angle": "The commerce feature brands treat as free upside is the thing costing them the audience, which is an argument for funding better video rather than more buttons.",
        "post": "Creators put 55% more purchase tags on their TikToks last quarter. Response to the tagged posts fell 41%.\n\nThat is from the Q2 TikTok Editing Format Index, published by Net Influencer with the social listening firm dig, across 58,037 US posts.\n\nThe absolute numbers are worse than the percentages suggest. The typical purchase-tagged post earned a 1.4% engagement rate. The typical post across everything they measured earned 6.4%.\n\nSo the format was already the weakest thing on the board, and it got weaker while more people made it.\n\nMost of us have been treating commerce features as free. Same video, one more button, some extra revenue. The data says the button is not free, and it gets charged at the worst possible moment, which is the half second before somebody decides to keep watching.\n\nA tag tells a viewer what the video is for before the video has made any case for itself.\n\nThe fix in the study is not stop selling. It is that the tag has to sit on something people already want to watch, rather than being the reason the post exists.\n\nOne caveat I would want if I were reading this: single study, from a publisher whose data partner sells this kind of analysis, nobody else has verified it. I would still check my own numbers against it this week.",
        "why": "It turns a feature every client assumes is costless into a measurable cost, which is the argument that gets video funded properly rather than decorated with commerce.",
    },
    {
        "who": "JAMES · CREATIVE DIRECTOR",
        "angle": "The US Open creator backlash was a briefing failure, and the part of the brief that failed is the part creative teams never write.",
        "post": "A hundred creators went to the US Open with official credentials. The people who stopped play during Naomi Osaka's match had no credentials at all. All hundred wore the backlash.\n\nDigiday reported this morning on what six creator marketing people took from it. The USTA roughly doubled its credentialed cohort this year. Play was halted on 31 August because of flash photography from a hospitality suite, and ESPN reported those people were not part of the official programme.\n\nCayley Stonehouse at Gupta Media put the gap plainly. A creator relationship should go beyond deliverables and talking points. It should cover the rules of the sport, the etiquette, when and where you can capture.\n\nI have written a lot of creator briefs. I know exactly what is in them. Product, message, deliverables, dates, tone, a list of things not to say.\n\nNothing about the room.\n\nWe brief the content and assume the behaviour. On a set we control that is fine, because we are standing there. At somebody else's live event it is the whole risk, and the etiquette is invisible to anyone who did not grow up in that sport.\n\nWhat bothers me is that the cost did not land on the people who caused it. It landed on the format, which means the next brand buying event access pays for it.",
        "why": "A creative director admitting the brief he writes has a hole in exactly the place that caused a public failure is uncomfortable, specific and checkable against today's reporting.",
    },
    {
        "who": "LAWRY · LEAD VIDEO EDITOR",
        "angle": "Where the reveal sits in a live run of show is an edit decision that silently decides what the sponsor gets, and nobody treats it as a commercial one.",
        "post": "Blizzard's own Twitch channel peaked at 233,206 viewers around BlizzCon. Across the nineteen hours Streams Charts logged on it in its last seven days, the channel averaged 73,803.\n\nFor every three people at the top of that broadcast, about one was there on average.\n\nNobody edits a live stream. Somebody edits what is left of it, and that is the job I keep thinking about, because nineteen hours becomes six minutes of highlights and a handful of clips.\n\nThat peak-and-average gap tells you exactly what to keep. Everyone came for the reveals. So the recut is reveals, back to back, and the long panel stretches in the middle do not survive.\n\nHere is the bit nobody in the commercial conversation sees coming. Sponsor material written for a live show tends to sit in the lulls, because the lulls are where there is room for it.\n\nThose are the first minutes an editor cuts.\n\nSo a brand can buy presence across a nineteen-hour broadcast and end up with nothing in the version most people actually watch, and whoever made that call was trimming for pace at four in the afternoon.\n\nMost editors would call that a pacing decision. It is a delivery decision.\n\nI would still cut the panel. You cannot pad a highlights reel to protect a logo, and I have never worked out what the honest alternative is.",
        "why": "It shows a routine pacing instinct quietly determining what a sponsor actually receives, which is an edit decision nobody in the commercial conversation knows is being made.",
    },
]
