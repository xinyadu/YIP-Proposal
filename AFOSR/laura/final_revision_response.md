# Response to the final Laura white-paper comments

This second revision addresses [final_comment.md](final_comment.md). It retains the three aims, title, formatting, measurement definitions, experimental controls, and limits of the first revision. The complete revised sources are [main.tex](main.tex) and [references.bib](references.bib); the distribution copy is [white_paper_laura.pdf](white_paper_laura.pdf).

| Item | Decision and revision |
| --- | --- |
| **1. Trust-repair precedents and competing prediction** | Added Dzindolet et al. (2003) to motivate the possibility that explanations restore reliance too broadly, including on recurring failures. The recurrence-versus-unrelated comparison tests that alternative to selective adjustment. Added de Visser et al. (2018) beside Lyons et al., described trust repair as an established research line, and connected the sequential model to de Visser et al. (2020). |
| **2. Source sensitivity and Ueno's findings** | Added Whalen et al. and Connor Desai et al., and stated Ueno et al.'s finding of greater reliance on independent than shared-source support with labeled relations and an always-correct simulated adviser. The proposed distinction is fallible evaluator panels and separate harmful/beneficial adoption outcomes. Qualified two premises in the comments, as explained below. |
| **3. Richer records could increase overreliance** | Added Si et al. and explicitly predicted that richer records might make wrong advice more persuasive. The balanced-correctness design measures that harm separately from beneficial adoption. Did not add the optional uncertainty-expression citation or a new wording manipulation: that would broaden the study rather than clarify its existing contrast. |
| **4. Computational precedents** | Added GLAD for expertise/difficulty, Dong et al. for copied-source discounting, PoLL for evaluator panels, and LM vs LM for cross-examination. Included expertise/difficulty and copied-source baselines alongside the existing comparisons. Clarified that the contribution connects provenance/recency checks, dependence assessment, separately measured detection/correction/harm, and human reliance. Added FlipFlop to the harmful-revision motivation. |
| **5. Falsifiable hypothesis** | Replaced “may” and “can” with a directional comparison: records plus a reliability estimate should reduce harmful adoption relative to the estimate alone without a practically meaningful loss of beneficial adoption. Did not assume that shared-source and independent endorsements receive “nearly” equal weight; prior findings vary, and that phrase would need its own equivalence margin. |
| **6. Study 1 design and benchmark** | Specified display between participants and sourcing, correctness, and task type within participants. The primary interaction compares records-plus-estimate with estimate-only across source conditions on harmful adoption. Success requires an actual reduction in harmful adoption on shared-source cases and beneficial-adoption non-inferiority within a margin fixed before confirmatory collection. Power planning now explicitly covers that criterion. The initial 200–300 range is not represented as a demonstrated adequate sample. |
| **7. Cover, expertise, and title** | Replaced “drafts have been prepared” with a concise list of related YIP portfolios and Program Officers. Actual submission status remains an author confirmation; “the PI is also submitting” was not asserted without evidence. Kept the existing consultation plan and title: the title remains concise and accurately identifies both the technical approach and trust objective. No consultant, collaborator, or endorsement was invented. |

## Qualifications from source checking

- **Yousif et al. do provide a task-dependent result.** Their full paper's Experiment 5, on a bear sighting, found substantial discounting of false consensus, unlike the earlier inference-heavy tasks. The earlier draft's statement was supported. Whalen and Connor Desai are useful additional grounding rather than a correction of that claim. [Full paper](https://raboody.github.io/website/Papers/Yousif,%20Aboody%20&%20Keil%20(2019)%20-%20False%20Consensus.pdf).
- **Ueno et al. establish a result under labeled sources, not a clean causal effect of adding labels.** The revised text reports the observed independent-versus-shared difference rather than saying labeling itself “removed” the illusion. Their study was already preregistered and included repeated measures, so those features are not presented as new contributions. [Full paper](https://arxiv.org/html/2304.11279v1).
- **Trust repair should not mean maximizing trust.** The proposed tests distinguish selective reliance from indiscriminate restoration. Neither the new citations nor the existing theory is treated as proof that the intervention will work.
- **Optional citations were omitted where they did not support a distinct necessary change.** Kim et al., Goel et al., and Hoff and Bashir were not added. The core source-dependence, overreliance, and trust-repair claims are already grounded by the selected references.

## Added BibTeX entries

Eleven entries were added to [references.bib](references.bib): `dzindolet2003role`, `devisser2020longitudinal`, `devisser2018repair`, `connordesai2022source`, `whalen2018shared`, `si2024convincingly`, `dong2009dependence`, `whitehill2009whose`, `verga2024juries`, `cohen2023lmvslm`, and `laban2023flipflop`. Connor Desai et al.'s DOI was checked and included. The original fifteen entries remain.

## Author decisions before submission or preregistration

- **[AUTHOR: Confirm which other YIP white papers are actually submitted and finalize the cover acknowledgment.]** The related portfolios are listed, but submission has not been inferred from repository files.
- **[AUTHOR: Confirm the proposed Study 1 factor assignment and primary contrast; set and justify the beneficial-adoption non-inferiority margin before confirmatory collection.]** Power simulations should determine the required sample rather than treating the planning range as a cap.
- **[AUTHOR: If a behavioral-science consultant or collaborator has agreed, supply the name and role; otherwise retain the current consultation plan.]**

The existing institutional budget confirmation and current PI CV attachment also remain submission tasks. Author notes are kept here rather than inserted as placeholders into the scientific narrative.

## Validation

The XeLaTeX build has **five narrative pages**, one cover page, and three reference pages (nine pages total). The preamble, 12-point Garamond, 1.5-line spacing, and one-inch margins are unchanged. The discretionary `Needspace` before the team paragraph was removed. Citations resolve, and the rendered distribution PDF was inspected for page flow and clipping. The uploaded comments and unrelated repository files are preserved.
