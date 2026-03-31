import re
from pathlib import Path
from xml.sax.saxutils import escape

from pypdf import PdfReader
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Flowable, PageBreak, Paragraph, Preformatted, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "final-project-report.md"
TARGET = ROOT / "final-project-report.pdf"
TEMP_TARGET = ROOT / "_temp_report_for_toc.pdf"
TOC_PAGE_COUNT = 2


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
            fontSize=24,
            leading=30,
            alignment=TA_CENTER,
            spaceAfter=18,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverSubtitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=22,
            alignment=TA_CENTER,
            spaceAfter=24,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverMetaLabel",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=12.8,
            leading=17,
            alignment=TA_CENTER,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverMetaValue",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=12.8,
            leading=17,
            alignment=TA_CENTER,
            spaceAfter=10,
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
    styles.add(
        ParagraphStyle(
            name="TOCTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=21,
            leading=25,
            alignment=TA_CENTER,
            spaceAfter=16,
        )
    )
    return styles


def build_doc(path: Path):
    return SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=1.9 * cm,
        rightMargin=1.9 * cm,
        topMargin=1.6 * cm,
        bottomMargin=1.5 * cm,
        title="RSS Feed Reader Project Using Git and GitHub",
        author="Tan Phat",
    )


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


def cover_label_and_value(text: str):
    if ":" not in text:
        return None, None
    label, value = text.split(":", 1)
    return label.strip() + ":", value.strip()


def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    canvas.drawRightString(A4[0] - 1.7 * cm, 1.0 * cm, f"Page {doc.page}")
    canvas.restoreState()


class TOCList(Flowable):
    LEVELS = {
        0: {"font": "Helvetica", "size": 11.8, "leading": 16.5, "indent": 0},
        1: {"font": "Helvetica", "size": 12.2, "leading": 16, "indent": 16},
        2: {"font": "Helvetica", "size": 11.5, "leading": 14.5, "indent": 32},
    }

    def __init__(self, entries):
        super().__init__()
        self.entries = entries
        self._height = sum(self.LEVELS[level]["leading"] for level, _, _ in entries) + 8

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        return availWidth, self._height

    def draw(self):
        canvas = self.canv
        y = self._height - 4
        for level, text, page in self.entries:
            conf = self.LEVELS[level]
            font_name = conf["font"]
            font_size = conf["size"]
            leading = conf["leading"]
            indent = conf["indent"]
            page_text = str(page)

            y -= leading
            canvas.setFont(font_name, font_size)

            text_width = canvas.stringWidth(text, font_name, font_size)
            page_width = canvas.stringWidth(page_text, font_name, font_size)
            page_x = self.width - page_width
            text_x = indent
            dots_x = text_x + text_width + 6
            dots_width = max(0, page_x - dots_x - 6)
            dot_width = max(canvas.stringWidth(".", font_name, font_size), 1)
            dot_count = max(0, int(dots_width / dot_width))

            canvas.drawString(text_x, y, text)
            if dot_count > 0:
                canvas.drawString(dots_x, y, "." * dot_count)
            canvas.drawString(page_x, y, page_text)


def normalize_text(text: str) -> str:
    return " ".join(text.split()).strip().lower()


def display_text_for_heading(text: str) -> str:
    if text.startswith("CHAPTER "):
        chapter_match = re.match(r"CHAPTER\s+(\d+):\s+(.+)", text)
        if chapter_match:
            heading_title = chapter_match.group(2)
            if chapter_match.group(1) == "3":
                heading_title = "APPLYING GIT AND GITHUB TO MANAGE SOURCE CODE"
            return f"Chapter {chapter_match.group(1)}. {heading_title}"
    if text.startswith("APPENDIX "):
        appendix_match = re.match(r"APPENDIX\s+([A-Z]):\s+(.+)", text)
        if appendix_match:
            return f"Appendix {appendix_match.group(1)}. {appendix_match.group(2).title()}"
    if text == "REFERENCES":
        return "References"
    return text


def collect_toc_entries(source_text: str):
    entries = []
    for raw_line in source_text.splitlines():
        line = raw_line.strip()
        if line.startswith("# "):
            text = line[2:].strip()
            if text.startswith("CHAPTER ") or text == "REFERENCES" or text.startswith("APPENDIX "):
                entries.append((0, display_text_for_heading(text), text))
        elif line.startswith("## "):
            text = line[3:].strip()
            if re.match(r"^\d+\.\d+\s+", text):
                entries.append((1, text, text))
        elif line.startswith("### "):
            text = line[4:].strip()
            if re.match(r"^\d+\.\d+\.\d+\s+", text):
                entries.append((2, text, text))
    return entries


def split_toc_entries(entries):
    split_index = 0
    for index, entry in enumerate(entries):
        if entry[1].startswith("Chapter 3."):
            split_index = index
            break
    if split_index == 0:
        split_index = max(1, len(entries) // 2)
    return entries[:split_index], entries[split_index:]


def locate_heading_pages(pdf_path: Path, entries):
    reader = PdfReader(str(pdf_path))
    page_map = {}
    for _, _, search_text in entries:
        needle = normalize_text(search_text)
        for page_number, page in enumerate(reader.pages, start=1):
            if page_number <= 5:
                continue
            raw_lines = (page.extract_text() or "").splitlines()
            normalized_lines = [normalize_text(line) for line in raw_lines if normalize_text(line)]
            line_pairs = [
                normalize_text(normalized_lines[i] + " " + normalized_lines[i + 1])
                for i in range(len(normalized_lines) - 1)
            ]
            if any(line == needle or line.startswith(needle) for line in normalized_lines):
                page_map[search_text] = page_number
                break
            if any(pair == needle or pair.startswith(needle) for pair in line_pairs):
                page_map[search_text] = page_number
                break
        if search_text not in page_map:
            raise ValueError(f"Could not locate heading in PDF: {search_text}")
    return page_map


def parse_markdown(source_text: str, styles, toc_mode="manual", toc_pages=None):
    story = []
    lines = source_text.splitlines()
    paragraph_buffer = []
    in_code_block = False
    code_lines = []
    cover_done = False
    skip_manual_toc = False

    def flush_paragraph():
        nonlocal paragraph_buffer, cover_done
        if not paragraph_buffer:
            return
        text = " ".join(item.strip() for item in paragraph_buffer).strip()
        paragraph_buffer = []
        if not text:
            return
        if not cover_done and text.upper() == "FINAL PROJECT REPORT":
            story.append(Spacer(1, 4.2 * cm))
            story.append(Paragraph(format_inline(text), styles["CoverTitle"]))
        elif not cover_done and text.startswith("## RSS Feed Reader Project Using Git and GitHub"):
            story.append(Paragraph(format_inline(text.replace("## ", "")), styles["CoverSubtitle"]))
        elif not cover_done:
            label, value = cover_label_and_value(text)
            if label and value:
                story.append(Paragraph(format_inline(label), styles["CoverMetaLabel"]))
                story.append(Paragraph(format_inline(value), styles["CoverMetaValue"]))
            else:
                story.append(Paragraph(format_inline(text), styles["CoverMetaValue"]))
        else:
            story.append(Paragraph(format_inline(text), styles["BodyProject"]))

    for raw_line in lines:
        line = raw_line.rstrip()

        if skip_manual_toc:
            if line.strip() == r"\newpage":
                skip_manual_toc = False
                cover_done = True
            continue

        if line.strip().startswith("```"):
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

        if line.startswith("## Table of Contents"):
            flush_paragraph()
            if toc_mode == "placeholder":
                story.append(Paragraph("TABLE OF CONTENTS", styles["TOCTitle"]))
                story.append(Spacer(1, 12 * cm))
                story.append(PageBreak())
                story.append(Spacer(1, 18 * cm))
                story.append(PageBreak())
            else:
                page_one_entries, page_two_entries = toc_pages
                story.append(Paragraph("TABLE OF CONTENTS", styles["TOCTitle"]))
                story.append(TOCList(page_one_entries))
                story.append(PageBreak())
                story.append(TOCList(page_two_entries))
                story.append(PageBreak())
            skip_manual_toc = True
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
            story.append(Paragraph(format_inline("&bull; " + line[2:]), styles["BulletProject"]))
            continue

        if line[:2].isdigit() and line[2:4] in [". ", ") "]:
            flush_paragraph()
            story.append(Paragraph(format_inline(line), styles["BulletProject"]))
            continue

        paragraph_buffer.append(line)

    flush_paragraph()
    return story


def build_pdf(path: Path, story):
    doc = build_doc(path)
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


def main():
    styles = build_styles()
    source_text = SOURCE.read_text(encoding="utf-8")
    heading_entries = collect_toc_entries(source_text)

    placeholder_story = parse_markdown(source_text, styles, toc_mode="placeholder")
    build_pdf(TEMP_TARGET, placeholder_story)

    page_map = locate_heading_pages(TEMP_TARGET, heading_entries)
    final_entries = [(level, display_text, page_map[search_text]) for level, display_text, search_text in heading_entries]
    toc_pages = split_toc_entries(final_entries)

    final_story = parse_markdown(source_text, styles, toc_mode="manual", toc_pages=toc_pages)
    build_pdf(TARGET, final_story)

    if TEMP_TARGET.exists():
        TEMP_TARGET.unlink()


if __name__ == "__main__":
    main()
