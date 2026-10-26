# Review: AFOSR YIP White Paper for the CCMI Portfolio

Oct 9, 2026 · @Xinya Du from @Claude

## Overall assessment

The paper is credible, unusually honest, and contains a real idea, but the idea sits in the wrong place. I reviewed `ben/main.tex` in [xinyadu/AFOSR-YIP](https://github.com/xinyadu/AFOSR-YIP); the committed PDF matches it.

The question worth funding is this: when an argument's premises are fallible readings of text, what can a checker guarantee, what should it check first, and what must it reopen when a reading changes? That question appears in only one sentence of "Research contribution."

The formal commitments land elsewhere, on properties that hold by construction or are classical results. A portfolio that places "the utmost emphasis on fundamental mathematical underpinnings and mathematical rigor" is the most likely to notice. Air Force relevance also gets one sentence, though it is half the white-paper score.

Everything to change before the deadline (11:59 PM Eastern on Oct 9, 2026, 8:59 PM Pacific) is sentence-level and fits in the free page. The narrative uses 4 of the 5 allowed pages, the cover has every required field, and all ten references check out.

## Five highest-priority issues

The issues are ranked by importance. Each gives the passage, why it matters, and a fix; the "before sending" fixes are sentence-level.

### 1. The real question is stated in passing, and the formal commitments sit on established ground

**From the paper:** "We ask: How can a reasoning system check its conclusions and revise them when evidence changes?" Aim 1: "establish sufficient conditions for an accepted derivation to be valid within the restricted rule system." Aim 2: "seeking conditions under which efficient policies approach the reference performance." Aim 3: "analyze when revisiting only affected dependencies preserves the conclusions obtained by complete recomputation under the same premises and rules."

**Why it matters.** When premises are taken as given, truth maintenance and model-based diagnosis already answer that question. The hypothesis, "explicit evidence dependencies help target checking and reduce the cost of revision," is the reason truth maintenance exists. The genuinely open part, "a misread shared premise can also spread error," gets one sentence.

As written, each formal objective lands on known ground:

- **Aim 1.** If every step is checked against sound rules, validity relative to the recorded premises holds by construction. Computing the answer from the checked chain is the [Faithful CoT](https://arxiv.org/abs/2301.13379) design.
- **Aim 2.** Choosing which uncertain premise to test under costs is a classical problem. [Greiner et al. (2006)](https://papersdb.cs.ualberta.ca/~papersdb/view_publication.php?pub_id=301) solve restricted AND-OR trees and show the problem is NP-hard once a test appears in more than one place or outcomes are correlated, which is exactly your shared-premise case. [De Kleer & Williams (1987)](https://www.fs.isy.liu.se/Edu/Courses/DocDiagnos/CourseMaterial/deKleer_Williams_1987.pdf) already pair an ATMS with probability-based choice of the next measurement.
- **Aim 2, single chain.** For one chain where any failed check rejects, a short swap argument shows the optimal order is increasing cost divided by failure probability. So "most uncertain first" is suboptimal whenever costs differ. (That argument is mine, not from a source.)
- **Aim 3.** Under fixed premises and rules, local revision agreeing with full recomputation is the standard correctness property of truth maintenance and of incremental view maintenance ([DRed, 1993](https://doi.org/10.1145/170036.170066)).

The program asks for "pathfinding new theories and frameworks rather than incremental engineering improvements." A formally trained reader may see re-derivations here and miss the novelty you do have.

**Fix before sending** (about one paragraph; no new machinery):

- **Pose the question in the regime the classical work assumes away.** For example: "When an argument's premises are fallible readings of text, the correct reading may be missing from the candidates, and misreadings of the same passage tend to occur together. In that setting, what can a checker guarantee about an accepted answer? Which readings should it verify first under a budget? Which conclusions must it reopen when one reading is corrected?"
- **Make the hypothesis a tradeoff that can fail.** Reusing checks and repairing locally save cost, but correlated misreadings can make both unsafe. Tracking each premise's source, which your representation already records, keeps the savings without raising unsupported answers. Test this against dependency-only reuse and exhaustive checking at matched cost.
- **Aim 1: state the shape of the guarantee.** The answer follows from the source if (A) every step instantiates a sound rule, and (B) each premise's correct reading is among those retained. (A) is checked exactly and is a design guarantee; (B) is the research.
- **Aim 2: position it, then ask the new question.** Cite Greiner et al. and de Kleer & Williams in one sentence. Then ask which approximation guarantees survive when checks are shared, correlated and three-valued, and the candidate set may be incomplete. Greedy bounds under adaptive submodularity ([Golovin & Krause, 2011](https://mlanthology.org/jair/2011/golovin2011jair-adaptive)) are the standard starting point.
- **Aim 3: cite the known part, ask the new one.** Treat equivalence under fixed premises as known. Ask instead which other premises must be re-checked when a corrected reading changes how the rest of the same passage should be read. Your event-time versus report-time example is exactly this case.

The conditions and proofs themselves can wait for the full proposal.

### 2. Air Force relevance is one generic sentence, and the program's best-matching wording goes unused

**From the paper:** "Its Air Force and Space Force relevance lies in drawing defensible conclusions from incomplete or changing reports."

**Why it matters.** The notice scores white papers on two equally weighted criteria: technical merit and relationship to Department of War (DoW) missions. It also lists "Potential impact on DAF and DoW capabilities" as required content. The paper names no mission setting.

The paper's output is an answer with a checkable derivation, explicit assumptions, or "unresolved" with the missing check named. That nearly matches the program's "real-time, falsifiable recommendations that fully communicate its degree of uncertainty," but the paper never makes the connection. Meanwhile, "reasoning that completes within resource limits" rests only on caps, a stretch next to the program's "time-to-completion bounds."

**Fix before sending:**

- **Add a labeled "Potential Impact on DAF and DoW Capabilities" paragraph** of four to six sentences.
  - Name one or two settings where conclusions come from reports that are incomplete and later corrected, such as incident or anomaly reports, maintenance records or intelligence summaries. Pick ones you can describe accurately.
  - Say what an operator gets: a checkable basis for each answer, explicit assumptions, a named missing check, and an auditable update when a report changes.
- **Quote the program's own wording in the fit sentence:** the "falsifiable recommendations" phrase; "theoretically justified prescriptions for how to use less transparent deep-learning systems and their compositions with other algorithms"; and "systems that can self-repair faulty arguments in finite time."
- **Drop "completes within resource limits"** unless you commit to a bound.
- **Avoid "information may be corrupted, denied, or manipulated."** In the program text, that phrase belongs to adversarial game-theoretic settings, which this paper doesn't address.

### 3. The evaluation can't yet reliably catch right answers reached through faulty reasoning

**From the paper:** "An accepted answer is unsupported if its disclosed derivation contains an invalid inference or a premise not justified by the supplied evidence."

**Why it matters:**

- **No independent judge.** The paper doesn't say who decides "not justified." If the system's own evidence checks decide, the metric is circular.
- **Baselines can't be scored the same way.** The metric is undefined for baselines that show no derivation, such as selective generation and direct answers.
- **The opening problem isn't measured on its own.** The unsupported-answer rate mixes right answers with faulty reasoning together with wrong answers.
- **MEQA's metrics won't catch it.** Completeness matches a single gold chain, which penalizes alternative valid support. Logical consistency only asks whether a step contradicts earlier steps. The [MEQA paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e560a0b22e4432003d0dba63ff8dc457-Abstract.html) itself notes that its script counted short explanations as consistent whenever the answer was correct (Sec. 6.3).

**Fix before sending** (two or three sentences):

- **Name the source of labels.** Use known derivations for generated cases and human step-level support annotation on a MEQA subset, never the system's own checkers.
- **Use one format for every system.** Each system discloses its derivation in the same step format; prompt baselines to do the same.
- **Report the opening problem directly.** Give the unsupported rate among correct accepted answers. Generate "trap" cases where a typical invalid step still reaches the right answer, such as reading a report time as an event time.
- **Keep the premise-change test.** It is the one check that works for every system.

The annotation protocol and the number of cases the reliability claim needs can wait for the full proposal.

### 4. The opening sentence, its citation, the example and the title don't match the project

**From the paper:** Title, "Faithful and Verifiable Reasoning in Language Models." Opening, "A language model can give the right answer for the wrong reason \[Chen et al. 2025\]." Aim 1, "This defines faithfulness at the system level; the recorded argument need not describe every internal computation of the language model."

**Why it matters:**

- **The citation shows something else.** [Chen et al.](https://arxiv.org/abs/2505.05410) measure whether reasoning models' chains of thought admit to using a hint that changed their answer; they often admit it less than 20% of the time. That is undisclosed influence, not a correct answer reached through invalid steps. A reader who knows the paper will notice in the first sentence.
- **The example doesn't illustrate the claim.** It shows a wrong conclusion, not a right answer reached for a wrong reason.
- **The title promises more than the paper delivers.** It promises faithful language-model reasoning, while Aim 1 defines faithfulness at the system level, which holds by construction. "Verifiable" also overstates, because the evidence checks are learned.

**Fix before sending:**

- **Retitle around what's new,** for example "Checking and Revising Arguments over Uncertain, Changing Evidence."
- **Open with claims the sources support.** Correct answers can rest on invalid steps: in [ProcessBench](https://arxiv.org/abs/2412.06559)'s expert-annotated math solutions, the share of correct-answer solutions containing an erroneous step rises with difficulty, to about half on the hardest subset. Stated reasoning can also omit what actually drove the answer (Chen et al.).
- **Add one clause to the example:** even if the outage did cause the failure, nothing in the model's argument established it.
- **Optionally, add your own evidence.** MEQA's error analysis (Appendix J) found models misreading event relations stated in the question, for example reading CAUSED BY as AT THE SAME TIME, which breaks the whole chain.

### 5. Aim 3's central experiment is nearly foregone, and the plan is too full for one PI

**From the paper:** "The central experiment will test whether this targeted feedback improves repair on unfamiliar combinations of rules compared with a generic request to try again." Plan: "Year 3 will develop and evaluate repair, integrate the three aims, and test transfer to new document sources."

**Why it matters:**

- **"Try again" is a weak baseline.** [Huang et al. (ICLR 2024)](https://arxiv.org/abs/2310.01798) found that self-correction without external feedback generally doesn't improve reasoning and sometimes hurts. [Logic-LM](https://aclanthology.org/2023.findings-emnlp.248/) already refines its formal translations using solver error messages.
- **A trained repair model is a whole extra pipeline.** It adds data generation and training on top of the representation, the rule library, the check-selection theory, a reliability study, the MEQA extension and six baselines. My rough estimate is that $150K a year, including indirect costs, supports about one PhD student plus modest compute and annotation.
- **Repair starts too late.** It is the piece closest to the program's "self-repair faulty arguments in finite time," yet it starts only in Year 3, at the same time as integration.

**Fix before sending:**

- **Change the central experiment.** Compare local repair against full recomputation when readings are uncertain, measuring cost saved and errors introduced. Use refinement from checker feedback, as Logic-LM does, as the baseline.
- **Make the trained repair proposer optional.**
- **Reorder the plan.** Build a thin end-to-end version of all three aims on generated cases in Year 1, then deepen each.

## Assessment by question

### 1. Program fit

The strongest matches are already in the paper but unclaimed; the gaps are complexity bounds and Air Force relevance.

| Program wording | Where the paper meets it | Status |
| --- | --- | --- |
| "real-time, falsifiable recommendations that fully communicate its degree of uncertainty" | Checks return supported, contradicted or unresolved; explicit assumptions; "reporting which missing checks prevent a decision" | Strong, unclaimed |
| "theoretically justified prescriptions for how to use less transparent deep-learning systems and their compositions with other algorithms" | The language model proposes and the checker decides; "Learned scores will guide this choice; they will not count as proofs." | Strong, unclaimed |
| "systems that can self-repair faulty arguments in finite time" | Aim 3 | Strong for repair; "finite time" is only a cap |
| "heuristic reasoning with quantifiable advantages"; "debuggable … modular architectures" | Aim 2's heuristics compared with exact reference policies; "locate the conflict instead of merely assigning the explanation a low score" | Fits, unclaimed |
| "asymptotic complexity bounds, rates of information-theoretic convergence" | Nothing | Gap; Aim 2 (Issue 1) is the natural home |

The paper stretches the program in four places:

- "Reasoning that completes within resource limits" rests only on caps.
- "Formal verification" applies only to the rule layer.
- The Computational Cognition sub-topic is about "Modeling human (or animal) cognitive processes." Cite its repair challenge, not the sub-topic itself.
- Air Force relevance is a single sentence.

It correctly avoids claiming causal analysis, adversarial robustness or autonomous knowledge discovery.

### 2. Scientific contribution

Yes, there is a coherent question beyond combining existing methods (Issue 1). The paper names its neighbors in one sentence without contrasts; the right-hand column, compressed, belongs in "Research contribution."

| Neighbor | What it already does | What this proposal adds |
| --- | --- | --- |
| Solver-assisted reasoning ([Faithful CoT](https://arxiv.org/abs/2301.13379), [Logic-LM](https://aclanthology.org/2023.findings-emnlp.248/), [LINC](https://arxiv.org/abs/2310.15164)) | Translates text into logic, and a solver derives the answer. LINC takes a majority vote over 10 sampled translations; its own error analysis blames translations that drop implicit or stated information. | Readings are checked against the source and kept explicit; disagreement leads to abstention, not a vote |
| Process supervision (PRMs, [FG-PRM](https://aclanthology.org/2025.findings-emnlp.228/)) | Learned scores on the steps of the model's own chain | Scores only decide what to check. Acceptance requires exact inference checks plus evidence checks, and reading errors stay separate from inference errors |
| Selective prediction ([selective generation](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a6815122f533193a022cbc41786c1cc-Abstract.html)) | Abstains under a confidence threshold, with a statistical guarantee on accepted answers | Abstention names the unresolved premise and supports revision. The statistical tools are shared, not new |
| Truth maintenance and diagnosis (ATMS, [GDE](https://www.fs.isy.liu.se/Edu/Courses/DocDiagnos/CourseMaterial/deKleer_Williams_1987.pdf)) | Tracks dependencies and chooses measurements for given premises with independent faults | Premises are readings of text: candidates may omit the truth, errors correlate within a source, and checks are imperfect and three-valued |

### 3. Technical credibility

Several formal promises are already established; the realistic research sits where readings are uncertain.

- **Established, or true by construction:** validity of a checked derivation; faithfulness of an answer computed from it; stopping because of caps; local revision matching recomputation under fixed premises; finite-sample error bounds for a fixed acceptance rule; the optimal check order on a single chain; targeted feedback beating "try again."
- **Realistic research objectives:** guarantees conditional on the retained readings including the correct one; check selection with shared or correlated premises; revision that tracks where each premise came from; reliability-cost curves on real documents; data containing ambiguities and corrections.
- **Too broad as written:** "We will study its extension to premises whose source interpretation is uncertain"; "integrate the three aims."
- **Hidden assumptions:**
  - The correct reading is among those retained.
  - Check errors are independent.
  - Check costs and outcome models are known.
  - Every library rule is sound. Rules that decide two mentions are the same entity are usually defaults, which can fail.
  - "Error-detection value" requires calibrated probabilities.
- **Logical gaps:**
  - The paper says learned scores "will not count as proofs," yet the evidence checks (relation extraction, textual entailment) are also learned and decide acceptance. Say instead that acceptance is exact inference checking plus empirically validated evidence checking.
  - "Retained plausible interpretations do not conflict" needs a rule for which readings are retained. It also needs a decision on whether a reading with no derivation counts as a conflict.

### 4. Coherence and feasibility

It is one project: one object, an argument graph whose premises keep their source, with three questions about it (accept, check, reopen). Saying that in one sentence would make the unity obvious, and the running example already threads through all three aims. Feasibility is covered in Issue 5; the theory is credibly restricted, and human annotation should stay at a few hundred cases.

### 5. Connection to your work

The connection is credible, and completed and proposed work are kept apart correctly. For example, the paper notes that FG-PRM's published setting is math and that extending it is proposed.

Two directions from the DARPA paper are now published: [MEQA](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e560a0b22e4432003d0dba63ff8dc457-Abstract.html) at NeurIPS 2024 Datasets & Benchmarks, and step-level process rewards, done for math as [FG-PRM](https://aclanthology.org/2025.findings-emnlp.228/) at EMNLP 2025 Findings. The DARPA paper's preliminary numbers aren't reused, which is right.

Two changes would strengthen the connection:

- **Replace the weak link.** AALC is about training shorter reasoning, not the cost of checking. [Search Wisely](https://arxiv.org/abs/2505.17281) (EMNLP 2025) and [HiPRAG](https://arxiv.org/abs/2510.07794) (ICLR 2026), which decide when a retrieval is actually needed, are closer to Aim 2.
- **Cite your strongest credential.** Your [event temporal relation extraction (MATCHING 2023) and document-level causal relation extraction (EMNLP Findings 2024)](https://xinyadu.github.io/publications.html) work underlies exactly the evidence checks on event order and causation. Neither is cited, and together they are your strongest credential for the hardest step.

### 6. Clarity and evaluation

A program officer outside natural language processing can follow the paper: the prose is plain and the running example does real work. A few terms are used before they are grounded: "retained plausible interpretations," "conditional possibilities" and "estimated error-detection value." With a page free, a small figure of the sensor example as an argument graph would help most.

The controls for the central hypothesis are right: exhaustive and uniform checking, full recomputation, budgets matched including checking and repair, error compared at matched coverage, and ablations. Detecting right answers with faulty reasoning needs the Issue 3 fixes.

## What's strong and should be kept

Keep these through the revision; they are what make the paper credible.

- **The core idea:** separating checks on how evidence is read from checks on the inference rules.
- **The running example and its honest ending:** "timing alone still does not establish the cause."
- **The disciplined limits:**
  - learned scores "will not count as proofs"
  - "Reaching a cap will return an unresolved result, not a claim that repair succeeded"
  - "neither invented premises nor weakened rules will count as successful repairs"
  - cases the rules can't represent "will count as unresolved rather than being removed from evaluation"
- **Three-valued checks**, and abstention that names the missing check.
- **The evaluation design:**
  - matched total compute and matched coverage
  - reliability-cost curves
  - the premise-change test
  - reporting where theory fails on documents, which fits the notice's emphasis on skepticism and on accepting negative results
- **The accurate split** between completed and proposed work.

## Before sending vs. later

About a page of edits is needed before tonight's deadline; everything else can wait for the full proposal.

### Before sending tonight

- [ ] If Doug's paper is also going in, add the required acknowledgment of the other submission to both covers, with one line on how the two differ, since the program contacts coordinate feedback.
- [ ] Replace the "\[PHONE NUMBER\]" placeholder on Doug's cover.
- [ ] Attach your CV.
- [ ] Make the minimal fixes for Issues 1–5.
- [ ] Swap the citations from question 5 and add the learned-checks sentence from question 3.
- [ ] Submit through the Qualtrics portal; emailing Ben doesn't count as a submission.

### Can wait for the full proposal

- the rule language and exact acceptance rules
- the formal conditions and proofs
- models of check cost and check errors
- the annotation protocol and sample sizes
- measurable per-year benchmarks, which the notice requires of full proposals
- the data management plan
- current and pending support, including any overlap with your CAREER award
- named students
- the figure, if time runs out tonight

## Note on Ben's IEEE page and Leilani's example

Nothing here is tailored to the program officer's preferences; the program text is specific enough to write to directly. I couldn't load Ben's IEEE page, because IEEE Xplore refused the automated request.

Leilani's paper is a good format reference, but it went to a different portfolio under an older announcement. Her Minsky citations are also the basis of her method (frame representations), which is why they read as substantive.

## Sources

- [ProcessBench (arXiv 2412.06559)](https://arxiv.org/abs/2412.06559)
- [Chen et al., Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410)
- [Greiner et al., Finding Optimal Satisficing Strategies for And-Or Trees (AIJ 2006)](https://papersdb.cs.ualberta.ca/~papersdb/view_publication.php?pub_id=301)
- [de Kleer & Williams, Diagnosing Multiple Faults (AIJ 1987)](https://www.fs.isy.liu.se/Edu/Courses/DocDiagnos/CourseMaterial/deKleer_Williams_1987.pdf)
- [Golovin & Krause, Adaptive Submodularity (JAIR 2011)](https://mlanthology.org/jair/2011/golovin2011jair-adaptive)
- [Gupta, Mumick & Subrahmanian, Maintaining Views Incrementally (SIGMOD 1993)](https://doi.org/10.1145/170036.170066)
- [LINC (EMNLP 2023)](https://arxiv.org/abs/2310.15164)
- [Faithful Chain-of-Thought Reasoning](https://arxiv.org/abs/2301.13379)
- [Logic-LM](https://aclanthology.org/2023.findings-emnlp.248/)
- [Huang et al., Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798)
- [Selective Generation for Controllable Language Models (NeurIPS 2024)](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a6815122f533193a022cbc41786c1cc-Abstract.html)
- [MEQA (NeurIPS 2024)](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e560a0b22e4432003d0dba63ff8dc457-Abstract.html)
- [FG-PRM (EMNLP 2025 Findings)](https://aclanthology.org/2025.findings-emnlp.228/)
- [Search Wisely](https://arxiv.org/abs/2505.17281)
- [HiPRAG](https://arxiv.org/abs/2510.07794)
- [Xinya Du, publication list](https://xinyadu.github.io/publications.html)
