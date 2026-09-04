# -*- coding: utf-8 -*-
"""Content for THE FEED — issue data only.  The render spec lives in build_feed.py."""

ISSUE = {
    "date_iso": "2026-09-04",
    "kicker": "Crux Media // Friday 4 September 2026",
    "tagline": "What brands did on YouTube yesterday, and whether it worked.",
    "pace": "STEADY",
    "next_drop": "Next drop: Monday, 06:30 MT",
}

LEAD = {
    "headline": "YOUTUBE IS GOING TO LABEL YOUR BRAND DEAL WHETHER THE CREATOR DECLARES IT OR NOT",
    "deck": "YouTube rewrote its branded content rules on Wednesday.  The change that matters is that automated systems will start applying a paid-promotion label to videos the creator never declared, on YouTube's own judgement.  Free product now counts as a brand deal.  So does a payment that arrives later.",
    "stamps": [
        ("PPC LAND · 3 SEP", "https://ppc.land/youtube-will-label-brand-deals-that-creators-fail-to-disclose/"),
        ("SOCIAL MEDIA TODAY · 3 SEP", "https://www.socialmediatoday.com/news/youtube-updates-branded-content-sourcing-and-disclosures/829643/"),
    ],
    "body": [
        "Every brand deal on YouTube runs on a checkbox.  The creator ticks it, the video carries a small line saying it includes paid promotion, and everyone gets on with their day.  On Wednesday YouTube announced it is taking that checkbox off the creator's desk.  In its own words, it <mark>may automatically apply the disclosure label on your behalf</mark> when its systems spot branded content that was not declared.  Rolling out over the coming months.",
        "Then there is the definition, which is the part almost nobody has read.  Branded content is now anything <mark>influenced by a brand partner in exchange for something of value</mark> — payment, free products or sponsorships, whether you receive the benefit now or later on.  Read that twice if you run a seeding programme.  The box of product you posted to fifty creators with no contract and no fee is, by this definition, a brand deal.  And the policy applies to the whole video, not just the thirty seconds where your logo is on screen.",
        "There is a genuinely useful piece in here too.  At the point of declaring, creators now get three controls: which countries the video shows in, an overall minimum viewing age, and a minimum age set separately for individual markets.  One upload, a different age gate in every country.  UK rules on advertising food high in fat, salt and sugar came into force in January, and until now a creator facing a rule like that either turned the deal down or took the risk.  Now they can gate it and take the money.",
        "One line in there is aimed straight at buyers.  YouTube says it may substitute an ad that conflicts with the sponsor's own advertising — a video sponsored by Brand A should not be carrying an ad for Brand B.  If any part of your plan involved buying ads against a competitor's sponsored videos, that inventory just stopped being reliable.  Declaring paid promotion also pulls a video out of the YouTube Kids app entirely.",
        "Scale: roughly 3 million channels sit inside the YouTube Partner Programme.  ASA research cited by IAB UK in May found only about 57% of influencer advertising met disclosure requirements, which means four in ten sponsored posts did not.  That gap is the whole reason the automation exists.  What YouTube has not published is what triggers detection, what the error rate is, or whether any of this looks backwards at videos already uploaded.",
        "There is an override.  Creators <mark>may have the option to certify that your video does not contain branded content</mark> and remove a label applied in error.  May.  That word is doing an enormous amount of work in a policy document, and nobody has yet said who fixes it, or how fast, when a genuine unpaid review gets flagged as an ad.",
    ],
    "numbers": [
        ("3M", "channels in the Partner Programme this now covers"),
        ("57%", "of influencer ads met UK disclosure rules — ASA research, May"),
        ("1", "upload can now carry a different age gate in every market"),
    ],
    "so_what": "The disclosure decision has moved from your creator to YouTube's classifier.  That changes who carries the risk on every deal you have running right now, because a label applied by machine is a label you did not brief, approve or time.  And the widened definition quietly drags gifting and product seeding into the same rules as paid campaigns.",
    "do_this": "Pull your live creator contracts today and add one clause: who fixes it, and inside what window, if YouTube applies a disclosure label the creator did not.  Then tell whoever runs your seeding to declare every gifted video from Monday, contract or no contract.",
}

SECTIONS = [
    {
        "id": "ws", "name": "W'S", "page": "pg. 02",
        "note": "what worked, and the exact reason it worked",
        "tint": "blue",
        "items": [
            {
                "title": "Set spent its promotion budget on people who had already bought, and did $3.5 million in a day",
                "hook": "Fifteen customers.  No creators.  The biggest drop in the brand's eight-year history.",
                "open": True,
                "stamps": [("GLOSSY · 4 SEP", "https://www.glossy.co/pop/set-customer-influencer-strategy-coastline-drop/")],
                "body": [
                    "On 14 August the activewear brand Set took over the Clam Bar in Amagansett to launch a collection called Coastline.  It did not fill the room with creators.  It opened the doors to its own customers and to whoever happened to be walking past.  The following day Coastline did <mark>$3.5 million online in 24 hours</mark>, which Set says is the highest-grossing limited-edition drop in its eight years of trading.",
                    "The amplification came from around 15 people the brand calls Set Insiders.  They are not creators.  They are existing customers picked out for buying often and engaging constantly with the brand's posts, and the whole programme started this year with exactly two of them.  Founder Lindsey Carter's brief was, in her words, to act like insiders and detectives, and Set would send free product.",
                    "The clever part is how they were briefed.  Rather than one asset pack going to fifteen people, each Insider got different products, different previews and a different piece of information — so no two posts said the same thing, and the reveal arrived in fifteen pieces instead of one.",
                    "The numbers on the day: 41% of the people who preordered at the event were new to Set.  A five-hour queue formed outside the New York flagship the next morning, 51% of shoppers in the store were first-timers, and the drop pulled 13% more new customers than the previous collection launch.  Carter's line is that fewer followers means more attainable, which means higher conversion.",
                    "One Insider's ordinary TikToks get around 300 views.  Her Set Insider posts get thousands.  She is not a bigger creator than she was a month ago.  She is a customer holding something nobody else has.",
                ],
                "numbers": [
                    ("$3.5M", "online in 24 hours — Set's biggest limited drop in eight years"),
                    ("41%", "of preorders at the event came from new customers"),
                    ("17%", "of consumers check follower count before engaging — Sprout Social, 2026"),
                ],
                "flagnote": "Set supplied every sales and new-customer figure here itself, and released no social reach or engagement data for the launch.",
                "so_what": "Reach is not what moved this.  Fifteen people with small audiences and a real relationship to the product beat the version of this campaign where you buy fifteen creators with big ones.  A 2026 Sprout Social study found only 17% of consumers even look at follower count before deciding whether to engage — so the number you are buying on is a number your audience mostly ignores.",
                "do_this": "Pull your top 20 customers by purchase frequency and engagement, send each one a different piece of your next launch a week early, and give each of them a different thing to reveal.  Enrol them in an affiliate tool so you can read the sales, not just the posts.",
            },
            {
                "title": "Poppi is putting a third of its back-to-school money into sorority houses.  Lucky Charms got filmed for the price of balloons",
                "hook": "Two brands, the same fortnight of the year, opposite economics.",
                "stamps": [("MARKETING BREW · 4 SEP", "https://www.marketingbrew.com/stories/sorority-rush-brand-sponsorships-poppi-lucky-charms-strategy")],
                "body": [
                    "American sorority recruitment week — RushTok — is now a media buy.  Poppi has been in it for years and this season plans to send more than a million cans to sororities plus 20,000 pieces of custom merchandise, alongside appearances from Love Island USA and Traitors cast members.  Poppi's VP of culture Sophia Sesto told Marketing Brew those efforts together can account for <mark>between 30% and 40% of the brand's entire back-to-school marketing budget</mark>.",
                    "That is an enormous bet on a two-week window, and it is a sampling bet rather than a media one.  Poppi built a dedicated college team three years ago because chapters were already writing in asking for product.",
                    "Lucky Charms went the other way entirely.  General Mills noticed the brand was already appearing organically in Kappa Delta chapters, because the sorority uses a shamrock.  So it hired a decor company called Presley Paige, made balloon art at the University of Arkansas chapter, and put bracelet-making stations on Bid Day.",
                    "Business unit director Megan Brooks told Marketing Brew there were no official creator partnerships with the chapter members — which, as she put it, made it more important that the thing was captivating on its own.  It was.  The chapter filmed it.  So did passers-by who stopped to look at the houses, which Brooks says she had not planned for at all.",
                ],
                "so_what": "Poppi bought volume and Lucky Charms bought a set.  Both got filmed.  Only one of them paid for the filming.  When your audience is already pointing cameras at a specific place on a specific date, the cheapest creative brief you will ever write is to build something in that place worth pointing a camera at.",
                "do_this": "Find the one date in your category where your customers already film — a race, a move-in week, an opening night — and put the money into the physical thing that will be in frame rather than into the people holding the phones.",
            },
        ],
    },
    {
        "id": "ls", "name": "L'S", "page": "pg. 03",
        "note": "what broke, and the failure mode behind it",
        "tint": "pink",
        "items": [
            {
                "title": "Wrong owner: nobody senior watched the ad, and this week it cost the chief executive and the president their jobs",
                "hook": "The CEO says he had not seen it before it ran.  That is the entire story.",
                "stamps": [
                    ("FRONT OFFICE SPORTS · 2 SEP", "https://frontofficesports.com/article/good-good-golf-ceo-steps-down-amid-callaway-driver-ad-fallout/"),
                    ("BUSINESS INSIDER · 2 SEP", "https://www.businessinsider.com/good-good-ceo-president-out-ad-memo-2026-9"),
                ],
                "body": [
                    "Quick recap for anyone who missed the first act.  Good Good Golf, a golf creator company that raised $45 million last year, made a co-branded driver ad with Callaway in which co-founder Garrett Clark shoves fellow member Alexis Miestowski to the ground.  It went out.  It did not survive contact with an audience.",
                    "This week the bill landed.  Staff were told on Wednesday that chief executive Matt Kendrick and president Joe Flannery have both resigned.  Callaway terminated the partnership.  Good Good walked away from title sponsorship of its own PGA Tour event.  Golf Channel cancelled a show built with them days before it was due to premiere.  Merchandise came off the shelves at Golf Galaxy, Dick's, PGA Tour Superstore and Target.",
                    "The VP of brand and marketing was fired along with another employee, and Callaway's director of content and production is out.  Callaway chief Chip Brewer said the company's content review process <mark>was not comprehensive enough</mark>.  Kendrick said he had not seen the ad before it ran.",
                    "Early investor Nahid Giga is interim chief executive.  Clark, the man in the ad, keeps his job and keeps making content.  Which tells you precisely where the value in a creator company sits, and it is not in the management layer.",
                ],
                "so_what": "This did not fail in the edit.  It failed in the twenty minutes nobody spent watching a finished cut alongside a person with the authority to say no.  Two brands, a broadcaster, a tour event and four retail accounts came apart because a review step that costs nothing was never put in a diary.",
                "do_this": "Name one person on each side of every co-branded project as the final viewer, put them in the calendar with the delivery date, and do not let a master file leave the building until both have watched it end to end.",
            },
            {
                "title": "Wrong owner: the ad was killed because the person who approved it was not who they said they were",
                "hook": "Everyone is reading this as an AI backlash.  It is a paperwork failure.",
                "stamps": [("VARIETY · 3 SEP", "https://variety.com/2026/digital/news/suno-kills-mary-j-blige-ad-endorse-ai-platform-1236850584/")],
                "body": [
                    "AI music company Suno has pulled an 85-second video ad in which Mary J. Blige appears in a studio while a producer builds a track called Pretty Flowers in seconds.  She seems to say the process is amazing and dope, though Variety is careful to note that the way the video is edited makes it unclear what exactly she is responding to.",
                    "Blige had not approved it.  Suno's statement to Variety says the company <mark>entered into a business deal with someone who presented themselves as Ms. Blige's official representative</mark>, and terminated the campaign as soon as it learned that was not the case and that she was uncomfortable.",
                    "Before that happened she took a wave of online abuse from people who assumed she had endorsed an AI music tool.  A representative for Blige had no further comment.  The clip circulated widely but appears to have been officially posted only on Suno's Facebook page, and a shorter, more heavily cut version is also going around with no clear origin.",
                    "Context on how much room Suno had for this: it is in ongoing litigation with Universal and Sony, was sued this week by Jason Isbell and others, and lost a German court ruling last month.  It has licensing deals with Warner and BMG.  A clearance error is the last thing that company needed.",
                ],
                "so_what": "The AI is why everyone is talking about it, but the AI is not the thing that broke.  A campaign got written, shot, cut, approved and posted on the say-so of somebody who did not have the authority to say it.  At no point did anyone in that chain ring the artist's known representation to check.",
                "do_this": "Before your next talent shoot, verify the representative independently — call the agency's published main line rather than the number in the email thread — and store the signed release from that verified contact in the same folder as the master.",
            },
        ],
    },
    {
        "id": "moves", "name": "MOVES", "page": "pg. 04",
        "note": "deals, hires, launches and rule changes worth knowing about",
        "tint": None,
        "items": [
            {
                "title": "Dude Perfect's first chief executive is out after two years, and the board could not agree what the company is",
                "hook": "$100 million raised, and a disagreement about the next phase.",
                "stamps": [("BUSINESS INSIDER · 3 SEP", "https://www.businessinsider.com/youtube-group-dude-perfect-ceo-andrew-yaffe-out-2026-9")],
                "body": [
                    "Andrew Yaffe, hired in October 2024 as Dude Perfect's first chief executive, has left.  The joint statement says that as the social media landscape continues to evolve, they developed different perspectives on the company's next phase and the best path forward.",
                    "Dude Perfect had raised $100 million before he arrived.  During his run the group grew revenue and landed State Farm, Disney, BODYARMOR and McDonald's, launched the 2026 Squad Games tour, the Almost Athletes podcast and Dude Perfect Outdoors, and quietly retreated from its original theme-park ambition toward smaller live formats.  Longtime investor and advisor Patrick Hurley is interim chief executive.",
                ],
                "so_what": "Two of the biggest creator companies in America lost their chief executives inside one week, and in both cases the creators stayed.  Outside management keeps getting hired to professionalise a creator business, then discovers the asset does not report to it.",
                "do_this": "When you contract with a creator company rather than a creator, name the individual creators in the deliverables schedule so a change of management does not change what you bought.",
            },
            {
                "title": "PepsiCo moved its global media out of Omnicom, and the knock-on pulled Publicis out of the Coca-Cola pitch",
                "hook": "One account moving takes a competitor off the table for another.",
                "stamps": [("MARKETING DIVE · 3 SEP", "https://www.marketingdive.com/news/pepsico-hands-global-media-to-publicis-amid-transformation-at-cpg-giant/829556/")],
                "body": [
                    "PepsiCo has confirmed it is moving global media from Omnicom to Publicis, which will build a single global media operating model covering strategy, planning, buying, data and technology across markets.",
                    "The consequence, per Adweek's sourcing, is that Publicis withdraws from the pitch for Coca-Cola's global media business — having already taken Coke's North American media and data off WPP last year.  You cannot hold both.",
                    "The number that matters for anyone selling video: PepsiCo posted Q2 net revenue of $24.2 billion, up 6.4% year on year, and executives have said North American marketing and advertising costs will rise in the second half of 2026 as the company plays offence.  Publicis grew Q2 net revenue 4.8% organically.  Omnicom is still mid-integration after buying IPG last autumn.",
                ],
                "so_what": "A rise in a company that size's marketing spend in the back half of the year is real money entering the market between now and Christmas, and it lands during an agency transition when a new shop is looking for early wins to justify the switch.",
                "do_this": "If you sell production or creator work into large packaged-goods brands, get your capability deck in front of the incoming Publicis team on PepsiCo in the next fortnight, while the roster is still being built.",
            },
            {
                "title": "Google will not have to sell its ad exchange, and the fix is a set of behaviour rules instead",
                "hook": "A monopoly finding in April, and no breakup in September.",
                "stamps": [("ADEXCHANGER · 2 SEP", "https://www.adexchanger.com/antitrust/google-wont-have-to-break-up-its-ad-tech-business-judge-brinkema-rules/")],
                "body": [
                    "US District Judge Leonie Brinkema has rejected the Department of Justice's proposed remedy that Google divest AdX, its ad exchange, and possibly DFP, its publisher ad server.  This is the same judge who ruled in April that Google held a monopoly.  She has adopted behavioural remedies instead.",
                    "The fixes likely to land include making real-time AdX bid amounts available to rival ad servers, dropping the pricing rules that stop publishers setting different price floors for different bidders, and giving up first-look and last-look bidding privileges.  Her reasoning was that a forced sale could damage the small publishers who use DFP for free, that a buyer brings its own complications, and that behaviour rules avoid years of appeals.",
                    "Not everyone is convinced.  Jay Friedman, who gave evidence at trial, asked the obvious question: what is a publisher supposed to do if it wants a different ad server but still wants Google's buy-side demand.",
                ],
                "so_what": "The plumbing under most digital ad buying stays owned by the same company, which means the pricing structure you plan against next year looks like this year's.  The one live change worth tracking is publishers getting the ability to set different floors for different buyers, which will move what some inventory costs.",
                "do_this": "Ask your media buyer, in writing, which of these behaviour remedies will change your effective cost to reach a thousand people in 2027, and get the answer as a number rather than a paragraph.",
            },
            {
                "title": "TikTok put voice notes, polls and photo carousels inside the comment section",
                "hook": "Your sponsored post's comments just became a place where a 60-second audio file can sit.",
                "stamps": [("SOCIAL MEDIA TODAY · 3 SEP", "https://www.socialmediatoday.com/news/tiktok-adds-voice-notes-and-image-carousels-in-comments/829640/")],
                "body": [
                    "Three new comment formats.  Voice Comments let users record up to 60 seconds, displayed as an audio file with auto-translated text underneath, rolling out globally over the next month to users aged 18 and over.  Comment Polls are creator-only, up to five options, with results tracked live in the comments and available now.  Photo comments allow up to nine images in a scrollable carousel, plus replies using Live Photos.",
                    "Read it as TikTok defending time spent in the app by making the comment layer somewhere you stay rather than somewhere you glance.",
                ],
                "so_what": "Every one of those is a new surface underneath your paid creator post, and two of them carry content your existing moderation tools cannot read.  A 60-second voice note under a brand video is not something a keyword filter catches.",
                "do_this": "Ask whoever moderates your sponsored posts whether their tool can flag audio and image comments, and if it cannot, add a human check on the first 48 hours of every paid creator post.",
            },
        ],
    },
    {
        "id": "onstream", "name": "ON STREAM", "page": "pg. 05",
        "note": "live audiences, and what the numbers actually measure",
        "tint": None,
        "items": [
            {
                "title": "Kick had its biggest month ever, and the number that proves it is not the one in the headline",
                "hook": "669 million hours is the vanity figure.  900,000 average viewers is the real one.",
                "open": True,
                "stamps": [("STREAMS CHARTS · 2 SEP", "https://streamscharts.com/news/kick-august-2026-recap")],
                "body": [
                    "Kick recorded 669.14 million hours watched in August, up 13% on July, with a peak of 2.36 million viewers, up 29%.  Hours watched is the figure that gets quoted in every press release and it is the one to distrust, because it climbs whenever an event simply runs longer or more channels get counted.",
                    "The honest number sits underneath.  <mark>Kick crossed 900,000 average concurrent viewers for the first time</mark>, a platform record.  Average concurrents cannot be inflated by scheduling.  They tell you the audience got deeper rather than just busier.",
                    "For a sense of scale, 2.36 million people watching the same platform at the same moment is roughly 26 full Wembley Stadiums.  Twitch did 1.56 billion hours in the same month, which puts Kick at around 43% of Twitch's watch time — no longer a rounding error.",
                    "Nine of the top ten genres grew.  Action led with 263.87 million hours, up 26%.  Simulator and Mobile both grew more than 40% on the back of Escape From Tarkov, BGMI and EA Sports FC 26.  In-real-life was the only decliner in the top ten, down 2%, and it was also the only genre averaging more than 2,000 live channels at once — a great many small rooms rather than a few enormous ones.",
                    "Most-watched creator was Nurideen Shabazz, up 43% on hours watched, off a 24-hour-a-day marathon stream with boxer Adrien Broner.",
                ],
                "so_what": "Kick is now big enough to plan against and still cheap enough to be early on.  But the reading lesson matters more than the platform: hours watched can be manufactured by making an event longer, and average concurrents cannot.  One of those numbers tells you how many people are actually there.",
                "do_this": "The next time a platform or an event sends you an hours-watched figure, reply asking for peak and average concurrents before you price anything against it, and treat a refusal as an answer.",
            },
            {
                "title": "Pokemon's world final broke 200,000 viewers for the first time, and the extra audience arrived on other people's channels",
                "hook": "Same tournament, same game.  A hundred more broadcasters.",
                "stamps": [("ESPORTS CHARTS · 3 SEP", "https://escharts.com/news/2026-pokemon-world-championships-viewership")],
                "body": [
                    "All four Pokemon World Championships titles set record peaks at the San Francisco event over 28 to 31 August.  The video game championship was the biggest at 215,600 peak viewers, hit during an all-Japanese final — the first Pokemon Worlds tournament in the series to pass 200,000.  The trading card, UNITE and GO events all cleared 150,000, the only other tournaments in the series ever to do so.",
                    "The driver is stated plainly by Esports Charts and it is not the games.  Almost all four events drew more than 100 unique broadcasting channels this year.  Last year only the UNITE championship got past 50 co-streamers.  Named co-casters include knekro, fuslie and kkatamina, though the official channels still took the bulk of the viewership.",
                    "Three of the four events landed in the all-time Pokemon top three for watch time.  Twitch was the dominant platform globally.  Next year's event goes to Singapore.",
                ],
                "so_what": "The audience did not grow because the event got better.  It grew because a hundred more people were allowed to rebroadcast it with their own commentary, each bringing their own room with them.  Co-streaming is a distribution decision made in the rights contract, months before any marketing happens.",
                "do_this": "In your next event or sponsorship contract, write in explicit co-streaming permissions and attach a named list of channels you will actively invite, and do it before the rights are signed rather than after.",
            },
            {
                "title": "A league lost 38% of its watch time on identical airtime, and the reason was one country",
                "hook": "Same number of hours broadcast.  A third of the audience gone.",
                "stamps": [("ESPORTS CHARTS · 4 SEP", "https://escharts.com/news/lcp-2026-viewership")],
                "body": [
                    "The League of Legends Championship Pacific closed its 2026 season on 30 August with total watch time down 38.2% year on year on near-identical airtime.  That last clause is what makes it real: this is audience loss, not a scheduling artefact.  Average viewership fell 37.6% even though more unique channels were broadcasting the matches.",
                    "The peak collapsed harder.  The season's highest concurrent audience fell 64.1%, from 483,444 to 173,607.  The grand final drew 152,696, which was 478 viewers short of being the biggest moment of the whole tournament — a final nobody stayed up for.",
                    "Esports Charts puts part of it down to GAM Esports missing the final, which cost the league its largest language audience, Vietnamese.",
                ],
                "so_what": "One team failing to reach a final removed roughly a third of a league's audience, because that team carried an entire language with it.  Any sponsorship priced off last season's league average was in fact priced off a roster, and rosters change every year.",
                "do_this": "Before you sign a league sponsorship, ask which teams carry which language audiences, and ask what your guaranteed numbers become if any one of them misses the playoffs.",
            },
        ],
    },
    {
        "id": "watch", "name": "ONE TO WATCH", "page": "pg. 06",
        "note": "one creator with momentum, and who should be buying them",
        "tint": None,
        "items": [
            {
                "title": "TA Outdoors",
                "hook": "A bushcraft channel started building a camper in June and its views went up tenfold.",
                "open": True,
                "stamps": [("YOUTUBE", "https://www.youtube.com/@TAOutdoors")],
                "body": [
                    "TA Outdoors is a British outdoors channel sitting at about 2.49 million subscribers.  For years it made bushcraft shelters, survival kit tests and woodland builds, running comfortably in the 40,000 to 80,000 view range per upload.  Solid, consistent, unremarkable.",
                    "In June it started a Stealth Camper build series, and because both formats now run side by side in the same feed the comparison is unusually clean.  The camper episodes did 718,591 views on 2 June, 925,744 on 16 June and 681,189 on 24 August.  The standard uploads across the same stretch did 42,172, 64,508, 67,631, 70,299, 72,306, 77,910 and 73,388.",
                    "That is a four to tenfold uplift per video on the same channel, with the same presenter, filmed in the same months, in the same shed.  The only variable is the format: a serialised build with an outcome, instead of a standalone film with a lesson.",
                    "And the biggest episode in the run is the first overnight — the payoff, where the thing he spent weeks building gets tested by weather that did not read the schedule.  That is where the story resolves, and that is where the audience turns up.",
                ],
                "watch": {
                    "label": "TOP VIDEO, LAST 3 MONTHS",
                    "title": "First Overnight in the Stealth Camper: Thunderstorms and Rain!",
                    "url": "https://www.youtube.com/watch?v=dC3k38gOF6s",
                    "meta": "925,744 views · published 16 June 2026",
                    "note": "He spends the first night in the camper he built, and thunderstorms and heavy rain arrive to test it.",
                },
                "so_what": "The obvious buyers are portable power stations — EcoFlow, Jackery, Bluetti — plus cordless tools, insulation, towing and 12-volt electrics, and sleep systems.  What you are buying is not a read at the top of one video.  It is the power and the tooling that a four to six episode build physically runs on, which puts your product in the spine of the series rather than in a break in it.",
                "do_this": "If you sell anything a build depends on, stop pricing single integrations and price the whole series instead — supply the kit for the next multi-part build and make certain your product is visible in the payoff episode, not only the assembly ones.",
            },
        ],
    },
    {
        "id": "money", "name": "THE MONEY", "page": "pg. 07",
        "note": "what things cost, and where the money is actually going",
        "tint": None,
        "items": [
            {
                "title": "Brands are buying creator rights in perpetuity for footage they will bin in three months",
                "hook": "Usage adds cost almost every single time, and nobody can tell you what it should cost.",
                "open": True,
                "stamps": [("DIGIDAY · 4 SEP", "https://digiday.com/media/marketers-say-usage-rights-are-driving-up-the-price-to-work-with-creators/")],
                "body": [
                    "There is no rate card for creator usage rights.  That is the finding.  Digiday went round the agencies and platforms and could not produce a single benchmark, because one does not exist — some creators price usage by the day, some fold it into the fee, some never price it at all.",
                    "Iluka Enright at Movers+Shakers says usage and exclusivity are an additional cost almost 100% of the time.  Danielle Wiley, who runs the creator network Sway, says there is no consistency in how the pricing is even presented; her own standard ask is the post plus 30 days paid usage, two months organic and 30 days exclusivity.  Roz Sedaghat at Pearpop blames shorthand — rights get described as organic or paid and the critical details never get written down.",
                    "The expensive habit is perpetuity.  Aundrea Leckie at Open Influence says brands increasingly demand rights forever with no intention of ever using the footage that long.  They are buying their way out of a future renegotiation, and paying for decades of a file they will delete.",
                    "Tim Sovay at CreatorIQ makes the point that kills it: <mark>brands are rewarded by replacing, feeding, and replacing their advertising assets month over month</mark>.  You need fresh creative this month to beat last month.  Which means a five-year licence on one piece of footage is worth close to nothing to you and costs a great deal.",
                    "The workaround already in market is non-concurrent usage.  Leckie got six months non-concurrent for a seasonal travel brand: lock the footage in February, use it again in December, and pay for none of the months in between.",
                ],
                "so_what": "You are paying a premium to avoid an awkward phone call in eighteen months' time.  Creative decays faster than the licence you bought, so the back half of every long usage window is money spent on an asset that will already have been replaced by something newer.",
                "do_this": "Rewrite your standard creator terms this week to buy non-concurrent usage in named windows plus a pre-agreed extension rate, and stop asking for perpetuity unless you can name the campaign that will still be running in year three.",
            },
            {
                "title": "Roblox paid creators $1.5 billion last year, and two-thirds of the American money went to places with no tech industry",
                "hook": "Up 63% in a year, and geographically nothing like where you think.",
                "stamps": [("TUBEFILTER · 3 SEP", "https://www.tubefilter.com/2026/09/03/roblox-creator-earnings-2025-usa-gdp-game-item-sales/")],
                "body": [
                    "Roblox creators earned more than $1.5 billion from game and item sales in 2025, up from $923 million in 2024 — a 63% jump in twelve months.  Around $673 million of that went to creators in the United States.",
                    "The distribution is the interesting bit.  66% of the American payments, roughly $444 million, went to people living in areas with below-average concentrations of tech workers.  Roblox puts the US economic impact at $752 million, up 69%, equivalent to 7,525 full-time American jobs and nearly 12,000 globally.  Cumulative US impact since 2017 is $2.37 billion.",
                ],
                "flagnote": "Roblox published these figures itself in its own Economic Impact Reports.  It is also currently being sued by close to a dozen US states over child safety on the platform, which Tubefilter details at length.",
                "so_what": "A billion and a half dollars of creator income is now being generated inside a game engine rather than on a video platform, and most of the American share of it is being earned a long way from any city you would open an office in.  If your brand thinks of Roblox as a marketing channel, the people building on it think of it as a job.",
                "do_this": "If you are commissioning anything in Roblox, brief and pay the independent studios who already live there rather than routing it through a games agency, and ask for their existing experience's concurrent player numbers before you commit.",
            },
        ],
    },
    {
        "id": "format", "name": "FORMAT LAB", "page": "pg. 08",
        "note": "how the thing was actually made, and what to steal",
        "tint": None,
        "items": [
            {
                "title": "Agencies are rewriting creator briefs so a chatbot will quote the video later, and Shorts are losing badly",
                "hook": "Models do not watch video.  They read your transcript.",
                "open": True,
                "stamps": [
                    ("DIGIDAY · 4 SEP", "https://digiday.com/marketing/future-of-marketing-brands-want-creators-who-can-win-over-humans-and-machines-at-once/"),
                    ("OTTERLY.AI STUDY · 5 MAR", "https://www.veed.io/learn/otterly-ai-citation-research-2026"),
                ],
                "body": [
                    "Digiday reported on Friday that creator briefs are being rewritten around whether an AI assistant will cite the video later.  At Tinuiti, AI visibility went from about a tenth of the factors it weighs in creator strategy six to eight months ago to about a quarter now, and the subject touches roughly 60% of its client list.  At Jellyfish, more than 90% of marketer clients now rank AI's effect on discovery in their top three concerns.",
                    "The format split is the useful part.  Lauren Lyster at Go Fish Digital says long-form is getting cited and Shorts largely are not.  The mechanism is boring and completely decisive: <mark>a language model never watches anything</mark>.  It reads the transcript, the description and the chapter list.  A fifteen-minute video hands it thousands of words of quotable text at a stable address.  A thirty-second Short hands it almost nothing.",
                    "A March study by Otterly.AI, looking at more than 100 million citation instances over 30 days across ChatGPT, Google AI Overviews, Perplexity, Copilot and Gemini, put numbers on it: 94% of YouTube citations went to long-form and 5.7% to Shorts.  It also found that 40.83% of cited videos had fewer than 1,000 views, and only 31% had any chapter structure at all.",
                    "The agency Dept has already changed what it asks creators to deliver: a reference list of exact product names and verifiable claims, chapter markers built around the questions people actually ask rather than round timestamps, and a clean human-checked transcript instead of auto-captions.",
                    "Rate cards have not moved.  Executives quoted by Digiday expect that in six to twelve months, which is roughly the window you have to buy this before it gets priced in.",
                ],
                "flagnote": "The Otterly.AI study is from March 2026 and Otterly.AI sells AI search monitoring software.  Read the long-form to Shorts ratio as directional rather than exact.",
                "so_what": "A creator video used to stop working the day the campaign ended.  If it gets cited, it carries on answering the question for as long as the model keeps the reference — and everything that decides whether it does sits in the export folder rather than in the cut.  Follower count barely correlates, which is why a specialist with 100,000 subscribers can beat a generalist with five million.",
                "do_this": "Add three lines to your next creator brief: deliver a human-checked transcript rather than auto-captions, set chapter markers on the actual questions viewers ask, and list exact product names and specifications in the description.",
            },
        ],
    },
]

FORECAST = [
    {
        "confidence": "LIKELY",
        "window": "by 31 October 2026",
        "headline": "Creator contracts grow a mislabel clause",
        "body": "YouTube's automated disclosure detection arrives over the coming months with no published error rate and no stated policy on old uploads.  The first genuinely unpaid review video from a large creator to get flagged as an ad will be a news story within a day.  The second thing that happens is that agency contract templates grow a clause covering who fixes a wrong label and inside what window, because talent lawyers move considerably faster than platforms do.",
        "do": "Draft that clause yourself now and put it into your next three creator contracts, before someone else's version becomes the market standard.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "by 30 November 2026",
        "headline": "The IAB's influencer measurement guidelines slip again, or land without a price benchmark",
        "body": "They were due this month and are now slated for October according to an IAB spokesperson.  The hard part is that a measurement standard requires the platforms to agree on what a view is, and they do not.  The likeliest outcome is something that standardises definitions without standardising rates, which leaves the pricing problem precisely where it is today.",
        "do": "Build your own record instead of waiting: log every creator quote, counter-offer and final fee across every team that touches a creator budget, and make it one shared file.",
    },
    {
        "confidence": "LIKELY",
        "window": "by 31 March 2027",
        "headline": "Non-concurrent usage windows become a normal line on a creator rate card",
        "body": "The perpetuity habit is expensive and everyone quoted this week knows it.  Non-concurrent windows solve it in both directions — the creator sells the same footage twice, the brand pays only for the months it uses.  Once two or three of the big creator networks publish it as a standard term the rest will follow, because it is far easier to sell than a discount.",
        "do": "Ask for a non-concurrent quote alongside your normal one on your next deal, and find out what the actual difference is before it becomes the default.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "by 31 December 2026",
        "headline": "Another large creator company swaps a hired executive back for a founder",
        "body": "Inside one week, Dude Perfect's first chief executive left over a disagreement about the company's next phase, and Good Good's chief executive and president resigned after an ad nobody senior watched.  In both cases the creators stayed and the management left.  The pattern is that outside leadership gets hired to professionalise a creator business and then discovers the asset does not report to it.",
        "do": "Audit which of your creator partners are contracted through a company rather than as individuals, and add the individuals by name to the deliverables schedule.",
    },
    {
        "confidence": "LONG SHOT",
        "window": "by 30 September 2027",
        "headline": "An agency publishes a price premium for creator video that gets cited by AI assistants",
        "body": "Nobody charges for this today, and every executive quoted this week expects rate cards to move within six to twelve months.  The blocker is attribution: you can count citations but you cannot yet trace a sale back to one.  Somebody will publish a premium anyway, because the commercial incentive to be first with a number in a market that has none is enormous.",
        "do": "Start logging which of your existing creator videos get cited in ChatGPT and Google AI Overviews now, so you own a baseline before anyone tries to charge you for one.",
    },
]

TLDR = [
    "YouTube will start automatically labelling undeclared brand deals over the coming months, and free product now counts as a brand deal.  Add a clause to your live creator contracts covering who fixes a wrongly applied label and how quickly.",
    "Set did $3.5 million online in 24 hours off around 15 existing customers rather than creators, with 41% of preorders at the event coming from new buyers.  Pick your 20 most engaged customers and give each of them a different piece of your next launch to reveal.",
    "Usage rights add cost on almost every creator deal and no benchmark exists, so brands are buying perpetuity for footage they will replace within a quarter.  Switch your standard terms to non-concurrent windows with a pre-agreed extension rate.",
    "Long-form creator video is getting cited by AI assistants and Shorts largely are not, and rate cards have not caught up yet.  Brief a human-checked transcript, real chapter markers and exact product names on your next creator video.",
    "Good Good Golf's chief executive and president both resigned this week over an ad the chief executive says he never watched before it ran.  Name one final viewer on each side of every co-branded project and put them in the calendar with the delivery date.",
    "Kick crossed 900,000 average concurrent viewers for the first time in August, on a 2.36 million peak.  Ask every platform and event for peak and average concurrents before you price anything against an hours-watched figure.",
    "Poppi is putting 30 to 40% of its back-to-school budget into sorority recruitment while Lucky Charms got filmed for the price of balloon art.  Find the date your customers already film on, and spend the money on the thing that will be in frame.",
]

SHARE = [
    {
        "who": "JARED · CEO",
        "angle": "The people with the smallest audiences brought in the most new customers, and the metric the whole market prices on is one shoppers barely check.",
        "post": "An activewear brand called Set did $3.5 million online in 24 hours last month. The amplification came from about fifteen people. None of them were creators.\n\nThey were customers. Set calls them Insiders, and picked them for buying often and engaging constantly. The programme started this year with two people.\n\nFigures from Glossy: 41% of the people who preordered at the launch event were new to the brand. A five-hour queue formed outside the New York store the following morning, and 51% of the shoppers in it were first-timers.\n\nThe part I keep returning to is a 2026 Sprout Social study quoted in the same piece. Only 17% of consumers check follower count before deciding whether to engage with a creator's post.\n\nSeventeen percent. That is the number the entire influencer market is priced on, and five in six people never look at it.\n\nI don't think this kills creator marketing. Set's founder is clear that it worked because these people were already customers, and you cannot manufacture that on a deadline.\n\nBut it does suggest the thing you buy when you buy reach is not the thing that converts. Those are two separate purchases, and most of us have been writing one cheque for both.",
        "why": "The number is large enough to open a conversation with a sceptical client, and the 17% is the part that changes what they think reach is worth buying.",
    },
    {
        "who": "JAMES · CREATIVE DIRECTOR",
        "angle": "Everyone is reading the Suno advert as an AI story.  It is a clearance story, and the craft was never the variable.",
        "post": "Suno pulled an 85-second ad this week featuring Mary J. Blige. Everyone is reading it as an AI backlash story. It's a clearance story.\n\nBlige never approved it. Suno told Variety it entered into a business deal with someone who presented themselves as her official representative, and killed the campaign once it learned that wasn't the case.\n\nSo: a script, a studio day, a shoot, an edit, a grade, a posting schedule. All of it downstream of one unverified email address.\n\nThe uncomfortable part for people who do my job is that the craft wasn't the problem. Variety notes the edit makes it unclear what Blige is actually responding to when she calls the process amazing. That ambiguity is an ordinary edit decision. You cut around the pauses, you tighten the reaction, you make it play.\n\nIn a properly cleared ad nobody would look at it twice. In an uncleared one, it's the thing that made her appear to endorse something she hadn't, and she took a wave of abuse for it before anyone stepped in.\n\nI don't have a clean lesson about AI here. What I keep thinking about is that everyone in that chain did their job well, and it made the outcome worse.",
        "why": "A creative director conceding that craft was not the variable is the rarest and most credible thing anyone in the discipline can say out loud.",
    },
    {
        "who": "LAWRY · LEAD VIDEO EDITOR",
        "angle": "The caption file and the chapter markers now decide whether a video is still working in a year, and they are the last thing anybody in an edit suite looks at.",
        "post": "94% of the YouTube videos that AI assistants cite are long-form. Shorts get 5.7%. That's from an Otterly.AI study in March covering over 100 million citation instances across ChatGPT, Google AI Overviews, Perplexity, Copilot and Gemini.\n\nThe reason isn't quality. It's that a model never watches the video. It reads the transcript, the description and the chapter list.\n\nWhich means the files I have spent my career treating as admin are the ones deciding whether a video is still doing work in eighteen months.\n\nDigiday reported this week that the agency Dept has started asking creators for a human-checked transcript instead of auto-captions, chapter markers built around the questions people actually ask rather than round timestamps, and a list of exact product names in the description.\n\nEvery one of those is an edit suite job. None of them has ever appeared in a brief I've been handed.\n\nSame study: 40.83% of the cited videos had fewer than a thousand views, and only 31% had any chapter structure at all.\n\nI still think the cut is the thing. A video nobody finishes doesn't get cited either. But I've started exporting the transcript before I grade, and I'm slightly annoyed about how much difference it appears to make.",
        "why": "It is the one insight in the issue that only comes from a person who actually exports the files, and it hands other editors something specific to change on Monday.",
    },
]
