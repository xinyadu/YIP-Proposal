# ONR FY27 YIP — Program Officer Feedback and Proposal Revision Notes

**Updated:** October 26, 2026  
**Sources:** Xinya Du's October 13–24, 2026 email correspondence with Dr. Predrag (“Pedja”) Neskovic and Dr. Behzad Kamgar-Parsi (ONR Code 311).  
**Purpose:** Internal working notes for revising the white papers, full technical proposal, CV, and institutional support materials. This is a synthesis, not an official ONR policy document. Comments about one research direction should not automatically be applied to the other.

## Executive summary

- **Predrag / collective intelligence and peer evaluation:** Confirmed that the proposed direction fits his Mathematical Data Science program (October 14). After reviewing the revised four-page white paper, he replied on **October 23**: “Very good, I like it.” He especially endorsed structuring the project around **one big question with distinct supporting tasks**. His remaining substantive critique is that the proposed methods **appear ad hoc** despite being sensible: the full proposal needs clearer *why-these-methods* arguments and, where feasible, mathematical grounding. He explicitly advised proceeding with the full proposal, getting a strong department-chair support letter, and sending short descriptions of past achievements and the importance of the future research. This is encouraging feedback, **not a funding commitment**.
- **Behzad / knowledge-grounded reasoning for agents:** Described the topic as interesting (October 13), but judged the approach **rather ad hoc** and the **evaluation and naval relevance insufficiently broad and comprehensive** in the one-page white paper. He emphasized three criteria in order: **(1) CV/track record and peer recognition, (2) principled and innovative basic research with broad applicability and rigorous guarantees, (3) tangible university support**. He also described a highly selective, multi-stage review process. This was feedback on a **separate proposal direction**, not a rejection of Predrag's project.
- **Shared implication:** Keep a coherent, accessible overarching question; replace a catalog of plausible mechanisms with a smaller number of justified scientific principles; explain the proposed methods with rigorous formulations, clear assumptions, and limitations; make the PI record and institutional commitment unusually strong.

## 1. Predrag Neskovic — peer evaluation, evidence-grounded deliberation, collective learning

### Confirmed feedback and chronology

| Date | Direct feedback / communication | Implication |
| --- | --- | --- |
| Oct 14 | “Yes, your proposed research is a good fit for my program.” He also noticed an incorrect “AFOSR YIP” document label and warned that the same proposal cannot be submitted to two agencies. | Correct labeling and keep submissions distinct. Fit does not guarantee selection. |
| Oct 20 | Following the meeting, sent **six questions** for the white paper and set the maximum at **four pages excluding references**. | Structure the research narrative around a single problem and a comprehensible answer to all six questions. |
| Oct 23 (Xinya's submission) | Xinya submitted the four-page revision, explicitly saying it was organized around the six questions, focused on one central problem, written for a cross-disciplinary panel, differentiated the weighting method from impartial peer review/panel selection, and treated AI-assisted peer review as an application. | These were communicated revision choices, not separate endorsements of every detail. |
| Oct 23 (Predrag's reply) | “Very good, I like it.” Approved the **one overarching problem with separate tasks** structure. Methods “make sense but they seem ad-hoc”; requested stronger justification for choosing them, “if possible, a more mathematically justified reasoning.” | **Principal remaining technical action:** explain the foundation and necessity of each mechanism, not merely its intuitive utility. |
| Oct 23 (same reply) | “The next steps: focus on writing the proposal. Make sure that you get a strong letter of support from the chair of your department. Send me the description of your past achievements and the importance of the proposed (future) work. You are all set. Good luck!” | Shift effort from repeated white-paper polishing to the full proposal, support letter, and two short statements. |

### Predrag's six questions (from Oct 20 email)

1. What problem are you trying to solve?
2. Why is it important?
3. How is it solved today, and what are the limitations of current solutions?
4. How will you solve it; what is new and better about your approach; why should it work?
5. What limitations will your solutions have?
6. What impact would success have?

### How to apply this to the full proposal

**Preserve the structure that Predrag explicitly liked.** Use *reliable collective reasoning by multiple AI agents* (or the final proposal's precise central question) as a single unifying scientific problem. Present peer evaluation, evidence-grounded deliberation, and collective learning as **complementary tasks that resolve identifiable subproblems**—not three loosely related inventions.

**Prioritize a principled through-line.** For each thrust, specify: (a) the precise failure mode; (b) the assumption or formal model explaining the failure; (c) the proposed method and why it addresses that failure; (d) a tractable property, derived objective, or testable hypothesis; and (e) limits or failure regimes. For instance, correlated evaluator errors undermine naive voting; traceable evidence and independent checks can constrain ungrounded consensus; diagnostic feedback can target the source of errors. These are **suggested formulations**, not formal models that Predrag mandated or independently validated.

**Avoid overcomplicating the white paper.** Predrag approved its high-level organization. Add formal intuition, carefully chosen equations, assumptions, or guarantees in the *full proposal* where they illuminate the argument; avoid proliferating modules or mathematical claims with no proof.

**Audience and positioning.** Xinya explicitly told Predrag the revised paper addressed a cross-disciplinary panel and distinguished peer weighting from impartial peer review and panel selection. Preserve those explanations and make the Navy-relevant use case credible without turning the program into a narrow application demonstration.

## 2. Behzad Kamgar-Parsi — knowledge-grounded reasoning and self-improving agents

### Specific October 13 feedback

Behzad said that the topic was **interesting**, but:
- The technical approach appeared **“rather ad hoc.”**
- The **evaluation** was not sufficiently broad or comprehensive.
- **Naval relevance** was also insufficiently broad or comprehensive.
- He acknowledged these shortcomings could be due to the tight one-page format.

This feedback refers to the **knowledge-grounded reasoning for AI agents** white paper, with neuro-symbolic evidence representations, fine-grained self-assessment, and learning from diagnostic feedback. Do not conflate its technical critique with Predrag's subsequent acceptance of the revised collective-reasoning white paper.

### Selection criteria, in Behzad's stated order

1. **CV and demonstrated impact / peer recognition.** Submit a *full* CV, not just a two-page summary. Behzad explicitly named all publications, best-paper and other awards/scholarships (including earlier career), conference/workshop organization, area-chair and program-committee roles, journal editorships, invited talks, and other evidence of research influence.
2. **Principled, innovative basic research** with **broad applicability and rigorous guarantees**. The proposed scientific advance must be more than an ad hoc assembly of techniques.
3. **University commitment.** A chair/dean letter should document substantive support, for example startup resources, teaching release, university-supported graduate students, matching funds, or other concrete commitments **only if actually authorized**.

### Selection process as Behzad described it

1. An ad hoc panel first identifies a **small pool of the most competitive CVs**.
2. That pool's proposals receive particularly rigorous examination for innovation; other proposals also receive review, but less intensive consideration.
3. Program officers recommend proposals aligned with their current focus areas from among panel selections.
4. ONR department leadership then selects **only five** of the most competitive recommended applications according to that year's departmental needs.

**Important:** This is Behzad's description of the process in his email, **not a verified rule for every future cycle** or an estimated probability of funding. Program fit, strong CV, and a positive officer response should not be interpreted as guaranteed advancement through these steps.

### Applying Behzad's feedback

For a Behzad-facing proposal, explain precisely what is novel in the diagnosis of perception/reasoning/action errors, formalize the causal or diagnostic assumptions if defensible, and tie those diagnostics to justified learning updates rather than listing model components. Broaden evaluation across tasks, error classes, uncertainty, settings and baselines, and articulate general naval applicability. For Predrag's proposal, Behzad's selection/CV/letter advice is useful cross-cutting context; the exact *technical* recommendations belong to his distinct concept.

## 3. Prioritized action items for the Predrag full proposal

| Priority | Task | Done when |
| --- | --- | --- |
| P0 | **Write the full technical proposal around one core scientific question.** | Every thrust contributes explicitly to a shared outcome and the six white-paper questions have clear answers. |
| P0 | **Remove the appearance of ad hoc technique selection.** | Every major mechanism has an explicit motivation, assumptions, mathematically grounded formulation where feasible, and connection to a specific failure mode. |
| P0 | **Strengthen the complete CV.** | A comprehensive track record includes publications, awards and scholarships, invited talks, community leadership, editorial and review roles, and concrete evidence of impact. |
| P0 | **Secure a strong, signed department-chair support letter.** | The letter emphasizes achievements, institutional commitment, and only genuinely approved tangible resources or release arrangements. |
| P0 | **Prepare the two short statements requested by Predrag.** | One concisely communicates major past achievements and peer recognition; the other explains the importance and potential impact of the proposed future research. Send as requested, without assuming that these replace formal application documents. |
| P1 | **Make the rigor concrete but proportionate.** | Theoretical properties, assumptions, ablations, and possible failure cases are linked to the research aims; no unsupported universal guarantees. |
| P1 | **Broaden experimental design and naval relevance.** | Clear quantitative tests across environments, error correlations, adversarial/outdated evidence, model diversity, and resource constraints, with plausible naval relevance and broad civilian applicability. |
| P1 | **Audit consistency and agency labels.** | White paper, proposal, abstract, CV, support letter, and focus area align; no accidental AFOSR labeling or duplicate agency submission. |

## 4. Suggested full-proposal narrative checklist

- **Problem:** Why do collectives of AI agents still fail even when each agent appears capable?
- **Scientific obstacle:** Correlated judgments, unsupported consensus, and uninformative feedback can magnify rather than cancel error.
- **Core hypothesis:** A collective can become more reliable when it can *assess whose judgment is credible*, *resolve conflicts with evidence*, and *learn from diagnosed failures* under stated assumptions.
- **Thrust 1 / peer assessment:** Formalize evaluator quality and dependence; justify any weighting or updating rule, its identifiable inputs, and its limits.
- **Thrust 2 / deliberation:** Formulate when additional verification is worth its cost, what constitutes independent evidence, and how to handle unresolved disagreement or abstention.
- **Thrust 3 / collective learning:** Define the feedback signal, link diagnosis to actionable improvement, and test whether gains transfer beyond the observed trajectories.
- **Cross-cutting:** State assumptions, measurable hypotheses, appropriate baselines, limits, failure cases, naval relevance, and expected impact. Do not promise formal guarantees without defensible derivation.

## 5. Important distinction between direct feedback and our interpretation

**Directly attributed to Predrag:** program fit; six framing questions; four-page white-paper cap; approval of the revised paper and its one-question/multiple-tasks structure; concern that methods look ad hoc; request for mathematical justification; strong chair letter; short past-achievements/future-impact descriptions; move on to full proposal.

**Directly attributed to Behzad:** interesting topic but ad hoc methods, insufficient evaluation and naval relevance; priority order of CV, principled basic research, university support; recommendation for a full CV; examples of institutional commitment; his description of the selection sequence and final five.

**Our synthesis / recommendations, not direct officer instructions:** specific possible mathematical frameworks for peer correlation, evidence checks, and error diagnosis; the P0/P1 prioritization; particular evaluation stress tests; the proposed unifying hypothesis and narrative checklist.

## 6. Source email references

- **Predrag**, “RE: ONR YIP Research Idea – Collective Intelligence through Peer Evaluation and Deliberation,” **Oct 23, 2026**, response to four-page revised paper.
- **Predrag**, same subject, **Oct 20, 2026**, six questions and ≤4-page white-paper requirement.
- **Predrag**, same subject, **Oct 14, 2026**, program-fit confirmation and agency-label warning.
- **Behzad**, “RE: ONR YIP Research Idea – Knowledge-Grounded Reasoning for AI Agents,” **Oct 13, 2026**, critiques, selection criteria, and review-process explanation.

*Note: dates above refer to the local calendar dates in the email thread; Outlook's UTC received timestamps may fall on the following day. This document does not contain or reproduce other researchers' confidential proposal materials.*
