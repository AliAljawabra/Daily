import json
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule
from openpyxl.utils import get_column_letter

topics=json.load(open('mg_topics.json'))
recs={r['name']:r for r in json.load(open('recs.json'))}
BASE="https://mathsgenie.co.uk/igcse/maths/edexcel/"

PMT={
"addition and subtraction":["Four Operations"],"multiplication and division":["Four Operations"],
"time":["Using Measures"],"writing simplifying and ordering fractions":["Fractions"],
"place value":[],"rounding":["Rounding"],"negative numbers":["Four Operations"],
"powers and roots":["Roots and Powers"],"bidmas":["Four Operations"],
"factors and multiples":["Primes, Factors and Multiples"],"coordinates":["Coordinates"],
"pictograms":["Interpreting Data"],
"calculation problems":["Calculating Problems"],"using a calculator":[],
"systematic listing":["Probability of Events"],"fractions of an amount":["Fractions"],
"fractions decimals and percentages":["Percentages"],"simplifying algebra":["Simplifying Expressions"],
"writing an expression":["Deriving Expressions"],"function machines":[],
"solving one step equations":["Solving Linear Equations"],"angles":["Properties of Angles"],
"area and perimeter":["Area","Perimeter"],"probability":["Probability of Events"],
"frequency polygons":["Interpreting Data"],"averages":["Mean, Median, Mode, Range"],
"bar charts":["Interpreting Data"],"pie charts":["Interpreting Data"],
"fractions":["Fractions"],"estimating":["Approximation and Estimation"],
"writing and simplifying ratio":["Ratio"],"ratio":["Ratio"],"proportion":["Proportion"],
"percentages":["Percentages"],"percentage change":["Percentage Increase or Decrease"],
"exchange rates":["Units of Measure"],"conversions and units":["Units of Measure"],
"scale drawings":["Maps and Scale Drawings"],"best buy questions":["Compound Measures"],
"substitution":["Substitution into Equations"],"solving equations":["Solving Linear Equations"],
"drawing graphs":["Graphs of Linear Equations"],"area and circumference of circles":["Area"],
"transformations":["Transformations of Shapes"],"area of compound shapes":["Compound Area"],
"frequency trees":["Probability of Events"],
"compound interest and depreciation":["Compound Interest"],"indices":["Indices"],
"prime factors hcf and lcm":["Primes, Factors and Multiples"],
"real life and distance time graphs":["Interpreting Gradients"],"inequalities":["Inequalities"],
"forming and solving equations":["Forming Equations"],"sequences nth term":["Sequences"],
"expanding and factorising":["Expanding Equations","Factorising Equations"],
"pythagoras":["Pythagoras' Theorem"],"angles in parallel lines":["Properties of Angles"],
"angles in polygons":["Properties of Polygons"],"surface area":["Volume and Surface Area"],
"volume of a prism":["Volume and Surface Area"],"cylinders":["Volume and Surface Area"],
"construction":["Constructions"],"bearings":["Bearings"],
"averages from frequency tables":["Frequency Tables"],
"reverse percentages":["Percentages"],"standard form":["Standard Form"],
"speed and density":["Speed","Compound Measures"],
"changing the subject of a formula":["Manipulation of Formulae"],
"expanding and factorising quadratics":["Factorising Equations"],
"solving quadratics":["Solving Quadratic Equations"],
"drawing quadratic graphs":["Graphs of Quadratic Equations"],
"simultaneous equations":["Simultaneous Equations"],
"inequalities on graphs":["Inequalities on Graphs"],
"similar shapes lengths":["Congruence and Similarity"],
"sohcahtoa trigonometry":["Trig Ratios and Exact Values"],"venn diagrams":["Venn Diagrams"],
"data":["Interpreting Data"],
"recurring decimals to fractions":["Recurring Decimals into Fractions"],
"fractional and negative indices":["Indices"],
"direct and inverse proportion":["Direct and Inverse Proportion"],
"expanding triple brackets":["Expanding Triple Brackets"],
"drawing other graphs cubic reciprocal":["Cubic and Reciprocal Graphs"],
"solving simultaneous equations graphically":["Simultaneous Equations on Graphs"],
"gradient of a line":["Gradients of Straight lines"],
"equation of a line":["Equations of Straight Lines"],
"spheres and cones":["Volume and Surface Area"],
"sector areas and arc lengths":["Sectors, Segments and Arcs"],
"parallel and perpendicular lines":["Parallel or Perpendicular Lines"],
"similar shapes area and volume":["Similar (2D or 3D)"],"circle theorems":["Circle Theorems"],
"cumulative frequency":["Cumulative Frequency Graphs"],"vectors":["Manipulating Vectors"],
"probability trees":["Tree Diagrams"],
"surds":["Surds"],"bounds":["Bounds"],"quadratic formula":["Solving Quadratic Equations"],
"factorising harder quadratics":["Factorising Equations"],"algebraic fractions":["Algebraic Fractions"],
"rearranging harder formulae":["Manipulation of Formulae"],
"trigonometric and exponential graphs":["Exponential and Trigonometric Graphs"],
"finding the area of any triangle":["Sine Rule, Cosine Rule and Area"],
"the sine rule":["Sine Rule, Cosine Rule and Area"],"the cosine rule":["Sine Rule, Cosine Rule and Area"],
"3d pythagoras and trigonometry":["Pythagoras and trig (3D)"],
"the magnitude of a vector":["Manipulating Vectors"],"histograms":["Histograms"],
"conditional probability":["Conditional Probability"],
"quadratic simultaneous equations":["Simultaneous Equations"],
"transforming graphs y f x":["Translations and Reflections of Functions"],
"proof":["Algebraic Proof"],"completing the square":["Completing the square"],
"inverse and composite functions":["Functions (Composite or Inverse)"],
"quadratic inequalities":["Quadratic Inequalities"],"sequences higher":["Sequences"],
"differentiation":[],"vectors proof questions":["Vector Proof"],
"probability equation questions":["Probability Equations"],
}
missing=[t['title'] for t in topics if t['title'] not in PMT]
assert not missing, missing
NAVY="FF162947"; GOLD="FFC3A965"; TINT="FFEFEBE1"
RED="FFF4CCCC"; AMB="FFFCE5CD"; GRN="FFD9EAD3"; INP="FFFFF2CC"
hdrF=Font(name="Arial",size=10,bold=True,color="FFF6F4EF"); hdrFill=PatternFill("solid",fgColor=NAVY)
bodyF=Font(name="Arial",size=10); linkF=Font(name="Arial",size=10,color="FF0563C1",underline="single")
thin=Side(style="thin",color="FFD8D3C6")
vrule=Side(style="medium",color=NAVY); bd=Border(bottom=thin)
wrap=Alignment(wrap_text=True,vertical="top"); top=Alignment(vertical="top")
GBAND={1:"FFF2F2F2",2:"FFF2F2F2",3:"FFF2F2F2",4:"FFFFFFFF",5:"FFFFFFFF",6:TINT,7:"FFEDEDED",8:"FFEDEDED"}

wb=Workbook()
s0=wb.active; s0.title="Start here"
s0["A1"]="Charlotte: maths topic check"; s0["A1"].font=Font(name="Arial",size=16,bold=True,color=NAVY)
s0["A2"]="Edexcel International GCSE Maths, Higher Tier. 119 topics, listed in grade order."
s0["A2"].font=Font(name="Arial",size=10,italic=True,color="FF5D6471")
intro=[("What to do","Go to the RAG tracker tab and put R, A or G in the 'Your rating' column for each topic. That is the only column to fill in, plus Notes if you want."),
("R","I could not start this, or I would get it wrong."),
("A","I can do it but slowly, or I get some right and some wrong."),
("G","I can do this confidently and quickly."),
("Be honest rather than kind","A topic marked G gets almost no time from us. If you are torn between two, pick the lower one."),
("The early grades matter most","Grades 1 to 3 will look easy. Do not skim them. A topic you rate R there is the most useful thing you can tell me, because those marks appear on every paper."),
("Topic link","Each row links to the Maths Genie page for that topic, which has a video, questions and worked solutions if you want to check before rating."),
("Grade","The topics are grouped into grade blocks with a navy header before each one. The grade is what Maths Genie puts the topic at."),
("How long","About 119 rows, mostly one glance each. Roughly 30 minutes."),
]
r=4
for k,v in intro:
    s0.cell(r,1,k).font=Font(name="Arial",size=10,bold=True,color=NAVY)
    s0.cell(r,2,v).font=Font(name="Arial",size=10); s0.cell(r,2).alignment=wrap
    s0.row_dimensions[r].height=30; r+=1
r+=1
s0.cell(r,1,"Example of a filled row").font=Font(name="Arial",size=11,bold=True,color=NAVY); r+=1
for c,h in enumerate(["Grade","Topic","Your rating","Notes"],1): s0.cell(r,c,h).font=hdrF; s0.cell(r,c).fill=hdrFill
r+=1
for c,v in enumerate([4,"Indices","A","Fine with x and divide, never sure about power of 0"],1):
    cc=s0.cell(r,c,v); cc.font=bodyF; cc.alignment=wrap; cc.border=bd
s0.cell(r,3).fill=PatternFill("solid",fgColor=AMB)
for col,wd in zip(range(1,5),[24,30,14,44]): s0.column_dimensions[get_column_letter(col)].width=wd

ws=wb.create_sheet("RAG tracker")
cols=["Grade","Topic","Your rating","Notes","Maths Genie","PMT worksheet","QP","MS","Ans"]
ws.append(cols)
for c in ws[1]: c.font=hdrF; c.fill=hdrFill; c.alignment=Alignment(vertical="center",wrap_text=True)
ws.cell(1,1).border=Border(right=vrule)
ws.row_dimensions[1].height=30; ws.freeze_panes="C2"
import collections
bygrade=collections.OrderedDict()
for t in topics: bygrade.setdefault(t['grade'],[]).append(t)
bandF=Font(name="Arial",size=11,bold=True,color="FFC3A965")
bandFill=PatternFill("solid",fgColor=NAVY)
i=1; blocks=[]
for g,items in bygrade.items():
    i+=1
    ws.cell(i,1,f"GRADE {g}")
    ws.cell(i,2,f"{len(items)} topics")
    for col in range(1,10):
        cell=ws.cell(i,col); cell.fill=bandFill; cell.font=bandF
        cell.alignment=Alignment(vertical="center")
    ws.cell(i,1).border=Border(right=vrule)
    ws.row_dimensions[i].height=22
    start=i+1
    for t in items:
        i+=1
        ws.cell(i,1,t['grade']); ws.cell(i,2,t['title'].title())
        ws.cell(i,3,""); ws.cell(i,4,"")
        c=ws.cell(i,5,"open"); c.hyperlink=BASE+t['slug']; c.font=linkF
        sheets=PMT[t['title']]
        ws.cell(i,6,"; ".join(sheets) if sheets else "no PMT sheet")
        if sheets and sheets[0] in recs:
            rec=recs[sheets[0]]
            for lab,k,col in (("QP","QP",7),("MS","MS",8),("Ans","MA",9)):
                cc=ws.cell(i,col,lab); cc.hyperlink=rec[k]; cc.font=linkF
        for col in range(1,10):
            cell=ws.cell(i,col)
            if col not in (5,7,8,9): cell.font=bodyF
            cell.border=bd; cell.alignment=wrap if col in (4,6) else top
        ws.cell(i,1).fill=PatternFill("solid",fgColor=GBAND[t['grade']])
        ws.cell(i,1).alignment=Alignment(horizontal="center",vertical="top")
        ws.cell(i,1).font=Font(name="Arial",size=10,color="FF5D6471")
        ws.cell(i,1).border=Border(bottom=thin,right=vrule)
        ws.cell(i,2).fill=PatternFill("solid",fgColor=GBAND[t['grade']])
        ws.cell(i,3).fill=PatternFill("solid",fgColor=INP); ws.cell(i,4).fill=PatternFill("solid",fgColor=INP)
        ws.cell(i,3).alignment=Alignment(horizontal="center",vertical="center")
        ws.cell(i,3).font=Font(name="Arial",size=11,bold=True)
    blocks.append((start,i))
last=i
dv=DataValidation(type="list",formula1='"R,A,G"',allow_blank=True,showDropDown=False)
dv.error="Enter R, A or G"; dv.prompt="R = cannot do it, A = shaky, G = confident"
ws.add_data_validation(dv); [dv.add(f"C{a}:C{b}") for a,b in blocks]
for val,col in (("R",RED),("A",AMB),("G",GRN)):
    ws.conditional_formatting.add(f"C2:C{last}",CellIsRule(operator="equal",formula=[f'"{val}"'],fill=PatternFill("solid",fgColor=col)))
for col,wd in zip(range(1,10),[8,38,11,34,11,34,6,6,6]): ws.column_dimensions[get_column_letter(col)].width=wd
wb.save("Charlotte_RAG_mathsgenie.xlsx"); print("built rows:",last-1)
