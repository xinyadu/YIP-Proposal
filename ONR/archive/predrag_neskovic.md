# Reliable Collective Reasoning and Evaluation for AI Agents

**Xinya Du — University of Texas at Dallas**  
**FY27 ONR YIP · Informal Brief Research Concept**  
**Prospective Program Officer:** Dr. Predrag Neskovic (Code 311; Mathematical Data Science)

## Motivation and central question

AI systems increasingly draw on multiple language models, specialized evaluators, and collaborating agents to solve knowledge-intensive tasks. Yet agreement does not necessarily establish correctness. Agents may reproduce a common misconception, use overlapping reports, or share a faulty intermediate reasoning step. Majority voting, discussion, or model-level scores may produce confident but unsupported consensus.

**Research question:** How can imperfect AI agents collectively assess uncertain evidence and reach reliable conclusions, while distinguishing genuinely independent corroboration from correlated mistakes?

We propose **evidence-grounded collective reasoning**: identify the evidence and reasoning behind each judgment, model where judgments depend on one another, and actively acquire new evidence when existing assessments are insufficient.

## Proposed research aims

**Aim 1 — Evidence-grounded assessment of individual agents.** Extract checkable intermediate assertions, link them to retrieved evidence and structured relations, and localize factual, contextual, and logical errors. Study how agent expertise varies across tasks and how process-level assessments can be calibrated on independent reference cases. Distinguish a plausible explanation from independently supported reasoning.

**Aim 2 — Dependence-aware collective inference.** Develop methods that jointly account for agent reliability, task difficulty, overlap in cited evidence, and correlated errors. Rather than treating endorsements as independent votes, estimate the incremental information supplied by each assessment and preserve uncertainty when the available evidence cannot distinguish hypotheses. Our Peer Rank and Discussion research provides a foundation for interactive evaluation, but the proposed advance is reasoning- and source-aware collective inference.

**Aim 3 — Active verification and adaptive deliberation.** When judgments conflict or appear spuriously unanimous, choose diagnostic actions: request independent sources, challenge an unsupported step, or invoke domain-specific checks. Update the collective conclusion only to the extent warranted by new findings. Study when an extra verification action is more informative than further discussion among the same agents.

## Evaluation and potential Naval relevance

We will test the approach on multi-document reasoning and evidence assessment under controlled source duplication, conflicting reports, varying expertise, and unseen tasks. Outcomes include error detection, calibration, conclusion accuracy at matched coverage, robustness to dependence, and total verification cost. Baselines include individual judges, majority vote, learned weighting, and multi-agent discussion with matched information and budgets.

The research relates to distributed information assessment and decision-making under uncertainty, including settings where Naval analysts must synthesize potentially overlapping reports and distinguish corroboration from repetition. The goal is fundamental methods for dependable multi-agent inference, not an operationally deployed system.

**Intended contribution:** Algorithms and evidence representations that support reliable collective judgments without equating consensus with truth.

---

**Draft provenance (internal; remove from PDF):** #1 NSF complex reasoning (compositional reasoning and faithful explanations); #6 Amazon FG-PRM (error taxonomy and process evaluation); #8 Amazon process-guided reasoning (synthetic trajectories and process feedback); AFOSR Laura/PeerEval (peer assessments, shared errors, diagnostic follow-ups and calibrated reliance). The proposed dependence-aware collective inference is a research direction, not a completed capability.
