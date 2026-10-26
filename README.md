# FY27 YIP proposals: AFOSR and ONR

This repository holds two sets of FY27 Young Investigator Program documents:

- [`AFOSR/`](AFOSR/): three AFOSR white papers, one per Program Officer.
- [`ONR/`](ONR/): the ONR white paper and concept note for Predrag Neskovic, plus archived drafts. See the [ONR README](ONR/README.md).

## AFOSR white papers

| Program Officer | Research direction | LaTeX source | PDF |
| --- | --- | --- | --- |
| Doug Riecken | Neural-symbolic verification and refinement of scientific claims | [AFOSR/doug/main.tex](AFOSR/doug/main.tex) | [Doug white paper](AFOSR/doug/white_paper_doug.pdf) |
| Ben Robinson | Faithful and verifiable reasoning with uncertain, changing evidence | [AFOSR/ben/main.tex](AFOSR/ben/main.tex) | [Ben white paper](AFOSR/ben/white_paper_ben.pdf) |
| Laura Steckman | Interactive peer evaluation for calibrated trust in AI advisers | [AFOSR/laura/main.tex](AFOSR/laura/main.tex) | [Laura white paper](AFOSR/laura/white_paper_laura.pdf) |

Each paper has its own folder with a README, bibliography, reviewed PDF, and revision notes: `AFOSR/doug/`, `AFOSR/ben/`, and `AFOSR/laura/`. Doug's and Laura's sources reuse the Garamond fonts bundled in `AFOSR/ben/fonts/`.

- [Doug README](AFOSR/doug/README.md): current focus and review decisions ([REVISION_NOTES.md](AFOSR/doug/REVISION_NOTES.md)).
- [Ben research guide](AFOSR/ben/README.md): a plain-language explanation of the three aims, their connection to the PI's prior work, and the scope of the theoretical analysis.
- [Laura research guide](AFOSR/laura/README.md): the connection to PRD and IQA-EVAL, the human-reliance experiments, program fit, and development questions.

### Compile the AFOSR papers

From the repository root:

```bash
latexmk -xelatex -cd -interaction=nonstopmode -halt-on-error -outdir=build AFOSR/doug/main.tex
latexmk -xelatex -cd -interaction=nonstopmode -halt-on-error -outdir=build AFOSR/ben/main.tex
latexmk -xelatex -cd -interaction=nonstopmode -halt-on-error -outdir=build AFOSR/laura/main.tex
```

The compiled files are `AFOSR/doug/build/main.pdf`, `AFOSR/ben/build/main.pdf`, and `AFOSR/laura/build/main.pdf`. The reviewed distribution copies are `AFOSR/doug/white_paper_doug.pdf`, `AFOSR/ben/white_paper_ben.pdf`, and `AFOSR/laura/white_paper_laura.pdf`.

In Overleaf, set the main document to `AFOSR/doug/main.tex`, `AFOSR/ben/main.tex`, or `AFOSR/laura/main.tex` and compile with XeLaTeX. All three sources find their fonts and bibliography whether compiled from the repository root or from their own folder.

### Before an official AFOSR submission

Ben's and Laura's papers include the cover page, research narrative, and cited references. Attach the PI's current CV with the complete publication and presentation information required by the notice. Confirm the institutional budget before submission.

The FY27 notice allows multiple white papers but requires acknowledging the other submissions on each. If more than one direction is submitted, add that acknowledgment to each submitted paper. Sending a paper to a Program Officer does not replace submission through the official white-paper portal.

Official sources: [FY27 YIP notice and Q&A](https://simpler.grants.gov/opportunity/c342c01d-4f34-440f-8bb2-4bdd4d763df0) and [AFOSR research interests](https://simpler.grants.gov/opportunity/de479d2e-aad1-466a-acc3-d5d11cf7918d).

## ONR documents

| Program Officer | Document | LaTeX source | PDF |
| --- | --- | --- | --- |
| Predrag Neskovic | Four-page white paper v4 (current) | [ONR/predrag/main-4page-v4.tex](ONR/predrag/main-4page-v4.tex) | [Predrag white paper](ONR/predrag/white_paper_predrag-4page-v4.pdf) |
| Predrag Neskovic | One-page discussion note | [ONR/predrag/main.tex](ONR/predrag/main.tex) | [Predrag one-page note](ONR/predrag/white_paper_predrag.pdf) |

Both compile with pdfLaTeX from `ONR/predrag/`; see [ONR/predrag/README.md](ONR/predrag/README.md) for build commands. Predrag's folder also holds the Program Officer feedback and meeting notes.

Earlier drafts and concept notes for other Program Officers (Kamgar-Parsi, Krebs, Goolsby, Morrison) are kept in [`ONR/archive/`](ONR/archive/).
