# -*- coding: utf-8 -*-
"""High-level university application steps for Lantern."""

from reportlab.lib.colors import Color, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

NAVY = Color(0.043, 0.122, 0.227)
GOLD = Color(0.769, 0.639, 0.353)
INK = Color(0.12, 0.14, 0.18)
MUTED = Color(0.33, 0.36, 0.42)
CREAM = Color(0.976, 0.965, 0.925)

OUT = r"C:\Users\zamee\Desktop\Lantern-university-application-steps.pdf"


def styles():
    return {
        "h1": ParagraphStyle("h1", fontName="Times-Bold", fontSize=20, leading=24, textColor=NAVY, spaceAfter=2 * mm),
        "body": ParagraphStyle("body", fontName="Times-Roman", fontSize=10.5, leading=14, textColor=INK, spaceAfter=1.5 * mm),
        "small": ParagraphStyle("small", fontName="Times-Italic", fontSize=9, leading=12, textColor=MUTED, spaceBefore=2 * mm),
        "num": ParagraphStyle("num", fontName="Times-Bold", fontSize=12, leading=14, textColor=NAVY, alignment=1),
        "title": ParagraphStyle("title", fontName="Times-Bold", fontSize=11, leading=13, textColor=NAVY),
        "who": ParagraphStyle("who", fontName="Times-Bold", fontSize=9, leading=11, textColor=GOLD),
        "td": ParagraphStyle("td", fontName="Times-Roman", fontSize=9.5, leading=12.5, textColor=INK),
    }


S = styles()


def P(text, style="body"):
    return Paragraph(text, S[style])


def draw_lantern(canvas, x, y, s=1.0):
    canvas.saveState()
    canvas.setStrokeColor(GOLD)
    canvas.setFillColor(GOLD)
    canvas.setLineWidth(0.6)
    canvas.setLineCap(1)
    canvas.line(x, y + 3.6 * s * mm, x, y + 4.1 * s * mm)
    p = canvas.beginPath()
    p.moveTo(x - 0.7 * s * mm, y + 3.6 * s * mm)
    p.lineTo(x + 0.7 * s * mm, y + 3.6 * s * mm)
    p.lineTo(x + 0.35 * s * mm, y + 3.05 * s * mm)
    p.lineTo(x - 0.35 * s * mm, y + 3.05 * s * mm)
    p.close()
    canvas.drawPath(p, stroke=1, fill=0)
    canvas.roundRect(x - 0.75 * s * mm, y + 0.7 * s * mm, 1.5 * s * mm, 2.35 * s * mm, 0.2 * s * mm, stroke=1, fill=0)
    canvas.line(x, y + 0.7 * s * mm, x, y + 3.05 * s * mm)
    canvas.line(x - 0.75 * s * mm, y + 1.85 * s * mm, x + 0.75 * s * mm, y + 1.85 * s * mm)
    canvas.line(x - 0.85 * s * mm, y + 0.55 * s * mm, x + 0.85 * s * mm, y + 0.55 * s * mm)
    canvas.line(x, y + 0.15 * s * mm, x, y + 0.55 * s * mm)
    canvas.restoreState()


def header_footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setFillColor(NAVY)
    canvas.rect(0, h - 18 * mm, w, 18 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, h - 19.4 * mm, w, 1.4 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("Times-Bold", 11)
    draw_lantern(canvas, 20 * mm, h - 13.6 * mm, 1.15)
    canvas.drawString(24 * mm, h - 11 * mm, "LANTERN")
    canvas.setFont("Times-Roman", 8.5)
    canvas.drawRightString(w - 18 * mm, h - 10 * mm, "University application steps")
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, w, 14 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, 14 * mm, w, 1.2 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("Times-Roman", 8)
    canvas.drawString(18 * mm, 6 * mm, "WhatsApp  +49 155 6755 0791    |    zameer.ou@gmail.com")
    canvas.drawRightString(w - 18 * mm, 6 * mm, str(doc.page))
    canvas.restoreState()


def steps_table():
    rows = [
        ("1", "First message", "Customer", "The customer sends the highest qualification, marks, English or German level, the subject, and the intake. They also say Bachelor or Master."),
        ("2", "Choose the path", "Lantern", "We confirm Bachelor or Master. An Ausbildung is a company training application, so it does not follow these university steps."),
        ("3", "Check the profile", "Lantern", "We look at marks, language, study gaps, and budget. If the path is not realistic, we say so before any documents are prepared."),
        ("4", "Pay the fee", "Customer", "The one-time fee is 16000 rupees. It is paid once, before the written plan starts. University fees are separate."),
        ("5", "Shortlist", "Lantern", "We send 5 to 8 programmes that fit the profile, with the real deadline and the portal for each one. The university page decides the date."),
        ("6", "Document list", "Lantern", "We list what that programme asks for: passport, transcripts, language proof, CV, and motivation letter. Some countries also need APS. We check that rule for the customer's country."),
        ("7", "Review the writing", "Both", "The customer writes the CV and motivation letter in their own words. Lantern reads them and points out what is unclear."),
        ("8", "Submit the application", "Customer", "The customer creates the account and submits. Some universities use uni-assist. Others use their own portal. Lantern can guide the clicks on a call. Lantern does not keep the password."),
        ("9", "Check before the deadline", "Both", "We compare the uploaded file with the university list and name anything still missing. The customer uploads the missing item."),
        ("10", "Wait for the decision", "University", "The university accepts, rejects, or asks for more papers. Lantern cannot promise an offer."),
        ("11", "Open the visa file", "Both", "Only after a real admission letter do we open the embassy checklist. The visa step does not start from a shortlist."),
    ]
    data = []
    for num, title, who, text in rows:
        data.append([
            P(num, "num"),
            [P(title, "title"), P(who, "who"), P(text, "td")],
        ])
    table = Table(data, colWidths=[14 * mm, 156 * mm])
    cmds = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, -1), 1 * mm),
        ("RIGHTPADDING", (0, 0), (0, -1), 1 * mm),
        ("LEFTPADDING", (1, 0), (1, -1), 3 * mm),
        ("RIGHTPADDING", (1, 0), (1, -1), 3 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 2 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm),
        ("LINEBELOW", (0, 0), (-1, -2), 0.3, Color(0.82, 0.78, 0.68)),
        ("BACKGROUND", (0, 0), (0, -1), CREAM),
    ]
    table.setStyle(TableStyle(cmds))
    return table


def build():
    doc = SimpleDocTemplate(
        OUT,
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=26 * mm,
        bottomMargin=22 * mm,
        title="Lantern - university application steps",
        author="Lantern",
    )
    story = [
        P("How a university application proceeds"),
        P(
            "These are the high-level steps Lantern follows with a customer for a Bachelor or a Master in Germany. "
            "We do the steps in this order. We do not jump to the visa before there is an admission letter."
        ),
        Spacer(1, 2 * mm),
        steps_table(),
        P(
            "Lantern is not a university and not the embassy. The customer submits every application in their own name. "
            "The one-time guidance fee is 16000 rupees. The blocked account, visa fee, translations, and semester fees are paid by the customer to those offices.",
            "small",
        ),
    ]
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(OUT)


if __name__ == "__main__":
    build()
