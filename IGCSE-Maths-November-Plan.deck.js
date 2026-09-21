const pptxgen = require("pptxgenjs");

// ============================================================
// BRAND PALETTE  — swap these six values to match alitutors.com
// ============================================================
const P = {
  navy:      "0D2B4E",  // primary / dominant
  navyDeep:  "071C33",  // dark slide backgrounds
  amber:     "F2A93B",  // accent
  amberDeep: "D4861B",  // accent, darker (text on light)
  slate:     "5A6B7C",  // muted body text
  tint:      "EEF3F8",  // card fill on white slides
  tintWarm:  "FDF3E2",  // card fill, accent flavour
  white:     "FFFFFF",
  green:     "2E8B6F",
  coral:     "C24B3F",
};

const FONT = "Calibri";
const W = 13.333, H = 7.5;

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.author = "Ali Tutors";
pres.company = "Ali Tutors";
pres.title = "IGCSE Maths Higher — November Plan";

// ---------- helpers ----------
const shadow = (o = {}) => ({
  type: "outer", angle: 90, blur: 12, offset: 2,
  color: "1A2E45", opacity: 0.12, ...o,
});

function titleBar(slide, kicker, title, opts = {}) {
  const dark = !!opts.dark;
  slide.addText(kicker.toUpperCase(), {
    x: 0.7, y: 0.42, w: 11.9, h: 0.3, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 12, bold: true, charSpacing: 2,
    color: dark ? P.amber : P.amberDeep,
  });
  slide.addText(title, {
    x: 0.7, y: 0.76, w: 11.9, h: 0.72, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 34, bold: true,
    color: dark ? P.white : P.navy,
  });
}

function numDot(slide, n, x, y, d = 0.52, fill = P.amber, txt = P.navy) {
  slide.addShape(pres.ShapeType.ellipse, {
    x, y, w: d, h: d, fill: { color: fill }, line: { color: fill, width: 0 },
  });
  slide.addText(String(n), {
    x, y, w: d, h: d, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 16, bold: true, color: txt,
    align: "center", valign: "middle",
  });
}

function card(slide, x, y, w, h, fill = P.tint) {
  slide.addShape(pres.ShapeType.roundRect, {
    x, y, w, h, rectRadius: 0.10,
    fill: { color: fill }, line: { color: fill, width: 0 },
    shadow: shadow(),
  });
}

function bullets(slide, items, o) {
  slide.addText(
    items.map((t, i) => ({
      text: t,
      options: { bullet: true, breakLine: i !== items.length - 1 },
    })),
    {
      isTextBox: true, margin: 0, fontFace: FONT,
      fontSize: o.size || 13, color: o.color || P.navy,
      lineSpacing: o.lineSpacing || 18, paraSpaceAfter: 5,
      x: o.x, y: o.y, w: o.w, h: o.h,
    }
  );
}

// ============================================================
// 1 — TITLE
// ============================================================
let s = pres.addSlide();
s.background = { color: P.navyDeep };
s.addShape(pres.ShapeType.ellipse, {
  x: 9.6, y: -1.9, w: 6.4, h: 6.4,
  fill: { color: P.navy }, line: { color: P.navy, width: 0 },
});
s.addShape(pres.ShapeType.ellipse, {
  x: 11.9, y: 4.6, w: 3.0, h: 3.0,
  fill: { color: P.amber }, line: { color: P.amber, width: 0 },
});
s.addText("ALI TUTORS", {
  x: 0.85, y: 0.75, w: 6, h: 0.32, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 13, bold: true, charSpacing: 3, color: P.amber,
});
s.addText("November\nMaths Plan", {
  x: 0.85, y: 1.7, w: 8.4, h: 2.3, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 60, bold: true, color: P.white, lineSpacing: 60,
});
s.addText("Edexcel IGCSE Mathematics A (4MA1)  ·  Higher Tier", {
  x: 0.85, y: 4.15, w: 8.4, h: 0.4, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 19, color: P.white,
});
s.addShape(pres.ShapeType.roundRect, {
  x: 0.85, y: 5.0, w: 4.55, h: 0.92, rectRadius: 0.1,
  fill: { color: P.amber }, line: { color: P.amber, width: 0 },
});
s.addText("Six weeks to Paper 1", {
  x: 0.85, y: 5.0, w: 4.55, h: 0.92, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 19, bold: true, color: P.navyDeep,
  align: "center", valign: "middle",
});
s.addText("Prepared 21 September 2026", {
  x: 0.85, y: 6.35, w: 6, h: 0.32, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 12, color: "9FB3C8",
});
s.addNotes("Timeline for the November 2026 resit. Audience: student and parent together.");

// ============================================================
// 2 — THE COUNTDOWN
// ============================================================
s = pres.addSlide();
s.background = { color: P.white };
titleBar(s, "The clock", "Two papers, two days apart");

const cd = [
  { big: "44", small: "days until Paper 1", sub: "Six teaching weeks and two days", fill: P.tint },
  { big: "Wed 4 Nov", small: "Paper 1H  ·  morning", sub: "2 hours · 100 marks · calculator", fill: P.tintWarm },
  { big: "Fri 6 Nov", small: "Paper 2H  ·  morning", sub: "2 hours · 100 marks · calculator", fill: P.tintWarm },
];
cd.forEach((c, i) => {
  const x = 0.7 + i * 4.06;
  card(s, x, 1.85, 3.76, 2.5, c.fill);
  s.addText(c.big, {
    x: x + 0.3, y: 2.08, w: 3.16, h: 0.85, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: c.big.length > 4 ? 32 : 46, bold: true, color: P.navy,
  });
  s.addText(c.small, {
    x: x + 0.3, y: 3.0, w: 3.16, h: 0.32, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 14, bold: true, color: P.amberDeep,
  });
  s.addText(c.sub, {
    x: x + 0.3, y: 3.38, w: 3.16, h: 0.6, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 12, color: P.slate,
  });
});

card(s, 0.7, 4.72, 11.94, 1.9, P.navy);
s.addText("Both papers allow a calculator.", {
  x: 1.1, y: 5.0, w: 11.1, h: 0.42, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 21, bold: true, color: P.amber,
});
s.addText("That matters more than it sounds. Every mark lost to arithmetic is recoverable with calculator technique rather than months of number work — so we teach the calculator properly in week one, and check the degree mode every single time.",
  { x: 1.1, y: 5.5, w: 11.1, h: 0.85, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 14, color: P.white, lineSpacing: 20 });
s.addNotes("Series runs 27 Oct to 19 Nov. She must stay available to 19 Nov.");

// ============================================================
// 3 — THE TARGET
// ============================================================
s = pres.addSlide();
s.background = { color: P.white };
titleBar(s, "The target", "We are hunting 65 marks, not a syllabus");

card(s, 0.7, 1.85, 5.1, 4.55, P.navy);
s.addText("65", {
  x: 1.05, y: 2.02, w: 4.4, h: 1.9, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 104, bold: true, color: P.amber,
});
s.addText("marks out of 200", {
  x: 1.05, y: 3.95, w: 4.4, h: 0.4, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 20, bold: true, color: P.white,
});
s.addText("That was the grade 5 boundary on Higher tier in November 2025 — just under a third of the paper.\n\nWe plan against 70 to leave margin, because boundaries move each series.",
  { x: 1.05, y: 4.5, w: 4.4, h: 1.6, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 13, color: "C3D4E5", lineSpacing: 19 });

const rows = [
  ["Grade", "Marks needed", "% of paper"],
  ["Grade 6", "86 / 200", "43%"],
  ["Grade 5", "65 / 200", "33%"],
  ["Grade 4", "45 / 200", "23%"],
];
s.addTable(
  rows.map((r, ri) =>
    r.map((c, ci) => ({
      text: c,
      options: {
        fontFace: FONT, fontSize: ri === 0 ? 13 : 16,
        bold: ri === 0 || ri === 2,
        color: ri === 0 ? P.white : (ri === 2 ? P.navy : P.slate),
        fill: { color: ri === 0 ? P.navy : (ri === 2 ? P.tintWarm : P.white) },
        align: ci === 0 ? "left" : "center", valign: "middle",
      },
    }))
  ),
  { x: 6.2, y: 1.85, w: 6.44, colW: [2.44, 2.2, 1.8], rowH: [0.42, 0.62, 0.62, 0.62],
    border: { type: "solid", color: "DCE6F0", pt: 1 } }
);

card(s, 6.2, 4.35, 6.44, 2.05, P.tint);
s.addText("Roughly 40% of every Higher paper — about 80 marks — is pitched at grades 4 and 5.", {
  x: 6.55, y: 4.6, w: 5.74, h: 0.62, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 16, bold: true, color: P.navy, lineSpacing: 21,
});
s.addText("So every mark she needs is sitting in the easiest 40% of the paper. The plan is to harvest that band almost perfectly — not to climb the whole tier.",
  { x: 6.55, y: 5.35, w: 5.74, h: 0.85, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 13, color: P.slate, lineSpacing: 19 });
s.addNotes("Nov 2025 Higher boundaries: 9=166, 8=136, 7=107, 6=86, 5=65, 4=45. Verify against Pearson before quoting.");

// ============================================================
// 4 — WHERE THE MARKS ARE
// ============================================================
s = pres.addSlide();
s.background = { color: P.white };
titleBar(s, "Where the marks are", "Number and algebra is 60% of the qualification");

s.addChart(
  pres.ChartType.bar,
  [{
    name: "Marks of 200",
    labels: ["Number & algebra", "Shape, space & measure", "Handling data"],
    values: [120, 50, 30],
  }],
  {
    x: 0.7, y: 1.9, w: 7.1, h: 4.4,
    barDir: "bar", barGrapicStyle: 1,
    chartColors: [P.navy, "3E6A96", P.amber],
    varyColors: true,
    showLegend: false, showTitle: false,
    showValue: true, dataLabelPosition: "outEnd",
    dataLabelColor: P.navy, dataLabelFontFace: FONT,
    dataLabelFontSize: 14, dataLabelFontBold: true,
    catAxisLabelColor: P.navy, catAxisLabelFontFace: FONT, catAxisLabelFontSize: 13,
    catAxisLabelFontBold: true, catGridLine: { style: "none" },
    valAxisLabelColor: P.slate, valAxisLabelFontFace: FONT, valAxisLabelFontSize: 11,
    valGridLine: { color: "E4EBF2", size: 1 },
    valAxisMaxVal: 140, barGapWidthPct: 55,
    chartArea: { fill: { color: P.white } },
  }
);

card(s, 8.15, 1.9, 4.49, 2.05, P.tintWarm);
s.addText("Her weakest area is also the biggest", {
  x: 8.5, y: 2.15, w: 3.79, h: 0.6, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 16, bold: true, color: P.navy, lineSpacing: 21,
});
s.addText("The Year 9 gaps sit in number and algebra. Fixing them pays out across 120 marks, not 20.",
  { x: 8.5, y: 2.8, w: 3.79, h: 0.95, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 13, color: P.slate, lineSpacing: 19 });

card(s, 8.15, 4.25, 4.49, 2.05, P.tint);
s.addText("Handling data is the cheapest 25 marks", {
  x: 8.5, y: 4.5, w: 3.79, h: 0.6, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 16, bold: true, color: P.navy, lineSpacing: 21,
});
s.addText("Averages, tables, probability and Venn diagrams barely touch algebra — so weak algebra does not block them.",
  { x: 8.5, y: 5.15, w: 3.79, h: 1.0, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 13, color: P.slate, lineSpacing: 19 });
s.addNotes("Weightings from the 4MA1 spec: AO1 Number & algebra 57-63%, AO2 Shape 22-28%, AO3 Data 12-18%.");

// ============================================================
// 5 — THE TIMELINE (hero)
// ============================================================
s = pres.addSlide();
s.background = { color: P.navyDeep };
titleBar(s, "The route", "Six weeks, at a glance", { dark: true });

const steps = [
  { n: "1", d: "21–27 Sep", t: "Diagnose" },
  { n: "2", d: "28 Sep–4 Oct", t: "Number" },
  { n: "3", d: "5–11 Oct", t: "Algebra" },
  { n: "4", d: "12–18 Oct", t: "Ratio + data" },
  { n: "5", d: "19–25 Oct", t: "Shape" },
  { n: "6", d: "26 Oct–1 Nov", t: "Papers" },
  { n: "★", d: "4 & 6 Nov", t: "Exams" },
];
const tY = 2.5;
s.addShape(pres.ShapeType.rect, {
  x: 1.55, y: tY + 0.24, w: 10.23, h: 0.055,
  fill: { color: "2C4A6B" }, line: { color: "2C4A6B", width: 0 },
});
steps.forEach((st, i) => {
  const cx = 0.7 + i * 1.705;
  const isExam = i === steps.length - 1;
  numDot(s, st.n, cx + 0.54, tY, 0.62, isExam ? P.amber : P.white, isExam ? P.navyDeep : P.navy);
  s.addText(st.d, {
    x: cx, y: tY + 0.85, w: 1.7, h: 0.3, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 11, color: isExam ? P.amber : "9FB3C8", align: "center",
  });
  s.addText(st.t, {
    x: cx, y: tY + 1.15, w: 1.7, h: 0.4, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 15, bold: true, color: P.white, align: "center",
  });
});

const ratio = [
  { k: "Weeks 1–3", v: "90% teaching  ·  10% exam questions" },
  { k: "Weeks 4–5", v: "Teaching and papers, roughly evenly split" },
  { k: "Week 6", v: "30% teaching  ·  70% full timed papers" },
];
s.addText("The balance shifts as we go", {
  x: 0.7, y: 4.75, w: 11.94, h: 0.36, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 17, bold: true, color: P.amber,
});
ratio.forEach((r, i) => {
  const x = 0.7 + i * 4.06;
  card(s, x, 5.25, 3.76, 1.15, P.navy);
  s.addText(r.k, {
    x: x + 0.28, y: 5.42, w: 3.2, h: 0.3, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 14, bold: true, color: P.amber,
  });
  s.addText(r.v, {
    x: x + 0.28, y: 5.74, w: 3.2, h: 0.55, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 12, color: P.white, lineSpacing: 16,
  });
});
s.addNotes("Past papers are a measuring tool, not a teaching tool. We do not spend them early.");

// ============================================================
// 6–8 — WEEK PAIRS
// ============================================================
const weeks = [
  {
    n: 1, dates: "21–27 Sep", name: "Diagnose",
    items: ["Fluency audit — 35 questions, 50 minutes",
            "Negative numbers, to automaticity",
            "Calculator drill: fraction key, ANS, degree mode",
            "Set up the error log"],
    hw: "Daily drill: negatives", paper: "No paper work this week",
  },
  {
    n: 2, dates: "28 Sep–4 Oct", name: "The number engine",
    items: ["Fractions — all four operations",
            "Percentage multipliers: increase and decrease",
            "Reverse percentages",
            "One method per topic, used every time"],
    hw: "Daily drill: negatives + fractions", paper: "6 past-paper percentage questions",
  },
  {
    n: 3, dates: "5–11 Oct", name: "The algebra spine",
    items: ["Collecting terms and expanding brackets",
            "Solving with x on both sides",
            "Substitution and rearranging formulae",
            "Re-run the audit — checkpoint 1"],
    hw: "Daily drill: fractions + percentages", paper: "First timed section — 25 minutes",
  },
  {
    n: 4, dates: "12–18 Oct", name: "The cheap marks",
    items: ["Ratio by the unitary method",
            "Averages and frequency tables",
            "Estimated mean from grouped data",
            "Probability, tree diagrams and Venn diagrams"],
    hw: "Daily drill: solving + ratio", paper: "Timed section — 40 minutes",
  },
  {
    n: 5, dates: "19–25 Oct", name: "Shape and space",
    items: ["Angle facts, area and perimeter",
            "Circles, prisms and cylinders",
            "Pythagoras and SOHCAHTOA",
            "The formula sheet, as a topic in itself"],
    hw: "Daily drill: all six bottleneck skills, mixed", paper: "First FULL paper — 2 hours, exam conditions",
  },
  {
    n: 6, dates: "26 Oct–1 Nov", name: "Half term: papers",
    items: ["Mark and patch the full paper",
            "Quadratic formula, sine and cosine rules",
            "Exam technique and pacing session",
            "Re-run the audit — checkpoint 2"],
    hw: "Daily drill: straight from the error log", paper: "Second full paper, then patch the top five losses",
  },
];

function weekCard(slide, w, x, y) {
  card(slide, x, y, 5.92, 4.52, P.tint);
  numDot(slide, w.n, x + 0.35, y + 0.32, 0.56);
  slide.addText(`WEEK ${w.n}  ·  ${w.dates}`, {
    x: x + 1.05, y: y + 0.32, w: 4.5, h: 0.26, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 11, bold: true, charSpacing: 1.5, color: P.amberDeep,
  });
  slide.addText(w.name, {
    x: x + 1.05, y: y + 0.58, w: 4.5, h: 0.4, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 21, bold: true, color: P.navy,
  });
  bullets(slide, w.items, { x: x + 0.38, y: y + 1.22, w: 5.2, h: 1.62, size: 13 });

  slide.addShape(pres.ShapeType.rect, {
    x: x + 0.38, y: y + 2.95, w: 5.18, h: 0.02,
    fill: { color: "D3DFEA" }, line: { color: "D3DFEA", width: 0 },
  });
  slide.addText("AT HOME", {
    x: x + 0.38, y: y + 3.1, w: 5.18, h: 0.24, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 10, bold: true, charSpacing: 1.5, color: P.slate,
  });
  slide.addText(w.hw, {
    x: x + 0.38, y: y + 3.33, w: 5.18, h: 0.3, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 13, bold: true, color: P.navy,
  });
  slide.addText("PAPER WORK", {
    x: x + 0.38, y: y + 3.72, w: 5.18, h: 0.24, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 10, bold: true, charSpacing: 1.5, color: P.slate,
  });
  slide.addText(w.paper, {
    x: x + 0.38, y: y + 3.95, w: 5.18, h: 0.42, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 13, bold: true, color: P.amberDeep, lineSpacing: 16,
  });
}

const pairs = [
  ["Weeks 1 and 2", "Fix the foundations first", [0, 1]],
  ["Weeks 3 and 4", "The biggest block of marks", [2, 3]],
  ["Weeks 5 and 6", "Shape, then papers", [4, 5]],
];
pairs.forEach(([kicker, title, idx]) => {
  const sl = pres.addSlide();
  sl.background = { color: P.white };
  titleBar(sl, kicker, title);
  weekCard(sl, weeks[idx[0]], 0.7, 1.82);
  weekCard(sl, weeks[idx[1]], 6.72, 1.82);
});

// ============================================================
// 9 — EXAM WEEK
// ============================================================
s = pres.addSlide();
s.background = { color: P.navyDeep };
titleBar(s, "Exam week", "2 – 6 November", { dark: true });

const days = [
  { d: "MON 2 NOV", t: "Last session", b: "No new content. Retrieval of everything, pacing rehearsal, calculator check. Finish on something she is good at.", accent: false },
  { d: "WED 4 NOV", t: "Paper 1H", b: "Morning · 2 hours · 100 marks. Two passes: everything she recognises first, then return. Last 10 minutes checking what she got right.", accent: true },
  { d: "THU 5 NOV", t: "The gap day", b: "The most valuable session in the plan. No detailed post-mortem — find the two or three topics she could not start, and drill exactly those.", accent: false },
  { d: "FRI 6 NOV", t: "Paper 2H", b: "Morning · 2 hours · 100 marks. Same pacing. Both papers cover the full specification, so topics recur.", accent: true },
];
days.forEach((dy, i) => {
  const x = 0.7 + i * 3.06;
  card(s, x, 1.9, 2.82, 4.4, dy.accent ? P.amber : P.navy);
  s.addText(dy.d, {
    x: x + 0.28, y: 2.15, w: 2.26, h: 0.28, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 11, bold: true, charSpacing: 1.5,
    color: dy.accent ? P.navyDeep : P.amber,
  });
  s.addText(dy.t, {
    x: x + 0.28, y: 2.45, w: 2.26, h: 0.7, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 22, bold: true,
    color: dy.accent ? P.navyDeep : P.white, lineSpacing: 25,
  });
  s.addText(dy.b, {
    x: x + 0.28, y: 3.25, w: 2.26, h: 2.8, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 12.5,
    color: dy.accent ? "3A2A0A" : "C3D4E5", lineSpacing: 18,
  });
});
s.addText("No new content after 28 October. The last week consolidates what is already there.", {
  x: 0.7, y: 6.55, w: 11.94, h: 0.35, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 14, bold: true, italic: true, color: P.amber,
});

// ============================================================
// 10 — WHAT WE ARE NOT DOING
// ============================================================
s = pres.addSlide();
s.background = { color: P.white };
titleBar(s, "Triage", "What we teach, and what we deliberately skip");

card(s, 0.7, 1.85, 5.92, 4.5, P.tint);
numDot(s, "✓", 1.05, 2.15, 0.56, P.green, P.white);
s.addText("We teach this", {
  x: 1.75, y: 2.2, w: 4.6, h: 0.42, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 22, bold: true, color: P.navy,
});
s.addText("Roughly 80 marks live here. This list alone, done well, is a grade 5.", {
  x: 1.08, y: 2.85, w: 5.2, h: 0.55, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 13, italic: true, color: P.slate, lineSpacing: 18,
});
bullets(s, [
  "Fractions, decimals, percentages, reverse percentages",
  "Negatives, indices, standard form, rounding",
  "Ratio and proportion by the unitary method",
  "Solving, expanding, substituting, rearranging",
  "Sequences and straight-line graphs",
  "Angles, area, circles, prisms, Pythagoras, trigonometry",
  "Averages, frequency tables, probability, Venn diagrams",
], { x: 1.08, y: 3.5, w: 5.2, h: 2.7, size: 12.5, lineSpacing: 17 });

card(s, 6.92, 1.85, 5.72, 4.5, P.white);
s.addShape(pres.ShapeType.roundRect, {
  x: 6.92, y: 1.85, w: 5.72, h: 4.5, rectRadius: 0.1,
  fill: { color: P.white }, line: { color: "E2E8EF", width: 1.5 },
});
numDot(s, "✕", 7.27, 2.15, 0.56, P.coral, P.white);
s.addText("We skip this", {
  x: 7.97, y: 2.2, w: 4.4, h: 0.42, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 22, bold: true, color: P.navy,
});
s.addText("Worth 60–80 marks she would convert almost none of in six weeks.", {
  x: 7.3, y: 2.85, w: 5.0, h: 0.55, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 13, italic: true, color: P.slate, lineSpacing: 18,
});
bullets(s, [
  "Circle theorems and their proofs",
  "Vectors and vector geometry",
  "Histograms with unequal class widths",
  "Algebraic fractions, functions, graph transformations",
  "Surds, bounds, 3D trigonometry",
  "Quadratic simultaneous equations and inequalities",
  "Area and volume scale factors",
], { x: 7.3, y: 3.5, w: 5.0, h: 2.7, size: 12.5, color: P.slate, lineSpacing: 17 });

s.addText("Instead, she learns to recognise one of these in ten seconds and move on. Time spent on a question she was never going to get is how you lose marks you already had.",
  { x: 0.7, y: 6.48, w: 11.94, h: 0.62, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 13.5, italic: true, color: P.navy, lineSpacing: 19 });

// ============================================================
// 11 — EVERY DAY, 20 MINUTES
// ============================================================
s = pres.addSlide();
s.background = { color: P.white };
titleBar(s, "Between sessions", "Twenty minutes a day is half the plan");

s.addText("Six days a week for six weeks is twelve hours — as much as every lesson combined. Automaticity comes from spacing, and no single long session substitutes for it.",
  { x: 0.7, y: 1.68, w: 11.94, h: 0.68, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 15, color: P.slate, lineSpacing: 21 });

const hw = [
  { m: "5 min", t: "Bottleneck drill", b: "Twenty quick reps of this week's target skill. Timed, score written down." },
  { m: "10 min", t: "Mixed retrieval", b: "Six questions from topics already taught, deliberately not grouped together." },
  { m: "5 min", t: "Error log", b: "Read it, then redo two past errors without looking at the correction." },
];
hw.forEach((h, i) => {
  const x = 0.7 + i * 4.06;
  card(s, x, 2.45, 3.76, 2.4, i === 1 ? P.tintWarm : P.tint);
  s.addText(h.m, {
    x: x + 0.3, y: 2.68, w: 3.16, h: 0.55, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 30, bold: true, color: P.amberDeep,
  });
  s.addText(h.t, {
    x: x + 0.3, y: 3.28, w: 3.16, h: 0.34, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 16, bold: true, color: P.navy,
  });
  s.addText(h.b, {
    x: x + 0.3, y: 3.66, w: 3.16, h: 1.0, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 12.5, color: P.slate, lineSpacing: 17,
  });
});

card(s, 0.7, 5.15, 11.94, 1.5, P.navy);
const rules = [
  "No new learning at home", "She marks her own work", "Same time every day", "Photo of the marked sheet",
];
rules.forEach((r, i) => {
  const x = 1.1 + i * 2.93;
  numDot(s, i + 1, x, 5.55, 0.44);
  s.addText(r, {
    x: x + 0.58, y: 5.58, w: 2.3, h: 0.5, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 13, bold: true, color: P.white, valign: "middle",
  });
});
s.addNotes("If the daily drill is not happening by end of week 2, that is the problem to solve before anything else.");

// ============================================================
// 12 — CHECKPOINTS
// ============================================================
s = pres.addSlide();
s.background = { color: P.white };
titleBar(s, "Progress", "How we will know it is working");

s.addText("Two numbers, tracked all the way through: her audit score, and her marks on a timed paper. Nothing else.",
  { x: 0.7, y: 1.72, w: 11.94, h: 0.4, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 15, color: P.slate });

const cps = [
  { w: "Week 1", t: "Baseline", v: "Audit recorded", note: "The map, not a grade" },
  { w: "Week 3", t: "Checkpoint 1", v: "Audit re-run", note: "Bottlenecks should have moved" },
  { w: "Week 5", t: "First full paper", v: "35 / 100", note: "On track for a grade 5" },
  { w: "Week 6", t: "Second full paper", v: "40 / 100", note: "And rising from week 5" },
];
cps.forEach((c, i) => {
  const x = 0.7 + i * 3.06;
  const hot = i >= 2;
  card(s, x, 2.35, 2.82, 3.1, hot ? P.navy : P.tint);
  s.addText(c.w.toUpperCase(), {
    x: x + 0.28, y: 2.6, w: 2.26, h: 0.26, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 10.5, bold: true, charSpacing: 1.5,
    color: hot ? P.amber : P.amberDeep,
  });
  s.addText(c.t, {
    x: x + 0.28, y: 2.88, w: 2.26, h: 0.62, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 16, bold: true, color: hot ? P.white : P.navy, lineSpacing: 20,
  });
  s.addText(c.v, {
    x: x + 0.28, y: 3.62, w: 2.26, h: 0.62, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: c.v.includes("/") ? 30 : 17, bold: true,
    color: hot ? P.amber : P.navy,
  });
  s.addText(c.note, {
    x: x + 0.28, y: 4.35, w: 2.26, h: 0.8, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 12.5, color: hot ? "C3D4E5" : P.slate, lineSpacing: 17,
  });
});

card(s, 0.7, 5.72, 11.94, 0.95, P.tintWarm);
s.addText("After every session you get one line: what we taught, her retrieval score out of six, and whether the homework came back.",
  { x: 1.1, y: 5.95, w: 11.1, h: 0.5, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 14, bold: true, color: P.navy, valign: "middle" });

// ============================================================
// 13 — CLOSE
// ============================================================
s = pres.addSlide();
s.background = { color: P.navyDeep };
s.addShape(pres.ShapeType.ellipse, {
  x: -2.2, y: 3.6, w: 6.6, h: 6.6,
  fill: { color: P.navy }, line: { color: P.navy, width: 0 },
});
s.addText("The whole plan, in one line", {
  x: 1.4, y: 1.55, w: 10.5, h: 0.36, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 13, bold: true, charSpacing: 2.5, color: P.amber,
});
s.addText("Fix six broken fundamentals,\nharvest the easiest 40% of the paper,\nand leave the rest alone.", {
  x: 1.4, y: 2.2, w: 10.5, h: 2.4, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 38, bold: true, color: P.white, lineSpacing: 52,
});

const next = [
  "Confirm the entry, tier and exam times with school",
  "Run the fluency audit in session one",
  "Set up the error log and the daily 20 minutes",
];
s.addText("THIS WEEK", {
  x: 1.4, y: 4.95, w: 10.5, h: 0.28, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 11, bold: true, charSpacing: 2, color: P.amber,
});
next.forEach((t, i) => {
  const x = 1.4 + i * 3.62;
  numDot(s, i + 1, x, 5.35, 0.46);
  s.addText(t, {
    x: x, y: 5.95, w: 3.3, h: 0.7, isTextBox: true, margin: 0,
    fontFace: FONT, fontSize: 13, color: P.white, lineSpacing: 18,
  });
});
s.addText("Ali Tutors", {
  x: 10.4, y: 6.75, w: 2.2, h: 0.3, isTextBox: true, margin: 0,
  fontFace: FONT, fontSize: 12, bold: true, charSpacing: 2, color: P.amber, align: "right",
});

pres.writeFile({ fileName: "/tmp/claude-0/-home-user-Daily/66a6df15-50ce-540f-aac0-2346f980a922/scratchpad/IGCSE-Maths-November-Plan.pptx" })
  .then(f => console.log("written:", f));
