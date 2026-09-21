import json
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

recs=json.load(open('recs.json'))

CORE, STR, LEAVE = "Core", "Stretch", "Leave"
C={
("Number","Fractions-Decimals-and-Percentages"):{"Fractions":CORE,"Percentages":CORE,"Recurring Decimals into Fractions":LEAVE},
("Number","Measures-and-Accuracy"):{"Approximation and Estimation":CORE,"Bounds":LEAVE,"Rounding":CORE,"Using Measures":CORE},
("Number","Structure-and-Calculation"):{"Calculating Problems":CORE,"Four Operations":CORE,"Indices":CORE,"Primes, Factors and Multiples":CORE,"Roots and Powers":CORE,"Standard Form":CORE,"Surds":LEAVE},
("Algebra","Notation-Vocabulary-and-Manipulation"):{"Algebraic Fractions":LEAVE,"Algebraic Proof":LEAVE,"Deriving Expressions":CORE,"Expanding Equations":CORE,"Expanding Triple Brackets":LEAVE,"Factorising Equations":CORE,"Forming Equations":CORE,"Functions (Composite or Inverse)":LEAVE,"Manipulation of Formulae":CORE,"Simplifying Expressions":CORE,"Substitution into Equations":CORE},
("Algebra","Sequences"):{"Sequences":CORE},
("Algebra","Graphs"):{"Circle Equations and Tangents":LEAVE,"Coordinates":CORE,"Cubic and Reciprocal Graphs":STR,"Equations of Straight Lines":CORE,"Exponential and Trigonometric Graphs":LEAVE,"Gradients of Straight lines":CORE,"Graphs of Circles":LEAVE,"Graphs of Linear Equations":CORE,"Graphs of Quadratic Equations":STR,"Interpreting Gradients":STR,"Parallel or Perpendicular Lines":STR,"Simultaneous Equations on Graphs":STR,"Translations and Reflections of Functions":LEAVE},
("Algebra","Solving-Equations-and-Inequalities"):{"Completing the square":LEAVE,"Inequalities":CORE,"Inequalities on Graphs":LEAVE,"Quadratic Inequalities":LEAVE,"Simultaneous Equations":CORE,"Solving Linear Equations":CORE,"Solving Quadratic Equations":STR,"Solving using Indices":LEAVE},
("Ratio-Proportion-and-Rates-of-Change",""):{"Algebraic Direct and Inverse Proportions":LEAVE,"Compound Interest":STR,"Compound Measures":CORE,"Compound Units":CORE,"Direct and Inverse Proportion":STR,"Percentage Increase or Decrease":CORE,"Proportion":CORE,"Ratio":CORE,"Scale Factors":CORE,"Speed":CORE,"Units of Measure":CORE},
("Geometry-and-Measures","Mensuration-and-Calculation"):{"Area":CORE,"Area of Shaded Region":CORE,"Area or Perimeter Problem":CORE,"Bearings":CORE,"Compound Area":CORE,"Perimeter":CORE,"Pythagoras and trig (3D)":LEAVE,"Pythagoras' Theorem":CORE,"Sine Rule, Cosine Rule and Area":LEAVE,"Trig Ratios and Exact Values":CORE,"Volume and Surface Area":CORE},
("Geometry-and-Measures","Vectors"):{"Manipulating Vectors":LEAVE,"Translations as 2D vectors":STR,"Vector Proof":LEAVE},
("Geometry-and-Measures","Properties-and-Constructions"):{"2D and 3D Shapes":CORE,"Circle Theorems":LEAVE,"Congruence and Similarity":STR,"Constructions":CORE,"Maps and Scale Drawings":CORE,"Properties of Angles":CORE,"Properties of Circles":CORE,"Properties of Polygons":CORE,"Sectors, Segments and Arcs":STR,"Similar (2D or 3D)":STR,"Transformations of Shapes":CORE,"Triangles":CORE,"Vocabulary and Notation":CORE},
("Probability",""):{"Conditional Probability":STR,"Probability Equations":CORE,"Probability of Events":CORE,"Tree Diagrams":CORE,"Venn Diagrams":CORE},
("Statistics",""):{"Cumulative Frequency Graphs":STR,"Frequency Tables":CORE,"Histograms":LEAVE,"Interpreting Data":CORE,"Mean, Median, Mode, Range":CORE},
}
WEEK={
1:[("Number","Structure-and-Calculation",n) for n in ["Calculating Problems","Four Operations","Indices","Primes, Factors and Multiples","Roots and Powers","Standard Form"]]
  +[("Number","Fractions-Decimals-and-Percentages",n) for n in ["Fractions","Percentages"]],
2:[("Number","Measures-and-Accuracy",n) for n in ["Approximation and Estimation","Rounding","Using Measures"]]
  +[("Ratio-Proportion-and-Rates-of-Change","",n) for n in ["Compound Measures","Compound Units","Percentage Increase or Decrease","Proportion","Ratio","Scale Factors","Speed","Units of Measure"]],
3:[("Algebra","Notation-Vocabulary-and-Manipulation",n) for n in ["Deriving Expressions","Expanding Equations","Factorising Equations","Forming Equations","Manipulation of Formulae","Simplifying Expressions","Substitution into Equations"]]
  +[("Algebra","Solving-Equations-and-Inequalities",n) for n in ["Inequalities","Simultaneous Equations","Solving Linear Equations"]],
4:[("Geometry-and-Measures","Mensuration-and-Calculation",n) for n in ["Area","Area of Shaded Region","Area or Perimeter Problem","Bearings","Compound Area","Perimeter","Pythagoras' Theorem","Trig Ratios and Exact Values","Volume and Surface Area"]],
5:[("Geometry-and-Measures","Properties-and-Constructions",n) for n in ["2D and 3D Shapes","Constructions","Maps and Scale Drawings","Properties of Angles","Properties of Circles","Properties of Polygons","Transformations of Shapes","Triangles","Vocabulary and Notation"]],
6:[("Algebra","Sequences","Sequences")]
  +[("Algebra","Graphs",n) for n in ["Coordinates","Equations of Straight Lines","Gradients of Straight lines","Graphs of Linear Equations"]]
  +[("Probability","",n) for n in ["Conditional Probability","Probability Equations","Probability of Events","Tree Diagrams","Venn Diagrams"] if C[("Probability","")][n]==CORE]
  +[("Statistics","",n) for n in ["Frequency Tables","Interpreting Data","Mean, Median, Mode, Range"]],
}
DATES={1:"21 to 27 Sep",2:"28 Sep to 4 Oct",3:"5 to 11 Oct",4:"12 to 18 Oct",5:"19 to 25 Oct",6:"26 Oct to 1 Nov"}
THEME={1:"Number: structure and calculation",2:"Number: accuracy, then ratio",3:"Algebra",
       4:"Geometry: mensuration",5:"Geometry: properties",6:"Graphs, probability and statistics"}
wk={}
for w,items in WEEK.items():
    for it in items: wk[it]=w

NAVY="FF162947"; GOLD="FFC3A965"; CREAM="FFF6F4EF"; TINT="FFEFEBE1"
hdrF=Font(name="Arial",size=10,bold=True,color="FFF6F4EF")
hdrFill=PatternFill("solid",fgColor=NAVY)
bodyF=Font(name="Arial",size=10)
linkF=Font(name="Arial",size=10,color="FF0563C1",underline="single")
thin=Side(style="thin",color="FFD8D3C6"); bd=Border(bottom=thin)

wb=Workbook(); ws=wb.active; ws.title="Session plan"
cols=["Week","Dates","Focus","Folder","Sub-folder","Worksheet","Priority","In session","At home","QP","MS","Answers","Done"]
ws.append(cols)
for i,c in enumerate(ws[1],1): c.font=hdrF; c.fill=hdrFill; c.alignment=Alignment(vertical="center")
ws.row_dimensions[1].height=22
ws.freeze_panes="A2"

def prio(r): return C[(r["topic"],r["sub"])][r["name"]]
rows=sorted(recs,key=lambda r:(wk.get((r["topic"],r["sub"],r["name"]),99),
                               {"Core":0,"Stretch":1,"Leave":2}[prio(r)], r["topic"], r["sub"], r["name"]))
rn=1
for r in rows:
    p=prio(r); key=(r["topic"],r["sub"],r["name"]); w=wk.get(key)
    if p==LEAVE: continue
    rn+=1
    wlabel=w if w else "Spare"
    ws.cell(rn,1,wlabel); ws.cell(rn,2,DATES.get(w,"if ahead")); ws.cell(rn,3,THEME.get(w,"Stretch topics"))
    ws.cell(rn,4,r["topic"].replace("-"," ")); ws.cell(rn,5,(r["sub"] or "-").replace("-"," "))
    ws.cell(rn,6,r["name"]); ws.cell(rn,7,p)
    ws.cell(rn,8,2 if p==CORE else 0); ws.cell(rn,9,4 if p==CORE else 6)
    for lab,k,col in (("QP","QP",10),("MS","MS",11),("Ans","MA",12)):
        c=ws.cell(rn,col,lab); c.hyperlink=r[k]; c.font=linkF
    ws.cell(rn,13,"")
    for col in range(1,14):
        c=ws.cell(rn,col)
        if col not in (10,11,12): c.font=bodyF
        c.border=bd
        if p==STR: c.fill=PatternFill("solid",fgColor=TINT)
last=rn
for col,wd in zip(range(1,14),[7,15,32,26,30,36,10,11,9,6,6,7,8]):
    ws.column_dimensions[get_column_letter(col)].width=wd

ws2=wb.create_sheet("Not covered")
ws2.append(["Folder","Sub-folder","Worksheet","Why it is left out"])
for i,c in enumerate(ws2[1],1): c.font=hdrF; c.fill=hdrFill
WHY={"Recurring Decimals into Fractions":"Grade 7","Bounds":"Grade 7, fiddly","Surds":"Grade 7",
"Algebraic Fractions":"Grade 7","Algebraic Proof":"Grade 8","Expanding Triple Brackets":"Grade 7",
"Functions (Composite or Inverse)":"Grade 7","Circle Equations and Tangents":"Grade 8",
"Exponential and Trigonometric Graphs":"Grade 8","Graphs of Circles":"Grade 7",
"Translations and Reflections of Functions":"Grade 8","Completing the square":"Grade 7",
"Inequalities on Graphs":"Grade 7","Quadratic Inequalities":"Grade 8","Solving using Indices":"Grade 7",
"Algebraic Direct and Inverse Proportions":"Grade 7","Pythagoras and trig (3D)":"Grade 7",
"Sine Rule, Cosine Rule and Area":"Grade 6 to 7, on the formula sheet but multi-step",
"Manipulating Vectors":"Grade 7","Vector Proof":"Grade 8","Circle Theorems":"Grade 6 to 7, proof heavy",
"Histograms":"Grade 7, unequal class widths"}
r2=1
for r in rows:
    if prio(r)!=LEAVE: continue
    r2+=1
    ws2.cell(r2,1,r["topic"].replace("-"," ")); ws2.cell(r2,2,(r["sub"] or "-").replace("-"," "))
    ws2.cell(r2,3,r["name"]); ws2.cell(r2,4,WHY.get(r["name"],"Above the target band"))
    for col in range(1,5): ws2.cell(r2,col).font=bodyF; ws2.cell(r2,col).border=bd
for col,wd in zip(range(1,5),[26,30,38,40]): ws2.column_dimensions[get_column_letter(col)].width=wd
ws2.freeze_panes="A2"

ws3=wb.create_sheet("Summary",0)
ws3["A1"]="Charlotte: PMT topic question plan"; ws3["A1"].font=Font(name="Arial",size=14,bold=True,color=NAVY)
ws3["A2"]="Edexcel IGCSE Maths A (4MA1) Higher. Source: PMT Questions by Topic."
ws3["A2"].font=Font(name="Arial",size=10,italic=True,color="FF5D6471")
hdr=["Week","Dates","Focus","Worksheets","Questions in session","Questions at home"]
ws3.append([]); ws3.append(hdr)
for c in ws3[4]: c.font=hdrF; c.fill=hdrFill
rr=4
for w in range(1,7):
    rr+=1
    ws3.cell(rr,1,w); ws3.cell(rr,2,DATES[w]); ws3.cell(rr,3,THEME[w])
    ws3.cell(rr,4,f"=COUNTIFS('Session plan'!$A$2:$A${last},$A{rr})")
    ws3.cell(rr,5,f"=SUMIFS('Session plan'!$H$2:$H${last},'Session plan'!$A$2:$A${last},$A{rr})")
    ws3.cell(rr,6,f"=SUMIFS('Session plan'!$I$2:$I${last},'Session plan'!$A$2:$A${last},$A{rr})")
    for col in range(1,7): ws3.cell(rr,col).font=bodyF; ws3.cell(rr,col).border=bd
rr+=1
ws3.cell(rr,1,"Spare"); ws3.cell(rr,2,"if ahead"); ws3.cell(rr,3,"Stretch topics, grade 6 single step")
ws3.cell(rr,4,f"=COUNTIFS('Session plan'!$A$2:$A${last},\"Spare\")")
ws3.cell(rr,5,f"=SUMIFS('Session plan'!$H$2:$H${last},'Session plan'!$A$2:$A${last},\"Spare\")")
ws3.cell(rr,6,f"=SUMIFS('Session plan'!$I$2:$I${last},'Session plan'!$A$2:$A${last},\"Spare\")")
for col in range(1,7): ws3.cell(rr,col).font=bodyF; ws3.cell(rr,col).border=bd
rr+=1
ws3.cell(rr,3,"Total"); ws3.cell(rr,4,f"=SUM(D5:D{rr-1})")
ws3.cell(rr,5,f"=SUM(E5:E{rr-1})"); ws3.cell(rr,6,f"=SUM(F5:F{rr-1})")
for col in range(3,7): ws3.cell(rr,col).font=Font(name="Arial",size=10,bold=True); ws3.cell(rr,col).fill=PatternFill("solid",fgColor=TINT)
note=rr+2
ws3.cell(note,1,"How to use it")
ws3.cell(note,1).font=Font(name="Arial",size=11,bold=True,color=NAVY)
for i,t in enumerate([
 "Each worksheet: 2 questions in the session (one modelled, one done by Charlotte), 4 at home. About half the sheet.",
 "Median PMT Higher worksheet is 13 pages, about 13 questions, about 45 marks. Six questions is roughly 20 marks.",
 "She marks her own at home against the MS column. The Answers column is worked solutions, for when the MS is not enough.",
 "Stretch rows (shaded) are grade 6 single step topics. Do them only once the Core rows for that week are done.",
 "The Not covered tab lists the 22 worksheets deliberately left out, with the reason for each.",
 "Tick the Done column on the Session plan tab."],start=1):
    ws3.cell(note+i,1,t); ws3.cell(note+i,1).font=Font(name="Arial",size=10,color="FF5D6471")
for col,wd in zip(range(1,7),[10,16,44,12,20,18]): ws3.column_dimensions[get_column_letter(col)].width=wd

wb.save("Charlotte_PMT_plan.xlsx"); print("saved, data rows:",last-1)
