#!/usr/bin/env python3
"""Render the accompanying Markdown statement to a one-page PDF.

Usage: python build_pi_statement.py [statement.md] [statement.pdf]
Requires reportlab, pypdf, and Liberation Serif or DejaVu Serif TrueType fonts.
"""

from __future__ import annotations

import html
from pathlib import Path
import re
import sys

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate


def inline(markdown: str) -> str:
    """Convert the limited inline Markdown used by this statement."""
    text = html.escape(markdown)
    text = re.sub(
        r"\[([^\]]+)\]\((https?://[^\s)]+)\)",
        lambda m: f'<link href="{m.group(2)}"><u>{m.group(1)}</u></link>',
        text,
    )
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    return text


def render(source: Path, output: Path) -> None:
    font_sets = [
        (Path("/usr/share/fonts/truetype/liberation"), "LiberationSerif"),
        (Path("/usr/share/fonts/truetype/liberation2"), "LiberationSerif"),
        (Path("/usr/share/fonts/truetype/dejavu"), "DejaVuSerif"),
    ]
    variants = {"": "", "-Bold": "-Bold", "-Italic": "-Italic", "-BoldItalic": "-BoldItalic"}
    for directory, family in font_sets:
        paths = {name: directory / f"{family}{suffix}.ttf" for name, suffix in variants.items()}
        # DejaVu names its regular face without a suffix; Liberation uses -Regular.
        if family == "LiberationSerif":
            paths[""] = directory / f"{family}-Regular.ttf"
        if all(path.is_file() for path in paths.values()):
            for suffix, path in paths.items():
                pdfmetrics.registerFont(TTFont("StatementSerif" + suffix, str(path)))
            break
    else:
        raise RuntimeError("Install Liberation Serif or DejaVu Serif TrueType fonts")
    pdfmetrics.registerFontFamily(
        "StatementSerif", normal="StatementSerif", bold="StatementSerif-Bold",
        italic="StatementSerif-Italic", boldItalic="StatementSerif-BoldItalic"
    )
    base = dict(fontName="StatementSerif", textColor=colors.black, alignment=TA_LEFT)
    styles = {
        "title": ParagraphStyle(
            "title", **base, fontSize=16, leading=19, spaceAfter=8
        ),
        "metadata": ParagraphStyle(
            "metadata", **base, fontSize=10.5, leading=12.5, spaceAfter=8
        ),
        "heading": ParagraphStyle(
            "heading", **base, fontSize=11.3, leading=14,
            spaceBefore=7, spaceAfter=4, keepWithNext=True
        ),
        "body": ParagraphStyle(
            "body", **base, fontSize=11.3, leading=14.1, spaceAfter=7
        ),
        "references": ParagraphStyle(
            "references", **base, fontSize=9.3, leading=11.5, spaceAfter=3
        ),
    }
    blocks = source.read_text(encoding="utf-8").strip().split("\n\n")
    story = []
    in_references = False
    for index, block in enumerate(blocks):
        if block.startswith("# "):
            story.append(Paragraph("<b>" + inline(block[2:]) + "</b>", styles["title"]))
        elif block.startswith("## "):
            heading = block[3:]
            in_references = heading == "Selected work and evidence"
            story.append(Paragraph("<b>" + inline(heading) + "</b>", styles["heading"]))
        elif index == 1:
            metadata = "<br/>".join(inline(line.rstrip()) for line in block.splitlines())
            story.append(Paragraph(metadata, styles["metadata"]))
        else:
            key = "references" if in_references else "body"
            story.append(Paragraph(inline(" ".join(block.splitlines())), styles[key]))
    output.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(
        str(output), pagesize=letter,
        rightMargin=61.2, leftMargin=61.2, topMargin=54, bottomMargin=54,
        title="Research Achievements and Future Impact - Xinya Du",
        author="Xinya Du",
        subject="ONR FY2027 YIP: past achievements and significance of proposed research",
        pageCompression=1,
    )
    document.build(story)
    reader = PdfReader(output)
    if len(reader.pages) != 1:
        raise ValueError(f"Expected one page; rendered {len(reader.pages)} pages")
    print(f"Created {output} ({len(reader.pages)} page)")


if __name__ == "__main__":
    default = Path(__file__).with_name("pi_achievements_and_research_significance.md")
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else default
    output = Path(sys.argv[2]) if len(sys.argv) > 2 else source.with_suffix(".pdf")
    render(source, output)
