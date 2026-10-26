# Reliable Knowledge-Grounded AI Copilots for Dynamic Information Synthesis

**Xinya Du — University of Texas at Dallas**  
**FY27 ONR YIP · Informal Brief Research Concept**  
**Prospective Program Officer:** Dr. Rebecca Goolsby (Code 341; Analytics, Modeling and Simulation)

## Motivation and central question

Retrieval-augmented AI copilots can summarize large collections of reports but do not necessarily synthesize them correctly. A copilot may merge obsolete and current statements, misattribute relations among entities, overlook qualifications, or generate a conclusion that is inconsistent with the retrieved evidence. Such errors are difficult to diagnose when sources are heterogeneous and the information environment changes rapidly.

**Research question:** How can a copilot construct grounded syntheses from evolving information, verify the claims it makes, and correct errors without introducing new unsupported conclusions?

We propose to integrate structured information extraction, multi-step claim verification, and fine-grained feedback-driven repair in a dynamic knowledge-intensive copilot.

## Proposed research aims

**Aim 1 — Structure heterogeneous, changing information.** Extract entities, attributes, events, temporal relations, and source provenance from documents into adaptable, consistent knowledge representations. Identify duplicated, contradictory, and superseded statements while retaining the original evidence. Study efficient incremental updating as new reports become available.

**Aim 2 — Verify synthesized claims through knowledge and reasoning tools.** Decompose a generated response into checkable assertions and identify each assertion's required facts, relations, rules, and assumptions. Use a verification planner to retrieve evidence, query structured knowledge, or execute symbolic and numerical checks. Produce diagnostic outcomes—supported, contradicted, or unresolved—without mistaking successful tool execution for proof that a principle applies.

**Aim 3 — Refine the synthesis using localized feedback.** Select targeted evidence-acquisition or correction actions for unsupported response components. Train and evaluate fine-grained feedback models for entity, attribute, relation, factuality, and reasoning consistency, using synthetic and independently labeled cases. Preserve supported content when repairing errors and check for downstream inconsistencies.

## Evaluation and potential Naval relevance

We will benchmark multi-document synthesis under controlled stale reports, conflicting claims, and shifts in topics or sources. Outcomes include claim support, logical consistency, update robustness, harmful revisions, coverage, and computation. Comparisons include conventional RAG, LLM self-critique, iterative retrieval, and unstructured verification.

The work may inform AI-assisted information synthesis for logistics, maintenance, and situation reports, where an analytic copilot should identify outdated evidence and expose the basis for its conclusions. This is foundational method research with public or synthetic evaluation material, not a claim of operational validation.

**Intended contribution:** Copilots that maintain evidence-grounded conclusions and can identify and selectively repair verification failures as information changes.

---

**Draft provenance (internal; remove from PDF):** #4 NSF CAREER (event extraction and dynamic consistent graphs); #3 DARPA FAIGEN (scientific-knowledge acquisition and neural-symbolic claim verification); #7 Google FG-RLAIF (entity/attribute/relation and logical/factual feedback); #6 Amazon FG-PRM and #8 Amazon process-guided reasoning (supporting localized feedback and training). Proposed synthesis is future research.
