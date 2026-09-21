const pptxgen = require("pptxgenjs");

const CREAM="F6F4EF", NAVY="162947", GOLD="C3A965", BODY="5D6471",
      CARD="FFFFFF", LINE="E3DFD5", TINT="EFEBE1", NAVYCARD="22355A",
      ONNAVY="E8E4DA", ONNAVYMUTE="A8B2C2";
const SERIF="Cambria", SANS="Arial";
const M=0.75, W=13.333, H=7.5, CW=W-2*M;

const p=new pptxgen();
p.layout="LAYOUT_WIDE";
p.author="Ali Tutors";
p.title="November Maths Plan";

function head(s,eyebrow,title,dark,titleSize){
  s.background={color: dark?NAVY:CREAM};
  s.addText(eyebrow,{x:M,y:0.46,w:CW,h:0.26,isTextBox:true,margin:0,
    fontFace:SANS,fontSize:10.5,bold:true,color:GOLD,charSpacing:2.6});
  s.addText(title,{x:M,y:0.76,w:CW,h:0.72,isTextBox:true,margin:0,
    fontFace:SERIF,fontSize:titleSize||33,color:dark?CREAM:NAVY,valign:"top"});
}
function card(s,x,y,w,h,fill,border){
  s.addShape(p.ShapeType.roundRect,{x,y,w,h,rectRadius:0.04,fill:{color:fill},
    line:border?{color:border,width:0.75}:{type:"none"}});
}
function badge(s,x,y,txt,fill,col,d){
  d=d||0.44;
  s.addShape(p.ShapeType.ellipse,{x,y,w:d,h:d,fill:{color:fill},line:{type:"none"}});
  s.addText(txt,{x,y,w:d,h:d,isTextBox:true,margin:0,align:"center",valign:"middle",
    fontFace:SERIF,fontSize:15,bold:true,color:col});
}
function bullets(s,items,x,y,w,size,color,gap){
  s.addText(items.map((t,i)=>({text:t,options:{bullet:{indent:14},breakLine:i<items.length-1}})),
    {x,y,w,h:items.length*(gap||0.3),isTextBox:true,margin:0,fontFace:SANS,
     fontSize:size,color:color,lineSpacing:size*1.22,paraSpaceAfter:5});
}
function kv(s,x,y,w,label,value,vcolor){
  s.addText(label,{x,y,w,h:0.2,isTextBox:true,margin:0,fontFace:SANS,fontSize:8.5,
    bold:true,color:"9AA0A8",charSpacing:1.8});
  s.addText(value,{x,y:y+0.2,w,h:0.62,isTextBox:true,margin:0,valign:"top",fontFace:SANS,
    fontSize:11,bold:true,color:vcolor||NAVY,lineSpacing:14.5});
}
function rule(s,x,y,w,c){
  s.addShape(p.ShapeType.line,{x,y,w,h:0,line:{color:c||LINE,width:0.75}});
}

/* ---------------------------------------------------------- 1 TITLE */
let s=p.addSlide(); s.background={color:NAVY};
s.addShape(p.ShapeType.ellipse,{x:9.55,y:-1.7,w:5.2,h:5.2,fill:{color:"1C3255"},line:{type:"none"}});
s.addShape(p.ShapeType.ellipse,{x:11.35,y:5.15,w:3.1,h:3.1,fill:{color:GOLD},line:{type:"none"}});
s.addText("ALI TUTORS",{x:M,y:0.85,w:6,h:0.3,isTextBox:true,margin:0,fontFace:SANS,
  fontSize:11,bold:true,color:GOLD,charSpacing:3});
s.addText("November\nMaths Plan",{x:M,y:1.5,w:8,h:2.2,isTextBox:true,margin:0,
  fontFace:SERIF,fontSize:58,color:CREAM,lineSpacing:62});
s.addText("Edexcel IGCSE Mathematics A (4MA1)  ·  Higher Tier",
  {x:M,y:3.95,w:8,h:0.36,isTextBox:true,margin:0,fontFace:SANS,fontSize:15,color:ONNAVY});
s.addShape(p.ShapeType.roundRect,{x:M,y:4.62,w:2.92,h:0.56,rectRadius:0.28,
  fill:{type:"none"},line:{color:GOLD,width:1}});
s.addText("SIX WEEKS TO PAPER 1",{x:M,y:4.62,w:2.92,h:0.56,isTextBox:true,margin:0,
  align:"center",valign:"middle",fontFace:SANS,fontSize:10,bold:true,color:GOLD,charSpacing:1.6});
s.addText("For Charlotte and her parents  ·  21 September 2026",
  {x:M,y:6.35,w:7,h:0.3,isTextBox:true,margin:0,fontFace:SANS,fontSize:11,color:ONNAVYMUTE});

/* ---------------------------------------------------------- 2 EXAMS */
s=p.addSlide(); head(s,"THE EXAMS","Two papers, two days apart");
card(s,M,1.85,3.55,3.1,NAVY);
s.addText("44",{x:M,y:2.05,w:3.55,h:1.25,isTextBox:true,margin:0,align:"center",
  fontFace:SERIF,fontSize:76,color:GOLD});
s.addText("days until Paper 1",{x:M,y:3.3,w:3.55,h:0.3,isTextBox:true,margin:0,
  align:"center",fontFace:SANS,fontSize:13,bold:true,color:CREAM});
s.addText("Six teaching weeks\nand two days",{x:M,y:3.72,w:3.55,h:0.7,isTextBox:true,margin:0,
  align:"center",fontFace:SANS,fontSize:11,color:ONNAVYMUTE,lineSpacing:16});

[["Wed 4 Nov","Paper 1H","Morning  ·  2 hours  ·  100 marks  ·  calculator"],
 ["Fri 6 Nov","Paper 2H","Morning  ·  2 hours  ·  100 marks  ·  calculator"]].forEach((pp,i)=>{
  const y=1.85+i*1.62;
  card(s,4.75,y,7.83,1.42,CARD,LINE);
  s.addText(pp[0],{x:5.1,y:y+0.24,w:2.1,h:0.36,isTextBox:true,margin:0,
    fontFace:SERIF,fontSize:20,color:GOLD});
  s.addText(pp[1],{x:7.1,y:y+0.28,w:2.2,h:0.32,isTextBox:true,margin:0,
    fontFace:SANS,fontSize:15,bold:true,color:NAVY});
  s.addText(pp[2],{x:5.1,y:y+0.78,w:7.1,h:0.3,isTextBox:true,margin:0,
    fontFace:SANS,fontSize:11.5,color:BODY});
});
card(s,M,5.25,11.83,1.45,TINT);
s.addText("Both papers allow a calculator, and both cover the whole specification.",
  {x:1.05,y:5.5,w:11.2,h:0.3,isTextBox:true,margin:0,fontFace:SANS,fontSize:13,bold:true,color:NAVY});
s.addText("Calculator technique is covered in the next session and checked before every timed piece of work. A topic that appears on Paper 1 is likely to appear again on Paper 2.",
  {x:1.05,y:5.86,w:11.2,h:0.6,isTextBox:true,margin:0,valign:"top",fontFace:SANS,fontSize:11.5,
   color:BODY,lineSpacing:16});

/* ---------------------------------------------------------- 3 TARGET */
s=p.addSlide(); head(s,"THE TARGET","The number we are working to");
card(s,M,1.85,3.9,4.15,NAVY);
s.addText("65",{x:M,y:2.15,w:3.9,h:1.4,isTextBox:true,margin:0,align:"center",
  fontFace:SERIF,fontSize:86,color:GOLD});
s.addText("marks out of 200",{x:M,y:3.6,w:3.9,h:0.3,isTextBox:true,margin:0,align:"center",
  fontFace:SANS,fontSize:14,bold:true,color:CREAM});
s.addText("The grade 5 boundary on Higher tier in November 2025, just under a third of the paper. Boundaries shift each series, so we treat this as a guide.",
  {x:1.1,y:4.15,w:3.2,h:1.5,isTextBox:true,margin:0,valign:"top",fontFace:SANS,fontSize:11.5,
   color:ONNAVYMUTE,lineSpacing:16.5});

const tx=5.05, tw=7.53, cw=[3.13,2.2,2.2];
s.addShape(p.ShapeType.rect,{x:tx,y:1.85,w:tw,h:0.46,fill:{color:NAVY},line:{type:"none"}});
["Grade","Marks needed","Share of total"].forEach((hd,i)=>{
  const cx=tx+cw.slice(0,i).reduce((a,b)=>a+b,0);
  s.addText(hd,{x:cx+0.22,y:1.85,w:cw[i]-0.44,h:0.46,isTextBox:true,margin:0,valign:"middle",
    align:i?"center":"left",fontFace:SANS,fontSize:11.5,bold:true,color:CREAM,charSpacing:0.6});
});
[["Grade 6","86 / 200","43%",false],["Grade 5","65 / 200","33%",true],
 ["Grade 4","45 / 200","23%",false]].forEach((r,ri)=>{
  const y=2.31+ri*0.46;
  s.addShape(p.ShapeType.rect,{x:tx,y,w:tw,h:0.46,fill:{color:r[3]?TINT:CARD},
    line:{color:LINE,width:0.6}});
  r.slice(0,3).forEach((cell,i)=>{
    const cx=tx+cw.slice(0,i).reduce((a,b)=>a+b,0);
    s.addText(cell,{x:cx+0.22,y,w:cw[i]-0.44,h:0.46,isTextBox:true,margin:0,valign:"middle",
      align:i?"center":"left",fontFace:SANS,fontSize:12.5,bold:r[3],color:r[3]?NAVY:BODY});
  });
});
card(s,5.05,4.02,7.53,1.98,CARD,LINE);
s.addText("Why we work towards 80",{x:5.4,y:4.24,w:6.9,h:0.34,isTextBox:true,margin:0,
  valign:"top",fontFace:SERIF,fontSize:19,color:NAVY});
s.addText("Boundaries shift, so aiming at last year's number exactly leaves no room. The larger factor is how many marks Charlotte is taught to attempt in the first place, which the next slide sets out.",
  {x:5.4,y:4.68,w:6.9,h:1.15,isTextBox:true,margin:0,valign:"top",fontFace:SANS,fontSize:12,
   color:BODY,lineSpacing:17});

/* ---------------------------------------------------------- 4 WHERE MARKS ARE */
s=p.addSlide(); head(s,"WHERE THE MARKS ARE","Number and algebra is 60% of the qualification");
s.addChart(p.ChartType.bar,[{name:"Marks of 200",labels:["Handling data","Shape, space and measure","Number and algebra"],values:[30,50,120]}],
 {x:0.55,y:1.75,w:6.3,h:2.9,barDir:"bar",chartColors:["9AA6B8",GOLD,NAVY],varyColors:true,
  showValue:true,dataLabelPosition:"outEnd",dataLabelColor:NAVY,dataLabelFontFace:SANS,
  dataLabelFontSize:12,dataLabelFontBold:true,showLegend:false,showTitle:false,
  catAxisLabelColor:NAVY,catAxisLabelFontFace:SANS,catAxisLabelFontSize:11.5,
  valAxisHidden:true,valGridLine:{style:"none"},catGridLine:{style:"none"},
  barGapWidthPct:55,valAxisMaxVal:140,chartArea:{fill:{color:CREAM}},plotArea:{fill:{color:CREAM}}});

[["The largest section is also the weakest","Charlotte's gaps are concentrated in number and algebra. Work there pays back across 120 marks, so the first three weeks stay on it."],
 ["Handling data does not depend on algebra","Averages, tables, probability and Venn diagrams are 30 marks that the algebra gaps do not block. They come in week 4."]].forEach((n,i)=>{
  const y=1.8+i*1.5;
  card(s,7.1,y,5.48,1.32,CARD,LINE);
  s.addText(n[0],{x:7.42,y:y+0.18,w:4.85,h:0.28,isTextBox:true,margin:0,
    fontFace:SANS,fontSize:12.5,bold:true,color:NAVY});
  s.addText(n[1],{x:7.42,y:y+0.5,w:4.85,h:0.7,isTextBox:true,margin:0,valign:"top",
    fontFace:SANS,fontSize:11,color:BODY,lineSpacing:15});
});
card(s,M,4.95,11.83,1.75,NAVY);
s.addText("How many marks we cover",{x:1.1,y:5.15,w:11.1,h:0.32,isTextBox:true,
  margin:0,fontFace:SERIF,fontSize:19,color:GOLD});
[["about 80","marks are pitched at grades 4 and 5","Covering only this band means converting 65 of 80, which leaves room to drop 15 marks across the two papers."],
 ["about 105","marks once single-step grade 6 topics are added","The target to pass stays at 65, with room to drop 40 marks."]].forEach((q,i)=>{
  const x=1.1+i*5.6;
  s.addText(q[0],{x,y:5.53,w:1.75,h:0.4,isTextBox:true,margin:0,valign:"top",fontFace:SERIF,fontSize:23,color:CREAM});
  s.addText(q[1],{x:x+1.82,y:5.6,w:3.45,h:0.34,isTextBox:true,margin:0,valign:"top",fontFace:SANS,
    fontSize:11,bold:true,color:ONNAVY,lineSpacing:14});
  s.addText(q[2],{x,y:6.0,w:5.3,h:0.6,isTextBox:true,margin:0,valign:"top",fontFace:SANS,fontSize:10.5,
    color:ONNAVYMUTE,lineSpacing:14.5});
});

/* ---------------------------------------------------------- 5 ROUTE */
s=p.addSlide(); head(s,"THE ROUTE","The six weeks");
const steps=[["1","21 to 27 Sep","Baseline"],["2","28 Sep to 4 Oct","Number"],["3","5 to 11 Oct","Algebra"],
             ["4","12 to 18 Oct","Ratio and data"],["5","19 to 25 Oct","Shape"],["6","26 Oct to 1 Nov","Papers"],
             ["★","4 and 6 Nov","Exams"]];
const n=steps.length, x0=0.95, span=11.45, gap=span/(n-1);
s.addShape(p.ShapeType.line,{x:x0+0.27,y:2.24,w:span,h:0,line:{color:"C9CEDB",width:1.25}});
steps.forEach((st,i)=>{
  const cx=x0+i*gap, last=i===n-1;
  badge(s,cx,2.02,st[0],last?GOLD:NAVY,last?NAVY:GOLD,0.44);
  s.addText(st[1],{x:cx-0.62,y:2.62,w:1.7,h:0.24,isTextBox:true,margin:0,align:"center",
    fontFace:SANS,fontSize:9.5,color:last?GOLD:BODY});
  s.addText(st[2],{x:cx-0.62,y:2.88,w:1.7,h:0.5,isTextBox:true,margin:0,align:"center",
    fontFace:SANS,fontSize:12,bold:true,color:NAVY,lineSpacing:14});
});
s.addText("How the balance shifts",{x:M,y:3.7,w:6,h:0.3,isTextBox:true,margin:0,
  fontFace:SERIF,fontSize:18,color:NAVY});
[["Weeks 1 and 2","80% teaching  ·  20% exam questions","Most of the time goes on content."],
 ["Weeks 3 to 5","Roughly half teaching, half timed work","Timed sections start short and lengthen."],
 ["Week 6","Full papers only, no new content","Two full papers, marked and reviewed."]].forEach((b,i)=>{
  const x=M+i*4.0;
  card(s,x,4.1,3.83,1.28,CARD,LINE);
  s.addText(b[0],{x:x+0.28,y:4.28,w:3.3,h:0.26,isTextBox:true,margin:0,fontFace:SANS,
    fontSize:11,bold:true,color:GOLD,charSpacing:1.2});
  s.addText(b[1],{x:x+0.28,y:4.56,w:3.3,h:0.44,isTextBox:true,margin:0,valign:"top",fontFace:SANS,
    fontSize:11.5,bold:true,color:NAVY,lineSpacing:15});
  s.addText(b[2],{x:x+0.28,y:5.0,w:3.3,h:0.28,isTextBox:true,margin:0,fontFace:SANS,
    fontSize:10,color:BODY});
});
card(s,M,5.62,11.83,1.08,TINT);
s.addText("Full papers come in weeks 1, 5 and twice in week 6, with timed sections in weeks 3 and 4.",
  {x:1.1,y:5.82,w:11.1,h:0.28,isTextBox:true,margin:0,fontFace:SANS,fontSize:12,bold:true,color:NAVY});
s.addText("That gives three rounds of feedback with time left to act on each one.",
  {x:1.1,y:6.14,w:11.1,h:0.3,isTextBox:true,margin:0,fontFace:SANS,fontSize:11,color:BODY});

/* ---------------------------------------------------------- 6 PAST PAPERS */
s=p.addSlide(); head(s,"PAST PAPERS","How they are used, and from when");
s.addText("Past papers do two jobs here, and we use them differently for each.",
  {x:M,y:1.6,w:11.4,h:0.3,isTextBox:true,margin:0,valign:"top",fontFace:SANS,fontSize:12.5,color:BODY});

card(s,M,2.02,5.7,2.98,CARD,GOLD);
s.addText("Questions, from the next session",{x:1.1,y:2.24,w:5.0,h:0.34,isTextBox:true,margin:0,
  valign:"top",fontFace:SERIF,fontSize:20,color:NAVY});
s.addText("Every topic is practised on real exam questions rather than textbook exercises.",
  {x:1.1,y:2.64,w:5.0,h:0.4,isTextBox:true,margin:0,valign:"top",fontFace:SANS,fontSize:10.5,
   italic:true,color:BODY,lineSpacing:14});
bullets(s,["Topic-sorted questions while the topic is being covered",
           "Mixed and ungrouped in the daily practice, so the method has to be chosen first",
           "Marked against the published mark scheme",
           "Anything wrong goes into the error log"],1.1,3.16,5.0,11,BODY,0.3);

card(s,6.88,2.02,5.7,2.98,NAVY);
s.addText("Whole papers, four of them",{x:7.23,y:2.24,w:5.0,h:0.34,isTextBox:true,margin:0,
  valign:"top",fontFace:SERIF,fontSize:20,color:CREAM});
s.addText("Timed, under exam conditions, on set dates. These are how we measure progress.",
  {x:7.23,y:2.64,w:5.0,h:0.4,isTextBox:true,margin:0,valign:"top",fontFace:SANS,fontSize:10.5,
   italic:true,color:ONNAVYMUTE,lineSpacing:14});
[["WEEK 1","Baseline paper, at home, timed"],
 ["WEEK 5","Full paper under exam conditions"],
 ["WEEK 6","Two full papers, marked and reviewed"]].forEach((r,i)=>{
  const y=3.10+i*0.44;
  s.addText(r[0],{x:7.23,y:y+0.03,w:1.0,h:0.26,isTextBox:true,margin:0,fontFace:SANS,
    fontSize:9.5,bold:true,color:GOLD,charSpacing:1.2});
  s.addText(r[1],{x:8.3,y,w:3.95,h:0.3,isTextBox:true,margin:0,valign:"top",fontFace:SANS,
    fontSize:11.5,color:ONNAVY});
});
s.addText("The baseline uses a past paper rather than the specimen, since part of the specimen has already been seen.\nAbout twelve hours in total, including the marking.",
  {x:7.23,y:4.26,w:5.0,h:0.6,isTextBox:true,margin:0,valign:"top",fontFace:SANS,fontSize:10,
   color:ONNAVYMUTE,lineSpacing:13.5});

card(s,M,5.2,11.83,1.5,TINT);
[["MARKING","A paper is only worth the time if it is marked and reviewed. Charlotte marks each one against the published mark scheme, and the session afterwards covers her five biggest losses."],
 ["WHY NOT MORE","There is no shortage of 4MA1 papers, so the limit is time. A full paper costs two hours to sit and one to review. In weeks 2 to 4 those hours are better spent on teaching and short timed sections."]
].forEach((c,i)=>{
  const x=1.1+i*5.9;
  s.addText(c[0],{x,y:5.38,w:5.3,h:0.24,isTextBox:true,margin:0,fontFace:SANS,fontSize:9,
    bold:true,color:GOLD,charSpacing:1.4});
  s.addText(c[1],{x,y:5.66,w:5.3,h:0.88,isTextBox:true,margin:0,valign:"top",fontFace:SANS,
    fontSize:10.5,color:BODY,lineSpacing:14.5});
});

/* ------------------------------------------------- 7-9 WEEK PAIRS */
const weekPairs=[
 {eyebrow:"WEEKS 1 AND 2",title:"Starting with the foundations",
  w:[{n:"1",label:"WEEK 1  ·  21 to 27 Sep",name:"Baseline and setup",
      pts:["Fluency audit: 35 questions, 50 minutes","Calculator setup: fraction key, ANS and STO, standard form, table mode, degree mode","The formula sheet: what is provided, so no time goes on learning it","Method marks: how working earns marks","Setting up the error log"],
      home:"Baseline paper at home, 2 hours, timed. Daily practice: negatives in algebra.",
      paper:"Baseline paper, reviewed together in session two"},
     {n:"2",label:"WEEK 2  ·  28 Sep to 4 Oct",name:"Number",
      pts:["Fractions: all four operations","Percentage multipliers, increase and decrease","Reverse percentages","Standard form and index laws","One method per topic, used every time"],
      home:"Daily practice: negatives and fractions.",
      paper:"Topic questions on percentages"}]},
 {eyebrow:"WEEKS 3 AND 4",title:"Algebra, then the data topics",
  w:[{n:"3",label:"WEEK 3  ·  5 to 11 Oct",name:"Algebra",
      pts:["Collecting terms and expanding brackets","Solving with x on both sides","Substitution and rearranging formulae","Linear simultaneous equations","Audit repeated (checkpoint 1)"],
      home:"Daily practice: fractions and percentages.",
      paper:"Timed section, 25 minutes, two-pass rule applied"},
     {n:"4",label:"WEEK 4  ·  12 to 18 Oct",name:"Ratio, data and graphs",
      pts:["Ratio and proportion by the unitary method","Averages and frequency tables","Estimated mean from grouped data","Probability, tree diagrams and Venn diagrams","Sequences and straight-line graphs"],
      home:"Daily practice: solving and ratio.",
      paper:"Timed section, 40 minutes, marked against the mark scheme"}]},
 {eyebrow:"WEEKS 5 AND 6",title:"Shape, then papers",
  w:[{n:"5",label:"WEEK 5  ·  19 to 25 Oct",name:"Shape and space",
      pts:["Angle facts, area and perimeter","Circles, prisms and cylinders","Pythagoras and right-angled trigonometry","Length, area and volume scale factors","Audit repeated (checkpoint 2)"],
      home:"Daily practice: all six target skills, mixed.",
      paper:"First full paper, 2 hours, exam conditions"},
     {n:"6",label:"WEEK 6  ·  26 Oct to 1 Nov",name:"Papers",
      pts:["Review and correct the week 5 paper","Second full paper, then the five biggest losses","Third full paper if the first two are on target","Pacing and exam technique session","No new content after 25 October"],
      home:"Daily practice: from the error log.",
      paper:"Two full papers, plus a third if week 5 reached 35 out of 100"}]}];

weekPairs.forEach(wp=>{
  const s=p.addSlide(); head(s,wp.eyebrow,wp.title);
  wp.w.forEach((wk,i)=>{
    const x=M+i*6.13;
    card(s,x,1.72,5.7,4.98,CARD,LINE);
    badge(s,x+0.35,1.98,wk.n,NAVY,GOLD,0.46);
    s.addText(wk.label,{x:x+0.95,y:2.0,w:4.5,h:0.24,isTextBox:true,margin:0,
      fontFace:SANS,fontSize:9.5,bold:true,color:GOLD,charSpacing:1.4});
    s.addText(wk.name,{x:x+0.95,y:2.24,w:4.5,h:0.34,isTextBox:true,margin:0,
      fontFace:SERIF,fontSize:20,color:NAVY});
    bullets(s,wk.pts,x+0.35,2.82,5.0,11.5,BODY);
    rule(s,x+0.35,4.86,5.0);
    kv(s,x+0.35,5.0,5.0,"AT HOME",wk.home);
    kv(s,x+0.35,5.84,5.0,"PAPER WORK",wk.paper,GOLD);
  });
});

/* ---------------------------------------------------------- 10 EXAM WEEK */
s=p.addSlide(); head(s,"EXAM WEEK","2 to 6 November");
[["MON 2 NOV","Last session","No new content. A run through everything covered, a pacing rehearsal and a calculator check, finishing on a topic Charlotte is confident with."],
 ["WED 4 NOV","Paper 1H","Morning, 2 hours, 100 marks. Two passes: the recognisable questions first, then back to anything flagged. The last ten minutes for checking."],
 ["THU 5 NOV","The day between","No full review of the paper. We go back to the questions Charlotte started and left, where a mark is often one line away, then cover the two or three topics she could not begin."],
 ["FRI 6 NOV","Paper 2H","Morning, 2 hours, 100 marks. Same pacing. Both papers cover the whole specification, so topics from Wednesday will come up again."]].forEach((d,i)=>{
  const x=M+i*3.0, dark=i===1||i===3;
  card(s,x,1.8,2.83,4.15,dark?NAVY:CARD,dark?null:LINE);
  s.addText(d[0],{x:x+0.28,y:2.02,w:2.3,h:0.24,isTextBox:true,margin:0,fontFace:SANS,
    fontSize:9.5,bold:true,color:GOLD,charSpacing:1.4});
  s.addText(d[1],{x:x+0.28,y:2.3,w:2.3,h:0.34,isTextBox:true,margin:0,fontFace:SERIF,
    fontSize:19,color:dark?CREAM:NAVY});
  s.addText(d[2],{x:x+0.28,y:2.82,w:2.3,h:2.9,isTextBox:true,margin:0,valign:"top",fontFace:SANS,
    fontSize:11,color:dark?ONNAVYMUTE:BODY,lineSpacing:15.5});
});
card(s,M,6.12,11.83,0.62,TINT);
s.addText("No new content after 25 October. The remaining time is for consolidation.",
  {x:1.1,y:6.12,w:11.1,h:0.62,isTextBox:true,margin:0,valign:"middle",fontFace:SANS,
   fontSize:12,bold:true,color:NAVY});

/* ---------------------------------------------------------- 11 SCOPE */
s=p.addSlide(); head(s,"SCOPE","What we cover, and what we leave out");
[{icon:"✓",t:"Covered",sub:"About 105 marks sit in this list, comfortably above the target.",
  fill:CARD,border:GOLD,col:NAVY,
  pts:["Fractions, decimals, percentages, reverse percentages","Negatives, indices, standard form, rounding","Ratio and proportion by the unitary method","Solving, expanding, substituting, rearranging","Linear simultaneous equations","Sequences and straight-line graphs","Angles, area, circles, prisms, Pythagoras, trigonometry","Length, area and volume scale factors","Averages, frequency tables, probability, Venn diagrams"]},
 {icon:"✕",t:"Left out",sub:"Worth 60 to 80 marks, and unlikely to repay the time in six weeks.",
  fill:TINT,border:LINE,col:BODY,
  pts:["Circle theorems and their proofs","Vectors and vector geometry","Histograms with unequal class widths","Algebraic fractions, functions, graph transformations","Surds, bounds, 3D trigonometry","Quadratic formula, sine and cosine rules","Quadratic simultaneous equations and inequalities","Iteration and numerical methods"]}
].forEach((c,i)=>{
  const x=M+i*6.13;
  card(s,x,1.72,5.7,4.18,c.fill,c.border);
  badge(s,x+0.35,1.96,c.icon,i===0?NAVY:"C4C8CE",i===0?GOLD:CREAM,0.42);
  s.addText(c.t,{x:x+0.92,y:1.97,w:4.5,h:0.36,isTextBox:true,margin:0,fontFace:SERIF,
    fontSize:20,color:NAVY});
  s.addText(c.sub,{x:x+0.35,y:2.46,w:5.0,h:0.46,isTextBox:true,margin:0,valign:"top",fontFace:SANS,
    fontSize:10.5,italic:true,color:BODY,lineSpacing:14});
  bullets(s,c.pts,x+0.35,3.0,5.0,11,c.col);
});
card(s,M,6.06,11.83,0.56,NAVY);
s.addText("Charlotte will learn to recognise the topics on the right quickly and move past them, so the time goes to questions she can answer.",
  {x:1.1,y:6.06,w:11.1,h:0.56,isTextBox:true,margin:0,valign:"middle",fontFace:SANS,
   fontSize:11.5,color:ONNAVY});

/* ---------------------------------------------------------- 12 TECHNIQUE */
s=p.addSlide(); head(s,"TECHNIQUE","Marks that do not need new content");
s.addText("Four habits, covered in week 1 and applied to every timed piece of work after it. At this level they are usually worth more than any single extra topic.",
  {x:M,y:1.62,w:11.4,h:0.34,isTextBox:true,margin:0,valign:"top",fontFace:SANS,fontSize:12.5,color:BODY});
[["01","Method marks","Working earns marks even when the final answer is wrong. Every question gets a substitution line and visible steps, and nothing is rubbed out."],
 ["02","Always something written","A correct first step scores, and a blank does not. Every question gets at least one line, including the ones we have left out."],
 ["03","Two passes","The recognisable questions first, then back to anything flagged. Practised on every timed section from week 3, so it is familiar by November."],
 ["04","The last line","Marks are often lost at the end of correct work. Answers get checked for units, for degrees, and for the rounding the question asked for."]
].forEach((t,i)=>{
  const x=M+i*3.0, dk=i%2===0;
  card(s,x,2.15,2.83,3.55,dk?NAVY:CARD,dk?null:LINE);
  s.addText(t[0],{x:x+0.28,y:2.38,w:1.2,h:0.44,isTextBox:true,margin:0,fontFace:SERIF,
    fontSize:28,color:GOLD});
  s.addText(t[1],{x:x+0.28,y:2.9,w:2.3,h:0.5,isTextBox:true,margin:0,valign:"top",fontFace:SERIF,
    fontSize:18,color:dk?CREAM:NAVY,lineSpacing:21});
  s.addText(t[2],{x:x+0.28,y:3.52,w:2.3,h:2.0,isTextBox:true,margin:0,valign:"top",fontFace:SANS,
    fontSize:11,color:dk?ONNAVYMUTE:BODY,lineSpacing:15.5});
});
card(s,M,5.95,11.83,0.78,TINT);
s.addText("Every marked piece of work records marks lost to blanks, to missing working and to the final line. We review those three numbers in weeks 3 and 5.",
  {x:1.1,y:5.95,w:11.1,h:0.78,isTextBox:true,margin:0,valign:"middle",fontFace:SANS,
   fontSize:11.5,color:NAVY,lineSpacing:16});

/* ---------------------------------------------------------- 13 HOME */
s=p.addSlide(); head(s,"BETWEEN SESSIONS","Twenty minutes a day, six days a week");
s.addText("This starts from the next session and runs to the exams. Six days a week for six weeks comes to about twelve hours, close to the total lesson time, and short daily sessions work better here than one long session at the weekend.",
  {x:M,y:1.62,w:11.4,h:0.4,isTextBox:true,margin:0,valign:"top",fontFace:SANS,fontSize:12.5,
   color:BODY,lineSpacing:17});
[["5 min","Target skill","Twenty questions on the week's target skill, written out in full and timed, with the score noted."],
 ["10 min","Mixed practice","Six questions from topics already covered, not grouped, so the method has to be chosen first."],
 ["5 min","Error log","Read through it, then redo two earlier errors without looking at the correction."]
].forEach((sl,i)=>{
  const x=M+i*4.0;
  card(s,x,2.2,3.83,1.95,CARD,LINE);
  s.addText(sl[0],{x:x+0.3,y:2.4,w:1.4,h:0.36,isTextBox:true,margin:0,fontFace:SERIF,
    fontSize:22,color:GOLD});
  s.addText(sl[1],{x:x+1.55,y:2.47,w:2.0,h:0.3,isTextBox:true,margin:0,fontFace:SANS,
    fontSize:12.5,bold:true,color:NAVY});
  s.addText(sl[2],{x:x+0.3,y:2.89,w:3.25,h:1.12,isTextBox:true,margin:0,valign:"top",fontFace:SANS,
    fontSize:10.5,color:BODY,lineSpacing:14.5});
});
[["1","Nothing new is learned at home"],["2","Charlotte marks her own work"],
 ["3","The same time each day"],["4","Sunday is five minutes, error log only"],
 ["5","A photo of the marked sheet, sent the same day"]].forEach((r,i)=>{
  const x=M+i*2.4;
  badge(s,x,4.48,r[0],NAVY,GOLD,0.38);
  s.addText(r[1],{x:x,y:4.95,w:2.2,h:0.56,isTextBox:true,margin:0,valign:"top",fontFace:SANS,
    fontSize:11,bold:true,color:NAVY,lineSpacing:14.5});
});
card(s,M,5.72,11.83,0.98,NAVY);
s.addText("We will look at how the daily work is going at the end of week 2.",
  {x:1.1,y:5.9,w:11.1,h:0.28,isTextBox:true,margin:0,fontFace:SANS,fontSize:12.5,bold:true,color:GOLD});
s.addText("It is the easiest part of the plan to lose and the hardest to make up. If twenty minutes is not fitting around everything else, please say so and we will adjust the plan around what is realistic.",
  {x:1.1,y:6.22,w:11.1,h:0.34,isTextBox:true,margin:0,valign:"top",fontFace:SANS,fontSize:11,color:ONNAVYMUTE});

/* ---------------------------------------------------------- 14 PROGRESS */
s=p.addSlide(); head(s,"PROGRESS","How we will track it");
s.addText("Two numbers: Charlotte's audit score, and her marks on a timed paper. Each checkpoint has a set response.",
  {x:M,y:1.62,w:11.4,h:0.3,isTextBox:true,margin:0,valign:"top",fontFace:SANS,fontSize:12.5,color:BODY});
[["WEEK 1","Baseline","Audit and a full paper","Recorded as a starting point."],
 ["WEEK 3","Checkpoint 1","Audit repeated","The weakest skills should have improved."],
 ["WEEK 5","First full paper","35 / 100 or better","On track. If it is below, see the note underneath."],
 ["WEEK 6","Second full paper","40 / 100 or better","80 out of 200, 15 clear of the boundary."]
].forEach((c,i)=>{
  const x=M+i*3.0, dk=i>=2;
  card(s,x,2.1,2.83,2.55,dk?NAVY:CARD,dk?null:LINE);
  s.addText(c[0],{x:x+0.28,y:2.3,w:2.3,h:0.24,isTextBox:true,margin:0,fontFace:SANS,
    fontSize:9.5,bold:true,color:GOLD,charSpacing:1.4});
  s.addText(c[1],{x:x+0.28,y:2.58,w:2.3,h:0.3,isTextBox:true,margin:0,fontFace:SANS,
    fontSize:12.5,bold:true,color:dk?CREAM:NAVY});
  s.addText(c[2],{x:x+0.28,y:2.98,w:2.3,h:0.6,isTextBox:true,margin:0,valign:"top",fontFace:SERIF,
    fontSize:17,color:dk?GOLD:NAVY,lineSpacing:20});
  s.addText(c[3],{x:x+0.28,y:3.66,w:2.3,h:0.85,isTextBox:true,margin:0,valign:"top",fontFace:SANS,
    fontSize:10.5,color:dk?ONNAVYMUTE:BODY,lineSpacing:14.5});
});
card(s,M,4.88,11.83,1.82,TINT);
s.addText("If a number comes in low",{x:1.1,y:5.05,w:5.2,h:0.3,isTextBox:true,
  margin:0,fontFace:SERIF,fontSize:17,color:NAVY});
bullets(s,["If the audit has not moved by week 3, the daily work is usually the cause, and we look at that first.",
           "Below 35 out of 100 in week 5, week 6 drops the third paper and goes back to the two weakest topics.",
           "Above 50 out of 100 in week 5, we add the single-step grade 6 topics."],
  1.1,5.45,7.6,10.5,BODY,0.28);
s.addShape(p.ShapeType.line,{x:9.05,y:5.05,w:0,h:1.45,line:{color:"D8D3C6",width:0.75}});
s.addText("AFTER EACH SESSION",{x:9.4,y:5.05,w:3.0,h:0.24,isTextBox:true,margin:0,fontFace:SANS,
  fontSize:9,bold:true,color:GOLD,charSpacing:1.4});
s.addText("A short note from me: what we covered, Charlotte's recall score out of six, and whether the daily work came back.",
  {x:9.4,y:5.34,w:3.1,h:1.1,isTextBox:true,margin:0,valign:"top",fontFace:SANS,fontSize:11,
   color:BODY,lineSpacing:15});

/* ---------------------------------------------------------- 15 CONTINGENCIES */
s=p.addSlide(); head(s,"CONTINGENCIES","What could get in the way, and what we do");
[["Entry or tier not confirmed","This one sits with you and the school. Entry deadlines for the November series fall in early October, so it is worth confirming in the next week or so."],
 ["A week is lost to illness","Week 6 carries the slack. The third full paper comes out first, then the pacing session. The teaching weeks stay as they are."],
 ["The daily work does not fit","We look at this at the end of week 2. If it is not working, week 5 shape content reduces to three topics and that time goes to number and algebra."],
 ["The audit is worse than expected","Weeks 2 and 3 stay as they are, and week 4 drops sequences and straight-line graphs. Number and algebra stay in."]
].forEach((r,i)=>{
  const x=M+(i%2)*6.13, y=1.78+Math.floor(i/2)*2.25;
  card(s,x,y,5.7,2.05,i%2===0?CARD:TINT,LINE);
  badge(s,x+0.35,y+0.26,String(i+1),NAVY,GOLD,0.42);
  s.addText(r[0],{x:x+0.92,y:y+0.28,w:4.5,h:0.34,isTextBox:true,margin:0,fontFace:SERIF,
    fontSize:17,color:NAVY});
  s.addText(r[1],{x:x+0.35,y:y+0.8,w:5.0,h:1.1,isTextBox:true,margin:0,valign:"top",fontFace:SANS,
    fontSize:11,color:BODY,lineSpacing:15.5});
});
s.addText("Each of these has a response and a point at which we decide.",
  {x:M,y:6.4,w:11.83,h:0.3,isTextBox:true,margin:0,fontFace:SANS,fontSize:11.5,color:BODY});

/* ---------------------------------------------------------- 16 CLOSE */
s=p.addSlide(); s.background={color:NAVY};
s.addShape(p.ShapeType.ellipse,{x:10.6,y:5.6,w:3.4,h:3.4,fill:{color:"1C3255"},line:{type:"none"}});
s.addText("THE PLAN",{x:M,y:0.95,w:6,h:0.3,isTextBox:true,margin:0,fontFace:SANS,
  fontSize:10.5,bold:true,color:GOLD,charSpacing:2.6});
s.addText("Rebuild number and algebra first.\nCover about 105 marks of content and work towards 80.\nLeave the rest out.",
  {x:M,y:1.45,w:11.2,h:2.2,isTextBox:true,margin:0,valign:"top",fontFace:SERIF,fontSize:28,
   color:CREAM,lineSpacing:44});
rule(s,M,3.95,6.2,"3A4E70");
s.addText("THIS WEEK",{x:M,y:4.22,w:4,h:0.3,isTextBox:true,margin:0,fontFace:SANS,
  fontSize:10.5,bold:true,color:GOLD,charSpacing:2.2});
[["1","Confirm the entry, tier and exam times with the school"],
 ["2","Fluency audit and calculator setup in the next session"],
 ["3","Baseline paper at home, and the error log set up"]].forEach((t,i)=>{
  const y=4.62+i*0.56;
  badge(s,M,y,t[0],NAVYCARD,GOLD,0.38);
  s.addText(t[1],{x:M+0.55,y:y+0.04,w:8.5,h:0.3,isTextBox:true,margin:0,fontFace:SANS,
    fontSize:13,color:ONNAVY});
});
s.addText("If anything here does not look right, please say and we will change it.",
  {x:M,y:6.3,w:8.5,h:0.3,isTextBox:true,margin:0,fontFace:SANS,fontSize:11.5,color:ONNAVYMUTE});
s.addText("Ali Tutors",{x:M,y:6.85,w:4,h:0.3,isTextBox:true,margin:0,fontFace:SERIF,
  fontSize:14,color:ONNAVYMUTE});

p.writeFile({fileName:"/tmp/claude-0/-home-user-Daily/1f1029ee-a03d-535a-b39f-f5f806492334/scratchpad/Charlotte_maths_plan.pptx"})
 .then(()=>console.log("written"));
