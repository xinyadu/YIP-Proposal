#!/usr/bin/env python3
"""Build the vector peer-weighting figure and its PNG preview.

Requires PyMuPDF, pdflatex, and standard LaTeX packages including TikZ.
"""
from pathlib import Path
import subprocess
import re
import fitz

root = Path(__file__).resolve().parent
icons = root / "model_icons"
for source, target in [
    ("openai.svg", "openai.pdf"),
    ("claude-color.svg", "claude.pdf"),
    ("gemini-color.svg", "gemini.pdf"),
]:
    svg = (icons / source).read_text().replace("1em", "24px")
    svg = svg.replace("currentColor", "#177c68")
    if source.startswith("gemini"):
        # A solid-blue variant remains legible in PDF engines without SVG gradients.
        svg = re.sub(r'fill="url\(#[^\)]+\)"', 'fill="#4285F4"', svg)
    with fitz.open(stream=svg.encode(), filetype="svg") as icon:
        (icons / target).write_bytes(icon.convert_to_pdf())
result = subprocess.run(
    ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "peer_weighting_loop.tex"],
    cwd=root, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
)
if result.returncode:
    print(result.stdout[-12000:])
    raise SystemExit(result.returncode)
with fitz.open(root / "peer_weighting_loop.pdf") as figure:
    if len(figure) != 1:
        raise ValueError("The figure must occupy one page")
    figure[0].get_pixmap(matrix=fitz.Matrix(3, 3)).save(root / "peer_weighting_loop.png")
print("Built peer_weighting_loop.pdf and peer_weighting_loop.png")
