# Research Achievements and Future Impact

**Xinya Du**  
Assistant Professor of Computer Science, The University of Texas at Dallas  
ONR FY2027 YIP | October 30, 2026  
Proposal: *Trustworthy Collective Reasoning and Evaluation for AI Agents*

## Past achievements

Since joining UT Dallas in 2022, I have built an independent research program on how AI systems can evaluate, verify, and improve their own reasoning. In PRD (TMLR 2024) [1], my group introduced peer ranking and peer discussion for evaluating large language models. We showed that a model used as the sole judge can favor its own answers, and that weighting and aggregating peer judgments can produce rankings more consistent with human judgments. This work treats evaluation as a collective inference problem: models assess one another, and their judgments are combined to reduce individual bias. It provides the foundation for PeerEval, our public leaderboard and evaluation tool, and directly motivates this proposal's study of reliable collective AI oversight.

My group has also developed methods and benchmarks that connect evaluation to measurable agent capabilities. DSBench (ICLR 2025) [2] evaluates agents on realistic data analysis and modeling workflows; OpenAI used it to evaluate ChatGPT agent. FG-PRM (Findings of EMNLP 2025) [3] identifies six types of hallucination at individual reasoning steps and improves mathematical answer verification, providing a basis for learning from detailed feedback. Together, these contributions establish my experience in peer evaluation, realistic agent assessment, and process-level supervision. My independent research has been recognized with an NSF CAREER Award, a Best Paper Award at the AAAI 2025 AI4Research Workshop, and a Best Poster Award at the ICML 2024 AI for Science Workshop.

## Importance of the proposed research

My proposed research addresses a central obstacle to scalable AI oversight: how can a group of agents reach trustworthy decisions when their reliability is unknown, their mistakes are correlated, and some agents may act strategically? As agents increasingly supply the evaluations and rewards used to train other agents, shared errors can propagate through both decisions and learning. The project develops statistical models that account for shared mistakes, impartial selection of debaters and judges, debates grounded in tool evidence the judge independently reproduces, and audits for collusion. It then uses the resulting decisions to improve agents through rewards designed to prevent agreement alone from being rewarded. The scientific goal is to establish when collective evaluation is reliable, what assumptions it requires, and where it fails, drawing on statistics, social choice, and reinforcement learning. For the Navy, this could enable auditable decision support when multiple AI tools reconcile copied, outdated, or conflicting reports under limited human oversight, including maritime domain awareness and intelligence analysis. My record in peer evaluation, agent benchmarks, and process rewards positions me to connect these foundations to working systems and rigorous empirical tests.

## Selected work and evidence

[1] [PRD, TMLR 2024](https://arxiv.org/abs/2307.02762) | [PeerEval leaderboard and tool](https://peereval-ai.github.io/)

[2] [DSBench, ICLR 2025](https://arxiv.org/abs/2409.07703) | [OpenAI's ChatGPT agent evaluation](https://openai.com/index/introducing-chatgpt-agent/)

[3] [FG-PRM, Findings of EMNLP 2025](https://aclanthology.org/2025.findings-emnlp.228/)
