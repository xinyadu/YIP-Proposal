# Claude comments: Goolsby note

Reviewer: Claude · 2026-10-13 · Scope: `ONR/goolsby/main.tex` on `main` at `08ae8ff`; the text last changed in `ee30d22` (Oct 13, 02:15 PT). Checked against Dr. Goolsby's program page, the FY27 NOFO focus-area list, and every linked paper and dataset. *(judgment)* marks my opinion; everything else is checked.

## Verdict

This is the clearest version of the idea so far *(judgment)*. "Lineage" is a better central concept than the earlier "deception-resilient" framing. Three ideas are worth keeping:

- the counterfactual streams, in which message volume changes but independent evidence does not
- the targeted search when "an apparent consensus rests on a single information pathway"
- the caution against treating repetition as proof of coordination

However, the 02:15 edit also removed four things the note needs: a measurable deception outcome, a testable hypothesis, the program's own language, and your KAIROS role. All four fit in the inch of empty space at the bottom of the page.

## Must fix before sending

1. **The committed PDF is out of date.** `white_paper_goolsby.pdf` still shows the earlier "Deception-Resilient Retrieval-Augmented Generation…" version.
   - Cause: since `a4c04d9`, the workflow compiles only one folder (now `behzad`), and its recent runs fail at that step.
   - Fix: restore `for d in predrag behzad morrison goolsby` in both loops of `.github/workflows/compile-onr.yml`. Alternatively, build locally and commit.
   - I compiled the current `main.tex` with pdflatex: it is one page with no overfull lines.
2. **Put back a deception metric.** The previous version measured "the rate at which planted false claims are incorrectly marked supported". The current note says only "resistance to amplified false claims". `chatgpt_revision_response.md` still says the metric is explicit. Pair the metric with its counterweight: recall and delay for independently verified alerts. That pair turns the note's "without suppressing legitimate early warnings" into something measurable.
3. **Say which data tests what.** CrisisFACTS (TREC 2022–2023) supplies multi-stream crisis data with assessor-built gold facts, and GDELT supplies event records. Neither labels false claims or copying. So the deception result can come only from the controlled streams, or from false claims planted into real streams. One sentence prevents a PO from assuming otherwise.
4. **Restore your KAIROS role.** `ee30d22` replaced it with "DARPA KAIROS RESIN-11 work", which says nothing about what you did. Use: "As a postdoc, the PI led system integration for the RESIN team in DARPA KAIROS (RESIN-11, NAACL 2022 Demo, first author)."

## Should fix

5. **Make the hypothesis comparative.** "Can distinguish genuine corroboration from information amplification" names no comparison and no outcome. The second sentence ("agents should retrieve and reconcile…") is a design principle; it belongs under the approach. "Agents" also appears there without being introduced.
6. **Name the program's interests in the Naval paragraph.** The previous version had a sentence naming the program's interests: AI-enhanced RAG, regional situation awareness, and decision tools for operations in the information environment. The edit dropped it. The suggested text below restores it and adds deception and obfuscation, which the program page also lists ("Problems of reflexive control, deception, cyber-attack, and obfuscation"). Optional *(judgment)*: the title no longer says "Retrieval-Augmented Generation", the program's own term. Consider putting it back, for example "Reasoning over Contested Evidence: Lineage-Aware RAG for Regional Situation Awareness".
7. **Say where the training labels come from.** Aim 2 trains "with supervision on claim support, source dependence, and revisions". Real crisis streams lack those labels, so name the source: the simulator's known lineages, plus a small annotated set of real streams.
8. **Say that FaithScore and FGAIF are being adapted.** Both are vision-language papers. A PO who clicks them should already know from the note that you will adapt them to text RAG.
9. **Position against the closest prior work in one clause** *(judgment)*. Truth-discovery methods estimate dependence between sources of structured claims (e.g., [Dong, Berti-Equille & Srivastava, PVLDB 2009](https://lunadong.com/publication/dependence_vldb.pdf)). Rumor detectors classify whole propagation threads (e.g., [Ma, Gao & Wong, ACL 2018](https://aclanthology.org/P18-1184/)). The note's difference is that it tracks lineage for individual event claims and uses it inside retrieval and generation. Stating it heads off the obvious comparison.
10. **Smaller wording fixes.**
    - "model how alternative information interventions change the inferred regional situation" could be read as planning influence operations. Say what is meant, for example "how a correction or a newly verified report would change the inferred situation".
    - Problem, second sentence: "although they all repeat one unverified claim while a later field test finds no contamination" stacks two conjunctions. Suggested: "dozens of posts may report contaminated drinking water, all repeating one unverified claim; a later field test finds none."
    - Aim 3, sim-to-real *(judgment)*: a PO will ask whether policies trained on simulated propagation transfer to real streams. One clause covers it: calibrate the simulator to real propagation statistics and test on held-out real events.

## Keep

- The typhoon water-contamination example. It is distinct from the other three notes.
- "Model uncertainty about these relationships so repeated reports do not automatically become independent confirmation or proof of intentional coordination."
- The counterfactual "message volume changes but independent evidence does not" design.
- The header and focus area. "Human and Biological Systems — Warfighter Decision Superiority and Readiness" matches the NOFO wording.
- The links. All of these resolve to the named item: FaithScore (`2024.findings-emnlp.290`), FGAIF (`Qhfw5CUVd7`), QA-based event extraction, RESIN-11, GDELT, and TREC CrisisFACTS.

## Suggested text (copy-ready)

**Hypothesis, first sentence**

> We hypothesize that retrieval and synthesis that track each claim's lineage (who first reported it, who repeated it, and what later corrected it) will report fewer amplified false claims as supported than passage-level RAG, without delaying independently verified alerts.

**Evaluation**

> We will use GDELT and TREC CrisisFACTS to test event coverage and handling of updates on real crisis streams, and controlled streams with known claim lineages, corrections, and planted false claims to test deception. Measures: the rate at which planted false claims are reported as supported, recall and delay for independently verified alerts, and traceability of each reported claim to its sources. Baselines: standard RAG, self-refining RAG, and aggregation by source count.

**Naval relevance, closing sentence**

> The work addresses the program's interests in AI-enhanced retrieval-augmented generation, modeling and simulation for operations in the information environment, and problems of deception and obfuscation.

**Prior work**

> Our QA-based event extraction (Du and Cardie, 2020) and RESIN-11 (NAACL 2022 Demo) support event representation across reports; as a postdoc, the PI led system integration for the RESIN team in DARPA KAIROS. FaithScore (Jing et al., 2024) and FGAIF (Jing and Du, 2025) developed fine-grained grounding feedback for vision-language models, which we will adapt to text RAG. The PI holds a 2024 NSF CAREER award on extracting consistent event graphs from long documents.

## Sources

- [ONR Analytics, Modeling and Simulation (Local and Regional)](https://www.onr.navy.mil/organization/departments/code-34/division-341/analytics-modeling-and-simulation-local-and-regional)
- [TREC CrisisFACTS track page](https://trec.nist.gov/data/crisis.html) and [CrisisFACTS data description](https://crisisfacts.github.io/)
- [RESIN-11, NAACL 2022 Demo](https://aclanthology.org/2022.naacl-demo.7/)
- [FaithScore, Findings of EMNLP 2024](https://aclanthology.org/2024.findings-emnlp.290/)
- [FGAIF, TMLR 2025](https://mlanthology.org/tmlr/2025/jing2025tmlr-fgaif/)
- Repository: `git show ee30d22` for the edit discussed above; `.github/workflows/compile-onr.yml` for the build loop
