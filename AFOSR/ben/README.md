# Ben Robinson white paper: research guide

**Checking and Revising Reasoning from Uncertain Evidence**

The revised draft is [white_paper_ben.pdf](white_paper_ben.pdf); editable sources are [main.tex](main.tex) and [references.bib](references.bib). It contains a cover, four narrative pages, and one references page. [revision_response.md](revision_response.md) explains the decisions made in response to Claude's review and the citation addendum. The original reviews are preserved.

## The idea in plain language

A system can reason correctly from a misread report. Checking its logic alone will not catch that mistake. We want it to keep track of how it read the evidence, spend effort resolving the uncertainties that matter, and revisit the right conclusions when a reading changes.

For example, a sensor failed at 10:02 and an outage was **reported** at 10:05. Those statements do not establish when the outage occurred. A correction placing the outage at 9:58 removes a possible temporal objection, but does not prove that the outage caused the failure. If the same report supplies other timestamps, the correction may require checking them too, even when their arguments have no logical link to the first one.

| Aim | Question | Starting experiment |
| --- | --- | --- |
| 1. Interpretations | What does the evidence actually establish? | Keep compatible candidate readings; require checked support for the same answer under every retained reading. Measure when the correct reading is missing. |
| 2. Checking | Which uncertainty should we resolve next? | Compare checking individual premises with checking shared source context, accounting for cost and correlated mistakes. |
| 3. Revision | What else must we reconsider? | Compare logical-descendant updates, source-aware updates, and full recomputation. |

The main hypothesis can fail: sharing source checks and reopening related interpretations may improve reliability, but may also consume enough computation to erase the benefit. We will measure both effects at comparable coverage and cost.

## What is new, and what is established

Rule checking, truth maintenance, cost-sensitive testing, and statistical validation are established tools. The proposed contribution concerns their use when the inputs are fallible interpretations, the correct interpretation can be missing, and one correction can affect several premises through shared context.

The conditional guarantee requires more than sound inference rules. The correct **joint** reading must remain among the candidates, and the answer must have checked support under every retained reading. An empty candidate set or a reading without a derivation produces an unresolved result. This does not guarantee that a report is true in the world.

The first formal experiments use finite graphs and specified joint check-outcome models. Exact policies for small cases provide reference points. Models of outcomes may be wrong; document evaluation and deliberately omitted interpretations test that limitation. Confidence bounds use independent validation cases for a policy fixed beforehand. A repair cap guarantees stopping, not a successful repair.

## Connection to your earlier work

The DARPA plan contributes structured examples, process supervision, and explanation evaluation. This project turns those into a study of evidence checking and revision. Your structured multi-hop reasoning and temporal extraction work support the representation; MEQA supports document evaluation; FG-PRM informs feedback on individual errors; Search Wisely informs decisions about gathering more information. Their extensions in this proposal are research goals, not previously demonstrated results.

## Program fit and Ben's publication

The [AFOSR Open BAA, Amendment 001, Section A.4.f, printed pages 52-53](https://files.simpler.grants.gov/opportunities/de479d2e-aad1-466a-acc3-d5d11cf7918d/attachments/fd9a4dfb-ac66-4c75-8166-592ea2daeb02/FA955026S0001_Amendment_0001_AFOSR_Open_BAA.pdf) emphasizes interpretable foundations, uncertainty, verification, and repair of faulty arguments. These are the primary basis for fit. Maintenance and anomaly reports provide a concrete motivating setting.

Aim 2 cites [Ubl, Robinson, and Hale, *Anomaly Search Over Many Sequences With Switching Costs*](https://arxiv.org/abs/2303.09647) once. The connection is the decision to keep inspecting one source or switch, accounting for observation and switching costs. Their paper studies data streams; this proposal studies interpretations and logical support. We do not claim its algorithms or guarantees carry over. This is a substantive connection, not evidence of the Program Officer's endorsement.

## Toward a full proposal

Start with a small end-to-end example in year one. Specify the rule language, candidate retention procedure, source groups, check outcomes, and compute accounting. Establish whether source-aware checking and revision help before expanding the scope or training a repair model. Keep all baseline support annotations independent of the system's checkers.

Compile with XeLaTeX, for example from the repository root:

```bash
latexmk -xelatex -cd -interaction=nonstopmode -halt-on-error -outdir=build ben/main.tex
```

This is the research draft. The CV and final acknowledgment of any other white papers being submitted remain submission-package items.
