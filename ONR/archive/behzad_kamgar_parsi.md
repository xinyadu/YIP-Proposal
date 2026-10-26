# Knowledge-Grounded Reasoning and Self-Improvement for Autonomous AI Agents

**Xinya Du — University of Texas at Dallas**  
**FY27 ONR YIP · Informal Brief Research Concept**  
**Prospective Program Officer:** Dr. Behzad Kamgar-Parsi (Code 311; Machine Learning, Reasoning and Intelligence)

## Motivation and central question

Autonomous AI agents are asked to reason over unfamiliar information, plan multi-step operations, use tools, and revise conclusions as their environment changes. Even powerful language models can produce plausible answers supported by faulty intermediate steps, apply valid rules under invalid conditions, or carry forward unverified assumptions. Rewarding a final answer alone offers weak supervision about why an agent's reasoning succeeded or failed.

**Research question:** How can an autonomous agent acquire relevant knowledge, learn reliable reasoning processes, and verify or repair its conclusions in open-world tasks?

We propose to connect structured knowledge grounding, **process-guided learning**, and tool-executable verification so agents can improve their reasoning rather than merely produce more fluent explanations.

## Proposed research aims

**Aim 1 — Ground reasoning in explicit external knowledge.** Retrieve and extract entities, events, relations, scientific principles, and contextual constraints from heterogeneous sources. Construct compact records that distinguish observed evidence, inferred relationships, uncertain assumptions, and the conditions under which a rule applies. Investigate how these records support compositional reasoning when facts are distributed across sources.

**Aim 2 — Learn reliable reasoning from synthetic processes and fine-grained feedback.** Generate multi-hop problems and candidate reasoning trajectories from structured knowledge, including controlled counterexamples and errorful steps. Develop evaluators for factual, contextual, and logical failures; use their localized feedback to select or improve trajectories and train agents. Test whether this process supervision generalizes beyond memorized solutions and improves on outcome-only training.

**Aim 3 — Verify and revise agentic reasoning in open environments.** Equip agents to formulate hypotheses or plans, identify prerequisites, retrieve missing evidence, select appropriate tools, and execute logical, numerical, or experimental checks. Use verification failures to repair particular assumptions or steps and propagate necessary changes to downstream conclusions. Scientific hypothesis discovery offers a demanding testbed, from literature-based inspiration through executable experiment validation.

## Evaluation and potential Naval relevance

We will assess intermediate-step validity, final outcomes, error localization, repair success, and cost on held-out knowledge compositions and changed operating conditions. Baselines include retrieval-augmented agents, outcome-supervised models, conventional PRMs, and tool-using agents without explicit condition tracking. Ablations will isolate grounding, process feedback, and verification.

Foundational advances in reasoning, planning, and verification may inform future intelligent autonomous systems that must respond to incomplete evidence and explain why conclusions or actions are warranted. The proposed research uses public, reproducible research tasks and does not assume access to operational Navy systems.

**Intended contribution:** Knowledge-grounded autonomous agents that improve through verifiable process feedback and adapt their reasoning to unfamiliar situations.

---

**Draft provenance (internal; remove from PDF):** #1 NSF complex reasoning (deductive/abductive/inductive reasoning); #2 NSF scientific discovery (retrieval–hypothesis–implementation cycle); #3 DARPA FAIGEN (scientific rules and neural-symbolic tool verification); #5 DARPA trustworthy reasoning (faithful multihop explanations); #6 Amazon FG-PRM (fine-grained hallucination feedback); #8 Amazon process-guided reasoning (synthetic multi-hop trajectories, PRM-based search and distillation). Also conceptually related to AFOSR Doug/Ben. Proposed integration is future work.
