# Getting Ali Tutors found on Google

Private working notes. This folder is **not** published: GitHub Pages only serves `docs/`.

## 1. What's already done on the site (no action needed)

| Area | Done |
|---|---|
| Pages Google can rank | One page per subject (8, including 11+ and 13+ entrance Maths), plus Pricing and About, each with its own title, description, canonical URL and H1 |
| Structured data | `LocalBusiness` + `WebSite` on the home page, `Person` on About, `Service` + breadcrumbs on every subject page. The self-published review/rating markup was removed because Google doesn't reward it and it can be treated as spam |
| Crawling | `sitemap.xml` lists all 11 public pages with real "last changed" dates; `robots.txt` points to it; `max-image-preview:large` allowed; thank-you, privacy and 404 pages are `noindex` |
| Speed | Lighthouse (local test) scores 100 for Performance, Accessibility, Best Practices and SEO on mobile and desktop. Phones now load a 3 KB headshot instead of 55 KB |
| Sharing | Redrawn share card, `og:locale`, `favicon.ico` (it was returning a 404) |
| Hooks | `tools/build_site.py` has blank `GSC_VERIFICATION`, `BING_VERIFICATION` and `SAME_AS` settings. Send me the values below and I'll wire them in |

Nothing above helps until the branch is merged and deployed.

## 2. Do these in week 1 (only you can, they need your accounts)

1. **Merge the branch** so the new pages go live.
2. **GitHub Pages settings:** Settings > Pages. Confirm the source is the `/docs` folder, the custom domain is `alitutors.com`, and **Enforce HTTPS** is ticked. At your DNS provider, `www` should be a CNAME to `alialjawabra.github.io` so `www.alitutors.com` redirects to the main address.
3. **Google Search Console** (search.google.com/search-console). This is the single biggest accelerator for a new site.
   - Add `alitutors.com`. If it asks for an HTML tag, send me the `content="..."` value and I'll add it.
   - Sitemaps > submit `https://alitutors.com/sitemap.xml`.
   - URL Inspection > paste each page > **Request indexing**. Do the home page first, then the subject pages (about 10 a day is the limit).
4. **Bing Webmaster Tools:** sign in and choose "Import from Google Search Console". This also covers DuckDuckGo, Ecosia and Copilot.
5. **Check what Google sees** after a week: search `site:alitutors.com`. You should see about 10 pages.

## 3. Google Business Profile: read before touching it

### I couldn't touch your profile, and it may not be eligible

- I have no access to your Google account, so I can't see or edit the profile, and I can't see whether it is verified or suspended.
- **Eligibility is the real issue.** Google requires a business to have in-person contact with customers (a place they visit, or you visiting them). Online-only businesses are not eligible, and ineligible profiles risk being suspended, which can take the reviews with them. Your site says sessions are online only, so as things stand a profile is risky. Sources I found (I could not open Google's own pages from this sandbox, so please confirm on Google's current guidelines):
  [Synup: GBP eligibility](https://synpost.synup.com/gbp-eligibility-for-special-business-types/),
  [Google Business Profile help](https://support.google.com/business/answer/7039811),
  [thestacc: tutoring and GBP](https://thestacc.com/blog/tutoring-google-business-profile/).

### Pick one route

**Route A: you genuinely offer some in-person tutoring** (for example lessons at students' homes around Bath, or at a fixed venue). Then you can be a *service-area business*. Create or fix the profile using section 4. Tell me and I'll update the website copy to say it, because the site and the profile must agree.

**Route B: stay online-only (the current model).** Don't create a profile, and if one already exists, don't build on it. Check its status in the "Needs attention" area, and update it to match reality or let me help you plan next steps. Put the effort into sections 5 and 6 instead. You lose map-pack placement but keep everything else, and you avoid a suspension.

**Never:** use a fake or virtual-office address, borrow someone's address, or claim in-person service you don't offer. These are the usual suspension triggers.

## 4. If you take Route A: profile contents, ready to paste

| Field | Value |
|---|---|
| Business name | `Ali Tutors` exactly as on the website. Don't add keywords or locations |
| Primary category | The closest of **Private tutor** or **Tutoring service** (check the dropdown; names change). Add at most one secondary category, and only if it's true |
| Address | **Hide it** (service-area business, no storefront). Don't publish a home address |
| Service area | Bath, plus only places you would really travel to |
| Phone | 07397 270583 (same as the website) |
| Website | `https://alitutors.com/` |
| Appointment link | `https://calendar.app.google/m9L2FUsJ7jZ5LGun6` |
| Hours | Only the hours you really answer. I don't know them, so I haven't guessed |
| Description (about 600 of 750 characters, no links) | See below |

> Ali Tutors offers one-to-one GCSE and A-level tutoring from Bath. Subjects: GCSE Maths, Combined and Triple Science and Business Studies; KS3 Maths and Science (Years 7 to 9); Maths for 11+ and 13+ entrance exams; A-level Maths, Economics and Philosophy. Ali got grade 8s and 9s in 10 GCSEs and A*A*A at A-level, so sessions follow the current specifications and what examiners reward, tailored to each student's exam board and target grade. DBS checked. Sessions are one-to-one and booked in blocks of five, with any unused sessions refunded. Start with a free intro call, no obligation.

(On Route A, add a sentence saying where in-person lessons happen.)

**Services** (add each under Services, with the price):

| Service | Price | Short description |
|---|---|---|
| A-level Maths tutoring | £35/hour | Pure, Statistics and Mechanics for AQA, Edexcel and OCR |
| A-level Economics tutoring | £35/hour | Micro, macro and the synoptic paper |
| A-level Philosophy tutoring | £35/hour | AQA: epistemology, ethics and metaphysics |
| GCSE Maths tutoring | £32/hour | Foundation and Higher tier |
| GCSE Combined & Triple Science tutoring | £32/hour | Biology, Chemistry and Physics |
| GCSE Business Studies tutoring | £32/hour | Marketing, finance, operations and exam technique |
| KS3 Maths & Science tutoring | £32/hour | Years 7 to 9 |
| 11+ & 13+ entrance exam Maths tutoring | £32/hour | Maths for private school 11+, the ISEB Pre-Test, grammar school 11+ and 13+ entrance (Years 5 and 6) |

**Photos:** logo = `docs/assets/icon-512.png`, cover = `docs/assets/og-card.jpg`, plus the headshot `docs/assets/ali-aljawabra.jpg`. Add 5 to 10 real photos (your set-up, whiteboard, a materials shot). Avoid stock images.

**Posts** (one a week, or fortnightly):
1. "Mocks are coming. I'm booking GCSE and A-level students now. Start with a free intro call: alitutors.com"
2. "What happens on a free intro call: we talk through the subject, the exam board and the target grade, and I tell you honestly whether I can help."
3. "Why KS3 matters: solid algebra, fractions and ratio in Years 7 and 8 make GCSE far less of a jump."

**Verification:** Google will ask you to verify (often by video). Do it as yourself, at your real location.

## 5. Reviews (works with or without a Google profile)

- You have two good ones (Sarah and Claire). Ask them, and each new family after results, for a review in whichever place you're listed.
- **Rules:** never offer anything in exchange for a review, and don't only ask the people you expect to be happy. Both break Google's policy (check their current wording).
- Message you can send:

> Hi [Name], it's Ali. It was a pleasure working with [child's name]. If you have two minutes, a short review would really help other families find me: [link]. Thank you so much!

- Reply to every review, short and specific.
- On the website, ask permission to add more testimonials with the subject and year group (like the two on the home page).

## 6. Other places to be listed (all fine for online tutoring)

- **Directories and platforms:** Superprof, Tutorful, Yell, Bark and similar. Some charge commission or a fee, so check each one's terms. A profile with reviews also builds trust and gives you backlinks.
- **Local word of mouth:** Bath parent groups, school PTA newsletters and community noticeboards. Link to your subject page that matches the year group (for example `gcse-maths.html` for a Year 10 group).
- **Apple Business Connect and Bing Places:** check each one's eligibility rules before applying, because they may also expect in-person contact.
- Keep your **name, phone and website identical everywhere** (Ali Tutors, 07397 270583, alitutors.com).

## 7. Honest expectations

- Nobody can guarantee a ranking. A new site typically takes weeks to be indexed and months to compete for terms like "GCSE maths tutor Bath", where Superprof, Tutorful and others are strong.
- Your best early chances are specific searches where there is less competition (A-level Philosophy and Economics tutors, "Edexcel A Economics Paper 3 help") and brand searches ("Ali Aljawabra tutor"). The new subject pages are built for those.
- Order of impact: (1) Search Console + sitemap, (2) real reviews, (3) a few quality links and listings, (4) more subject content over time.
- **Paid ads:** a small Google Ads budget on exact searches like "gcse maths tutor bath" can bring enquiries while the site ranks, but only worth it once you can measure which clicks become calls. There is currently no analytics (the privacy policy says so). Say the word if you want cookieless analytics added; I'd update the privacy policy at the same time.
