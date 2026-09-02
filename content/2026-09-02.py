# -*- coding: utf-8 -*-
"""Content for THE FEED — issue data only.  The render spec lives in build_feed.py."""

ISSUE = {
    "date_iso": "2026-09-02",
    "kicker": "Crux Media // Wednesday 2 September 2026",
    "tagline": "What brands did on YouTube yesterday, and whether it worked.",
    "pace": "STEADY",
    "next_drop": "Next drop: Thursday, 06:30 MT",
}

LEAD = {
    "headline": "A COMPANY SITTING ON A HUGE VIDEO LIBRARY WENT FROM 1 MILLION VIEWS A MONTH TO 150 MILLION.  THE LIBRARY DID NOT CHANGE",
    "deck": "Collab licenses other people's clips for a living.  One of its YouTube channels sat at 500,000 to 1 million views a month for years off that library.  In January one of the founders started writing and improvising voiceovers over the same footage.  By July the channel was doing 150 million views a month.",
    "stamps": [
        ("TUBEFILTER · 1 SEP", "https://www.tubefilter.com/2026/09/01/rufus-goodboy-collab-will-mcfadden-animal-youtube-compilation-channel/"),
        ("YOUTUBE CHANNEL", "https://www.youtube.com/@Rufusisagoodboy"),
    ],
    "body": [
        "The channel is called Rufus Goodboy and it posts talking-animal compilations.  Stay with it, because the business underneath is the point.  Collab is a company the McFadden brothers founded in 2012 that collects, licenses, manages and protects the usage rights of user-made video.  Owning clips is the entire business.  The channel launched around 2019 or 2020 as a straight compilation channel pulling from that library, and it did what straight compilation channels do: <mark>it floated between 500,000 and 1 million views per month</mark> for years.",
        "In January 2026 Will McFadden, Collab's chief creative officer, took direct control and started doing the voices himself.  He curates the week's clips, picks animals that are expressive and emoting, and talks over them.  <mark>The channel has gone from around 80,000 subscribers to over 700,000, and in July it hit 150 million views per month.</mark>  We checked the channel this morning: 716,000 subscribers.",
        "Nothing else changed.  Same library.  Same licensing.  No new shoots, no crew, no location, no talent fee.  The input that moved the number was a person with a microphone deciding what the dog is thinking.",
        "Two craft details are worth stealing, and they are both counter-intuitive.  The first is that he does not lip-sync.  He calls it a Homeward Bound-style voiceover and speaks over a closed mouth rather than matching the animal's mouth movements.  Every instinct in an edit suite says to sync the audio to the picture.  He deliberately does not, and the result reads as a thought rather than as a puppet show.",
        "The second is that the reads are improvised.  In his words: usually the voiceover is improvised, and he likes the looseness of improv, the mistakes and the little eccentricities that come with riffing.  A scripted read on animal footage lands as a joke being told at you.  A messy one lands as somebody in the room with you, watching the same clip.",
        "For anyone running an owned channel, the number that should sting is the one before the change.  Collab had the rarest asset in the category — a legally clean, enormous, exclusive video library — and for six years it converted that into about a million views a month.  The library was never the asset.  The write was.",
    ],
    "numbers": [
        ("150M", "views in July 2026, from 500,000 to 1 million a month before"),
        ("716K", "subscribers, up from around 80,000 when the voiceovers started"),
        ("0", "new footage shot to produce any of it"),
    ],
    "flagnote": "The view and subscriber history comes from Tubefilter's interview with Will McFadden and is supplied by Collab.  It is not independently audited.  The current subscriber count is the one YouTube displays on the channel page and we read it directly.  Note also that the channel posts roughly twice a day plus vertical clips, so the monthly total spans a lot of uploads rather than a few hits.",
    "so_what": "Archive is cheap and interpretation is expensive, and almost every brand has the ratio backwards.  Companies spend enormous money acquiring footage and almost nothing on the person who decides what it means, then wonder why the library underperforms.  This is the same argument Google made yesterday with its own conversion numbers, arriving from the opposite direction — there, a voice was worth 12 percent on a paid ad; here, a voice was worth the entire channel.",
    "do_this": "Pull your three worst-performing owned videos this week and recut one of them with nothing changed except a new improvised voiceover recorded in a single unscripted pass.  Ship it as a new upload and compare it against the original.  If your company has a footage archive nobody touches, put one writer on it for two weeks before you commission anything new.",
}

SECTIONS = [
    {
        "id": "ws", "name": "W'S", "page": "pg. 02",
        "note": "what worked, and the exact reason it worked",
        "tint": "blue",
        "items": [
            {
                "title": "Brands are buying older creators, and the thing they are actually buying is a timestamp",
                "hook": "You cannot art-direct having been through something.  That is the whole mechanism.",
                "open": True,
                "stamps": [("DIGIDAY · 2 SEP", "https://digiday.com/media/why-brands-are-turning-to-older-creators-for-authenticity-ai-cant-fake/")],
                "body": [
                    "Digiday reported this morning on brands moving budget toward creators who have aged on camera alongside their audience.  The clearest case in the piece is Alex and Jon, a couple with more than 10 million followers who started in August 2020 posting dual-income-no-kids content.  When they announced a pregnancy, part of the audience turned on them.  Then Madison had a miscarriage at 27 weeks.  They now have a daughter, and Similac has signed them for a campaign about the reality of motherhood.",
                    "The other example is smaller and more instructive.  Ellie Fletcher is a hairdresser with 36,000 TikTok followers and 3.5 million likes who started the account to build a client list.  In 2025 she began talking about infertility and endometriosis.  Women's health brands now partner with her.  36,000 followers.",
                    "The numbers around it are borrowed rather than new, and worth naming precisely.  A WordPress VIP survey cited in the piece has <mark>60% of US consumers describing AI in brand messaging as a turnoff</mark>.  eMarketer has 34% of social users more likely to buy based on an authentic creator review.  Edison Research has 47% of TikTok users aged 25 to 44 buying products they heard about on the platform.  And Harris Poll data from March this year has close to two-thirds of Gen Z saying they have stopped buying through TikTok Shop.",
                    "Lauren Lyster, who heads social at Go Fish Digital, puts the supply side plainly: as this generation of creators has grown up, the topics they cover have matured right alongside them.  Nilou Ajdari at Currents Management says the briefs coming in have shifted toward deeper partnerships that want conversation rather than a post.",
                ],
                "so_what": "Every other input in a creator deal can now be synthesised.  A face, a voice, a kitchen, a script, a plausible life — all of it is cheap to fake and getting cheaper.  What cannot be faked is that a specific person was publicly on the record about something difficult before your brief existed, with a date on it.  That is why the 36,000-follower hairdresser gets women's health money and a bigger account does not.",
                "do_this": "For your next health, parenting, finance or care category brief, search your shortlisted creators' back catalogue for the moment they first talked about the thing your product addresses, and check it predates your category interest by at least a year.  Buy the ones where it does, and let them talk about it in their own words instead of writing them a script.",
            },
            {
                "title": "Hershey's built a 60-second spot around a hand gesture it did not have to invent",
                "hook": "The creative job here was recognition, not invention, and that is uncomfortable to say out loud.",
                "stamps": [("MARKETING DIVE · 1 SEP", "https://www.marketingdive.com/news/how-hersheys-katseye-campaign-takes-on-gen-zs-desire-for-indulgence/829013/")],
                "body": [
                    "Hershey's launched an integrated campaign for salted caramel and affogato Creme Bars with the girl group Katseye, whose Wild EP debuted at number one on the Billboard 200 in August.  The centrepiece is a 60-second spot set on a subway train.  A member bites the bar, the group's track Pinky Up kicks in, and the carriage breaks into choreography built on the pinky gesture the song is named after.",
                    "Look at what the creative team had to supply.  Not the song.  Not the gesture.  Not the choreography.  Not the audience that already knows the move.  All four of those arrived attached to a record that was already at number one.  The team supplied the subway, the product moment and the edit.  Origin story, per Marketing Dive: somebody on the team watched Katseye play Pinky Up at Coachella.",
                    "Two operational details worth noting.  The creative is split across two holding companies — MiltonOne inside Publicis made it, with creative direction from Omnicom's Martin.  And this is a term deal running through 2026 and into next year with in-person appearances, not a one-off spot.  Senior brand manager Katrina Vatter framed the brief as how to infuse it with Gen Z culture in a way that is authentic and not cringy.",
                    "The spend context sits in the same piece.  Hershey posted 3.6% organic net sales growth in Q2 2026 and plans a 30% year-on-year increase in brand investment through 2027.",
                ],
                "so_what": "A gesture that already exists in a hit song comes with something no brand can buy: an audience that already performs it.  You are not teaching a behaviour, you are borrowing one, which removes the most expensive and least reliable part of a campaign.  The reason this is uncomfortable is that the highest-value decision was made by whoever was at Coachella paying attention, not by anyone at a whiteboard.",
                "do_this": "Before your next music or talent partnership, list the specific physical action, catchphrase or gesture your audience already does because of that artist, and build the spot around that instead of around the person.  If you cannot name one, you are buying a face and you should price it as a face.",
            },
        ],
    },
    {
        "id": "ls", "name": "L'S", "page": "pg. 03",
        "note": "what broke, and the failure mode behind it",
        "tint": "pink",
        "items": [
            {
                "title": "Wrong economics: the fix for creator pricing just slipped a month, and the people calling it a bubble are now the creators",
                "hook": "Everyone has been waiting on one document.  It moved from September to October, so stop waiting.",
                "open": True,
                "stamps": [("DIGIDAY · 2 SEP", "https://digiday.com/future-of-tv/future-of-tv-briefing-how-strong-are-the-fundamentals-of-the-creator-economy-really/")],
                "body": [
                    "Digiday's Future of TV briefing this morning asks whether the branded content half of the creator economy has fundamentals underneath it at all.  The framing is that a market with no agreed price and no agreed measurement corrects eventually, the way the automated ad-buying market did.",
                    "The concrete, dated thing in it: the IAB's measurement currency guidelines for creator media, which the industry has been waiting on to settle what a creator impression even is, <mark>have moved from a September release to October 2026</mark>.  That is the mechanism everyone has been pointing at when asked how they plan to fix pricing.  It just moved.",
                    "The rest is the market talking about itself.  Emma Chamberlain, on a podcast, says the bubble seems to be bursting right before it is about to burst.  Gabe Gordon at Reach Agency says creators are not interchangeable media inventory.  Harley Block, chief executive of IF7, calls creator pricing out of control.  Danielle Wiley, who runs Sway, claims brands overpay 90% of the time — an assertion from an agency chief, not a measurement.  Digiday puts the 2026 creator economy at $43.9 billion with no source attached to the figure.",
                    "We covered the underlying pricing survey last week, so treat that as known: Billion Dollar Boy's poll of 1,000 marketing and procurement leaders found half misprice creator fees and 40% of those felt they had overpaid.  What is new today is the timeline slipping and who is saying it out loud.",
                ],
                "flagnote": "Almost every number in this piece comes from a company that sells influencer marketing services and benefits from the industry looking either bigger or more in need of fixing.  The 90% overpayment claim is one agency chief's estimate with no method behind it.  The $43.9 billion market size carries no attribution in the article.",
                "so_what": "Waiting for a standard is a strategy with a delivery date attached, and that date has now moved once.  A standard that slips a month usually slips again, and even when it lands it will be guidance rather than something anyone is obliged to trade on.  The brands that will be fine in Q4 are the ones that wrote their own definitions into their own contracts instead of holding a slot for somebody else's.",
                "do_this": "Write your own definition of a paid creator impression into every Q4 contract this week — which platform, which view standard, what counts as delivered, and what the remedy is if it under-delivers.  Do not put an IAB reference in the contract, because the document is not out and the date has already moved.",
            },
            {
                "title": "Wrong owner: the FTC says YouTube's published rules and its enforced rules are two different documents",
                "hook": "Your brand safety plan is built on the published one.  That is the exposure.",
                "stamps": [("TUBEFILTER · 1 SEP", "https://www.tubefilter.com/2026/09/01/youtube-moderation-ftc-lawsuit-violative-video/")],
                "body": [
                    "Bloomberg reported on 27 August, citing people familiar with the probe, that the Federal Trade Commission is in the final stages of preparing a complaint against YouTube.  Tubefilter wrote it up yesterday.  The allegation is not about content.  It is a deception case: that YouTube's publicly stated rules appear to permit content which the platform later treats as violative, producing suspensions and demotion in the algorithm.",
                    "FTC chair Andrew Ferguson said in August that whatever your policies are, you have to follow them, and that you cannot present one form of policy to consumers and then have a completely different one in practice.  No filing date has been announced and YouTube has not commented.",
                    "Read past the creator-suspension angle to the advertiser one.  Your suitability settings, your exclusion lists, your agency's brand safety commitments and every assurance you have given a client about where your ads will not appear are all built on YouTube's published policy documents.  The FTC's entire theory is that the published document is not the operative one.",
                    "The direction of the risk is worth being precise about.  If the FTC prevails or settles, YouTube gets pushed toward publishing what it actually enforces, which is good for planning and probably bad for inventory volume.  Nobody should be modelling that yet.  But the cheap move — knowing which of your own controls depend on YouTube's word rather than on your own verification — costs an afternoon.",
                ],
                "flagnote": "This is a rumoured complaint reported by Bloomberg from unnamed sources.  Nothing has been filed, no policy categories have been identified, and YouTube has not responded.  Treat it as a signal about regulatory direction, not as a fact about YouTube's conduct.",
                "so_what": "Every brand safety promise in your business ultimately terminates in a platform policy page that the platform can reinterpret without telling you.  You are not buying a guarantee, you are buying a description of intent.  That has always been true and it is about to be argued in public, which is the part that changes client conversations.",
                "do_this": "List every brand safety commitment in your live client contracts that depends on a platform's published policy rather than on something you measure yourself, and put a verification step against each one this week.  Then check whether your own creator agreements let you take an asset down for reasons the platform has not flagged.",
            },
        ],
    },
    {
        "id": "moves", "name": "MOVES", "page": "pg. 04",
        "note": "who did what, and what it changes",
        "tint": None,
        "items": [
            {
                "title": "The NFL renewed TikTok a week before kickoff, and the interesting part is what advertisers can buy next to",
                "hook": "The league sells adjacency to its own account now.  Most rights holders still cannot.",
                "stamps": [("ADWEEK · 2 SEP", "https://www.adweek.com/convergent-tv/nfl-expands-tiktok-playbook-with-renewed-deal/")],
                "body": [
                    "Adweek reported this morning that the NFL has renewed its TikTok partnership on a multi-year deal, ahead of a season that starts on 9 September.  Three components matter.  TikTok GamePlan gives the league dedicated hubs and branded experiences.  Pulse Premiere keeps NFL inventory in TikTok's ad product, which lets an advertiser place its content directly alongside the @nfl account and official club accounts.  And TikTok is extending its Pro Events feature to the NFL with a dedicated fan hub launching in the coming weeks.",
                    "No financial terms, no view numbers and no named executives were disclosed in the piece.",
                    "The Pulse Premiere piece is the one to understand, because it is a rights structure rather than a media buy.  The league has agreed that a third party can pay to sit next to its owned social output.  That is a rights holder monetising its own organic feed as inventory, and very few sports properties have that switched on.",
                    "The Pro Events hub matters differently.  It is a permanent destination inside TikTok for a season that runs to February, rather than a set of posts that decay in a feed.  A hub with a season behind it is a place a brand can buy a presence in repeatedly.  A post is not.",
                ],
                "so_what": "There is a difference between advertising against football and advertising inside the football account's neighbourhood, and only the second one borrows the league's credibility.  For any brand without an official league deal, this is the closest legal substitute — and the reason it exists is that the league worked out its organic feed was inventory it already owned.",
                "do_this": "If you have NFL-adjacent spend this autumn, ask your TikTok rep specifically about Pulse Premiere availability against @nfl and club accounts before the 9 September opener, because the good adjacencies sell out first.  And if you represent any rights holder, price your own organic feed as sellable adjacency this quarter.",
            },
            {
                "title": "Ina Garten is launching a YouTube channel and Vox Media is selling it",
                "hook": "A television cook goes owned video, and a media company takes the sales job.",
                "stamps": [("NET INFLUENCER · 31 AUG", "https://www.netinfluencer.com/ina-garten-launches-youtube-channel-with-vox-media-backed-video-podcast/")],
                "body": [
                    "Ina Garten has launched her first official YouTube channel.  The show is Happy Hour With Ina Garten, a weekly video podcast filmed in her New York apartment covering food, culture, entertainment, sports and the arts.  It premieres Wednesday 16 September and runs every Wednesday at 5am Pacific, also going out on Apple Podcasts, Spotify, Instagram and TikTok.",
                    "Vox Media produces it and handles sales, marketing and distribution.  No audience numbers were disclosed.",
                    "The structure is the story.  A talent with three decades of television behind her did not sign a network deal and did not self-publish.  She took a media company as a commercial partner and kept the channel in her own name.  Vox does the part that is genuinely hard for an individual — selling it — and the show lives on a platform where the audience does not need a subscription to find it.",
                ],
                "so_what": "The sales function is the last thing an individual talent cannot replicate alone, and it is now available as a service without giving up the channel.  For a brand, that means the number of credible, professionally sold, personality-led video properties is going up fast, and most of them will be cheaper than a comparable television buy for the first year while nobody has a benchmark.",
                "do_this": "Ask your agency for a list of personality-led video podcasts launching this autumn that have a media company handling sales, and get on the first-season rate card before there is a delivery history to price against.  Set your success measure on completed views, not impressions, before you sign.",
            },
        ],
    },
    {
        "id": "onstream", "name": "ON STREAM", "page": "pg. 05",
        "note": "live audiences, and what the numbers actually mean",
        "tint": None,
        "items": [
            {
                "title": "Twitch had its biggest month of the year with fewer people at its peak",
                "hook": "Average audience up 6 percent, peak down 10 percent.  That combination tells you exactly what to buy.",
                "open": True,
                "stamps": [
                    ("STREAMS CHARTS · 1 SEP", "https://streamscharts.com/news/twitch-august-2026-results"),
                    ("STREAMS CHARTS · 28 AUG", "https://streamscharts.com/news/gta-vi-gameplay-reveal-viewership"),
                    ("STREAMS CHARTS · 9 SEP 2025", "https://streamscharts.com/news/z-event-2025-charity-records"),
                ],
                "body": [
                    "Streams Charts published Twitch's August numbers yesterday and they are the strongest of 2026.  <mark>1.56 billion hours watched.  Average concurrent viewers 2.14 million, up 6% on July.  Peak concurrent viewers 4,173,855, down 10% on July.</mark>",
                    "Average up and peak down at the same time is the signature of a month carried by duration rather than by moments.  The category data confirms it.  Escape from Tarkov did 51.2 million hours watched, up 525% on July on the back of a patch.  Minecraft was up 54%, driven by the Kai Cenat and IShowSpeed marathon.  Dota 2 more than doubled on The International.  Counter-Strike was up 38% on the Esports World Cup.  Simulator games were up 45% month on month on both hours and average viewers.  League of Legends was the only top-ten game to fall, and general life content was down 12%.",
                    "Give the peak a comparison that means something.  4,173,855 people watching Twitch simultaneously is larger than the entire cross-platform peak for the GTA VI gameplay reveal on 27 August, which drew 3.97 million concurrent viewers across every platform at once and was the biggest single gaming moment of the year.  Twitch on an ordinary August night out-peaks the whole industry's biggest event.",
                    "And a scale check on the hours.  1.56 billion hours in one month is around 178,000 years of continuous watching, from one platform, in 31 days.",
                    "The GTA VI reveal itself carries a warning for anyone planning a live moment.  The official broadcast went out on Netflix at 19:00 UTC on 27 August.  Netflix and Twitch both buckled and some viewers could not get in for 40 to 50 minutes.  Streams Charts analysed over 100,000 chat messages and found negative sentiment at 17 to 20%, mostly aimed at the technical failure.  What saved the audience was 9,000 or more streamers restreaming it, who between them generated 5.2 million hours watched, with Twitch taking 44% of those hours, YouTube 34.8% and Kick 20.2%.",
                    "One to diary.  ZEvent runs its tenth and final edition this week — opening concert Thursday 3 September in Montpellier, marathon from Friday 4 September through the night of 6 to 7 September.  Last year's edition raised more than €16.1 million, the largest sum ever collected in a charity livestream marathon, on 784,599 peak concurrent viewers, over 17 million hours watched and more than 330 channels.  This is the last one.",
                ],
                "numbers": [
                    ("2.14M", "average concurrent viewers on Twitch across August, up 6 percent"),
                    ("4,173,855", "peak concurrent viewers, down 10 percent on July"),
                    ("1.56B", "hours watched, the platform's biggest month of 2026"),
                ],
                "flagnote": "Streams Charts does not include audiences from Chinese livestreaming services, so any global comparison understates events with large Chinese audiences.",
                "so_what": "Peak concurrent viewers prices a moment and average concurrent viewers prices a month, and they are moving in opposite directions on Twitch right now.  A month like this rewards always-on presence across a lot of mid-sized channels and punishes anyone who bought a single tentpole night.  The GTA VI failure is the other half of the same lesson: the biggest live moment of the year was rescued by thousands of small channels while the official feed was down.",
                "do_this": "Shift your Q4 live budget toward a standing presence across many mid-sized channels rather than one big night, and use average concurrent viewers as the number you price against.  If you are producing a live moment, brief a restream policy that lets creators carry your feed, because that is the only redundancy that actually held up in August.",
            },
        ],
    },
    {
        "id": "watch", "name": "ONE TO WATCH", "page": "pg. 06",
        "note": "one creator with momentum, and what to buy from them",
        "tint": None,
        "items": [
            {
                "title": "Gary Eats",
                "hook": "He has already trained his audience to accept money changing hands on camera.  Almost nobody in food has.",
                "open": True,
                "stamps": [("YOUTUBE CHANNEL", "https://www.youtube.com/@GaryEats")],
                "body": [
                    "523,000 subscribers.  152,538,826 total channel views since July 2023.  A British restaurant reviewer publishing every three days, 17 to 20 minutes an episode, going to ordinary places and saying what he thinks.",
                    "The momentum is in the floor, not the ceiling.  Through July and August his uploads sat between 226,815 and 331,906 views.  The last two have cleared it: 447,573 on 29 August and 438,593 on 1 September.  His three-month ceiling is 1,068,141 on the London steakhouse review from 31 July.  When the floor moves up by a third and stays there, that is a channel the recommendation system has re-rated, not a channel that got lucky once.",
                    "Now the part a media buyer should care about, and it is unusual enough to be worth the whole item.  On 13 August he published a video titled £4000 Paid Review — the fee disclosed in the title — and it did 456,623 views, above his baseline rather than below it.  <mark>His audience does not punish him for being paid.  They turn up for it.</mark>",
                    "That is a rare asset in food, where reviewer credibility normally collapses the moment money appears.  He has built the disclosure into the format itself, which means a sponsored appearance is not a compromise his audience has to forgive.  It is the show.",
                    "The rest of his catalogue tells you what he is good at: cheap places treated seriously, expensive places treated sceptically, and a strong instinct for a title.  The world's most expensive restaurant to build.  The UK's cheapest breakfast at £2.  A café that closed, where he gave the owner £1,000.",
                ],
                "watch": {
                    "label": "TOP VIDEO, LAST 3 MONTHS",
                    "title": "London's Worst Steakhouse? REFUNDED THE WHOLE BILL!",
                    "url": "https://www.youtube.com/watch?v=nD1_Wjfy0xc",
                    "meta": "1,068,141 views · published 31 July 2026",
                    "note": "A London steakhouse review that goes badly enough that the restaurant refunds the entire bill on camera.",
                },
                "so_what": "The expensive problem in creator food marketing is that paying a reviewer usually destroys the thing you paid for.  He has already solved that in public, with a fee in a title and a view count above his own average, which means you are buying reach and credibility at the same time rather than trading one for the other.  At 523,000 subscribers with a floor that just moved up by a third, the rate card is lagging the delivery.",
                "do_this": "If you sell hospitality payments or booking software, food delivery, kitchen equipment, supermarket own-brand or UK travel, approach him this week and buy a disclosed paid visit in his existing format rather than a read at the top of someone else's video.  Price it against his last four uploads, not his subscriber count, and ask for a multi-video commitment before the floor resets his rate.",
            },
        ],
    },
    {
        "id": "money", "name": "THE MONEY", "page": "pg. 07",
        "note": "where the spend is going, and what the numbers exclude",
        "tint": None,
        "items": [
            {
                "title": "Livestreaming stopped growing last quarter, and two providers disagree by 10 billion hours about how big it is",
                "hook": "Up 0.1 percent.  Everything that looks like growth is share moving between platforms.",
                "open": True,
                "stamps": [
                    ("NET INFLUENCER · 1 SEP", "https://www.netinfluencer.com/livestreaming-industry-stalls-in-q2-as-youtube-live-extends-its-lead/"),
                    ("NET INFLUENCER · 15 JUL", "https://www.netinfluencer.com/q2-2026-livestreaming-sets-record-31-4b-hours-watched-as-world-cup-lifts-youtube/"),
                ],
                "body": [
                    "The Streamlabs and Stream Hatchet Q2 report landed on Monday.  <mark>Total industry hours watched: 21.5 billion, up 0.1% on Q1 and up 7.6% year on year.</mark>  Quarter on quarter, that is a flat market.",
                    "Underneath it, everything is moving.  YouTube Live took 12.97 billion hours and 60.3% share, up 2.7% on the quarter and 18% year on year.  Kick did 1.34 billion hours, up 36.7% year on year but decelerating.  Twitch was down 0.7% on the quarter and 8.3% on the year.  YouTube Gaming specifically fell 19.3% on the quarter and 18.9% on the year, and Facebook Gaming collapsed to 14.8 million hours, down 64.8% year on year.",
                    "Hold those two YouTube numbers next to each other, because they are the trap.  YouTube Live is up 18% year on year and YouTube Gaming is down 18.9%.  Buying live on YouTube and buying gaming on YouTube are now opposite trades, and a plan that says YouTube live streaming is growing is true and useless.",
                    "Then the number in the report that nobody quotes and that actually prices a sponsorship: viewers per channel.  YouTube Live runs at about 308 viewers per channel.  Twitch runs at about 23, across 7.94 million unique channels.  That is not a quality judgement — it means the two platforms need completely different buying structures.  One is a small number of large rooms.  The other is millions of tiny ones.",
                    "One caveat that should change how you use any of this.  Streams Charts measured the same quarter at 31.4 billion hours watched, because its tracking includes TikTok LIVE, CHZZK, SOOP, BIGO LIVE, Rumble and others that the Streamlabs figure does not.  Two credible providers, one quarter, a gap of nearly 10 billion hours.  Neither is wrong.  They are counting different rooms.",
                ],
                "flagnote": "Streamlabs sells streaming software and Stream Hatchet is owned by Streamlabs' parent, so this report is published by a company with a commercial interest in the health of the category it measures.  Neither provider publishes a full platform list with every release.",
                "so_what": "A flat category means every gain you see in a deck is somebody else's loss, which changes what a growth number is worth in a pitch.  And viewers per channel is the number that decides whether your live money should buy a few big streams or a hundred small ones — 308 against 23 is not a rounding difference, it is two different businesses.",
                "do_this": "When a seller quotes you a livestreaming total or share this week, ask which platforms are inside the number before you write it down, because the honest answer changes the total by nearly half.  Then split your live plan explicitly by platform structure rather than by platform name, and stop treating YouTube Live and YouTube Gaming as one line.",
            },
        ],
    },
    {
        "id": "format", "name": "FORMAT LAB", "page": "pg. 08",
        "note": "how the work is actually being made",
        "tint": None,
        "items": [
            {
                "title": "The Chicago Cubs made a 17-episode vertical rom-com in house and put it on their own TikTok",
                "hook": "No creator, no agency, no distribution deal.  A baseball team standing up scripted drama with its own production unit.",
                "open": True,
                "stamps": [("TUBEFILTER · 1 SEP", "https://www.tubefilter.com/2026/09/01/chicago-cubs-tiktok-rom-com-web-series-nine-innings-to-love/")],
                "body": [
                    "Nine Innings To Love premieres Friday 4 September on the Chicago Cubs' official TikTok account.  Seventeen vertical episodes, set entirely inside a single game at Wrigley Field, following two strangers who meet in the bleachers.  Veronica Garrubbo and Sid Kutikkad star, Adam Sobel directs, and it was made by Cubs Productions, the club's in-house unit, with support from Coyote Sun Productions.",
                    "The premise came from a real constraint of the venue.  The Budweiser Bleachers are general admission, so you do not know who you will end up sitting next to.  Sobel's line is that you never know who might end up beside you.  That is a format built out of an asset the club already owns rather than an idea imported from somewhere else.",
                    "The structural choice worth studying is the episode count against the setting.  Seventeen episodes across nine innings of one game gives the series a finish line the audience understands before episode one — the game ends, and so does the story.  That is a scheduled payoff, and scheduled payoffs are the thing vertical drama is best at and most brand video does not have.",
                    "No budget and no follower numbers were disclosed.  Nothing has aired yet, so there is no performance to judge and anyone telling you this works or does not work is guessing.  What is judgeable today is the production decision: a sports property chose to build scripted entertainment internally instead of renting a creator's audience.",
                ],
                "so_what": "Vertical microdrama is the cheapest scripted form currently available — short episodes, one location, two actors, no coverage requirements — which is exactly why a team's in-house video unit can attempt it without a network.  The serialised structure is what makes it worth doing rather than posting seventeen unrelated clips: each episode has to sell the next one, so the audience compounds instead of resetting.",
                "do_this": "Take one physical constraint of a place your brand already controls — a queue, a shared table, a shift change, a waiting room — and outline a ten-episode vertical series set entirely inside it, with the ending fixed before you write episode one.  Shoot the first three with your in-house team before you brief an agency on anything.",
            },
        ],
    },
]

FORECAST = [
    {
        "confidence": "LIKELY",
        "window": "by 31 December 2026",
        "headline": "Media companies start selling ad inventory on channels they do not own",
        "body": "Vox Media taking the sales, marketing and distribution job on Ina Garten's own YouTube channel is a template, not a one-off.  Publishers have surplus sales capacity and shrinking owned audiences, and individual talent has the opposite problem.  The deal shape — talent keeps the channel, publisher takes the commercial function — solves both without an acquisition.  Expect several more announcements in this exact structure before the year ends, and expect the first rate cards to be soft while nobody has delivery history.",
        "do": "Ask your agency to keep a running list of personality-led channels with a media company handling sales, and buy into first seasons before benchmarks exist.",
    },
    {
        "confidence": "LIKELY",
        "window": "by 31 March 2027",
        "headline": "Sports rights holders start selling adjacency to their own social feeds",
        "body": "The NFL's Pulse Premiere arrangement lets an advertiser pay to sit next to the league's own organic posts.  That converts a cost centre — the social team — into inventory, and it requires no new content.  Every rights holder that sees the NFL do it will ask its platform partners for the same thing, because it is the cheapest new revenue line available to them.  Watch for it appearing in leagues, federations and large clubs first, then in music festivals and awards shows.",
        "do": "If you work with any rights holder, model what their organic feed would be worth as sellable adjacency before their platform partner proposes it.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "by 30 November 2026",
        "headline": "Archive recuts become a standard line in owned video budgets",
        "body": "The Rufus Goodboy jump is the loudest possible demonstration that interpretation beats acquisition, and it arrived the same week Google published its own figure on what a human voice is worth in an ad.  Two independent signals pointing the same way tend to produce budget lines.  The version that spreads will be unglamorous: a writer, an archive, a microphone, and a rule that nothing gets commissioned until the existing footage has been through one pass.",
        "do": "Put a named writer and a recording slot against your existing footage archive in your Q4 budget, as a line item rather than as spare capacity.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "by 28 February 2027",
        "headline": "The IAB creator measurement guidelines slip again, or land as something nobody trades on",
        "body": "The release has already moved from September to October 2026.  Measurement standards that slip once usually slip again, because the disagreement causing the delay does not resolve on a schedule.  And even a document that lands on time is guidance rather than a traded currency — the automated ad market took years to move from published standards to contracts written on them.  Planning on this arriving and being usable inside a quarter is the mistake to avoid.",
        "do": "Write your own creator delivery definitions into Q4 and Q1 contracts now, and treat any IAB document that appears as a check on your language rather than a replacement for it.",
    },
]

TLDR = [
    "A company whose entire business is licensing other people's video clips went from about a million views a month to 150 million by adding one person doing improvised voiceovers over the same library.  Recut your three worst-performing owned videos with nothing changed except a new unscripted voice track, and put a writer on your footage archive before commissioning anything new.",
    "Twitch posted its biggest month of 2026 with average concurrent viewers up 6 percent to 2.14 million while its peak fell 10 percent to 4,173,855, because the month was carried by long marathons rather than single events.  Shift your Q4 live budget to a standing presence across many mid-sized channels and price it on average concurrent viewers.",
    "Livestreaming as a category grew 0.1 percent last quarter, and YouTube Live is up 18 percent year on year while YouTube Gaming is down 18.9 percent.  Split your live plan by platform structure rather than platform name, and ask any seller which platforms sit inside their total before you use it.",
    "The IAB's creator measurement guidelines moved from September to October 2026, which is the standard everyone has been waiting on to fix creator pricing.  Write your own definition of a delivered creator impression into every Q4 contract this week instead of holding a slot for the document.",
    "Brands are moving budget to creators who publicly went through the thing the product addresses, years before the brief existed — one example is a hairdresser with 36,000 followers now taking women's health money.  Search your shortlist's back catalogue for that moment and buy the creators where it predates your category interest.",
    "The NFL renewed TikTok a week before kickoff and is selling advertisers adjacency to its own organic account through Pulse Premiere.  Ask your TikTok rep about that availability before the 9 September opener, and price your own rights holders' organic feeds as sellable inventory this quarter.",
    "Gary Eats published a review with a £4,000 fee disclosed in the title and it beat his own average, on a channel whose floor has just moved from around 300,000 views to 440,000.  If you sell hospitality, food or UK travel, buy a disclosed paid visit inside his existing format and price it against his last four uploads.",
]

SHARE = [
    {
        "who": "JARED · CEO",
        "angle": "Livestreaming grew 0.1 percent last quarter.  Every growth number in your deck is somebody else's decline.",
        "post": "Livestreaming grew 0.1% last quarter. Not 10%. Zero point one.\n\nThat is the Streamlabs and Stream Hatchet Q2 report, out Monday: 21.5 billion hours watched across the industry, up 0.1% on Q1.\n\nEvery growth number you have been shown this year sits inside that. YouTube Live up 18% year on year. Kick up 36.7%. Facebook Gaming down 64.8%. Twitch down 8.3%. Those are not a growing market. They are a fixed amount of attention moving between rooms.\n\nThe number I keep going back to is a smaller one. Viewers per channel. YouTube Live runs at about 308. Twitch runs at about 23, across 7.94 million channels.\n\nSo when someone says put money into live, that sentence has two completely different meanings depending on the platform, and the plans they produce look nothing like each other. One is a handful of large rooms. The other is millions of tiny ones.\n\nThere is a wrinkle I cannot resolve. Streams Charts measured the same quarter at 31.4 billion hours, because it counts platforms the other report does not. Two credible firms, one quarter, a gap of ten billion hours.\n\nI do not think either is being dishonest. I do think it means nobody should quote a livestreaming total without saying which rooms they counted, and most decks do not.",
        "why": "The reader arrives believing live streaming is a growth market and leaves with a flat category, a 10 billion hour measurement gap, and a specific question to ask a seller.",
    },
    {
        "who": "JAMES · CREATIVE DIRECTOR",
        "angle": "What brands are buying from older creators is not craft or wisdom.  It is a timestamp, and no amount of direction produces one.",
        "post": "A hairdresser with 36,000 TikTok followers is taking women's health money. Accounts a hundred times her size are not.\n\nDigiday reported this morning on brands moving budget toward creators who have aged in public alongside their audience. Ellie Fletcher started her account to get clients. In 2025 she started talking about infertility and endometriosis. That is why the brands are there.\n\nI want to be precise about what is being bought, because I do not think it is authenticity, and I have used that word in enough decks to be embarrassed about it.\n\nIt is a date. She was on the record about this before anyone had a brief. That record exists, it is timestamped, and it cannot be produced later by anyone at any budget.\n\nWhich is a strange thing for me to sit with. Everything else in the frame is mine to influence. Casting, lighting, script, tone, pacing, how many takes we do before it stops sounding written. None of that touches the only variable that mattered here.\n\nThe piece also cites a WordPress VIP survey where 60% of US consumers call AI in brand messaging a turnoff. I would treat that number carefully. Survey answers about AI are people telling you who they want to be.\n\nThe timestamp I believe, though. It is the one thing in the whole process that a good director cannot improve.",
        "why": "A creative director naming the one variable his craft cannot touch, and admitting he has used the word authenticity in decks, is a concession almost nobody posts.",
    },
    {
        "who": "LAWRY · LEAD VIDEO EDITOR",
        "angle": "The channel that went from a million views a month to 150 million works because the voiceover deliberately does not sync to the mouth.",
        "post": "A YouTube channel went from about a million views a month to 150 million a month. Same footage library. Same licensing. No new shoots.\n\nOne person started doing voiceovers over the clips.\n\nTubefilter interviewed Will McFadden of Collab yesterday about Rufus Goodboy. Collab's whole business is licensing other people's video, and this channel sat between 500,000 and 1 million views a month for about six years pulling from that library. He took it over in January. In July it did 150 million.\n\nThe craft detail is the part I cannot stop thinking about. He does not lip-sync. He speaks over a closed mouth rather than matching the animal's mouth movements.\n\nEvery instinct I have says sync it. Sync is what makes a thing feel intentional. You spend your life nudging audio two frames so a word lands on a lip. Here the whole effect depends on not doing that, because a synced mouth reads as a puppet and an unsynced one reads as a thought.\n\nHe also improvises the reads. His words: he likes the looseness of improv, the mistakes and the eccentricities that come with riffing.\n\nI have cut a lot of archive material for clients who paid a fortune to own the footage. We treated the library as the asset and the voiceover as the last job before delivery, written in a hurry.\n\nOn the evidence, we had it backwards.",
        "why": "Only someone in an edit suite would name the not-syncing as the mechanism, and the admission that he has treated voiceover as the last job before delivery is the honest part.",
    },
]
