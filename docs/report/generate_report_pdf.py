from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Preformatted, SimpleDocTemplate, Spacer, PageBreak


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "final-project-report.md"
TARGET = ROOT / "final-project-report.pdf"


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="BodyProject",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=12.9,
            leading=17.8,
            alignment=TA_JUSTIFY,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Heading1Project",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=22,
            spaceBefore=8,
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Heading2Project",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=15,
            leading=19,
            spaceBefore=6,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Heading3Project",
            parent=styles["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=16,
            spaceBefore=4,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=23,
            leading=28,
            alignment=TA_CENTER,
            spaceAfter=14,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BulletProject",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=12.6,
            leading=17.2,
            leftIndent=18,
            firstLineIndent=-10,
            spaceAfter=5,
        )
    )
    return styles


def format_inline(text: str) -> str:
    escaped = escape(text)
    parts = escaped.split("`")
    if len(parts) == 1:
        return escaped
    chunks = []
    for idx, part in enumerate(parts):
        if idx % 2 == 1:
            chunks.append(f"<font name='Courier'>{part}</font>")
        else:
            chunks.append(part)
    return "".join(chunks)


def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    canvas.drawRightString(A4[0] - 1.7 * cm, 1.0 * cm, f"Page {doc.page}")
    canvas.restoreState()


def parse_markdown(source_text: str, styles):
    story = []
    lines = source_text.splitlines()
    paragraph_buffer = []
    in_code_block = False
    code_lines = []
    cover_done = False

    def flush_paragraph():
        nonlocal paragraph_buffer, cover_done
        if not paragraph_buffer:
            return
        text = " ".join(item.strip() for item in paragraph_buffer).strip()
        paragraph_buffer = []
        if not text:
            return
        style = styles["BodyProject"]
        if not cover_done and text.upper() == "FINAL PROJECT REPORT":
            story.append(Spacer(1, 5 * cm))
            story.append(Paragraph(format_inline(text), styles["CoverTitle"]))
        elif not cover_done and text.startswith("## RSS Feed Reader Project Using Git and GitHub"):
            story.append(Paragraph(format_inline(text.replace("## ", "")), styles["Heading2Project"]))
        else:
            story.append(Paragraph(format_inline(text), style))

    for raw_line in lines:
        line = raw_line.rstrip()

        if line.strip() == "```":
            if in_code_block:
                story.append(
                    Preformatted(
                        "\n".join(code_lines),
                        ParagraphStyle(
                            "CodeProject",
                            fontName="Courier",
                            fontSize=10.2,
                            leading=13,
                            leftIndent=12,
                            rightIndent=12,
                            spaceBefore=4,
                            spaceAfter=8,
                        ),
                    )
                )
                code_lines = []
                in_code_block = False
            else:
                flush_paragraph()
                in_code_block = True
            continue

        if in_code_block:
            code_lines.append(line)
            continue

        if line.strip() == r"\newpage":
            flush_paragraph()
            story.append(PageBreak())
            cover_done = True
            continue

        if not line.strip():
            flush_paragraph()
            story.append(Spacer(1, 0.15 * cm))
            continue

        if line.startswith("# "):
            flush_paragraph()
            story.append(Paragraph(format_inline(line[2:]), styles["Heading1Project"]))
            continue

        if line.startswith("## "):
            flush_paragraph()
            story.append(Paragraph(format_inline(line[3:]), styles["Heading2Project"]))
            continue

        if line.startswith("### "):
            flush_paragraph()
            story.append(Paragraph(format_inline(line[4:]), styles["Heading3Project"]))
            continue

        if line.startswith("- "):
            flush_paragraph()
            story.append(Paragraph(format_inline("• " + line[2:]), styles["BulletProject"]))
            continue

        if line[:2].isdigit() and line[2:4] in [". ", ") "]:
            flush_paragraph()
            story.append(Paragraph(format_inline(line), styles["BulletProject"]))
            continue

        paragraph_buffer.append(line)

    flush_paragraph()
    return story


def main():
    styles = build_styles()
    source_text = SOURCE.read_text(encoding="utf-8")
    story = parse_markdown(source_text, styles)

    doc = SimpleDocTemplate(
        str(TARGET),
        pagesize=A4,
        leftMargin=1.9 * cm,
        rightMargin=1.9 * cm,
        topMargin=1.6 * cm,
        bottomMargin=1.5 * cm,
        title="RSS Feed Reader Project Using Git and GitHub",
        author="Tan Phat",
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    main()
