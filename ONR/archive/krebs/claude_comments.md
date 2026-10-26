# Claude comments: William Krebs concept note (historically in `morrison/`)

Reviewer: Claude · 2026-10-13 · Scope: `ONR/morrison/main.tex` on `main` at `08ae8ff`; the text last changed in `e7f2146` (Oct 13, 02:15 PT). Checked against Dr. Krebs's Command and Control program page, the FY27 NOFO focus-area list, and every linked paper and dataset. *(judgment)* marks my opinion; everything else is checked.

## Verdict

Retargeting to Dr. Krebs was the right call. He is listed on ONR's directory, and the note now uses his program's language: a common tactical picture, and uncertain and out-of-sequence information.

The new two-layer design is a real improvement *(judgment)*. One layer keeps immutable source assertions; the other holds revisable event interpretations. The edit also states the key limit plainly: mergeable records do not make "neural interpretations identical".

However, the edit made the hypothesis and the evaluation vaguer, and it removed your KAIROS role. The fixes below fit in the half inch of empty space, more if you shorten the header.

## Must fix before sending

1. **The committed PDF is out of date.** `white_paper_morrison.pdf` still shows the earlier "Distributed Event Reasoning and Information Fusion for Decision Support" version.
   - Cause: since `a4c04d9`, the workflow compiles only one folder (now `behzad`), and its recent runs fail at that step.
   - Fix: restore `for d in predrag behzad morrison goolsby` in both loops of `.github/workflows/compile-onr.yml`. Alternatively, build locally and commit.
   - I compiled the current `main.tex` with pdflatex: it is one page with no overfull lines.
   - Rename the attachment before sending, as the folder README says, for example `Du_UTD_ONR-YIP_Krebs.pdf`.
2. **Make the hypothesis testable.** "Makes distributed reasoning both more consistent and more useful" names no measure and no comparison. The previous version had a test ("when nodes receiving the same evidence converge … and how accurately they answer standing questions when communication is limited"). Put one back; suggested text is below.
3. **Make the evaluation measurable.** "Evidence fidelity, reconciliation of conflicting event hypotheses, and query-relevant communication" are categories, not measures. The previous version named graph agreement, query accuracy, delivery latency, and bandwidth. Also:
   - Define the two baselines in a few words.
   - Replace "KAIROS-style event scenarios" with a corpus name or a one-line description; a PO cannot look that phrase up.
4. **Restore your KAIROS role.** `e7f2146` replaced "As a postdoc, the PI led system integration for the RESIN-11 team in DARPA KAIROS" with "DARPA KAIROS RESIN-11 system work", which drops what you did.

## Should fix

5. **Say where the research is** *(judgment)*. A grow-only layer of source assertions with message identifiers converges by construction. This is standard in replicated logs and conflict-free replicated data types ([Shapiro et al., SSS 2011](https://doi.org/10.1007/978-3-642-24550-3_29)). The open problem is the interpretation layer: making model-based entity matching, event coreference, and temporal ordering independent of the order in which evidence arrived, without recomputing everything. Aim 2 already says this implicitly. One explicit sentence makes the novelty unmistakable.
6. **Make the example's failure explicit.** "A shore node may receive these messages in reverse order" stops before the failure. Suggested ending: "…and conclude that two vessels are present."
7. **Use the standard term.** "Commanders' standing information needs" is a paraphrase of commander's critical information requirements (CCIRs), the standard C2 term. The previous version said "critical information requirements".
8. **Clarify "shared identifiers".** Message identifiers make deduplication easy, but event identity across nodes is the hard, inferred part. Say which kind you mean.
9. **"Receiver-aware summaries"** *(judgment)*. Over degraded links the sender may not know what the receiver holds. Say what the summaries are based on, for example the receiver's last acknowledged state.
10. **Strengthen the PI evidence.**
    - Add [Toward Consistent and Informative Event-Event Temporal Relation Extraction](https://aclanthology.org/2023.matching-1.3/) (Jin, Wen, Du, and Ji, MATCHING 2023). It is your most direct work on keeping event relations consistent.
    - The note says "2024 NSF CAREER award on consistent event graphs". A reader will ask what ONR funding would add, and one clause answers it: CAREER covers consistency within long documents, while this project covers consistency across disconnected nodes.
11. **Header (optional).** The full focus-area name takes three lines, with "Systems" alone on the last. The short form fits on two lines: "C5ISR and Naval Space — Intelligence, Decision Superiority, Command and Control (C2), and Combat Systems". The short form uses the NOFO's own abbreviation.

## Keep

- The two-layer design, with explicit conflict sets.
- The vessel example. It is distinct from the other notes and directly naval.
- "Expose unresolved ambiguity rather than assuming that mergeable records make neural interpretations identical."
- Selecting updates that "correct an important inference, resolve a conflict, or materially change the support for a current answer".
- The program language in the Naval paragraph, and the PO line. Dr. Krebs is the Information Science & C2 Program Officer named on the Command and Control page.
- The links. All of these resolve to the named item: QA-based event extraction, RESIN-11, MAVEN-ERE (`2022.emnlp-main.60`), and MEQA. The note uses two different MEQA links, the NeurIPS proceedings page and the OpenReview page; both are correct, but using one throughout is tidier.

## Housekeeping

- `morrison/README.md` contains a literal `\n\n` ("…do not send the PDF with Morrison's name.\n\nThe LaTeX uses…"). Replace it with a blank line.
- The README says the workflow checks each PDF and publishes it, which is not true for this folder until the workflow loop is restored (item 1).

## Suggested text (copy-ready)

**Problem, example sentence**

> An afloat node first receives a warning about an unidentified vessel and later learns it is scheduled support traffic; a shore node receives the identification first and the warning second, and may conclude that two vessels are present.

**Hypothesis**

> We hypothesize that keeping source assertions in an order-independent evidence layer, and deriving event interpretations from it with explicit conflict sets, will let nodes that hold the same evidence reach the same event hypotheses, or the same flagged ambiguities, regardless of arrival order, at a fraction of the bandwidth of full replication; chronological overwrite will not.

**Aim 2, added sentence**

> The evidence layer converges by construction; the research question is the interpretation layer, namely how to make model-based entity matching, event coreference, and temporal ordering insensitive to arrival order without recomputing from scratch.

**Evaluation**

> We will partition MAVEN-ERE documents, MEQA questions, and [named scenario corpus] across simulated nodes with delayed, duplicated, missing, and reordered reports. Measures: cross-node agreement of event hypotheses after links are restored, accuracy on standing CCIR queries over time, bytes sent per correct answer, and the share of conflicts flagged rather than silently resolved. Baselines: full replication (every report to every node) and chronological overwrite (the last message wins).

**Prior work**

> Our QA-based event extraction (Du and Cardie, 2020), consistent event-event temporal relation extraction (Jin et al., 2023), and MEQA benchmark (Li et al., 2024) provide methods for extracting and reasoning over event knowledge; as a postdoc, the PI led system integration for the RESIN team in DARPA KAIROS (RESIN-11, NAACL 2022 Demo, first author). The PI's 2024 NSF CAREER award studies consistent event graphs within long documents; this project asks how they stay consistent across disconnected nodes.

## Sources

- [ONR Command and Control program page](https://www.onr.navy.mil/organization/departments/code-31/division-311/command-and-control) and [program-officer directory](https://www.onr.navy.mil/our-research/our-program-officers)
- [MAVEN-ERE, EMNLP 2022](https://aclanthology.org/2022.emnlp-main.60/)
- [MEQA, NeurIPS 2024 Datasets and Benchmarks](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e560a0b22e4432003d0dba63ff8dc457-Abstract-Datasets_and_Benchmarks_Track.html)
- [RESIN-11, NAACL 2022 Demo](https://aclanthology.org/2022.naacl-demo.7/)
- [Jin et al., MATCHING 2023](https://aclanthology.org/2023.matching-1.3/)
- [Shapiro et al., Conflict-Free Replicated Data Types, SSS 2011](https://doi.org/10.1007/978-3-642-24550-3_29)
- Repository: `git show e7f2146` for the edit discussed above; `.github/workflows/compile-onr.yml` for the build loop
