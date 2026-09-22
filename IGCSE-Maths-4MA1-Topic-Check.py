"""Edexcel IGCSE Maths A (4MA1) — student topic RAG sheet."""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule
from openpyxl.utils import get_column_letter

# ---- palette (matches the deck) ----
NAVY, AMBER_D, SLATE = "0D2B4E", "D4861B", "5A6B7C"
TINT, WHITE, HAIR = "EEF3F8", "FFFFFF", "DCE6F0"
G_BG, G_TX = "DCF0E4", "1B6B4A"
A_BG, A_TX = "FCEBCE", "8A5A00"
R_BG, R_TX = "FADCD9", "9B2C20"
F = "Calibri"

TOPICS = [
 ("1  Number and the number system", [
  ("Place value, ordering, rounding to decimal places and significant figures", "Both"),
  ("Four operations with integers, decimals and negative numbers", "Both"),
  ("Factors, multiples, primes, HCF and LCM, prime factorisation", "Both"),
  ("Fractions: simplifying, comparing, all four operations, mixed numbers", "Both"),
  ("Converting between fractions, decimals and percentages", "Both"),
  ("Percentage of an amount; percentage increase and decrease", "Both"),
  ("Percentage change, profit and loss", "Both"),
  ("Reverse percentages (finding the original amount)", "Both"),
  ("Compound interest, depreciation, growth and decay", "Both"),
  ("Ratio: simplifying, sharing in a ratio, the unitary method", "Both"),
  ("Direct and inverse proportion", "Both"),
  ("Compound measures: speed, density and pressure", "Both"),
  ("Powers, roots and the index laws", "Both"),
  ("Negative and fractional indices", "Higher"),
  ("Standard form: writing, converting and calculating", "Both"),
  ("Surds: simplifying and rationalising the denominator", "Higher"),
  ("Upper and lower bounds; error intervals", "Higher"),
  ("Recurring decimals into fractions", "Higher"),
  ("Set language, set notation and Venn diagrams", "Both"),
 ]),
 ("2  Equations, formulae and identities", [
  ("Algebraic notation and collecting like terms", "Both"),
  ("Expanding single brackets", "Both"),
  ("Expanding double brackets", "Both"),
  ("Factorising using a common factor", "Both"),
  ("Factorising quadratics of the form x² + bx + c", "Both"),
  ("Factorising quadratics of the form ax² + bx + c", "Higher"),
  ("The difference of two squares", "Higher"),
  ("Substituting numbers into expressions and formulae", "Both"),
  ("Solving linear equations, including x on both sides", "Both"),
  ("Solving equations with brackets and with fractions", "Both"),
  ("Rearranging a formula to change the subject", "Both"),
  ("Rearranging where the new subject appears twice", "Higher"),
  ("Simultaneous linear equations", "Both"),
  ("Simultaneous equations where one is quadratic", "Higher"),
  ("Solving quadratic equations by factorising", "Both"),
  ("Solving quadratic equations with the formula", "Higher"),
  ("Completing the square", "Higher"),
  ("Algebraic fractions: simplifying and the four operations", "Higher"),
  ("Solving equations that contain algebraic fractions", "Higher"),
  ("Linear inequalities and representing them on a number line", "Both"),
  ("Quadratic inequalities", "Higher"),
  ("Proportionality, including squares and cubes", "Higher"),
  ("Forming an equation from a worded problem, then solving it", "Both"),
  ("Algebraic proof and reasoning", "Higher"),
 ]),
 ("3  Sequences, functions and graphs", [
  ("Sequences: term-to-term rules and number patterns", "Both"),
  ("The nth term of a linear sequence", "Both"),
  ("The nth term of a quadratic sequence", "Higher"),
  ("Coordinates and the midpoint of a line segment", "Both"),
  ("Plotting straight-line graphs", "Both"),
  ("Gradient, intercept and the equation y = mx + c", "Both"),
  ("Finding the equation of a line through two points", "Both"),
  ("Parallel and perpendicular lines", "Higher"),
  ("Real-life graphs, including distance–time graphs", "Both"),
  ("Plotting and interpreting quadratic graphs", "Both"),
  ("Cubic and reciprocal graphs", "Higher"),
  ("Exponential graphs, growth and decay", "Higher"),
  ("Graphs of sine, cosine and tangent", "Higher"),
  ("Solving equations graphically", "Both"),
  ("Function notation f(x)", "Higher"),
  ("Composite and inverse functions", "Higher"),
  ("Transformations of graphs", "Higher"),
  ("Differentiating polynomials (the power rule)", "Higher"),
  ("The gradient of a curve at a point, and tangents", "Higher"),
  ("Turning points: maximum and minimum", "Higher"),
  ("Kinematics: displacement, velocity and acceleration", "Higher"),
 ]),
 ("4  Geometry and trigonometry", [
  ("Angle facts: on a line, at a point, and in a triangle", "Both"),
  ("Angles in parallel lines", "Both"),
  ("Interior and exterior angles of polygons", "Both"),
  ("Properties of triangles and quadrilaterals", "Both"),
  ("Congruence and similarity", "Both"),
  ("Similar shapes: length scale factor", "Both"),
  ("Similar shapes: area and volume scale factors", "Higher"),
  ("Perimeter and area of rectangles, triangles, parallelograms, trapezia", "Both"),
  ("Circles: circumference and area", "Both"),
  ("Arcs, sectors and segments", "Higher"),
  ("Circle theorems", "Higher"),
  ("Volume and surface area of prisms and cylinders", "Both"),
  ("Volume and surface area of cones, spheres and pyramids", "Higher"),
  ("Pythagoras' theorem", "Both"),
  ("Trigonometry in right-angled triangles (SOHCAHTOA)", "Both"),
  ("Angles of elevation and depression", "Both"),
  ("Bearings", "Both"),
  ("Pythagoras and trigonometry in 3D", "Higher"),
  ("The sine rule and the cosine rule", "Higher"),
  ("Area of a triangle using ½ab sin C", "Higher"),
  ("Constructions and loci", "Both"),
  ("Scale drawings and maps", "Both"),
  ("Symmetry", "Both"),
 ]),
 ("5  Vectors and transformation geometry", [
  ("Reflection, rotation, translation and enlargement", "Both"),
  ("Negative and fractional scale factors", "Higher"),
  ("Combined transformations", "Higher"),
  ("Vector notation, magnitude, addition and scalar multiples", "Higher"),
  ("Vector geometry and vector proof", "Higher"),
 ]),
 ("6  Statistics and probability", [
  ("Collecting data: tally charts and frequency tables", "Both"),
  ("Two-way tables", "Both"),
  ("Bar charts, pictograms and pie charts", "Both"),
  ("Mean, median, mode and range", "Both"),
  ("Mean from a frequency table", "Both"),
  ("Estimated mean from grouped data", "Both"),
  ("Scatter graphs, correlation and the line of best fit", "Both"),
  ("Cumulative frequency graphs", "Higher"),
  ("Box plots and quartiles", "Higher"),
  ("Histograms with unequal class widths", "Higher"),
  ("The probability scale and single-event probability", "Both"),
  ("Mutually exclusive and exhaustive events", "Both"),
  ("Relative frequency and expected frequency", "Both"),
  ("Sample space diagrams", "Both"),
  ("Tree diagrams, with replacement", "Both"),
  ("Tree diagrams without replacement; conditional probability", "Higher"),
  ("Venn diagrams in probability", "Both"),
 ]),
]

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
    cell.alignment = Alignment(horizontal=kw.get("h", "left"),
                               vertical=kw.get("v", "center"),
                               wrap_text=kw.get("wrap", False))
    if kw.get("border"):
        cell.border = box
    return cell

# ---------- header ----------
put(1, 1, "Edexcel IGCSE Mathematics A (4MA1)  —  Topic check", size=17, bold=True, color=NAVY)
put(2, 1, "Please fill this in before our first lesson. It takes about ten minutes. Don't think too hard about any single row.", size=10.5, color=SLATE)

put(4, 1, "NAME", size=9, bold=True, color=AMBER_D)
put(4, 2, "TIER", size=9, bold=True, color=AMBER_D)
put(4, 3, "DATE", size=9, bold=True, color=AMBER_D)
for c in (1, 2, 3):
    put(5, c, "", fill=TINT, border=True)

for i, (name, meaning, bg, tx) in enumerate([
        ("Green", "I could do this in a test tomorrow", G_BG, G_TX),
        ("Amber", "I've seen it, but I'd need reminding", A_BG, A_TX),
        ("Red",   "I don't recognise this, or I always get it wrong", R_BG, R_TX)]):
    put(7 + i, 1, f"{name}  —  {meaning}", size=10.5, fill=bg, color=tx)

put(10, 1, "Rows marked Higher are on the Higher paper only. On Foundation, leave those blank. There is no wrong answer here \u2014 an honest red is worth far more to me than a hopeful green.", size=10, italic=True, color=SLATE)

# ---------- live counts ----------
HEAD = 12
FIRST = HEAD + 1
total_rows = sum(len(v) + 1 for _, v in TOPICS)
LAST = FIRST + total_rows - 1
put(7, 4, "RUNNING TOTAL", size=9, bold=True, color=AMBER_D)
ws.cell(row=8, column=4,
        value=f'=COUNTIF(C{FIRST}:C{LAST},"Green")&" green    "&'
              f'COUNTIF(C{FIRST}:C{LAST},"Amber")&" amber    "&'
              f'COUNTIF(C{FIRST}:C{LAST},"Red")&" red"').font = Font(name=F, size=12, bold=True, color=NAVY)
put(9, 4, "Fills in as you go.", size=9.5, italic=True, color=SLATE)

# ---------- table ----------
for i, h in enumerate(["Topic", "Tier", "How I feel about it", "Anything you want to tell me"], start=1):
    put(HEAD, i, h, bold=True, color=WHITE, fill=NAVY, size=10.5,
        h="left" if i in (1, 4) else "center")
ws.row_dimensions[HEAD].height = 22

row = FIRST
area_ranges = []
for area, items in TOPICS:
    put(row, 1, area, bold=True, color=NAVY, fill=TINT, size=11.5)
    for c in (2, 3, 4):
        put(row, c, "", fill=TINT)
    ws.row_dimensions[row].height = 21
    row += 1
    start = row
    for topic, tier in items:
        put(row, 1, topic, size=10.5, border=True)
        put(row, 2, tier, size=9.5, color=SLATE if tier == "Both" else AMBER_D,
            h="center", border=True, bold=(tier == "Higher"))
        put(row, 3, "", h="center", border=True)
        put(row, 4, "", size=10, color=SLATE, border=True)
        ws.row_dimensions[row].height = 18
        row += 1
    area_ranges.append((area, start, row - 1))

# ---------- dropdown + colour ----------
dv = DataValidation(type="list", formula1='"Green,Amber,Red"', allow_blank=True, showDropDown=False)
dv.prompt = "Green, Amber or Red"
dv.promptTitle = "How do you feel about this topic?"
ws.add_data_validation(dv)
# only the real topic rows — not the six section-header rows
topic_rngs = [f"C{a}:C{b}" for _, a, b in area_ranges]
for tr in topic_rngs:
    dv.add(tr)

for word, bg, tx in [("Green", G_BG, G_TX), ("Amber", A_BG, A_TX), ("Red", R_BG, R_TX)]:
  for tr in topic_rngs:
    ws.conditional_formatting.add(tr, CellIsRule(
        operator="equal", formula=[f'"{word}"'],
        fill=PatternFill("solid", start_color=bg, end_color=bg),
        font=Font(name=F, size=10.5, bold=True, color=tx)))

# ---------- layout ----------
for col, w in zip("ABCD", (74, 10, 21, 42)):
    ws.column_dimensions[col].width = w
ws.freeze_panes = f"A{FIRST}"
ws.print_title_rows = f"{HEAD}:{HEAD}"
ws.page_setup.orientation = "portrait"
ws.page_setup.fitToWidth = 1
ws.page_setup.fitToHeight = 0
ws.sheet_properties.pageSetUpPr.fitToPage = True
ws.print_area = f"A1:D{LAST}"

# ============ sheet 2: summary ============
s2 = wb.create_sheet("Summary")
s2.sheet_view.showGridLines = False
def put2(r, c, v, **kw):
    cell = s2.cell(row=r, column=c, value=v)
    cell.font = Font(name=F, size=kw.get("size", 11), bold=kw.get("bold", False),
                     color=kw.get("color", "000000"), italic=kw.get("italic", False))
    if kw.get("fill"):
        cell.fill = PatternFill("solid", fgColor=kw["fill"])
    cell.alignment = Alignment(horizontal=kw.get("h", "left"), vertical="center")
    if kw.get("border"):
        cell.border = box
    return cell

put2(1, 1, "Summary", size=18, bold=True, color=NAVY)
put2(2, 1, "Fills in on its own as the topic sheet is completed.", size=10.5, color=SLATE)
for i, h in enumerate(["Area", "Green", "Amber", "Red", "Not yet rated"], start=1):
    put2(4, i, h, bold=True, color=WHITE, fill=NAVY, size=10.5,
         h="left" if i == 1 else "center")
s2.row_dimensions[4].height = 22

r = 5
for area, a, b in area_ranges:
    put2(r, 1, area, size=10.5, border=True)
    n = b - a + 1
    for j, word in enumerate(["Green", "Amber", "Red"], start=2):
        c = put2(r, j, f"='Topic check'!$A$1", border=True)
        c.value = f'=COUNTIF(\'Topic check\'!C{a}:C{b},"{word}")'
        c.alignment = Alignment(horizontal="center", vertical="center")
        c.font = Font(name=F, size=10.5, color=[G_TX, A_TX, R_TX][j - 2], bold=True)
    c = put2(r, 5, f'={n}-SUM(B{r}:D{r})', border=True, h="center", color=SLATE, size=10.5)
    s2.row_dimensions[r].height = 19
    r += 1

put2(r, 1, "Total", bold=True, color=NAVY, fill=TINT, size=11)
for j in range(2, 6):
    c = put2(r, j, f"=SUM({get_column_letter(j)}5:{get_column_letter(j)}{r-1})",
             bold=True, h="center", fill=TINT, size=11, color=NAVY)
s2.row_dimensions[r].height = 21

put2(r + 2, 1, "We start with the reds in the biggest areas. Ambers get folded into practice. Greens we leave alone.",
     size=11, italic=True, color=NAVY)
for col, w in zip("ABCDE", (40, 12, 12, 12, 16)):
    s2.column_dimensions[col].width = w

# ============ sheet 3: practice ============
s3 = wb.create_sheet("Where to practise")
s3.sheet_view.showGridLines = False
def put3(r, c, v, **kw):
    cell = s3.cell(row=r, column=c, value=v)
    cell.font = Font(name=F, size=kw.get("size", 11), bold=kw.get("bold", False),
                     color=kw.get("color", "000000"), italic=kw.get("italic", False))
    if kw.get("fill"):
        cell.fill = PatternFill("solid", fgColor=kw["fill"])
    cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=kw.get("wrap", False))
    if kw.get("border"):
        cell.border = box
    return cell

put3(1, 1, "Where to practise", size=18, bold=True, color=NAVY)
put3(2, 1, "All free. Search any topic name from the checklist and you'll find questions on it.", size=10.5, color=SLATE)
for i, h in enumerate(["Site", "What it's best for"], start=1):
    put3(4, i, h, bold=True, color=WHITE, fill=NAVY, size=10.5)
s3.row_dimensions[4].height = 22
sites = [
 ("Maths Genie", "Past-paper questions sorted by topic and by grade, with worked solutions. Start here."),
 ("Physics & Maths Tutor", "Edexcel IGCSE 4MA1 questions grouped by topic, with mark schemes."),
 ("Corbettmaths", "A short video and a worksheet for every topic. The 5-a-day sheets are ideal for daily practice."),
 ("Dr Frost Maths", "Free account, marks itself, and remembers what you got wrong."),
 ("Save My Exams", "Revision notes and topic questions for 4MA1 specifically."),
 ("Past papers", "4MA1 papers back to 2018, plus the R variants. Always use the real mark scheme."),
]
r = 5
for name, what in sites:
    put3(r, 1, name, size=11, bold=True, color=NAVY, border=True)
    put3(r, 2, what, size=10.5, color=SLATE, border=True)
    s3.row_dimensions[r].height = 20
    r += 1
put3(r + 1, 1, "Check you're getting IGCSE 4MA1 material, not domestic GCSE — the overlap is large but not total, and both IGCSE papers allow a calculator.",
     size=10.5, italic=True, color=NAVY)
s3.column_dimensions["A"].width = 26
s3.column_dimensions["B"].width = 86

OUT = "/tmp/claude-0/-home-user-Daily/66a6df15-50ce-540f-aac0-2346f980a922/scratchpad/IGCSE-Maths-4MA1-Topic-Check.xlsx"
wb.save(OUT)
print("saved", OUT)
print("topics:", sum(len(v) for _, v in TOPICS), "| rows", FIRST, "-", LAST)
