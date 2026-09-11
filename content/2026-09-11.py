# -*- coding: utf-8 -*-
"""Content for THE FEED — issue data only.  The render spec lives in build_feed.py."""

ISSUE = {
    "date_iso": "2026-09-11",
    "kicker": "Crux Media // Friday 11 September 2026",
    "tagline": "What brands did on YouTube yesterday, and whether it worked.",
    "pace": "STEADY",
    "next_drop": "Next drop: Monday, 06:30 MT",
}

LEAD = {
    "headline": "MOLSON COORS QUADRUPLED ENGAGEMENT ON ITS CREATOR CONTENT.  THE THING IT CHANGED WAS THE APPROVAL PROCESS",
    "deck": "No new agency.  No new creators.  The company took its social work out of a television approval process and sorted every decision into three lanes, one of which is a straight yes.  Engagement on creator content is four times what it was in March, and 230 marketers across more than a hundred brands now work this way.",
    "stamps": [
        ("DIGIDAY · 11 SEP", "https://digiday.com/media/molson-coors-ditches-its-tv-era-workflow-to-move-at-creator-speed-quadrupling-engagement/"),
        ("DIGIDAY · 8 SEP", "https://digiday.com/media/whats-in-and-out-for-creators-heading-into-q4/"),
    ],
    "body": [
        "Alyssa Mercante reported this at Digiday this morning.  Molson Coors, a company worth more than seven billion dollars, rebuilt how it makes social video in March.  <mark>Engagement on its creator content has quadrupled since.</mark>  The new way of working is now trained across <mark>230 marketers managing more than a hundred brands</mark> in the United States and Canada, including Miller High Life, Fever Tree and Zoa.",
        "Here is what actually changed, because it is not the part anyone would put in a case study.  The legal team built what Molson Coors calls freedom within a framework: <mark>every social decision lands in one of three lanes — fast-track, needs a conversation, or a hard no.</mark>  Before that, social work was routed the way a television campaign is routed, which means everything got the same treatment as the most expensive thing in the building.",
        "Justine Stauffer, senior director of creative effectiveness at Molson Coors, says what the lawyers being in the room did for pace.  We've moved mountains so much faster than we were before, because we had our legal team involved in the process the entire way, they understand the ecosystem better, they understand how consumers operate in this space.",
        "The second change is quieter and harder to copy.  The company redefined what good looks like.  Stauffer again: we really needed to be thinking about how we defined the quality of content in this space so much differently than we think about other channels.  In practice that means looser creator briefs, lo-fi footage that would have been rejected eighteen months ago, and a decision to stop treating every organic post as a high-stakes television campaign.  It also picks audiences first and platforms second, which is the reverse of how most media plans are still written.",
        "Evan Horowitz, chief executive and co-founder of the agency Movers and Shakers, supplies the diagnosis for everyone who has not done this yet.  Brands, he says, are talking at customers and not really understanding the reality, which is that there's these hundreds of conversations happening.  What social should be instead: it should be experimental, it should be this place where we can test and learn and look at signals, and learn about our communities, and really build our brands from the fans for the feed.",
        "Now say the obvious thing.  Engagement is the softest number a marketing team can report, Molson Coors has published no sales figure next to it, and four times a small number is still a small number.  All true.  It also does not touch the mechanism, which is that the bottleneck was never the idea or the creator.  It was the distance between the two, measured in days of review.  A brand that publishes in three days is making content about a live conversation.  A brand that publishes in three weeks is making content about a conversation that ended.",
    ],
    "numbers": [
        ("4x", "engagement on Molson Coors creator content since March 2026"),
        ("230", "marketers now working to the new model across the US and Canada"),
        ("3", "lanes the legal team sorts every social decision into"),
    ],
    "flagnote": "Digiday reports that engagement with creator content has quadrupled, without naming the metric, the baseline or the platforms it covers, and Molson Coors has disclosed no sales, revenue or brand-tracking figure alongside it.  The market diagnosis in the piece comes from Evan Horowitz, whose agency sells brands the kind of creator work the story recommends.  There is no independent verification of the engagement figure and no named comparison period other than March 2026.",
    "so_what": "Almost every fix proposed for weak social performance is a creative fix — better idea, better creator, better edit.  This one is an operations fix, and it moved a number four times further than most creative changes do.  The reason is that speed is a creative variable disguised as an administrative one.  Anything that has to be funny about right now stops being funny somewhere in week two of legal review, and the team never sees the version that would have worked.",
    "do_this": "Measure the real elapsed time from brief to published post on your last five social pieces, then write down which single approval step ate the most days and who owns it.  Take that one number into your next status meeting and ask for a fast-track lane for anything under a named spend threshold.",
}

SECTIONS = [
    {
        "id": "ws", "name": "W'S", "page": "pg. 02",
        "note": "what worked, and the exact reason it worked",
        "tint": "blue",
        "items": [
            {
                "title": "Rich people trust creators nearly five times more than celebrities, and the reason is that they watch the product get tested",
                "hook": "Creators 38.4 percent.  Celebrities 8 percent.  And almost nine in ten said a live test beat a polished film.",
                "open": True,
                "stamps": [
                    ("NET INFLUENCER · 10 SEP", "https://www.netinfluencer.com/affluent-shoppers-trust-creators-nearly-5x-more-than-celebrities-youtube-anchors-luxury-purchase-journey-per-report/"),
                ],
                "body": [
                    "The advertising intelligence firm Precisify surveyed 500 US adults aged 18 to 60 with a household income of at least 150,000 dollars and a stated interest in luxury.  Asked who they trust for an in-depth product review: <mark>content creators 38.4%, friends and family 29.5%, brand ambassadors 23.1%, celebrities 8%.</mark>  Creators are 4.8 times more trusted than the famous person a luxury house pays to hold the handbag, which is the single most expensive line in that category's marketing.",
                    "The number that explains the ranking is the next one, and it is the only one in the study with a mechanism attached.  <mark>Almost 90% of respondents said watching a creator perform a real-time test of a luxury product made them more confident in its quality than a polished broadcast or streaming commercial.</mark>",
                    "Read that as a statement about risk rather than taste.  A commercial cannot go wrong, because every frame was approved before you saw it.  A test can go wrong, and both of you know it while you are watching.  That possibility is the entire value of the format.  The polish you paid for is the thing telling the viewer the brand controlled the outcome.",
                    "The platform figures point the same way.  <mark>68% of this group spend an hour or more a day on YouTube</mark>, against 61% on TikTok and 58% on Instagram, and social platforms are named as the biggest influence on a purchase over 5,000 dollars <mark>by 48% during the deep research phase</mark> — more than double the 22% who name it while comparing options and the 17% who name it at first discovery.  So the moment they arrive is not the moment you are advertising at them.  It is after they have already decided they want one and are looking for a reason not to buy.",
                    "The awareness gaps in the same study are worth a second look for anyone who thinks reach is the problem.  Louis Vuitton is at 70% awareness and 55% ownership among this group, Rolex 67% and 51%, Hermes 59% and 44%, Celine 38% and 29%.  Every one of those brands has an awareness surplus.  None of them has an awareness problem.  What sits in the gap is conviction, and conviction is what a test produces and a film does not.",
                ],
                "flagnote": "This is a 500-person survey from Precisify, a firm that sells advertising intelligence to the brands being measured, and it does not publish its fieldwork dates, its margin of error or the exact wording of its questions.  Every figure is self-reported stated preference rather than observed purchasing, and the sample is United States only.  Treat the 38.4% against 8% as a large directional gap rather than a precise ratio.",
                "so_what": "The reason a handheld test outperforms a beautiful film with the same product in it has nothing to do with authenticity as a vibe.  It is that one of them can fail on camera and the other cannot, and the viewer knows which is which.  Production value signals control, and control is exactly what a buyer at the point of conviction is trying to see past.  That is also why moving a creator's footage into a brand-controlled frame tends to lose you the thing you paid for.",
                "do_this": "Take the highest-consideration product you sell and commission one unscripted test of it this week — someone using it hard, on camera, with the failure allowed to stay in the cut.  Put it where somebody researching that purchase will find it, and judge it against your last polished film on conversion rather than on views.",
            },
            {
                "title": "Ariana Grande's beauty brand got 41 shooting days it did not have to build, and 260 million views out of them",
                "hook": "450 creators, 3,000 pieces of content, 10 pop-ups, 15,000 people through the door.  The venue was already booked.",
                "stamps": [
                    ("GLOSSY · 11 SEP", "https://www.glossy.co/pop/pop-newsletter-how-ariana-grandes-r-e-m-beauty-capitalized-on-the-eternal-sunshine-tour-to-drive-engagement-and-sales/"),
                ],
                "body": [
                    "Danny Parisi wrote this up at Glossy this morning.  R.E.M. Beauty ran itself through the whole of Ariana Grande's Eternal Sunshine tour — <mark>41 shows over two months, ending on 1 September</mark> — and came out with <mark>260 million social views</mark> across the run, <mark>450 brand creators producing more than 3,000 pieces of content</mark>, and pop-ups in 10 cities that drew <mark>15,000 people in person</mark>.  Ulta Beauty reports higher foot traffic and repeat sell-outs on the Plumping Lip Gloss and the Essential Drip Glossy Balm.",
                    "The mechanism here is not celebrity founder.  Plenty of celebrity beauty brands are flat.  The mechanism is that a concert tour is a content production schedule that somebody else is paying for.  Forty-one nights, a built set, a full crew, a guaranteed audience and a news cycle, repeating twice a week for two months.  Most brands spend that budget manufacturing one afternoon of that.",
                    "And the product moments were written into the show rather than bolted onto it.  Grande applied the Essential Drip Glossy Balm before performing 7 Rings, and did a full face at an on-stage vanity using several R.E.M. products before Into You.  Those are not sponsor reads.  They are the reason a phone comes up in the crowd, which is how 41 nights becomes 3,000 pieces of content nobody at the brand had to shoot.",
                    "The detail most people will skip is the retail one.  The pop-ups were where Ulta debuted a new mobile point-of-sale system, which Ulta now intends to roll out into its stores.  So the brand's tour marketing doubled as a live retail test for its largest stockist, which is a very cheap way to become the partner your retailer learns things with.",
                    "Bryan Mochizuki, senior vice president of global brand marketing at R.E.M., on the wider shift: beauty today is so creative and dynamic, and the marketing playbook for beauty brands is constantly evolving.  Kaitlin Rinehart, vice president of merchandising at Ulta Beauty, on why the retailer cared: we've seen firsthand how powerful it can be when a brand and its founder create a cultural moment.",
                ],
                "flagnote": "The 260 million views figure is attributed to Ulta Beauty and R.E.M. rather than to independent measurement, and neither company has published how it is counted or across which platforms and accounts.  Sell-outs are reported without units, revenue or comparison to a normal period, and no figure separates tour-driven sales from the brand's baseline.",
                "so_what": "Every brand wants a moment and almost none of them want to pay for the two months of production a moment actually requires.  A tour, a season, a tournament, a festival run — these are somebody else's standing production, and a brand that attaches to one buys repetition instead of a launch.  Repetition is what produced 3,000 pieces of content from 450 people, and you cannot brief that into existence in a single week of shooting.",
                "do_this": "Find the one recurring event your customers already attend on a schedule — a tour, a league season, a convention circuit, a market — and price attaching to the whole run rather than one date.  Brief a moment inside the event itself that makes a phone come up, and agree with your biggest retailer what they get to test at it.",
            },
            {
                "title": "Burger King found a Good Mythical Morning episode it had not paid for, and bought the sequel",
                "hook": "The format was already made, already tested and already popular.  Burger King's brief was to not change it.",
                "stamps": [
                    ("TUBEFILTER · 10 SEP", "https://www.tubefilter.com/2026/09/10/burger-king-rhett-and-link-good-mythical-morning-whopper-guarantee/"),
                ],
                "body": [
                    "Sam Gutelle broke this at Tubefilter yesterday.  Rhett and Link had already made an episode of Good Mythical Morning that compared Whoppers bought from different Burger King locations, as ordinary programming rather than as a brand deal.  Burger King executives found it afterwards.  The company has now turned it into a paid partnership around its Whopper Guarantee — the claim that a Whopper is the same wherever you buy it.",
                    "What the deal contains: <mark>three branded spots running on YouTube and connected television, a two-week takeover of the main Good Mythical Morning hub, and a new episode in which the pair stress-test the guarantee</mark> and meet the chain's Your Way Champions.  Built with Google and Unreasonable Studios.  The two had promoted Burger King's Fiery Menu before, so there was a commercial relationship already.  Jacob Moncrief, president of Mythical, Rhett and Link's company: this partnership is a great example of what happens when a brand leans into an authentic creator relationship.",
                    "Now the part worth stealing.  The creative risk in this deal is close to zero, and not because Burger King wrote a safe brief.  It is because the format had already been tested on the audience at the brand's own expense of nothing, with the brand as the subject, and it worked well enough for the company to hear about it.",
                    "Compare that to the normal path.  A brand writes a brief, an agency invents a format, a creator adapts it, and the first time anyone finds out whether the audience wants it is after the money is spent.  Here the order is reversed.  The audience voted first.",
                    "There is a second thing in it that most brands would never allow.  The premise of the episode is a test of whether Burger King's own quality claim survives contact with reality, across different restaurants, on camera.  That is the same mechanism as the Precisify finding above — a test that could go badly is worth more than a film that cannot.",
                ],
                "so_what": "Somewhere on YouTube, several creators have already made a video about your product, your category or your claim, without being asked.  Those videos are the only market research you will ever get where the audience had no idea a brand was watching.  The cheapest good brief you can write this quarter is the one that copies the format of whichever of those videos did the biggest number.",
                "do_this": "Search your brand name and your three biggest product names on YouTube this week, sort by view count, and find the top five videos nobody at your company paid for.  Take the best-performing format to the creator who made it and ask what a sequel costs, instead of briefing a new idea.",
            },
        ],
    },
    {
        "id": "ls", "name": "L'S", "page": "pg. 03",
        "note": "what broke, and the failure mode underneath it",
        "tint": "pink",
        "items": [
            {
                "title": "Wrong owner: a brand paid a streamer to be replaced by an AI of himself, and it won on the only metric anybody was counting",
                "hook": "Most-viewed of his last twenty streams.  Other creators described it as him removing himself from the equation.",
                "open": True,
                "stamps": [
                    ("THE PUBLISH PRESS · 9 SEP", "https://news.thepublishpress.com/p/can-a-livestreamer-be-replaced-by-ai"),
                ],
                "body": [
                    "Hannah Doyle and Syd Cohen reported this at The Publish Press on Tuesday.  The streamer N3on, in a paid partnership with the AI video company Higgsfield AI, launched an AI-generated livestream of himself that runs when he is not live — an AI N3on wandering New York, on his channel, on his schedule, without him.",
                    "It performed.  The stream <mark>became his most-viewed video on demand out of his last twenty streams</mark>.  He disclosed the partnership as paid and disclosed the feed as fully AI-generated, which is more than most brands manage.  And it still went badly.",
                    "Kwebbelkop, on what the audience actually bought: a lot of people followed and subscribed to see the real N3on.  Now, with this AI, he's removing himself from the equation.  MoistCr1tikal, more bluntly: it's very clear that the motive wasn't to try to be innovative or new.  It was to make money.",
                    "The failure mode is ownership, and it is worth being precise about it.  Higgsfield did not buy N3on's audience.  It bought his face, his channel and his name, and removed the only thing the audience was there for.  A livestream audience is not watching a person-shaped video.  It is watching a person who might do something unplanned in the next ten minutes, and an AI feed is the one format that guarantees nothing unplanned will ever happen.",
                    "Note also which number said yes.  Views said it worked.  Views will always say a novelty worked, because a novelty is exactly the thing people click once.  The cost lands somewhere views do not measure: in whether the next sponsor read on that channel is believed.",
                ],
                "flagnote": "The Publish Press does not report what Higgsfield AI paid, how long the stream ran, its concurrent viewership, or any follower or subscriber change either way.  Most-viewed out of his last twenty streams is the only performance figure published, and there is no comment from N3on or from Higgsfield AI in the piece.  The criticism quoted is from other creators rather than from measured audience response.",
                "so_what": "If you are buying a creator, the thing you are buying is the audience's belief that a specific person is choosing to stand next to your product.  Anything that weakens the specific person weakens the asset, and an AI version of them weakens it completely while looking identical in the deliverable.  It is the same mechanism as recutting a creator's footage into a brand-owned post: you keep the face and lose the person vouching for it.",
                "do_this": "Add one line to your creator contract template this week requiring that the human named in the deal personally appears in and approves every deliverable, and that no synthetic or AI-generated likeness of them may carry your brand.  Then ask every creator you already work with whether they have licensed their likeness to anyone.",
            },
            {
                "title": "Wrong format: Walgreens spent 200 million dollars putting video between the shopper and the product",
                "hook": "The screens flickered, crashed, showed the wrong products and caught fire.  The retry moves them beside the shelf instead of over it.",
                "stamps": [
                    ("MODERN RETAIL · 11 SEP", "https://www.modernretail.co/marketing/walgreens-says-its-focused-on-higher-peforming-ad-placements-as-it-tries-again-with-digital-screens/"),
                ],
                "body": [
                    "Mitchell Parton at Modern Retail reported this morning that Walgreens is going back into in-store video.  <mark>Screens in 1,200 stores from October</mark>, with the in-store media firm Looma, which runs <mark>more than 7,000 screens across 10 retail chains reaching 13 million shoppers a month</mark>.  Two large displays per store near the entrance and the pharmacy waiting area, plus digital end caps.",
                    "The reason this is filed under losses is the last attempt.  From 2018 Walgreens ran Cooler Screens, which replaced fridge doors with digital displays showing virtual products and advertising.  <mark>It was a 200 million dollar programme.</mark>  The screens flickered, crashed, displayed the wrong products and caught fire.  Cooler Screens sued Walgreens in 2023 after the retailer pulled out, and the vendor quietly cut the data feeds to more than a hundred Chicago stores.",
                    "The design error is the one worth carrying into your own work, because it is not really about hardware reliability.  The screens were mounted where the product was.  A shopper who wants to see what is in the fridge is looking at a rendering of what is in the fridge.  Every second of video you put there is bought by deleting the thing the shopper came for.",
                    "Looma's screens sit next to products rather than in front of them, and Walgreens says the content is designed to educate rather than interrupt.  John Storms, vice president of digital and retail media at Walgreens — hired six months ago, having built the Lowe's media network after twenty years at Target — is explicit that the company is chasing better placements rather than more of them.",
                    "One more change worth noting, because it is the part that usually does not change.  Walgreens says it will judge this on performance across the whole path to purchase rather than on how often an ad played and how many people saw it.  A retailer measuring in-store screens by how many times an ad ran is measuring the supply of advertising, not the effect of it.",
                ],
                "so_what": "In-store video is the only channel where your advertising physically occupies the same space as the thing being sold, which means placement is not a media decision, it is a merchandising one.  Video that blocks the product costs you the sale it was bought to create, and no amount of production quality recovers that.  The same trap exists online whenever an interstitial sits over the page somebody came to read.",
                "do_this": "For every screen, banner or pre-roll placement you are buying this quarter, write down what the viewer was trying to look at in that moment and whether your video is in the way of it.  Cut the placements where the answer is yes, and move that money to the ones sitting alongside the thing being considered.",
            },
        ],
    },
    {
        "id": "moves", "name": "MOVES", "page": "pg. 04",
        "note": "platform, policy and legal changes that alter what you can make and buy",
        "tint": None,
        "items": [
            {
                "title": "Three US states and the EU now require you to say when the person in your ad is not a person",
                "hook": "New York's law has been live since June and is already drawing complaints.  Hawaii copied it.  California is on the governor's desk.",
                "stamps": [
                    ("NET INFLUENCER · 10 SEP", "https://www.netinfluencer.com/new-york-ai-disclosure-law-draws-first-complaints-as-california-hawaii-follow-suit/"),
                ],
                "body": [
                    "New York's synthetic performer disclosure law was signed in December 2025 and took effect in June 2026.  It requires advertisers to state explicitly when an AI-generated synthetic performer — digitally created media that appears to be a real person — is used in an advertisement.  It is enforceable only by the New York Attorney General's office, with no route for a consumer to sue directly, and it is now drawing its first complaints.",
                    "The map filled in fast.  Hawaii enacted a near-identical law in July 2026.  California's legislature passed its own version in August and it is awaiting Governor Newsom's signature.  The EU AI Act's transparency requirements came into force in August 2026.  Governor Kathy Hochul, on the intent: in New York, we are setting the rules of the road instead of letting AI run the show.",
                    "The gaps lawyers are pointing at are the ones that will catch a video team out.  Samantha Rothaus, a partner at Davis and Gilbert, and Robert Freund of Robert Freund Law both flag that there is a carve-out for AI-generated voices, which the disclosure requirement does not cover, and no clarity on what triggers disclosure for a partial body shot or a background crowd.  Rebecca Damon, chief labor policy officer at SAG-AFTRA and executive director of its New York local, is quoted in support of the law.",
                    "So the practical position today is that a fully synthetic presenter in a New York-facing ad needs a label, a synthetic voice over real footage probably does not, and nobody can tell you where a synthetic extra in the background of frame four sits.  That ambiguity is the risk, not the rule itself.",
                ],
                "so_what": "Most brand video teams have started using AI somewhere in the pipeline without anyone writing down where, which means nobody currently knows which of your live assets contain a synthetic person.  Three jurisdictions have now made that an answerable legal question rather than a production detail.  The teams that get caught will not be the ones that used AI deliberately.  They will be the ones that cannot say whether they did.",
                "do_this": "Build a one-page register this week listing every live ad and organic video that contains an AI-generated or AI-altered human, whether face, body or voice, and who signed it off.  Add a mandatory yes-or-no field on synthetic performers to your production sign-off sheet so the next one answers itself.",
            },
            {
                "title": "X rewrote its terms so you cannot sue it with anybody else, and the venue is now Texas",
                "hook": "Jury trial waived.  Class actions waived.  Your social manager is the person who clicks accept.",
                "stamps": [
                    ("SOCIAL MEDIA TODAY · 9 SEP", "https://www.socialmediatoday.com/news/x-adds-new-anti-lawsuit-provision-to-terms-of-service/829993/"),
                ],
                "body": [
                    "Andrew Hutchinson reported the change at Social Media Today on Tuesday.  Three things moved in X's terms of service.  Disputes are now handled in Texas courts under Texas law, matching X's absorption into SpaceX.  Users are made responsible for their own use of the service, including features that perform autonomous actions on your behalf.  And the new clause: you and X waive the right to a jury trial, and you and X waive the right to bring or join a class, collective, or other representative action.",
                    "It applies to all users and, where the law allows, to corporate affiliates.  The context is an active class action brought by sexual abuse survivors over material generated by xAI's Grok, which is the kind of case the new language is designed to prevent from grouping.",
                    "The reason this belongs in a brief about brand video rather than a legal newsletter is who accepts it.  Terms updates are accepted by whoever next opens the app on the brand account, which in most companies is the most junior person in the social team, at speed, on a phone.  That click binds the accepting entity.",
                    "The autonomous actions line is the second half.  Any team using an automated posting tool, a scheduler with agent features or an AI reply assistant on X has just been told in writing that whatever it does is theirs.",
                ],
                "so_what": "Nothing about your buying on X changes this week, which is exactly why this gets missed.  What changed is the size of the downside if something goes wrong, and the fact that the person who agrees to it on your behalf has no idea they are doing it.  Platform terms are the one contract in your marketing stack that nobody negotiates and everybody signs.",
                "do_this": "Send the updated X terms to whoever handles your contracts before anyone on your team accepts them, and get a named person other than the day-to-day social manager to be the one who does.  While you are there, list every automated or AI tool with posting rights on your X account and decide which ones keep them.",
            },
        ],
    },
    {
        "id": "onstream", "name": "ON STREAM", "page": "pg. 05",
        "note": "what the biggest live audiences of the week were actually worth",
        "tint": None,
        "items": [
            {
                "title": "Apple's own channel carried 3.1 million of the 3.4 million peak, and everyone co-streaming it shared the difference",
                "hook": "The biggest single livestream of the week was brand-owned, and the brand's own channel did about nine tenths of it.",
                "open": True,
                "stamps": [
                    ("STREAMS CHARTS · 10 SEP", "https://streamscharts.com/news/apples-iphone-duo-reveal-draws-34m-peak-viewers-livestreaming"),
                    ("STREAMS CHARTS · 10 SEP 2025", "https://streamscharts.com/news/apple-event-2025-iphone-17-revealed"),
                    ("STREAMS CHARTS · 11 SEP 2024", "https://streamscharts.com/news/apples-iphone16-presentation-viewership"),
                ],
                "body": [
                    "Apple's iPhone Duo event ran on Tuesday and drew <mark>more than 3.4 million concurrent viewers at its peak across all channels, with more than 3.1 million of those on Apple's own YouTube channel.</mark>  That is about nine tenths of the peak sitting on the brand's own account — our calculation from the two figures Streams Charts publishes.  Streams Charts ranks it third among Apple events ever by peak viewers, behind the company's September showcases in 2022 and 2024.",
                    "Put the number somewhere recognisable, because three point four million concurrent means nothing on its own.  It is roughly <mark>38 sold-out Wembley Stadiums watching the same thing at the same second</mark> — again our arithmetic, on Wembley's 90,000 capacity.  Against gaming, the year's benchmark is the GTA VI gameplay reveal on 27 August, which peaked at 3.97 million across every platform with more than 9,000 channels co-streaming it.  Apple got within 14% of that with essentially one channel.",
                    "The trend line matters more than the rank.  Apple's September 2024 event peaked at 3.57 million.  September 2025, the iPhone 17, peaked at 2.8 million.  This one, 3.4 million — up about 21% year on year and still short of 2024.  A foldable phone and a new chief executive bought back most of a bad year, which is a useful reminder that a brand channel's audience tracks what you have to announce far more than how well you produce it.",
                    "The creator layer was there and it was not the story.  IShowSpeed attended in person and drew the largest audience among independent channels, and Streams Charts does not publish his peak.  Tim Cook, who handed the chief executive job to John Ternus earlier this month, appeared only briefly.",
                    "One honest caveat on the comparison.  Streams Charts does not publish average concurrents, hours watched or airtime for this event, and peak alone tells you about the size of the moment rather than how long anybody stayed.  A two-hour keynote and a three-hour gameplay reveal are not the same product even when their peaks are close.",
                ],
                "numbers": [
                    ("3.4M", "peak concurrent viewers across all channels for Apple's iPhone Duo event"),
                    ("3.1M", "of those on Apple's own YouTube channel"),
                    ("3.97M", "peak for the GTA VI gameplay reveal on 27 August, across 9,000-plus channels"),
                ],
                "flagnote": "Streams Charts publishes only peak viewers for this event — no average concurrents, no hours watched, no airtime and no channel count — so the comparison with the GTA VI reveal is peak against peak and nothing else.  The nine-tenths share and the Wembley comparison are this brief's calculations from the published figures, not Streams Charts numbers.  IShowSpeed's individual peak is not disclosed.  Peaks across separate channels are not strictly additive either, so read the nine-tenths figure as a share of the aggregate peak rather than as a head count.",
                "so_what": "The standard argument for creator co-streams is reach you cannot get on your own channel.  This is the largest brand livestream of the year and its own channel carried about nine tenths of the peak, which means the co-stream layer was doing something other than supplying the audience.  What it supplies is a second room where people react, argue and clip — valuable, but not the number.  Buy it as commentary, and price it that way.",
                "do_this": "For your next live event, set two separate targets before you book anybody: a peak for your owned channel and a peak for the co-stream layer.  Ask every livestream proposal you receive for peak, average concurrents, hours watched and airtime together, and refuse to price one of them without the other three.",
            },
        ],
    },
    {
        "id": "money", "name": "THE MONEY", "page": "pg. 07",
        "note": "the numbers that change what a thing is worth buying",
        "tint": None,
        "items": [
            {
                "title": "Snap says creator-made ads hold attention 16 percent better than the ads brands make themselves",
                "hook": "Played 25 percent longer.  16 percent more active attention.  Snap's own numbers, on Snap's own inventory.",
                "open": True,
                "stamps": [
                    ("SOCIAL MEDIA TODAY · 9 SEP", "https://www.socialmediatoday.com/news/snap-ceo-discusses-ad-development-and-ai/829986/"),
                ],
                "body": [
                    "Evan Spiegel published a letter to Snap staff on Tuesday marking the company's fifteenth anniversary, and Andrew Hutchinson pulled the numbers that matter to a video team out of it at Social Media Today.  <mark>Creator ads played 25% longer than standard branding ads and drove 16% more active attention</mark>, and <mark>more than 300,000 creators</mark> on Snapchat are now eligible to work with brands.",
                    "Those two figures are the same comparison run twice — identical placement, identical platform, different maker.  Duration held and attention paid both move in the creator's favour, and neither is explained by reach, targeting or budget, because none of those changed.",
                    "Be clear about what this is, though.  It is a chief executive's staff letter, not a study.  Snap has published no methodology, no time period, no sample size and no definition of what counts as a standard branding ad, and Snap sells the inventory the comparison flatters.  Take the direction and treat the size of it as unproven.",
                    "The rest of the letter explains why Snap wants you to believe it.  Spiegel is building toward what he calls generative advertising, meaning ads assembled by an AI model from what it thinks you want next rather than from something you searched for.  His argument for it: today, digital advertising relies heavily on explicit intent signals, like searching for a product or visiting a website and adding something to your cart.  It is difficult for advertisers to generate incremental demand instead of competing to convert intent that already exists.",
                    "That is an honest description of a real problem — most performance advertising harvests demand that was already there and calls it growth — and it is also a sales pitch for a product that does not yet exist, with no launch date, no pricing and nothing to buy.  What you can act on is the creator number, today, on inventory you already have access to.",
                ],
                "flagnote": "Every figure here comes from Snap's own internal data, disclosed inside a staff letter rather than a research release, with no methodology, no sample size, no field dates and no definition of a standard branding ad.  Snap sells the advertising the comparison favours, and active attention is Snap's own measure rather than an independent one.  Generative advertising has no launch date, no pricing and no buyable product attached.",
                "so_what": "Two different platforms have now put a number on the same thing in a month: an ad made by the creator outperforms the same idea made by the brand, in the same slot.  The variable is not production budget, because the brand version almost always has more of it.  It is that one of them looks like the platform it is sitting on and the other looks like an advertisement someone bought space for.",
                "do_this": "Take your next Snap or vertical video buy and split it: half the budget on the asset your team made, half on the same brief handed to a creator to make their own way, same placement and same spend.  Compare completion rate rather than reach, and report both numbers even if the wrong one wins.",
            },
        ],
    },
    {
        "id": "format", "name": "FORMAT LAB", "page": "pg. 08",
        "note": "the format decision underneath the numbers",
        "tint": None,
        "items": [
            {
                "title": "An investment firm that owns the CSI library is buying YouTube channels, and it screens them on one question",
                "hook": "Would somebody watch this in five years?  Hot Ones passes.  Anything built on the news fails.",
                "open": True,
                "stamps": [
                    ("NET INFLUENCER · 10 SEP", "https://www.netinfluencer.com/why-a-hollywood-ip-investment-firm-is-treating-youtube-channels-like-film-libraries/"),
                ],
                "body": [
                    "Cecilia Carloni reported this at Net Influencer yesterday.  Content Partners, founded in Los Angeles in 2006 and holder of film and television libraries including CSI, launched Wonderloom Media in July 2026 to buy YouTube channels as catalogue assets.  Its first purchase is Dr Insanity, a long-form true-crime channel with <mark>5.8 million subscribers and episodes running 44 to 55 minutes.</mark>",
                    "John Mass, the firm's president, joined in 2014 after seventeen years at William Morris Agency.  His screen is one question, and he benchmarks it against The Godfather and The Shawshank Redemption: <mark>is it the kind of thing that I could watch today, and I could watch it five years from now</mark>.  Hot Ones passes.  Dr Insanity passes, because videos two and three years old are still accumulating views.  News-driven material fails, and he says why in one line: today it's worth something, tomorrow worth less, two days from now worth even less.",
                    "Here is why this is a format item rather than a business one.  Nearly everything that makes a video fail that test is put into it deliberately, in the edit, for a good reason at the time.  The topical joke in the first thirty seconds.  The reference to last week's upload.  The date in the voiceover.  A price on screen.  A trending sound under the montage.  Each buys a little attention this month and sets an expiry date on the file.",
                    "Which reframes what a brand is buying when it funds a series.  If your sponsored video is built on a moment, you have bought a month of views.  If it is built on a question people will still be asking in three years, you have bought a shelf, and the cost of reaching a thousand people on it keeps falling for as long as it keeps being found.",
                    "Mass is also candid about the limits, and it is worth hearing.  He puts the share of creators building genuinely durable businesses at roughly 1%, and describes the rest as chasing metrics without building a lasting relationship with an audience.  He is talking about what he will not buy, which is a more useful signal than what he will.",
                ],
                "so_what": "Whether a video has a shelf life is decided in the timeline, not in the brief, and almost nobody treats it as a commercial decision.  An investment firm applying film-library economics to YouTube is now pricing exactly that, which gives you a test you can apply to your own work before you commission it.  The version of your video that strips out the dates, the prices and the topical references is usually 5% less fun and worth several times more over three years.",
                "do_this": "Take the sponsored video you are briefing next and list everything in it that will be out of date in twelve months — a price, a date, a trend, a reference to another video.  Cut what you can, move what you cannot into a separate short, and brief the main piece around a question somebody will still be searching for in 2029.",
            },
        ],
    },
]

FORECAST = [
    {
        "confidence": "LIKELY",
        "window": "by 30 June 2027",
        "headline": "Time from brief to published post becomes a number brands report and agencies get judged on",
        "body": "Molson Coors has put a performance figure next to an approval process, which is the first thing needed to turn an internal annoyance into a benchmark.  Once one large advertiser can say its social engagement quadrupled after it rebuilt its review lanes, every marketing director with slow legal gets a number to point at, and every agency pitch starts including cycle time because a rival's does.  The measure is easy to calculate and embarrassing to publish, which is usually the combination that makes a metric spread.",
        "do": "Start logging brief-to-publish elapsed days on every social piece now, so that when somebody asks for the number in six months you have a baseline rather than an estimate.",
    },
    {
        "confidence": "LIKELY",
        "window": "by 31 December 2026",
        "headline": "A named brand gets publicly called out for an undisclosed AI performer in an ad",
        "body": "New York's law has been enforceable since June, complaints are already arriving, Hawaii has matched it, California is a signature away and the EU's transparency rules are live.  Enforcement sits with attorneys general rather than private claimants, which means the first case will be chosen for visibility rather than for damages.  The carve-outs that lawyers are flagging — synthetic voices, partial shots, background crowds — are precisely where a brand will get caught being technically compliant and publicly wrong, and that argument plays out in the press long before it reaches a court.",
        "do": "Decide now, in writing, whether your brand discloses AI-generated humans everywhere or only where a law compels it, so the answer exists before a journalist asks for it.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "by 30 September 2027",
        "headline": "The price of a YouTube channel acquisition leaks, and creator rate expectations reset around it",
        "body": "Wonderloom is buying channels as libraries and nobody has published a multiple.  The moment one deal price becomes public — through a lawsuit, a disclosure, or a seller who talks — every creator with a durable catalogue can value their channel against it, and the conversation about a sponsorship fee starts sitting next to a number for the whole asset.  That changes who you negotiate with too, because a creator who knows what their library is worth thinks differently about signing a year of exclusivity to a single brand.",
        "do": "Ask the creators you work with most whether they have been approached about selling, and find out who else has been buying in your category before you next negotiate an exclusive.",
    },
    {
        "confidence": "LONG SHOT",
        "window": "by 31 December 2027",
        "headline": "A major brand buys a creator's back catalogue instead of sponsoring new videos",
        "body": "If library economics work on YouTube, the logical buyer is not only an investment firm.  A brand that owns three years of a channel's videos owns the search results, the recommendation surface and the sponsor slot in all of them, at a price fixed once, while the views keep arriving.  The reason it is a long shot is that brands are structurally bad at buying assets rather than campaigns, and the first company to try it will have to explain to a finance team why a purchase belongs in a marketing budget.  The one that gets the explanation right acquires a permanent distribution channel for roughly the cost of a year of sponsorships.",
        "do": "Price it as a thought experiment before you need to: work out what three years of your best creator partner's catalogue would cost against what you have paid them in sponsorship over the same period.",
    },
]

TLDR = [
    "Molson Coors quadrupled engagement on its creator content after moving social out of a television approval process and sorting every decision into three lanes, one of which is a straight yes, across 230 marketers and more than a hundred brands.  Measure brief-to-publish elapsed days on your last five social pieces this week and ask for a fast-track lane below a named spend threshold.",
    "Almost 90% of affluent shoppers told Precisify that watching a creator run a real-time test of a luxury product made them more confident in its quality than a polished commercial did, and they trust creators at 38.4% against celebrities at 8%.  Commission one unscripted test of your highest-consideration product, leave the failure in the cut, and judge it against your last polished film on conversion.",
    "Higgsfield AI paid the streamer N3on to run an AI-generated version of himself when he is offline, it became the most-viewed of his last twenty streams, and other creators described it as removing himself from the equation.  Add a clause to your creator contract template requiring the named human to appear in and approve every deliverable, with no synthetic likeness carrying your brand.",
    "Walgreens is putting screens into 1,200 stores from October with Looma, having spent 200 million dollars on a previous programme whose screens sat in front of the products and flickered, crashed, showed the wrong items and caught fire.  Write down what the viewer was trying to look at for every placement you are buying this quarter, and cut the ones your video is standing in front of.",
    "Apple's iPhone Duo event peaked above 3.4 million concurrent viewers with more than 3.1 million of those on Apple's own channel, within 14% of the GTA VI reveal's 3.97 million peak that needed 9,000 co-streaming channels.  Set separate peak targets for your owned channel and your co-stream layer before your next live event, and demand peak, average, hours watched and airtime together on every proposal.",
    "New York has required advertisers to disclose AI-generated synthetic performers since June, Hawaii has matched it, California is awaiting a signature and the EU's transparency rules are live, with carve-outs for synthetic voices and no clarity on background crowds.  Build a register this week of every live asset containing an AI-generated human and add a synthetic-performer field to your sign-off sheet.",
    "An investment firm holding the CSI library is buying YouTube channels as catalogue assets and screens them on whether somebody would still watch in five years, which news-driven content fails and Hot Ones passes.  List everything in your next sponsored video that expires within twelve months, cut what you can, and brief the main piece around a question people will still be searching in 2029.",
]

SHARE = [
    {
        "who": "JARED · CEO",
        "angle": "The four-times gain in Molson Coors' creator performance was produced by the legal department, not the creative one.",
        "post": "Molson Coors has quadrupled engagement on its creator content since March. The department that produced that number was legal.\n\nDigiday reported it this morning. The company stopped routing social work through a television-era approval process and rebuilt the decisions into three lanes: fast-track, needs a conversation, and hard no. Justine Stauffer, who runs creative effectiveness there, says the lawyers sat inside the process the whole way and learned how the ecosystem actually works. 230 marketers across more than a hundred brands now work that way.\n\nNobody hired a better agency. Nobody found a better creator.\n\nThey shortened the distance between an idea and a published post.\n\nI have sat in a lot of meetings where the proposed fix for weak social performance was more creative. It is almost never the creative. It is the eleven days the creative spent in review, arriving after the thing it was responding to stopped being interesting.\n\nThe part I keep turning over is that this had no media cost attached. There is nothing to buy here. There is only a decision to make about who has to be in a room before something gets posted.\n\nEngagement is a soft number and Molson Coors has published no sales figure next to it. I would still take that trade.",
        "why": "It reframes a performance gain that everyone will read as a creative win into an argument about organisational speed, which is the one lever a chief executive can actually pull.",
    },
    {
        "who": "JAMES · CREATIVE DIRECTOR",
        "angle": "Almost nine in ten wealthy buyers said an unscripted test beat a polished film, which makes production value the liability rather than the asset.",
        "post": "Almost 90% of wealthy shoppers said watching a creator run a real-time test of a luxury product made them more confident in its quality than a polished commercial did.\n\nThat is from Precisify, surveying 500 US adults earning over 150,000 dollars. The same survey put trust in creators at 38.4% and trust in celebrities at 8%.\n\nI want to be fair about it. Five hundred people, a company that sells advertising intelligence, and stated preference rather than observed purchasing.\n\nBut the direction is not flattering to my side of the business, and I cannot argue it away.\n\nThe polished film is the thing creative directors are proudest of. The lighting, the grade, the right lens on the right day. What it signals to somebody about to spend five thousand pounds is that the brand controlled every frame.\n\nWhich is the problem. A test can go wrong while you are watching it. A commercial cannot. That is why one reads as evidence and the other reads as decoration.\n\nSo the honest implication is that a chunk of the money should move from the film to the demonstration. I do not especially like it. Craft was not the variable here. Exposure to being wrong on camera was.",
        "why": "A creative director conceding that production value actively works against conviction at the point of purchase is both surprising and defensible from the data.",
    },
    {
        "who": "LAWRY · LEAD VIDEO EDITOR",
        "angle": "Whether a video still has value in five years is decided in the timeline, by choices nobody in the room treats as commercial ones.",
        "post": "A Hollywood investment firm that owns the CSI library has started buying YouTube channels, and it screens them the way it screens films. John Mass, its president, describes the test as content he could watch today and still watch five years from now.\n\nHot Ones passes. News-driven content fails, because it is worth less tomorrow than it is today.\n\nIts first purchase was Dr Insanity, a true-crime channel whose videos are still pulling views two and three years after they went up.\n\nHere is the part that sits in the edit.\n\nAlmost everything that stops a video passing that test is put there by an editor, deliberately, usually for a sensible reason at the time. The topical joke in the cold open. The line about last week's upload. The date in the voiceover. A price on screen. A trending sound under the montage.\n\nEach one buys a bit of attention this month and quietly sets an expiry date on the file.\n\nMost editors would call those pacing decisions. They are valuation decisions, and nobody in the room says so out loud.\n\nI still put some of them in, because the version without them is flatter. The choice being made in the timeline is whether this is an asset or a post, and it gets made by whoever is trying to hold the middle together at four in the afternoon.",
        "why": "It shows a routine editing habit turning out to be the thing that decides whether a video has a three-year shelf life, which is a decision nobody credits an editor with making.",
    },
]
