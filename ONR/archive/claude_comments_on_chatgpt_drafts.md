# Comments on the ChatGPT ONR YIP brief topic descriptions (round 2)

Reviewer: Claude · Date: 2026-10-12 · Scope: the four notes on `main` at `e60d15f` (`ONR/<po>/main.tex` and `white_paper_<po>.pdf`; text last changed in the 15:11 PT commits) and `chatgpt_revision_response.md`. Checked against the FY27 ONR YIP NOFO (N0001426SF004), ONR's program-officer directory and program pages (today), the AFOSR papers in `../ben`, `../doug`, `../laura`, and the public record of every cited paper.

This file replaces my earlier comments, which remain in git history. My alternative one-pagers are the `claude_*.pdf` files in this folder; their sources are in [`claude_src/`](claude_src/). Statements marked *(judgment)* are my opinion; everything else is checked against the sources at the end.

## Bottom line

**The form is now right.** Each note has the PI, Program Officer, NOFO number, and a proposed S&T Focus Area in its header. Each calls itself a brief topic description, states a hypothesis, gives a concrete example, links prior work, and describes Naval relevance without disclaimers. Keep all of that.

**Must fix before any note is sent**

1. **Two links are wrong** (Kamgar-Parsi and Goolsby notes).
   - **FaithScore.** `aclanthology.org/2024.findings-emnlp.287` is Ma et al., "Learning Autonomous Driving Tasks via Human Feedbacks with Large Language Models". FaithScore is [`2024.findings-emnlp.290`](https://aclanthology.org/2024.findings-emnlp.290/), pp. 5042–5063 (the pages already in `references.bib`).
   - **FGAIF.** The notes and both `references.bib` files use OpenReview ID `QhJw5CUVd7`. Your homepage and the TMLR 2025 record give `Qhfw5CUVd7`, with a lowercase f. Fix the ID or use [arXiv 2404.05046](https://arxiv.org/abs/2404.05046).
2. **The last edit removed what made each note distinct.** The 15:11 commits ("Strengthen … around program fit and research expertise") replaced each note's specific question with a broader one:
   - The Neskovic note now restates AFOSR Laura Aim 1 and Ben Aim 2.
   - The Morrison note moves back onto CAREER's ground.
   - The Goolsby note demotes deception, which her program page names.
   - With the Morrison and Goolsby retitles, three of the four titles now begin "Knowledge-Grounded" (Kamgar-Parsi's already did).

   `chatgpt_revision_response.md` still describes the earlier versions, so it no longer matches `main`. Details are in Section 2.
3. **The Morrison note cannot go out as written.** Its header reads "Dr. Jeffrey Morrison, Code 341 (assignment unconfirmed)", and he is not in ONR's program-officer directory. Choose the officer first; the right content depends on who it is (Section 3).
4. **The KAIROS ranking has no independent public source.** Three notes say "the team achieved top performance among participants", and the Kamgar-Parsi note says "high-performing".
   - The only public statement is your own publications page: "Top ranking system at DARPA KAIROS Evaluation". It links to DARPA's KAIROS program page, which reports no evaluation results.
   - Neither RESIN demo paper (NAACL 2021, NAACL 2022) compares RESIN with other KAIROS teams, and I found no DARPA or university statement that does.
   - My first comments recommended this wording without flagging that it had no independent source. That was my error.
   - The claim is yours to make. If you have the evaluation results and would stand behind them if a PO asked, use your homepage's wording rather than "top performance among participants". Otherwise give the role only: "As a postdoc, the PI led system integration for the RESIN team in DARPA KAIROS ([RESIN-11](https://doi.org/10.18653/v1/2022.naacl-demo.7), NAACL 2022 Demo, first author)."
5. **All four notes use the same kind of scenario.**
   - Neskovic: "five agents assessing whether a coastal route has reopened"
   - Goolsby: "after flooding closes a coastal access route, later updates may contradict early reopening claims"
   - Morrison: "a port has closed, while a later message corrects its reopening time"
   - Kamgar-Parsi: a port-entry tide table

   The Neskovic and Goolsby examples are nearly the same: unreliable reports about whether a coastal route has reopened. If Krebs replaces Morrison, three notes go to Code 311. Give each note its own scenario.

**Should fix**

6. **Add the 2023 Amazon Research Award** ("Process-guided Fine-tuning for Answering Complex Questions") to the Kamgar-Parsi and Neskovic notes. It is publicly listed and on topic.
7. **Use the empty space.** Each page ends 1.7–2.0 inches above the bottom margin. Use a few of those lines for the fixes above and for one sentence that separates the topic from your closest pending work. Don't add a fourth aim.
8. **Housekeeping.**
   - The MEQA OpenReview ID (`snNuvAOQxB`) matches the NeurIPS 2024 record. Switching to the [proceedings page](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e560a0b22e4432003d0dba63ff8dc457-Abstract.html) is optional.
   - The folder READMEs say the notes use 10-pt type; they use 11-pt.
   - The repository is public. The ONR README names your DARPA, Amazon, and Google source proposals, and the AFOSR drafts are visible. If that isn't intended, make the repo private after this round; I would then need the Claude GitHub App to read it.

## 1. What I verified

| Claim in the notes | Status |
| --- | --- |
| Neskovic, Code 311, Mathematical Data Science | ✅ |
| Kamgar-Parsi, Code 311, AI / Machine Learning, Reasoning and Intelligence | ✅ Directory title "Artificial Intelligence Program Officer" |
| Goolsby, Code 341, Analytics, Modeling and Simulation (Local and Regional) | ✅ |
| Morrison, Code 341, Command Decision Making | ❌ Not in the directory. The only Morrison listed is Mr. Peter Morrison, Code 353 (Directed Energy). The CDM page lists three officers (Steinhauser, Squire, McKenna), none with a CDM title. |
| Krebs (the alternative), Code 311 | ✅ "Information Science & C2 Program Officer", named on the Command and Control program page |
| Proposed S&T Focus Areas | ✅ All names appear in the NOFO's list |
| FG-PRM (DOI), PRD (arXiv 2307.02762), HiPRAG (arXiv 2510.07794), QA-based event extraction (DOI) | ✅ |
| FaithScore link (`…287`) | ❌ Wrong paper; use `…290` |
| FGAIF OpenReview link (`QhJw5CUVd7`) | ❌ Mistyped. Your homepage and the TMLR record give `Qhfw5CUVd7`. |
| MEQA OpenReview link (`snNuvAOQxB`) | ✅ Matches the NeurIPS 2024 record |
| MuSiQue, ScienceQA, MAVEN-ERE, GDELT | ✅ Public datasets |
| 2024 NSF CAREER; "on consistent event graphs" (Morrison note) | ✅ Award 2340435, "Learning to Extract Consistent Event Graphs from Long and Complex Documents", start 2024-05-01 |
| KAIROS role | ✅ for involvement: you are first author of RESIN-11 (NAACL 2022 Demo), funded by DARPA KAIROS. "Led system integration" is your own description; I found no public source for or against it. |
| KAIROS ranking ("top performance among participants", "high-performing") | ❓ Self-reported only. Your publications page says "Top ranking system at DARPA KAIROS Evaluation"; no paper, DARPA, or university source says so. |
| 2023 Amazon Research Award | ✅ Public; not yet used in any note |

## 2. What the 15:11 edit changed

| Note | 14:59 version | Now on `main` (15:11) | Effect *(judgment)* |
| --- | --- | --- | --- |
| Neskovic | `b297fd5`, "Statistical Foundations for Reliable AI Reasoning under Compute Constraints". Dependence among one model's sampled traces; when to sample, check, or stop; risk control; accuracy–compute curves. | `96fc647`, "Reliable Collective Reasoning and Evaluation for AI Agents". Panels of agents and judges; "expertise and correlated errors"; "the effective number of independent assessments"; choosing the next check. | Restates Laura Aim 1 and Ben Aim 2 (table in Section 3). Drops the computation-versus-accuracy question, a stated thrust of the program. |
| Kamgar-Parsi | `1a3a166`. The tide-table mistake is "a violated precondition"; the third aim is "Turn self-assessment into selective action" (re-read, inspect a crop, fix a tool input, backtrack, or ask; "penalize unnecessary retries and missed deadlines"). | `a25ac16`. Ground, then diagnose, then self-improve. | Still the best fit, but less specific. The new first aim, "Ground multi-step reasoning in external knowledge", is infrastructure. |
| Morrison | `285ca2f`, "Distributed Event Reasoning and Information Fusion for Decision Support". Order-independent merging, standing queries for critical information requirements, bandwidth limits; centralized and last-writer-wins baselines. | `f3aebbc`, "Knowledge-Grounded AI Reasoning for Dynamic Decision Support". "Distributed nodes provide a demanding test case, but are not the only setting." | Aims 1–2 now sit on CAREER (event graphs from long documents) and next to Ben Aim 3 (revision after corrections). The new framing suits CDM; the old one suits Krebs's C2 program. |
| Goolsby | `f9416b8`, "Deception-Resilient Retrieval-Augmented Generation for Regional Situation Awareness". "treating five copied articles as five independent confirmations"; claims "marked supported, disputed, or unverified"; "Adapt … feedback from our vision-language work to textual RAG". | `2e10edb`, "Knowledge-Grounded Retrieval-Augmented Generation for Regional Situation Awareness". "We will investigate adversarial deception as a critical robustness challenge, while making accurate regional knowledge synthesis the primary research objective." | Demotes the part of the topic her program names: "Problems of reflexive control, deception, cyber-attack, and obfuscation". |

If the goal of the edit was to keep each topic close to your publication record, the 14:59 versions already did that. The trace statistics build on FG-PRM, PRD, and HiPRAG. The fusion note builds on your event-extraction work. The deception note builds on event extraction plus FaithScore and FGAIF.

**Recommendation** *(judgment)*:

1. Restore the 14:59 text for Neskovic, Kamgar-Parsi, and Goolsby: `git show b297fd5:ONR/predrag/main.tex`, `git show 1a3a166:ONR/behzad/main.tex`, `git show f9416b8:ONR/goolsby/main.tex`.
2. For the fourth note, choose by officer (Section 3).
3. Then apply fixes 1 and 4–6. The 14:59 versions have the same wrong FaithScore and FGAIF links, the same KAIROS ranking, and port or route examples.

## 3. Note by note

### Kamgar-Parsi: strongest fit, send first *(judgment)*

Keep the hypothesis (step-level diagnosis beats outcome-only training) and the program language (self-assessment, uncertain reasoning, planning).

- **Title.** Put "self-assessment" in it. It is the program page's own term: "Reasoning with uncertain and qualitative information, as well as self-assessment". For example: "Learning Typed Self-Assessment for Tool-Using AI Agents".
- **Aims.** Replace "Ground multi-step reasoning in external knowledge" with the 14:59 aim "Turn self-assessment into selective action". A typed diagnosis is valuable because it says what to do next. The current third aim acts on the diagnosis only generically ("revise an erroneous step, continue a valid partial plan, or gather additional evidence") and never ties the next action to the error type.
- **Example.** The local-time-versus-UTC error is the same kind of mistake as the AFOSR Ben example (a report time read as an event time). Consider an error that is not about time, such as reading the wrong line of a photographed document.
- **Evaluation.** "Controlled tool-use environments" is unnamed. Name an existing benchmark, or say you will build tasks with injected argument errors and held-out tools.
- **Scope.** ScienceQA is a set of multimodal science questions, about half with an image, not a scene-understanding benchmark. Keep images as one evidence type, and don't widen the claim.
- **PI evidence.** Fix the FaithScore and FGAIF links and the KAIROS wording, and add the Amazon Research Award.
- **Overlap.** Ben uses FG-PRM as a baseline, and Doug extracts applicability conditions for scientific calculations. One sentence in the full proposal covers both: here, agents learn to diagnose their own steps by error type and act on the diagnosis.

### Neskovic: restore the 14:59 version

The current note maps onto your AFOSR papers almost clause for clause:

| Neskovic note (now) | AFOSR text |
| --- | --- |
| "Use shared citations, agreement patterns, and limited reference labels to infer expertise and correlated errors"; "quantify the effective number of independent assessments" | Laura Aim 1: "fit a regularized model of reviewer skill, task difficulty, and shared source effects"; "how much independent checking is needed before a panel's agreement becomes a useful reliability signal" |
| "five agents … may all cite summaries copied from one incorrect bulletin" | Laura: "three references to one notice will be distinguished from support drawn from separately checked records" |
| "a decision between asking another agent, consulting an independent source, testing an inference, or stopping"; "sequential risk control" | Ben Aim 2: "choose the next check using its cost, its estimated effect on the acceptance decision, and the premises that share its source"; "keeping the error rate among accepted answers below a specified level" |

The 14:59 version asks a different question: how dependent one model's sampled traces are, and when extra computation is worth spending. That question is distinct from both AFOSR papers. It also fits two interests on the program page. The program wants "rigorous mathematical and algorithmic answers to questions" now "addressed using heuristics or non-principled approaches". It also wants to balance limited computing against accuracy. Majority voting and fixed best-of-N are exactly such heuristics *(judgment)*.

- **Keep from the current note:** abstaining "when apparently unanimous opinions share weak support", and error at matched coverage.
- **Phrase guarantees as questions.** Write "which risk-control guarantees survive dependent samples", not a promise of guarantees; the 14:59 text already does this.
- **Two adjacencies remain even after restoring.** Laura Aim 2 uses "extra samples from one model" as a comparison condition, and Ben Aim 2 controls the error rate among accepted answers. Name both in the full proposal. The ONR object is the statistics of one system's own samples and the decision of how much computation to spend.

### Morrison: choose the officer first

- **If the officer is Krebs (Code 311, C2):** use the 14:59 content (`285ca2f`).
  - His program page lists "Development of a common tactical picture", "Automated Information Integration Across Enterprise Sensors and Information Stores", and decision making with "uncertain information, out of sequence information". Order-independent fusion of text-derived events over degraded links speaks to all three.
  - Consider the focus area "Command, Control, Communications, Computers, Cyber, Intelligence, Surveillance, and Reconnaissance (C5ISR) and Naval Space", sub-area "Intelligence, Decision Superiority, Command and Control (C2), and Combat Systems".
  - The `\POline` suggested in `chatgpt_revision_response.md` works.
- **If ONR names a CDM officer:** the current framing fits better. The CDM page describes decision support tools "proactive in providing relevant information at appropriate times" and lists "Developing proactive decision support tools for military command and control".
  - Add one sentence each separating the note from CAREER (consistent event graphs from documents) and from Ben Aim 3 (revising conclusions after a correction).
  - The Naval paragraph names both "command decision making and command-and-control interests". Name one program.
- **Either way:** replace the port example.

To find out, email ONRYIP@navy.mil, or any Code 341 officer, and ask who manages Command Decision Making.

### Goolsby: put contested information back at the center

- **Hypothesis.** Replace the second sentence. It reads like a reply to a reviewer, and it demotes what her program asks for. A possible replacement: "In a contested information environment, copied, delayed, and deliberately false reports are the normal condition, so the event knowledge that grounds generation must record where each claim came from and whether it is disputed."
- **Restore the 14:59 specifics:**
  - "treating five copied articles as five independent confirmations"
  - claims "marked supported, disputed, or unverified"
  - "Adapt … feedback from our vision-language work to textual RAG"

  FaithScore and FGAIF are vision-language papers. A PO who opens them should already know from the note that you are adapting them.
- **Example.** Replace the reopened-route scenario, which duplicates the Neskovic note.
- **Metric.** Define "sensitivity to deception", for example as the rate at which planted false claims appear as supported.
- **Overlap.** "distinguish independent corroboration, unresolved contradiction, and duplicated claims" is close to Laura's discounting of shared sources. The object differs: source reports that feed generation, with no human-reliance study. One sentence in the full proposal is enough.

## 4. Overlap with your pending and funded work

| ONR note | Current `main` overlaps | After restoring 14:59 (or Claude version) | What to state in the full proposal |
| --- | --- | --- | --- |
| Kamgar-Parsi | Ben (learned evidence checks; FG-PRM as a baseline); Doug (applicability conditions). Minor. | Same | Agents diagnose their own steps by error type and use the diagnosis to act and to train. |
| Neskovic | Laura Aim 1 and Ben Aim 2. Major. | Laura Aim 2's "extra samples from one model" condition; Ben Aim 2's error control. Minor. | The statistics of one system's own traces, and how much computation to spend. |
| Morrison / Krebs | CAREER; Ben Aim 3 (corrections). Moderate. | CAREER as the foundation; correction handling is adjacent to Ben Aim 3. | Order-independent convergence across nodes, and bandwidth-limited sharing. |
| Goolsby | CAREER; Laura (duplicated versus independent sources). Moderate. | Same, smaller | Contestation tracked through retrieval and generation; adversarial test environments. |

The NOFO warns that current and pending support "may render an applicant ineligible for funding". You will also submit only one AFOSR YIP proposal, so the overlap that matters is with the AFOSR topic you actually submit:

- If it is Laura, don't send the current Neskovic note.
- If it is Ben, separate the Neskovic stopping rules and the fourth note's correction handling from Ben Aims 2 and 3.

## 5. The Claude versions

**Files.** Each is exactly one page, built with XeLaTeX and the EB Garamond fonts in `../ben/fonts`.

| File | Title |
| --- | --- |
| [`claude_behzad_kamgar_parsi.pdf`](claude_behzad_kamgar_parsi.pdf) | Self-Assessing AI Agents: Learning Where Their Own Reasoning Fails and What to Do Next |
| [`claude_predrag_neskovic.pdf`](claude_predrag_neskovic.pdf) | When Is More Computation Worth It? Statistical Foundations for Aggregating Dependent AI Reasoning Traces |
| [`claude_william_krebs.pdf`](claude_william_krebs.pdf) | Convergent Event Knowledge for a Common Tactical Picture over Degraded Networks (replaces Morrison) |
| [`claude_rebecca_goolsby.pdf`](claude_rebecca_goolsby.pdf) | Contest-Aware, Event-Grounded Retrieval-Augmented Generation for Regional Situation Awareness |

**What changed from my previous versions**

- **KAIROS:** the role only, linked to RESIN-11. The ranking is left out; add your homepage wording if you decide to keep it.
- **Links:** every paper is linked (DOI, arXiv, or NeurIPS page), and I opened each link today. FaithScore now points to `…290`.
- **Scenarios:** each note has its own, and none involves a port closure, a reopened route, or a time-zone error.
  - Kamgar-Parsi: a quantity read from the wrong line of a photographed packing list
  - Neskovic: a fuel estimate in which 15 of 20 sampled traces reuse one misread consumption rate
  - Krebs: a loitering-vessel report and a later status update, arriving in opposite orders at two nodes
  - Goolsby: a fabricated water-contamination rumor after a typhoon
- **PI evidence:** the Amazon Research Award is in the Kamgar-Parsi and Neskovic notes. The Neskovic and Krebs notes each say which prior work supplies the starting tools and what is new.
- **Checking:** a separate reviewer checked every link, quotation, and factual claim in these notes and in this file against its source. Its corrections are applied: hedged statements about prior work, a convergence claim limited to the merge layer, and the NOFO's exact focus-area wording.

The Claude versions are alternatives. ChatGPT can borrow from them, or you can send one directly.

**Confirm before sending any version**

- "Led system integration for the RESIN team" is your own description (it matches proposal #3). Also decide whether to state the KAIROS ranking.
- Krebs, or a CDM officer confirmed by ONR.
- Which AFOSR topic you will submit, and whether NSF proposal #2 is pending; both affect current and pending support.
- Eligibility given your appointment. Ask ONRYIP@navy.mil before Oct 16.

## 6. Sending and deadlines

- **This week (Oct 12–13).** Email each officer with ONRYIP@navy.mil on cc (first email only). Attach the PDF under a descriptive name, such as `Du_UTD_ONR-YIP_topic_Kamgar-Parsi.pdf`, not `white_paper_behzad.pdf` or `claude_*.pdf`. Ask for a 20-minute call.
- **Deadlines.** Eligibility and technical questions are due **Oct 16, 5 pm ET**, and grants questions Oct 29. Full applications are due **Oct 30, 5 pm ET** through UTD; check the Office of Sponsored Programs' internal deadline.
- **One application per PI.** My ranking is unchanged: Kamgar-Parsi, Goolsby, Krebs, Neskovic *(judgment, based on program-page fit and your publication record)*.
- **Full proposal reminders:**
  - 12-pt Times New Roman, single-spaced, 1-inch margins; Technical Proposal of at most 20 pages
  - Abstract marked "Approved for Public Release"
  - Typical award $750K over 36 months, at most $250K per 12 months
  - SF-424 field 4b in the form `311 [Kamgar-Parsi, Behzad]`
  - Field 11 asks for an "ONR White Paper Tracking Number" although white papers are not accepted; ask ONRYIP@navy.mil what to enter

**Email template**

> **Subject:** FY27 ONR YIP — brief topic description for discussion (Xinya Du, UT Dallas)
>
> Dear Dr. [Last name],
>
> I am an assistant professor of computer science at UT Dallas and plan to apply to the FY27 ONR Young Investigator Program (N0001426SF004). I have attached a one-page description of a research topic that I believe fits your [program name] program: [one-sentence summary].
>
> I would be grateful for your view on whether this direction matches your program's priorities, and on how to strengthen its Naval relevance. Would you have 20 minutes for a call this week?
>
> Thank you for your time.
>
> Best regards,
> Xinya Du
>
> *cc: ONRYIP@navy.mil (first email only)*

## Sources

- ONR: [program-officer directory](https://www.onr.navy.mil/our-research/our-program-officers); program pages for [Mathematical Data Science](https://www.onr.navy.mil/organization/departments/code-31/division-311/mathematical-data-science), [Machine Learning, Reasoning and Intelligence](https://www.onr.navy.mil/organization/departments/code-31/division-311/machine-learning-reasoning-and-intelligence), [Command and Control](https://www.onr.navy.mil/organization/departments/code-31/division-311/command-and-control), [Command Decision Making](https://www.onr.navy.mil/organization/departments/code-34/division-341/command-decision-making-cdm), and [Analytics, Modeling and Simulation](https://www.onr.navy.mil/organization/departments/code-34/division-341/analytics-modeling-and-simulation-local-and-regional)
- Papers:
  - [FaithScore, Findings of EMNLP 2024](https://aclanthology.org/2024.findings-emnlp.290/), and the paper the notes link instead: [Ma et al. 2024](https://aclanthology.org/2024.findings-emnlp.287/)
  - [FGAIF, arXiv 2404.05046](https://arxiv.org/abs/2404.05046)
  - [MEQA, NeurIPS 2024 Datasets and Benchmarks](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e560a0b22e4432003d0dba63ff8dc457-Abstract.html)
  - [RESIN-11, NAACL 2022 Demo](https://aclanthology.org/2022.naacl-demo.7/)
  - [AALC, arXiv 2506.20160](https://arxiv.org/abs/2506.20160)
  - [Consistent event–event temporal relation extraction, MATCHING 2023](https://aclanthology.org/2023.matching-1.3/)
- Awards: [NSF award 2340435](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2340435); [Amazon Research Award listing](https://www.amazon.science/research-awards/recipients/xinya-du)
- Repository: `git log -- ONR/<po>/main.tex` for the commit history cited in Section 2; `../laura/main.tex` and `../ben/main.tex` for the AFOSR quotations
