# Response to the review and citation addendum

Revised October 9, 2026. This note accompanies the revised draft; it is not part of the submission narrative.

## Adopted

- **Center the actual uncertainty.** The opening, hypothesis, and all three aims now focus on fallible text interpretations, missing correct readings, and errors shared through source context. The running example explicitly distinguishes report time from event time.
- **Clarify the contribution.** Rule checking, truth maintenance, cost-sensitive testing, and finite-sample validation are acknowledged as established foundations. Added Greiner et al. (2006) and de Kleer and Williams (1987). The project studies their limits when interpreting evidence is uncertain.
- **Specify acceptance.** The same answer must have checked support under every retained compatible joint reading. Empty candidates, absent derivations, and unresolved necessary evidence checks lead to further checking or abstention.
- **Strengthen revision.** Compare logical-descendant revision, source-aware revision, and full recomputation. A corrected reading can require reopening other premises even without inference edges between them.
- **Improve evaluation.** Labels come from task specifications and independent human annotations. Baselines disclose support in a common format. Report unsupported reasoning among correct accepted answers separately; preserve alternative valid derivations in scoring.
- **Make the impact concrete.** Added a labeled DAF/DoW impact paragraph using maintenance and anomaly investigations, with auditable support, named missing checks, and updates after corrected reports.
- **Improve feasibility.** All three aims have a small end-to-end implementation in year one. Checker-guided refinement is the repair baseline. Training a repair proposer is a follow-on experiment.
- **Use closer prior work.** Temporal relation extraction and Search Wisely replace the less direct CLORE/AALC links in the narrative. MEQA, structured reasoning, and FG-PRM remain.
- **Retitle and align the opening.** The new title is *Checking and Revising Reasoning from Uncertain Evidence*. Removed the Chen et al. opening citation, whose specific finding did not support the old opening claim.

## Modified or not adopted

- **The suggested guarantee needed an extra condition.** Sound rules plus retention of each premise's correct reading are insufficient. Readings must form compatible joint interpretations, and the accepted answer must be derivable under all retained readings. The revised statement makes those conditions explicit. It is a conditional design property, not a novel theorem or a guarantee of real-world source truth.
- **No blanket approximation guarantee.** Adaptive-submodularity results require conditions that have not been established here. The draft instead commits to exact small-case reference policies, analysis of specified joint outcome models, and tests of model misspecification. Stronger approximation results can be selected after the formal problem is fixed.
- **No long quotations from the portfolio.** Plain-language alignment communicates fit without crowding the scientific argument. The program description remains the main basis for positioning.
- **No unsupported budget staffing calculation.** Retained the total budget and PI/student structure; did not adopt an unverified estimate of how many students it funds.

## Citation to Ben's work

The addendum proposed an analogy to covariance-based signal detection. We used a closer connection: [Ubl, Robinson, and Hale (2023), *Anomaly Search Over Many Sequences With Switching Costs*](https://arxiv.org/abs/2303.09647). Its public manuscript identifies Benjamin Robinson with AFRL's Sensors Directorate. It studies observation costs and costs of switching streams; Aim 2 similarly considers whether to continue checking a source or move to another, with measured source-context costs.

The citation appears once in Aim 2. It motivates the cost model, while explicitly distinguishing the logical-support and missing-interpretation problems here. We do not import the paper's assumptions, thresholds, or guarantees. The covariance-estimation analogy was not added: it would introduce a less direct connection and would require distinguishing false-positive rates from the fraction of accepted answers that are unsupported.

Citing relevant work can make the intellectual connection easier to recognize. It does not establish personal preference, endorsement, or a causal explanation of another applicant's funding outcome.

## Verification and package status

The revised PDF has four narrative pages, plus a cover and one references page. It uses the existing 12-point Garamond, letter paper, one-inch margins, and 1.5-spacing layout. The source and PDF were compiled and all pages visually inspected. Original review files and the other portfolio folders were preserved. The CV and acknowledgment of other submissions must be finalized with the submission package; the draft does not assert that any paper has been submitted.
