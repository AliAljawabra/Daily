import json
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
wb=load_workbook("Charlotte_RAG_mathsgenie.xlsx")
ws=wb["RAG tracker"]; last=ws.max_row
NAVY="FF162947"; TINT="FFEFEBE1"; RED="FFF4CCCC"; AMB="FFFCE5CD"; GRN="FFD9EAD3"
hdrF=Font(name="Arial",size=10,bold=True,color="FFF6F4EF"); hdrFill=PatternFill("solid",fgColor=NAVY)
bodyF=Font(name="Arial",size=10); thin=Side(style="thin",color="FFD8D3C6"); bd=Border(bottom=thin)
wrap=Alignment(wrap_text=True,vertical="top")

# spec ref -> Maths Genie topics that cover it
COVER={
"1.1":["Addition And Subtraction","Multiplication And Division","Place Value","Negative Numbers","Bidmas","Factors And Multiples"],
"1.2":["Writing Simplifying And Ordering Fractions","Fractions Of An Amount","Fractions"],
"1.3":["Place Value","Fractions Decimals And Percentages","Recurring Decimals To Fractions"],
"1.4":["Powers And Roots","Indices","Prime Factors Hcf And Lcm","Fractional And Negative Indices","Surds"],
"1.5":["Venn Diagrams"],
"1.6":["Percentages","Percentage Change","Reverse Percentages","Compound Interest And Depreciation","Fractions Decimals And Percentages"],
"1.7":["Writing And Simplifying Ratio","Ratio","Proportion","Best Buy Questions","Scale Drawings"],
"1.8":["Rounding","Estimating","Bounds"],
"1.9":["Standard Form"],
"1.10":["Conversions And Units","Time","Calculation Problems","Exchange Rates"],
"1.11":["Using A Calculator"],
"2.1":["Simplifying Algebra","Indices","Fractional And Negative Indices"],
"2.2":["Simplifying Algebra","Writing An Expression","Expanding And Factorising","Expanding And Factorising Quadratics","Expanding Triple Brackets","Factorising Harder Quadratics","Algebraic Fractions","Completing The Square","Proof"],
"2.3":["Substitution","Changing The Subject Of A Formula","Rearranging Harder Formulae","Writing An Expression"],
"2.4":["Solving One Step Equations","Solving Equations","Forming And Solving Equations"],
"2.5":["Direct And Inverse Proportion"],
"2.6":["Simultaneous Equations","Solving Simultaneous Equations Graphically","Quadratic Simultaneous Equations"],
"2.7":["Solving Quadratics","Quadratic Formula","Expanding And Factorising Quadratics"],
"2.8":["Inequalities","Inequalities On Graphs","Quadratic Inequalities"],
"3.1":["Sequences Nth Term","Sequences Higher"],
"3.2":["Function Machines","Inverse And Composite Functions"],
"3.3":["Coordinates","Drawing Graphs","Real Life And Distance Time Graphs","Drawing Quadratic Graphs","Drawing Other Graphs Cubic Reciprocal","Gradient Of A Line","Equation Of A Line","Parallel And Perpendicular Lines","Trigonometric And Exponential Graphs","Transforming Graphs Y F X"],
"3.4":["Differentiation"],
"4.1":["Angles","Angles In Parallel Lines"],
"4.2":["Angles In Polygons","Angles"],
"4.3":[],
"4.4":["Time","Conversions And Units","Bearings","Speed And Density","Best Buy Questions"],
"4.5":["Construction"],
"4.6":["Area And Circumference Of Circles","Circle Theorems"],
"4.7":["Angles","Angles In Parallel Lines","Angles In Polygons"],
"4.8":["Pythagoras","Sohcahtoa Trigonometry","The Sine Rule","The Cosine Rule","Finding The Area Of Any Triangle","3D Pythagoras And Trigonometry"],
"4.9":["Area And Perimeter","Area Of Compound Shapes","Area And Circumference Of Circles","Sector Areas And Arc Lengths"],
"4.10":["Surface Area","Volume Of A Prism","Cylinders","Spheres And Cones"],
"4.11":["Similar Shapes Lengths","Similar Shapes Area And Volume"],
"5.1":["Vectors","The Magnitude Of A Vector","Vectors Proof Questions"],
"5.2":["Transformations"],
"6.1":["Pictograms","Bar Charts","Pie Charts","Frequency Polygons","Cumulative Frequency","Histograms","Data"],
"6.2":["Averages","Averages From Frequency Tables","Data","Cumulative Frequency"],
"6.3":["Probability","Frequency Trees","Venn Diagrams","Probability Trees","Conditional Probability","Probability Equation Questions","Systematic Listing"],
}
TITLE={"1.1":"Integers","1.2":"Fractions","1.3":"Decimals","1.4":"Powers and roots","1.5":"Set language and notation",
"1.6":"Percentages","1.7":"Ratio and proportion","1.8":"Degree of accuracy","1.9":"Standard form",
"1.10":"Applying number","1.11":"Electronic calculators","2.1":"Use of symbols","2.2":"Algebraic manipulation",
"2.3":"Expressions and formulae","2.4":"Linear equations","2.5":"Proportion","2.6":"Simultaneous linear equations",
"2.7":"Quadratic equations","2.8":"Inequalities","3.1":"Sequences","3.2":"Function notation","3.3":"Graphs",
"3.4":"Calculus","4.1":"Angles, lines and triangles","4.2":"Polygons","4.3":"Symmetry","4.4":"Measures",
"4.5":"Construction","4.6":"Circle properties","4.7":"Geometrical reasoning","4.8":"Trigonometry and Pythagoras",
"4.9":"Mensuration","4.10":"3D shapes and volume","4.11":"Similarity","5.1":"Vectors",
"5.2":"Transformation geometry","6.1":"Graphical representation of data","6.2":"Statistical measures","6.3":"Probability"}
present={str(ws.cell(r,3).value) for r in range(2,last+1)}
gaps=[]; bad=[]
for ref,lst in COVER.items():
    for t in lst:
        if t not in present: bad.append((ref,t))
    if not lst: gaps.append(ref)
print("mapped topic names not found in tracker:",bad or "none")
print("spec refs with NO Maths Genie topic:",gaps)

s3=wb.create_sheet("Summary",0)
s3["A1"]="Summary"; s3["A1"].font=Font(name="Arial",size=16,bold=True,color=NAVY)
s3["A2"]="Fills in automatically once the RAG tracker is completed."
s3["A2"].font=Font(name="Arial",size=10,italic=True,color="FF5D6471")
s3.append([]); s3.append(["Rating","Topics in scope","What we do","Questions each","Questions total"])
for c in s3[4]: c.font=hdrF; c.fill=hdrFill
rr=4
for val,act,q in [("R","Full worksheet, taught first",13),("A","Work until 3 right in a row",6),("G","2 question spot check",2)]:
    rr+=1
    s3.cell(rr,1,val); s3.cell(rr,2,f"=COUNTIFS('RAG tracker'!$E$2:$E${last},$A{rr},'RAG tracker'!$D$2:$D${last},\"<>Not this time\")")
    s3.cell(rr,3,act); s3.cell(rr,4,q); s3.cell(rr,5,f"=$B{rr}*$D{rr}")
    for c in range(1,6): s3.cell(rr,c).font=bodyF; s3.cell(rr,c).border=bd
    s3.cell(rr,1).fill=PatternFill("solid",fgColor={"R":RED,"A":AMB,"G":GRN}[val])
rr+=1
s3.cell(rr,1,"Not yet rated"); s3.cell(rr,2,f"=COUNTIFS('RAG tracker'!$E$2:$E${last},\"\")")
s3.cell(rr,3,"Counts every row, including the ones we are not scheduling")
for c in range(1,6): s3.cell(rr,c).font=bodyF; s3.cell(rr,c).border=bd
rr+=1
s3.cell(rr,3,"Total questions"); s3.cell(rr,5,f"=SUM(E5:E7)")
for c in (3,5): s3.cell(rr,c).font=Font(name="Arial",size=10,bold=True); s3.cell(rr,c).fill=PatternFill("solid",fgColor=TINT)
rr+=1; s3.cell(rr,3,"Hours at about 2.5 min a question"); s3.cell(rr,5,f"=ROUND($E{rr-1}*2.5/60,1)")
rr+=1; s3.cell(rr,3,"Hours per week over six weeks"); s3.cell(rr,5,f"=ROUND($E{rr-1}/6,1)")
for r2 in (rr-1,rr):
    s3.cell(r2,3).font=bodyF; s3.cell(r2,5).font=bodyF
rr+=2
s3.cell(rr,1,"By grade").font=Font(name="Arial",size=11,bold=True,color=NAVY); rr+=1
for c,h in enumerate(["Grade","Topics","In our plan","Red","Amber","Green"],1): s3.cell(rr,c,h).font=hdrF; s3.cell(rr,c).fill=hdrFill
gstart=rr+1
for g in range(1,9):
    rr+=1
    s3.cell(rr,1,g)
    s3.cell(rr,2,f"=COUNTIFS('RAG tracker'!$A$2:$A${last},$A{rr})")
    s3.cell(rr,3,"Core" if g<=5 else ("Stretch" if g==6 else "Not this time"))
    for c,val in ((4,"R"),(5,"A"),(6,"G")):
        s3.cell(rr,c,f"=COUNTIFS('RAG tracker'!$A$2:$A${last},$A{rr},'RAG tracker'!$E$2:$E${last},\"{val}\")")
    for c in range(1,7): s3.cell(rr,c).font=bodyF; s3.cell(rr,c).border=bd
rr+=1
s3.cell(rr,1,"Total"); s3.cell(rr,2,f"=SUM(B{gstart}:B{rr-1})")
for c in (4,5,6): s3.cell(rr,c,f"=SUM({get_column_letter(c)}{gstart}:{get_column_letter(c)}{rr-1})")
for c in range(1,7): s3.cell(rr,c).font=Font(name="Arial",size=10,bold=True); s3.cell(rr,c).fill=PatternFill("solid",fgColor=TINT)
for col,wd in zip(range(1,7),[18,12,38,16,16,16]): s3.column_dimensions[get_column_letter(col)].width=wd

s4=wb.create_sheet("Spec check")
s4["A1"]="Cross-check against the Pearson 4MA1 specification"
s4["A1"].font=Font(name="Arial",size=14,bold=True,color=NAVY)
s4["A2"]="Every subsection of the specification, and the Maths Genie topics that cover it. Built so nothing is lost by using Maths Genie as the spine."
s4["A2"].font=Font(name="Arial",size=10,italic=True,color="FF5D6471")
s4.append([]); s4.append(["Spec ref","Specification topic","Covered by","Status"])
for c in s4[4]: c.font=hdrF; c.fill=hdrFill
r4=4
for ref in sorted(COVER,key=lambda r:(int(r.split('.')[0]),int(r.split('.')[1]))):
    r4+=1
    s4.cell(r4,1,ref); s4.cell(r4,2,TITLE[ref])
    s4.cell(r4,3,", ".join(COVER[ref]) if COVER[ref] else "NOTHING")
    s4.cell(r4,4,"Covered" if COVER[ref] else "GAP")
    for c in range(1,5): s4.cell(r4,c).font=bodyF; s4.cell(r4,c).border=bd; s4.cell(r4,c).alignment=wrap
    if not COVER[ref]:
        for c in range(1,5): s4.cell(r4,c).fill=PatternFill("solid",fgColor=RED)
    s4.row_dimensions[r4].height=28
r4+=2
s4.cell(r4,1,"Notes").font=Font(name="Arial",size=11,bold=True,color=NAVY)
for i,t in enumerate([
 "4.3 Symmetry has no Maths Genie topic. Lines of symmetry and order of rotational symmetry are on the specification. Cover it inside Transformations.",
 "Congruence (4.2 F and G) has no topic of its own. It sits inside Similar Shapes Lengths and Transformations.",
 "Set notation beyond Venn diagrams (union, intersection, complement, n(A), subsets) sits only inside Venn Diagrams. Check she has seen the symbols.",
 "Everything else on the specification maps to at least one Maths Genie topic.",
 "Grade 7 and above rows say 'Not scheduled' whatever the rating, and are excluded from the question totals above.",
 "Grades shown are Maths Genie's estimates, not Pearson's. Boundaries move each series."],start=1):
    s4.cell(r4+i,1,t).font=Font(name="Arial",size=10,color="FF5D6471")
for col,wd in zip(range(1,5),[10,34,70,12]): s4.column_dimensions[get_column_letter(col)].width=wd
wb.save("Charlotte_RAG_mathsgenie.xlsx"); print("saved")
