# Peer-weighting figure

The figure adapts the structure of Figure 1 in PRD to explain the shared
weighting loop and distinguish two update rules:

- Original PRD uses each model's peer-assessed answer score as its next reviewer weight.
- The proposed extension uses a judge's agreement with judges from other model families.

The matrix is schematic and contains no experimental results. The depicted
providers illustrate a panel, not the final choice of models. Human votes are
used to evaluate the proposed weights and do not enter their updates.

Build the figure with `python build_figure.py` from this directory. The script
converts the SVG icons to PDF, compiles the editable TikZ source, and writes a
PNG preview. It requires PyMuPDF and a LaTeX installation with TikZ.

Model icons come from [LobeHub Icons](https://github.com/lobehub/lobe-icons),
under the MIT license reproduced in `model_icons/LICENSE-lobehub.txt`.
Provider names and marks identify the illustrative model families.
