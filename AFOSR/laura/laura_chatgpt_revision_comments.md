# Revision comments for ChatGPT — Laura Steckman (Trust and Influence) white paper

**How to use:** attach `laura/main.tex` and `laura/references.bib` to ChatGPT, then paste everything below the line.

---

You are revising an AFOSR FY27 Young Investigator Program (YIP) white paper written in LaTeX. Treat it as an initial white paper, not a full proposal. It needs a compelling basic-research question, a credible approach, and a clear link to the PI's expertise. Its technical commitments must be meaningful and defensible. Apply the revisions below, in priority order.

## Context

- **Paper:** "Interactive Peer Evaluation for Calibrated Trust in AI Advisers."
- **Portfolio:** Trust and Influence, Dr. Laura Steckman (AFOSR Open BAA FA9550-26-S-0001, Amendment 0001, Section A.4.g).
- **PI:** Xinya Du, The University of Texas at Dallas.
- **Deadline:** 9 October 2026, 11:59 PM Eastern, through the official Qualtrics portal.
- **How white papers are scored:** two criteria of equal importance, technical merit and "Potential relationship of the proposed research and development to DoW missions" (YIP notice FA9550-26-S-0003, F.2.b.1).
- **Required content:** includes "Potential impact on DAF and DoW capabilities" (YIP notice, D.2.b).

## Hard constraints

1. **Page limit.** The narrative must stay within 5 pages; the cover page, CV and references don't count. Format is US Letter, 1-inch margins, 12-point Garamond, 1.5 spacing. The current draft uses 4 narrative pages, so about one page is available for additions. Recompile with XeLaTeX and confirm the count.
2. **Keep it compiling.** Keep the current preamble and fonts.
3. **Invent nothing.** Do not invent citations, results, collaborators, program text, mission details or DoD practices. Add only citations from the verified list at the end. Where the author must supply a fact, write `[AUTHOR: …]`.
4. **Change only what's asked.** Keep every sentence these comments don't ask you to change. Do not add jargon or complexity to make the paper sound more technical.
5. **Return four things:**
   - the full revised `main.tex`
   - the BibTeX entries you added
   - a change log keyed to the numbers below
   - every `[AUTHOR: …]` item

## Program text you may quote

These passages come from the program's public description. The current BAA's A.4.g opens with the same first sentence.

- "The Trust and Influence program funds interdisciplinary high risk, transformative basic research that (1) elucidates the social and cognitive principles and processes surrounding the establishment, maintenance, and repair of trust between and among humans and intelligent agents, machines, algorithms, and/or other emergent technologies"
- "with particular interest in situations where these concepts apply to heterogeneous, distributed teams or teaming constellations (i.e. teams of teams)"
- "(2) advances the science of social influence" … "shape or affect human beliefs, perceptions, attitudes, and/or behaviors."
- "research designs that utilize laboratory studies, modeling, and/or field research intended to develop novel, transformative theories, frameworks, or evaluative measures."

The draft currently says the project addresses the portfolio's "interests in dynamic evaluation of human-agent teams, drivers of trust, and joint performance." That wording was not verified against the current A.4.g text. Keep it as program language only if the author confirms it appears there: `[AUTHOR: confirm against BAA A.4.g]`.

## Reviewer assessment (context for the edits)

- **Program fit.** The fit is strong but under-claimed:
  - Study 2 is trust repair.
  - Multiple AI endorsements act as a consensus cue, which is social influence.
  - A person working with an AI adviser and an evaluator panel is a heterogeneous team.

  The paper uses none of the program's own words for these. Its DoW relevance is a single sentence.
- **Scientific contribution.** The contribution is real. It joins dependence-aware evaluation of AI evaluators with a behavioral test of whether people discount agreement that rests on one shared source. The behavioral half is the T&I science, but the paper reads as two-thirds NLP methods.
- **Technical credibility.** The design is careful: preregistration, a judge–advisor design, matched displays, and separate scoring of beneficial and harmful adoption. Gaps:
  - The behavioral hypotheses aren't anchored in the trust and advice-taking literature.
  - Aim 1's statistical model is classical rater-aggregation work and isn't cited as such.
  - Behavioral-science expertise is described only as consultation the PI "will seek."
- **Coherence and feasibility.** The three aims form one project. The main feasibility risk is running two confirmatory human studies without a named behavioral collaborator.
- **Connection to the PI's work.** The connection is credible and honest. PRD (TMLR 2024) and IQA-EVAL (NeurIPS 2024) are described accurately, and their limits are stated. PeerEval is described as more than its public page shows.
- **Clarity and evaluation.** The prose is clear, but the running example shows three *advisers* agreeing while the aims study a panel of *evaluators* judging one adviser. The evaluation tests the hypotheses well.

## Keep these — do not weaken them

- The three definitions (reliability, trust, reliance), and the sentence "Higher reported trust or more frequent agreement with AI will not by itself establish improvement."
- Recording the participant's own answer and confidence before the advice, and scoring beneficial and harmful adoption separately.
- Study 1's targeted contrast, which holds the advice, endorsements and numerical estimate fixed, plus its comprehension checks.
- Study 2's design: a recurrence of the failure type versus unrelated reliable advice.
- These honest limits:
  - "Neither result establishes that peer scores are probabilities of correctness or that simulated users reproduce human trust."
  - "Source overlap is observable evidence of dependence; different model names or prompts will not be treated as proof of independence."
  - detection, correction and persuasion scored as separate outcomes
  - measured harm from inappropriate challenges
  - ambiguous cases kept as unresolved
  - "Failure to improve reliance despite improved automated assessment is an informative result"
- The strong baselines: the best single judge selected on development data, and a supervised aggregator given the same labels.
- Preregistration, power simulation, mixed-effects analysis and institutional review.

## Revisions, ranked — make these before sending

### 0. Administrative (required)

- **Acknowledge the other submissions.** The YIP notice (D.2.b) says: "You may submit more than one white paper to a single or multiple research discipline; but you must acknowledge so on each submission." Add one line to the cover page: "The PI is also submitting white papers to the Computational Cognition and Machine Intelligence portfolio (Dr. Ben Robinson) `[AUTHOR: and to Dr. Doug Riecken's portfolio, if submitted]`. This paper is distinct: it studies how people weigh and repair trust in AI evaluation evidence; the others study automated verification of reasoning."
- **Leave the cover's other fields unchanged.** They are already complete.

### 1. Make trust-and-influence science the spine of the paper

> This project asks: When does agreement among AI evaluators provide useful evidence for human reliance, and when can targeted interaction reveal that the agreement is misleading?

> The project addresses the Trust and Influence portfolio's interests in dynamic evaluation of human-agent teams, drivers of trust, and joint performance.

**Why.** Aims 1–2 extend NLP methods (PRD, IQA-EVAL). A T&I reviewer will judge the paper by what it reveals about the social and cognitive principles of trust and influence. Several of the program's own phrases describe this paper better than the current fit sentence does:
- Study 2 is about the "repair of trust."
- AI agreement acting as a consensus cue is "social influence" on "beliefs … and/or behaviors."
- A person with an AI adviser and an evaluator panel forms a heterogeneous team.
- The evaluation record and reliance measures are "evaluative measures."

**Change.**
- **Restate the central question around the human.** For example: "How do people weigh agreement among AI agents, do they discount agreement that comes from a single shared source, and what evidence helps them calibrate their reliance and repair trust after errors?" Keep the computational question as the means: when panel agreement carries evidence, and which follow-up questions expose shared errors.
- **Add one sentence in Section 1 on how the aims connect.** Aims 1–2 produce and validate the evaluation evidence that Aim 3 tests with people.
- **Name the two studies by what they test.** Study 1 tests "AI consensus as social influence." Study 2 tests "trust repair after errors."
- **Replace the fit sentence** with no more than two sentences built from the verified program quotes above.

### 2. Anchor the behavioral hypotheses in the literature T&I reviewers know, with competing predictions

> We distinguish three concepts.

> We predict that disclosure will reduce harmful adoption of shared errors without a comparable loss of beneficial adoption of well-supported advice.

> We will test whether the evidence supports selective adjustment rather than indiscriminate acceptance or rejection of the adviser.

**Why.** The core behavioral question has direct precedents with human sources:
- **Yousif, Aboody & Keil (2019).** People were as confident in a "consensus" built on a single primary source as in one built on independent sources, even right after judging the independent consensus more believable. This makes Study 1's outcome genuinely uncertain, which is good for basic research. It also supplies a competing prediction: disclosure may *not* remove the illusion.
- **Dietvorst, Simmons & Massey (2015).** People abandon algorithms after seeing them err (algorithm aversion). Study 2 tests a remedy for this.
- **Lee & See (2004).** The trust-versus-reliance distinction comes from this paper.
- **Bonaccio & Dalal (2006).** The initial answer → advice → final answer design is the judge–advisor paradigm they review.

Citing these shows command of the behavioral science and sharpens the hypotheses.

**Change.** Add one sentence at each point below; add no new aims.
- **Concepts paragraph:** cite Lee & See (2004) for trust versus reliance and appropriate reliance. Keep Schemmer et al.
- **Study 1:** state the competing prediction from the illusion of consensus. Say the study tests whether the illusion extends to AI evaluators and whether disclosure removes it.
- **Study 2:** frame it against algorithm aversion. Predict that diagnostic evidence supports selective adjustment rather than blanket avoidance after an error.
- **Aim 3's design sentence:** name the judge–advisor paradigm and cite Bonaccio & Dalal (2006).

### 3. Add a labeled DAF/DoW impact paragraph

> For the Air Force and Space Force, the motivating need is to judge AI-assisted interpretations of incomplete or conflicting reports.

**Why.** DoW relevance is half of the white-paper score, and the notice requires a "Potential impact on DAF and DoW capabilities" element. The shipment example is already a logistics scenario, but the paper never says so.

**Change.** Add a paragraph headed **"Potential Impact on DAF and DoW Capabilities"**, four to six sentences long, using the free page:
- **The setting.** Personnel relying on AI summaries of logistics, maintenance or status reports, where several AI tools may draw on the same upstream report. `[AUTHOR: confirm settings you can describe accurately]`
- **The risk.** Apparent consensus that is really one source repeated.
- **What the work provides:**
  - evidence displays and diagnostic questions that help people calibrate reliance and repair trust after errors
  - measures of when AI consensus deserves reliance
- **What not to add.** No program names and no claims about how DoD currently works, unless the author supplies them.

### 4. Fix the adviser/evaluator mismatch; describe PeerEval accurately

> Consider three advisers that report a shipment has arrived. All cite summaries derived from one outdated notice; a revised log records a delay.

> PeerEval can provide the experimental interface; the research contribution will be the methods and findings rather than the interface itself.

**Why.**
- **The example doesn't match the aims.** It shows three *advisers* agreeing on an answer. The question and Aim 1 concern a panel of *evaluators* judging one adviser's advice ("Evaluators will first judge candidate answers independently"). A reader outside NLP won't know which agreement the person actually sees.
- **PeerEval is described beyond its public page.** That page shows a PRD-based leaderboard on which seven LLMs answer and judge each other. It shows no human-study interface, and the paper never says what PeerEval is.

**Change.**
- **Rewrite the example.** One AI adviser says the shipment arrived. Three AI evaluators endorse the advice, but all three checked summaries of the same outdated notice. A revised log records a delay. Define "adviser," "evaluator panel" and "evaluation record" once, early.
- **Replace the PeerEval sentence** with an accurate one. For example: "PeerEval, the PI's public PRD-based leaderboard in which seven LLMs answer and judge each other, will be extended to host the studies and offers a ready panel for measuring evaluator dependence." `[AUTHOR: confirm this description]`

### 5. Show behavioral-study capacity and position the computational methods

> The PI will seek consultation on behavioral study design and power analysis before confirmatory data collection.

> On independently adjudicated development cases, a regularized statistical model will separate reviewer skill, task difficulty, and shared source effects.

> The system will select up to three follow-up questions using estimated error-detection value and interaction cost.

> We will also measure damage from inappropriate challenges, including correct advice changed to an incorrect answer.

**Why.**
- **Behavioral expertise is the main feasibility risk.** T&I reviewers will look for it, and a computer science PI who "will seek consultation" is a weak point.
- **Aim 1 rests on classical work it doesn't cite.** Estimating rater skill and item difficulty is classical rater aggregation (Dawid & Skene, 1979). What is new is dependence through shared evidence sources, which provenance makes observable.
- **Harmful revisions are a known LLM failure.** Correct answers changed under challenge are a form of sycophancy, which Sharma et al. report is general across assistants.
- **One phrase repeats another submission.** "Estimated error-detection value" appears verbatim in the PI's CCMI white paper, and the program officers coordinate their feedback.

**Change.**
- **Team paragraph:**
  - Name a behavioral-science consultant or collaborator only if one is confirmed. `[AUTHOR: name and role, or "none confirmed"]`
  - Otherwise keep the concrete plan already in the paper, and add the PI's relevant experience with human evaluation. `[AUTHOR: e.g., IQA-EVAL's validation against human ratings]`
- **Aim 1:** cite Dawid & Skene (1979), and state that the new element is source-level dependence among LLM evaluators.
- **Aim 2:**
  - Cite Sharma et al. where harmful revisions are discussed.
  - Reword "estimated error-detection value," for example "how likely a question is to expose an error, relative to its cost."

### 6. Cite one closely related paper from the Air Force trust-research community

I found no research publication by Dr. Steckman that bears on this project. Her findable work is a contribution to a 2016 Strategic Multi-Layer Assessment white paper on cognitive engagement, and a reference book, *Examining Internet and Technology around the World*. Citing those would read as decoration. The closest relevant work from the Air Force trust community is a review by AFRL researchers:

- **Lyons, Sycara, Lewis & Capiola (2021), "Human–Autonomy Teaming: Definitions, Debates, and Directions."** It argues that trust in human–autonomy teams depends partly on perceived benevolence and on how machines communicate intent and repair trust after violations.

**Change.** Add one citation, in one of two places:
- **In Study 2**, where trust repair after errors is introduced.
- **Or in the revised fit sentence**, where the person, the AI adviser and the evaluator panel are described as a heterogeneous team.

Make the citation do real work in the sentence; do not add praise.

## Later — leave for the full proposal

- The dependence model and calibrator, the reference-label protocol, and the features used to choose questions.
- Power simulations, final sample sizes and attrition. Also test at the naturally occurring error rate, and with participants whose backgrounds resemble DAF users.
- The data management plan, measurable benchmarks for each year, and current and pending support.

## Verified citations you may add

```bibtex
@article{lee2004trust,
  title={Trust in Automation: Designing for Appropriate Reliance},
  author={Lee, John D. and See, Katrina A.},
  journal={Human Factors},
  volume={46}, number={1}, pages={50--80}, year={2004}
}
@article{yousif2019illusion,
  title={The Illusion of Consensus: A Failure to Distinguish Between True and False Consensus},
  author={Yousif, Sami R. and Aboody, Rosie and Keil, Frank C.},
  journal={Psychological Science},
  volume={30}, number={8}, pages={1195--1204}, year={2019},
  doi={10.1177/0956797619856844}
}
@article{dietvorst2015algorithm,
  title={Algorithm Aversion: People Erroneously Avoid Algorithms after Seeing Them Err},
  author={Dietvorst, Berkeley J. and Simmons, Joseph P. and Massey, Cade},
  journal={Journal of Experimental Psychology: General},
  volume={144}, number={1}, pages={114--126}, year={2015},
  doi={10.1037/xge0000033}
}
@article{bonaccio2006advice,
  title={Advice Taking and Decision-Making: An Integrative Literature Review, and Implications for the Organizational Sciences},
  author={Bonaccio, Silvia and Dalal, Reeshad S.},
  journal={Organizational Behavior and Human Decision Processes},
  volume={101}, number={2}, pages={127--151}, year={2006}
}
@article{dawid1979maximum,
  title={Maximum Likelihood Estimation of Observer Error-Rates Using the {EM} Algorithm},
  author={Dawid, A. P. and Skene, A. M.},
  journal={Applied Statistics},
  volume={28}, number={1}, pages={20--28}, year={1979},
  doi={10.2307/2346806}
}
@article{lyons2021hat,
  title={Human--Autonomy Teaming: Definitions, Debates, and Directions},
  author={Lyons, Joseph B. and Sycara, Katia and Lewis, Michael and Capiola, August},
  journal={Frontiers in Psychology},
  volume={12}, pages={589585}, year={2021},
  doi={10.3389/fpsyg.2021.589585}
}
@article{sharma2023sycophancy,
  title={Towards Understanding Sycophancy in Language Models},
  author={Sharma, Mrinank and Tong, Meg and Korbak, Tomasz and Duvenaud, David and Askell, Amanda and Bowman, Samuel R. and Cheng, Newton and Durmus, Esin and Hatfield-Dodds, Zac and Johnston, Scott R. and Kravec, Shauna and Maxwell, Timothy and McCandlish, Sam and Ndousse, Kamal and Rausch, Oliver and Schiefer, Nicholas and Yan, Da and Zhang, Miranda and Perez, Ethan},
  journal={arXiv preprint arXiv:2310.13548}, year={2023}
}
```

All seven existing entries in `references.bib` were checked and resolve. That covers PRD, IQA-EVAL, Kim et al. (ICML 2025), Kohli (arXiv 2605.29800), Schemmer et al. (IUI 2023), Buçinca et al. (2021) and Gor et al. (arXiv 2605.28255).

## Sources checked

- [Trust and Influence program description](https://community.apan.org/wg/afosr/w/researchareas/7676/trust-and-influence)
- [Yousif, Aboody & Keil 2019](https://doi.org/10.1177/0956797619856844)
- [Lee & See 2004](https://doi.org/10.1518/hfes.46.1.50_30392)
- [Dietvorst et al. 2015](https://doi.org/10.1037/xge0000033)
- [Bonaccio & Dalal 2006](https://ideas.repec.org/a/eee/jobhdp/v101y2006i2p127-151.html)
- [Dawid & Skene 1979](https://doi.org/10.2307/2346806)
- [Sharma et al.](https://arxiv.org/abs/2310.13548)
- [Kohli 2026](https://arxiv.org/abs/2605.29800)
- [Gor et al. 2026](https://arxiv.org/abs/2605.28255)
- [Kim et al. 2025](https://proceedings.mlr.press/v267/kim25e.html)
- [IQA-EVAL](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a23b26eaaefd187973658f5001f4fe-Paper-Conference.pdf)
- [PeerEval](https://peereval-ai.github.io/)
- [Lyons et al. 2021](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.589585/full)
- [SMA white paper on cognitive engagement (contributor list)](https://nsiteam.com/social/bio-psycho-social-applications-to-cognitive-engagement/)
