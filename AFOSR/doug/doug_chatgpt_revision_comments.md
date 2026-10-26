# Revision comments for ChatGPT — Doug Riecken (Science of Information, Computation, Learning, and Fusion) white paper

**How to use:** attach `doug/main.tex` and `doug/references.bib` to ChatGPT, then paste everything below the line.

**Check this yourself before editing.** In the current AFOSR Open BAA (FA9550-26-S-0001, Amendment 0001, posted 21 Aug 2026), the Information and Networks team lists six programs, A.2.a–A.2.f. A.2.f is now "Complex Networks" (Dr. Donald K. Wagner). In the initial FY26 announcement, A.2.f was "Science of Information, Computation, Learning, and Fusion" under Dr. Doug Riecken. I could not read the amendment's A.4 section, where CCMI and Trust and Influence now sit, so the program may have moved there.

Search the amendment PDF for "Riecken" and "Science of Information." If neither appears, confirm with Dr. Riecken or afosryip@us.af.mil before submitting under this discipline. The YIP notice seeks proposals "in the research areas of interest identified in the most recent Broad Agency Announcement".

---

You are revising an AFOSR FY27 Young Investigator Program (YIP) white paper written in LaTeX. Treat it as an initial white paper, not a full proposal. It needs a compelling basic-research question, a credible approach, and a clear link to the PI's expertise. Its technical commitments must be meaningful and defensible. Apply the revisions below in priority order.

## Context

- **Paper:** "Neural-Symbolic Verification and Refinement of LLM-Generated Scientific Claims."
- **Portfolio:** Science of Information, Computation, Learning, and Fusion, Dr. Doug Riecken. `[AUTHOR: confirm section number in the current BAA]`
- **PI:** Xinya Du, The University of Texas at Dallas.
- **Deadline:** 9 October 2026, 11:59 PM Eastern, through the official Qualtrics portal.
- **Scoring:** two criteria of equal importance, technical merit and "Potential relationship of the proposed research and development to DoW missions" (YIP notice FA9550-26-S-0003, F.2.b.1).
- **Required content:** includes "Potential impact on DAF and DoW capabilities" (D.2.b). The draft already has this section.

## Hard constraints

1. **Page limit.**
   - The narrative must stay within 5 pages, excluding cover, CV and references.
   - Format: US Letter, 1-inch margins, 12-point Garamond, 1.5 spacing.
   - The current draft already fills about 5 narrative pages, so every addition must be offset by a cut of equal length. Recompile with pdfLaTeX (`ebgaramond` package) and confirm the page count.
2. **Invent nothing.** Do not invent citations, results, collaborators, program text, mission details or scientific facts. Add only citations from the verified list at the end. Where the author must supply something, write `[AUTHOR: …]`.
3. **Change only what's asked.** Keep every other sentence. Do not add jargon or complexity to sound more technical.
4. **Return four things:**
   - the full revised `main.tex`
   - BibTeX entries added or corrected
   - a change log keyed to the numbers below
   - every `[AUTHOR: …]` item

## Program text

Quote only text the author pastes from the current BAA. Until then, keep the draft's paraphrase. For orientation, the initial FY26 announcement described the program's thrusts roughly as follows. These are paraphrased, not quotations, except where marked:

- handling diverse data and information types
- integrating multiple reasoning and learning components
- bridging correlational and causal discovery
- local-to-global data-fusion problems
- "Mechanize reasoning/learning and computing in the same computational environment" (verbatim)
- provably efficient analytics with guaranteed performance on high-dimensional, massive data

The stated goals included moving from sensing to information awareness, understanding the foundations of autonomy, reducing cognitive overload, and improving human-machine interfaces.

## Reviewer assessment (context for the edits)

- **Program fit.**
  - *Strong:* integrating multiple reasoning and learning components, and combining bottom-up extraction with top-down knowledge-driven checking.
  - *Not addressed:* causal discovery, sensor data fusion and performance guarantees.
  - *Generic:* DAF relevance ("not tied to a single mission application").
  - *Biggest risk:* the portfolio's status in the current BAA (see the check above).
- **Scientific contribution.**
  - The stated hypothesis is the general premise of tool-augmented and neuro-symbolic reasoning, which reviewers will see as established.
  - The genuinely open question sits in Task 2: when a formally valid check actually applies to a claim.
  - The closest 2026 work already separates symbolic validity from semantic grounding, so the paper must say exactly what it adds.
- **Technical credibility.**
  - The planner and routing are vague.
  - Knowledge acquisition is the bottleneck. The paper acknowledges this.
  - The test cases are generated from the same principle library the verifier uses, which makes the evaluation circular.
  - "Successful correction" can be gamed by weakening a claim.
  - There is no formal component.
- **Coherence and feasibility.**
  - The represent → verify → refine pipeline is coherent.
  - The scope is far too broad for one PI over three years, and the paper is already at the page limit.
- **Connection to the PI's work.**
  - CLORE and FaithScore are cited.
  - "LLM-based scientific discovery" is claimed without a citation, and the most relevant completed work (FG-PRM, SciEvent, hypothesis discovery) is missing.
  - "The original FAIGen proposal" is an unexplained internal reference.
- **Clarity and evaluation.**
  - The prose is clear and the figure helps, but there is no running example.
  - The evaluation doesn't name its datasets or define success.

## Keep these — do not weaken them

- The distinction between **execution validity** and **semantic groundedness**, and the sentence "However, a successful execution will not itself be treated as proof of scientific correctness; semantic applicability remains an explicit check."
- **Verification receipts:** the principle used, its source, the representation, the executor, the result, and the validity conditions.
- The explicit test of **representation fidelity**, with links back to the source.
- The **regression guard:** "A revised claim will be accepted only if the failed checks are resolved without invalidating components that previously passed".
- **Controlled challenge sets** that vary quantities, applicability conditions and rule compositions. Keep the idea and fix the circularity (item 2).
- The **baselines** "tool-augmented neural reasoning without explicit applicability checks" and "symbolic-only variants," plus the ablations.
- The labeled **DAF/DoW impact section**, the **framework figure**, and the **research questions** under each task.

## Revisions, ranked — make these before sending

### 0. Administrative (required)

- **Replace the cover's `[PHONE NUMBER]` placeholder** with `+1 (972) 883-2634`, as on the PI's other white papers. `[AUTHOR: confirm]`
- **Acknowledge the other submissions** (D.2.b: "you must acknowledge so on each submission"). Add one line to the cover page:

  > "The PI is also submitting white papers to the Computational Cognition and Machine Intelligence (Dr. Ben Robinson) and Trust and Influence (Dr. Laura Steckman) portfolios. This paper is distinct: it studies whether general scientific principles apply to LLM-generated scientific claims. The CCMI paper studies checking and revising arguments built from uncertain readings of evidence documents; the T&I paper studies human trust in AI evaluation."

  `[AUTHOR: list only papers actually submitted]`

### 1. Make semantic groundedness the central question, and position it against the closest work

> This project asks a fundamental question: How can LLM-generated scientific claims be systematically verified and refined using explicit scientific facts, rules, and constraints?

> The central hypothesis is that scientific claims can be verified more reliably when the relevant principles are represented explicitly and the reasoning process is divided among specialized mechanisms rather than performed implicitly by a single neural model.

> Recent work has highlighted this executable-but-ungrounded failure mode in structured STEM reasoning

**Why.**
- **The hypothesis is already established.** It is the general premise of tool-augmented and neuro-symbolic reasoning, which the draft itself cites (Toolformer, Logic-LM). FacTool already applies tool-augmented checking across knowledge QA, code, math and scientific literature review.
- **The open question is buried.** It sits in Task 2: when an executable check passes, what else must hold for it to establish the claim? That means the right principle, its applicability conditions in context, and correct variable and entity bindings.
- **The closest 2026 work overlaps.** Neuro-symbolic PRM (Zi et al.) already separates symbolic validity from semantic grounding in reasoning steps. It also generates counterfactual flawed steps that still pass the verifier. The paper must say precisely what it adds beyond "generalize this problem beyond fixed quantitative traces".
- **It overlaps the PI's CCMI paper.** Both concern whether a formal representation faithfully captures the text, and the program officers coordinate their feedback.

**Change.** Keep the total length the same.
- **Central question.** For example: "When an executable check passes, what else must hold for it to establish a scientific claim — the right principle, its applicability conditions in this context, and correct variable and entity bindings — and how can a verifier establish these from scientific sources?"
- **Hypothesis**, stated so it could fail. For example: "On compositional scientific claims, many failures of tool-augmented verification come from applicability and binding errors rather than execution errors. Checking applicability conditions explicitly catches errors that execution-only verification passes." It is tested by the existing baseline, tool-augmented reasoning without applicability checks, on cases with known applicability violations.
- **Positioning,** in two or three sentences:
  - FacTool: tool-augmented factuality checking across several task types.
  - AutoVerifier: claim triples and knowledge graphs for technical claims.
  - Neuro-symbolic PRM: validity versus grounding within structured reasoning traces, with a learned grounding scorer.
  - This project: acquiring and checking the applicability conditions of heterogeneous principles for open-domain claims, with receipts that tie each check to its source and conditions.
  - Claim no more novelty than this supports.
- **Differentiation from the CCMI paper,** in one sentence: this paper concerns whether general principles apply to a claim; the CCMI paper concerns uncertain readings of specific evidence and revision when that evidence changes.

### 2. Fix the evaluation: break the circularity, name datasets, define success, close the vacuous-revision loophole

> Evaluation will combine existing scientific claim-verification resources with controlled challenge sets generated from known scientific principles.

> We will use the symbolic representations from Task 1 to construct counterfactual and compositional cases, execute them to obtain verified outcomes, and use these traces as training or preference signals.

> A primary success criterion is a substantial reduction in verification errors on compositional and previously unseen settings relative to the strongest end-to-end neural baseline

**Why.**
- **Circular evaluation.** If test cases come from the same principle library the verifier uses, the verifier is graded against its own representation. High scores would then show self-consistency, not validity.
- **Undefined success.** "Substantial" has no definition, and the existing resources aren't named.
- **Vacuous revisions.** A refinement can "succeed" by weakening a claim into something vague that passes every check.
- **Weak baseline.** Self-refinement without external feedback is known to be weak (Huang et al., ICLR 2024), so it can't serve as the main comparison.

**Change** (about three sentences, offset by cuts from item 3):
- **Independent test cases.** Build them from principles held out of the verifier's library, or have them authored by people not involved in building it. Report human-labeled sets separately.
- **Name the resources.** Use SciFact (already cited) and SciTab (compositional numerical claims over scientific tables). `[AUTHOR: add others you plan to use]`
- **Primary comparison.** Measure error on claims with applicability or binding violations, at matched compute, against the strongest tool-augmented baseline without applicability checks.
- **What counts as a correction.** A correction succeeds only if the revised claim keeps the original's scope and specificity, judged against a reference, and passes every check. Report weakened or vacuous revisions separately.
- **Baselines.** Keep self-refinement as a sanity baseline, and make the tool-augmented baseline the main one.

### 3. Narrow the scope to fit one PI, three years and five pages

> We will develop a claim-driven scientific principle representation with four complementary forms

> it can construct a first-order, logic-programming, or SMT representation and execute a solver

> We will further study whether verified representations can improve generalization before an error occurs.

**Why.**
- **Too many components.** The plan covers knowledge acquisition for four representation types, a semantic parser, a planner, at least four executors, diagnosis, refinement, generation of training data, and evaluation across domains. By the reviewer's estimate, $150K a year including indirect costs supports about one PhD student, which is less than this plan needs.
- **No room left.** The paper is at the page limit, and items 1, 2 and 4 need space.

**Change.**
- **Limit the scope.** Restrict the work to quantitative relations with units and applicability conditions, using evidence-backed facts as inputs, in one or two domains. `[AUTHOR: choose domains; the draft names physical and engineering relations]`
- **Make the generalization component optional.** This is the second half of Task 3, which uses verified cases as training or preference signals.
- **Choose one formal backend** for logical constraints instead of three.
- **Restructure the plan.** Year 1 builds a thin end-to-end version in one domain, then the work deepens.
- **Use the space saved** for items 1, 2 and 4.

### 4. Add a running example and remove internal references

> This component adapts the simulation-based synthetic-data idea from the original FAIGen proposal while making verification, rather than generic fine-tuning, the central source of supervision.

> The project is not tied to a single mission application

**Why.**
- **No running example.** The PI's other white papers make their ideas concrete with one; this paper stays abstract, so a program officer can't see what an applicability check looks like.
- **Unexplained internal name.** "FAIGen" means nothing to the reader and suggests text carried over from another proposal.
- **Weak impact statement.** "Not tied to a single mission application" undercuts the impact section.

**Change.**
- **Add an example.** Write three or four sentences in Section 1 and reuse the example briefly in Tasks 1–3. A candidate: a claim that applies the ideal gas law to a gas at very high pressure, where the law's assumptions break down. The representation records the law's conditions, execution "passes," and the applicability check flags the claim. `[AUTHOR: confirm or replace with an example from your chosen domain — do not let ChatGPT invent domain science]`
- **Remove "from the original FAIGen proposal".** Describe the idea directly instead.
- **Replace the "not tied to a single mission application" sentence** with one or two concrete settings in which AI-generated technical analyses must be checked before use. `[AUTHOR: settings you can describe accurately]`

### 5. Connect to the PI's strongest relevant work and fix a reference

> The PI's prior work spans information extraction and knowledge representation, explicit logical reasoning over natural-language explanations, fine-grained hallucination evaluation, and LLM-based scientific discovery.

**Why.** "LLM-based scientific discovery" has no citation, and the most relevant completed work is missing:
- **FG-PRM** (EMNLP 2025 Findings) detects typed hallucinations in individual mathematical reasoning steps, a direct precursor to Task 3's typed diagnoses for quantitative claims.
- **SciEvent** (EMNLP 2025) benchmarks structured event extraction from scientific text, a precursor to Task 1.
- **Open-domain scientific hypothesis discovery** (ACL 2024 Findings; the PI is co-leading author) and the **LLM4SR** survey (2025) support the scientific-discovery claim.

**Change.**
- **Cite these where they support Tasks 1 and 3** and in the team paragraph.
- **Keep completed and proposed work separate.** For example: "FG-PRM detects typed errors in mathematical steps; extending typed diagnosis to applicability errors is proposed."
- **Fix the AutoVerifier reference.** The arXiv listing names four authors (Yuntao Du, Minh Dinh, Kaiyuan Zhang, Ninghui Li). Remove "TruSeLLM Team" unless the paper's PDF lists it.

### 6. Cite the program officer's own work where Task 2 genuinely builds on it

Dr. Riecken's own work connects to Task 2. His article "M: An Architecture of Integrated Agents" appeared in Communications of the ACM 37(7), July 1994. The same issue on intelligent agents includes his "Intelligent agents" and "A conversation with Marvin Minsky about agents" (with Minsky). Task 2's multi-strategy verifier, in which a planner routes the parts of a claim to specialized reasoners, is an integrated architecture of the same general kind.

**Change.** Where Task 2 introduces the multi-strategy verifier, add one sentence. For example: "This design belongs to the line of integrated-agent architectures that combine specialized components on one problem [Riecken 1994]; what is new here is that each component returns a receipt recording the principle, source and conditions under which its result holds."

- **Describe the article only by its title** unless the author confirms its content. `[AUTHOR: skim Riecken (1994) and confirm the sentence fits]`
- **Keep it to one sentence** and add no praise. It must not push the paper over the page limit.

## Later — leave for the full proposal

- **One analyzable property.** For example, how a check's soundness depends on representation fidelity, or the cost of planning verification. This would speak to the program's interest in guaranteed performance.
- **Details:** the domain choice, annotation protocol, inter-annotator agreement and sample sizes.
- **Required elements:** the data management plan, measurable benchmarks for each year, and current and pending support.

## Verified citations you may add or correct

```bibtex
@article{chern2023factool,
  title={FacTool: Factuality Detection in Generative {AI} -- A Tool Augmented Framework for Multi-Task and Multi-Domain Scenarios},
  author={Chern, I-Chun and Chern, Steffi and Chen, Shiqi and Yuan, Weizhe and Feng, Kehua and Zhou, Chunting and He, Junxian and Neubig, Graham and Liu, Pengfei},
  journal={arXiv preprint arXiv:2307.13528}, year={2023}
}
@inproceedings{lu2023scitab,
  title={{SCITAB}: A Challenging Benchmark for Compositional Reasoning and Claim Verification on Scientific Tables},
  author={Lu, Xinyuan and Pan, Liangming and Liu, Qian and Nakov, Preslav and Kan, Min-Yen},
  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
  pages={7787--7813}, year={2023}
}
@inproceedings{huang2024selfcorrect,
  title={Large Language Models Cannot Self-Correct Reasoning Yet},
  author={Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},
  booktitle={International Conference on Learning Representations (ICLR)}, year={2024}
}
@inproceedings{li2025fgprm,
  title={{FG-PRM}: Fine-grained Hallucination Detection and Mitigation in Language Model Mathematical Reasoning},
  author={Li, Ruosen and Luo, Ziming and Du, Xinya},
  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},
  pages={4247--4278}, year={2025},
  doi={10.18653/v1/2025.findings-emnlp.228}
}
@inproceedings{dong2025scievent,
  title={{SciEvent}: Benchmarking Multi-domain Scientific Event Extraction},
  author={Dong, Bofu and Shah, Pritesh and Sonawane, Sumedh and Banerjee, Tiyasha and Brady, Erin and Du, Xinya and Jiang, Ming},
  booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
  year={2025}
}
@inproceedings{yang2024hypotheses,
  title={Large Language Models for Automated Open-domain Scientific Hypotheses Discovery},
  author={Yang, Zonglin and Du, Xinya and Li, Junxian and Zheng, Jie and Poria, Soujanya and Cambria, Erik},
  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},
  year={2024}
}
@article{luo2025llm4sr,
  title={{LLM4SR}: A Survey on Large Language Models for Scientific Research},
  author={Luo, Ziming and Yang, Zonglin and Xu, Zexin and Yang, Wei and Du, Xinya},
  journal={arXiv preprint arXiv:2501.04306}, year={2025}
}
@article{riecken1994m,
  title={M: An Architecture of Integrated Agents},
  author={Riecken, Doug},
  journal={Communications of the ACM},
  volume={37}, number={7}, year={1994}
}
@article{du2026autoverifier,
  title={AutoVerifier: An Agentic Automated Verification Framework Using Large Language Models},
  author={Du, Yuntao and Dinh, Minh and Zhang, Kaiyuan and Li, Ninghui},
  journal={arXiv preprint arXiv:2604.02617}, year={2026}
}
```

I checked these existing entries and they resolve: Logic-LM, CLORE, FaithScore, Neuro-symbolic PRM (arXiv 2608.26329) and AutoVerifier (arXiv 2604.02617). The rest (Ji et al., SciFact, Toolformer, Self-Refine) are standard, well-known papers I did not re-check.

## Sources checked

- [Initial FY26 AFOSR BAA (ICF at A.2.f)](https://files.simpler.grants.gov/competitions/485021fe-dec0-4b92-ae37-6e31b1a04a5f/instructions/78dd3dd6-5592-409d-bc36-bcb12297e38b/PKG00293108.pdf)
- [Amendment 0001 (A.2.f = Complex Networks)](https://files.simpler.grants.gov/opportunities/de479d2e-aad1-466a-acc3-d5d11cf7918d/attachments/fd9a4dfb-ac66-4c75-8166-592ea2daeb02/FA955026S0001_Amendment_0001_AFOSR_Open_BAA.pdf)
- [ICF program description](https://community.apan.org/wg/afosr/w/researchareas/7684.science-of-information-computation-and-fusion.aspx)
- [Neuro-symbolic PRM](https://arxiv.org/abs/2608.26329)
- [AutoVerifier](https://arxiv.org/abs/2604.02617)
- [FacTool](https://arxiv.org/abs/2307.13528)
- [SciTab](https://aclanthology.org/2023.emnlp-main.483)
- [Huang et al.](https://arxiv.org/abs/2310.01798)
- [FG-PRM](https://aclanthology.org/2025.findings-emnlp.228/)
- [PI publication list](https://xinyadu.github.io/publications.html)
- [CACM July 1994 issue (Riecken articles)](https://cacm.acm.org/issue/july-1994)
