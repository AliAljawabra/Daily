import json
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule
from openpyxl.utils import get_column_letter

recs=json.load(open('recs.json'))
LINK={r['name']:r for r in recs}

F,H,B="Foundation","Higher only","Foundation + Higher"
CORE,STR,LEAVE="Core","Stretch","Not this time"

# ref, topic, what it covers, level, plan, [PMT worksheets]
ROWS=[
("1.1","Integers and the number system","Negative numbers, place value, ordering, the four operations, order of operations, factors, multiples and primes",F,CORE,["Four Operations","Primes, Factors and Multiples","Calculating Problems"]),
("1.2","Fractions","Equivalent fractions and simplifying, mixed numbers, all four operations, a fraction of a quantity, converting to decimals and percentages",F,CORE,["Fractions"]),
("1.3","Decimals","Place value, ordering decimals, converting decimals to fractions and percentages",F,CORE,["Fractions"]),
("1.3H","Recurring decimals","Converting a recurring decimal into a fraction",H,LEAVE,["Recurring Decimals into Fractions"]),
("1.4","Powers and roots","Squares, cubes and their roots, index laws for positive and negative powers, product of prime factors, HCF and LCM",F,CORE,["Roots and Powers","Indices","Primes, Factors and Multiples"]),
("1.4H","Surds and fractional indices","Simplifying and manipulating surds, rationalising a denominator, fractional and negative powers",H,LEAVE,["Surds","Indices"]),
("1.5","Set language and Venn diagrams","Set notation, universal and empty set, complement, Venn diagrams, n(A), subsets",B,CORE,["Venn Diagrams"]),
("1.6","Percentages","Percentage of a quantity, one number as a percentage of another, increase and decrease, reverse percentages, compound interest and depreciation, repeated percentage change",B,CORE,["Percentages","Percentage Increase or Decrease","Compound Interest"]),
("1.7","Ratio and proportion","Ratio notation and simplifying, dividing a quantity in a ratio, unitary method, direct proportion, maps and scale diagrams",F,CORE,["Ratio","Proportion","Scale Factors","Maps and Scale Drawings"]),
("1.8","Degree of accuracy","Rounding to decimal places and significant figures, estimating by rounding to 1 significant figure",F,CORE,["Rounding","Approximation and Estimation"]),
("1.8H","Upper and lower bounds","Identifying bounds and solving problems using them",H,LEAVE,["Bounds"]),
("1.9","Standard form","Calculating with and interpreting numbers in standard form, and solving problems with it",B,CORE,["Standard Form"]),
("1.10","Applying number","Units of mass, length, area, volume and capacity, time calculations, money and currency",F,CORE,["Units of Measure","Using Measures","Calculating Problems"]),
("1.11","Calculator use","Using a scientific calculator to get accurate numerical results",F,CORE,[]),
("2.1","Use of symbols","Symbols for numbers and variables, index notation including zero and negative powers, index laws",B,CORE,["Simplifying Expressions","Indices"]),
("2.2","Algebraic manipulation","Substituting values, collecting like terms, expanding a single bracket and two brackets, taking out common factors, factorising quadratics",B,CORE,["Expanding Equations","Factorising Equations","Simplifying Expressions","Substitution into Equations"]),
("2.2H","Harder algebraic manipulation","Triple brackets, algebraic fractions, completing the square, algebraic proof",H,LEAVE,["Expanding Triple Brackets","Algebraic Fractions","Completing the square","Algebraic Proof"]),
("2.3","Expressions and formulae","Writing and using formulae, substitution, deriving an expression, changing the subject including when the subject appears twice",B,CORE,["Manipulation of Formulae","Deriving Expressions","Forming Equations"]),
("2.4","Linear equations","Solving equations with the unknown on one or both sides, including fractional coefficients, and setting them up from given information",F,CORE,["Solving Linear Equations"]),
("2.5","Proportion (algebraic)","Setting up direct and inverse proportion problems and relating them to graphs",H,STR,["Direct and Inverse Proportion","Algebraic Direct and Inverse Proportions"]),
("2.6","Simultaneous equations","Solving two linear equations in two unknowns, and reading the solution as the intersection of two lines",B,CORE,["Simultaneous Equations","Simultaneous Equations on Graphs"]),
("2.7","Quadratic equations","Solving by factorising",F,STR,["Solving Quadratic Equations","Factorising Equations"]),
("2.7H","Harder quadratics","The quadratic formula, completing the square, forming quadratics from context, one linear and one quadratic simultaneously",H,LEAVE,["Solving Quadratic Equations","Completing the square"]),
("2.8","Inequalities","Inequality symbols, number lines, solving linear inequalities, shading regions on a graph",F,CORE,["Inequalities","Inequalities on Graphs"]),
("2.8H","Quadratic inequalities","Solving quadratic inequalities and harder shaded regions",H,LEAVE,["Quadratic Inequalities"]),
("3.1","Sequences","Term to term and position to term rules, continuing a sequence, the nth term of an arithmetic sequence",F,CORE,["Sequences"]),
("3.1H","Arithmetic series","First term and common difference, the nth term formula, the sum of the first n terms",H,STR,["Sequences"]),
("3.2","Function notation","f(x) notation, domain and range, composite and inverse functions",H,LEAVE,["Functions (Composite or Inverse)"]),
("3.3","Coordinates and straight lines","Coordinates in four quadrants, midpoint of a line segment, gradient, y = mx + c, drawing and interpreting straight line graphs including conversion graphs",F,CORE,["Coordinates","Equations of Straight Lines","Gradients of Straight lines","Graphs of Linear Equations","Interpreting Gradients"]),
("3.3b","Curves and real life graphs","Plotting and interpreting quadratic graphs, distance time and speed time graphs",B,STR,["Graphs of Quadratic Equations","Cubic and Reciprocal Graphs"]),
("3.3H","Harder graphs","Cubic, reciprocal, exponential and trigonometric graphs, transformations of y = f(x), gradients of curves by tangent, circle equations",H,LEAVE,["Exponential and Trigonometric Graphs","Translations and Reflections of Functions","Circle Equations and Tangents","Graphs of Circles","Parallel or Perpendicular Lines"]),
("3.4","Calculus","Differentiating powers of x, gradients and rates of change, stationary points, maxima and minima, linear kinematics",H,LEAVE,[]),
("4.1","Angles, lines and triangles","Types of angle, angles on a line and at a point, parallel line angles, angle sum and exterior angle of a triangle, isosceles and equilateral properties",F,CORE,["Properties of Angles","Triangles"]),
("4.2","Polygons","Naming polygons and quadrilaterals, their properties, interior and exterior angles of regular polygons, angle sum of a polygon, congruence",F,CORE,["Properties of Polygons","2D and 3D Shapes","Vocabulary and Notation"]),
("4.3","Symmetry","Lines of symmetry and order of rotational symmetry",F,CORE,["2D and 3D Shapes"]),
("4.4","Measures","Reading scales, 12 and 24 hour clock, estimating measures, three figure bearings, measuring angles, speed distance time, compound measures such as density and pressure",F,CORE,["Bearings","Speed","Compound Measures","Compound Units","Using Measures"]),
("4.5","Construction","Measuring and drawing accurately, constructing triangles, scale drawings, perpendicular bisector and angle bisector with compasses",F,CORE,["Constructions","Maps and Scale Drawings"]),
("4.6","Circle properties","Circle vocabulary, chord and tangent properties",F,CORE,["Properties of Circles","Vocabulary and Notation"]),
("4.6H","Circle theorems","Intersecting chord properties, cyclic quadrilaterals, angle at the centre, angle in a semicircle, alternate segment",H,LEAVE,["Circle Theorems"]),
("4.7","Geometrical reasoning","Giving reasons for angle answers using standard geometrical statements",B,CORE,["Properties of Angles"]),
("4.8","Pythagoras and trigonometry in 2D","Pythagoras' theorem, sine cosine and tangent in right angled triangles, problems in two dimensions including bearings",F,CORE,["Pythagoras' Theorem","Trig Ratios and Exact Values","Bearings"]),
("4.8H","Advanced trigonometry","Obtuse angles, elevation and depression, sine and cosine rules, area of a triangle using ½ab sin C, Pythagoras and trigonometry in 3D",H,LEAVE,["Sine Rule, Cosine Rule and Area","Pythagoras and trig (3D)"]),
("4.9","Perimeter and area","Converting area units, perimeter and area of triangles, rectangles, parallelograms and trapezia, circumference and area of circles and semicircles",F,CORE,["Area","Perimeter","Compound Area","Area of Shaded Region","Area or Perimeter Problem"]),
("4.9H","Sectors and arcs","Perimeter and area of sectors of circles",H,STR,["Sectors, Segments and Arcs"]),
("4.10","3D shapes and volume","Naming solids, faces edges and vertices, surface area, surface area of a cylinder, volume of prisms and cylinders, converting volume units",F,CORE,["Volume and Surface Area","2D and 3D Shapes"]),
("4.10H","Spheres and cones","Surface area and volume of a sphere and a right circular cone",H,STR,["Volume and Surface Area"]),
("4.11","Similarity","Similar figures have corresponding lengths in the same ratio, using and interpreting maps and scale drawings",F,CORE,["Congruence and Similarity","Maps and Scale Drawings"]),
("4.11H","Area and volume of similar shapes","Areas in the ratio of the square, volumes in the ratio of the cube, and using these to solve problems",H,STR,["Similar (2D or 3D)"]),
("5.1","Vectors","Magnitude and direction, column vectors, multiplying by a scalar, adding and subtracting, modulus, resultant, vector proof",H,LEAVE,["Manipulating Vectors","Vector Proof","Translations as 2D vectors"]),
("5.2","Transformation geometry","Rotations about a point, reflections in a mirror line, translations by a column vector, enlargement by a scale factor about a centre, describing a transformation fully",F,CORE,["Transformations of Shapes","Translations as 2D vectors"]),
("6.1","Presenting data","Pictograms, bar charts, pie charts, two way tables, tabulating data and interpreting statistical diagrams",F,CORE,["Interpreting Data","Frequency Tables"]),
("6.1H","Histograms and cumulative frequency","Histograms with unequal class intervals, constructing and using cumulative frequency diagrams",H,LEAVE,["Histograms","Cumulative Frequency Graphs"]),
("6.2","Averages","Mean, median, mode and range, estimated mean for grouped data, the modal class",F,CORE,["Mean, Median, Mode, Range","Frequency Tables"]),
("6.2H","Spread and quartiles","Median from a cumulative frequency diagram, interquartile range from a data set and from a diagram",H,STR,["Cumulative Frequency Graphs"]),
("6.3","Probability","Probability language and scale, sample space, listing outcomes, Venn diagrams, complement, addition rule for mutually exclusive events, expected frequency",F,CORE,["Probability of Events","Probability Equations","Venn Diagrams"]),
("6.3H","Tree diagrams and conditional probability","Tree diagrams, independent events, simple conditional probability",H,CORE,["Tree Diagrams","Conditional Probability"]),
]

NAVY="FF162947"; GOLD="FFC3A965"; TINT="FFEFEBE1"
RED="FFF4CCCC"; AMB="FFFCE5CD"; GRN="FFD9EAD3"
hdrF=Font(name="Arial",size=10,bold=True,color="FFF6F4EF"); hdrFill=PatternFill("solid",fgColor=NAVY)
bodyF=Font(name="Arial",size=10); linkF=Font(name="Arial",size=10,color="FF0563C1",underline="single")
thin=Side(style="thin",color="FFD8D3C6"); bd=Border(bottom=thin)
wrap=Alignment(wrap_text=True,vertical="top"); top=Alignment(vertical="top")

wb=Workbook()

# ---------- Start here ----------
s0=wb.active; s0.title="Start here"
s0["A1"]="Charlotte: maths topic check"; s0["A1"].font=Font(name="Arial",size=16,bold=True,color=NAVY)
s0["A2"]="Edexcel International GCSE Mathematics A (4MA1), Higher Tier. Every topic below is taken from the Pearson specification."
s0["A2"].font=Font(name="Arial",size=10,italic=True,color="FF5D6471")
intro=[("What to do","Go to the RAG tracker tab. For each row, read the topic and what it covers, then put R, A or G in the 'Your rating' column. That is the only column you need to fill in, plus Notes if you want."),
("R","I could not start this, or I would get it wrong."),
("A","I can do it but slowly, or I get some of it right and some wrong."),
("G","I can do this confidently and quickly."),
("Be honest rather than kind","A topic marked G gets almost no time from us. If you are unsure between two ratings, pick the lower one."),
("Higher only rows","Some rows are marked 'Higher only'. Those are the harder end of the paper. Rate them anyway, even if you have never seen them."),
("How long","About 55 rows. It should take 20 to 30 minutes. You do not need to do any maths to fill it in."),
]
r=4
for k,v in intro:
    s0.cell(r,1,k).font=Font(name="Arial",size=10,bold=True,color=NAVY)
    s0.cell(r,2,v).font=Font(name="Arial",size=10); s0.cell(r,2).alignment=wrap
    s0.row_dimensions[r].height=30; r+=1
r+=1
s0.cell(r,1,"Example of a filled row").font=Font(name="Arial",size=11,bold=True,color=NAVY); r+=1
ex=["Ref","Topic","What it covers","Level","Your rating","Notes"]
for c,h in enumerate(ex,1): s0.cell(r,c,h).font=hdrF; s0.cell(r,c).fill=hdrFill
r+=1
exv=["1.2","Fractions","Equivalent fractions and simplifying, mixed numbers, all four operations","Foundation","A","Fine adding, always get stuck dividing"]
for c,v in enumerate(exv,1):
    cc=s0.cell(r,c,v); cc.font=bodyF; cc.alignment=wrap; cc.border=bd
s0.cell(r,5).fill=PatternFill("solid",fgColor=AMB)
for col,wd in zip(range(1,7),[22,26,46,16,12,34]): s0.column_dimensions[get_column_letter(col)].width=wd

# ---------- RAG tracker ----------
ws=wb.create_sheet("RAG tracker")
cols=["Ref","Topic","What it covers","Level","Your rating","Notes","In our plan","What we do about it"]
ws.append(cols)
for c in ws[1]: c.font=hdrF; c.fill=hdrFill; c.alignment=Alignment(vertical="center",wrap_text=True)
ws.row_dimensions[1].height=30; ws.freeze_panes="A2"
for i,(ref,topic,covers,level,plan,sheets) in enumerate(ROWS,start=2):
    ws.cell(i,1,ref); ws.cell(i,2,topic); ws.cell(i,3,covers); ws.cell(i,4,level)
    ws.cell(i,5,""); ws.cell(i,6,""); ws.cell(i,7,plan)
    ws.cell(i,8,f'=IF($E{i}="","",IF($E{i}="R","Full worksheet, taught first",'
                f'IF($E{i}="A","Work until 3 right in a row",'
                f'IF($E{i}="G","2 question spot check in week 5",""))))')
    for c in range(1,9):
        cell=ws.cell(i,c); cell.font=bodyF; cell.border=bd
        cell.alignment=wrap if c in (3,6,8) else top
    ws.row_dimensions[i].height=34
last=len(ROWS)+1
dv=DataValidation(type="list",formula1='"R,A,G"',allow_blank=True,showDropDown=False)
dv.error="Enter R, A or G"; dv.prompt="R = cannot do it, A = shaky, G = confident"
ws.add_data_validation(dv); dv.add(f"E2:E{last}")
for val,col in (("R",RED),("A",AMB),("G",GRN)):
    ws.conditional_formatting.add(f"E2:E{last}",
        CellIsRule(operator="equal",formula=[f'"{val}"'],fill=PatternFill("solid",fgColor=col)))
inputFill=PatternFill("solid",fgColor="FFFFF2CC")
for i in range(2,last+1):
    ws.cell(i,5).fill=inputFill; ws.cell(i,6).fill=inputFill
    ws.cell(i,5).alignment=Alignment(horizontal="center",vertical="center")
    ws.cell(i,5).font=Font(name="Arial",size=11,bold=True)
for col,wd in zip(range(1,9),[7,30,60,17,11,30,13,27]): ws.column_dimensions[get_column_letter(col)].width=wd

# ---------- Worksheets ----------
ws2=wb.create_sheet("Worksheets")
ws2.append(["Ref","Topic","In our plan","Your rating","PMT worksheet","Questions","QP","MS","Answers","Started","3 in a row","Cleared"])
for c in ws2[1]: c.font=hdrF; c.fill=hdrFill; c.alignment=Alignment(vertical="center",wrap_text=True)
ws2.row_dimensions[1].height=30; ws2.freeze_panes="A2"
r=1; missing=[]
for i,(ref,topic,covers,level,plan,sheets) in enumerate(ROWS,start=2):
    if not sheets:
        r+=1
        ws2.cell(r,1,ref); ws2.cell(r,2,topic); ws2.cell(r,3,plan)
        ws2.cell(r,4,f"='RAG tracker'!$E{i}")
        ws2.cell(r,5,"No PMT worksheet for this topic")
        for c in range(1,13): ws2.cell(r,c).font=bodyF; ws2.cell(r,c).border=bd
        continue
    for sname in sheets:
        r+=1
        ws2.cell(r,1,ref); ws2.cell(r,2,topic); ws2.cell(r,3,plan)
        ws2.cell(r,4,f"='RAG tracker'!$E{i}")
        ws2.cell(r,5,sname)
        rec=LINK.get(sname)
        if rec:
            ws2.cell(r,6,13)
            for lab,k,col in (("QP","QP",7),("MS","MS",8),("Ans","MA",9)):
                cc=ws2.cell(r,col,lab); cc.hyperlink=rec[k]; cc.font=linkF
        else:
            missing.append(sname)
        for c in range(1,13):
            cell=ws2.cell(r,c)
            if c not in (7,8,9): cell.font=bodyF
            cell.border=bd
        for c in (10,11,12): ws2.cell(r,c).fill=inputFill
for val,col in (("R",RED),("A",AMB),("G",GRN)):
    ws2.conditional_formatting.add(f"D2:D{r}",
        CellIsRule(operator="equal",formula=[f'"{val}"'],fill=PatternFill("solid",fgColor=col)))
for col,wd in zip(range(1,13),[7,28,13,10,34,10,6,6,7,10,11,10]): ws2.column_dimensions[get_column_letter(col)].width=wd
wsheets_last=r

# ---------- Summary ----------
s3=wb.create_sheet("Summary",0)
s3["A1"]="Summary"; s3["A1"].font=Font(name="Arial",size=16,bold=True,color=NAVY)
s3["A2"]="Fills in automatically once the RAG tracker is completed."
s3["A2"].font=Font(name="Arial",size=10,italic=True,color="FF5D6471")
s3.append([]); s3.append(["Rating","Topics","What we do","Questions each","Questions total"])
for c in s3[4]: c.font=hdrF; c.fill=hdrFill
plan_rows=[("R","Full worksheet, taught first",13),("A","Work until 3 right in a row",6),("G","2 question spot check",2)]
rr=4
for val,act,q in plan_rows:
    rr+=1
    s3.cell(rr,1,val); s3.cell(rr,2,f"=COUNTIFS('RAG tracker'!$E$2:$E${last},$A{rr})")
    s3.cell(rr,3,act); s3.cell(rr,4,q); s3.cell(rr,5,f"=$B{rr}*$D{rr}")
    for c in range(1,6): s3.cell(rr,c).font=bodyF; s3.cell(rr,c).border=bd
    s3.cell(rr,1).fill=PatternFill("solid",fgColor={"R":RED,"A":AMB,"G":GRN}[val])
rr+=1
s3.cell(rr,1,"Not yet rated"); s3.cell(rr,2,f"=COUNTIFS('RAG tracker'!$E$2:$E${last},\"\")")
for c in range(1,6): s3.cell(rr,c).font=bodyF; s3.cell(rr,c).border=bd
rr+=1
s3.cell(rr,3,"Total questions"); s3.cell(rr,5,f"=SUM(E5:E7)")
s3.cell(rr,3).font=Font(name="Arial",size=10,bold=True); s3.cell(rr,5).font=Font(name="Arial",size=10,bold=True)
s3.cell(rr,3).fill=PatternFill("solid",fgColor=TINT); s3.cell(rr,5).fill=PatternFill("solid",fgColor=TINT)
rr+=1
s3.cell(rr,3,"Hours at about 2.5 min a question"); s3.cell(rr,5,f"=ROUND($E{rr-1}*2.5/60,1)")
s3.cell(rr,3).font=bodyF; s3.cell(rr,5).font=bodyF
rr+=1
s3.cell(rr,3,"Hours per week over six weeks"); s3.cell(rr,5,f"=ROUND($E{rr-1}/6,1)")
s3.cell(rr,3).font=bodyF; s3.cell(rr,5).font=bodyF
rr+=2
s3.cell(rr,1,"Assumptions").font=Font(name="Arial",size=11,bold=True,color=NAVY)
for i,t in enumerate([
 "13 questions per worksheet is the measured median of the PMT Higher sheets (13 pages, about 45 marks).",
 "2.5 minutes a question is an estimate. Charlotte has extra time, so treat the hours as a floor.",
 "Amber topics stop at 3 correct in a row, so 6 is an average rather than a fixed number.",
 "Rows marked 'Not this time' in the plan column sit above a grade 5 and are not scheduled, whatever the rating.",
 "3.4 Calculus is on the Higher specification but PMT has no topic worksheet for it."],start=1):
    s3.cell(rr+i,1,t).font=Font(name="Arial",size=10,color="FF5D6471")
for col,wd in zip(range(1,6),[18,12,38,16,16]): s3.column_dimensions[get_column_letter(col)].width=wd

wb.save("Charlotte_RAG_tracker.xlsx")
print("rows:",len(ROWS),"worksheet rows:",wsheets_last-1,"unmatched:",set(missing))
