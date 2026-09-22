"""Edexcel IGCSE Maths A (4MA1) Higher Tier — student topic RAG sheet.
Single sheet. Every topic row links straight to a live search scoped to
Maths Genie + Physics & Maths Tutor. Three confirmed hub links sit at the
top (these are real, checked URLs — nothing below is guessed).
"""
from urllib.parse import quote_plus
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule
from openpyxl.utils import get_column_letter

NAVY, AMBER_D, SLATE = "0D2B4E", "D4861B", "5A6B7C"
TINT, WHITE, HAIR = "EEF3F8", "FFFFFF", "DCE6F0"
LINK = "1155CC"
G_BG, G_TX = "DCF0E4", "1B6B4A"
A_BG, A_TX = "FCEBCE", "8A5A00"
R_BG, R_TX = "FADCD9", "9B2C20"
F = "Calibri"

# (topic text, short search keywords used to build the practice link)
TOPICS = [
 ("1  Number", [
  ("Place value, ordering, rounding to d.p. and significant figures", "rounding significant figures"),
  ("Four operations with integers, decimals and negatives", "negative numbers"),
  ("Factors, multiples, primes, HCF and LCM", "HCF LCM prime factors"),
  ("Fractions: simplifying, comparing, all four operations", "fractions"),
  ("Converting between fractions, decimals and percentages", "fractions decimals percentages"),
  ("Percentage of an amount; increase and decrease", "percentage increase decrease"),
  ("Percentage change, profit and loss", "percentage change profit loss"),
  ("Reverse percentages", "reverse percentages"),
  ("Compound interest, depreciation, growth and decay", "compound interest depreciation"),
  ("Ratio: simplifying, sharing, the unitary method", "ratio"),
  ("Direct and inverse proportion", "direct inverse proportion"),
  ("Compound measures: speed, density, pressure", "speed density pressure"),
  ("Powers, roots and the index laws", "index laws"),
  ("Negative and fractional indices", "fractional indices"),
  ("Standard form", "standard form"),
  ("Surds: simplifying and rationalising", "surds"),
  ("Upper and lower bounds; error intervals", "upper lower bounds"),
  ("Recurring decimals into fractions", "recurring decimals fractions"),
  ("Set language, notation and Venn diagrams", "venn diagrams sets"),
 ]),
 ("2  Equations, formulae and identities", [
  ("Algebraic notation and collecting like terms", "collecting like terms"),
  ("Expanding single brackets", "expanding brackets"),
  ("Expanding double brackets", "expanding double brackets"),
  ("Factorising: common factor", "factorising common factor"),
  ("Factorising quadratics: x² + bx + c", "factorising quadratics"),
  ("Factorising quadratics: ax² + bx + c", "factorising quadratics harder"),
  ("The difference of two squares", "difference of two squares"),
  ("Substituting into expressions and formulae", "substitution formulae"),
  ("Solving linear equations, x on both sides", "solving linear equations"),
  ("Solving equations with brackets and fractions", "equations brackets fractions"),
  ("Rearranging a formula to change the subject", "changing the subject"),
  ("Rearranging where the subject appears twice", "change subject appears twice"),
  ("Simultaneous linear equations", "simultaneous equations"),
  ("Simultaneous equations, one quadratic", "simultaneous equations quadratic"),
  ("Solving quadratics by factorising", "solving quadratic equations"),
  ("Solving quadratics with the formula", "quadratic formula"),
  ("Completing the square", "completing the square"),
  ("Algebraic fractions: simplifying, the four operations", "algebraic fractions"),
  ("Equations with algebraic fractions", "equations algebraic fractions"),
  ("Linear inequalities on a number line", "linear inequalities"),
  ("Quadratic inequalities", "quadratic inequalities"),
  ("Proportionality: squares and cubes", "proportion squares cubes"),
  ("Forming an equation from a worded problem", "forming equations"),
  ("Algebraic proof", "algebraic proof"),
 ]),
 ("3  Sequences, functions and graphs", [
  ("Sequences: term-to-term rules", "sequences term to term"),
  ("nth term of a linear sequence", "nth term linear sequence"),
  ("nth term of a quadratic sequence", "nth term quadratic sequence"),
  ("Coordinates and the midpoint of a line", "midpoint of a line"),
  ("Plotting straight-line graphs", "straight line graphs"),
  ("Gradient, intercept, y = mx + c", "gradient y=mx+c"),
  ("Equation of a line through two points", "equation of a line"),
  ("Parallel and perpendicular lines", "parallel perpendicular lines"),
  ("Real-life graphs, distance–time", "distance time graphs"),
  ("Plotting and interpreting quadratic graphs", "quadratic graphs"),
  ("Cubic and reciprocal graphs", "cubic reciprocal graphs"),
  ("Exponential graphs, growth and decay", "exponential graphs"),
  ("Graphs of sine, cosine and tangent", "trig graphs"),
  ("Solving equations graphically", "solving equations graphically"),
  ("Function notation f(x)", "function notation"),
  ("Composite and inverse functions", "composite inverse functions"),
  ("Transformations of graphs", "transformations of graphs"),
  ("Differentiating polynomials (power rule)", "differentiation power rule"),
  ("Gradient of a curve, tangents", "gradient of a curve"),
  ("Turning points: maximum and minimum", "turning points"),
  ("Kinematics: displacement, velocity, acceleration", "kinematics differentiation"),
 ]),
 ("4  Geometry and trigonometry", [
  ("Angle facts: lines, points, triangles", "angle facts"),
  ("Angles in parallel lines", "angles parallel lines"),
  ("Interior and exterior angles of polygons", "angles polygons"),
  ("Properties of triangles and quadrilaterals", "properties of quadrilaterals"),
  ("Congruence and similarity", "congruence similarity"),
  ("Similar shapes: length scale factor", "similar shapes"),
  ("Similar shapes: area and volume scale factors", "similar shapes area volume"),
  ("Perimeter and area of standard shapes", "area and perimeter"),
  ("Circles: circumference and area", "circumference area of circle"),
  ("Arcs, sectors and segments", "arc length sector area"),
  ("Circle theorems", "circle theorems"),
  ("Volume and surface area: prisms, cylinders", "volume prisms cylinders"),
  ("Volume and surface area: cones, spheres, pyramids", "volume cone sphere"),
  ("Pythagoras' theorem", "pythagoras theorem"),
  ("Trigonometry (SOHCAHTOA)", "trigonometry sohcahtoa"),
  ("Angles of elevation and depression", "angle of elevation depression"),
  ("Bearings", "bearings"),
  ("Pythagoras and trigonometry in 3D", "pythagoras trigonometry 3d"),
  ("The sine rule and the cosine rule", "sine rule cosine rule"),
  ("Area of a triangle using ½ab sin C", "area of a triangle sine"),
  ("Constructions and loci", "constructions and loci"),
  ("Scale drawings and maps", "scale drawings maps bearings"),
  ("Symmetry", "symmetry"),
 ]),
 ("5  Vectors and transformation geometry", [
  ("Reflection, rotation, translation, enlargement", "transformations reflection rotation"),
  ("Negative and fractional scale factors", "enlargement negative fractional scale factor"),
  ("Combined transformations", "combined transformations"),
  ("Vector notation, magnitude, addition", "vectors"),
  ("Vector geometry and proof", "vector proof geometry"),
 ]),
 ("6  Statistics and probability", [
  ("Tally charts and frequency tables", "frequency tables"),
  ("Two-way tables", "two way tables"),
  ("Bar charts, pictograms, pie charts", "pie charts"),
  ("Mean, median, mode and range", "mean median mode range"),
  ("Mean from a frequency table", "mean from frequency table"),
  ("Estimated mean from grouped data", "estimated mean grouped data"),
  ("Scatter graphs, correlation, line of best fit", "scatter graphs correlation"),
  ("Cumulative frequency graphs", "cumulative frequency"),
  ("Box plots and quartiles", "box plots quartiles"),
  ("Histograms with unequal class widths", "histograms"),
  ("Probability scale, single-event probability", "probability basics"),
  ("Mutually exclusive and exhaustive events", "mutually exclusive events"),
  ("Relative and expected frequency", "relative frequency expected frequency"),
  ("Sample space diagrams", "sample space diagrams"),
  ("Tree diagrams, with replacement", "tree diagrams"),
  ("Tree diagrams without replacement", "tree diagrams without replacement"),
  ("Venn diagrams in probability", "venn diagrams probability"),
 ]),
]

def search_link(keywords: str) -> str:
    q = f"(site:physicsandmathstutor.com OR site:mathsgenie.co.uk) {keywords} edexcel igcse"
    return "https://www.google.com/search?q=" + quote_plus(q)

RATE_COL, LINK_COL, NOTE_COL = 2, 3, 4
RC, LC = get_column_letter(RATE_COL), get_column_letter(LINK_COL)

wb = Workbook()
ws = wb.active
ws.title = "Topic check"
ws.sheet_view.showGridLines = False
thin = Side(style="thin", color=HAIR)
box = Border(bottom=thin)

def put(r, c, v, **kw):
    cell = ws.cell(row=r, column=c, value=v)
    cell.font = Font(name=F, size=kw.get("size", 11), bold=kw.get("bold", False),
                     color=kw.get("color", "000000"), italic=kw.get("italic", False))
    if kw.get("fill"):
        cell.fill = PatternFill("solid", fgColor=kw["fill"])
    cell.alignment = Alignment(horizontal=kw.get("h", "left"), vertical="center",
                               wrap_text=kw.get("wrap", False))
    if kw.get("border"):
        cell.border = box
    return cell

def link_cell(r, c, url, text, **kw):
    cell = put(r, c, text, color=kw.get("color", LINK), size=kw.get("size", 10.5),
              bold=kw.get("bold", False), h=kw.get("h", "left"))
    cell.hyperlink = url
    return cell

# ---------- header ----------
put(1, 1, "Edexcel IGCSE Mathematics A (4MA1) Higher  —  Topic check", size=17, bold=True, color=NAVY)
put(2, 1, "Ten minutes, before our first lesson. An honest red beats a hopeful green.", size=10.5, color=SLATE)

for i, lab in enumerate(["NAME", "TARGET GRADE", "DATE"]):
    put(4, i + 1, lab, size=9, bold=True, color=AMBER_D)
    put(5, i + 1, "", fill=TINT, border=True)

for i, (name, meaning, bg, tx) in enumerate([
        ("Green", "could do it in a test tomorrow", G_BG, G_TX),
        ("Amber", "seen it, would need reminding", A_BG, A_TX),
        ("Red",   "don't recognise it / always wrong", R_BG, R_TX)]):
    put(7 + i, 1, f"{name} — {meaning}", size=10.5, fill=bg, color=tx)

HEAD_RES = 11
put(HEAD_RES, 1, "PRACTICE HUBS", size=9, bold=True, color=AMBER_D)
resources = [
    ("Maths Genie — full IGCSE index", "https://www.mathsgenie.co.uk/igcse.php"),
    ("PMT — questions by topic (Higher + Foundation)", "https://www.physicsandmathstutor.com/maths-revision/gcse-questions-edexcel-igcse/"),
    ("PMT — full past papers + mark schemes", "https://www.physicsandmathstutor.com/past-papers/gcse-maths/edexcel-igcse-a-paper-1/"),
]
for i, (label, url) in enumerate(resources):
    link_cell(HEAD_RES + 1 + i, 1, url, f"  {label}", size=10.5)

RUN_ROW = HEAD_RES
put(RUN_ROW, 3, "RUNNING TOTAL", size=9, bold=True, color=AMBER_D)

HEAD = 16
FIRST = HEAD + 1
LAST = FIRST + sum(len(v) + 1 for _, v in TOPICS) - 1

ws.cell(row=RUN_ROW + 1, column=3,
        value=f'=COUNTIF({RC}{FIRST}:{RC}{LAST},"Green")&" green   "&'
              f'COUNTIF({RC}{FIRST}:{RC}{LAST},"Amber")&" amber   "&'
              f'COUNTIF({RC}{FIRST}:{RC}{LAST},"Red")&" red"').font = Font(
    name=F, size=12, bold=True, color=NAVY)
put(RUN_ROW + 2, 3, "of 109 topics", size=9.5, italic=True, color=SLATE)
put(RUN_ROW, 4, "Column C opens a search of Maths Genie + PMT for that exact topic.",
    size=9.5, italic=True, color=SLATE, wrap=True)

# ---------- table ----------
for i, h in enumerate(["Topic", "Rating", "Practice", "Notes"], start=1):
    put(HEAD, i, h, bold=True, color=WHITE, fill=NAVY, size=10.5,
        h="center" if i in (RATE_COL, LINK_COL) else "left")
ws.row_dimensions[HEAD].height = 22

row = FIRST
area_ranges = []
for area, items in TOPICS:
    n = len(items)
    start = row + 1
    end = start + n - 1
    put(row, 1, area, bold=True, color=NAVY, fill=TINT, size=11.5)
    ws.cell(row=row, column=2,
            value=f'=COUNTIF({RC}{start}:{RC}{end},"Green")&"G "&'
                  f'COUNTIF({RC}{start}:{RC}{end},"Amber")&"A "&'
                  f'COUNTIF({RC}{start}:{RC}{end},"Red")&"R"').font = Font(
        name=F, size=9, bold=True, color=AMBER_D)
    ws.cell(row=row, column=2).fill = PatternFill("solid", fgColor=TINT)
    ws.cell(row=row, column=2).alignment = Alignment(horizontal="center", vertical="center")
    for c in (3, 4):
        put(row, c, "", fill=TINT)
    ws.row_dimensions[row].height = 21
    row += 1
    for topic, kw in items:
        put(row, 1, topic, size=10.5, border=True)
        put(row, RATE_COL, "", h="center", border=True)
        link_cell(row, LINK_COL, search_link(kw), "Find →", h="center", size=10)
        ws.cell(row=row, column=LINK_COL).border = box
        put(row, NOTE_COL, "", size=10, color=SLATE, border=True)
        ws.row_dimensions[row].height = 18
        row += 1
    area_ranges.append((area, start, row - 1))

assert row - 1 == LAST

dv = DataValidation(type="list", formula1='"Green,Amber,Red"', allow_blank=True, showDropDown=False)
dv.promptTitle = "How do you feel about this topic?"
dv.prompt = "Green, Amber or Red"
ws.add_data_validation(dv)
topic_rngs = [f"{RC}{a}:{RC}{b}" for _, a, b in area_ranges]
for tr in topic_rngs:
    dv.add(tr)
for word, bg, tx in [("Green", G_BG, G_TX), ("Amber", A_BG, A_TX), ("Red", R_BG, R_TX)]:
    for tr in topic_rngs:
        ws.conditional_formatting.add(tr, CellIsRule(
            operator="equal", formula=[f'"{word}"'],
            fill=PatternFill("solid", start_color=bg, end_color=bg),
            font=Font(name=F, size=10.5, bold=True, color=tx)))

for col, w in zip("ABCD", (70, 12, 12, 38)):
    ws.column_dimensions[col].width = w
ws.freeze_panes = f"A{FIRST}"
ws.print_title_rows = f"{HEAD}:{HEAD}"
ws.page_setup.orientation = "portrait"
ws.page_setup.fitToWidth = 1
ws.page_setup.fitToHeight = 0
ws.sheet_properties.pageSetUpPr.fitToPage = True
ws.print_area = f"A1:D{LAST}"

OUT = ("/tmp/claude-0/-home-user-Daily/66a6df15-50ce-540f-aac0-2346f980a922/"
       "scratchpad/IGCSE-Maths-4MA1-Higher-Topic-Check.xlsx")
wb.save(OUT)
print("saved", OUT)
print("topics:", sum(len(v) for _, v in TOPICS), "rows", FIRST, "-", LAST)
