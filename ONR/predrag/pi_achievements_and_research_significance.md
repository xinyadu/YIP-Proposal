# Research Achievements and Future Impact

**Xinya Du**  
Assistant Professor of Computer Science, The University of Texas at Dallas  
ONR FY2027 YIP | October 30, 2026  
Proposal: *Trustworthy Collective Reasoning and Evaluation for AI Agents*

## Past achievements

Since starting my lab at UT Dallas in 2022, I have led research on how language models evaluate one another and learn from feedback. In PRD (TMLR 2024) [1], we showed that a model judging its own answers can give itself an unfairly high ranking. We introduced peer ranking and peer discussion, in which models review one another's answers and their judgments are weighted and combined. The resulting rankings were closer to human preferences. This work led to PeerEval, a public leaderboard and tool for using panels of AI judges.

We also built DSBench (ICLR 2025) [2] to test agents on realistic data analysis and modeling tasks. OpenAI used DSBench to evaluate ChatGPT agent. In FG-PRM (Findings of EMNLP 2025) [3], we identified six types of hallucination in mathematical reasoning and built a model that detects these errors step by step and helps select correct solutions. I received an NSF CAREER Award in 2024. My group's work has also received a Best Paper Award at the AAAI 2025 AI4Research Workshop and a Best Poster Award at the ICML 2024 AI for Science Workshop.

## Importance of the proposed research

The proposed project studies how AI agents can make reliable decisions when they share mistakes or try to mislead one another. Several agents may agree because they repeat the same outdated report, and training on their answers can reinforce the error. I will develop methods to estimate each agent's reliability while accounting for shared information, choose debaters and judges so that manipulating ratings does not help an agent get selected, and resolve disputes using evidence the judge checks by rerunning tool calls. I will also test ways to detect collusion and train agents from the group's decisions without rewarding agreement alone. The scientific contribution is to identify the conditions under which these methods work, derive guarantees under explicit assumptions, and test their limits with real agents. For the Navy, this could help analysts combine conflicting port reports, ship tracks, or intelligence assessments while seeing which sources actually support the decision. My experience developing both AI judges and feedback for training agents lets me study how errors in evaluation affect later learning.

## Selected work and evidence

[1] [PRD, TMLR 2024](https://arxiv.org/abs/2307.02762) | [PeerEval leaderboard and tool](https://peereval-ai.github.io/)

[2] [DSBench, ICLR 2025](https://arxiv.org/abs/2409.07703) | [OpenAI's ChatGPT agent evaluation](https://openai.com/index/introducing-chatgpt-agent/)

[3] [FG-PRM, Findings of EMNLP 2025](https://aclanthology.org/2025.findings-emnlp.228/)
