# Evidence-Grounded Reasoning Agents for Human-AI Decision Support

**Xinya Du — University of Texas at Dallas**  
**FY27 ONR YIP · Informal Brief Research Concept**  
**Prospective Program Officer:** Dr. Jeffrey Morrison (Code 341; Command Decision Making)

## Motivation and central question

Decision makers must integrate information spread across reports, archives, and updates. Different sources may describe different aspects of an event, contradict earlier reports, or become obsolete. A language-model assistant can summarize these materials but still overlook event relationships, confound observations with assumptions, or make a confident recommendation unsupported by the underlying evidence. Better summaries alone do not establish better human decisions.

**Research question:** How can AI agents maintain consistent knowledge from evolving information and support human decisions through inspectable, evidence-grounded reasoning?

We propose dynamic event-knowledge representations coupled with verifiable multi-step reasoning and human-directed verification.

## Proposed research aims

**Aim 1 — Build and maintain consistent event knowledge.** Extract events, participants, attributes, and temporal or causal relations across long document collections. Use open-schema, question-answer-style knowledge representations to capture changing details and source provenance. Investigate incremental updates, conflicting evidence, and global logical/temporal consistency without requiring repeated processing of the entire collection.

**Aim 2 — Reason with provenance and uncertainty.** Combine structured event knowledge with retrieved text to construct answers and explanations requiring multiple steps across sources. Trace each intermediate inference to its supporting evidence; distinguish reported observations, derived conclusions, assumptions, and unresolved conflicts. Localize reasoning failures instead of presenting unsupported certainty.

**Aim 3 — Enable interactive evidence inspection and decision support.** Let users challenge an inference, ask which reports support a conclusion, or request a specific additional check. Study how the agent should represent uncertainty and revise conclusions following updates. Evaluate whether exposing provenance and limitations reduces harmful reliance on incorrect advice without discouraging appropriate reliance on correct advice.

## Evaluation and potential Naval relevance

Evaluation will examine knowledge coverage, provenance accuracy, update consistency, multi-step reasoning validity, and adaptability to conflicting reports. Human-facing studies will separately measure decision accuracy, beneficial versus harmful adoption of AI suggestions, and information-inspection burden. Comparisons will include conventional RAG, flat summarization, and assistants without explicit event representations.

The foundations may support information-intensive command decision-making, including the interpretation of changing status reports and collaborative analysis, while preserving the evidence needed for human oversight. We will use unclassified document tasks rather than presupposing Naval deployment.

**Intended contribution:** A framework for human-AI decision support that connects evolving structured knowledge to verifiable inferences and useful evidence inspection.

---

**Draft provenance (internal; remove from PDF):** #4 NSF CAREER (open-schema event graphs, document hierarchy and consistency); #1 NSF complex reasoning (multi-hop event/entity reasoning); #5 DARPA trustworthy reasoning (faithfulness); AFOSR Laura/PeerEval (human reliance and diagnostic interactions); #8 Amazon process-guided reasoning (supporting step-level verification). Human decision-support experiments are proposed new work.
