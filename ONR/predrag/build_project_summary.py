"""Build project-summary.tex and project-summary.pdf from the text in project-summary.md.

Usage (from ONR/predrag): python3 build_project_summary.py
The text's first paragraph must be "Approved for Public Release"; each later
paragraph starts with a run-in label ending in a period, set in bold in the PDF.
"""
import os
import re
import subprocess
import sys

LABELS = ["Problem.", "Objective.", "Approach.", "Outcomes.", "Impact on DoW capabilities."]

here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, "project-summary.md")
out_tex = os.path.join(here, "project-summary.tex")
text = open(src, encoding="utf-8").read()
if "\n---\n" in text:
    text = text.split("\n---\n")[1]
paras = [p.strip() for p in text.strip("\n").split("\n\n")]
assert paras[0] == "Approved for Public Release", paras[0]
body = []
for p in paras[1:]:
    assert all(32 <= ord(c) < 127 for c in p), p[:40]
    assert not any(ch in p for ch in "%&$#_{}~^\\\"`"), p[:40]
    label = next((l for l in LABELS if p.startswith(l + " ")), None)
    assert label, p[:40]
    rest = p[len(label) + 1:].replace("'", "\\textquotesingle{}")
    body.append("\\textbf{" + label + "} " + rest)

tex = r"""% Project Summary/Abstract (SF 424 Project Abstract; upload for R&R Other Project Information, Field 7)
% ONR FY27 YIP, NOFO N0001426SF004. Compile with pdfLaTeX. The NOFO limit is one page or
% 4,000 characters including spaces, whichever is less, in standard keyboard characters.
% The text is the same as in project-summary.md (the labels are bold here); edit both together.
% Apostrophes are \textquotesingle{} and ligatures are off, so text copied from the PDF stays ASCII.
\documentclass[12pt,letterpaper]{article}
\usepackage[letterpaper,margin=1in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{textcomp}
\usepackage{mathptmx}
\usepackage{microtype}
\DisableLigatures{encoding = *, family = *}
\usepackage[hidelinks]{hyperref}
\hypersetup{pdftitle={Project Summary/Abstract: Trustworthy Collective Reasoning and Evaluation for AI Agents},pdfauthor={Xinya Du}}
\setlength{\parindent}{0pt}
\setlength{\parskip}{4pt}
\hyphenpenalty=10000 \exhyphenpenalty=10000
\pagestyle{empty}
\begin{document}
{\centering
{\large\bfseries Trustworthy Collective Reasoning and Evaluation for AI Agents\par}
\vspace{3pt}
Xinya Du (PI), The University of Texas at Dallas\par
\vspace{1pt}
{\itshape Approved for Public Release}\par}
\vspace{3pt}
@@BODY@@
\end{document}
""".replace("@@BODY@@", "\n\n".join(body))
open(out_tex, "w", encoding="utf-8").write(tex)

d = os.path.dirname(os.path.abspath(out_tex))
name = os.path.splitext(os.path.basename(out_tex))[0]
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", os.path.basename(out_tex)],
                   cwd=d, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
pdf = os.path.join(d, name + ".pdf")
info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
pages = [l for l in info.splitlines() if l.startswith("Pages")][0].split()[-1]
bbox = subprocess.run(["pdftotext", "-bbox", pdf, "-"], capture_output=True, text=True).stdout
ys = [float(m) for m in re.findall(r'yMax="([\d.]+)"', bbox)]
copied = subprocess.run(["pdftotext", pdf, "-"], capture_output=True, text=True).stdout
nonascii = sorted({c for c in copied if ord(c) > 126})
print(f"pdflatex exit {r.returncode}; pages {pages}; room at bottom {720 - max(ys):.1f} pt (14.5 pt per line); "
      f"non-ASCII when copied: {nonascii or 'none'}")
for ext in ("aux", "log", "out"):
    try:
        os.remove(os.path.join(d, name + "." + ext))
    except FileNotFoundError:
        pass
