# Peer-weighting figure

The figure explains the proposed mutual-agreement weighting loop. Models review
anonymous answer pairs, their votes produce weighted decisions, and each judge's
agreement with judges from other model families determines its next weight.
Weights start equal and are smoothed and normalized after each update.

The matrix is schematic and contains no experimental results. The depicted
providers illustrate a panel, not the final choice of models. Human votes are
used to evaluate the proposed weights and do not enter their updates.

Build the figure with `python build_figure.py` from this directory. The script
converts the SVG icons to PDF, compiles the editable TikZ source, and writes a
PNG preview. It requires PyMuPDF and a LaTeX installation with TikZ.

Model icons come from [LobeHub Icons](https://github.com/lobehub/lobe-icons),
under the MIT license reproduced in `model_icons/LICENSE-lobehub.txt`.
Provider names and marks identify the illustrative model families.
