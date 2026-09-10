# -*- coding: utf-8 -*-
"""Content for THE FEED — issue data only.  The render spec lives in build_feed.py."""

ISSUE = {
    "date_iso": "2026-09-10",
    "kicker": "Crux Media // Thursday 10 September 2026",
    "tagline": "What brands did on YouTube yesterday, and whether it worked.",
    "pace": "STEADY",
    "next_drop": "Next drop: Friday, 06:30 MT",
}

LEAD = {
    "headline": "TWO FORECASTERS RAISED THEIR US AD SPEND OUTLOOK IN TWENTY FOUR HOURS.  ONE OF THEM PUTS NEXT YEAR AT 4.1 PERCENT",
    "deck": "The IAB raised its 2026 US forecast to 12.3% this morning, up from the 9.5% it published in January.  Madison and Wall raised its US number to 15.6% yesterday.  Both upgrades are real, and almost all of the growth inside them comes from events that do not happen again next year.  The number that belongs in your 2027 plan is 4.1.",
    "stamps": [
        ("IAB · 10 SEP", "https://www.iab.com/news/iab-raises-2026-u-s-ad-spend-forecast/"),
        ("IAB — 2026 OUTLOOK, SEPTEMBER UPDATE", "https://www.iab.com/insights/2026-outlook-study-september-update/"),
        ("MEDIAPOST · 9 SEP", "https://www.mediapost.com/publications/article/417751/ad-outlook-composite-improves-on-mw-upgrade.html"),
        ("DIGIDAY · 10 SEP", "https://digiday.com/media-buying/ad-spend-forecasts-revised-upward-as-more-ad-dollars-are-handled-by-ai-tools/"),
    ],
    "body": [
        "The IAB published its September revision this morning.  <mark>US ad spend now grows 12.3% in 2026, up 2.8 points from the 9.5% it forecast in January.</mark>  The channel split is where it gets interesting for anyone who sells video: social media 16.5%, connected TV 15.6%, commerce media 13.6%, podcasts 8.7%, paid search 8.1%, digital out of home 7.0%, linear TV minus 1.5%.  One video line got revised down — <mark>digital video excluding connected TV fell from 9.6% to 9.4%</mark>, the only channel besides search and out of home to lose ground since January.",
        "Yesterday Madison and Wall went further.  Joe Mandese reported at MediaPost that the firm had raised its US growth projection by 3.5 points to <mark>15.6%</mark> and its global number by 2.2 points to 11.6%.  MediaPost's blended composite of several forecasters lands at 9.6% for the US, which tells you Madison and Wall is the outlier on the high side rather than the consensus.",
        "Now read what is actually producing the growth.  The IAB names it plainly: a stronger than expected first half fuelled by major cyclical events, including the Winter Olympics and the FIFA World Cup.  Madison and Wall says something the IAB does not — its figures include US political ad spending.  Digiday reports the same firm's global growth at 9.8% once US political money is stripped out.  So one forecaster's headline number contains an election, and both contain two sporting events that happen once every four years.",
        "Which brings you to the number nobody is putting in a headline.  <mark>Madison and Wall's own 2027 forecast for the US is 4.1%.</mark>  Global is 5.9%.  MediaPost's composite has US 2027 at 4.4%.  The same people telling you this year grows 15.6% are telling you next year grows at roughly a quarter of that rate, because the Olympics, the World Cup and the midterms do not come back.",
        "David Cohen, chief executive of the IAB, hedges carefully in the release: the first half was strong, major live events delivered, and advertisers have increasingly powerful tools in their arsenal to find and engage customers.  At the same time, the economy has real areas of uncertainty.  There is growth to be found, but there are no easy wins.",
        "One more thing buried in the same study, and it matters more to you than the top line.  Asked which ad types they are increasing focus on, buyers put <mark>creator and influencer advertising and partnerships at the top of the list, on 54%</mark> — ahead of demographic and cohort targeting at 53%, publishers with first-party data at 48% and contextual at 45%.  The market is growing for a reason that will not repeat, and the money inside it is moving toward the thing you make.",
    ],
    "numbers": [
        ("12.3%", "the IAB's new 2026 US growth forecast, raised from 9.5% in January"),
        ("15.6%", "Madison and Wall's US number for 2026, political money included"),
        ("4.1%", "the same firm's US forecast for 2027"),
    ],
    "flagnote": "The IAB's entire published methodology is that the study draws on more than 200 brand and agency ad investment decision-makers.  No field dates, no sample breakdown, no margin of error and no dollar figures are disclosed, and it measures buyer intent rather than spend that has happened.  It is published by a trade body whose members sell the inventory being forecast.  Madison and Wall's underlying report is subscriber-only; MediaPost reports its global 2026 growth as 11.6% and Digiday as 11%, a gap this brief could not reconcile from public sources, so the global figure is quoted here as MediaPost has it.",
    "so_what": "Growth like this is a calendar, not a verdict on your work.  Two once-in-four-years sporting events and an American election cycle are carrying it, which is exactly why the firm with the biggest 2026 number has the smallest 2027 one.  If your next budget conversation is anchored on this year's headline, you are anchoring on a growth rate the market itself expects to fall by about three quarters within twelve months.",
    "do_this": "Rebuild your 2027 line this week on the number that excludes political and cyclical money — Madison and Wall's US 4.1% — and take that version into the budget meeting alongside the headline, so you own the comparison before someone else makes it.",
}

SECTIONS = [
    {
        "id": "ws", "name": "W'S", "page": "pg. 02",
        "note": "what worked, and the exact reason it worked",
        "tint": "blue",
        "items": [
            {
                "title": "A data-removal service sponsored a true-crime video that did 17.9 million views, and the fear in the video is the product demonstration",
                "hook": "Fourth-biggest branded video of the week, in a chart where the top two are MrBeast at 47 million each.",
                "open": True,
                "stamps": [
                    ("TUBEFILTER · 8 SEP", "https://www.tubefilter.com/2026/09/08/top-5-branded-videos-mrbeast-gaming-jordan-matter-salish-matter-dr-insanity/"),
                    ("TUBEFILTER · 20 NOV 2025", "https://www.tubefilter.com/2025/11/20/morgan-morgan-injury-law-firm-youtube-sponsored-creator-program/"),
                ],
                "body": [
                    "Tubefilter's weekly branded-video chart, built on Gospel Stats data, ran on Monday.  The top two are both MrBeast — Feastables at 47,456,973 views and Old Navy at 47,082,142.  Third is Jordan Matter with GoGo squeeZ at 20,991,542 views.  Fourth is the one worth studying: a 34-minute true-crime video on the channel Dr Insanity, called Hidden Camera Reveals Wanted Killer Living Inside Familys Attic, sponsored by the data-removal service Aura, at <mark>17,876,710 views</mark>.",
                    "Tubefilter says the mechanism out loud, and it is worth quoting exactly: these stories are harrowing, and often told in a way that's meant to instill wariness and nerves in viewers.  So what better moment to sell them something that claims to protect them?",
                    "The read itself does the rest.  Your data is being sold right now.  My sponsor Aura will find the brokers selling it and remove you automatically.  Thirty minutes into a story about a man living undetected in a family's attic, the viewer is already unsettled.  Every other sponsorship you buy interrupts the mood the content built.  This one finishes it.",
                    "Here is the part that turns an observation into evidence.  A completely unrelated advertiser landed on the same genre from the opposite end of the market.  Tubefilter reported last November that Morgan and Morgan, described there as America's largest injury law firm, runs <mark>an average of 230 pieces of branded content a month on YouTube alone</mark>, and its regular creator partners are concentrated in true crime and sensational news coverage — Law&Crime Network, Levi Nichs, Jay Reed.  Shaul Wolf, its senior director of social and creators, explains the selection rule in one line: if you're a fashion influencer and you're promoting a fashion brand, it makes sense.  But if you're a random creator promoting a law firm, it's really out of context.",
                    "The firm also puts a number on the economics that almost nobody publishes.  It told Tubefilter that <mark>the cost to reach a thousand people on a sponsored video falls by between 30% and 50% over the twelve months after it posts</mark>, because you pay the creator a flat fee once and the views keep arriving for a year.  That is the second half of why this genre works: long, heavy, searchable videos keep getting found, and the price you paid stops moving.",
                    "Now the uncomfortable bit.  Most brand-safety exclusion lists delete true crime by default.  That deletion is usually made in a spreadsheet by somebody who has never watched a minute of it, and for at least two categories it may be removing the best-fitting inventory on the platform.",
                ],
                "numbers": [
                    ("17,876,710", "views on the Aura-sponsored true-crime video, week to 8 September"),
                    ("230", "branded videos a month Morgan and Morgan runs on YouTube alone"),
                    ("30-50%", "fall the firm reports in its cost to reach a thousand people over twelve months"),
                ],
                "flagnote": "The chart data comes from Gospel Stats, a vendor Tubefilter partners with commercially and promotes inside the piece, and the view counts are public YouTube figures, which since late August have started counting the moment playback begins rather than once somebody has watched a stretch of the video.  The 30% to 50% figure is Morgan and Morgan's own unaudited claim, reported by Tubefilter in November 2025 and included here as context rather than as new reporting.  Nobody has published what Aura spends on creator sponsorship, and one third-party scan of sponsor frequency logs Aura mostly against personal finance channels rather than true crime, so treat the genre fit as a mechanism to test rather than a proven strategy.",
                "so_what": "Fit is not about whether the creator's audience matches your customer.  It is about whether the emotional state the content produces is the one your product resolves.  A true-crime video manufactures unease for half an hour and then hands the microphone to a company that sells the end of unease, which is a far tighter join than any lifestyle placement gets.  It also explains how a law firm and a data-removal service, with nothing else in common, arrived independently at the same shelf.",
                "do_this": "Open your brand-safety exclusion list this week and find out who blocked true crime and when.  If you sell security, insurance, legal services, identity protection, home monitoring or anything else people buy because they are worried, fund one test placement in the genre and measure it against your best lifestyle placement over ninety days rather than thirty.",
            },
            {
                "title": "YouTube asked people what everyone is into now, and creators came within two points of Hollywood",
                "hook": "Creators 77.  Memes 78.  Hollywood celebrities 79.  The Super Bowl 83.",
                "stamps": [("YOUTUBE BLOG · 10 SEP", "https://blog.youtube/culture-and-trends/youtube-culture-trends-modern-mainstream-research/")],
                "body": [
                    "YouTube's Culture and Trends team published research with the agency NRG this morning, under the title In Search of Mainstream.  Asked what lots of people seem to be into nowadays, respondents put <mark>YouTube creators at 77% and memes at 78%, against Hollywood celebrities at 79% and the Super Bowl at 83%</mark>.",
                    "Say the obvious thing before anyone builds a deck slide out of it.  Creators did not overtake Hollywood.  Celebrities are two points ahead and the Super Bowl is six ahead, and the sample for that question is 496 people, so the honest reading is parity inside the noise.  Parity is still the story.  Five years ago nobody would have put those four things on the same axis at all.",
                    "The more useful numbers come from a second, larger sample in the same study.  <mark>65% agree that something feels more real or legitimate when they see it show up on YouTube.</mark>  73% say YouTube is the best place to deeply explore their personal interests.  72% say they stay interested in things long after discovery because of YouTube.",
                    "Those two sets of numbers are doing different jobs, and it is worth separating them.  The first set measures recognition: does everyone else know about this?  The second measures legitimacy: does this feel real to me?  With enough money you can buy recognition in a single weekend.  Legitimacy is not on sale at any price, and that 65% figure is describing where people go to check.",
                    "The case study YouTube attaches to it is instructive on scale.  Kane Parsons started posting found-footage horror shorts to YouTube as a teenager; the first one has drawn over 90 million views, and the A24 film adaptation opened to 118 million dollars globally.  The channel was not the marketing for the film.  It was the thing that made the film worth making.",
                ],
                "flagnote": "This is YouTube's own research about YouTube, published by YouTube.  The survey is United States only and runs on two separate samples fielded in April 2026 — the 77, 78, 79 and 83 comparison comes from 496 respondents aged 14 to 29, while the legitimacy and interest figures come from 939 respondents aged 14 to 44.  The exact survey question is not published, only YouTube's paraphrase of it, and the metric is perceived wide recognition rather than preference or importance.  The 90 million view figure is YouTube's own lifetime data and the 118 million dollar opening is cited by YouTube in the same post.",
                "so_what": "Most brand video briefs quietly assume one job — get this in front of more people.  This study describes a second job, one that plenty of budget already pays for by accident and nobody measures.  When somebody hears about your product in an ad and then goes to YouTube before buying, that YouTube video is not a second impression.  It is the verdict, and it is the only part of your marketing the customer can go and check for themselves.",
                "do_this": "Take the one thing you are launching this quarter and write down, in a sentence, whether the video's job is to make it known or to make it believable.  If the answer is believable, move that money to depth — longer, more specific, more searchable — and brief it to be found by someone who is already looking rather than shown to someone who is not.",
            },
        ],
    },
    {
        "id": "ls", "name": "L'S", "page": "pg. 03",
        "note": "what broke, and the failure mode underneath it",
        "tint": "pink",
        "items": [
            {
                "title": "Wrong owner: Wimbledon will not create a creator credential, and the numbers used to justify creator credentials were earned without one",
                "hook": "The US Open went from about 50 creators to 100.  Wimbledon posted 144 million engagements in a season without a single one.",
                "open": True,
                "stamps": [
                    ("NET INFLUENCER · 10 SEP", "https://www.netinfluencer.com/wimbledon-rules-out-influencer-accreditation-following-us-open-disruptions/"),
                    ("TUBEFILTER · 9 SEP", "https://www.tubefilter.com/2026/09/09/sports-influencer-backlash-us-open-wimbledon-tennis-nfl/"),
                ],
                "body": [
                    "Wimbledon will not create an accreditation category for influencers or content creators.  The decision surfaced this week after a US Open in which the accredited creators became the story rather than the coverage.",
                    "The USTA's programme credentialed roughly 50 creators when it launched in September 2025, across food and drink, lifestyle, entertainment, fashion and family content, and <mark>expanded to 100 for this year's tournament</mark>.  Two improperly credentialed creators had their passes revoked.  Ring lights went into the stands.  Aryna Sabalenka paused a third-round match over what she described as a very strong smell of marijuana.  Adrian Mannarino put it hardest: people are allowed to move around in the crowd during points.  The tournament puts up with it, and I don't know if it's the best thing for tennis in general.  There's a smell of marijuana on the court, noise everywhere.  The truth is it's turning into a bit of a zoo.",
                    "Here is the detail that turns this from a manners story into a business one.  When the USTA launched the programme in September 2025, Jonathan Zipper, who runs its social media, cited Wimbledon as the model — pointing to a season in which <mark>Wimbledon's channels generated 144 million engagements, up 26%, and 2.7 billion video views, up 71%, while growing its social audience by 2.3 million to 23.5 million</mark>.  Wimbledon produced every one of those numbers with no creator accreditation category at all.",
                    "So the benchmark that justified handing out 100 credentials was set by a tournament that hands out none.  The All England Club's conditions of entry already prohibit anything that could disturb play, ring lights included, and it reviews its social policies annually.",
                    "The other half of the market went the opposite way in the same week, which is what makes this a failure of ownership rather than a verdict on creators.  The NFL's Creator of the Week programme is back for 2026, TikTok has announced a full slate of NFL partnerships, and YouTube put creators inside the season opener.  Football wants them.  Tennis has decided it does not.",
                ],
                "flagnote": "The Wimbledon decision is reported without a named official and without a stated year, and the underlying account is ESPN's.  The 144 million engagement figure describes Wimbledon's own channels over an unspecified season and was cited by the USTA in September 2025, so it predates this year's tournament.  The two revoked US Open passes were revoked for being improperly credentialed, not for disrupting play — those are two separate strands of the same story and the reporting does not join them.",
                "so_what": "Almost everything in a sports plan has a substitute you can find in a fortnight.  Access does not, and it is the one element you do not own.  Lose the talent, the crew or the edit and you rebuild.  Lose the credential and there is nothing to shoot.  And the awkward fact underneath the whole episode is that the tournament everyone held up as proof that this works had never bought it in the first place.",
                "do_this": "For every 2027 sports plan on your board, write down who issues the credential, what would cause them to withdraw it, and what you would shoot instead if they did.  Get the access named in the contract this quarter rather than assuming standard media accreditation covers a creator with a camera.",
            },
            {
                "title": "Wrong brand: the loudest apparel campaign of the summer is attached to the division that shrank",
                "hook": "Aerie comparable sales up 19%.  American Eagle down 1%.  Same company, same quarter, same building.",
                "stamps": [("MODERN RETAIL · 9 SEP", "https://www.modernretail.co/operations/aerie-soars-in-back-to-school-sales-while-american-eagle-works-to-balance-denim/")],
                "body": [
                    "American Eagle Outfitters reported this week.  Total net revenue was <mark>1.38 billion dollars, up 8%</mark>, alongside a 196 million dollar tariff refund including interest.  Underneath that headline sit two very different businesses: <mark>Aerie comparable sales up 19%, American Eagle comparable sales down 1%</mark>.",
                    "American Eagle's back-to-school campaign launched on 22 July as a ten-week effort — Sydney Sweeney, the country singer Ella Langley, the footballer Lamine Yamal, mall events, campus partnerships and five sorority chapters making rush content.  It was, by a distance, the most discussed apparel marketing of the summer.",
                    "Be precise about what the minus one measures, because a lot of people this week will not be.  The campaign launched roughly ten days before the quarter closed.  The minus one is almost entirely pre-campaign.  It is not the campaign's result.  It is the hole the campaign was hired to fill.",
                    "The campaign's actual result sits in the guidance, and the guidance is modest.  For the quarter that does contain the campaign, the company expects comparable sales <mark>relatively flat at American Eagle, and in the high teens to 20% at Aerie and its sister label Offline</mark>.  Jennifer Foyle, the company's president, on the denim work: we are moving in the right direction, yet there remains work to do.",
                    "Meanwhile the division growing 19% ran something far quieter.  Aerie Realmakers, a creator programme that debuted in April with an explicit stipulation that participants use no AI, nearly doubled its ambassador roster during the quarter.  No celebrity, no launch moment, no discourse.",
                    "Two honest caveats before anyone runs with this.  These are different categories with different demand curves — denim and intimates do not move together — so it is not a controlled test.  And American Eagle was fixing a real inventory problem, not just a marketing one.  What the numbers do give you is unusually clean conditions: one company, one quarter, one set of economic conditions, two marketing approaches, twenty points apart.",
                ],
                "so_what": "Attention arrives the week you launch.  Demand shows up a quarter later, by which point the team has moved on, so the conversation ends up being the only evidence anyone actually looks at.  The conversation is not in these numbers.  What is in them is that the division nobody wrote about grew nineteen percent while running an always-on creator programme with no talent fee attached, and the division everybody wrote about is guided to flat.  That is not proof the celebrity money was wasted.  It is the comparison your finance director is going to make anyway.",
                "do_this": "Put a date in the calendar now for the week after your current campaign's quarter reports, and write down today the single number you will judge it on.  Go back and look on that date whether or not anybody asks you to.",
            },
        ],
    },
    {
        "id": "moves", "name": "MOVES", "page": "pg. 04",
        "note": "platform, policy and money changes that alter what you can buy",
        "tint": None,
        "items": [
            {
                "title": "Amazon's ad buying tool went live inside ChatGPT this morning",
                "hook": "A pilot, a handful of US advertisers, and one named brand.  The fee comparison is the story.",
                "stamps": [("DIGIDAY · 10 SEP", "https://digiday.com/media-buying/amazon-brings-its-dsp-to-openais-chatgpt-ads-extending-its-supply-chasing-streak/")],
                "body": [
                    "From today, advertisers using Amazon Ads can buy placements inside the ChatGPT app.  It is a pilot, limited to selected US advertisers, and <mark>Delta Vacations is the only brand named</mark>.  Seb Joseph reported it at Digiday this morning.",
                    "The competitive detail is the pricing.  Buying tools like these take a cut of whatever an advertiser spends through them.  Digiday's read is that Amazon already undercuts rivals there, its own cut often landing near zero on deals where the inventory is guaranteed in advance, against <mark>The Trade Desk's historical 15 to 20%</mark> of spend, or Google's similar slice.  Note the hedges — often, near zero, and only on guaranteed deals.  That is not a claim about everything Amazon sells.",
                    "OpenAI has already connected Criteo and StackAdapt and cut deals with the major agency holding companies.  It started testing ads in February and is <mark>reportedly aiming at 100 billion dollars of ad revenue by 2030</mark>, a target Digiday calculates would need compound growth above 200% a year.",
                    "Chris Conetta, director of omnichannel supply at Amazon Ads, gives the pitch: conversational ads represent the fastest growing engagement opportunity for brands to reach new and existing audiences.  Nate Elliott, principal analyst for AI at eMarketer, gives the counterweight: it'd be overly generous to call Q4 a stress test for OpenAI's ad business.  They're still trying to build out even many of the basics of a functional ad sales operation, including their team, technology, vendor partnerships, ad formats, and pricing.",
                ],
                "so_what": "Most of the ad markets that ended up mattering started roughly like this, with a pilot, one named brand and measurement nobody would defend.  What makes this one move faster than usual is that the demand side is already plumbed in — if your agency buys Amazon, it can buy this without a new contract, a new vendor or a new approval.  The friction that normally slows a new channel down for two years is missing.",
                "do_this": "Ask your media agency this week whether your Amazon buying is set up in a way that could extend into ChatGPT, and if it is, agree in advance what you would need to see reported before you spend a dollar there.",
            },
            {
                "title": "YouTube turned live reactions on by default, and the views land in your report",
                "hook": "Someone can now go live over your sponsored stream, earn from it, and none of the revenue is shared.",
                "stamps": [("YOUTUBE HELP — FEATURE EXPERIMENTS · 3 SEP", "https://support.google.com/youtube/thread/18138167?hl=en&msgid=464758566")],
                "body": [
                    "TeamYouTube posted this to its feature experiments thread on 3 September and it has only reached the trade press this week.  Eligible mobile creators get a React live button in the share panel of another creator's stream.  Tapping it broadcasts their reaction alongside the original.  The phone camera locks horizontal and cannot be switched off.",
                    "Two mechanics matter if you sponsor livestreams.  First, revenue: the reacting creator earns as normal on their reaction, and <mark>revenue from reactions is not shared</mark> with the person whose stream they are reacting to.  Second, measurement: <mark>the concurrent viewership, public views and watch time from all the reactions are attributed back to the source content</mark>.",
                    "Read that second one twice.  If you buy a live integration and somebody talks over it to their own audience, those viewers count toward the number your partner reports to you — and some of them never saw your integration, they saw a face in the corner talking about it.",
                    "The default is on.  YouTube's wording: by default, eligible streams are opted in to allow other creators to react.  Opting out is not retroactive.  You update the app, then change the React live setting in the mobile metadata editor from Allow eligible channels to No one, before going live.",
                ],
                "flagnote": "The primary source is YouTube's own feature experiments thread, dated 3 September, not a blog post — some coverage this week has attributed it to blog.youtube, which does not carry it.  YouTube publishes no eligibility criteria, no geography and no size for the experiment group, and no timing for a wider rollout.",
                "so_what": "This is the third change in a month that makes a creator's reported audience bigger without making your integration reach more people.  Public view counts now start at the first frame.  A private co-viewing estimate multiplies a TV playback by however many people YouTube guesses are on the sofa.  And now the audience watching somebody else react to a stream is credited back to the stream.  None of the three is dishonest, and all three land on the same side of the negotiation.  The reaction attribution is the sharpest of them, because it is the only one where the extra viewers were demonstrably watching something other than your integration.  The counter is engaged views, the figure YouTube itself pays creators on, which only counts somebody who actually watched rather than somebody the video merely loaded for.",
                "do_this": "Add one line to every live sponsorship brief: the creator turns the React live setting to No one before going live, and reports engaged views, the paid-on figure, rather than the public view count.  Send it to any partner streaming for you in the next fortnight, because the setting has to be changed before the stream starts.",
            },
            {
                "title": "TikTok moved creator videos onto physical screens across Europe, and one UK network alone has more than 4,500 of them",
                "hook": "Your talent contract almost certainly does not cover a screen in a shopping centre.",
                "stamps": [("NET INFLUENCER · 10 SEP", "https://www.netinfluencer.com/tiktok-expands-ad-placements-across-europe-launches-newsletter-to-grow-livestreaming/")],
                "body": [
                    "TikTok added six partners to its Out of Phone product across the UK, France, Belgium, Spain and Italy — Alight Media, DooH it, Powerpill, Zoom Media, Next-Gen Media and C-Screens.  The product puts organic creator content on physical screens, and advertisers can sponsor that content or extend an existing TikTok campaign onto the screens.",
                    "The reach claims, all from the partners: <mark>Alight Media carries it across more than 4,500 digital screens in over 1,000 UK venues</mark>.  Zoom Media's fitness screens claim more than 500 gyms and over 4 million monthly UK viewers.  Next-Gen Media covers more than 500 screens in UK and Irish student housing and claims over 16 million daily impressions.  Powerpill reports a 17% average lift in engagement and dwell time across more than 150 active screens in Italy.",
                    "Jade Walton, TikTok's director of business development for global media and licensing partnerships: we created Out of Phone to bring the creativity and joy of TikTok off platform and into the real world.",
                    "Separately, TikTok launched a newsletter for its live creators and put a number on that population — <mark>more than 250 million creators went live globally in 2025, and more than 150 million earned rewards for doing so</mark>.",
                ],
                "flagnote": "Every audience figure here is supplied by the screen network selling the placement, with no third-party verification and no stated measurement method.  Powerpill's 17% lift is a vendor claim with no sample or comparison group published.",
                "so_what": "The interesting problem is not the media, it is the paperwork.  Standard creator usage rights are written for social feeds, and a screen in a supermarket is not a social feed.  If a brand extends a campaign onto these networks using footage a creator made, and the contract says social media, somebody has just used that person's face in out-of-home without buying it.",
                "do_this": "Pull your three most recent creator contracts and check whether the usage clause names out-of-home or physical screens.  If it does not, add the wording to your template this week and price it as a separate line rather than discovering it after a campaign has run.",
            },
            {
                "title": "IMDb added a Digital Creator category and dropped the requirement for a film or TV credit",
                "hook": "Streamer, vlogger, video essayist, video creator, gaming creator, influencer.  Six professions, no screen credit needed.",
                "stamps": [("VARIETY · 9 SEP", "https://variety.com/2026/digital/news/imdb-digital-creator-profiles-1236855930/")],
                "body": [
                    "Amazon-owned IMDb has opened Digital Creator as a professional category on IMDb and IMDbPro, available for the first time to people with no traditional film or television credit.  Six sub-professions, and a creator can hold several at once.  It is currently limited to IMDbPro Premium members, and IMDb is marking it with an invite-only industry event at the Toronto festival on 14 September.  Todd Spangler filed the original at Variety yesterday morning.",
                    "Nikki Santoro, chief executive of IMDb, names the audience for it directly, and it is not fans: digital creators and their representatives need that same infrastructure, and producers, casting directors, studio executives and <mark>brand partners</mark> need a reliable way to find them.",
                ],
                "so_what": "Read this next to the live reactions item above and it stops being a filing-cabinet story.  Every number a platform gives you about a creator is currently getting bigger for reasons that have nothing to do with that creator, and the only durable record of what somebody is worth is what they have actually made.  A profile built for casting workflows indexes on the work.  Follower count, which is the field every existing tool exposes because it is the easy one, indexes on the number that is being inflated.",
                "do_this": "If you brief talent teams or vet creators for anything with production or usage-rights implications, get one person a Premium seat and run your next shortlist through it alongside your usual tools, then compare which method surfaced the better candidates.",
            },
        ],
    },
    {
        "id": "onstream", "name": "ON STREAM", "page": "pg. 05",
        "note": "live audiences, and what the numbers actually measure",
        "tint": None,
        "items": [
            {
                "title": "Valorant's season got 3% more watch time and nearly a fifth fewer viewers, and Twitch now carries under half of it",
                "hook": "218 million hours watched.  Peak viewers down 18.7%.  Airtime up 24.5%.",
                "open": True,
                "stamps": [("ESPORTS CHARTS · 9 SEP", "https://escharts.com/news/vct-2026-vs-2025-viewership-comparison")],
                "body": [
                    "Esports Charts published the full-season comparison for the Valorant Champions Tour yesterday.  <mark>More than 218 million hours watched in 2026, up 3.1% year on year.</mark>  Average viewers <mark>fell 17.4%</mark>.  Peak viewers <mark>fell 18.7%</mark>.  Airtime rose 24.5%.",
                    "Esports Charts explains it without being asked, which is to its credit: the increase in hours watched was largely driven by a 24.5% rise in airtime, because Stage 2's expanded format pulled Challengers teams through the play-ins and added teams and matches.  More hours of broadcast, multiplied by a smaller audience, produced a slightly bigger total.  Hours watched went up.  The audience went down.",
                    "For scale, put it against something.  Twitch's own report last week counted 8.6 billion hours of gaming watched on the platform between 1 January and 1 September.  An entire global season of one of the biggest esports leagues in the world is therefore <mark>about two and a half percent</mark> of the gaming watched on one platform over eight months.  Esports numbers sound enormous in isolation and normal in context.",
                    "The part nobody will lead with is where the audience went.  <mark>Twitch carried less than half of the season's hours watched, and Kick went from 0.2% of them in 2025 to 4.6% in 2026</mark> — more than twenty times its share in a single season.  The audience did not grow.  It relocated.",
                    "Language tells the same story of redistribution rather than growth.  Japanese hours up 24.6%, Portuguese up 20.7%, English down about 3%, Korean down 16%, Spanish down 23.9%.",
                ],
                "flagnote": "Esports Charts publishes peak and average viewers for this comparison as percentage changes only, with no absolute figures, so the size of the audience at its biggest cannot be checked from the source.  Community and co-stream channels are included in the platform mix, which is part of why the channel distribution moved.",
                "so_what": "Airtime is the variable that quietly inflates every livestream number you are shown.  Add matches, add a play-in round, add co-streamers, and hours watched rises while the actual audience shrinks — and hours watched is the figure that goes in the deck, because it is the only one that went up.  The platform shift underneath is the more useful signal.  Twitch now carries under half of a season it used to dominate, and Kick has gone from a rounding error to 4.6% of it in twelve months, so a Twitch-only gaming plan reaches a measurably smaller slice of this audience than it did last season.",
                "do_this": "Make peak viewers, average viewers, airtime and channel count a standing requirement on every livestream proposal you receive, and reject any number given as hours watched alone.  For gaming buys this quarter, price a Kick line into the plan and see what it costs before you assume it is not worth having.",
            },
        ],
    },
    {
        "id": "watch", "name": "ONE TO WATCH", "page": "pg. 06",
        "note": "one creator with momentum, and who should be calling them",
        "tint": None,
        "items": [
            {
                "title": "Mr Carlson's Lab did ten times its own median views by settling an argument about components, and carries no sponsor at all",
                "hook": "539,000 subscribers.  A 731,651-view breakout at ten times his median.  No sponsor on any recent upload.",
                "open": True,
                "stamps": [("YOUTUBE CHANNEL", "https://www.youtube.com/@MrCarlsonsLab")],
                "body": [
                    "Mr Carlson's Lab is a one-man electronics bench channel with <mark>539,000 subscribers</mark>, read from YouTube this morning.  For most of its life it has been a slow, beloved vintage radio restoration channel — thirty to fifty minute repairs, filmed at one bench, watched by people who genuinely care about capacitors.  That format still runs and it still does about 40,000 views: the DeWald radio restoration in April did 37,809, the capacitor bench session in July did 45,931.",
                    "Something else started working.  On 24 August he posted a seventeen-minute video called Why Put Diodes Together In Both Directions.  It has done <mark>731,651 views</mark>.  The median across his last ten long-form uploads is <mark>72,680</mark>, so that is a shade over ten times his own middle, and his biggest video ever.",
                    "The reason to pay attention is that it is not one lucky video.  It is the fourth step of a trend on the same new format — short, argumentative, one component, one contested claim, one definitive answer.  Track the ceiling on that format: about 76,000 views on which capacitor to buy, about 108,000 on a wiring question, <mark>379,981 on the best cable for audio in June</mark>, then 731,651 on diodes in August.  Four points, all upward, while the restoration videos hold flat at about forty thousand.",
                    "What changed underneath is commercially more interesting than the numbers.  He has moved from restoring old radios to adjudicating buying arguments — speaker wire, cable quality, which capacitors are worth the money, which tubes hold their value.  He is becoming the person who settles it, in a category where people spend enormous sums on contested claims and nobody neutral ever measures anything.",
                    "And there is no sponsor.  Not on the breakout, not on the four before it, no promo code, no affiliate link, no gifted product.  He funds it through his own courses, circuit designs and forum.  A creator with a 730,000-view video and no commercial partner attached to any of it.",
                ],
                "watch": {
                    "label": "TOP VIDEO, LAST 3 MONTHS",
                    "title": "Why Put Diodes Together In Both Directions? Explained With Examples!",
                    "url": "https://www.youtube.com/watch?v=SjOxBg6SJuw",
                    "meta": "731,651 views · published 24 August 2026 · 17m 49s",
                    "note": "Seventeen minutes, one component, one question people argue about, and a bench meter settling it.",
                },
                "flagnote": "No publication has covered this channel.  The subscriber count, the view counts and the median of the last ten long-form uploads were read from YouTube's own public data on 10 September rather than from a third-party tracker, and Shorts were excluded from the median.  The featured video link was confirmed to resolve.  Sponsor status is based on reading the descriptions of the last five uploads, so an unmarked verbal read inside a video cannot be ruled out, though the absence of any accompanying link makes one unlikely.",
                "so_what": "The thing he sells without knowing it is adjudication.  His format is a claim, a meter and a verdict, and the credibility of the verdict is inseparable from the instrument producing it — which means the buyable placement is not a read at the top of the video, it is the equipment on the bench during the measurement.  For a brand selling test and measurement equipment that is the most persuasive placement available in the category, and on the evidence of his recent uploads nobody has bought it.",
                "do_this": "If you sell oscilloscopes, meters, soldering equipment, bench supplies or components — Rigol, Siglent, Keysight, Fluke, Hakko, JBC, DigiKey, Mouser and everyone competing with them — email him this week and offer to fund a series of measured comparisons using your instrument, with no approval rights over the conclusion.  If you sell cable or connectors and your product genuinely measures well, offer to fund the test that says so and accept the result whichever way it lands.",
            },
        ],
    },
    {
        "id": "money", "name": "THE MONEY", "page": "pg. 07",
        "note": "where the spend is actually going",
        "tint": None,
        "items": [
            {
                "title": "Buyers cut their use of AI to make ads by nine points, and made being found by AI their number one priority",
                "hook": "Generative AI in campaigns down from 78% to 69%.  Optimising content for AI answers up to 76% and first on the list.",
                "open": True,
                "stamps": [("IAB — 2026 OUTLOOK, SEPTEMBER UPDATE", "https://www.iab.com/insights/2026-outlook-study-september-update/")],
                "body": [
                    "Inside the same IAB study that carries today's lead, there is a reversal nobody predicted.  Asked whether they use generative AI in campaigns, <mark>69% said yes, down from 78% in January</mark>.  Eight months, nine points, in the wrong direction for every assumption in the industry.",
                    "In the same eight months, <mark>optimising content for AI answers became the biggest area of increased focus overall, at 76%, well clear of any individual ad type</mark>.  Adapting to AI-driven search is the top challenge buyers name, at 44%.  Concern about low-quality AI content sits at 38%.  And <mark>86% say they are changing, or expect to change, how they measure within twelve months because of conversational AI</mark>, with 45% naming the comparison between AI and traditional customer journeys as the hardest measurement problem they have.",
                    "Put those together and the direction is unambiguous.  The money moved from using a machine to make the advertising, to making sure a machine repeats what you said.  One of those is a production saving.  The other is a distribution question, and distribution questions are always the bigger ones.",
                    "The rest of the goal mix moved with it.  Customer acquisition jumped nine points since January to <mark>63%</mark> as the top media goal, brand equity rose six to 43%, repeat purchase stayed flat at 24%.",
                ],
                "flagnote": "Same caveats as today's lead: more than 200 brand and agency decision-makers, no field dates, no sample breakdown, no margin of error, published by a trade body whose members sell the inventory.  These are stated intentions rather than audited behaviour, and a nine-point fall in a survey of this size should be read as a direction rather than a precise magnitude.",
                "so_what": "The interesting half of this is what the drop implies about the first wave.  A lot of teams tried generative AI on campaign work in the past year and a meaningful number appear to have stopped.  The survey does not say why, and it is worth resisting the obvious explanations in both directions.  Meanwhile every one of those teams now has a harder problem: their work has to survive being summarised by something that never watched it.",
                "do_this": "Pick your three highest-value products and ask a chatbot what it says about each one, then read the answer as a customer would.  Where it is wrong or empty, commission one long, specific, plainly spoken video or page that gives it something accurate to repeat, and check the answer again in thirty days.",
            },
            {
                "title": "Machines already buy twelve percent of American advertising, and the forecast is twenty-seven by 2030",
                "hook": "Three companies take 60% of North American ad revenue.  One agency thinks automation ends at 90.",
                "stamps": [("DIGIDAY · 10 SEP", "https://digiday.com/media-buying/ad-spend-forecasts-revised-upward-as-more-ad-dollars-are-handled-by-ai-tools/")],
                "body": [
                    "Digiday's round-up of this week's forecast upgrades carries a Madison and Wall figure that is more consequential than the growth numbers everyone is quoting.  The US market is worth roughly 479 billion dollars once political money is excluded, and <mark>AI-run and automated campaigns already account for about 12% of it</mark>.  The firm expects that to reach <mark>158 billion dollars, or 27% of the US market, by 2030</mark>.",
                    "The concentration underneath it is the part to sit with.  Alphabet, Meta and Amazon together take <mark>60% of North American ad revenue</mark>.  Luke Stillman, managing director at Madison and Wall, describes what is happening in four words: this is a share shift.",
                    "John Dawson, vice president of strategy at the agency Jellyfish, puts the ceiling far higher than the forecast does: we don't think automation in media stops at 20% or 30% — we think it gets to 90%.",
                    "Read that against today's lead and the picture resolves.  The market is growing on a one-off calendar of sporting events and an election, the buying of it is being handed to automated systems inside three companies, and the ad type buyers say they are increasing focus on most is creator and influencer work — the part of the market that is hardest to automate, because it involves a person agreeing to say something.",
                ],
                "flagnote": "Madison and Wall's underlying report is subscriber-only, so these figures are as Digiday reports them.  The definition of an AI-run or automated campaign is not published, and it is doing a lot of work — a broad definition would include long-standing automated bidding, a narrow one would not.  Jellyfish sells services in this area.",
                "so_what": "Automated buying converges.  Two competitors handing similar budgets and similar objectives to the same three systems will be shown to overlapping people at similar prices, because the systems are solving the same problem the same way.  What does not converge is the thing being shown, and who says it.  That is the argument for creator work being the ad type buyers are increasing focus on most, and it is a better argument than the one usually given for it.",
                "do_this": "Work out what share of your own media is already bought by an automated system rather than a person, and get the answer in writing from your agency this week.  Whatever the number is, move the equivalent share of your planning time out of buying decisions and into what the machines are being handed.",
            },
        ],
    },
    {
        "id": "format", "name": "FORMAT LAB", "page": "pg. 08",
        "note": "one format, taken apart",
        "tint": None,
        "items": [
            {
                "title": "The brand podcast graveyard: Gucci has not posted since May 2025, Nordstrom has done nearly 120 episodes",
                "hook": "Three luxury houses let their feeds go quiet.  A department store is approaching episode 120.",
                "open": True,
                "stamps": [("GLOSSY · 10 SEP", "https://www.glossy.co/fashion/fashion-briefing-fashion-companies-are-launching-podcasts-to-add-more-depth-to-their-communities/")],
                "body": [
                    "Danny Parisi's fashion briefing at Glossy this morning is unusually useful because it names the failures rather than only the launches.  Hermès shut an experimental podcast in 2021.  Chloé discontinued Chloé Radio.  <mark>Gucci's podcast has not been updated since May of 2025</mark>, after habitually leaving several months between episodes.  Chanel and Dior are still going.",
                    "The counter-example is not a luxury house.  Nordstrom's The Nordy Pod has held a regular release cadence for two years, <mark>put out nearly 120 episodes</mark> and picked up a Shorty Award nomination.",
                    "Whatever killed those three, it was not the budget.  Hermès, Gucci and Chloé can outspend Nordstrom on any line item you care to name, and all three feeds have gone quiet while Nordstrom's approaches its 120th episode.  The thing Nordstrom has that the others did not is a release schedule it has actually held to for two years.",
                    "The new entrant this week is Fashionphile Unboxed, weekly, hosted by chief executive and co-founder Sarah Davis, with the fashion creator Charles Gross in the first episode.  Davis is explicit that the point is shelf life: we talk to so many interesting people, and we make a lot of content, and with social, it feels like it just goes away.  With Reels and other social content, we get a lot of value out of it, but also it disappears so fast.  With the podcast, we wanted to create a catalog that you can discover and really dig into.  Glossy reports she refused to launch without a long-term commitment to the cadence.",
                    "Jack Williams, principal strategist at the consultancy Mackasey, names the failure mode: brands considering starting a podcast should consider creating a content calendar that is varied and deep enough to provide listeners from a variety of different backgrounds and levels of interest in the brand with distinct, compelling entry points.  Translated: a feed that only talks about the brand runs out of guests, and a feed that runs out of guests stops publishing.",
                    "The version that pays for itself belongs to Daydream, an AI-powered fashion shopping app.  Its video podcast The Fashion Stack just wrapped a first season, and Jennifer Koen, its head of marketing and communications, describes it as inventory as much as content: we partner with over 325 fashion brands, and, in addition to offering them another distribution channel, we wanted to be a partner in growing their brand and awareness through co-marketing.",
                ],
                "flagnote": "This is a Glossy member-exclusive briefing.  Success for The Nordy Pod is measured here in episode count and an award nomination — no downloads, no audience figure and no attributed revenue appear anywhere in the piece.  The listening statistics Glossy cites are attributed to Riverside, a podcast software company, with no study title, date or sample published.  Gucci's feed is described as dormant rather than cancelled.",
                "so_what": "An owned series fails on supply, not on demand.  Episode one is easy because you have the best guest, the best story and everyone's attention.  Episode fourteen is where it dies, because nobody worked out in advance who else there is to talk to, and a luxury house with a small approved-spokesperson list runs dry faster than a retailer that can talk to anyone who works there.  The commitment being tested is not budget.  It is whether you can name the next twelve guests today.",
                "do_this": "Before you greenlight any owned series, write down the first twelve guests or episode subjects by name and get them approved in the same meeting as the budget.  If you cannot fill the list, commission a season of six and say so publicly, rather than launching something open-ended that quietly stops.",
            },
        ],
    },
]

FORECAST = [
    {
        "confidence": "LIKELY",
        "window": "by 31 March 2027",
        "headline": "The 2027 budget conversation gets ugly, because 2026's growth was a calendar",
        "body": "Two forecasters raised the US ad market this week on the back of a Winter Olympics, a World Cup and an American election cycle, and the same firm with the highest 2026 number has 2027 at 4.1%.  Every marketing team that plans against this year's growth rate is going to walk into a room in January and be asked why their number assumes a repeat of three events that do not repeat.  The teams that separate cyclical money from underlying demand now will spend that meeting explaining a plan.  The rest will spend it defending one.",
        "do": "Split this year's performance into cyclical and underlying before anyone asks you to, and bring both numbers to the first 2027 planning meeting.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "by 30 June 2027",
        "headline": "Creator access at sports events becomes a paid contractual line rather than a media credential",
        "body": "Wimbledon has declined to create a creator accreditation category, the US Open revoked passes and doubled its cohort in the same year, and the property everyone cited as the model built its numbers without a programme at all.  Meanwhile the NFL is expanding creator access aggressively.  When two rights holders in the same sport move in opposite directions, the market usually resolves it by pricing the thing — which means access stops being something a communications team requests and becomes something a commercial team buys, with terms, exclusivity and a cancellation clause.",
        "do": "Ask your biggest sports rights holder what a guaranteed creator access package would cost, even if you have no intention of buying one this year, so you know the number before you need it.",
    },
    {
        "confidence": "LIKELY",
        "window": "by 31 December 2026",
        "headline": "Engaged views becomes standard contract language for creator deals",
        "body": "In one month YouTube has moved public view counting to the first frame, introduced a private co-viewing estimate it tells creators to use in negotiations, and switched on third-party live reactions whose audience is attributed back to the source stream.  Every one of those changes makes the number a seller quotes larger without making your integration reach more people.  Buyers do not have to win an argument about any of them individually — they only have to write one metric into the contract, and engaged views is the one YouTube itself uses to pay creators.",
        "do": "Add engaged views as the reported metric to your creator contract template this month, and make the next deal you sign the first one that uses it.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "by 30 June 2027",
        "headline": "Threat-adjacent content stops being a brand-safety exclusion and starts being a targeting category",
        "body": "A data-removal service put a sponsor read on a true-crime video that did nearly 18 million views, and the largest personal injury firm in America independently concentrated its creator partners in the same genre.  Two advertisers with nothing in common found the same shelf, and the reason is that the content produces the emotional state their product resolves.  As soon as one measurement vendor publishes a genre-level performance cut showing this, the exclusion lists start coming apart, and whoever got there first will have spent that whole period buying attention nobody else was bidding against.",
        "do": "Audit which content categories your brand-safety list blocks and why, and identify the one exclusion you would reverse first if the performance data supported it.",
    },
]

TLDR = [
    "The IAB raised its 2026 US ad growth forecast to 12.3% and Madison and Wall raised its US number to 15.6%, but the growth is a Winter Olympics, a World Cup and an American election, and the same firm forecasts 4.1% for 2027.  Rebuild your 2027 budget line on the number that excludes political and cyclical money before your next planning meeting.",
    "A data-removal service sponsored a 34-minute true-crime video that did 17,876,710 views, and a personal injury firm running 230 branded videos a month independently concentrated its partners in the same genre because the content manufactures the feeling the product resolves.  Review who blocked true crime on your brand-safety list, and fund one test placement if you sell anything people buy out of worry.",
    "Aerie's comparable sales rose 19% while it ran a quiet always-on creator programme, and American Eagle fell 1% in the same quarter at the same company, with the celebrity back-to-school campaign guided to flat.  Diary the week after your current campaign's quarter reports and write down today the one number you will judge it on.",
    "YouTube turned third-party live reactions on by default, and the reaction stream's views, watch time and concurrent viewers are attributed back to your sponsored content while none of the revenue is shared.  Put the opt-out instruction and an engaged-views reporting clause in every live sponsorship brief this week, because the setting must be changed before going live.",
    "Valorant's season posted 218 million hours watched, up 3.1%, while average viewers fell 17.4% and peak fell 18.7% on airtime up 24.5%, and Kick went from 0.2% to 4.6% of the hours watched.  Require peak, average, airtime and channel count on every livestream proposal, and price a Kick line into your next gaming buy.",
    "Buyers cut generative AI use in campaigns from 78% to 69% since January while making optimisation for AI answers their top focus at 76%, and 86% expect to change measurement within a year because of conversational AI.  Ask a chatbot about your three biggest products this week and commission accurate long-form content wherever the answer is wrong.",
    "Hermès, Chloé and Gucci have all let brand podcasts lapse while Nordstrom has published nearly 120 episodes in two years, so the variable is cadence commitment rather than budget.  Name your first twelve episodes and guests in the same meeting that approves the money, or commission a fixed season of six instead.",
]

SHARE = [
    {
        "who": "JARED · CEO",
        "angle": "The ad market's upgrade is a calendar artefact, and the same forecaster's number for next year is a quarter of it.",
        "post": "Two forecasters raised their US ad market projections in the space of 24 hours this week. The higher of the two, Madison and Wall, now has 2026 growing 15.6%.\n\nThe same firm has 2027 at 4.1%.\n\nThat gap is the whole story and almost nobody is going to put it in a deck.\n\nWhat produced 2026: a Winter Olympics, a FIFA World Cup and an American election cycle. The IAB names the first two directly in its release this morning when it raised its own forecast to 12.3%. Madison and Wall says plainly that its US figure includes political advertising. Digiday reports the same firm's global growth at 9.8% once political money comes out.\n\nSo the market did not get healthier. The calendar got busier.\n\nI think this cuts the opposite way to how it will be read. If your growth this year came from a crowded calendar rather than from demand, then the thing worth funding is the asset that keeps working when the calendar empties. Owned video, a channel, a series, the things that are still there in a quiet year.\n\nThe brands that will struggle in 2027 are the ones that spent 2026 renting attention at the exact moment it was most expensive, and have nothing left over.\n\nI would rather build the thing that does not care what year it is.",
        "why": "It takes an upgraded forecast, which everyone will read as good news, and turns it into an argument for funding owned assets before the cyclical money disappears.",
    },
    {
        "who": "JAMES · CREATIVE DIRECTOR",
        "angle": "The most-discussed campaign of the summer sat on the division that shrank, and the quiet creator programme sat on the one that grew 19%.",
        "post": "American Eagle Outfitters reported this week. Aerie comparable sales up 19%. American Eagle comparable sales down 1%.\n\nSame company. Same quarter. Same economy.\n\nAmerican Eagle ran the most talked-about apparel campaign of the summer: Sydney Sweeney, Ella Langley, Lamine Yamal, mall events, five sorority chapters. Aerie ran a creator programme called Realmakers that debuted in April, roughly doubled its ambassador roster, and generated no discourse whatsoever.\n\nI want to be fair about the numbers. The campaign launched about ten days before the quarter closed, so that -1% is not its result. And denim and intimates are different businesses with different problems.\n\nBut here is what I cannot get past.\n\nI would have been in the room arguing for the celebrity version. I would have argued it well. And the argument I would have made, that this gets us talked about, is the part these figures say nothing about either way.\n\nWe grade our work on the conversation because the conversation arrives in week one and the number arrives in month four, by which point everyone has moved on to the next thing.\n\nI do not know how to fix that in a client meeting. The quarter that actually contains this campaign is guided to flat, and I intend to go back and look at it in December, which is not something I have historically been good at.",
        "why": "A creative director admitting he would have argued for the loud version, and that the industry grades itself on discourse because the real number arrives too late, is uncomfortable and specific.",
    },
    {
        "who": "LAWRY · LEAD VIDEO EDITOR",
        "angle": "Where the sponsor read sits on the timeline is a media decision, and it gets made by an editor nobody thought to ask.",
        "post": "The most valuable decision in a sponsored video is which minute the sponsor speaks on. It gets made in an edit suite, by whoever is cutting, and nobody asks them about it.\n\nA 34-minute true crime video did 17,876,710 views last week. The sponsor was Aura, which removes your details from data broker lists. Tubefilter's read on why it works: the story is built to make you wary, and the sponsor sells the end of being wary.\n\nThat only pays if the read is late. At 45 seconds the viewer has not felt anything yet, they are still deciding whether to stay. The same copy, placed after half an hour of a man living undetected in a family's attic, is a different advert entirely.\n\nEditors move reads constantly, and we justify it as craft. You need a breath to cut out of, and a tense sequence does not hand you many. You need two or three seconds on the other side to get back in without it landing like a jump cut. So the read drifts to where the edit can carry it.\n\nWe call that pacing. It is closer to a buying decision, made on a timeline, by the only person who has watched the whole thing at full length.\n\nThe brief normally arrives with the timecode already on it, written by somebody who has not seen a frame.",
        "why": "A craft observation that reframes sponsor placement as a media decision, made from inside the timeline by the person least likely to be consulted about it.",
    },
]
