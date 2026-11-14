#!/usr/bin/env python3
"""Builds the alitutors.com static site into docs/.

    python3 tools/build_site.py

Every page shares one header, footer and stylesheet (docs/assets/site.css), so
change the nav, footer, rates or contact details HERE and re-run, rather than
editing the generated docs/*.html files by hand (they are overwritten).

Facts that live in one place:
  * RATES / links / contact details: the constants just below.
  * Subject pages: the SUBJECTS list.
  * Analytics: set UMAMI_WEBSITE_ID (blank = off). Clicks on the intro-call,
    WhatsApp, phone, email and Stripe links are then counted automatically,
    and the privacy policy updates itself to say so.
"""
import html
import json
import re
import subprocess
from datetime import date
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs"
SITE = "https://alitutors.com"

CALL = "https://calendar.app.google/m9L2FUsJ7jZ5LGun6"
STRIPE_A = "https://buy.stripe.com/6oU00j6Oq3tb0mP0uFgMw01"   # A-level block of five
STRIPE_G = "https://buy.stripe.com/8x2aEX0q28Nv5H95OZgMw02"   # GCSE, KS3 and 11+ block of five
PHONE_TEL = "+447397270583"
PHONE = "07397 270583"
EMAIL = "alitutoring@outlook.com"
# Fill these in later and re-run the build. Blank = not emitted.
SAME_AS = []              # public profile URLs (Google Business Profile, directory listings, ...)
GSC_VERIFICATION = ""     # content="" of Google Search Console's google-site-verification meta tag
BING_VERIFICATION = ""    # content="" of Bing Webmaster Tools' msvalidate.01 meta tag
UMAMI_WEBSITE_ID = ""     # Umami Cloud "Website ID". Blank = no analytics script at all.
WA_NUMBER = "447397270583"   # WhatsApp wants the international format, no "+"

TIERS = {
    "A": dict(label="A-level", rate=35, block=175, stripe=STRIPE_A),
    "G": dict(label="GCSE, KS3 & 11+", rate=32, block=160, stripe=STRIPE_G),
}

esc = html.escape
TODAY = date.today().isoformat()
YEAR = date.today().year

# --------------------------------------------------------------------------
# Subjects
# --------------------------------------------------------------------------
HONEST_RECENT = ("I sat these papers recently, so the specifications and mark schemes "
                 "I teach from are the current ones.")

SUBJECTS = [
    dict(
        slug="a-level-maths", name="A-level Maths", level="A-level", tier="A",
        title="A-level Maths Tutor, Online from Bath",
        desc="One-to-one A-level Maths tutoring online for AQA, Edexcel and OCR. Pure, Statistics and Mechanics, tailored to your target grade. £35/hour, from Bath.",
        h1="A-level Maths tutoring",
        lede="Pure, Statistics and Mechanics, taught to your exam board's specification and your target grade. I sat A-level Maths recently and got an A, so the papers are still fresh in my mind.",
        card="Pure, Statistics and Mechanics for AQA, Edexcel and OCR.",
        boards="AQA, Edexcel, OCR",
        topics=[
            ("Pure Mathematics", ["Algebra and functions", "Coordinate geometry", "Sequences and series", "Trigonometry", "Exponentials and logarithms", "Differentiation and integration", "Proof, vectors and numerical methods"]),
            ("Statistics", ["Sampling and data presentation, including the large data set", "Probability", "Binomial and normal distributions", "Hypothesis testing"]),
            ("Mechanics", ["Kinematics, including variable acceleration", "Forces and Newton's laws", "Moments", "Projectiles"]),
        ],
        structure_h="How the exams work",
        structure=[
            "A-level Maths is examined in three 2-hour papers, each worth 100 marks. How Pure, Statistics and Mechanics are split between the papers depends on the exam board, so we work from your board's specification and past papers.",
        ],
        lose=[
            "Algebraic slips in long, multi-step questions",
            "Not showing enough working in &ldquo;show that&rdquo; and proof questions",
            "Mechanics modelling: naming the assumptions the question is looking for",
            "Hypothesis test conclusions that aren't written in context",
        ],
        results=[("A", "A-level Maths"), ("A*A*A", "Economics, Philosophy &amp; Maths")],
        review=None,
        faq=[
            ("Which exam boards do you teach?",
             "<p>AQA, Edexcel and OCR. Sessions are tailored to the board your school sits, so the question styles match your papers.</p>"),
            ("Can sessions focus on the topics I find hardest?",
             "<p>That's what the free intro call is for: we talk through what's needed (topics, exam board and target grade) and plan from there.</p>"),
            ("Do you teach Year 12 and Year 13?",
             "<p>Yes, both years of the A-level, tailored to what the student is covering in school.</p>"),
        ],
    ),
    dict(
        slug="a-level-economics", name="A-level Economics", level="A-level", tier="A",
        title="A-level Economics Tutor, Online from Bath",
        desc="One-to-one A-level Economics tutoring online, tailored to your exam board. A* in Economics, 96% in Edexcel A Paper 3. £35/hour, from Bath.",
        h1="A-level Economics tutoring",
        lede="Micro, macro and the synoptic paper, taught to your exam board and target grade. I took Edexcel A myself and got an A*, including 96% in Paper 3.",
        card="Micro, macro and the synoptic paper, for Edexcel, AQA and OCR.",
        boards="Edexcel A, AQA, OCR",
        topics=[
            ("Theme 1: Markets and market failure", ["How markets work: supply, demand and elasticity", "Market failure", "Government intervention"]),
            ("Theme 2: The UK economy", ["Measures of economic performance", "Aggregate demand and aggregate supply", "Economic growth", "Macroeconomic objectives and policies"]),
            ("Theme 3: Business behaviour and the labour market", ["Business growth and objectives", "Revenues, costs and profits", "Market structures", "The labour market"]),
            ("Theme 4: A global perspective", ["International economics", "Poverty and inequality", "Emerging and developing economies", "The financial sector and the role of the state"]),
        ],
        topics_note="Themes shown are for Edexcel A, the specification I sat. AQA and OCR group the same ideas differently, so we follow your board's structure.",
        structure_h="How the exams work",
        structure=[
            "Edexcel A has three papers. <b>Paper 1</b> is Markets and business behaviour (Themes 1 and 3), <b>Paper 2</b> is The national and global economy (Themes 2 and 4), and <b>Paper 3</b> is Microeconomics and macroeconomics: the synoptic paper, drawing on all four themes.",
            "Across all of them, marks go to diagrams that are explained, chains of reasoning, quantitative skills and evaluation.",
        ],
        lose=[
            "Describing a point without developing it into a chain of reasoning",
            "Evaluation that could apply to any case, rather than the context given",
            "Diagrams that are drawn but not explained",
            "Data-response answers that don't use the extract",
        ],
        results=[("A*", "A-level Economics"), ("96%", "Paper 3, Edexcel A")],
        review=None,
        faq=[
            ("I'm on AQA or OCR, not Edexcel. Can you still help?",
             "<p>Yes. Sessions are tailored to whichever board your school sits. Edexcel A is the specification I sat myself.</p>"),
            ("What is Paper 3?",
             "<p>On Edexcel A, Paper 3 is the synoptic paper, bringing together micro and macro across all four themes.</p>"),
            ("Do I need to be good at maths for Economics?",
             "<p>Some. Quantitative skills such as elasticity, the multiplier and real versus nominal figures are assessed across the papers, so we practise them as they come up.</p>"),
        ],
    ),
    dict(
        slug="a-level-philosophy", name="A-level Philosophy", level="A-level", tier="A",
        title="A-level Philosophy Tutor, Online from Bath",
        desc="One-to-one A-level Philosophy tutoring online for AQA. A* with 196/200 across both papers. Epistemology, ethics and metaphysics. £35/hour, from Bath.",
        h1="A-level Philosophy tutoring",
        lede="Epistemology, moral philosophy, and the metaphysics of God and of mind. I took AQA Philosophy myself and got an A*, with 196/200 across the two papers.",
        card="Epistemology, ethics and metaphysics, for AQA.",
        boards="AQA",
        topics=[
            ("Paper 1: Epistemology", ["What knowledge is", "Perception", "Reason as a source of knowledge", "The limits of knowledge and scepticism"]),
            ("Paper 1: Moral philosophy", ["Utilitarianism", "Kantian ethics", "Aristotelian virtue ethics", "Applied ethics", "Meta-ethics"]),
            ("Paper 2: Metaphysics of God", ["Arguments for the existence of God", "The attributes of God", "The problem of evil", "Religious language"]),
            ("Paper 2: Metaphysics of mind", ["Dualism", "Physicalism", "Functionalism", "The problem of other minds"]),
        ],
        structure_h="How the exams work",
        structure=[
            "AQA A-level Philosophy is examined in two papers, each 3 hours and worth 100 marks. Paper 1 covers Epistemology and Moral philosophy; Paper 2 covers the Metaphysics of God and the Metaphysics of mind.",
            "With that much writing time, a big part of doing well is building a clear argument and weighing it up, rather than listing everything you know.",
        ],
        lose=[
            "Listing arguments instead of evaluating them",
            "Skipping the strongest objections and the replies to them",
            "Lopsided answers: all knowledge, very little judgement",
            "Running short of time across a three-hour paper",
        ],
        results=[("A*", "A-level Philosophy"), ("196/200", "AQA, across both papers")],
        review=None,
        faq=[
            ("Which specification do you teach?",
             "<p>AQA A-level Philosophy, the specification I sat myself.</p>"),
            ("What makes a strong Philosophy essay?",
             "<p>Broadly: a clear line of argument, precise use of the arguments and key terms, real engagement with objections, and a reasoned judgement at the end.</p>"),
            ("Do I need to have studied Philosophy before?",
             "<p>No. If you're at A-level, we start from what you've covered in school and build from there.</p>"),
        ],
    ),
    dict(
        slug="gcse-maths", name="GCSE Maths", level="GCSE", tier="G",
        title="GCSE Maths Tutor, Online from Bath",
        desc="One-to-one GCSE Maths tutoring online, Foundation and Higher, for AQA, Edexcel and OCR. Tailored to your target grade. £32/hour, from Bath.",
        h1="GCSE Maths tutoring",
        lede="Foundation and Higher tier, taught to your exam board and target grade, from number and algebra to geometry and statistics. I sat my GCSEs recently, with 8s and 9s in 10 subjects, so the current papers are familiar to me.",
        card="Foundation and Higher tier: number, algebra, geometry and statistics.",
        boards="AQA, Edexcel, OCR",
        topics=[
            ("Number and algebra", ["Fractions, percentages and standard form", "Expressions, equations and formulae", "Graphs and sequences", "Quadratics and simultaneous equations"]),
            ("Ratio, proportion and geometry", ["Ratio and proportion", "Compound measures and rates of change", "Angles, area and volume", "Trigonometry and Pythagoras", "Transformations and vectors (Higher)"]),
            ("Probability and statistics", ["Probability, including tree diagrams", "Averages and spread", "Charts and graphs", "Sampling and cumulative frequency (Higher)"]),
        ],
        structure_h="How the exams work",
        structure=[
            "GCSE Maths is examined in three papers, including a non-calculator paper, at one of two tiers: <b>Foundation</b> (grades 1 to 5) or <b>Higher</b> (grades 4 to 9). Your school decides the tier, and sessions follow it.",
        ],
        lose=[
            "Not showing working, so method marks are lost even when the answer is wrong",
            "Algebra: rearranging formulae and expanding brackets",
            "Ratio and proportion problems set in context",
            "Unfamiliar multi-step problems where the first step isn't obvious",
        ],
        results=[("8s &amp; 9s", "across 10 GCSEs")],
        review="claire",
        faq=[
            ("Foundation or Higher tier?",
             "<p>Your school decides which tier a student is entered for. Sessions follow whichever it is. If you're unsure, raise it on the free intro call.</p>"),
            ("Which exam boards do you teach?",
             "<p>AQA, Edexcel and OCR, among others. Sessions are tailored to the board your school sits.</p>"),
            ("My child is in Year 7 to 9. Can you help?",
             "<p>Yes, see <a href=\"ks3-maths-science.html\">KS3 Maths &amp; Science</a>, at the same rates as GCSE.</p>"),
        ],
    ),
    dict(
        slug="gcse-science", name="GCSE Combined & Triple Science", level="GCSE", tier="G",
        title="GCSE Science Tutor, Combined & Triple",
        desc="One-to-one GCSE Combined and Triple Science tutoring online: Biology, Chemistry and Physics for AQA, Edexcel and OCR. £32/hour, from Bath.",
        h1="GCSE Combined &amp; Triple Science tutoring",
        lede="Biology, Chemistry and Physics, taught to your exam board, whether you're sitting Combined or Triple Science. I sat my GCSEs recently, with 8s and 9s in 10 subjects, so the current specifications are familiar to me.",
        card="Combined and Triple: Biology, Chemistry and Physics.",
        boards="AQA, Edexcel, OCR",
        topics=[
            ("Biology", ["Cell biology and organisation", "Infection and response", "Bioenergetics: photosynthesis and respiration", "Homeostasis and inheritance", "Evolution and ecology"]),
            ("Chemistry", ["Atomic structure and the periodic table", "Bonding and structure", "Quantitative chemistry", "Chemical and energy changes", "Rates of reaction and organic chemistry", "Chemical analysis, the atmosphere and resources"]),
            ("Physics", ["Energy", "Electricity", "Particle model of matter", "Atomic structure and radiation", "Forces and motion", "Waves and magnetism"]),
        ],
        structure_h="Combined or Triple?",
        structure=[
            "<b>Combined Science</b> is worth two GCSEs and covers a core of Biology, Chemistry and Physics. <b>Triple Science</b> (separate Biology, Chemistry and Physics) is three GCSEs with more content. Combined is typically examined in six papers; Triple in two per science. Your school decides which one a student sits, and I teach both.",
        ],
        lose=[
            "Rearranging equations and keeping track of units in Physics calculations",
            "Extended-response questions with no clear structure",
            "Required practicals: method, variables and evaluating results",
            "Imprecise use of key terms, such as &ldquo;energy&rdquo; versus &ldquo;force&rdquo;",
        ],
        results=[("8s &amp; 9s", "across 10 GCSEs")],
        review="claire",
        faq=[
            ("Combined or Triple Science?",
             "<p>Your school enters each student for one or the other. Combined Science is two GCSEs; Triple Science is three separate GCSEs. Sessions follow whichever your child is sitting.</p>"),
            ("Are the required practicals part of the exam?",
             "<p>Yes. Questions on the required practicals appear in the written papers, so method, variables and evaluation are all worth practising.</p>"),
            ("Which exam boards do you teach?",
             "<p>AQA, Edexcel and OCR, among others. Sessions are tailored to the board your school sits.</p>"),
        ],
    ),
    dict(
        slug="gcse-business-studies", name="GCSE Business Studies", level="GCSE", tier="G",
        title="GCSE Business Studies Tutor, Online from Bath",
        desc="One-to-one GCSE Business Studies tutoring online. Marketing, finance, operations and exam technique. £32/hour, from Bath.",
        h1="GCSE Business Studies tutoring",
        lede="Marketing, finance, operations and the exam technique that helps turn knowledge into marks. One student I tutored went from a grade 3 to a grade 8.",
        card="Marketing, finance, operations and exam technique.",
        boards="AQA, Edexcel, OCR",
        topics=[
            ("Business in the real world", ["Enterprise and entrepreneurs", "Business ownership and aims", "Stakeholders", "Technology, ethics and the economic climate"]),
            ("Operations and people", ["Production and quality", "Suppliers and customer service", "Organisational structures", "Recruitment, motivation and training"]),
            ("Marketing and finance", ["Market research and segmentation", "The marketing mix", "Sources of finance", "Cash flow, break-even and profit"]),
        ],
        structure_h="How the exams work",
        structure=[
            "GCSE Business Studies is examined in two written papers, mixing short answers, calculations and longer questions set around a business case study. The longer questions reward applying your knowledge to the business in front of you and reaching a justified conclusion.",
        ],
        lose=[
            "Describing a concept instead of applying it to the business in the question",
            "Extended answers that never reach a justified recommendation",
            "Finance calculations: break-even, margins and cash flow",
            "Imprecise definitions of key terms",
        ],
        results=[("8s &amp; 9s", "across 10 GCSEs")],
        review="sarah",
        faq=[
            ("Which exam boards do you teach?",
             "<p>AQA, Edexcel and OCR, among others. Sessions are tailored to the board your school sits.</p>"),
            ("Is there much maths in Business Studies?",
             "<p>A little. Finance questions use break-even, profit margins and cash flow, usually in a business case-study setting.</p>"),
            ("My child has written Business Studies off. Is it too late?",
             "<p>Every student is different, but one parent wrote that their daughter was on a grade 3 and finished on a grade 8. Book a free intro call and we can talk through where your child is now.</p>"),
        ],
    ),
    dict(
        slug="ks3-maths-science", name="KS3 Maths & Science", level="KS3", tier="G", suffix=" (Years 7 to 9)",
        title="KS3 Maths & Science Tutor, Years 7-9",
        desc="One-to-one KS3 Maths and Science tutoring online for Years 7 to 9, tailored to what's covered in school. £32/hour, from Bath.",
        h1="KS3 Maths &amp; Science tutoring",
        lede="Years 7 to 9 Maths and Science, tailored to what the student is covering in school. A confident start can make the step up to GCSE feel smaller.",
        card="Years 7 to 9 Maths and Science, tailored to what's covered in school.",
        boards="School curriculum",
        boards_label="Follows",
        topics=[
            ("Maths", ["Number, fractions and percentages", "Algebra and equations", "Ratio and proportion", "Geometry and measures", "Probability and statistics"]),
            ("Science", ["Biology: cells, body systems and ecosystems", "Chemistry: particles, reactions and the periodic table", "Physics: forces, energy, electricity and waves"]),
        ],
        structure_h="Why start at KS3",
        structure=[
            "In many schools, GCSE content starts to appear in Year 9. Solid foundations in Years 7 and 8, especially in algebra, fractions and ratio, can make GCSE Maths and Science less of a jump.",
        ],
        lose=[
            "Fractions, decimals and percentages that were never quite secure",
            "Algebra introduced before the number work underneath it is solid",
            "Science vocabulary that gets muddled as topics pile up",
        ],
        lose_h="Where gaps often start",
        topics_intro="Sessions follow what the student is covering in school. These are the main areas.",
        structure_kicker="Why KS3", lose_kicker="Common gaps",
        results_h="Building towards GCSE",
        results_p="I sat my GCSEs recently, so I have a clear picture of what KS3 work leads into.",
        results=[("8s &amp; 9s", "across 10 GCSEs")],
        review=None,
        faq=[
            ("Which years does KS3 cover?",
             "<p>Years 7 to 9, so students aged roughly 11 to 14. For younger students sitting entrance exams, see <a href=\"11-plus-maths.html\">11+ and 13+ entrance Maths</a>.</p>"),
            ("Is it the same price as GCSE?",
             "<p>Yes: &pound;32 per hour, or &pound;160 for a block of five sessions.</p>"),
            ("Do you follow the school curriculum?",
             "<p>Sessions are tailored to what the student is covering in school.</p>"),
        ],
    ),
    dict(
        slug="11-plus-maths", name="11+ & 13+ Entrance Maths", level="Entrance", tier="G",
        level_label="Years 5 and 6, plus 13+", kicker="Entrance exams",
        title="11+ & 13+ Maths Tutor, Online from Bath",
        desc="One-to-one Maths tutoring online for 11+ and 13+ entrance exams: private school papers, the ISEB Pre-Test and grammar school 11+. Years 5 and 6, £32/hour.",
        h1="11+ &amp; 13+ entrance exam Maths tutoring",
        lede="One-to-one Maths preparation for private school 11+ papers, the ISEB Pre&#8209;Test, grammar school 11+ and 13+ entrance. We work on secure core arithmetic first, then on the problem solving and speed these papers need.",
        card="Maths for private school 11+, the ISEB Pre&#8209;Test, grammar school 11+ and 13+ entrance. Years 5 and 6.",
        boards="Private &amp; grammar 11+, 13+, ISEB&nbsp;Pre&#8209;Test",
        boards_label="Exams",
        topics=[
            ("Number and arithmetic", ["Place value, rounding and negative numbers", "Written and mental methods for all four operations", "Fractions, decimals and percentages", "Factors, multiples, primes, squares and cubes"]),
            ("Problem solving and algebra", ["Multi-step word problems", "Ratio and proportion", "Sequences, simple equations and formulae", "Reasoning and logic questions"]),
            ("Geometry, measures and data", ["Area, perimeter and volume", "Angles, shapes and coordinates", "Units, time and money", "Tables, charts and averages"]),
        ],
        topics_intro="Sessions follow the exams your child is sitting and the dates they're sitting them. These are the main areas of entrance exam Maths.",
        structure_kicker="The exams", structure_h="How entrance exams work",
        structure=[
            "Formats vary from school to school. Many independent schools set their own papers, some use the <b>ISEB Common Pre&#8209;Test</b> (taken online, and it adapts to the student's answers), and grammar school 11+ tests are set by providers such as GL Assessment. <b>13+ entrance</b> has its own papers, sat later.",
            "Most entrance tests include English and reasoning as well as Maths. My sessions cover the Maths, planned around the dates and formats of the schools you're applying to.",
        ],
        lose=[
            "Rushing, and arithmetic slips under time pressure",
            "Word problems where the maths is hidden in the wording",
            "Topics a little beyond what's been covered in school so far",
            "Not checking answers, or spending too long on one question",
        ],
        results=[("8s &amp; 9s", "across 10 GCSEs"), ("A*A*A", "at A-level")],
        results_h="My own results",
        results_p="Sessions are one-to-one and paced to your child, planned around the exams they're sitting.",
        review=None,
        faq=[
            ("Do you cover English and reasoning too?",
             "<p>No, I teach the Maths. Most entrance tests also include English and verbal or non-verbal reasoning, so plan for those separately.</p>"),
            ("When should we start?",
             "<p>Many families start in Year 5, a year before the 11+. I take students in Years 5 and 6, and for 13+ entrance.</p>"),
            ("Which exams do you prepare for?",
             "<p>Private school 11+ papers, the ISEB Common Pre&#8209;Test, grammar school 11+ tests and 13+ entrance. Tell me which schools you're applying to on the free intro call and we'll plan around their exams.</p>"),
            ("Is it the same price as GCSE?",
             "<p>Yes: &pound;32 per hour, or &pound;160 for a block of five sessions.</p>"),
        ],
    ),
]
BY_SLUG = {s["slug"]: s for s in SUBJECTS}

REVIEWS = {
    "sarah": dict(
        quote="My daughter was sitting at a grade 3 in Business Studies when we came to Ali. She finished with a grade 8 and she is absolutely over the moon, and honestly so are we. Ali took a subject she had written herself off in and gave her the confidence to actually enjoy it. We can't recommend him highly enough.",
        who="Sarah, parent", ctx="GCSE Business Studies, grade 3 to 8", hl="She finished with a grade 8"),
    "claire": dict(
        quote="Ali tutored my son in Maths and Chemistry during Year 11 and was a huge help. He was very organised, kind and supportive, and really helped my son to get to grips with what he was finding difficult. We were delighted with the exam results and I would highly recommend him.",
        who="Claire, parent", ctx="GCSE Maths &amp; Chemistry, Year 11", hl="We were delighted with the exam results"),
}


def wa_url(text="Hi Ali, I'd like to ask about tutoring."):
    return f"https://wa.me/{WA_NUMBER}?text={quote(text)}"


def photo(sizes, extra=""):
    return ('<img src="assets/ali-aljawabra.jpg" '
            'srcset="assets/ali-160.webp 160w, assets/ali-330.webp 330w, assets/ali-660.webp 660w" '
            f'sizes="{sizes}" alt="Ali Aljawabra, GCSE and A-level tutor in Bath" width="640" height="640"{extra}>')


def price_text(tier):
    t = TIERS[tier]
    return f"&pound;{t['rate']}"


# --------------------------------------------------------------------------
# Components
# --------------------------------------------------------------------------
def a(href, text, cls="", ext=False):
    extra = ' target="_blank" rel="noopener"' if ext else ""
    c = f' class="{cls}"' if cls else ""
    sr = '<span class="sr-only"> (opens in a new tab)</span>' if ext else ""
    return f'<a{c} href="{href}"{extra}>{text}{sr}</a>'


def call_btn(text="Book a free intro call", cls="btn btn-primary"):
    return a(CALL, text, cls, ext=True)


def review_html(key, light=False):
    r = REVIEWS[key]
    q = esc(r["quote"], quote=False)
    if r.get("hl"):
        phrase = esc(r["hl"], quote=False)
        q = q.replace(phrase, f"<mark>{phrase}</mark>", 1)
    cls = "quote quote-card" if light else "quote"
    return (f'<figure class="{cls}"><blockquote><p>{q}</p></blockquote>'
            f'<figcaption><span class="avatar" aria-hidden="true">{r["who"][0]}</span>'
            f'<span><b>{r["who"]}</b><span>{r["ctx"]}</span></span></figcaption></figure>')


def faq_item(q, answer_html):
    return (f'<details class="faq-item"><summary>{q}</summary>'
            f'<div class="answer">{answer_html}</div></details>')


LEVEL_GROUPS = [("A-level", "A-level", "A"), ("GCSE", "GCSE", "G"), ("KS3", "Key Stage 3", "G"), ("Entrance", "Entrance exams", "G")]


def subject_row(s):
    return (f'<li><a class="row-link" href="{s["slug"]}.html"><span class="row-name">{s["name"].replace("&", "&amp;")}</span>'
            f'<span class="row-desc">{s["card"]}</span><span class="row-go" aria-hidden="true"></span></a></li>')


def subject_index(exclude=None, compact=False):
    groups = []
    for level, label, tier in LEVEL_GROUPS:
        subs = [s for s in SUBJECTS if s["level"] == level and s["slug"] != exclude]
        if subs:
            groups.append(f'<div class="index-group"><div class="index-label"><h3>{label}</h3>'
                          f'<p>&pound;{TIERS[tier]["rate"]} an hour</p></div>'
                          f'<ul class="index-list">{"".join(subject_row(s) for s in subs)}</ul></div>')
    return f'<div class="index{" index-compact" if compact else ""}">{"".join(groups)}</div>'





def tier_html(key):
    t = TIERS[key]
    subs = [s for s in SUBJECTS if s["tier"] == key]
    items = "".join(f'<li>{a(s["slug"] + ".html", s["name"].replace("&", "&amp;") + s.get("suffix", ""))}</li>' for s in subs)
    return (f'<div class="tier"><h3 class="tier-label">{t["label"].replace("&", "&amp;")}</h3>'
            f'<p class="tier-price"><span class="amount">&pound;{t["block"]}</span><span class="unit">for five sessions</span></p>'
            f'<p class="tier-per">&pound;{t["rate"]} an hour, paid upfront</p>'
            f'<ul class="check-list">{items}</ul>'
            f'<div class="tier-actions">{a(t["stripe"], "Book a block of five", "btn btn-ghost", ext=True)}'
            f'{a(CALL, "or start with a free intro call", "text-link", ext=True)}</div></div>')


def slip_html(rows, note=None, simple=False):
    """A printed-results-slip table. rows: (subject, board, grade, detail, circled).
    simple=True: two columns, label and result, for the short slips on subject pages."""
    trs = ""
    for subj, board, grade, detail, circled in rows:
        det = f'<span class="circled">{detail}</span>' if circled else detail
        sub = f"<small>{board}</small>" if board else ""
        detail_cell = "" if simple else f'<td class="detail">{det}</td>'
        trs += f'<tr><th scope="row">{subj}{sub}</th><td class="grade">{grade}</td>{detail_cell}</tr>'
    n = f'<p class="slip-note" aria-hidden="true">{note}</p>' if note else ""
    return (f'<div class="slip{" slip-simple" if simple else ""}"><div class="slip-head" aria-hidden="true"><span>Results</span><span>Ali Aljawabra</span></div>'
            f'<table><caption class="sr-only">Exam results</caption><tbody>{trs}</tbody></table>{n}</div>')


MY_RESULTS = [
    ("A-level Philosophy", "AQA", "A*", "196/200", False),
    ("A-level Economics", "Edexcel A", "A*", "96% in Paper 3", False),
    ("A-level Maths", "", "A", "", False),
    ("GCSEs", "10 subjects", "8s &amp; 9s", "", False),
]


def cta_band(h="Let's see if I can help", p="Book a free intro call. We'll talk through what's needed, and whether I'm the right tutor.", wa_text=None, id_=None):
    wa = wa_url(wa_text) if wa_text else wa_url()
    sid = f' id="{id_}"' if id_ else ""
    return (f'<section class="cta-band"{sid}><div class="wrap cta-grid"><div><h2>{h}</h2><p>{p}</p></div>'
            f'<div class="cta-actions">{call_btn("Book a free intro call", "btn btn-light")}'
            f'<ul class="cta-contacts"><li>{a("tel:" + PHONE_TEL, "Call " + PHONE)}</li>'
            f'<li>{a(wa, "WhatsApp me", ext=True)}</li><li>{a("mailto:" + EMAIL, "Email me")}</li></ul></div></div></section>')


NAV = [("Subjects", "index.html#subjects", None), ("Pricing", "pricing.html", "pricing"),
       ("About", "about.html", "about"), ("FAQ", "index.html#faq", None)]


def nav_html(current, nav_cta=True):
    def links(cls_a=""):
        out = []
        for label, href, key in NAV:
            cur = ' aria-current="page"' if key and key == current else ""
            out.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
        return "".join(out)
    panel = "".join(
        f'<a href="{href}"' + (' aria-current="page"' if key and key == current else "") + f'>{label}</a>'
        for label, href, key in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="nav">
  <div class="wrap nav-bar">
    <a class="brand" href="index.html"><img src="assets/mark.svg" alt="" width="34" height="34">Ali Tutors</a>
    <nav class="nav-links" aria-label="Main"><ul>{links()}</ul></nav>
    {a(CALL, "Free intro call", "btn btn-primary btn-sm nav-cta", ext=True) if nav_cta else '<span class="nav-cta"></span>'}
    <details class="menu"><summary aria-label="Menu"><span class="bars"></span></summary>
      <nav class="menu-panel" aria-label="Menu">{panel}</nav>
    </details>
  </div>
</header>'''


def footer_html():
    def col(level):
        return "".join(f'<li>{a(s["slug"] + ".html", s["name"].replace("&", "&amp;"))}</li>' for s in SUBJECTS if s["level"] in level)
    return f'''<footer class="footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand" href="index.html"><img src="assets/mark-light.svg" alt="" width="34" height="34">Ali Tutors</a>
        <p>One-to-one GCSE, A-level and 11+ tutoring, online, from Bath. DBS checked.</p>
        <p>{a("tel:" + PHONE_TEL, PHONE)}<br>{a(wa_url(), "WhatsApp", ext=True)}<br>{a("mailto:" + EMAIL, EMAIL)}</p>
      </div>
      <div><h2>A-level</h2><ul>{col(("A-level",))}</ul></div>
      <div><h2>GCSE, KS3 &amp; 11+</h2><ul>{col(("GCSE", "KS3", "Entrance"))}</ul></div>
      <div><h2>Site</h2><ul>
        <li><a href="pricing.html">Pricing</a></li>
        <li><a href="about.html">About Ali</a></li>
        <li><a href="index.html#faq">FAQ</a></li>
        <li><a href="terms.html">Terms</a></li>
        <li><a href="privacy.html">Privacy Policy</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">&copy; {YEAR} Ali Aljawabra, trading as Ali Tutors. Bath &amp; online.</div>
  </div>
</footer>'''


def head(title, desc, path, jsonld=None, noindex=False):
    url = SITE + "/" if path == "index.html" else f"{SITE}/{path}"
    t, d = esc(title), esc(desc)
    robots = ('<meta name="robots" content="noindex">\n' if noindex else
              '<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">\n')
    if path == "index.html" and not noindex:
        if GSC_VERIFICATION:
            robots += f'<meta name="google-site-verification" content="{esc(GSC_VERIFICATION)}">\n'
        if BING_VERIFICATION:
            robots += f'<meta name="msvalidate.01" content="{esc(BING_VERIFICATION)}">\n'
    meta_social = "" if noindex else f'''<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Ali Tutors">
<meta property="og:locale" content="en_GB">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:image" content="{SITE}/assets/og-card.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Ali Aljawabra, GCSE and A-level tutor, Bath and online">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{SITE}/assets/og-card.jpg">
'''
    analytics = (f'<script defer src="https://cloud.umami.is/script.js" data-website-id="{esc(UMAMI_WEBSITE_ID)}"></script>\n'
                 if UMAMI_WEBSITE_ID else "")
    ld = "".join(f'<script type="application/ld+json">\n{json.dumps(j, indent=2, ensure_ascii=False)}\n</script>\n' for j in (jsonld or []))
    return f'''<!DOCTYPE html>
<!-- Generated by tools/build_site.py. Edit that file and re-run it; changes made directly here will be overwritten. -->
<html lang="en-GB">
<head>
<meta charset="utf-8">
<title>{t}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{d}">
<meta name="theme-color" content="#0F2A4A">
{robots}{meta_social}<link rel="icon" href="favicon.ico" sizes="48x48">
<link rel="icon" type="image/svg+xml" href="assets/mark.svg">
<link rel="icon" type="image/png" sizes="512x512" href="assets/icon-512.png">
<link rel="apple-touch-icon" sizes="180x180" href="assets/icon-180.png">
<link rel="preload" href="assets/fonts/fraunces-600.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/figtree-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/site.css">
{analytics}{ld}</head>'''


MENU_JS = """<script>
/* Close the phone menu after a link is tapped, on Escape, or on a tap outside it. */
document.addEventListener('click', function (e) {
  var m = document.querySelector('.menu[open]');
  if (m && (!m.contains(e.target) || e.target.closest('.menu-panel a'))) m.open = false;
});
document.addEventListener('keydown', function (e) {
  var m = document.querySelector('.menu[open]');
  if (e.key === 'Escape' && m) { m.open = false; m.querySelector('summary').focus(); }
});
</script>"""


EVENTS = [(CALL, "intro-call"), ("https://wa.me/", "whatsapp"), ("tel:", "phone"),
          ("mailto:", "email"), ("https://buy.stripe.com/", "book-block")]


def tag_events(doc):
    """With analytics on, name the clicks that matter so they show up as events."""
    if not UMAMI_WEBSITE_ID:
        return doc
    def add(m):
        for prefix, name in EVENTS:
            if m.group(1).startswith(prefix):
                return m.group(0).replace("<a ", f'<a data-umami-event="{name}" ', 1)
        return m.group(0)
    return re.sub(r'<a [^>]*href="([^"]*)"[^>]*>', add, doc)


def absolutize(doc):
    """Make every internal link root-relative, so pages work from any path (the 404 page is
    served at whatever URL was mistyped) and nothing links to /index.html instead of /."""
    def fix(url):
        if re.match(r"(https?:|mailto:|tel:|#|/|data:)", url):
            return url
        if url == "index.html" or url.startswith("index.html#"):
            return "/" + url[len("index.html"):]
        return "/" + url
    doc = re.sub(r'(href|src)="([^"]*)"', lambda m: f'{m.group(1)}="{fix(m.group(2))}"', doc)
    doc = re.sub(r'srcset="([^"]*)"',
                 lambda m: 'srcset="' + ", ".join(fix(p.strip().split(" ")[0]) + " " + p.strip().split(" ")[1]
                                                    for p in m.group(1).split(",")) + '"', doc)
    return doc


def page(path, title, desc, body, current=None, jsonld=None, noindex=False, nav_cta=True):
    doc = (head(title, desc, path, jsonld, noindex) + "\n<body>\n" + nav_html(current, nav_cta)
           + '\n<main id="main">\n' + body + "\n</main>\n" + footer_html() + "\n" + MENU_JS + "\n</body>\n</html>\n")
    doc = tag_events(absolutize(doc))
    (OUT / path).write_text(doc, encoding="utf-8")
    print("wrote", path)


def breadcrumb_ld(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(trail)]}


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------
def season_text(month):
    """Sep to Jan: mocks. Feb to May: summer exams. Jun to Aug: next school year."""
    if 2 <= month <= 5:
        return "Now booking for the summer exams"
    if 6 <= month <= 8:
        return "Now booking for the new school year"
    return "Now booking ahead of mocks"


SEASON_JS = """<script>
/* Keeps the hero badge in season even if the site isn't rebuilt (same rule as season_text). */
(function () {
  var m = new Date().getMonth() + 1;
  var text = (m >= 2 && m <= 5) ? 'Now booking for the summer exams'
    : (m >= 6 && m <= 8) ? 'Now booking for the new school year' : 'Now booking ahead of mocks';
  document.querySelectorAll('[data-season]').forEach(function (b) { b.textContent = text; });
})();
</script>"""


def build_home():
    faqs = [
        ("Which exam boards do you cover?",
         "<p>Content is tailored to whichever exam board the student's school uses (AQA, Edexcel, OCR and others, depending on the subject) for GCSE Maths, Combined Science, Triple Science, Business Studies, and A-level Maths, Economics and Philosophy. Each subject page lists what's covered.</p>"),
        ("What grades did you get?",
         "<p>A* in Economics and A* in Philosophy, and an A in Maths, including 196/200 across the AQA Philosophy papers and 96% in Paper 3 of Edexcel A Economics. At GCSE, grades 8 and 9 across 10 subjects. I sat all of these recently, so the specs and mark schemes I teach from are the current ones.</p>"),
        ("Do you tutor students younger than GCSE?",
         "<p>Yes. <a href=\"ks3-maths-science.html\">KS3 Maths and Science</a> for Years 7 to 9, tailored to what the student's covering in school, and <a href=\"11-plus-maths.html\">Maths for 11+ and 13+ entrance exams</a>, from Year 5. Both are at the same rates as GCSE.</p>"),
        ("Are sessions online or in person?",
         "<p>Online only, held via Google Meet. No travel time, and easier to fit around school and other commitments.</p>"),
        ("What happens after the free intro call?",
         "<p>If it's a good fit, you book a block of five weekly sessions. There's no obligation to continue after the call itself.</p>"),
        ("How does payment work, and what if I need to cancel?",
         "<p>Blocks of five are paid upfront, before the sessions begin. Cancel before a block starts for a full refund. Once a block is underway, any sessions not yet taken are refunded; sessions already delivered are not. Full details are on the <a href=\"pricing.html\">pricing page</a>.</p>"),
    ]

    body = f'''
<section class="hero" id="top">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <div class="hero-id"><strong>Ali Aljawabra</strong><span>GCSE, A-level &amp; 11+ tutor</span></div>
      <p class="season-pill" data-season>{season_text(date.today().month)}</p>
      <p class="eyebrow">GCSE, A-level &amp; 11+ tutor &middot; Bath and online</p>
      <h1>GCSE &amp; A-level tutoring from someone who&rsquo;s <mark>been through it recently</mark>.</h1>
      <p class="lede">I'm Ali, a tutor in Bath. I got <strong>8s and 9s in 10 GCSEs</strong> and <strong>A*A*A at A&#8209;level</strong>, and the specifications I studied are the ones students sit today. Now in my second year of tutoring, before I start at Durham in 2027.</p>
      <div class="cta-row">{call_btn()}<a class="link-arrow" href="#subjects">See subjects and prices</a></div>
      <ul class="ticks"><li>DBS checked</li><li>Online via Google Meet</li><li>Unused sessions refunded</li></ul>
    </div>
    <div class="hero-visual">
      <figure class="portrait">{photo("(max-width: 860px) 72px, 380px", ' fetchpriority="high"')}</figure>
      <p class="sticky" data-season>{season_text(date.today().month)}</p>
      <p class="hand-note" aria-hidden="true">that's me<svg viewBox="0 0 64 52" width="64" height="52"><path d="M56 5C42 9 24 18 15 40" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/><path d="M8 29l7 12 11-6" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></p>
    </div>
  </div>
</section>

<section class="section proof" id="results">
  <div class="wrap proof-grid">
    <div class="proof-copy">
      <p class="kicker">for the record</p>
      <h2>My own exam results</h2>
      <p class="section-sub">I sat these exams recently, so the specifications and mark schemes I teach from are the current ones, and I remember what it's like to prepare for them.</p>
      <p><a class="link-arrow" href="about.html">More about me</a></p>
    </div>
    {slip_html(MY_RESULTS)}
  </div>
</section>

<section class="section alt" id="reviews">
  <div class="wrap">
    <div class="section-head"><p class="kicker">from parents</p><h2>What parents say</h2></div>
    <div class="quotes">{review_html("sarah")}{review_html("claire")}</div>
  </div>
</section>

<section class="section" id="subjects">
  <div class="wrap">
    <div class="section-head split">
      <div><p class="kicker">pick a subject</p><h2>What I teach</h2></div>
      <p class="section-sub">One-to-one, tailored to the student's exam board and target grade. Each subject page covers the topics, how the exams work and the price.</p>
    </div>
    {subject_index()}
  </div>
</section>

<section class="section alt" id="pricing">
  <div class="wrap">
    <div class="section-head split">
      <div><p class="kicker">clear prices</p><h2>Prices, in blocks of five</h2></div>
      <p class="section-sub">Weekly sessions, booked five at a time for a steady routine. <strong>Any session you don't use is refunded.</strong></p>
    </div>
    <div class="tiers">{tier_html("A")}{tier_html("G")}</div>
    <p class="fine">Cancel before a block starts for a full refund. {a("pricing.html", "How blocks, payment and refunds work", "link-arrow")}</p>
  </div>
</section>

<section class="section" id="how">
  <div class="wrap">
    <div class="section-head"><p class="kicker">three steps</p><h2>How it works</h2></div>
    <ol class="steps">
      <li class="step"><span class="n" aria-hidden="true">1</span><h3>Free intro call</h3><p>We talk through what's needed: the subject, the exam board and the target grade. Parents or A-level students can book it. No obligation.</p></li>
      <li class="step"><span class="n" aria-hidden="true">2</span><h3>Book a block of five</h3><p>Five weekly sessions, booked in advance and paid upfront. Any you don't use are refunded.</p></li>
      <li class="step"><span class="n" aria-hidden="true">3</span><h3>Sessions on Google Meet</h3><p>Online, so there's no travel, which makes it easier to fit around school and other commitments.</p></li>
    </ol>
  </div>
</section>

<section class="section alt" id="faq">
  <div class="wrap faq-grid">
    <div class="faq-aside">
      <p class="kicker">good questions</p>
      <h2>Questions parents ask</h2>
      <p class="section-sub">Not answered here? Send me a message and I'll get back to you.</p>
      <p>{a(wa_url(), "WhatsApp me", "btn btn-ghost", ext=True)}</p>
    </div>
    <div class="faq-list">{"".join(faq_item(q, ans) for q, ans in faqs)}</div>
  </div>
</section>

{cta_band(id_="contact")}
{SEASON_JS}'''

    offers = [{"@type": "Offer", "url": f"{SITE}/{s['slug']}.html",
               "itemOffered": {"@type": "Service", "name": s["name"].replace("&amp;", "&") + " Tutoring"},
               "price": str(TIERS[s["tier"]]["rate"]), "priceCurrency": "GBP"} for s in SUBJECTS]
    business = {
        "@context": "https://schema.org", "@type": "LocalBusiness", "@id": f"{SITE}/#business", "name": "Ali Tutors",
        "description": "One-to-one GCSE and A-level tutoring in Maths, Science, Business Studies, Economics and Philosophy, held online via Google Meet from Bath.",
        "image": f"{SITE}/assets/ali-aljawabra.jpg", "logo": f"{SITE}/assets/icon-512.png", "url": f"{SITE}/",
        "telephone": PHONE_TEL, "email": EMAIL,
        "knowsAbout": [s["name"].replace("&amp;", "&") for s in SUBJECTS],
        "areaServed": [{"@type": "City", "name": "Bath"}, {"@type": "Country", "name": "United Kingdom"}],
        "address": {"@type": "PostalAddress", "addressLocality": "Bath", "addressCountry": "GB"},
        "priceRange": "£32-£35", "makesOffer": offers,
    }
    if SAME_AS:
        business["sameAs"] = SAME_AS
    ld = [business, {"@context": "https://schema.org", "@type": "WebSite", "@id": f"{SITE}/#website", "url": f"{SITE}/",
                     "name": "Ali Tutors", "inLanguage": "en-GB", "publisher": {"@id": f"{SITE}/#business"}}]
    page("index.html", "GCSE & A-level Tutor in Bath, Online · Ali Tutors",
         "Online GCSE, A-level and 11+ tutoring from Bath: Maths, Science, Business Studies, Economics and Philosophy. 8s and 9s in 10 GCSEs, A*A*A at A-level.",
         body, jsonld=ld)


def build_subject(s):
    t = TIERS[s["tier"]]
    name_h = s["name"].replace("&", "&amp;")
    kicker = s.get("kicker") or {"A-level": "A-level", "GCSE": "GCSE", "KS3": "Key Stage 3 &middot; Years 7 to 9"}[s["level"]]
    topics = "".join(f'<div class="topic"><h3>{h}</h3><ul class="check-list">{"".join(f"<li>{i}</li>" for i in items)}</ul></div>' for h, items in s["topics"])
    topics_note = f'<p class="section-sub" style="margin-top:18px;font-size:14.5px;color:var(--muted)">{s["topics_note"]}</p>' if s.get("topics_note") else ""
    structure = "".join(f"<p>{p}</p>" for p in s["structure"])
    lose = "".join(f"<li>{x}</li>" for x in s["lose"])
    lose_h = s.get("lose_h", "Where marks are often lost")
    results_box = slip_html([(lbl, "", num, "", False) for num, lbl in s["results"]], simple=True)
    results_h = s.get("results_h", "Taught by someone who sat the papers")
    results_p = s.get("results_p", HONEST_RECENT)
    if s["review"]:
        results_section = (f'<section class="section alt"><div class="wrap"><div class="two-col">'
                           f'<div><p class="kicker">Results</p><h2>{results_h}</h2>'
                           f'<div class="prose"><p>{results_p}</p></div><div class="slip-wrap">{results_box}</div></div>'
                           f'<div>{review_html(s["review"], light=True)}</div></div></div></section>')
    else:
        results_section = (f'<section class="section alt"><div class="wrap"><div class="two-col">'
                           f'<div><p class="kicker">Results</p><h2>{results_h}</h2>'
                           f'<div class="prose"><p>{results_p}</p></div></div>'
                           f'<div>{results_box}</div></div></div></section>')
    glance_rows = [
        ("Level", s.get("level_label") or {"A-level": "A-level", "GCSE": "GCSE", "KS3": "Years 7 to 9"}[s["level"]]),
        (s.get("boards_label", "Exam boards"), s["boards"]),
        ("Format", "Online, one-to-one"),
        ("Rate", f"&pound;{t['rate']} / hour"),
        ("Block of five", f"&pound;{t['block']}"),
    ]
    glance = "".join(f'<div class="row"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in glance_rows)
    others_all = subject_index(exclude=s["slug"], compact=True)

    wa_msg = f"Hi Ali, I'd like to ask about {s['name']} tutoring."
    body = f'''
<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span aria-current="page">{name_h}</span></nav></div>

<section class="page-hero">
  <div class="wrap page-hero-grid">
    <div>
      <p class="kicker">{kicker}</p>
      <h1>{s["h1"]}</h1>
      <p class="lede">{s["lede"]}</p>
      <div class="cta-row">{call_btn()}<a class="link-arrow" href="#rates">See the price: &pound;{t['rate']} an hour</a></div>
      <ul class="ticks"><li>Online via Google Meet</li><li>DBS checked</li><li>Unused sessions refunded</li></ul>
    </div>
    <aside class="glance" aria-labelledby="glance-h"><h2 id="glance-h">At a glance</h2><dl>{glance}</dl></aside>
  </div>
</section>

<section class="section alt" id="topics">
  <div class="wrap">
    <div class="section-head"><p class="kicker">Topics</p><h2>What we'll cover</h2><p class="section-sub">{s.get("topics_intro", "Sessions follow your exam board's specification and your target grade. These are the main areas.")}</p></div>
    <div class="topics{' n4' if len(s['topics']) == 4 else ''}">{topics}</div>{topics_note}
  </div>
</section>

<section class="section">
  <div class="wrap two-col">
    <div><p class="kicker">{s.get("structure_kicker", "The exams")}</p><h2>{s["structure_h"]}</h2><div class="prose">{structure}</div></div>
    <div><p class="kicker">{s.get("lose_kicker", "Exam technique")}</p><h2>{lose_h}</h2><ul class="lose-list">{lose}</ul></div>
  </div>
</section>

{results_section}

<section class="section" id="rates">
  <div class="wrap">
    <div class="pricebar">
      <div>
        <p class="kicker">Rates</p>
        <p class="tier-price"><span class="amount">&pound;{t["block"]}</span><span class="unit">for five sessions</span></p>
        <p class="pricebar-sub">&pound;{t["rate"]} an hour, paid upfront. Any session you don't use is refunded. {a("pricing.html", "How blocks and refunds work", "text-link")}</p>
      </div>
      <div class="actions">{call_btn()}{a(t["stripe"], "Book a block of five", "btn btn-ghost", ext=True)}</div>
    </div>
  </div>
</section>

<section class="section alt" id="faq">
  <div class="wrap">
    <div class="section-head"><p class="kicker">FAQ</p><h2>{name_h}: common questions</h2></div>
    <div class="faq-list">{"".join(faq_item(q, ans) for q, ans in s["faq"])}</div>
  </div>
</section>

<section class="section more-subjects">
  <div class="wrap">
    <div class="section-head"><p class="kicker">More subjects</p><h2>Also tutoring</h2></div>
    {others_all}
  </div>
</section>

{cta_band(wa_text=wa_msg)}'''

    plain_name = s["name"].replace("&amp;", "&")
    ld = [
        {"@context": "https://schema.org", "@type": "Service", "name": plain_name + " Tutoring", "serviceType": "Private tutoring",
         "description": s["desc"],
         "provider": {"@type": "LocalBusiness", "@id": f"{SITE}/#business", "name": "Ali Tutors", "url": SITE + "/"},
         "areaServed": [{"@type": "City", "name": "Bath"}, {"@type": "Country", "name": "United Kingdom"}],
         "offers": {"@type": "Offer", "price": str(t["rate"]), "priceCurrency": "GBP", "url": f"{SITE}/{s['slug']}.html"}},
        breadcrumb_ld([("Home", SITE + "/"), (plain_name, f"{SITE}/{s['slug']}.html")]),
    ]
    page(s["slug"] + ".html", s["title"] + " · Ali Tutors", s["desc"], body, jsonld=ld)


def build_pricing():
    rows = "".join(
        f'<tr><td>{a(s["slug"] + ".html", s["name"].replace("&", "&amp;"))}</td><td>{ {"Entrance": "11+ and 13+"}.get(s["level"], s["level"])}</td>'
        f'<td class="num">&pound;{TIERS[s["tier"]]["rate"]}</td><td class="num">&pound;{TIERS[s["tier"]]["block"]}</td></tr>'
        for s in SUBJECTS)
    body = f'''
<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span aria-current="page">Pricing</span></nav></div>
<section class="page-hero">
  <div class="wrap">
    <p class="kicker">Rates</p>
    <h1>Pricing, in blocks of five</h1>
    <p class="lede">Sessions are booked in blocks of five for steadier weekly progress, rather than one-off lessons. Any sessions you don't take are always refunded.</p>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2 class="sr-only">Prices by level</h2>
    <div class="tiers">{tier_html("A")}{tier_html("G")}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><p class="kicker">Every subject</p><h2>All rates at a glance</h2></div>
    <div class="table-wrap"><table class="rates">
      <thead><tr><th scope="col">Subject</th><th scope="col">Level</th><th scope="col">Per hour</th><th scope="col">Block of five</th></tr></thead>
      <tbody>{rows}</tbody>
    </table></div>
  </div>
</section>

<section class="section alt" id="how">
  <div class="wrap">
    <div class="section-head"><p class="kicker">How it works</p><h2>From first call to first session</h2></div>
    <ol class="steps">
      <li class="step"><span class="n" aria-hidden="true">1</span><h3>Free intro call</h3><p>A free call to talk through what's needed. If it's a good fit, you book a block. There's no obligation to continue after the call.</p></li>
      <li class="step"><span class="n" aria-hidden="true">2</span><h3>Pay for a block of five</h3><p>Blocks of five are paid upfront, before the sessions begin.</p></li>
      <li class="step"><span class="n" aria-hidden="true">3</span><h3>Book your session times</h3><p>After paying, you book all five sessions, ideally the same day and time each week. You get a Google Meet link before the first session.</p></li>
    </ol>
  </div>
</section>

<section class="section" id="policy">
  <div class="wrap">
    <div class="section-head"><p class="kicker">Policies</p><h2>Payment, rescheduling and refunds</h2></div>
    <dl class="policy">
      <div class="row"><dt>Payment</dt><dd>Blocks of five are paid upfront, before the sessions begin.</dd></div>
      <div class="row"><dt>Rescheduling</dt><dd>Let me know as early as possible and we'll find another time within the same block.</dd></div>
      <div class="row"><dt>Cancelling before a block starts</dt><dd>Cancel before a block starts for a full refund.</dd></div>
      <div class="row"><dt>Once a block is underway</dt><dd>Any sessions not yet taken are refunded. Sessions already delivered are not.</dd></div>
      <div class="row"><dt>After the free intro call</dt><dd>No obligation. You only book a block if it's a good fit.</dd></div>
    </dl>
    <p style="margin-top:20px">{a("terms.html", "Read the full terms", "text-link")}</p>
  </div>
</section>

{cta_band("Questions before you book?", "Book a free intro call, or call, message on WhatsApp or email any time.")}'''
    page("pricing.html", "Pricing: Blocks of Five from £160 · Ali Tutors",
         "Tutoring rates from Ali Tutors: £35/hour for A-level and £32/hour for GCSE, KS3 and 11+, booked in blocks of five. Unused sessions are always refunded.",
         body, current="pricing", jsonld=[breadcrumb_ld([("Home", SITE + "/"), ("Pricing", f"{SITE}/pricing.html")])])


def build_about():
    body = f'''
<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span aria-current="page">About</span></nav></div>
<section class="page-hero">
  <div class="wrap about-grid">
    <div>
      <p class="kicker">About</p>
      <h1>Hi, I'm Ali</h1>
      <p class="lede">I'm Ali Aljawabra, a Bath-based tutor in my second year of tutoring, before I start at Durham in 2027. I tutor GCSE and A-level students one-to-one over Google Meet.</p>
      <div class="cta-row">{call_btn()}<a class="link-arrow" href="pricing.html">See pricing</a></div>
    </div>
    <figure class="portrait about-portrait">{photo("(max-width: 860px) 240px, 360px", ' fetchpriority="high"')}</figure>
  </div>
</section>

<section class="section alt">
  <div class="wrap two-col">
    <div>
      <p class="kicker">Background</p>
      <h2>A tutor who sat these exams recently</h2>
    </div>
    <div class="prose">
      <p>I sat these papers recently, so the specifications and mark schemes I teach from are the current ones.</p>
      <p>Sessions are one-to-one and tailored to the student's exam board and target grade.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="proof-grid">
      <div><p class="kicker">Results</p><h2>My own grades</h2><p class="section-sub">Sat recently, so the specifications and mark schemes I teach from are the current ones.</p></div>
      {slip_html(MY_RESULTS)}
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap two-col">
    <div>
      <p class="kicker">Working together</p>
      <h2>What to expect</h2>
    </div>
    <ul class="check-list">
      <li>DBS checked</li>
      <li>Online via Google Meet, no travel time</li>
      <li>A free intro call before you commit to anything</li>
      <li>Blocks of five weekly sessions, with unused sessions refunded</li>
      <li>Tutoring online across the UK, from Bath</li>
    </ul>
  </div>
</section>

{cta_band("Want to see if we're a good fit?")}'''
    page("about.html", "About Ali Aljawabra · GCSE & A-level Tutor in Bath",
         "Meet Ali Aljawabra: Bath-based GCSE and A-level tutor with 8s and 9s in 10 GCSEs and A*A*A at A-level. DBS checked, tutoring online across the UK.",
         body, current="about", jsonld=[
             {"@context": "https://schema.org", "@type": "Person", "@id": f"{SITE}/about.html#ali", "name": "Ali Aljawabra",
              "jobTitle": "Private tutor", "url": f"{SITE}/about.html", "image": f"{SITE}/assets/ali-aljawabra.jpg",
              "worksFor": {"@id": f"{SITE}/#business"},
              "knowsAbout": ["GCSE Maths", "GCSE Science", "GCSE Business Studies", "A-level Maths", "A-level Economics", "A-level Philosophy", "11+ Maths"],
              **({"sameAs": SAME_AS} if SAME_AS else {})},
             breadcrumb_ld([("Home", SITE + "/"), ("About", f"{SITE}/about.html")])])


def build_thanks():
    body = f'''
<section class="page-simple thanks">
  <div class="narrow">
    <span class="badge">Payment received</span>
    <h1>Thank you. One last step</h1>
    <p>Your block of five sessions is paid. Now book all five session times, ideally the same day and time each week.</p>
    <ol class="steps-list">
      <li>Click the button below <b>five times</b>, once for each session, choosing the same weekly day and time where possible.</li>
      <li>In the notes field each time, write the subject and &ldquo;paid block of five&rdquo; (not an intro call).</li>
      <li>You'll get a confirmation for each one, and the Google Meet link before your first session.</li>
    </ol>
    <p>{call_btn("Book a session time")}</p>
    <div class="note">
      Already know your preferred time, or the calendar doesn't have a slot that works? Just reply to your payment confirmation email or call {a("tel:" + PHONE_TEL, PHONE, "text-link")} directly.
    </div>
    <p style="margin-top:24px;color:var(--muted);font-size:15px">Any questions before then, email {a("mailto:" + EMAIL, EMAIL)}.</p>
    <p><a href="index.html">Back to the homepage</a></p>
  </div>
</section>'''
    page("thank-you.html", "Thank You · Ali Tutors", "Thank you for your booking.", body, noindex=True, nav_cta=False)


def build_privacy():
    global ANALYTICS_LINE
    ANALYTICS_LINE = ("This site uses Umami, a privacy-friendly analytics service, to count page visits and button clicks. "
                      "It doesn't use cookies or collect personal information." if UMAMI_WEBSITE_ID
                      else "This site does not use tracking cookies or analytics.")
    body = f'''
<section class="page-simple">
  <div class="narrow">
    <h1>Privacy Policy</h1>
    <p class="updated">Last updated: November 2026</p>

    <p>This page explains what personal information is collected through alitutors.com, why, and what your rights are. This site is run by Ali Aljawabra, trading as Ali Tutors, a Bath-based private tutor.</p>

    <h2>What's collected</h2>
    <ul>
      <li><strong>Booking a free intro call:</strong> your name and email address, via Google Calendar's appointment booking system.</li>
      <li><strong>Booking a block of sessions:</strong> your name, email, and payment details, handled entirely by Stripe (payment details are never seen or stored by Ali Tutors directly).</li>
      <li><strong>Contacting by phone, email or WhatsApp:</strong> whatever you choose to share (name, contact details, your child's subject/exam board).</li>
    </ul>

    <h2>Why it's collected</h2>
    <p>Solely to arrange, schedule, and deliver tutoring sessions, and to communicate with you about bookings, payments, and rescheduling. Nothing collected here is used for advertising or sold to third parties.</p>

    <h2>Who it's shared with</h2>
    <ul>
      <li><strong>Stripe</strong> (payment processing): see <a href="https://stripe.com/gb/privacy" target="_blank" rel="noopener">Stripe's privacy policy</a>.</li>
      <li><strong>Google Calendar</strong> (appointment scheduling): see <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google's privacy policy</a>.</li>
      <li><strong>WhatsApp</strong> (messaging, only if you choose to contact me that way): see <a href="https://www.whatsapp.com/legal/privacy-policy" target="_blank" rel="noopener">WhatsApp's privacy policy</a>.</li>
    </ul>
    <p>No other third parties receive your information. {ANALYTICS_LINE}</p>

    <h2>How long it's kept</h2>
    <p>Contact and booking details are kept only as long as needed to deliver tutoring and meet basic accounting/tax record-keeping obligations, then deleted.</p>

    <h2>Your rights</h2>
    <p>Under UK GDPR, you can ask to see, correct, or delete the personal data held about you at any time. To do so, or with any other privacy question, email {a("mailto:" + EMAIL, EMAIL)}.</p>

    <p style="margin-top:36px"><a href="index.html">Back to the homepage</a></p>
  </div>
</section>'''
    page("privacy.html", "Privacy Policy · Ali Tutors", "Privacy policy for alitutors.com.", body, noindex=True)


def build_terms():
    body = f'''
<section class="page-simple">
  <div class="narrow">
    <h1>Terms</h1>
    <p class="updated">Last updated: November 2026</p>

    <p>These terms cover tutoring from Ali Aljawabra, trading as Ali Tutors, a Bath-based private tutor. Questions about them: {a("mailto:" + EMAIL, EMAIL)} or {a("tel:" + PHONE_TEL, PHONE)}.</p>

    <h2>The service</h2>
    <p>One-to-one tutoring in GCSE, A-level and KS3 subjects, and Maths for 11+ and 13+ entrance exams, held online via Google Meet. Sessions are charged at the hourly rates on the {a("pricing.html", "pricing page")}.</p>

    <h2>Booking and payment</h2>
    <ul>
      <li>You can start with a free intro call. There's no obligation to continue after it.</li>
      <li>Sessions are booked in blocks of five, paid upfront through Stripe before the sessions begin.</li>
      <li>After paying, you book your session times through the online calendar, ideally the same day and time each week.</li>
    </ul>

    <h2>Rescheduling</h2>
    <p>Let me know as early as possible and we'll find another time within the same block.</p>

    <h2>Cancellations and refunds</h2>
    <ul>
      <li>Cancel before a block starts for a full refund.</li>
      <li>Once a block is underway, any sessions not yet taken are refunded. Sessions already delivered are not.</li>
    </ul>

    <h2>Your rights</h2>
    <p>Nothing in these terms affects your legal rights as a consumer.</p>

    <h2>Your information</h2>
    <p>How your personal information is handled is explained in the {a("privacy.html", "privacy policy")}.</p>

    <p style="margin-top:36px"><a href="index.html">Back to the homepage</a></p>
  </div>
</section>'''
    page("terms.html", "Terms · Ali Tutors", "Terms for tutoring with Ali Tutors.", body, noindex=True)


def build_404():
    links = "".join(f"<li>{a(s['slug'] + '.html', s['name'].replace('&', '&amp;'))}</li>" for s in SUBJECTS)
    body = f'''
<section class="page-simple">
  <div class="narrow">
    <p class="kicker">404</p>
    <h1>That page doesn't exist</h1>
    <p>The link may be out of date. Try one of these instead:</p>
    <ul>
      <li><a href="index.html">Home</a></li>
      <li><a href="pricing.html">Pricing</a></li>
      <li><a href="about.html">About Ali</a></li>
      {links}
    </ul>
    <p>{call_btn()}</p>
  </div>
</section>'''
    page("404.html", "Page not found · Ali Tutors", "Page not found.", body, noindex=True)


def lastmod(page):
    """Date the file last actually changed: today if it has uncommitted changes, else its last commit date."""
    f = "docs/" + (page or "index.html")
    try:
        dirty = subprocess.run(["git", "status", "--porcelain", "--", f], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
        if dirty:
            return TODAY
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", f], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
        return out or TODAY
    except Exception:
        return TODAY


def build_sitemap():
    pages = ["", "pricing.html", "about.html"] + [s["slug"] + ".html" for s in SUBJECTS]
    urls = "".join(
        f"  <url>\n    <loc>{SITE}/{p}</loc>\n    <lastmod>{lastmod(p)}</lastmod>\n"
        f"    <priority>{'1.0' if p == '' else '0.8'}</priority>\n  </url>\n" for p in pages)
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n",
        encoding="utf-8")
    print("wrote sitemap.xml")


def main():
    build_home()
    for s in SUBJECTS:
        build_subject(s)
    build_pricing()
    build_about()
    build_thanks()
    build_privacy()
    build_terms()
    build_404()
    build_sitemap()


if __name__ == "__main__":
    main()
