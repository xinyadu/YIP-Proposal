# Final revision comments for ChatGPT (round 2) — Doug Riecken (Science of Information, Computation, Learning, and Fusion) white paper

**How to use:** attach the current `doug/main.tex` and `doug/references.bib` to ChatGPT, then paste everything below the line.

---

You are revising an AFOSR FY27 Young Investigator Program (YIP) white paper written in LaTeX. This is the second round of revisions. The first round is already in the draft, so don't redo it. Treat this as an initial white paper, not a full proposal: every technical commitment must be meaningful and defensible, and nothing should be added just to sound more technical. Apply the revisions below in priority order.

## Context

- **Paper:** "Neural-Symbolic Verification and Refinement of LLM-Generated Scientific Claims."
- **Portfolio:** Science of Information, Computation, Learning, and Fusion, Dr. Richard D. (Doug) Riecken (AFOSR Open BAA Amendment 0001, Section A.4.i, as confirmed by the author). Computational Cognition and Machine Intelligence (A.4.f) sits in the same branch.
- **PI:** Xinya Du, The University of Texas at Dallas.
- **Deadline:** 9 October 2026, 11:59 PM Eastern, through the official Qualtrics portal.
- **Scoring:** two equally weighted criteria, technical merit and "Potential relationship of the proposed research and development to DoW missions" (YIP notice FA955026S0003, F.2.b.1). The topic contacts "will coordinate to provide feedback on the white papers."

## Hard constraints

1. **Page limit.**
   - The narrative may not exceed 5 pages; the cover, CV and references don't count.
   - The current draft uses about 4.6 narrative pages; the last page is about 60% full, leaving roughly 140 words.
   - Any addition beyond that must be offset by a cut of equal length. Item 8 lists cuts.
   - Recompile with XeLaTeX (the repository README's command) and report the narrative page count.
2. **Invent nothing.** No new citations except the verified entries at the end. No results, pilot numbers, collaborators, program text, mission details or physics the author hasn't supplied. Where the author must supply something, write `[AUTHOR: …]`.
3. **Change only what's asked.** Keep every sentence the items below don't touch, and everything under "Keep."
4. **Return:**
   - the full revised `main.tex`
   - the BibTeX entries you added
   - a change log keyed to the item numbers
   - every `[AUTHOR: …]` item
   - the final narrative page count

## Already done — don't redo

- **Program location and cover:** confirmed at A.4.i; program officer and phone added.
- **Running example:** the vessel example replaced the vague one; FAIGen references removed.
- **Scope:** narrowed to thermodynamic and mechanical relations, three checker roles and one SMT backend; trained repair is optional.
- **Positioning:** Neuro-symbolic PRM is credited.
- **Evaluation:**
  - labels are independent and hidden from every system
  - splits separate principles and source documents
  - cases without sufficient information get an unresolved reference outcome
  - the primary metric is defined at matched coverage and cost
- **Repair:** corrections must preserve the claim's scope.
- **References:** the PI's work is cited, AutoVerifier's authors are corrected, and the Riecken/Minsky connection is added.

## Remaining problems, ranked

### 1. Make the paper clearly distinct from the PI's CCMI white paper

> Each component will return a verification receipt: its principle, source, variable bindings, operation, result, and supported, contradicted, or unresolved conditions.

> The primary outcome is the fraction of accepted claims that are invalid, at matched coverage (the fraction accepted) and total cost, including retrieval, model calls, execution, and retries.

**Why.** The two papers now sit in the same AFOSR branch, and the program contacts coordinate feedback. The CCMI paper, as revised on 9 October, overlaps this one in five places:
- **Verdicts:** "Each evidence check returns supported, contradicted, or unresolved."
- **Repair rule:** "invented premises or weakened rules will not count as repairs."
- **Evaluation design:** "compare error at matched coverage," and "Questions outside the rule library will count as unresolved rather than being discarded."
- **Check types:** "Rule checks will be exact within the specified formal language; evidence checks will be learned and empirically validated." This paper says the same thing about calculations and evidence judgments.
- **Foundations and repair:** both cite FG-PRM and Logic-LM. The CCMI paper uses solver feedback "as in Logic-LM" as its initial repair mechanism, and this paper's Task 3 also compares against solver-error feedback.

Read side by side, the two can look like one project written twice, which weakens both. What only this paper has:
- applicability conditions of *general scientific principles*
- units and variable bindings
- the survival of those conditions across a calculation engine and an SMT solver
- paired tests that change one applicability condition while keeping the calculation fixed

**Change.**
- **Name the boundary.** Add one sentence to "Relation to current work":
  > "A companion CCMI white paper studies how uncertain readings of evidence documents propagate through arguments and how those arguments are revised when the evidence changes; this project instead concerns general scientific principles—their applicability conditions, units and variable bindings—and whether these survive composition across calculation and constraint solving."
- **Keep length neutral.** Delete the impact section's sentence "Its scope is automated scientific verification; it is distinct from the PI's CCMI concept on revising arguments from changing reports and the Trust and Influence concept on human reliance."
- **Make the figure distinctive.** Replace the last box ("Supported, contradicted, or unresolved") with this paper's typed diagnoses: "Source, applicability, binding, or execution failure." Update the caption to match.
- **Promote the signature test.** Make the paired condition-change test the first comparison named in the Evaluation section.
- **Don't copy sentences from the CCMI paper.** Keep the shared good practices, but phrase them independently.

### 2. Position against the classical work on applicability conditions and the closest LLM systems

> Our proposed contribution is a way to make the conditions for using and combining these methods explicit and testable when those conditions must be recovered from scientific sources.

> Checks that use another component's output will also inherit the conditions attached to that output.

**Why.**
- **Explicit operating conditions are classical.** Compositional modeling (Falkenhainer & Forbus, 1991) builds models from fragments with explicit modeling and operating assumptions, such as steady state or Reynolds-number bounds. It checks simulation results against those assumptions and reformulates the model when one is violated. Without this citation, "explicit conditions" reads as new.
- **The citation sharpens the real novelty.** Those systems used hand-built domain theories. Here the conditions are recovered from text by fallible neural extraction and must stay intact across neural and symbolic components.
- **Two LLM systems are close.**
  - ProgramFC (Pan et al., ACL 2023) writes a reasoning program that splits a claim into sub-tasks handled by specialized functions. It is the closest prior work to Task 2's planner.
  - SatLM (Ye et al., NeurIPS 2023) has an LLM write a declarative specification that an automated theorem prover solves. It is the closest prior work to the SMT backend.

**Change.**
- **Add 2–3 sentences to "Relation to current work":**
  - Compositional modeling made models' operating conditions explicit and checked results against them, but relied on hand-encoded domain theories [Falkenhainer & Forbus].
  - ProgramFC decomposes claims into programs of specialized checks [Pan et al.].
  - SatLM pairs LLM-written specifications with automated solvers [Ye et al.].
  - The new problem is recovering conditions from scientific text, measuring extraction errors (omitted conditions and invented restrictions), and preserving conditions across component boundaries.
- **Name a concrete baseline.** In the Evaluation section, name ProgramFC as the concrete instance of "tool-augmented verification without explicit conditions".

### 3. Show the problem is real for current models, and make the hard cases visible

> Suppose a language model reads that gas in a sealed, rigid vessel is heated from 300 K to 600 K and concludes that its volume doubles.

> The initial scope is quantitative claims about elementary thermodynamic and mechanical systems, expressed in short scientific passages and tables.

**Why.**
- **The example is too easy.** The deciding fact ("rigid") sits in the claim itself, so any strong LLM judge would probably catch it. It illustrates the idea but doesn't show the need.
- **The domain may look solved.** A reviewer may worry that frontier models already handle elementary thermodynamics and mechanics, leaving too few errors to measure.
- **No evidence is cited.** The paper cites nothing showing that current systems miss applicability errors.

**Change** (2–3 sentences, no new aims):
- **Cite evidence of the failure.**
  - SciBench's error analysis lists assumption identification among the ten skills whose failures cause errors in college-level science problems (Wang et al., ICML 2024).
  - On "trap problems," where an inserted condition invalidates the standard solution, models often fail to apply knowledge they have (Zhao et al., EMNLP 2024).
  - Make no numerical claims from either paper.
- **Point to the hard cases.** After the example, add one sentence: the hard cases are those where the deciding condition is stated in another passage, implied (a "steel tank" rather than "rigid"), or established only by an earlier check. These are exactly what Task 2 varies.
- **Add pilot data if it exists.** If the PI has even a small pilot in which a strong LLM judge accepted such cases, report it in one sentence. `[AUTHOR: pilot result, or omit]`
- **Optional: a more Air Force-relevant held-out domain.** Use compressible-flow or propulsion relations for Year 3 instead of generic mechanics. For example, isentropic relations do not hold across a shock wave. `[AUTHOR: confirm domain and example — do not let ChatGPT supply physics]`

### 4. Fix the attribution to Riecken (1994)

> Riecken's integrated-agent work and the architecture of diversity developed by McCarthy, Minsky, Riecken, and colleagues emphasize both this diversity and knowledge of when each method is appropriate

**Why.** "Re-Membering: A Theory of Agents" describes a society of agents (the MARVIN prototype) that combines spatial, structural, functional, temporal and causal reasoning. It does not discuss knowing when each method applies. McCarthy et al. (2002) does: techniques must "determine whether or not they are suited for a given task". Citations of the program officer's own work need to describe it exactly.

**Change.** Replace the sentence with:
> "Riecken's agent architecture combined spatial, structural, functional, temporal and causal reasoning [Riecken 1994]; McCarthy, Minsky, Riecken and colleagues further argued that each technique must determine whether it suits a given task [McCarthy et al. 2002]."

### 5. Ground Task 1 in the PI's own lead-author extraction work

> This extends the PI's work on structured scientific information extraction in SciEvent

**Why.**
- **SciEvent is co-authored.** The PI is sixth of seven authors, so calling it "the PI's work" invites a question about her role.
- **Her strongest credential is uncited.** Task 1 extracts records with slots from documents. Her first-author template-filling work (GTT, NAACL 2021) jointly extracts role fillers and recognizes templates across a document.

**Change.**
- Rewrite as: "This builds on the PI's document-level template filling [GTT] and her co-authored scientific event extraction benchmark [SciEvent]."
- Don't add Search Wisely here. The revised CCMI paper now cites it, and item 1 asks the two papers to rest on distinct foundations.

### 6. Retitle and finalize the cover

> The PI has also prepared distinct white papers for Computational Cognition and Machine Intelligence (uncertain evidence and argument revision), and Trust and Influence (human reliance on AI evaluation).

**Why.**
- **The title is generic.** It names a method, while the contribution is now applicability conditions.
- **The cover line isn't an acknowledgment.** The notice (D.2.b) requires each submission to acknowledge the others, and "prepared" describes a draft, not a submission. It also reads oddly to a program officer.
- **The NOFO number is formatted differently.** It appears as "FA9550-26-S-0003" here but "FA955026S0003" in the notice and in the other two papers.

**Change.**
- **Title.** For example: "When Does a Scientific Calculation Apply? Condition-Aware Verification of LLM-Generated Scientific Claims."
- **Cover line.**
  > "The PI is also submitting white papers to the Computational Cognition and Machine Intelligence (Dr. Ben Robinson) and Trust and Influence (Dr. Laura Steckman) portfolios."

  `[AUTHOR: list only papers actually submitted]`
- **Layout.** Left-align that line; it is currently centered.
- **NOFO.** Write it as "FA955026S0003."

### 7. State one measurable benchmark

> Success requires improved discrimination and transfer to held-out principles.

**Why.** Reviewers weigh "clear benchmarks for measuring success and progress", and full proposals must include them (YIP notice C.3.b, EO 14332). One sentence now costs little.

**Change.** Add:
> "The primary benchmark is a lower rate of invalid accepted claims than the strongest tool-augmented baseline at matched coverage and cost on held-out principles, with the margin and sample size fixed before testing; the Year 1 milestone is an end-to-end prototype evaluated on independently annotated thermodynamic cases."

### 8. Where to find the space

The additions in items 1–7 total about 170–200 words. These cuts cover the gap beyond the ~140 free words:
- **Impact section.** Delete the CCMI/T&I distinction sentence (item 1 moves it).
- **"Relation to current work."** Merge the FacTool and AutoVerifier sentences into one.
- **Evaluation.** Delete "Self-refinement without external feedback will be a sanity baseline."
- **Task 2, last paragraph.** Merge its second and third sentences.

## Keep — do not weaken

- The vessel example, with item 3's added sentence.
- "A missing condition will remain unknown rather than be silently assumed true" and "Conflicting sources will retain their separate conditions".
- "they cannot be satisfied by the claim under examination itself."
- Independent annotations of both omitted conditions and invented restrictions.
- Annotator-supplied records used to separate extraction failures from reasoning failures.
- The falsifiable hypothesis with its stated failure modes (extraction errors, over-conservative checks).
- Scope-preserving repair, with legitimate narrowing labeled separately.
- The baselines: verifier-first process scoring, and symbolic checking with human-validated records.

## Leave for the full proposal

- **Specifications:** the principle inventory, annotators' expertise, numerical tolerances and sample sizes.
- **An analyzable model** of how per-component extraction errors propagate into end-to-end false acceptance.
- **Required elements:** the Gold Standard Science commitment (EO 14303), the data management plan, and per-year benchmarks.

## Verified citations to add

```bibtex
@article{falkenhainer1991compositional,
  title={Compositional Modeling: Finding the Right Model for the Job},
  author={Falkenhainer, Brian and Forbus, Kenneth D.},
  journal={Artificial Intelligence},
  volume={51}, pages={95--143}, year={1991}
}
@inproceedings{pan2023programfc,
  title={Fact-Checking Complex Claims with Program-Guided Reasoning},
  author={Pan, Liangming and Wu, Xiaobao and Lu, Xinyuan and Luu, Anh Tuan and Wang, William Yang and Kan, Min-Yen and Nakov, Preslav},
  booktitle={Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages={6981--7004}, year={2023}
}
@inproceedings{ye2023satlm,
  title={{SatLM}: Satisfiability-Aided Language Models Using Declarative Prompting},
  author={Ye, Xi and Chen, Qiaochu and Dillig, Isil and Durrett, Greg},
  booktitle={Advances in Neural Information Processing Systems},
  volume={36}, year={2023}
}
@inproceedings{wang2024scibench,
  title={{SciBench}: Evaluating College-Level Scientific Problem-Solving Abilities of Large Language Models},
  author={Wang, Xiaoxuan and Hu, Ziniu and Lu, Pan and Zhu, Yanqiao and Zhang, Jieyu and Subramaniam, Satyen and Loomba, Arjun R. and Zhang, Shichang and Sun, Yizhou and Wang, Wei},
  booktitle={Proceedings of the 41st International Conference on Machine Learning},
  series={Proceedings of Machine Learning Research}, volume={235}, year={2024}
}
@inproceedings{zhao2024trap,
  title={Exploring the Compositional Deficiency of Large Language Models in Mathematical Reasoning Through Trap Problems},
  author={Zhao, Jun and Tong, Jingqi and Mou, Yurong and Zhang, Ming and Zhang, Qi and Huang, Xuanjing},
  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
  pages={16361--16376}, year={2024},
  doi={10.18653/v1/2024.emnlp-main.915}
}
@inproceedings{du2021gtt,
  title={Template Filling with Generative Transformers},
  author={Du, Xinya and Rush, Alexander and Cardie, Claire},
  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  pages={909--914}, year={2021},
  doi={10.18653/v1/2021.naacl-main.70}
}
```

I also checked the two Riecken-related entries already in `references.bib` against their primary texts. Both exist as cited; item 4 corrects how the first one is described.

## Sources checked

- [Falkenhainer & Forbus 1991 (PDF)](https://www.qrg.northwestern.edu/papers/Files/QRG_Dist_Files/QRG_1991/FalkenhainerForbus_1991_CompModeling.pdf)
- [ProgramFC, ACL 2023](https://aclanthology.org/2023.acl-long.386/)
- [SatLM, NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8e9c7d4a48bdac81a58f983a64aaf42b-Abstract-Conference.html)
- [SciBench (error analysis, Section 5)](https://arxiv.org/html/2307.10635v3)
- [Trap problems, EMNLP 2024](https://aclanthology.org/2024.emnlp-main.915/)
- [Template Filling with Generative Transformers](https://aclanthology.org/2021.naacl-main.70/)
- [Riecken 1994, Re-Membering](https://cdn.aaai.org/Symposia/Spring/1994/SS-94-03/SS94-03-019.pdf)
- [McCarthy et al. 2002](https://www.jfsowa.com/ikl/McCarthy02.pdf)
