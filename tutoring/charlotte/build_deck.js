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
s.addText("Prepared for Charlotte  ·  21 September 2026",
  {x:M,y:6.35,w:7,h:0.3,isTextBox:true,margin:0,fontFace:SANS,fontSize:11,color:ONNAVYMUTE});
s.addNotes("Audience: student and parent together. Series runs 27 Oct to 19 Nov, so she must stay available to 19 Nov.");

/* ---------------------------------------------------------- 2 EXAMS */
s=p.addSlide(); head(s,"THE EXAMS","Two papers, two days apart");
card(s,M,1.85,3.55,3.1,NAVY);
s.addText("44",{x:M,y:2.05,w:3.55,h:1.25,isTextBox:true,margin:0,align:"center",
  fontFace:SERIF,fontSize:76,color:GOLD});
s.addText("days until Paper 1",{x:M,y:3.3,w:3.55,h:0.3,isTextBox:true,margin:0,
  align:"center",fontFace:SANS,fontSize:13,bold:true,color:CREAM});
s.addText("Six teaching weeks\nand two days",{x:M,y:3.72,w:3.55,h:0.7,isTextBox:true,margin:0,
  align:"center",fontFace:SANS,fontSize:11,color:ONNAVYMUTE,lineSpacing:16});

const papers=[["Wed 4 Nov","Paper 1H","Morning  ·  2 hours  ·  100 marks  ·  calculator"],
              ["Fri 6 Nov","Paper 2H","Morning  ·  2 hours  ·  100 marks  ·  calculator"]];
papers.forEach((pp,i)=>{
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
s.addText("Both papers allow a calculator, and both cover the full specification.",
  {x:1.05,y:5.48,w:11.2,h:0.3,isTextBox:true,margin:0,fontFace:SANS,fontSize:13,bold:true,color:NAVY});
s.addText("Calculator technique is taught in session one, not left to habit, and the mode is checked before every timed piece of work. Because both papers sample the whole specification, a topic missed on Paper 1 is likely to reappear on Paper 2.",
  {x:1.05,y:5.82,w:11.2,h:0.66,isTextBox:true,margin:0,fontFace:SANS,fontSize:11.5,color:BODY,lineSpacing:16});
s.addNotes("Confirm exact session times with the school. Late entry deadlines for the November series fall in early October.");

/* ---------------------------------------------------------- 3 TARGET */
s=p.addSlide(); head(s,"THE TARGET","The number we are working to");
card(s,M,1.85,3.9,4.15,NAVY);
s.addText("65",{x:M,y:2.15,w:3.9,h:1.4,isTextBox:true,margin:0,align:"center",
  fontFace:SERIF,fontSize:86,color:GOLD});
s.addText("marks out of 200",{x:M,y:3.6,w:3.9,h:0.3,isTextBox:true,margin:0,align:"center",
  fontFace:SANS,fontSize:14,bold:true,color:CREAM});
s.addText("The grade 5 boundary on Higher tier in November 2025, which is just under a third of the paper. Boundaries move each series, so this is a reference point, not a guarantee.",
  {x:1.1,y:4.15,w:3.2,h:1.5,isTextBox:true,margin:0,fontFace:SANS,fontSize:11.5,
   color:ONNAVYMUTE,lineSpacing:16.5});

const tx=5.05, tw=7.53, cw=[3.13,2.2,2.2];
const hdr=["Grade","Marks needed","Share of total"];
s.addShape(p.ShapeType.rect,{x:tx,y:1.85,w:tw,h:0.46,fill:{color:NAVY},line:{type:"none"}});
hdr.forEach((hd,i)=>{
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
s.addText("We plan to 80 marks, not to 65",{x:5.4,y:4.24,w:6.9,h:0.34,isTextBox:true,margin:0,
  valign:"top",fontFace:SERIF,fontSize:19,color:NAVY});
s.addText("Two reasons. Boundaries move, so a plan that lands exactly on last year's number can still miss. More importantly, margin does not come from the target we set. It comes from the size of the pool of marks we teach, which is the next two slides.",
  {x:5.4,y:4.68,w:6.9,h:1.15,isTextBox:true,margin:0,valign:"top",fontFace:SANS,fontSize:12,
   color:BODY,lineSpacing:17});
s.addNotes("Nov 2025 Higher boundaries used here: 9=166, 8=136, 7=107, 6=86, 5=65, 4=45. Verify against the Pearson published boundaries before quoting to the parent.");

/* ---------------------------------------------------------- 4 TIER */
s=p.addSlide(); head(s,"THE TIER","Why Higher, and when it is confirmed");
const tiers=[
 {t:"Higher tier",sub:"Grades 4 to 9",pick:true,
  pts:["Grade 5 needs 65 of 200, which is 33%","She can leave two thirds of the paper and still reach the target","Roughly 60% of the content sits above her band","No cap on the grade if she outperforms"]},
 {t:"Foundation tier",sub:"Grades 1 to 5",pick:false,
  pts:["Grade 5 needs roughly three quarters of the paper","Every topic sits inside our teach list, so nothing is wasted","Almost no room for error across 200 marks","Grade 5 is the ceiling, whatever she scores"]}];
tiers.forEach((t,i)=>{
  const x=M+i*6.13;
  card(s,x,1.8,5.7,2.82,t.pick?CARD:TINT,t.pick?GOLD:LINE);
  s.addText(t.t,{x:x+0.35,y:2.02,w:3.4,h:0.34,isTextBox:true,margin:0,
    fontFace:SERIF,fontSize:21,color:NAVY});
  s.addText(t.sub,{x:x+0.35,y:2.4,w:3.4,h:0.26,isTextBox:true,margin:0,
    fontFace:SANS,fontSize:10.5,bold:true,color:GOLD,charSpacing:1.4});
  if(t.pick){
    s.addShape(p.ShapeType.roundRect,{x:x+4.05,y:2.05,w:1.3,h:0.38,rectRadius:0.19,
      fill:{color:NAVY},line:{type:"none"}});
    s.addText("CHOSEN",{x:x+4.05,y:2.05,w:1.3,h:0.38,isTextBox:true,margin:0,align:"center",
      valign:"middle",fontFace:SANS,fontSize:9,bold:true,color:GOLD,charSpacing:1.4});
  }
  bullets(s,t.pts,x+0.35,2.9,5.0,12,t.pick?NAVY:BODY);
});
card(s,M,5.02,11.83,1.6,NAVY);
s.addText("Higher, because at 33% her mistakes are cheap.",{x:1.1,y:5.26,w:11.1,h:0.3,
  isTextBox:true,margin:0,fontFace:SANS,fontSize:13,bold:true,color:GOLD});
s.addText("On Foundation the same grade asks for near accuracy on every question, which is the opposite of her profile. The school confirms the entry and tier in week one. Edexcel entry deadlines for the November series fall in early October, so this is the first action on the list, not an administrative detail to settle later.",
  {x:1.1,y:5.6,w:11.1,h:0.85,isTextBox:true,margin:0,valign:"top",fontFace:SANS,fontSize:11.5,
   color:ONNAVY,lineSpacing:16});
s.addNotes("Foundation grade 5 on 4MA1 has typically sat around 73 to 80 per cent of 200. Check the current figure before presenting. If the school has already entered her, confirm which tier and whether a change is still possible.");

/* ---------------------------------------------------------- 5 WHERE MARKS ARE */
s=p.addSlide(); head(s,"WHERE THE MARKS ARE","Number and algebra is 60% of the qualification");
s.addChart(p.ChartType.bar,[{name:"Marks of 200",labels:["Handling data","Shape, space and measure","Number and algebra"],values:[30,50,120]}],
 {x:0.55,y:1.75,w:6.3,h:2.9,barDir:"bar",chartColors:["9AA6B8",GOLD,NAVY],varyColors:true,
  showValue:true,dataLabelPosition:"outEnd",dataLabelColor:NAVY,dataLabelFontFace:SANS,
  dataLabelFontSize:12,dataLabelFontBold:true,showLegend:false,showTitle:false,
  catAxisLabelColor:NAVY,catAxisLabelFontFace:SANS,catAxisLabelFontSize:11.5,
  valAxisHidden:true,valGridLine:{style:"none"},catGridLine:{style:"none"},
  barGapWidthPct:55,valAxisMaxVal:140,chartArea:{fill:{color:CREAM}},plotArea:{fill:{color:CREAM}}});

const notes5=[["Her weakest area is also the largest","The Year 9 gaps sit in number and algebra. Fixing them pays out across 120 marks rather than 20, so the first three weeks go there and nowhere else."],
              ["Handling data needs very little algebra","Averages, tables, probability and Venn diagrams are 30 marks that weak algebra does not block. They are taught in week 4, once the algebra spine is in place."]];
notes5.forEach((n,i)=>{
  const y=1.8+i*1.5;
  card(s,7.1,y,5.48,1.32,CARD,LINE);
  s.addText(n[0],{x:7.42,y:y+0.18,w:4.85,h:0.28,isTextBox:true,margin:0,
    fontFace:SANS,fontSize:12.5,bold:true,color:NAVY});
  s.addText(n[1],{x:7.42,y:y+0.5,w:4.85,h:0.7,isTextBox:true,margin:0,
    fontFace:SANS,fontSize:11,color:BODY,lineSpacing:15});
});

card(s,M,4.95,11.83,1.75,NAVY);
s.addText("The pool, and why it decides the plan",{x:1.1,y:5.15,w:11.1,h:0.32,isTextBox:true,
  margin:0,fontFace:SERIF,fontSize:19,color:GOLD});
const pool=[["about 80","marks are pitched at grades 4 and 5","Teach only this band and she must convert 65 of 80, so she can afford to drop 15 marks in two hours."],
            ["about 105","marks once we add single-step grade 6 work","Same target of 65 to pass, but now she can afford to drop 40 marks and still get there."]];
pool.forEach((q,i)=>{
  const x=1.1+i*5.6;
  s.addText(q[0],{x,y:5.53,w:1.75,h:0.4,isTextBox:true,margin:0,valign:"top",fontFace:SERIF,fontSize:23,color:CREAM});
  s.addText(q[1],{x:x+1.82,y:5.6,w:3.45,h:0.34,isTextBox:true,margin:0,valign:"top",fontFace:SANS,
    fontSize:11,bold:true,color:ONNAVY,lineSpacing:14});
  s.addText(q[2],{x,y:6.0,w:5.3,h:0.6,isTextBox:true,margin:0,valign:"top",fontFace:SANS,fontSize:10.5,
    color:ONNAVYMUTE,lineSpacing:14.5});
});
s.addNotes("Weightings from the 4MA1 specification: Number and algebra 57 to 63%, Shape space and measure 22 to 28%, Handling data 12 to 18%. The pool figures are estimates from past paper analysis, not published values. Say so if asked.");

/* ---------------------------------------------------------- 6 ROUTE */
s=p.addSlide(); head(s,"THE ROUTE","Six weeks, at a glance");
const steps=[["1","21-27 Sep","Diagnose"],["2","28 Sep-4 Oct","Number"],["3","5-11 Oct","Algebra"],
             ["4","12-18 Oct","Ratio and data"],["5","19-25 Oct","Shape"],["6","26 Oct-1 Nov","Papers"],
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
s.addText("The balance shifts as we go",{x:M,y:3.7,w:6,h:0.3,isTextBox:true,margin:0,
  fontFace:SERIF,fontSize:18,color:NAVY});
const bal=[["Weeks 1 and 2","80% teaching  ·  20% exam questions","Content is broken, so content comes first."],
           ["Weeks 3 to 5","Roughly half teaching, half timed work","Timed sections start short and lengthen."],
           ["Week 6","Full papers only, no new content","Two full papers, marked and patched."]];
bal.forEach((b,i)=>{
  const x=M+i*4.0;
  card(s,x,4.1,3.83,1.28,CARD,LINE);
  s.addText(b[0],{x:x+0.28,y:4.28,w:3.3,h:0.26,isTextBox:true,margin:0,fontFace:SANS,
    fontSize:11,bold:true,color:GOLD,charSpacing:1.2});
  s.addText(b[1],{x:x+0.28,y:4.56,w:3.3,h:0.44,isTextBox:true,margin:0,fontFace:SANS,
    fontSize:11.5,bold:true,color:NAVY,lineSpacing:15});
  s.addText(b[2],{x:x+0.28,y:5.0,w:3.3,h:0.28,isTextBox:true,margin:0,fontFace:SANS,
    fontSize:10,color:BODY});
});
card(s,M,5.62,11.83,1.08,TINT);
s.addText("Full papers are sat in weeks 1, 5 and twice in week 6, with timed sections in weeks 3 and 4.",
  {x:1.1,y:5.82,w:11.1,h:0.28,isTextBox:true,margin:0,fontFace:SANS,fontSize:12,bold:true,color:NAVY});
s.addText("Five timed pieces gives three rounds of feedback that can still change the plan. A first full paper in week 5 would leave only one.",
  {x:1.1,y:6.14,w:11.1,h:0.3,isTextBox:true,margin:0,fontFace:SANS,fontSize:11,color:BODY});
s.addNotes("Past papers are a measuring tool as well as a teaching tool. The week 1 paper is a baseline, sat at home over the first weekend and marked together in session two.");

/* ------------------------------------------------- 7-9 WEEK PAIRS */
const weekPairs=[
 {eyebrow:"WEEKS 1 AND 2",title:"Fix the foundations first",
  w:[{n:"1",label:"WEEK 1  ·  21-27 Sep",name:"Diagnose and set up",
      pts:["Fluency audit: 35 questions, 50 minutes","Calculator setup: fraction key, ANS and STO, standard form, table mode, degree mode","The formula sheet: what is given, so we do not drill it","Method marks: the working rules, applied from day one","Set up the error log"],
      home:"Baseline paper at home, 2 hours, timed. Daily drill: negatives inside algebra.",
      paper:"Baseline Paper 1H, marked together in session two"},
     {n:"2",label:"WEEK 2  ·  28 Sep-4 Oct",name:"The number engine",
      pts:["Fractions: all four operations","Percentage multipliers, increase and decrease","Reverse percentages","Standard form and index laws","One method per topic, used every time"],
      home:"Daily drill: negatives and fractions.",
      paper:"Six past paper percentage questions, untimed"}]},
 {eyebrow:"WEEKS 3 AND 4",title:"The biggest block of marks",
  w:[{n:"3",label:"WEEK 3  ·  5-11 Oct",name:"The algebra spine",
      pts:["Collecting terms and expanding brackets","Solving with x on both sides","Substitution and rearranging formulae","Linear simultaneous equations","Re-run the audit: checkpoint 1"],
      home:"Daily drill: fractions and percentages.",
      paper:"First timed section, 25 minutes, two-pass rule applied"},
     {n:"4",label:"WEEK 4  ·  12-18 Oct",name:"The low-cost marks",
      pts:["Ratio and proportion by the unitary method","Averages and frequency tables","Estimated mean from grouped data","Probability, tree diagrams and Venn diagrams","Sequences and straight-line graphs"],
      home:"Daily drill: solving and ratio.",
      paper:"Timed section, 40 minutes, marked against the mark scheme"}]},
 {eyebrow:"WEEKS 5 AND 6",title:"Shape, then papers only",
  w:[{n:"5",label:"WEEK 5  ·  19-25 Oct",name:"Shape and space",
      pts:["Angle facts, area and perimeter","Circles, prisms and cylinders","Pythagoras and right-angled trigonometry","Length, area and volume scale factors","Re-run the audit: checkpoint 2"],
      home:"Daily drill: all six bottleneck skills, mixed.",
      paper:"First full paper, 2 hours, exam conditions"},
     {n:"6",label:"WEEK 6  ·  26 Oct-1 Nov",name:"Half term: papers",
      pts:["Mark and patch the week 5 paper","Second full paper, then patch the top five losses","Third full paper if the first two are on target","Exam technique and pacing session","No new content after 25 October"],
      home:"Daily drill: straight from the error log.",
      paper:"Two full papers, plus a third if week 5 cleared 35 out of 100"}]}];

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
const days=[["MON 2 NOV","Last session","No new content. Retrieval across everything taught, a pacing rehearsal, and a calculator check. The session finishes on a topic she is strong at."],
            ["WED 4 NOV","Paper 1H","Morning, 2 hours, 100 marks. Two passes: everything she recognises first, then back to the flagged questions. The last ten minutes go to checking work she has already done."],
            ["THU 5 NOV","The gap day","No detailed post-mortem. We re-run the questions she started and abandoned, because those are the ones where a method mark was one line away, then drill the two or three topics she could not begin."],
            ["FRI 6 NOV","Paper 2H","Morning, 2 hours, 100 marks. Same pacing rules. Both papers sample the full specification, so topics from Wednesday will recur."]];
days.forEach((d,i)=>{
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
s.addText("No new content after 25 October. The last week and a half consolidate what is already there.",
  {x:1.1,y:6.12,w:11.1,h:0.62,isTextBox:true,margin:0,valign:"middle",fontFace:SANS,
   fontSize:12,bold:true,color:NAVY});
s.addNotes("Thursday is the highest-value session in the week. Keep it short and specific. Do not review the whole paper.");

/* ---------------------------------------------------------- 11 TRIAGE */
s=p.addSlide(); head(s,"TRIAGE","What we teach, and what we leave");
const cols=[
 {icon:"✓",t:"We teach this",sub:"About 105 marks live here. This list, done well, clears the target with margin.",
  fill:CARD,border:GOLD,col:NAVY,
  pts:["Fractions, decimals, percentages, reverse percentages","Negatives, indices, standard form, rounding","Ratio and proportion by the unitary method","Solving, expanding, substituting, rearranging","Linear simultaneous equations","Sequences and straight-line graphs","Angles, area, circles, prisms, Pythagoras, trigonometry","Length, area and volume scale factors","Averages, frequency tables, probability, Venn diagrams"]},
 {icon:"✕",t:"We leave this",sub:"Worth 60 to 80 marks she would convert very little of in six weeks.",
  fill:TINT,border:LINE,col:BODY,
  pts:["Circle theorems and their proofs","Vectors and vector geometry","Histograms with unequal class widths","Algebraic fractions, functions, graph transformations","Surds, bounds, 3D trigonometry","Quadratic formula, sine and cosine rules","Quadratic simultaneous equations and inequalities","Iteration and numerical methods"]}];
cols.forEach((c,i)=>{
  const x=M+i*6.13;
  card(s,x,1.72,5.7,4.18,c.fill,c.border);
  badge(s,x+0.35,1.96,c.icon,i===0?NAVY:"C4C8CE",i===0?GOLD:CREAM,0.42);
  s.addText(c.t,{x:x+0.92,y:1.97,w:4.5,h:0.36,isTextBox:true,margin:0,fontFace:SERIF,
    fontSize:20,color:NAVY});
  s.addText(c.sub,{x:x+0.35,y:2.46,w:5.0,h:0.46,isTextBox:true,margin:0,fontFace:SANS,
    fontSize:10.5,italic:true,color:BODY,lineSpacing:14});
  bullets(s,c.pts,x+0.35,3.0,5.0,11,c.col);
});
card(s,M,6.06,11.83,0.56,NAVY);
s.addText("She learns to recognise a left topic within ten seconds and move on. The time saved goes to questions inside her band.",
  {x:1.1,y:6.06,w:11.1,h:0.56,isTextBox:true,margin:0,valign:"middle",fontFace:SANS,
   fontSize:11.5,color:ONNAVY});
s.addNotes("The additions to the teach list since the first draft are linear simultaneous equations and scale factors. Both are single-rule topics that recur and cost under half a session each. The quadratic formula and the sine and cosine rules move to the leave list: they sit above her band and were the only new content previously scheduled for the final week.");

/* ---------------------------------------------------------- 12 TECHNIQUE */
s=p.addSlide(); head(s,"TECHNIQUE","Marks that do not require new content");
s.addText("Four habits, taught in week one and applied to every timed piece of work after it. On past papers these are worth more to a student at this level than any single topic on the teach list.",
  {x:M,y:1.62,w:11.4,h:0.34,isTextBox:true,margin:0,fontFace:SANS,fontSize:12.5,color:BODY});
const tech=[["01","Method marks","Working earns marks on this paper even when the final answer is wrong. Every question gets a substitution line and visible steps. No jumping straight to an answer, and nothing rubbed out."],
            ["02","Nothing blank","A first step that is correct scores. A blank scores nothing. Every question gets at least one written line, including the questions we have chosen to leave."],
            ["03","Two passes","Pass one takes everything she can start within twenty seconds. Pass two returns to what she flagged. Practised on every timed section from week 3, not introduced on the day."],
            ["04","The last line","Marks are lost at the end of correct work. Answers are checked for units, for degrees, and for the rounding the question actually asked for."]];
tech.forEach((t,i)=>{
  const x=M+i*3.0;
  card(s,x,2.15,2.83,3.55,i%2===0?NAVY:CARD,i%2===0?null:LINE);
  const dk=i%2===0;
  s.addText(t[0],{x:x+0.28,y:2.38,w:1.2,h:0.44,isTextBox:true,margin:0,fontFace:SERIF,
    fontSize:28,color:GOLD});
  s.addText(t[1],{x:x+0.28,y:2.92,w:2.3,h:0.34,isTextBox:true,margin:0,fontFace:SERIF,
    fontSize:18,color:dk?CREAM:NAVY});
  s.addText(t[2],{x:x+0.28,y:3.38,w:2.3,h:2.15,isTextBox:true,margin:0,valign:"top",fontFace:SANS,
    fontSize:11,color:dk?ONNAVYMUTE:BODY,lineSpacing:15.5});
});
card(s,M,5.95,11.83,0.78,TINT);
s.addText("Measured the same way as the content: every marked piece of work records marks lost to blanks, to missing working, and to the final line. Those three numbers are reviewed in week 3 and week 5.",
  {x:1.1,y:5.95,w:11.1,h:0.78,isTextBox:true,margin:0,valign:"middle",fontFace:SANS,
   fontSize:11.5,color:NAVY,lineSpacing:16});
s.addNotes("This slide is new. On a calculator paper at grade 5, blanks and missing working are usually worth more than any topic we could add.");

/* ---------------------------------------------------------- 13 HOME */
s=p.addSlide(); head(s,"BETWEEN SESSIONS","Twenty minutes a day, six days a week");
s.addText("Six days a week for six weeks is about twelve hours, which is close to the total lesson time. Retention comes from spacing the work out, so a long session at the weekend does not replace it.",
  {x:M,y:1.62,w:11.4,h:0.34,isTextBox:true,margin:0,fontFace:SANS,fontSize:12.5,color:BODY});
const slots=[["5 min","Method drill","Twenty reps of this week's target skill, written out in full. Timed, and the score is recorded."],
             ["10 min","Mixed retrieval","Six questions from topics already taught, deliberately not grouped by topic, so she has to identify the method first."],
             ["5 min","Error log","Read it, then redo two past errors without looking at the correction."]];
slots.forEach((sl,i)=>{
  const x=M+i*4.0;
  card(s,x,2.15,3.83,1.95,CARD,LINE);
  s.addText(sl[0],{x:x+0.3,y:2.35,w:1.4,h:0.36,isTextBox:true,margin:0,fontFace:SERIF,
    fontSize:22,color:GOLD});
  s.addText(sl[1],{x:x+1.55,y:2.42,w:2.0,h:0.3,isTextBox:true,margin:0,fontFace:SANS,
    fontSize:12.5,bold:true,color:NAVY});
  s.addText(sl[2],{x:x+0.3,y:2.84,w:3.25,h:1.12,isTextBox:true,margin:0,valign:"top",fontFace:SANS,
    fontSize:10.5,color:BODY,lineSpacing:14.5});
});
const rules=[["1","No new learning at home"],["2","She marks her own work"],
             ["3","Same time every day"],["4","Sunday is five minutes, error log only"],
             ["5","Photo of the marked sheet by 8pm"]];
rules.forEach((r,i)=>{
  const x=M+i*2.4;
  badge(s,x,4.45,r[0],NAVY,GOLD,0.38);
  s.addText(r[1],{x:x,y:4.92,w:2.2,h:0.56,isTextBox:true,margin:0,fontFace:SANS,
    fontSize:11,bold:true,color:NAVY,lineSpacing:14.5});
});
card(s,M,5.7,11.83,1.0,NAVY);
s.addText("If the daily work is not happening by the end of week 2, that is the problem we solve before we teach anything else.",
  {x:1.1,y:5.88,w:11.1,h:0.28,isTextBox:true,margin:0,fontFace:SANS,fontSize:12.5,bold:true,color:GOLD});
s.addText("A plan that assumes twelve hours of home practice and gets three is a different plan. We would drop the week 5 shape content to three topics and put the time into the number and algebra weeks instead.",
  {x:1.1,y:6.2,w:11.1,h:0.34,isTextBox:true,margin:0,fontFace:SANS,fontSize:11,color:ONNAVYMUTE});

/* ---------------------------------------------------------- 14 PROGRESS */
s=p.addSlide(); head(s,"PROGRESS","Two numbers, and what we do about them");
s.addText("Her audit score and her marks on a timed paper. Nothing else is tracked, and each checkpoint has a stated response rather than an opinion.",
  {x:M,y:1.62,w:11.4,h:0.3,isTextBox:true,margin:0,fontFace:SANS,fontSize:12.5,color:BODY});
const cps=[["WEEK 1","Baseline","Audit plus a full paper","Recorded, not graded. This is the map."],
           ["WEEK 3","Checkpoint 1","Audit re-run","Bottleneck scores should have moved."],
           ["WEEK 5","First full paper","35 / 100 or better","On track. Below this, see the rule opposite."],
           ["WEEK 6","Second full paper","40 / 100 or better","80 of 200, which is 15 clear of the boundary."]];
cps.forEach((c,i)=>{
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
s.addText("What happens if a number comes in low",{x:1.1,y:5.05,w:5.2,h:0.3,isTextBox:true,
  margin:0,fontFace:SERIF,fontSize:17,color:NAVY});
bullets(s,["Audit has not moved by week 3: the cause is the daily work, and we fix that before adding content.",
           "Below 35 out of 100 in week 5: week 6 drops the third paper and returns to the two weakest topics on the teach list.",
           "Above 50 out of 100 in week 5: we add the single-step grade 6 shortlist rather than repeating work she already has."],
  1.1,5.45,7.6,10.5,BODY,0.28);
rule(s,9.1,5.1,0,LINE);
s.addShape(p.ShapeType.line,{x:9.05,y:5.05,w:0,h:1.45,line:{color:"D8D3C6",width:0.75}});
s.addText("REPORTING",{x:9.4,y:5.05,w:3.0,h:0.24,isTextBox:true,margin:0,fontFace:SANS,
  fontSize:9,bold:true,color:GOLD,charSpacing:1.4});
s.addText("After every session you get one line: what we taught, her retrieval score out of six, and whether the homework came back.",
  {x:9.4,y:5.34,w:3.1,h:1.1,isTextBox:true,margin:0,fontFace:SANS,fontSize:11,color:BODY,lineSpacing:15});

/* ---------------------------------------------------------- 15 RISK */
s=p.addSlide(); head(s,"IF SOMETHING GOES WRONG","The four things most likely to cost the grade");
const risks=[["Entry or tier not confirmed","Confirmed with the school in week 1. The parent owns this one, because late entry deadlines for the November series fall in early October and nothing else in the plan matters if the entry is wrong."],
             ["A week is lost to illness","Week 6 carries the slack. The third full paper is the first thing dropped, then the pacing session. The teaching weeks are not compressed."],
             ["The daily work does not happen","Reviewed at the end of week 2. If it is not running, the shape week is cut to three topics and that time moves to number and algebra."],
             ["The audit is worse than expected","Weeks 2 and 3 hold, and week 4 loses sequences and straight-line graphs. Number and algebra are never the thing we cut."]];
risks.forEach((r,i)=>{
  const x=M+(i%2)*6.13, y=1.78+Math.floor(i/2)*2.25;
  card(s,x,y,5.7,2.05,i%2===0?CARD:TINT,i%2===0?LINE:LINE);
  badge(s,x+0.35,y+0.26,String(i+1),NAVY,GOLD,0.42);
  s.addText(r[0],{x:x+0.92,y:y+0.28,w:4.5,h:0.34,isTextBox:true,margin:0,fontFace:SERIF,
    fontSize:17,color:NAVY});
  s.addText(r[1],{x:x+0.35,y:y+0.8,w:5.0,h:1.1,isTextBox:true,margin:0,valign:"top",fontFace:SANS,
    fontSize:11,color:BODY,lineSpacing:15.5});
});
s.addText("Every item above has a named response and a week by which it is decided. None of them is left to be noticed in week 5.",
  {x:M,y:6.4,w:11.83,h:0.3,isTextBox:true,margin:0,fontFace:SANS,fontSize:11.5,color:BODY});

/* ---------------------------------------------------------- 16 CLOSE */
s=p.addSlide(); s.background={color:NAVY};
s.addShape(p.ShapeType.ellipse,{x:10.6,y:5.6,w:3.4,h:3.4,fill:{color:"1C3255"},line:{type:"none"}});
s.addText("THE PLAN",{x:M,y:0.95,w:6,h:0.3,isTextBox:true,margin:0,fontFace:SANS,
  fontSize:10.5,bold:true,color:GOLD,charSpacing:2.6});
s.addText("Fix the fundamentals in number and algebra.\nTeach a pool of about 105 marks and work to 80.\nLeave the rest of the paper alone.",
  {x:M,y:1.45,w:11.2,h:2.2,isTextBox:true,margin:0,valign:"top",fontFace:SERIF,fontSize:28,color:CREAM,lineSpacing:44});
rule(s,M,4.05,6.2,"3A4E70");
s.addText("THIS WEEK",{x:M,y:4.35,w:4,h:0.3,isTextBox:true,margin:0,fontFace:SANS,
  fontSize:10.5,bold:true,color:GOLD,charSpacing:2.2});
const todo=[["1","Confirm the entry, tier and exam times with the school"],
            ["2","Run the fluency audit and the calculator setup in session one"],
            ["3","Sit the baseline paper at home, and set up the error log"]];
todo.forEach((t,i)=>{
  const y=4.78+i*0.58;
  badge(s,M,y,t[0],NAVYCARD,GOLD,0.38);
  s.addText(t[1],{x:M+0.55,y:y+0.04,w:8.5,h:0.3,isTextBox:true,margin:0,fontFace:SANS,
    fontSize:13,color:ONNAVY});
});
s.addText("Ali Tutors",{x:M,y:6.75,w:4,h:0.3,isTextBox:true,margin:0,fontFace:SERIF,
  fontSize:14,color:ONNAVYMUTE});

p.writeFile({fileName:"/tmp/claude-0/-home-user-Daily/1f1029ee-a03d-535a-b39f-f5f806492334/scratchpad/Charlotte_maths_plan.pptx"})
 .then(f=>console.log("written",f));
