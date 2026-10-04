# -*- coding: utf-8 -*-
"""Customer plan: Lantern, one-time fee 16000 rupees."""

from reportlab.lib.colors import Color, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable,
)

NAVY = Color(0.043, 0.122, 0.227)
GOLD = Color(0.769, 0.639, 0.353)
INK = Color(0.12, 0.14, 0.18)
MUTED = Color(0.33, 0.36, 0.42)
CREAM = Color(0.976, 0.965, 0.925)

OUT = r"C:\Users\zamee\Desktop\Study-in-Germany-customer-plan.pdf"


def styles():
    return {
        "h1": ParagraphStyle("h1", fontName="Times-Bold", fontSize=22, leading=26, textColor=NAVY, spaceAfter=2 * mm),
        "h2": ParagraphStyle("h2", fontName="Times-Bold", fontSize=14, leading=18, textColor=NAVY, spaceBefore=4 * mm, spaceAfter=2 * mm),
        "h3": ParagraphStyle("h3", fontName="Times-Bold", fontSize=11.5, leading=14, textColor=NAVY, spaceBefore=2 * mm, spaceAfter=1 * mm),
        "body": ParagraphStyle("body", fontName="Times-Roman", fontSize=10.5, leading=14.5, textColor=INK, spaceAfter=1.6 * mm),
        "item": ParagraphStyle("item", fontName="Times-Roman", fontSize=10.5, leading=14.5, textColor=INK, leftIndent=4 * mm, spaceAfter=1.2 * mm),
        "small": ParagraphStyle("small", fontName="Times-Italic", fontSize=9, leading=12, textColor=MUTED, spaceAfter=1.5 * mm),
        "th": ParagraphStyle("th", fontName="Times-Bold", fontSize=9, leading=11.5, textColor=white),
        "td": ParagraphStyle("td", fontName="Times-Roman", fontSize=9, leading=12, textColor=INK),
        "tdbold": ParagraphStyle("tdbold", fontName="Times-Bold", fontSize=9.5, leading=12, textColor=NAVY),
    }


S = styles()


def P(text, style="body"):
    return Paragraph(text, S[style])


def bullets(items):
    return [P("-  " + item, "item") for item in items]


def callout(title, text):
    data = [[P("<b>%s</b>" % title, "h3")], [P(text)]]
    t = Table(data, colWidths=[170 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CREAM),
        ("BOX", (0, 0), (-1, -1), 1.2, GOLD),
        ("LEFTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("TOPPADDING", (0, 0), (-1, 0), 2.5 * mm),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 2.5 * mm),
        ("TOPPADDING", (0, 1), (-1, 1), 0),
    ]))
    return t


def draw_lantern(canvas, x, y, s=1.0):
    """Gold street-lantern outline. x, y is the bottom center. s matches letter height."""
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
    canvas.drawRightString(w - 18 * mm, h - 10 * mm, "Bachelor  |  Master  |  Ausbildung")
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, w, 14 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, 14 * mm, w, 1.2 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("Times-Roman", 8)
    canvas.drawString(18 * mm, 6 * mm, "WhatsApp  +49 155 6755 0791    |    zameer.ou@gmail.com")
    canvas.drawRightString(w - 18 * mm, 6 * mm, str(doc.page))
    canvas.restoreState()


def path_table():
    header = [P("Path", "th"), P("What it is", "th"), P("What we look at", "th")]
    rows = [
        ("Bachelor", "A first university degree, usually after school.", "Your school marks, the language of the programme, and whether you need a foundation year or Studienkolleg."),
        ("Master", "A second university degree, after a Bachelor.", "Your Bachelor subject and marks, the language, and whether your degree matches the Master you want."),
        ("Ausbildung", "Vocational training with a company in Germany. You learn a trade and often earn a training salary.", "Your school level, German language, and the training occupation you want. Most Ausbildung places expect German."),
    ]
    data = [header]
    for a, b, c in rows:
        data.append([P(a, "tdbold"), P(b, "td"), P(c, "td")])
    t = Table(data, colWidths=[32 * mm, 58 * mm, 80 * mm], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("BACKGROUND", (0, 1), (-1, 1), CREAM),
        ("BACKGROUND", (0, 2), (-1, 2), white),
        ("BACKGROUND", (0, 3), (-1, 3), CREAM),
        ("GRID", (0, 0), (-1, -1), 0.3, Color(0.75, 0.72, 0.64)),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 2.2 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2.2 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 1.8 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.8 * mm),
    ]))
    return t


def build():
    doc = SimpleDocTemplate(
        OUT,
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=26 * mm,
        bottomMargin=22 * mm,
        title="Lantern - one-time fee 16000 rupees",
        author="Lantern",
    )
    story = []
    story.append(P("Lantern", "h1"))
    story.append(P("Bachelor, Master, and Ausbildung in Germany", "h2"))
    story.append(P(
        "Lantern helps students who want to study or train in Germany. "
        "The name means a light that shows you the path. "
        "I am a student in Germany myself. I have already gone through the real steps. "
        "I will help you see which path fits you: a Bachelor, a Master, or an Ausbildung. "
        "The fee is one time, because I help students directly, not through a large agency."
    ))
    story.append(Spacer(1, 1.5 * mm))
    story.append(callout(
        "One-time fee: 16000 rupees",
        "You pay 16000 rupees once. That fee covers one full guidance for the path you choose: "
        "Bachelor, Master, or Ausbildung. There is no second package fee. "
        "You pay this fee to Lantern. University fees, the blocked account, the visa fee, "
        "translations, and language tests are separate. You pay those to the university, the bank, or the embassy.",
    ))
    story.append(Spacer(1, 2 * mm))
    story.append(callout(
        "Please read this before you pay",
        "Lantern is not a law firm, and I do not work for the embassy or for a university. "
        "I cannot promise that a university or a training company will accept you, and I cannot promise a visa. "
        "Those decisions belong to them and to the embassy. "
        "What I can do is make your path clearer and your documents complete and honest.",
    ))

    story.append(P("The three paths", "h2"))
    story.append(path_table())
    story.append(Spacer(1, 2 * mm))
    story.append(P(
        "On the first message, tell me which path you want. If you are not sure, I will say which of the three is realistic for your marks, language, and age.",
        "small",
    ))

    story.append(P("What the 16000 rupees includes", "h2"))
    story.extend(bullets([
        "A check of your qualification, marks, language, and budget.",
        "A clear recommendation: Bachelor, Master, or Ausbildung.",
        "A written shortlist for that path, with deadlines and the documents each place asks for.",
        "The order of steps, from application to the visa checklist on the embassy website.",
        "Feedback on your CV and a short motivation letter, so they sound like you.",
        "A simple explanation of the blocked account and the costs you still pay yourself.",
        "Answers to your questions about that one path, by WhatsApp, until your application set for that path is ready to submit.",
    ]))

    story.append(P("What the 16000 rupees does not include", "h2"))
    story.extend(bullets([
        "The blocked account. For a student visa, the figure widely used for 2026 is 11,904 euro for 12 months, which is 992 euro a month. We confirm the exact number on your embassy website before you transfer any money. An Ausbildung can use a different money proof. We check the rule for your case.",
        "Semester fees. Many public universities charge no tuition, but they charge a semester contribution, often about 100 to 400 euro. In Baden-Wurttemberg, non-EU students usually pay about 1,500 euro tuition per semester.",
        "The visa fee, health insurance, translations, a language test, or a uni-assist fee.",
        "A second path. If you later change from Bachelor to Master, or from university to Ausbildung, that is a new guidance.",
        "A promise of admission or a visa.",
    ]))

    story.append(P("How we work", "h2"))
    story.extend(bullets([
        "Message Lantern on WhatsApp. Send your highest qualification, your marks, your English or German level, and whether you want a Bachelor, a Master, or an Ausbildung.",
        "I reply and we confirm that I can help. The 16000 rupees is paid once, before I write your plan.",
        "If you cancel before I start, I return the 16000 rupees. If the written plan is already done, the fee stays paid.",
        "You submit every application in your own name. I guide you. I do not keep your university or company password.",
    ]))

    story.append(P("The path we follow", "h2"))
    story.extend(bullets([
        "<b>1. Your profile.</b> Qualification, marks, any study gap, and language.",
        "<b>2. The right path.</b> Bachelor, Master, or Ausbildung. We do not mix them.",
        "<b>3. Your budget.</b> The money you show must be real.",
        "<b>4. A list.</b> University programmes, or Ausbildung occupations, that match you.",
        "<b>5. Applications.</b> Universities may use uni-assist or their own portal. Ausbildung applications usually go to the training company.",
        "<b>6. Offer first.</b> We open the visa checklist only after you have a real admission or a real Ausbildung contract.",
        "<b>7. After you arrive.</b> Register your address, sort health insurance, and enrol or start the training.",
    ]))

    story.append(Spacer(1, 2 * mm))
    story.append(HRFlowable(width="100%", thickness=0.6, color=GOLD, spaceAfter=3 * mm))
    story.append(P("Start here", "h2"))
    story.append(callout(
        "Message Lantern",
        "WhatsApp +49 155 6755 0791, or email zameer.ou@gmail.com. "
        "Write Bachelor, Master, or Ausbildung, plus your qualification, your marks, and your language level. "
        "The guidance fee is 16000 rupees, one time.",
    ))
    story.append(P(
        "Lantern. Updated 4 October 2026. The one-time fee is 16000 rupees. "
        "Blocked-account and university fee figures must be checked again on the official page before you pay those offices.",
        "small",
    ))
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(OUT)


if __name__ == "__main__":
    build()
