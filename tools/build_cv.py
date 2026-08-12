from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether

OUT = "assets/Anthony_Bwembya_CV.pdf"
NAVY = colors.HexColor("#173B59")
TEAL = colors.HexColor("#278C91")
PALE = colors.HexColor("#F2F6F8")
INK = colors.HexColor("#263238")
MUTED = colors.HexColor("#60727D")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Name", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=24, leading=27, textColor=NAVY, alignment=TA_CENTER, spaceAfter=4))
styles.add(ParagraphStyle(name="Tagline", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10, leading=13, textColor=TEAL, alignment=TA_CENTER, spaceAfter=6))
styles.add(ParagraphStyle(name="Contact", parent=styles["Normal"], fontSize=8.4, leading=11, textColor=MUTED, alignment=TA_CENTER, spaceAfter=10))
styles.add(ParagraphStyle(name="Section", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=12, leading=15, textColor=NAVY, spaceBefore=10, spaceAfter=6, borderWidth=0, borderColor=TEAL, borderPadding=0))
styles.add(ParagraphStyle(name="Role", parent=styles["Heading3"], fontName="Helvetica-Bold", fontSize=10.2, leading=13, textColor=NAVY, spaceAfter=2))
styles.add(ParagraphStyle(name="Meta", parent=styles["Normal"], fontName="Helvetica-Oblique", fontSize=8.6, leading=11, textColor=MUTED, spaceAfter=4))
styles.add(ParagraphStyle(name="BodyCV", parent=styles["BodyText"], fontSize=9.1, leading=12.3, textColor=INK, spaceAfter=5))
styles.add(ParagraphStyle(name="BulletCV", parent=styles["BodyText"], fontSize=8.9, leading=12, leftIndent=11, firstLineIndent=-7, bulletIndent=3, textColor=INK, spaceAfter=3))
styles.add(ParagraphStyle(name="Skill", parent=styles["BodyText"], fontSize=8.8, leading=11.5, textColor=INK))

def header(story):
    story += [Paragraph("ANTHONY BWEMBYA", styles["Name"]),
              Paragraph("SENSOR SYSTEMS | SCIENTIFIC COMPUTING | AI & DATA", styles["Tagline"]),
              Paragraph("Netherlands  ·  anthonybwembya@gmail.com  ·  +31 6 8406 8779  ·  linkedin.com/in/anthony-bwembya  ·  github.com/abwembya", styles["Contact"])]

def section(story, title):
    story.append(Paragraph(title.upper(), styles["Section"]))
    story.append(Table([[""]], colWidths=[174*mm], rowHeights=[0.7*mm], style=TableStyle([("BACKGROUND",(0,0),(-1,-1),TEAL)])))
    story.append(Spacer(1, 3))

def bullets(story, items):
    for item in items:
        story.append(Paragraph("• " + item, styles["BulletCV"]))

def role(story, title, meta, items):
    block=[Paragraph(title, styles["Role"]), Paragraph(meta, styles["Meta"])]
    for item in items: block.append(Paragraph("• " + item, styles["BulletCV"]))
    story.append(KeepTogether(block))
    story.append(Spacer(1,4))

doc=SimpleDocTemplate(OUT, pagesize=A4, rightMargin=18*mm, leftMargin=18*mm, topMargin=14*mm, bottomMargin=15*mm,
                      title="Anthony Bwembya - CV", author="Anthony Bwembya")
story=[]
header(story)
section(story,"Professional profile")
story.append(Paragraph("Experimental physicist and sensor-data specialist with experience developing, calibrating and validating complex radio, optical and detector-based measurement systems. Strong background in Python/C++ scientific software, signal reconstruction, sensor-response modelling, uncertainty analysis, automated quality control and machine learning for physical measurements. Combines hands-on instrumentation with reproducible, data-driven analysis.", styles["BodyCV"]))

section(story,"Core competencies")
skills=[
    ("Scientific programming & data", "Python, C++, Bash, SQL, NumPy, SciPy, pandas, Matplotlib, Jupyter, Linux, Git, HPC/SLURM"),
    ("Machine learning & AI", "PyTorch, scikit-learn, feature engineering, classification, regression, clustering, anomaly detection and model validation"),
    ("Signal processing", "RF processing, Fourier and spectral analysis, phase calibration, timing synchronisation, coherent reconstruction and noise modelling"),
    ("Sensors & instrumentation", "Antenna arrays, detector calibration, LiDAR, fluorescence telescopes, PMTs, radiation detectors, DAQ and RF/DC chains"),
    ("Modelling & quality", "Statistical inference, uncertainty propagation, CORSIKA/CoREAS, GALPROP, model-to-data comparison and automated quality control"),
    ("Collaboration & delivery", "Technical documentation, scientific communication, stakeholder engagement, teaching, mentoring, safety and field operations"),
]
data=[]
for title, body in skills:
    data.append([Paragraph(f"<b>{title}</b><br/>{body}",styles["Skill"])])
t=Table(data,colWidths=[174*mm],rowHeights=None,spaceBefore=2)
t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),PALE),("BOX",(0,0),(-1,-1),0.45,colors.HexColor('#D8E3E8')),("INNERGRID",(0,0),(-1,-1),0.35,colors.HexColor('#D8E3E8')),("LEFTPADDING",(0,0),(-1,-1),7),("RIGHTPADDING",(0,0),(-1,-1),7),("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5)]))
story.append(t)

section(story,"Professional experience")
role(story,"Sensor Development, Calibration and Intelligent Data Processing","Radboud University / Pierre Auger Observatory · Netherlands / Argentina · 2021–2026",[
"Developed precision calibration and synchronisation methods for a distributed detector array, achieving nanosecond-level timing alignment across autonomous stations.",
"Built Python and C++ workflows for waveform processing, spectral analysis, feature extraction, reconstruction, sensor diagnostics and automated quality control.",
"Designed network-level consistency tests to identify anomalous sensors, timing drift, geometry errors, ambiguous solutions and inconsistent measurements.",
"Modelled wave propagation, detector geometry, atmospheric refractivity and antenna response to validate reconstructed events against physical expectations.",
"Developed coherent interferometric reconstruction methods for weak signals, culminating in the first successful reconstruction of a highly inclined event with AugerPrime radio-detector data.",
"Supported LiDAR and fluorescence-detector calibration and operations, including atmospheric monitoring and detector-performance assessment."])

story.append(PageBreak())
section(story,"Professional experience continued")
role(story,"Research & Technical Officer - Radiation Measurements and Instrumentation","Radiation Protection Authority, Zambia · 2021–2022",[
"Performed radiation and spectroscopic measurements, instrument checks, detector calibration, sample preparation, spectral interpretation and technical reporting.",
"Investigated anomalous readings, evaluated measurement uncertainty, and supported field inspections and compliance documentation."])
role(story,"Teaching Assistant - Machine Learning, Physics & Scientific Computing","Radboud University · 2021–2025",[
"Supported teaching in machine learning for particle physics and astrophysics, experimental physics, scientific programming and data interpretation.",
"Guided students in model evaluation, feature-based analysis, uncertainty, Python workflows and technical communication."])
role(story,"Research Intern - Radiation Detection and Materials Analysis","National Institute for Scientific and Industrial Research, Zambia · 2017",[
"Performed alpha/gamma spectroscopy, X-ray fluorescence measurements, sample preparation and laboratory calibration."])

section(story,"Education")
role(story,"Doctoral Research in High-Energy Physics","Radboud University, Netherlands · 2021–2026",["Thesis: <i>In Phase With the Cosmos: Mass Composition of Cosmic Rays via Radio Interferometry</i>. Thesis completed and approved for defence."])
role(story,"MSc, Nuclear Physics and Technology","National Research Nuclear University MEPhI, Russia · 2018–2021",["Investigated the high-energy positron excess using PAMELA and AMS-02 observations with GALPROP propagation modelling."])
role(story,"BSc, Physics","University of Zambia · 2013–2017",["Broad foundation in mechanics, electromagnetism, quantum mechanics, statistical physics, electronics, solid-state physics, renewable energy and computational physics."])

section(story,"Languages")
lang_data=[
[Paragraph("<b>English</b><br/>Fluent - international working language",styles["Skill"]),Paragraph("<b>Bemba</b><br/>Native",styles["Skill"])],
[Paragraph("<b>Nyanja</b><br/>Native",styles["Skill"]),Paragraph("<b>Russian</b><br/>Professional working level",styles["Skill"])],
[Paragraph("<b>Dutch</b><br/>Developing",styles["Skill"]),Paragraph("<b>Work eligibility</b><br/>No visa sponsorship required in the Netherlands",styles["Skill"])] ]
lt=Table(lang_data,colWidths=[87*mm,87*mm])
lt.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),PALE),("BOX",(0,0),(-1,-1),.4,colors.HexColor('#D8E3E8')),("INNERGRID",(0,0),(-1,-1),.35,colors.HexColor('#D8E3E8')),("PADDING",(0,0),(-1,-1),7)]))
story.append(lt)

def footer(canvas, doc):
    canvas.saveState(); canvas.setFont("Helvetica",8); canvas.setFillColor(MUTED)
    canvas.drawCentredString(A4[0]/2,8*mm,f"Anthony Bwembya · CV · Page {doc.page}")
    canvas.restoreState()

doc.build(story,onFirstPage=footer,onLaterPages=footer)
