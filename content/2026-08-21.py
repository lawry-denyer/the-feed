# -*- coding: utf-8 -*-
"""Content for THE FEED — issue data only.  The render spec lives in build_feed.py."""

ISSUE = {
    "date_iso": "2026-08-21",
    "kicker": "Crux Media // Friday 21 August 2026",
    "tagline": "What brands did on YouTube yesterday, and whether it worked.",
    "pace": "STEADY",
    "next_drop": "Next drop: Monday, 06:30 MT",
}

LEAD = {
    "headline": "BRANDS ARE HANDING CREATORS C-SUITE TITLES WHILE THEIR OWN CREATOR TEAMS TOP OUT AT MANAGER",
    "deck": "Digiday reported this morning that eyewear brand Blenders made Jordan Howlett its chief content officer, on a multi-year deal the CEO says is the biggest the company has ever signed.  Four days earlier, a staffing study found that fewer than 1% of the people doing creator work inside the largest packaged goods companies hold a VP title.  Both things are true at once, and that is the story.",
    "stamps": [
        ("DIGIDAY · 21 AUG", "https://digiday.com/media/for-brands-the-creator-ambassador-is-becoming-a-creator-executive/"),
        ("LINQIA REPORT", "https://www.linqia.com/cpg-influencer-staffing-report/"),
        ("NET INFLUENCER · 17 AUG", "https://www.netinfluencer.com/cpg-brands-have-built-out-influencer-teams-but-few-reach-leadership-level-research-finds/"),
    ],
    "body": [
        "Start with what Blenders actually bought.  Jordan \"The Stallion\" Howlett has around 50 million followers across platforms.  The San Diego eyewear company did not book him for three posts.  It gave him the title chief content officer, a multi-year deal, and input on how the brand makes things.  <mark>CEO Jack Gray's line is the whole argument: \"I don't necessarily believe in renting a customer or renting culture.\"</mark>",
        "The first thing Howlett did with the job is the part worth stealing.  He walked into a Blenders store and told a store associate with barely 100 followers to film him shopping.  The video is the associate throwing the glasses around the shop to show they do not break.  It has close to 200,000 views on Instagram.  Nobody storyboarded that.  A creator with an internal title had the authority to make a staff member the camera operator, and it outperformed things the brand paid an agency for.",
        "He also spent a full day shooting in one of their stores and then binned all of it, because it did not feel right.  That is not a creator behaving like talent.  That is a creator behaving like someone who owns the output.",
        "Now the other number.  Linqia went through LinkedIn and found 152 roles tied to creator work across the biggest packaged goods companies — a set representing more than 700 brands and over $20 billion of advertising spend.  <mark>Manager level is 34% of those roles.  VP is 1%.  \"Head of\" is another 1%.</mark>  Unilever has the most in the United States at 32 roles.  Several companies have fewer than five.  Half the companies have hired exactly one in-house creator, and not one of them has hired a second.",
        "Put the two side by side and you get the shape of the problem.  Brands are willing to give an outside creator a C-suite title, and unwilling to give the person who actually runs creator spend inside the building anything above manager.  So the external creator has a title and no budget authority, and the internal owner has budget and no seniority, and every decision goes up to someone whose job is something else entirely.",
        "Lily Comba, who runs the agency Superbloom, says the quiet part on the record: <mark>\"Some of these C-suite appointments are just a partnership with a fancier title... it was an ego thing to give them that title.\"</mark>  Her test is whether the appointment survives past the launch announcement.  Most have not.  Howlett is a partner of Blenders, not an employee, so the same test applies to him — check again in six months.",
    ],
    "numbers": [
        ("50M", "howlett followers, all platforms"),
        ("1%", "cpg creator roles at vp level"),
        ("200K", "views on a 100-follower staffer's post"),
    ],
    "flagnote": "Blenders would not disclose any financial terms of the Howlett deal, and \"exceeded all internal KPIs\" is the brand's own unaudited claim about its own video.  Linqia sells influencer marketing software, so a report concluding that this function deserves more senior ownership flatters what Linqia sells.  Its data is a point-in-time LinkedIn scrape of job titles, not a survey — it counts people who label the work, and misses anyone doing it under a different title.",
    "so_what": "A creator with a title can make decisions in the room, and a creator with a contract can only deliver what the contract says.  That is the entire difference, and it is why the store-associate video happened.  But a title with no budget line behind it is a press release, and right now most brands have built the announcement without building the authority underneath it.",
    "do_this": "Write down the name of the person inside your company who owns creator spend, then find out the largest sum they can approve without escalating, and get that number raised before you hand anyone outside the building a title.",
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
                "title": "Live viewers will sit through 8.7 minutes of ads an hour, and 79% would take the same or more",
                "hook": "The only video format where the audience does not want the ads to stop.",
                "open": True,
                "stamps": [
                    ("PPC LAND · 20 AUG", "https://ppc.land/live-streamers-accept-8-7-minutes-of-ads-per-hour-magnite-study-finds/"),
                ],
                "body": [
                    "Magnite published a study yesterday, run with the research firm Bounce Insights, surveying 835 American adults aged 18 and over who already watch live content through streaming services.  Asked where their ceiling sits, the average tolerance came out at <mark>8.7 minutes of advertising per hour of live content</mark>.  Asked to compare live against on-demand, 79% said they would accept the same number of ads or more.",
                    "Nobody says that about anything else you buy.  Every other video format is a negotiation about how few ads you can get away with.  Live is the one place the audience has priced the interruption in already, because they know the alternative is missing the thing they turned up for.",
                    "Two more numbers change how you cut.  <mark>41% prefer 15-second spots against 36% who prefer 30 seconds</mark>, and 14% want 60.  And 66% could remember an ad from their most recent live session, with food and drink the most-recalled category at 46%, retail at 32%, entertainment at 29% and cars at 28%.  Financial services came last of ten at 15%.",
                    "The mechanism is the room, not the screen.  92% of these viewers use a television for live, and 69% of them always or often watch with other people — on average three others.  Live sport is the highest at 64% shared viewing.  So your ad is not landing on one person with a phone in their hand.  It is landing on four people who are all facing the same screen and cannot skip it, and one of them will say something out loud about it.",
                    "The commerce number is the one to take to a planning meeting.  Among viewers aware of shoppable ads, 38% added something to a basket or bought it, against 27% purchase conversion for traditional in-stream breaks.  Magnite's explanation is timing: 55% of those purchase actions happen during the stream, while the second screen is already open, rather than after it when the intent has gone.",
                    "Read the sample properly before you act on it.  Every respondent already watches live streaming, so this tells you how an existing live audience behaves.  It tells you nothing about how many people you can reach.",
                ],
                "numbers": [
                    ("8.7", "minutes of ads per hour accepted"),
                    ("41%", "who prefer 15-second spots"),
                    ("38%", "shoppable viewers who bought or added"),
                ],
                "flagnote": "Magnite is a sell-side advertising company that sells the live and connected-TV inventory this study makes look attractive.  Every figure is self-reported by survey respondents rather than observed behaviour, and the co-viewing number, 69%, sits above both Google's own measurement and a February study from the VAB and TVision that put co-viewing at 60% of impressions on premium video and 45% on YouTube.",
                "so_what": "Live is the last video format with a captive room in front of it, and this is the first survey to put a number on how much the room will take.  8.7 minutes an hour is roughly double what people tolerate in on-demand, and the reason is that they cannot fast-forward without losing the event.  The 15-second preference matters more than it looks — most brands only have a 30 and a 6, so they are buying the format the audience likes least.",
                "do_this": "Cut a 15-second version of your current hero film this week and put it against your 30 in your next live buy, then ask your seller for a shoppable in-stream unit rather than a standard break.",
            },
            {
                "title": "K18 rolled a 150-pound ball of human hair through Manhattan and deliberately did not post about it",
                "hook": "161 billion strands, collected from salon floors, and the brand stayed quiet for the first day.",
                "stamps": [
                    ("MARKETING BREW · 21 AUG", "https://www.marketingbrew.com/stories/k18-tumblehair-hairball-activation-ooh-strategy"),
                ],
                "body": [
                    "The Unilever Prestige hair brand K18 built a 10-foot ball of real human hair and pushed it through Midtown, the West Village, Chinatown and Seaport, ending outside a Sephora in the Meatpacking District.  It weighed 150 pounds and had to be moved by hand — CMO Kleona Mack says they tried several mechanisms and in the end needed people to push it.",
                    "The hair came from K18's own partner salons, who were asked to bag the offcuts from haircuts that were going in the bin anyway.  <mark>The number is not decorative: the product claims to save 19,000 hairs on one head, multiplied by New York's population of roughly 8.5 million, which lands at a little over 161 billion strands.</mark>  So the object is the claim, at scale, in the street.",
                    "Here is the decision that made it work.  <mark>K18 did not claim the hairball on its own social accounts right away.</mark>  Mack let it roll through four neighbourhoods as an unexplained object, so that the people filming it were filming a mystery rather than an advertisement.  Paid creator posts came afterwards, once other people had already made the thing worth explaining.",
                    "They also planned for disgust rather than flinching at it.  Mack's line: \"We didn't fear it.  We expected it, because we had those reactions every time we presented it to partners and our internal teams.\"  Either people were repelled or fixated, and the brief wanted both, because both produce a post.",
                    "CreatorIQ's estimate of what came back is roughly $150,000 in earned media value, over 1.1 million social impressions and around 30,000 engagements.  That is a modest return in absolute terms for a stunt of this size, and it is worth saying so — the reusable part here is the sequencing, not the scoreboard.",
                ],
                "flagnote": "The $150,000 earned media value, the 1.1 million impressions and the 30,000 engagements are a CreatorIQ estimate reported by Marketing Brew, not audited results, and earned media value is a modelled number that every vendor calculates differently.  K18 disclosed no production cost, so there is no way to judge the return.",
                "so_what": "Posting your own stunt on day one turns it into an advertisement, and people scroll past advertisements.  Staying quiet turns it into a thing that happened, and things that happen get filmed by strangers whose followers trust them.  K18 bought the object and let other people supply the distribution, which is the cheapest half of any street campaign and the half most brands throw away by putting their logo on the first post.",
                "do_this": "On your next street stunt, hold your own brand post until day two and brief your creator partners to publish only after organic footage is already circulating.",
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
                "title": "Wrong roster: Meta paid creators to promote teen safety and one of them was nine years old",
                "hook": "The campaign was about who is old enough to use Instagram.",
                "open": True,
                "stamps": [
                    ("DEXERTO · 19 AUG", "https://www.dexerto.com/entertainment/metas-paid-teen-safety-campaign-included-a-9-year-old-influencer-too-young-to-use-instagram-3400123/"),
                ],
                "body": [
                    "The Tech Transparency Project found that Meta recruited parenting, lifestyle and mental health creators around the world to promote Instagram Teen Accounts, with sponsored posts running in India, Brazil, Canada, France, Spain and the United Kingdom — frequently while those countries were debating age limits or outright bans on social media for minors.",
                    "One of the paid endorsements came from a child creator in the UAE, Yosi Time, who the Tech Transparency Project says appears to be about nine years old, with roughly 493,000 Instagram followers.  <mark>Instagram's own minimum age is 13, and Teen Accounts are designed for 13 to 17.</mark>  The report also says his post did not carry the paid-partnership label that other posts in the same campaign carried.",
                    "Meta's response is that it has run more than 40 events since 2024 promoting teen safety tools, that it works with creators because they are \"local voices trusted by parents in their communities,\" and that all paid partnerships were clearly disclosed and compliant with local advertising rules.  It does not disclose individual partnership terms.",
                    "The failure mode is not the message.  It is the roster.  A campaign that ran across six countries had a sign-off process good enough to approve creative and not good enough to ask a creator how old they are, on a campaign whose entire subject is how old you have to be.",
                    "This is what happens when a creator campaign is bought at scale through local teams with no single owner checking the list.  Nobody made a bad decision.  Nobody made the check either.",
                ],
                "flagnote": "Every finding here originates with the Tech Transparency Project, a single advocacy organisation, and has not been independently confirmed.  Meta disputes the disclosure claim directly, saying all paid partnerships in the campaign were clearly labelled.  The age of the creator is the Tech Transparency Project's assessment, not a confirmed date of birth.",
                "so_what": "The bigger your creator roster, the more likely something on it contradicts the thing you are paying it to say.  A multi-country campaign with local buying means nobody is looking at the whole list at once, and the contradiction only becomes visible when a journalist or a watchdog reads it end to end.  Age and disclosure are the two cheapest checks available and the two most commonly skipped.",
                "do_this": "Pull your full active creator list into one sheet this week with each creator's age and each post's disclosure status in two columns, and have one named person sign it off before any multi-market campaign goes live.",
            },
            {
                "title": "Wrong format: AI ads that pretend to be real get roasted, AI ads that admit it get 6.4x",
                "hook": "Almost half of American consumers already think AI has made content worse.",
                "stamps": [
                    ("MODERN RETAIL · 20 AUG", "https://www.modernretail.co/marketing/the-new-ai-playbook-the-rules-brands-are-setting-around-customer-facing-content/"),
                ],
                "body": [
                    "Two numbers, pointing in opposite directions.  Canva's State of Marketing report found <mark>97% of marketing leaders use AI in their daily creative work and 99% planned to increase AI investment this year</mark>.  Gartner found in June that <mark>49% of American consumers think AI has made content quality worse, rising to 57% among Gen Z and millennials</mark>.",
                    "The failures are the obvious ones.  REI was roasted this summer over an AI-generated ad showing a woman with a bicycle that had two sets of handlebars.  Quip got accused of using AI on a surrealist campaign where it had not used AI at all, which is arguably the worse outcome — you carry the cost of the suspicion without having saved anything.",
                    "Now the win, from the same reporting.  Koia, a plant-based protein drink brand, used AI as the basis for a Costco protein powder launch and got <mark>48,000 organic views, about 6.4 times the organic performance it normally gets on Instagram Reels</mark>.  VP of marketing Diane DiLorenzo explains why plainly: \"In those situations, everyone knows it's AI, and I think that's another reason why performance is good.  People are engaging with it and not feeling deceived.\"",
                    "So the dividing line is not whether you used AI.  It is whether the viewer was supposed to notice.  Use it for the floating product, the dream sequence, the thing you could never film, and the audience reads it as craft.  Use it to fake a real person in a real place and you are asking the audience to spot the mistake, and they will, because 57% of the under-45s are already looking for it.",
                    "Mack Reynolds, now at Shuttlerock and previously a creative strategy lead at Meta, draws the same line between building templates for product photography and having AI-generated people talk to camera about why a product is good.  One is a tool.  The other is a claim.",
                ],
                "so_what": "AI is safe wherever reality was never on the table, and dangerous everywhere it was.  The two-handlebar bicycle is not an AI problem, it is a review problem, but the audience does not separate those and neither will the comments.  Koia's result says the discount for admitting it is zero and the discount for being caught is large, which makes the decision easy.",
                "do_this": "Add one line to your creative brief that states whether AI use in this asset is meant to be visible or invisible, and refuse to sign off any invisible use that includes a human face or a real location.",
            },
        ],
    },
    {
        "id": "moves",
        "name": "MOVES",
        "page": "pg. 04",
        "note": "structural changes that alter what you can buy",
        "tint": None,
        "items": [
            {
                "title": "Gap hired a Walmart marketer to build original shows and characters",
                "hook": "A mass apparel retailer is now standing up a development function.",
                "stamps": [
                    ("VARIETY · 20 AUG", "https://variety.com/2026/digital/news/justin-breton-gap-brand-marketing-walmart-fashiontainment-1236838762/"),
                ],
                "body": [
                    "Justin Breton, previously at Walmart, joins Gap Inc. on 31 August as VP of development, based in New York, to build original shows and characters rooted in Gap's brands.  He reports to Pam Kaufman, the Nickelodeon and Viacom veteran who became Gap's first chief entertainment officer in February.",
                    "The company calls the programme \"Fashiontainment.\"  The title to pay attention to is not the initiative name, it is \"VP of development\" — that is a television job title, and it means someone at Gap now has the job of finding and greenlighting formats rather than approving campaigns.",
                    "No slate, budget or platform has been disclosed.  Treat this as a hiring signal rather than a plan.",
                ],
                "so_what": "The gap between a brand that makes advertising and a brand that makes programming is one person whose job is development.  Gap has now hired that person, under an executive who ran a children's television network.  Every apparel competitor will be asked in a board meeting within a quarter why they have not.",
                "do_this": "Look at your own org chart and identify who would receive an unsolicited format pitch from a production company, then tell them that is now part of their job.",
            },
            {
                "title": "Meta is removing the option to exclude ad placements",
                "hook": "The lever you use to keep your ads off certain surfaces is going away.",
                "stamps": [
                    ("SOCIAL MEDIA TODAY · 20 AUG", "https://www.socialmediatoday.com/news/meta-removes-option-to-exclude-ad-placements/828461/"),
                ],
                "body": [
                    "Meta has begun telling advertisers it will remove the Placements option from ad sets, ending the ability to exclude specific placements such as Facebook search results or in-stream slots between Reels.  According to Meta ads specialist Jon Loomer, it also removes the ability to exclude entire platforms.  No timeline has been announced.",
                    "The direction is the one Mark Zuckerberg has described out loud: <mark>\"you come to us, you tell us what your objective is, you connect to your bank account, you don't need any creative, you don't need any targeting demographic, you don't need any measurement.\"</mark>  Every step toward that end state removes a control from the buyer.",
                    "The practical cost is brand safety.  If you currently keep your ads off a particular surface because of what runs next to them, you are about to lose the switch that does it.",
                ],
                "flagnote": "This rests entirely on a screenshot of an in-product notice shared by one advertiser, Jon Loomer.  Meta has issued no statement and given no timeline, and the platform-exclusion detail is his interpretation rather than Meta's wording.",
                "so_what": "Automated placement usually delivers better numbers, because the system finds the cheapest inventory that converts.  The thing it cannot know is which surfaces your legal team would object to.  Losing the exclusion switch means the only brand-safety control left on Meta is the decision to buy there at all.",
                "do_this": "Export your current Meta placement exclusions this week and model what your spend looks like with all of them switched on, so you know the cost before the choice is taken away.",
            },
            {
                "title": "OpenAI turns on ChatGPT ads across 31 European markets on Monday",
                "hook": "Bought through six agency groups, not through a self-serve tool.",
                "stamps": [
                    ("DIGIDAY · 19 AUG", "https://digiday.com/marketing/openais-ads-business-hits-europe-at-the-six-month-mark/"),
                ],
                "body": [
                    "From Monday 24 August, ChatGPT ads run in 31 European markets including Germany, France, Spain, Italy, Poland, Sweden, Norway, Denmark, Ireland and the Netherlands.  That is six months after the February pilot in the United States, and follows Canada, Australia, New Zealand, the UK, Mexico, Brazil, Japan and South Korea.",
                    "Buying runs through Publicis, Omnicom, WPP, Havas, Dentsu and MediaPlus.  This is agency-repped inventory, not something you can switch on yourself — the American self-serve tool launched this spring with a $50,000 minimum that has since been dropped.",
                    "The scale claim from ads VP Dave Dugan: 900 million weekly active users, with roughly <mark>20% of queries showing direct commercial intent</mark>.  Bidding has shifted to cost per click, which now accounts for most of the spend.",
                ],
                "so_what": "One in five queries with buying intent is a higher-intent pool than almost any social surface, and it is being sold through the same six holding companies that already handle your media.  That means it will appear in a plan you are shown rather than as a decision you make.  Ask what it is displacing.",
                "do_this": "Ask your agency this week whether ChatGPT inventory is in your European plan from Monday, and if it is, what line it came out of.",
            },
            {
                "title": "YouTube folded AI likeness claims into the same place as copyright claims",
                "hook": "One tab now, four ways to dispute, and no strike on your channel.",
                "stamps": [
                    ("SOCIAL MEDIA TODAY · 20 AUG", "https://www.socialmediatoday.com/news/youtube-simplifies-its-ai-claims-process/828462/"),
                ],
                "body": [
                    "The \"copyright\" menu in video details becomes \"Claims,\" holding both Content ID copyright claims and privacy-based AI likeness claims.  Four dispute categories arrive with it: Explicit Consent, Parody or Satire or Public Interest, Content Not Altered or Made with AI, and Claimed Content Doesn't Appear.",
                    "YouTube opened likeness detection to all users over 18 in May, letting anyone upload their image and have YouTube scan new uploads for it.  <mark>A valid likeness claim can restrict or block a video, but YouTube says it produces no copyright or community guidelines strike and does not affect a channel's standing.</mark>",
                    "The category that matters for brand work is Explicit Consent, which means verified permission to use someone's voice or likeness.",
                ],
                "so_what": "If you make anything with a synthetic version of a real person — a creator, a spokesperson, a founder — the release you hold is now the thing that gets you back online after a claim.  A signed agreement in a filing cabinet is not the same as verified permission inside YouTube's dispute form.  Find out which one you have.",
                "do_this": "Check that every talent agreement covering synthetic voice or likeness in your current work contains explicit written consent you can produce inside a YouTube dispute, and fix any that do not before you publish.",
            },
        ],
    },
    {
        "id": "onstream",
        "name": "ON STREAM",
        "page": "pg. 05",
        "note": "live numbers, and what they are actually worth",
        "tint": None,
        "items": [
            {
                "title": "The biggest live broadcaster on the planet is a Brazilian YouTube channel, and on Sunday it starts doing the Premier League",
                "hook": "24,227,687 people watching one stream at the same moment.",
                "open": True,
                "stamps": [
                    ("TUBEFILTER · 20 AUG", "https://www.tubefilter.com/2026/08/20/live-mode-cazetv-english-premier-league-uefa-champions-league/"),
                    ("PODER360 · 19 JUL", "https://www.poder360.com.br/poder-midia/com-pico-de-209-mi-cazetv-nao-renova-recorde-de-audiencia-na-final/"),
                    ("CNN BRASIL · 19 AUG", "https://www.cnnbrasil.com.br/esportes/futebol/futebol-internacional/dona-da-cazetv-transmitira-champions-e-premier-league-no-youtube-entenda/"),
                    ("STREAMS CHARTS · 20 JUL", "https://streamscharts.com/news/fifa-world-cup-2026-livestreaming-recap"),
                ],
                "body": [
                    "Peak first.  <mark>CazéTV's France against Spain World Cup semi-final on 14 July peaked at 24,227,687 concurrent devices</mark>, per Poder360, and YouTube separately confirmed \"24+ million simultaneous devices\" for the same match.  Five CazéTV streams cleared 20 million concurrent.  YouTube says the channel holds 29 of the top 30 biggest livestreams in the platform's history.",
                    "Make that number mean something.  The Maracanã holds about 78,800 people.  <mark>24.2 million at one moment is roughly 307 full Maracanãs, all watching the same feed, for free, on a channel run by one Brazilian creator.</mark>  For scale inside our own industry: Gamescom Opening Night Live, the biggest games showcase of the year, peaked at just over 2 million concurrent in 2025.",
                    "Two honesty notes, because this is exactly where live numbers get mangled.  The World Cup final did not set the record — CazéTV peaked at 20,934,534 on Spain against Argentina.  The widely-repeated \"27 million\" for that final is YouTube's platform-wide figure across more than 40 markets, not CazéTV's channel.  Those are different measures and merging them overstates one channel by about 30%.",
                    "On hours watched, be careful in the other direction.  Streams Charts logged more than 2.4 billion hours across all tracked platforms for the whole tournament, with YouTube about 95% of it, spread over 66,509 channels.  <mark>That is the tournament, not the channel.</mark>  CazéTV's own published figure is 2.5 billion views across all 104 matches plus 12 million new subscribers in 30 days, and views are not hours.  Nobody has published CazéTV's hours watched, so do not quote one.",
                    "Now the move.  CazéTV's parent, LiveMode, has sublicensed one Premier League match per round in Brazil from ESPN Brazil, for three seasons, with the right to pick a match involving one of the five biggest-drawing clubs.  It starts on Sunday 23 August with Manchester City against Bournemouth.  Separately, and this is a different deal, LiveMode launches LiveModeTV in Portugal through DAZN, carrying one Champions League and one Premier League match per round free on YouTube.  Cristiano Ronaldo is a shareholder in the international business.",
                    "The structure is the interesting part.  A free creator-hosted match is the shop window for a paid subscription — Portuguese viewers who want more than one match a week have to subscribe to DAZN.  It is the same shape as DAZN letting KSI stream matches of Dagenham & Redbridge, the club he part-owns, in Britain.",
                ],
                "so_what": "Live sport is quietly moving onto free creator channels, and the audience there is larger than any broadcast equivalent because the price is zero and the host is someone people already follow.  If you sponsor sport, the rights sheet you are shown probably prices the paid broadcast and treats the free YouTube stream as promotion.  On these numbers the free stream is the bigger audience, and right now it is the cheaper one.",
                "do_this": "Watch Sunday's Manchester City against Bournemouth stream on CazéTV, record the peak concurrent figure yourself, and take it to your next sports rights conversation as the number the paid broadcast has to beat.",
            },
        ],
    },
    {
        "id": "watch",
        "name": "ONE TO WATCH",
        "page": "pg. 06",
        "note": "one creator with momentum, and what to buy from them",
        "tint": None,
        "items": [
            {
                "title": "Reckless Ben",
                "hook": "Roughly half of an eleven-year channel's lifetime views arrived in the last three months.",
                "open": True,
                "stamps": [
                    ("THE PUBLISH PRESS · 19 AUG", "https://news.thepublishpress.com/p/did-youtube-views-just-decrease-in-value"),
                    ("HOLLYWOOD REPORTER · 10 JUL", "https://www.hollywoodreporter.com/business/business-news/ben-schneider-signs-with-caa-1236643944/"),
                    ("YOUTUBE CHANNEL", "https://www.youtube.com/@RecklessBen"),
                ],
                "body": [
                    "Ben Schneider makes long undercover investigations of businesses.  On 21 May he started a series on the Lego resale chain Bricks & Minifigs.  <mark>The Publish Press reported on Tuesday that the series has drawn 43 million views since May, and that he went from around 500,000 subscribers at the start of the summer to 1.8 million.</mark>  His channel now shows 1.85 million subscribers and 96.2 million lifetime views, so roughly half of everything an eleven-year-old channel has ever earned arrived in the last three months.",
                    "CAA signed him on 10 July, per The Hollywood Reporter.  He has also started a second channel under his own name, which is already past 200,000 subscribers off six videos.  A talent agency taking a creator mid-run is the clearest available signal that someone with a rate card thinks this is not a spike.",
                    "One correction worth carrying, because the wrong version is already circulating.  His 15 August video documented Provo Canyon School, and it did not close it.  <mark>Utah had already revoked the licences on 6 July and 17 July, with a closure deadline of 16 August — the day after his video went up.</mark>  He documented the final days of a closure that was already ordered.  That is still a good video.  It is not the thing people are saying it is.",
                    "The format itself is the reason this grew.  His videos run 40 to 50 minutes, land as series with cliffhangers rather than one-offs, and each opens with a stretch where he lays out the equipment he is about to use.  That kit segment is the highest-attention minute in the whole video and it is already in the edit.",
                    "Now the part most brands will not want to hear.  His method is deception and his targets are businesses, and he is facing criminal misdemeanour charges over entering corporate offices with a hidden camera, plus further charges filed in March, with active suits running.  Most brand safety policies will not clear him.  The ones that can are the ones whose product is the camera.",
                ],
                "watch": {
                    "label": "TOP VIDEO, LAST 3 MONTHS",
                    "title": "Bricks and Minifigs Tried to Get Me Arrested to Stop This Video",
                    "url": "https://www.youtube.com/watch?v=auf_-bVs2WA",
                    "meta": "7,708,939 views · published 9 July 2026 · 47m 22s",
                    "note": "The middle episode of the Lego resale investigation, and the one where the company's response becomes the story.",
                },
                "flagnote": "Schneider faces criminal misdemeanour charges from American Fork police over entering Bricks & Minifigs corporate offices with a hidden camera in December 2025, plus stalking and residential picketing charges filed on 27 March 2026, with active suits and countersuits.  None of it is resolved.  The 43 million and 1.8 million figures come from The Publish Press; the 1.85 million subscriber and 96.2 million lifetime view counts are from his channel today.",
                "so_what": "This is what real momentum looks like when it is not a viral fluke — a repeatable series format, a second channel already working, and an agency signing him mid-run.  The brand fit is narrow but it is unusually clean, because his kit segment is a product demonstration he was going to film anyway.  You are not asking him to change what he makes.  You are paying to be the equipment inside it.",
                "do_this": "If you sell action cameras, storage, audio kit or field gear, brief his CAA representation this week on buying the kit segment across a full six-episode arc rather than a single video, and price it before the second trade profile runs.",
            },
        ],
    },
    {
        "id": "money",
        "name": "THE MONEY",
        "page": "pg. 07",
        "note": "where the spend actually moved",
        "tint": None,
        "items": [
            {
                "title": "Ralph Lauren pushed marketing to 8.2% of sales and told investors it is working",
                "hook": "Up from 7.5% a year ago, and about 3.5% earlier in the turnaround.",
                "open": True,
                "stamps": [
                    ("GLOSSY · 21 AUG", "https://www.glossy.co/fashion/luxury/ralph-lauren-us-open-retail-marketing-strategy/"),
                ],
                "body": [
                    "<mark>Ralph Lauren's marketing investment hit 8.2% of sales in fiscal Q1 2027, up from 7.5% a year earlier and around 3.5% earlier in its \"elevation\" phase.</mark>  Quarterly revenue rose 13% in constant currency to $1.96 billion, average unit retail rose 15%, and the brand recruited 1.5 million new direct-to-consumer customers in the quarter.  CEO Patrice Louvet told the August earnings call the company is seeing \"really good returns\" on the increased spend.",
                    "The US Open piece is where the discipline shows.  The tournament runs 23 August to 13 September.  <mark>Ralph Lauren's campaign runs 4 August to 20 September — roughly twice the length of the event it is attached to.</mark>  It starts with a Nordstrom flagship takeover in New York and ends a week after the final.",
                    "They are also dressing 800 people at the tournament: 300 ball crew, 215 on-court officials, 285 court attendants.  And the certified vintage programme, launched in September 2024 with pieces from $150 to $3,500, comes to the Open for the first time.",
                ],
                "so_what": "Most sponsorships are bought for the length of the event, which means the spend is compressed into the two weeks when every competitor is also shouting.  Doubling the window is not a bigger budget, it is the same budget spread across a period when attention is cheaper on both sides of the peak.  And a public company raising marketing intensity by 0.7 points of revenue and defending it on an earnings call is the most credible endorsement of that approach you will get.",
                "do_this": "Take your next event sponsorship and move a third of the budget into the four weeks before and the week after, then compare cost per reach against the in-event weeks.",
            },
            {
                "title": "The Athletic went from 5 World Cup sponsors to 25 by starting two years early",
                "hook": "Readership up 40% and the 2027 briefs are already arriving.",
                "stamps": [
                    ("MARKETING BREW · 20 AUG", "https://www.marketingbrew.com/stories/world-cup-the-athletic-audience-sponsorship"),
                ],
                "body": [
                    "The Athletic had about five sponsors during the 2022 World Cup in Qatar.  For 2026 it had <mark>25 official advertising partners, not counting one-off banner deals</mark>, according to chief commercial officer Sebastian Tomich.  Readership rose 40% year over year in the first few weeks of the tournament.",
                    "The sold units are worth copying because they are formats, not slots.  Heineken sponsored the daily live blogs from 3pm to 8pm eastern, every day.  Amazon Fire TV sponsored a 30-minute daily streaming show.  Google Search ran a series profiling one fan group per competing nation across app, site, social, email and creator partnerships.  More than 70 journalists covered the event.",
                    "Two things made it possible.  Planning began roughly two years out through a cross-functional group, and North American hosting opened American budgets — Google, Amazon, EA Sports — that simply were not available in 2022.",
                    "Tomich says briefs are already arriving for the 2027 Women's World Cup in Brazil: \"A lot of marketers are going to have a women's sports strategy for next year.\"",
                ],
                "so_what": "Five to twenty-five sponsors is not a sales result, it is a product result — they built things a brand could own for a whole tournament rather than impressions to sell.  A daily 5pm live blog with one name on it is a format a brand can be identified with, which a run of banners never is.  And the reason it sold is that they started building it two years before anyone was buying.",
                "do_this": "Send a brief for the 2027 Women's World Cup in Brazil this month, and ask for a named daily format you can own for the whole tournament rather than a package of impressions.",
            },
        ],
    },
    {
        "id": "format",
        "name": "FORMAT LAB",
        "page": "pg. 08",
        "note": "one thing about how to actually make the video",
        "tint": None,
        "items": [
            {
                "title": "Stop buying a brand trip and start buying a deliverable count",
                "hook": "One creator, one month, 37 pieces of content.",
                "open": True,
                "stamps": [
                    ("GLOSSY · 21 AUG", "https://www.glossy.co/fashion/why-controversies-still-havent-killed-the-brand-trip/"),
                ],
                "body": [
                    "The brand trip is not dying, it is being restructured, and the restructure is a production lesson.  Glossy's number for the old version: a major brand trip can top $1 million, per Sierra Moore, senior creative director at Open Influence.  For that money you get a weekend, a group, and a set of near-identical posts from people in the same place at the same time.",
                    "The new version is Rent the Runway's month-long Air France \"sabbatical\" with one creator, Candace Marie.  <mark>The deal requires 37 pieces of content from that single creator over a month.</mark>  Rent the Runway's chief merchant officer Sarah Tam states the mechanism outright: \"going deeper with one creator can actually produce better economics than going broader with many.\"",
                    "Do the arithmetic on why that is true.  Twenty creators on a four-day trip give you twenty versions of the same four days, shot in the same light, in the same locations, and they all publish inside the same week and cannibalise each other.  One creator over a month gives you 37 assets across four weeks of changing settings, published on a schedule you can plan around, with a narrative that builds.  <mark>The second option is a production contract wearing a holiday's clothes.</mark>",
                    "The accompanying customer giveaway drew 1,200 entries in its first week, which is the other half of the design — the trip is content and the giveaway is the reason your actual customers pay attention to it.",
                    "Compare against the range.  Urban Outfitters flew 200 micro-creators to Joshua Tree in April.  Dove sent a fan rather than a creator to the 2025 US Open.  Kourtney Kardashian Barker's Lemme is running a $20,000 vacation sweepstakes with one entry per dollar spent.  All different answers to the same question: who is the trip for, the creator or the customer?",
                    "VML North America's chief strategy officer Ellie Bamford adds the note most brands ignore when they brief these: \"Show some failure.  People don't mind it.\"  A month of flawless footage reads as a commercial.  A month with one bad day reads as a trip.",
                ],
                "so_what": "The reason brand trips get mocked is that they look like a reward rather than a job, and 20 people posting the same sunset in the same week confirms it.  Buying 37 assets from one person over a month solves both problems at once — it produces a volume of usable footage no group trip can match, and it looks like work because it is work.  You are paying for a content contract with travel attached, not travel with content attached.",
                "do_this": "Price your next creator trip as a deliverable count instead of a headcount — one creator, one month, a written number of assets — and put the giveaway in front of your customers rather than the itinerary.",
            },
        ],
    },
]

FORECAST = [
    {
        "confidence": "LIKELY",
        "window": "by end of Q1 2027",
        "headline": "Creator C-suite titles start coming with a budget line, or they stop being announced",
        "body": "Right now the external creator gets the title and the internal owner gets the budget, and neither one can act alone.  That arrangement produces exactly one good launch video and then stalls, which is what Superbloom's Lily Comba is describing when she says most of these appointments turn out to be a partnership with a fancier title.  The brands that fix it will hand the internal role real approval authority rather than hand another outsider a bigger title, because the second option is cheaper and has now visibly stopped working.",
        "do": "Raise the sum your internal creator lead can approve without escalation before you announce anyone's title.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "next 3 months",
        "headline": "The free creator livestream becomes a standard clause on European sports rights",
        "body": "Three separate versions of the same structure are now live: ESPN Brazil sublicensing a match a week to CazéTV, DAZN putting one Champions League and one Premier League match a round on a free YouTube channel in Portugal, and DAZN letting KSI stream his own club in Britain.  In each case the free creator broadcast exists to sell a paid subscription behind it.  The next set of European rights negotiations will price that stream explicitly rather than treat it as promotion, and once it is priced it becomes something a sponsor can buy separately.",
        "do": "Ask any sports rights holder you work with what their free creator-channel plan is, and get the audience forecast in writing before you renew.",
    },
    {
        "confidence": "LIKELY",
        "window": "next 6 months",
        "headline": "Ad loads on live inventory get rewritten upward, and the 15-second spot comes back",
        "body": "Magnite has just handed every live seller a number that says viewers accept 8.7 minutes an hour and 79% would take the same or more than on-demand.  Sellers do not sit on a figure like that.  Expect heavier loads on live sport and events, sold as something the audience asked for, and expect the format mix to shift because 41% prefer 15 seconds against 36% for 30.  Buyers who only have a 30 and a 6 will be paying for the format the audience likes least.",
        "do": "Get a 15-second cut of your current hero film into your asset library now, before the next live buy.",
    },
    {
        "confidence": "WATCH CLOSELY",
        "window": "next 6 months",
        "headline": "Brand-safety spend moves toward platforms that still let you choose where you appear",
        "body": "Meta removing placement exclusions takes away the last granular safety control a buyer has there, and the direction Zuckerberg describes is a system where you supply an objective and a bank account and nothing else.  Some categories can live with that.  Regulated categories, children's products and anything with a legal review cannot.  Those budgets do not disappear, they move to inventory where the buyer can still name the surface, which currently means direct creator deals and premium video.",
        "do": "Log every placement you exclude on Meta today, and price what moving that spend to direct creator buys would cost.",
    },
    {
        "confidence": "LONG SHOT",
        "window": "next 12 months",
        "headline": "Brands start labelling AI use in ads the way they label paid partnerships",
        "body": "Gartner has 49% of Americans saying AI made content worse, rising to 57% under 45, and the REI and Quip incidents show the cost lands whether or not you actually used it.  Koia's Costco launch is the counter-example that makes labelling thinkable: everyone knew it was AI and it ran at 6.4 times the brand's normal organic performance.  If disclosure carries no performance penalty and concealment carries a reputational one, someone large will label first and the rest will follow within two quarters.",
        "do": "Decide now which of your current assets you would be comfortable labelling, and fix the ones you would not.",
    },
]

TLDR = [
    "Blenders made Jordan Howlett its chief content officer on a multi-year deal, while a Linqia study of 152 creator roles across the biggest packaged goods companies found only 1% sit at VP level.  Find out the largest sum your internal creator lead can approve alone, and raise it before you hand anyone outside the building a title.",
    "Magnite surveyed 835 American live-stream viewers and found they accept 8.7 minutes of ads per hour, 79% would take the same or more than on-demand, and 41% prefer 15-second spots over 30.  Cut a 15-second version of your hero film this week and put it against your 30 in the next live buy.",
    "CazéTV peaked at 24,227,687 concurrent viewers on a single World Cup match, holds 29 of YouTube's 30 biggest livestreams ever, and starts carrying a free Premier League match every week from Sunday.  Watch Sunday's Manchester City against Bournemouth stream, record the peak yourself, and take that number into your next sports rights conversation.",
    "Meta is removing the ability to exclude ad placements, taking away the switch that keeps your ads off specific surfaces, with no timeline announced.  Export your current exclusions this week and model what your spend looks like with every one of them switched on.",
    "Koia's openly AI-made Costco launch got 48,000 organic views, about 6.4 times its normal Instagram Reels performance, while REI got roasted for an AI ad with two sets of handlebars and Gartner has 49% of Americans saying AI made content worse.  Add a line to your creative brief stating whether AI use is meant to be visible, and refuse invisible use on human faces and real locations.",
    "Ralph Lauren raised marketing to 8.2% of sales from 7.5%, grew revenue 13% to $1.96 billion, and runs its US Open campaign for twice the length of the tournament.  Move a third of your next event sponsorship budget into the four weeks before and the week after, then compare cost per reach.",
    "Rent the Runway swapped the group brand trip for one creator on a month-long deal worth 37 pieces of content, because depth beats breadth on economics.  Price your next creator trip as a written deliverable count from one person rather than a headcount on a plane.",
]
