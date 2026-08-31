# -*- coding: utf-8 -*-
"""Content for THE FEED — issue data only.  The render spec lives in build_feed.py."""

ISSUE = {
    "date_iso": "2026-08-31",
    "kicker": "Crux Media // Monday 31 August 2026",
    "tagline": "What brands did on YouTube yesterday, and whether it worked.",
    "pace": "STEADY",
    "next_drop": "Next drop: Tuesday, 06:30 MT",
}

LEAD = {
    "headline": "CHIPOTLE SHIPPED A MENU ITEM ITS CUSTOMERS INVENTED, THEN LET 100 OF THEM SHOOT THE TV AD",
    "deck": "Two separate decisions landed in the same press release this morning, and they are the same decision.  Chipotle took a food hack its customers had been posting for four years and turned it into a product.  Then it handed the cameras to 100 creators and put the footage on national television without shooting a single frame itself.",
    "stamps": [
        ("CHIPOTLE PRESS RELEASE · 31 AUG", "https://www.prnewswire.com/news-releases/chipotle-marks-a-brand-first-with-all-new-pollo-asado-and-the-debut-of-chili-lime-chips-302863254.html"),
        ("ADWEEK · 31 AUG", "https://www.adweek.com/brand-marketing/fernando-machado-just-let-100-creators-loose-in-50-chipotle-kitchens/"),
    ],
    "body": [
        "Here is the fact that should stop you.  Chipotle says that <mark>since 2022, mentions of seasoned chips paired with Chipotle entrees have increased more than 1,500% across social platforms, while related TikTok and Instagram content has generated approximately 96 million engagements</mark>.  People have been buying a bag of flavoured crisps somewhere else, bringing them into a Chipotle, crushing them over a burrito bowl or tipping the bowl into the bag, and filming it.  For four years.",
        "This morning Chipotle put Chili Lime Chips on its own menu.  Rewards members today, everyone from 4 September.  Alongside it, a rebuilt Pollo Asado.  Fernando Machado, the chief brand officer who arrived in April, described the pair like this: <mark>\"One menu item generated real momentum before going national; the other was inspired directly by how our fans eat Chipotle.\"</mark>",
        "Now the second half.  To sell them, Chipotle <mark>put cameras in the hands of 100 creators at restaurants across the U.S., U.K. and Canada</mark> — 50 kitchens, per Adweek.  No scripts.  No shot lists.  And then the line that matters more than any of the numbers: <mark>\"The resulting national TV campaign features no brand-shot footage, with every frame captured by creators.\"</mark>",
        "Read that as a production decision and you will miss it.  A brand did not commission creators to make social content that sits alongside the real ad.  The creator footage <mark>is</mark> the real ad, running in the most expensive, most heavily controlled, most lawyer-reviewed place a brand buys.  Chipotle gave up the one thing brands never give up, which is the frame.",
        "And notice what the two halves have in common.  In both cases Chipotle stopped treating its audience as the thing being sold to and started treating it as the thing being read.  The chips came out of watching what people already did with the product.  The ad came out of watching how people already film it.  Neither required a new idea.  Both required the brand to accept that the good idea had already happened in public, on someone else's phone, and that the job was to notice.",
        "The risk sits right there too, and it is not theoretical this week.  A hundred unmanaged creators inside food-prep areas is exactly the structure that just cost Good Good its Callaway deal, its retail distribution and a golf tournament.  Machado has a track record of getting nervy work approved — he ran Burger King through the Whopper Detour and the restaurants-on-fire campaign — so he will have priced that.  Everyone copying this on Tuesday will not have.",
    ],
    "numbers": [
        ("1,500%", "rise in social mentions of seasoned chips with Chipotle since 2022"),
        ("96M", "engagements on the TikTok and Instagram content behind that trend"),
        ("100", "creators who shot every frame of the national TV campaign"),
    ],
    "flagnote": "The 1,500% and 96 million figures come from Chipotle's own press release.  No measurement provider, methodology or definition of an engagement is named, and no third party has verified them.  Treat the direction as real and the precision as marketing.",
    "so_what": "Your audience is running product research and shooting your ad for free, and almost nobody is reading either as data.  Social listening usually reports into marketing, so it produces campaign ideas.  Chipotle pointed it at the kitchen and it produced a menu item, then pointed the camera the same way and produced a TV spot with no production company attached to the footage.",
    "do_this": "Pull the last twelve months of social mentions for your product and sort them by what people are physically doing with it rather than what they are saying about it.  Take the top three behaviours to whoever owns the product, not to your agency.",
}

SECTIONS = [
    {
        "id": "ws", "name": "W'S", "page": "pg. 02",
        "note": "what worked, and the exact reason it worked",
        "tint": "blue",
        "items": [
            {
                "title": "Maybelline put the lip gloss on shelf four weeks before the show it was built for, and weekly sales grew ten times over",
                "hook": "The product was already everywhere before anyone wanted it.  That gap is the entire trick.",
                "open": True,
                "stamps": [
                    ("GLOSSY · 28 AUG", "https://www.glossy.co/pop/glossy-pop-newsletter-how-maybelline-leveraged-love-island-to-supercharge-lip-gloss-sales/"),
                ],
                "body": [
                    "Glossy published the numbers on Friday, sourced from the commerce data firm Daash Intelligence.  Weekly sales of Maybelline's Lifter Gel Lip Oil-in-Gel grew <mark>ten times over between the Love Island premiere on 2 June and the finale on 12 July</mark>.  The product went from <mark>under 5% of Maybelline's lip business by unit in May to more than 30% in July</mark>.  Eight shades, under $10, in Target, CVS, Walmart and Amazon.",
                    "Three decisions produced that, and only one of them is the sponsorship.",
                    "First, timing.  Maybelline launched the product <mark>four weeks before the premiere</mark>, fully distributed across retail, TikTok Shop and the show's own app.  Daash chief marketing officer Melissa Munnerlyn gave the mechanism plainly: <mark>\"the window between discovery and purchase really has compressed... if someone sees something on Love Island, they search for it, and it's not available yet, then you really risk losing that demand.\"</mark>  Demand created on a Tuesday night does not wait until Friday.  If the shelf is empty at the moment of the search, the sale does not get delayed.  It disappears.",
                    "Second, depth.  Brand president Yasmin Dastmalchi says they went past product placement into a Lifter Gel challenge inside the show and a recreated glam room with shade matching in the show's own app.  Viewers started calling it the Love Island lip gloss on their own, which is the only branding that has ever worked.",
                    "Third, staffing.  The team included actual fans of the show, so when a contestant was challenged on air to do another islander's makeup, they recognised the moment while it was still live and moved on it.  They then signed the season winners for an exclusive TikTok content and shop bundle.  You cannot brief that reaction time.  You can only hire for it.",
                ],
                "numbers": [
                    ("10x", "weekly sales growth between premiere and finale"),
                    ("30%", "share of Maybelline's lip business by unit in July, from under 5% in May"),
                    ("4 weeks", "gap between the product landing and the show starting"),
                ],
                "flagnote": "The sales figures come from Daash Intelligence, which sells commerce intelligence to beauty brands, supplied to Glossy.  Maybelline has not published its own sales numbers for the product.",
                "so_what": "Most media plans put the product and the campaign live on the same day, because that is when the money starts.  That is backwards for anything discovered on screen, because the audience searches within minutes and buys within hours, and an unavailable product converts a spike of intent into nothing at all.  Landing four weeks early cost Maybelline four weeks of shelf space and bought it the entire eight-week run.",
                "do_this": "For your next campaign tied to a show, a release or a sporting event, get the product fully distributed and searchable four weeks before the first ad runs, and check availability on every retailer you name in the creative before the first spot airs.",
            },
            {
                "title": "A 30-year-old drinks flask brand got one backstage story post and had a reaction video out the same day",
                "hook": "The seeding was planned.  The moment was luck.  The speed was the only thing that turned one into money.",
                "stamps": [
                    ("MODERN RETAIL · 31 AUG", "https://www.modernretail.co/marketing/what-happened-when-bubba-took-its-new-brand-identity-to-lollapalooza/"),
                ],
                "body": [
                    "Bubba is a Newell Brands product from the early nineties, known for large insulated jugs, and it turned up at Lollapalooza this year trying to be something else entirely.  Personalised, colourful bottles.  Vice president Jimmy Jia is refreshingly unembarrassed about the target: <mark>\"We are unapologetically going after a younger female, a baddie.  And we know [festivals] are where the baddies are.\"</mark>",
                    "The plan was to seed bottles into artist suites.  That part is ordinary.  Then headliner Zara Larsson posted one backstage to her Instagram story, and Bubba's own TikTok reacting to that moment did <mark>over 15,000 views against a normal four-figure baseline</mark>.  Newell's outdoor segment grew <mark>4% in the second quarter</mark>.",
                    "Fifteen thousand views is a small number and I am not going to inflate it.  What is worth taking is the sequence.  The brand did not ask Larsson for anything, did not pay her, and did not know it was coming.  It had someone on site with permission to publish, who saw the story, and got a reaction out while the story was still up.  Instagram stories live for 24 hours.  An approval chain that takes two days turns that into nothing.",
                    "Jia says it straight: <mark>\"you can't plan for a small viral moment like that.\"</mark>  Correct.  You can only be staffed to catch one.",
                ],
                "so_what": "Seeding product into rooms where talent already is costs almost nothing and occasionally produces a post nobody had to negotiate.  The reason most brands get nothing out of it is that the resulting moment expires before legal has read the caption.  The win here was not the seeding, which everyone does.  It was one person with a phone and standing permission to post.",
                "do_this": "Name one person on your team who can publish to your brand accounts without approval for anything under 30 seconds long, and give them a written list of what they are allowed to say.  Do it before your next event, not after it.",
            },
        ],
    },
    {
        "id": "ls", "name": "L'S", "page": "pg. 03",
        "note": "what broke, and the failure mode that broke it",
        "tint": "pink",
        "items": [
            {
                "title": "Wrong owner: the golf company fired the people who made the ad, and the founder who is in it still has a job",
                "hook": "Six days on, nobody who signed it off has been named, and the two companies are now arguing in public.",
                "stamps": [
                    ("TUBEFILTER · 30 AUG", "https://www.tubefilter.com/2026/08/30/good-good-callaway-driver-ad-controversy/"),
                    ("CBS NEWS · 28 AUG", "https://www.cbsnews.com/news/good-good-golf-callaway-backlash-ad/"),
                    ("CNN · 27 AUG", "https://www.cnn.com/2026/08/27/sport/good-good-callaway-advertisement"),
                ],
                "body": [
                    "We covered the collapse on Friday.  This is the second act, and it is the more instructive one.",
                    "Recap in one line: golf creator company Good Good made a 60-second spot for a new Callaway driver in which co-founder Garrett Clark shoves golfer Alexis Miestowski to the ground for touching the club.  Callaway approved it.  Chief executive Chip Brewer then said <mark>\"that approval should never have happened\"</mark>, ended the three-year partnership and pledged <mark>$1 million</mark> to organisations preventing violence against women.  Target, Golf Galaxy and Dick's pulled the merchandise.  Golf Channel cancelled a fully-filmed season of its Good Good show.  Good Good gave up a PGA Tour title sponsorship Tubefilter reports at <mark>$6 million</mark>.",
                    "Over the weekend Good Good chief executive Matt Kendrick told Front Office Sports he has <mark>\"removed people responsible\"</mark> and that he never saw the ad before it went out.  He would not say whether Clark, who is in the ad, is among them.  Then he went at his own client on X, accusing Callaway of asking Good Good to take the fall before dropping them in a coordinated media blitz.",
                    "Two things are now true at once.  Callaway has bought distance — a fast termination and a large cheque, and by next quarter it is a brand that handled a supplier problem quickly.  Good Good cannot buy distance, because Good Good is the asset.  There is no separate company to blame and no other product to sell.  When your entire enterprise value is four guys people like, a firing announcement does not remove the problem from the screen.",
                    "And the public fight is the compounding error.  A creative failure is survivable and forgettable.  A creative failure followed by the founder attacking his largest former partner in public is a different question for every brand safety review from now on, because the question stops being \"was the ad bad\" and becomes \"what happens to us when something goes wrong.\"",
                    "Crisis consultant Patrick Riccards put the accountability part to CBS with no room left in it: <mark>\"They approved the offensive ad, they produced the offensive ad, they released the offensive ad.\"</mark>",
                ],
                "flagnote": "The $6 million PGA Tour sponsorship figure comes from Tubefilter alone.  CNN, ESPN and CBS confirm the sponsorship ended but do not put a number on it.",
                "so_what": "Co-produced brand video has two owners and usually no single approver, which is exactly how a spot reaches air with both parties assuming the other one checked.  The brand can exit that arrangement in a day.  The creator company cannot, because it has no separate balance sheet to hide behind, so it absorbs the whole loss and then tends to make things worse defending itself.  If you are the creator side of one of these deals, the asymmetry is the deal.",
                "do_this": "Write one name into every co-produced brief as the single person who gives final sign-off, and add a clause covering what each side may and may not say publicly in the first 72 hours of a problem.  Do it on the next contract you sign, not the next one you renew.",
            },
            {
                "title": "Wrong format: the ad worked because nobody could tell it was an ad, and now nobody can tell whether any of it was true",
                "hook": "Thirteen videos, ten million views on the first one, a disclosure hashtag on every single post, and it still fooled the brand it was not even for.",
                "stamps": [
                    ("DEXERTO · 28 AUG", "https://www.dexerto.com/food/viral-oreogate-mom-drama-was-a-paid-ai-ad-and-its-creator-wont-say-if-it-was-real-3403588/"),
                ],
                "body": [
                    "Instagram creator ashleighjamz ran a <mark>13-video</mark> serial about a parent group chat melting down over a mother demanding that classmates stop packing Oreos, escalating to lunchbox searches and separate seating.  The <mark>first video passed 10 million views</mark>.  Parents argued.  Medical professionals weighed in.  <mark>Oreo's own official Threads account engaged with it</mark> as though it were real drama.",
                    "It was a paid campaign for Suno, the AI music generator.  The alleged WhatsApp messages were turned into songs using Suno's tech, and every post carried the tag #sunopartner.  Suno confirms the paid relationship and says it did not control the storyline.  The account is <mark>less than a month old</mark> and contains almost nothing but Suno-sponsored content in the same format.  The creator will not say whether the mother, the child or the messages exist.",
                    "So the disclosure was technically there on every post and functionally invisible on all of them.  That is the failure mode, and it is a format failure rather than a legal one.  Screenshots of a group chat are the single most trusted visual grammar on social right now, because they read as evidence rather than as content.  Wrap an ad in evidence grammar and the audience files it under news, not marketing, and a hashtag at the end of a caption does not move it back.",
                    "The bill lands on people who did not sign anything.  Oreo bought nothing, briefed nothing and approved nothing, and spent a week as a character in a competitor category's campaign.  If you sell a product that people argue about in group chats — food, kids, schools, health — you are one convincing screenshot serial away from being cast in someone else's ad."
                ],
                "so_what": "Disclosure only works when it arrives before belief does.  A hashtag sits after the payoff, which means the viewer has already decided the thing is real, and the correction never reaches the 10 million who saw only the first video.  The engagement was bought with the ambiguity, which means the ambiguity was the product, and that is a very short-lived asset for any brand attached to it.",
                "do_this": "Put a spoken or on-screen disclosure in the first three seconds of every creator video you pay for, and write into your contract that documentary-style formats — screenshots, texts, receipts, hidden camera — must be labelled as recreated.  Set up an alert on your own brand name so you find out you are in someone else's campaign on day one rather than day nine.",
            },
        ],
    },
    {
        "id": "moves", "name": "MOVES", "page": "pg. 04",
        "note": "the shifts that change what you can buy next quarter",
        "items": [
            {
                "title": "Twitch put a public performance label on channels and pulled it within three days",
                "hook": "It said \"viewership surging.\"  Streamers read the version it implied when it was absent.",
                "stamps": [
                    ("DEXERTO · 31 AUG", "https://www.dexerto.com/twitch/twitch-rolls-back-viewership-trend-experiment-after-backlash-3404072/"),
                ],
                "body": [
                    "On 28 August, industry watcher Zach Bussey spotted Twitch testing public channel labels reading <mark>\"viewership surging\"</mark> and <mark>\"keeping viewers\"</mark> on a limited set of channels.  Streamers turned on it within hours.  Twitch Support conceded the next day, saying some of the language <mark>\"doesn't really capture\"</mark> the intent and confirming it would roll both labels back.",
                    "The intent was discovery.  The effect was a scoreboard.  Every other label on a channel describes the content — the game, the category, the language, whether it is live.  These two described the channel's trajectory, which means the absence of one is information too.  A streamer having a soft fortnight now carries a visible negative signal into every browse page.",
                    "For anyone buying streamers, the useful part is what did not change.  Twitch clearly has surge and retention data at channel level and was comfortable enough with it to put it on the front end.  That data is the thing you have been asking sellers for and getting a screenshot of instead.",
                ],
                "so_what": "Platforms keep discovering that momentum metrics are safe internally and radioactive in public, because publishing them turns a discovery tool into a ranking.  But the experiment confirms Twitch computes exactly the trend data brands need to price a sponsorship, and it is currently only visible to the platform and, briefly, to everyone.",
                "do_this": "Ask your Twitch sales contact or your streamer's manager for 90-day trend on average concurrent viewers, not a peak screenshot, and make it a standard field in your sponsorship template.",
            },
            {
                "title": "Ina Garten is starting a YouTube channel, and Vox Media is selling the ads on it",
                "hook": "The talent is 78 and the distribution deal is the newest thing about it.",
                "stamps": [
                    ("YOUTUBE BLOG · 28 AUG", "https://blog.youtube/creator-and-artist-stories/ina-garten-official-youtube-channel-happy-hour/"),
                    ("THE HOLLYWOOD REPORTER · 28 AUG", "https://www.hollywoodreporter.com/business/digital/ina-garten-launches-youtube-channel-happy-hour-1236684203/"),
                ],
                "body": [
                    "Garten is launching an official YouTube channel hosting <mark>Happy Hour</mark>, a weekly interview show filmed in her New York apartment with guests from food, culture, art, entertainment and sport.  It premieres <mark>16 September</mark>.  <mark>Vox Media handles sales, marketing and distribution.</mark>",
                    "Food Network built her.  She is going YouTube-first anyway, and she is not doing it alone or in-house — she has taken a publisher partner to do the commercial work, which is the part most legacy talent gets wrong when they arrive on the platform and try to sell their own sponsorships at television rates.",
                    "For brands this is a rare thing: a genuinely premium, genuinely adult, low-risk video property arriving on YouTube with a professional sales operation attached from day one, in a category — food and drink — where the endorsement actually converts.",
                ],
                "so_what": "The interesting move is structural rather than editorial.  Legacy talent going YouTube-first now comes with a media company doing sales, which means you can buy it through a process you already recognise instead of negotiating with a manager who has never priced a video sponsorship.  Expect more of these, and expect the early ones to be underpriced while nobody has a benchmark.",
                "do_this": "Get on Vox Media's list for Happy Hour sponsorship before the 16 September premiere, while the rate is set against an unproven channel rather than an established one.",
            },
            {
                "title": "Hank Green is launching a paid kids' video app with no autoplay and no infinite feed",
                "hook": "Everything the last decade optimised for, deliberately removed.",
                "stamps": [
                    ("TUBEFILTER · 28 AUG", "https://www.tubefilter.com/2026/08/28/hank-green-clockwisetv-content-app/"),
                ],
                "body": [
                    "ClockwiseTV is a paid, ad-free, tablet-only science and arts video app for children aged 8 to 12.  Parents set a session length and the app closes when the time is up.  No autoplay, no endless feed, no data tracking.  Launch creators include Green, Complexly, MinutePhysics, Odd Animal Specimens and Evan and Katelyn.  Leslie Morgan is chief executive.",
                    "The model is re-editing existing creator catalogues for the age group, and Green says the app does all of the heavy lifting.  Tubefilter flags the open question directly: <mark>it is not clear whether the participating creators get a revenue share.</mark>",
                    "The timing is not an accident.  Australia has banned teenagers from social media, Roblox has banned reward-driven scrolling feeds for its youngest users, and Meta has just agreed to daily time caps for teens.  A paid product whose selling point is that it stops is aimed squarely at parents who have watched all of that and drawn a conclusion.",
                ],
                "so_what": "If children's attention keeps getting regulated into shorter, paid, ad-free environments, the advertising route to that audience narrows and the licensing route widens.  Nobody is buying a pre-roll here.  The commercial question becomes whether your brand can own or fund the programme itself, which is a different budget line and a much longer lead time.",
                "do_this": "If you sell to families, brief your team on what a sponsored or funded show inside a paid, ad-free kids' environment would cost and look like, so you have an answer ready when the first one offers it.",
            },
            {
                "title": "OpenAI is making it easier to buy ads on ChatGPT, and matching your first $500",
                "hook": "A new ad platform with matched credits is a new ad platform that needs advertisers.",
                "stamps": [
                    ("MARKETING BREW · 31 AUG", "https://www.marketingbrew.com/stories/openai-streamlining-chatgpt-ad-campaign-creation"),
                ],
                "body": [
                    "Following the ChatGPT ad rollout across <mark>31 countries</mark>, OpenAI has redesigned its campaign onboarding and is offering new advertisers <mark>$500 in matching credits on $500 of spend</mark>.",
                    "Matched credits are what an ad platform does when it has inventory and not enough buyers.  That is not a criticism, it is a window.  The people who tested Facebook video in 2014 and TikTok in 2020 learned the format while it was cheap and while nobody senior was watching the results.",
                    "For anyone making brand video, the honest note is that this is a text and answer environment, not a video one.  The value of testing it now is learning how your brand gets described inside a chatbot answer, which is quietly becoming a distribution channel of its own — Tubefilter reported last week that YouTube creator content already appears in a quarter of AI chatbot responses.",
                ],
                "so_what": "Every new ad platform is cheapest in the months when it is begging.  The learning is worth more than the media at this stage, because the thing you are actually buying is an early read on how purchase questions get answered when there is no feed and no thumbnail.",
                "do_this": "Put $500 into a ChatGPT test campaign this week, claim the match, and pick a product question you already know the answer to so you can judge how the environment handles it.",
            },
        ],
    },
    {
        "id": "onstream", "name": "ON STREAM", "page": "pg. 05",
        "note": "the live numbers, and what they actually measure",
        "items": [
            {
                "title": "The full count on the GTA VI reveal is 3.97 million people at once, and 9,000 channels did the distribution for free",
                "hook": "We gave you 1.8 million on Friday.  The platform-wide number is more than double that, and the gap is the whole lesson.",
                "open": True,
                "stamps": [
                    ("STREAMS CHARTS · 28 AUG", "https://streamscharts.com/news/gta-vi-gameplay-reveal-viewership"),
                    ("STREAMS CHARTS · SIDEMEN MATCH", "https://streamscharts.com/news/sidemen-charity-match-2026"),
                ],
                "body": [
                    "Streams Charts published the full recap of the GTA VI Extended Look on Friday.  The broadcast ran on Netflix at 19:00 UTC on 27 August, with restreaming allowed.  Across livestreaming platforms it peaked at <mark>3,970,000 concurrent viewers</mark>, drew <mark>5.2 million hours watched</mark>, and was co-streamed by <mark>more than 9,000 channels</mark>.  Twitch carried 44% of the hours watched, YouTube 34.8%, Kick 20.2%.  The largest individual co-streamer was IlloJuan at 233,500.",
                    "Two honest caveats before the number gets used in a deck.  Streams Charts did not publish an average concurrent figure, so peak is all we have, and peak is the flatterable one.  And Netflix, which carried the official feed, did not break out its own audience — so 3.97 million is everyone watching a restream and nobody watching the source.  The real total is higher and unknowable.",
                    "Make it mean something.  The Sidemen Charity Match at Wembley in April peaked at <mark>2,260,000</mark> with <mark>90,000 people in the stadium</mark>.  So a games publisher showing a trailer out-drew the biggest creator livestream in Britain this year by roughly three quarters, and put about 44 Wembleys in front of the same frames at the same second.  It also beat Summer Game Fest 2026, which peaked at 3,810,000.",
                    "The mechanism is the 9,000 channels.  Rockstar did not buy that reach.  It made the material exclusive to one place at one time, allowed everyone else to react to it live, and let nine thousand people with audiences spend their own evening and their own bandwidth carrying it.  Every one of those streams was a personality vouching for the thing while watching it — which is worth far more than the same footage played in a pre-roll, and cost nothing.",
                    "One thing worth noticing for your own planning: this was a single asset with a single start time, and the audience organised itself around the clock rather than around the platform.  Twitch, YouTube and Kick all carried it because none of them owned it.",
                ],
                "flagnote": "Friday's issue carried a 1.8 million peak from Downdetector and crowd-reported Twitch data.  Streams Charts' 3.97 million is a platform-wide count published after the fact and supersedes it.  Average concurrent viewers were not published for this event.",
                "so_what": "Co-streaming is the cheapest distribution available to owned video and almost nobody plans for it, because it requires giving away control of the frame around your asset.  The trade is enormous: nine thousand channels of reach, all of it fronted by someone the viewer already trusts, in exchange for not controlling the commentary.  The trigger is not the content.  It is the single start time, which is what forces everyone to arrive together.",
                "do_this": "For your next big owned video, publish a single premiere time, state in writing that co-streaming is permitted, and send the time and the rules to every creator in your category a week ahead so they can schedule around it.",
            },
        ],
    },
    {
        "id": "watch", "name": "ONE TO WATCH", "page": "pg. 06",
        "note": "one creator, picked for momentum rather than size",
        "items": [
            {
                "title": "Cameron Das Racing",
                "hook": "A licensed professional driver who turned a karting channel into a season-long quest, and grew 918% in a quarter doing it.",
                "open": True,
                "stamps": [
                    ("YOUTUBE CHANNEL", "https://www.youtube.com/@camerondasracing"),
                    ("PIXABILITY VIA NET INFLUENCER · 23 JUL", "https://www.netinfluencer.com/sports-creator-growth-on-youtube-shows-subscriber-count-alone-isnt-enough-report-finds/"),
                ],
                "body": [
                    "Cameron Das is a real racing driver with a real racing record, and until this year his YouTube channel was a pleasant hobby.  As of this morning it carries <mark>938,000 subscribers</mark> across 464 videos.  Pixability's YouTube Creator Hot List for sports put his <mark>subscriber growth at 918% quarter on quarter in the second quarter of 2026</mark> — a list built specifically around momentum rather than size.",
                    "The turn is visible in his own upload history, and you can check it yourself on YouTube's public feed.  On 21 February he posted a video about racing his subscribers that did <mark>25,070 views</mark>.  Two weeks later, on 7 March, he posted one titled <mark>I'm entering the Kart World Championship, if I can qualify</mark>.  It has <mark>678,150</mark>.",
                    "Nothing about the production changed.  The premise did.  He stopped uploading individual outings and started uploading chapters of one story with a stated goal and a real chance of failure, and every video since has been a step toward or away from it.  The payoff chapter went up on 29 August.",
                    "Two other things moved at the same time.  His runtimes went long — the best video of the last three months is over an hour — and he started collaborating upward: an F1 driver at Silverstone, the Super GT channel on the World Championship film, and an invitation from Ayrton Senna's family to a celebrity kart race in Brazil in July.  Access is compounding faster than the subscriber count, which is usually the tell.",
                    "The view counts are volatile — 51,000 in June, 250,000 later the same month, 385,000 in August — and that volatility is exactly why he is still affordable.",
                ],
                "watch": {
                    "label": "TOP VIDEO, LAST 3 MONTHS",
                    "title": "I Hired A Formula 1 Driver To Win The 24 Hours of Silverstone",
                    "url": "https://www.youtube.com/watch?v=aFtqYQQC5Y4",
                    "meta": "385,038 views · published 1 August 2026 · 1h 4m",
                    "note": "An hour-long documentary in which he assembles a team and an actual Formula 1 driver for a 24-hour endurance kart race, and you watch the whole thing.",
                },
                "flagnote": "The 918% growth figure comes from Pixability, which sells creator selection services, reported by Net Influencer.  The baseline subscriber number behind the percentage is not published.  The subscriber count, view counts and publication dates above are taken from YouTube's own channel page and public feed on 31 August 2026.",
                "so_what": "The people who should be calling are tyre, brake and lubricant brands, sim-racing hardware, and the endemic motorsport categories, because he holds an actual licence and a technical claim survives in his mouth in a way it does not in a lifestyle creator's.  What they would be buying is not a 60-second read.  It is an hour-long, chaptered documentary with a season arc and a hundred thousand to nearly four hundred thousand people watching it at feature length, which is watch time no pre-roll can buy.",
                "do_this": "Approach him about title sponsorship of the next season arc rather than a single video, and ask for equipment supply inside the kart so the result becomes the proof.  Do it before he crosses a million subscribers, because that is the number that resets a rate card.",
            },
        ],
    },
    {
        "id": "money", "name": "THE MONEY", "page": "pg. 07",
        "note": "who is spending, and on what",
        "items": [
            {
                "title": "A $160 million advertiser just picked its lead agency with no pitch, on the Monday football season starts",
                "hook": "Two betting giants launched celebrity campaigns within hours of each other.  The interesting number is who is handling the money.",
                "open": True,
                "stamps": [
                    ("ADWEEK · 31 AUG", "https://www.adweek.com/agencies/jon-hamm-ad-kicks-off-betmgms-aor-partnership-with-indie-agency-cape/"),
                    ("VARIETY · 31 AUG", "https://variety.com/2026/tv/news/draftkings-kevin-hart-nick-jonas-sports-commercial-1236847055/"),
                ],
                "body": [
                    "BetMGM has named the independent shop Cape its lead agency, formalising two years of project work, and it did so <mark>with no formal pitch process</mark>.  COMvergence puts BetMGM's net media spend at an estimated <mark>$160 million</mark>.  The relationship launches with a Jon Hamm spot.",
                    "The same morning, DraftKings launched a long-running campaign with Kevin Hart and Nick Jonas on a cross-country road trip, with further creative featuring Chad Ochocinco and Carmelo Anthony.  iSpot data puts DraftKings at approximately <mark>$69.5 million advertising inside NFL games in 2025</mark>, and <mark>$12.8 million inside NBA games</mark>.",
                    "Look at why both landed on famous, likeable people rather than product.  In sports betting every operator runs near-identical frequency against a near-identical audience with a near-identical product, at the same moment in the calendar, in a category where you cannot make functional claims.  When the media plan, the audience and the offer are all the same, the only remaining variable is who is on screen and whether you enjoy them.",
                    "The structural note is the pitch that never happened.  A nine-figure advertiser handing lead agency duties to an independent with no review, in the same week Digiday is reporting a wobbling turnaround at the largest holding company, is a real data point about where confidence sits.",
                ],
                "so_what": "Two things to take.  First, in a saturated category, casting is the media plan — you are not buying attention, you are buying the difference between your ad and the identical one before it.  Second, large advertisers are increasingly willing to skip the review process entirely for a partner who has already done the work, which means the way to win big accounts now is to do small projects for them first.",
                "do_this": "If you want a bigger account, take the small project and treat it as the pitch.  If you are the buyer, look at what your incumbent has actually shipped this year before you spend six months running a review.",
            },
            {
                "title": "The Telegraph's podcast audience is up 161% and it is now selling video, events and memberships against it",
                "hook": "2.4 million weekly YouTube views on three news shows, from a 170-year-old newspaper.",
                "stamps": [
                    ("DIGIDAY · 31 AUG", "https://digiday.com/media/the-telegraphs-next-podcast-play-video-events-and-paid-memberships/"),
                ],
                "body": [
                    "The Telegraph is turning its podcasts into franchises that run across video, live events and paid membership.  The numbers behind the decision: <mark>podcast audience up 161% year on year</mark>, and <mark>2.4 million weekly average YouTube views</mark> across three daily news shows.",
                    "Matthew Bayley, its executive editor of audio and visuals, says the quiet part: <mark>\"There is no escaping the fact that video is now becoming the primary method by which news and journalism is consumed.\"</mark>",
                    "For a brand buyer this is a category of inventory that barely existed three years ago and is still priced like radio in a lot of places — daily, appointment-based, video-first news shows with a named host and a defined audience, sitting on YouTube rather than behind a paywall.",
                ],
                "so_what": "Publishers moving their audio franchises to video-first are creating host-read sponsorship inventory that behaves like a creator deal but comes with an editorial brand attached.  It is the cheapest way currently available to get a trusted human voice reading your product to an adult daily audience, and the rates have not caught up to the audience yet.",
                "do_this": "Ask your media team to price host-read sponsorship on three publisher-owned daily video shows in your market and compare the cost per thousand viewers against your current creator rates.",
            },
        ],
    },
    {
        "id": "format", "name": "FORMAT LAB", "page": "pg. 08",
        "note": "one structural idea you can steal this week",
        "items": [
            {
                "title": "Cheez-It stopped making commercials and started making podcast episodes",
                "hook": "Same length, same media buy, completely different shape.  The audience never asked for a stadium.",
                "open": True,
                "stamps": [
                    ("ADWEEK · 31 AUG", "https://www.adweek.com/creativity/cheez-it-brings-game-day-hot-takes-from-the-stands-to-the-couch/"),
                ],
                "body": [
                    "Cheez-It launched its first new creative direction since 2022 today, from BBDO New York, with a national television debut on <mark>6 September</mark>.  It is called the Cheez-It Couch Committee, it is set on an orange couch, and the spots are built to play like episodes of a talk show — people arguing about college football, helmet stickers and extended eligibility.",
                    "That is the whole idea and it is worth taking seriously.  Sports advertising has one default shape: the stadium, the slow motion, the athlete, the swell of music.  Cheez-It's audience does not spend its week watching stadiums.  It spends its week watching two or three people argue about sport on a couch, because that is what the entire sports media business now looks like on YouTube.",
                    "So the brand copied the format its audience actually consumes rather than the format the medium traditionally sells.  A 30-second spot shaped like a clip from a show has an obvious second life — it can be 30 seconds on television and eleven minutes on YouTube, and the long version is not a cut-down or an extension.  It is the thing itself.",
                    "The test of whether they meant it will be whether a long-form version appears on the Cheez-It channel next week.  If it does not, this is a format borrowed for its look rather than its economics.",
                ],
                "so_what": "Most brands make a television ad and then chop it into social versions, which is why the social versions feel like offcuts.  Building in the shape of a show that already exists gets you the reverse: the television spot is the trailer, and the full episode is the asset that earns watch time on the platform where the audience actually is.  It costs the same to shoot.",
                "do_this": "Take your next 30-second concept and write the eleven-minute version of it first, then cut the 30 seconds out of that.  If the long version is not watchable on its own, the concept was an ad rather than a format.",
            },
        ],
    },
]

FORECAST = [
    {
        "confidence": "LIKELY",
        "window": "by 31 March 2027",
        "headline": "\"No brand-shot footage\" turns up as a line in briefs, and the savings get eaten by rights and clearance",
        "body": "Chipotle has just proved a national television campaign can be assembled entirely from creator-shot material, and that is the kind of result that gets screenshotted into a hundred planning decks by Friday.  The production saving is real and obvious.  What is not obvious to the people about to copy it is that a hundred contributors means a hundred usage agreements, a hundred music and likeness clearances, and a hundred people who can post the outtakes.  Expect a wave of imitators in the first quarter, and expect at least one to discover that the legal cost of clearing crowd-sourced footage for broadcast exceeds what a crew would have cost.",
        "do": "Price the rights and clearance work for a hundred-contributor campaign now, so you know the real number before someone in your company proposes one.",
    },
    {
        "confidence": "LIKELY",
        "window": "next 12 months",
        "headline": "A regulator forces disclosure into the opening seconds of creator video rather than the caption",
        "body": "The Oreo and Suno case is the cleanest possible argument that hashtag disclosure fails when the creative is built to read as documentary evidence, and it produced a brand being pulled into a campaign it had no part in.  Regulators in the UK and the US have both been circling creator disclosure for years without settling the placement question.  A serial that fooled a rival brand's own account is the sort of specific, embarrassing example that moves guidance from principle to position, and the obvious position is that the disclosure has to arrive before the story does.",
        "do": "Move disclosure to the first three seconds across all your creator work now, so a rule change costs you nothing.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "next 9 months",
        "headline": "Co-streaming rights become a negotiated, paid line in launch plans instead of a free-for-all",
        "body": "Nine thousand channels carried the GTA VI reveal and every one of them did it for nothing, which is the best distribution deal in media right now and therefore an unstable one.  Two pressures will change it.  Publishers and brands will start wanting the largest co-streamers on message and on time, which means paying them.  And the largest co-streamers will start noticing they supplied the reach and captured only the ad revenue on their own channel.  The likely shape is a tier system: open permission for everyone, paid slots with early access and talking points for the top fifty.",
        "do": "Build a list of the twenty creators in your category who would co-stream your next launch, and find out today what a paid early-access slot would cost.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "by 30 June 2027",
        "headline": "Brands start buying the season rather than the video, and creators start pricing arcs",
        "body": "Cameron Das grew 918% in a quarter by converting standalone uploads into chapters of one story, and he is not unusual — serialised goals are becoming the dominant retention structure on long-form YouTube because they give the viewer a reason to return rather than a reason to click.  Single-video sponsorship prices a chapter as though it were a standalone, which is either a bargain or a waste depending on where in the arc you land.  Expect the better-advised creators to start selling arc-level packages with a fixed number of chapters and a resolution, and expect the first brands in to get them cheap.",
        "do": "Ask any creator you are about to book what their next three videos build toward, and price the sponsorship against the arc rather than the upload.",
    },
    {
        "confidence": "LONG SHOT",
        "window": "next 18 months",
        "headline": "A large consumer brand puts social listening inside product development and says so on the packaging",
        "body": "Chipotle's chips came out of four years of watching what people did with the product, but the company still framed the whole thing as marketing, and the listening function almost certainly still reports into marketing.  The obvious next step is a brand that moves that team next to product development and then markets the fact — packaging that says this was your idea, with the count of posts on the back.  It is a long shot because it requires two departments that do not currently talk to share a budget, and because the first brand to try it will be accused of taking credit for its customers' work.  It would also be the single most convincing piece of packaging on the shelf.",
        "do": "Get whoever runs your social listening into one meeting with whoever runs product this quarter, with the top ten customer behaviours printed out.",
    },
]

TLDR = [
    "Chipotle turned a four-year-old customer food hack into a menu item and shot the entire national TV campaign with 100 creators and no brand footage, on social mentions it says rose more than 1,500% since 2022 across roughly 96 million engagements.  Pull your last twelve months of social mentions, sort them by what people physically do with your product rather than what they say, and take the top three behaviours to whoever owns the product.",
    "Maybelline put its Love Island lip gloss on shelf four weeks before the premiere and weekly sales grew ten times over between premiere and finale, taking the product from under 5% to more than 30% of its lip business by unit — because demand created on screen is searched within minutes and dies if the shelf is empty.  Get product fully distributed and searchable four weeks before your first ad runs on any campaign tied to a show or an event.",
    "The GTA VI reveal peaked at 3.97 million concurrent viewers with 5.2 million hours watched, carried by more than 9,000 co-streaming channels Rockstar paid nothing for, against 2.26 million for the Sidemen's Wembley match in April.  Publish a single premiere time for your next big owned video, say in writing that co-streaming is permitted, and tell every creator in your category the time a week ahead.",
    "Good Good's chief executive says he has removed the people responsible for the Callaway ad, will not say whether the founder who appears in it is among them, and is now attacking his former partner in public — after losing a three-year deal, retail distribution, a TV season and a tour sponsorship reported at $6 million.  Write one named final approver into every co-produced brief and add a clause governing what each side may say publicly in the first 72 hours of a problem.",
    "A 13-video Instagram serial about a school Oreo ban passed 10 million views on the first episode, carried a #sunopartner tag on every post, fooled Oreo's own Threads account, and the creator still will not say whether any of it was real.  Put a spoken or on-screen disclosure in the first three seconds of every creator video you pay for, and require documentary-style formats to be labelled as recreated.",
    "BetMGM handed lead agency duties on an estimated $160 million in net media to an independent shop with no pitch process, while DraftKings — which spent about $69.5 million inside NFL games last year — launched a Kevin Hart and Nick Jonas campaign the same morning.  Take the small project as your pitch if you want the big account, and check what your incumbent has actually shipped this year before you run a six-month review.",
    "Cheez-It's first new creative direction since 2022 is built as talk-show episodes rather than stadium commercials, debuting on national television on 6 September, because its audience watches people argue on a couch rather than watching stadiums.  Write the eleven-minute version of your next 30-second concept first and cut the spot out of it — if the long version is not watchable alone, you have an ad rather than a format.",
]
