# Final revision comments for ChatGPT (round 2) — Laura Steckman (Trust and Influence) white paper

**How to use:** attach the current `laura/main.tex` and `laura/references.bib` to ChatGPT, then paste everything below the line.

---

You are revising an AFOSR FY27 Young Investigator Program (YIP) white paper written in LaTeX. This is the second round of revisions. The first round is already in the draft, so don't redo it. Treat this as an initial white paper, not a full proposal: every technical commitment must be meaningful and defensible, and nothing should be added just to sound more technical. Apply the revisions below in priority order.

## Context

- **Paper:** "Interactive Peer Evaluation for Calibrated Trust in AI Advisers."
- **Portfolio:** Trust and Influence, Dr. Laura Steckman (AFOSR Open BAA Amendment 0001, Section A.4.g). The program funds research on "the establishment, maintenance, and repair of trust" between humans and intelligent agents, and on social influence.
- **PI:** Xinya Du, The University of Texas at Dallas.
- **Deadline:** 9 October 2026, 11:59 PM Eastern, through the official Qualtrics portal.
- **Scoring:** two equally weighted criteria, technical merit and "Potential relationship of the proposed research and development to DoW missions" (YIP notice FA955026S0003, F.2.b.1).

## Hard constraints

1. **Page limit.**
   - The narrative may not exceed 5 pages; the cover, CV and references don't count.
   - The last narrative page is about 45% full, roughly 200 words of room.
   - Removing `\Needspace{10\baselineskip}` before "Team and work plan" reclaims about 80 more words (tested).
   - Offset anything beyond that with cuts. Recompile with XeLaTeX and report the narrative page count.
2. **Invent nothing.** No new citations except the verified entries at the end. No results, collaborators, consultants, program text or mission details the author hasn't supplied. Where the author must supply something, write `[AUTHOR: …]`.
3. **Change only what's asked.** Keep every sentence the items below don't touch, and everything under "Keep."
4. **Return:**
   - the full revised `main.tex`
   - the BibTeX entries you added
   - a change log keyed to the item numbers
   - every `[AUTHOR: …]` item
   - the final narrative page count

## Already done — don't redo

- **Question and fit:** the central question is now human-centered; Studies 1–2 are named for social influence and trust repair; the program's own wording is used.
- **Running example:** one adviser and three evaluators, with roles defined; PeerEval is described accurately.
- **Behavioral grounding:** Lee & See, Yousif et al., Bonaccio & Dalal, Dietvorst et al., Lyons et al. and Ueno et al. are cited.
- **Methods:** Dawid & Skene is cited, with an observer-error baseline; Sharma et al. is cited for harmful revisions.
- **Relevance and team:** the Air Force and Space Force impact paragraph and the IQA-EVAL experience sentence are added.

## Remaining problems, ranked

### 1. Study 2 misses its closest precedent, which predicts the opposite of selective adjustment

> Prior work shows that seeing an algorithm err can induce avoidance; trust repair remains an open question in human-autonomy teaming.

> We will test whether the evidence supports selective adjustment rather than indiscriminate acceptance or rejection of the adviser.

**Why.**
- **The closest precedent is uncited.** In Dzindolet et al. (2003), people who watched an automated aid err distrusted it unless told why it might err. That explanation raised trust and reliance, even when the trust was unwarranted.
- **It is a direct precedent for the Study 2 manipulation**, which compares a correction alone with a correction plus diagnostic evidence.
- **It supplies a sharp competing prediction.** Diagnostic evidence may restore reliance *globally*, including on the recurring failure type, rather than selectively. The design already separates the two predictions, since it shows both recurrences of the failure type and unrelated advice.
- **Trust repair is an established research line, not only an open question.** Two key papers:
  - de Visser, Pak & Shaw (2018) on trust repair in human–machine interaction.
  - de Visser et al. (2020) on longitudinal trust calibration in human–robot teams. This one is supported by the Air Force Office of Scientific Research, and its first author is at the US Air Force Academy's Warfighter Effectiveness Research Center.

**Change.**
- **Add the competing prediction to Study 2.** For example:
  > "Explanations of why an aid errs can raise reliance even when it is unwarranted [Dzindolet et al. 2003], so diagnostic evidence might restore reliance indiscriminately; the recurrence-versus-unrelated contrast distinguishes this from selective adjustment."
- **Cite the trust-repair line.** Cite de Visser et al. (2020) where the paper claims "dynamic trust assessment" or introduces the sequential behavioral model. Cite de Visser, Pak & Shaw (2018) beside Lyons et al. Rephrase "trust repair remains an open question" so it doesn't imply the topic is unstudied.

### 2. Study 1: report what Ueno et al. found, and cite the work on when the illusion of consensus shrinks

> Behavioral research finds an illusion of consensus even when people can identify shared sources, although the effect depends on the task. Prior work has also tested source consensus in AI explanations using a curated, accurate adviser.

**Why.**
- **Ueno et al. already observed the main Study 1 prediction.** In their CHI 2023 extended abstract (35 participants), no illusion of consensus appeared when the AI agent labeled how its sources related. True consensus produced more reliance than false consensus. Reviewers will therefore ask what Study 1 adds, and the paper should answer against that finding.
- **The answer is already in the design:**
  - evaluators that can themselves be wrong
  - harmful *and* beneficial adoption, measured separately
  - a preregistered, larger sample
  - repeated decisions over time
- **Yousif et al. don't support "the effect depends on the task."** Their abstract reports people about equally confident in single-source and independent consensus, even after judging independent consensus more believable. Two other papers supply the moderating evidence:
  - Connor Desai, Xie & Hayes (2022): the illusion shrinks when people learn the sources used different data and methods, though false consensus is still not fully discounted.
  - Whalen, Griffiths & Buchsbaum (2018): people discount agreement that comes from shared evidence in some settings but not in others.

**Change.** Rewrite the two quoted sentences as three or four:
- Yousif et al. for the illusion.
- Connor Desai et al. and Whalen et al. for when it shrinks.
- Ueno et al. for the AI case: labeling source relations removed the illusion in a small study with an always-accurate agent.
- Close with: "Study 1 tests whether this holds when the evaluators themselves can be wrong, measuring harmful and beneficial adoption separately."

### 3. Add a second competing prediction: richer evaluation records may increase over-reliance

> randomly assign participants to three displays: an endorsement count, a calibrated reliability estimate, and the same estimate accompanied by checked sources and unresolved objections.

**Why.**
- **Explanations can backfire.** Si et al. (NAACL 2024) found that LLM explanations help people verify claims, except when the model is convincingly wrong; then they increase over-reliance. The richest display (checked sources) could likewise make wrong advice look better supported.
- **Hedged language can help.** Kim et al. (FAccT 2024, 404 participants) found that first-person uncertainty expressions reduced over-reliance, though not completely. That bears on how "unresolved objections" should be worded.

**Change.**
- **State the risk.** Add one sentence to Study 1 naming it as a competing prediction, citing Si et al.
- **Credit the design.** Note that the balanced-correctness design already tests it.
- **Optional:** cite Kim et al. where unresolved concerns are displayed.

### 4. Position Aims 1–2 against the closest computational prior work

> A starting method will adjust peer weights using these estimates and group endorsements that rely on the same source.

> Candidate questions will request a precise supporting passage, challenge an apparent contradiction, or ask whether a newer record changes the answer.

**Why.**
- **Aim 1 has close precedents.**
  - **Discounting copied sources is established.** Truth discovery already detects copying between sources and discounts copied votes (Dong, Berti-Equille & Srivastava, VLDB 2009).
  - **Difficulty modeling needs a citation.** Jointly estimating rater expertise and item difficulty is GLAD (Whitehill et al., NeurIPS 2009). Dawid & Skene alone doesn't model difficulty, as the revision response itself notes.
  - **Panels of LLM judges are a current method.** See Verga et al. (2024). Increasingly similar mistakes across strong models undermine oversight, including judges favoring similar models (Goel et al., ICML 2025).
- **Aim 2 has close precedents.**
  - **Cross-examination is the closest prior work.** A second language model questions the first to detect factual errors (Cohen et al., EMNLP 2023).
  - **Answer-flipping is documented.** When challenged with "Are you sure?", models change answers in about 46% of cases, and accuracy drops (Laban et al., 2023). That is the harmful revision Aim 2 measures.

**Change.**
- **Aim 1:** cite Whitehill et al. for difficulty and Dong et al. for copied sources. State that the new element is dependence among LLM evaluators, observable through provenance, and how that dependence affects human reliance. Cite Verga et al. where the panel is introduced; Goel et al. is optional.
- **Aim 2:** cite Cohen et al. and add one clause on the difference: these questions target provenance and recency, are scored separately for detection, correction and harm, and feed the human studies. Cite Laban et al. beside Sharma et al.

### 5. Sharpen the central hypothesis

> Our central hypothesis is that people may treat repeated endorsements as corroboration, while diagnostic evidence can help them distinguish shared error from independent support.

**Why.** "May" and "can" make the hypothesis hard to falsify.

**Change.**
> "Our central hypothesis is that people weigh endorsements that share a single source nearly as heavily as independent ones, and that disclosing shared sources together with diagnostic evidence reduces harmful adoption without reducing beneficial adoption."

### 6. State the Study 1 design and one measurable benchmark

> An initial planning range is 200–300 participants per study

**Why.**
- **Many factors, modest sample.** Study 1 crosses display (three levels), sourcing (shared versus separate), advice correctness and task type (lookup versus integration). With 200–300 participants, reviewers will want to know which factors vary within participants and which contrast is primary.
- **Benchmarks are weighed.** Reviewers weigh "clear benchmarks", and full proposals must include them (YIP notice C.3.b, EO 14332).

**Change.** Add, for example:
> "Display varies between participants; sourcing, advice correctness and task type vary within participants. The preregistered primary contrast is display by sourcing on harmful adoption, with beneficial adoption tested for non-inferiority against a margin fixed in preregistration."

`[AUTHOR: confirm design]`

### 7. Cover acknowledgment, behavioral expertise, and title

> Separate drafts have been prepared for Dr. Ben Robinson and Dr. Doug Riecken.

> The PI will seek consultation on behavioral protocols and power analysis before confirmatory data collection.

**Why.**
- **The cover line isn't an acknowledgment.** The notice (D.2.b) requires each submission to acknowledge the others; "drafts have been prepared" is not that, and it reads oddly to a program officer.
- **Behavioral expertise is still the main feasibility gap**, and this portfolio's reviewers will look for it.
- **The title describes the method, not the science.** It foregrounds the method rather than the trust-and-influence science the paper now centers.

**Change.**
- **Cover.**
  > "The PI is also submitting white papers to the Computational Cognition and Machine Intelligence (Dr. Ben Robinson) and Science of Information, Computation, Learning, and Fusion (Dr. Doug Riecken) portfolios."

  `[AUTHOR: list only papers actually submitted]`
- **Expertise.** Name a behavioral-science consultant or collaborator only if one has agreed. `[AUTHOR: name and role, or leave as is]`
- **Title (optional).** For example: "When Does AI Consensus Deserve Trust? Shared Sources, Diagnostic Evidence, and Human Reliance on AI Evaluators."

## Keep — do not weaken

- **Measures:** the definitions of reliability, trust and reliance; initial answer and confidence recorded before the advice; beneficial and harmful adoption scored separately, with both-wrong cases analyzed apart.
- **Study 1:** the targeted contrast that holds advice, endorsements and estimate fixed, plus its comprehension checks.
- **Study 2:** recurrence versus unrelated advice, with randomized evidence presentation.
- **Honest limits:** "Neither result establishes that peer scores are probabilities of correctness or that simulated users reproduce human trust." Also: source overlap treated as observable dependence; ambiguous cases kept as unresolved.
- **Analysis:** the strong baselines; preregistration; power simulation; repeated-measures analysis; institutional review; and negative results counted as informative.

## Leave for the full proposal

- **Study details:** the reference-label protocol and the dependence model's specification; power simulations, attrition and final sample sizes.
- **A second population:** a test with participants whose backgrounds resemble DAF users.
- **Required elements:** the Gold Standard Science commitment (EO 14303), the data management plan, and per-year benchmarks.

## Verified citations

**Add now:**

```bibtex
@article{dzindolet2003role,
  title={The Role of Trust in Automation Reliance},
  author={Dzindolet, Mary T. and Peterson, Scott A. and Pomranky, Regina A. and Pierce, Linda G. and Beck, Hall P.},
  journal={International Journal of Human-Computer Studies},
  volume={58}, number={6}, pages={697--718}, year={2003},
  doi={10.1016/S1071-5819(03)00038-7}
}
@article{devisser2020longitudinal,
  title={Towards a Theory of Longitudinal Trust Calibration in Human--Robot Teams},
  author={de Visser, Ewart J. and Peeters, Marieke M. M. and Jung, Malte F. and Kohn, Spencer and Shaw, Tyler H. and Pak, Richard and Neerincx, Mark A.},
  journal={International Journal of Social Robotics},
  volume={12}, number={2}, pages={459--478}, year={2020},
  doi={10.1007/s12369-019-00596-x}
}
@article{devisser2018repair,
  title={From `Automation' to `Autonomy': The Importance of Trust Repair in Human--Machine Interaction},
  author={de Visser, Ewart J. and Pak, Richard and Shaw, Tyler H.},
  journal={Ergonomics},
  volume={61}, number={10}, pages={1409--1427}, year={2018},
  doi={10.1080/00140139.2018.1457725}
}
@article{connordesai2022source,
  title={Getting to the Source of the Illusion of Consensus},
  author={Connor Desai, Saoirse and Xie, Belinda and Hayes, Brett K.},
  journal={Cognition},
  volume={223}, pages={105023}, year={2022}
}
@article{whalen2018shared,
  title={Sensitivity to Shared Information in Social Learning},
  author={Whalen, Andrew and Griffiths, Thomas L. and Buchsbaum, Daphna},
  journal={Cognitive Science},
  volume={42}, number={1}, pages={168--187}, year={2018},
  doi={10.1111/cogs.12485}
}
@inproceedings{si2024convincingly,
  title={Large Language Models Help Humans Verify Truthfulness -- Except When They Are Convincingly Wrong},
  author={Si, Chenglei and Goyal, Navita and Wu, Tongshuang and Zhao, Chen and Feng, Shi and Daum{\'e} III, Hal and Boyd-Graber, Jordan},
  booktitle={Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
  pages={1459--1474}, year={2024},
  doi={10.18653/v1/2024.naacl-long.81}
}
@inproceedings{dong2009dependence,
  title={Integrating Conflicting Data: The Role of Source Dependence},
  author={Dong, Xin Luna and Berti-Equille, Laure and Srivastava, Divesh},
  booktitle={Proceedings of the VLDB Endowment},
  volume={2}, year={2009}
}
@inproceedings{whitehill2009whose,
  title={Whose Vote Should Count More: Optimal Integration of Labels from Labelers of Unknown Expertise},
  author={Whitehill, Jacob and Wu, Ting-fan and Bergsma, Jacob and Movellan, Javier R. and Ruvolo, Paul L.},
  booktitle={Advances in Neural Information Processing Systems},
  volume={22}, year={2009}
}
@article{verga2024juries,
  title={Replacing Judges with Juries: Evaluating {LLM} Generations with a Panel of Diverse Models},
  author={Verga, Pat and Hofstatter, Sebastian and Althammer, Sophia and Su, Yixuan and Piktus, Aleksandra and Arkhangorodsky, Arkady and Xu, Minjie and White, Naomi and Lewis, Patrick},
  journal={arXiv preprint arXiv:2404.18796}, year={2024}
}
@inproceedings{cohen2023lmvslm,
  title={{LM} vs {LM}: Detecting Factual Errors via Cross Examination},
  author={Cohen, Roi and Hamri, May and Geva, Mor and Globerson, Amir},
  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
  pages={12621--12640}, year={2023},
  doi={10.18653/v1/2023.emnlp-main.778}
}
@article{laban2023flipflop,
  title={Are You Sure? {C}hallenging {LLMs} Leads to Performance Drops in The {FlipFlop} Experiment},
  author={Laban, Philippe and Murakhovs'ka, Lidiya and Xiong, Caiming and Wu, Chien-Sheng},
  journal={arXiv preprint arXiv:2311.08596}, year={2023}
}
```

**Optional:**

```bibtex
@inproceedings{kim2024uncertainty,
  title={``{I}'m Not Sure, But...'': Examining the Impact of Large Language Models' Uncertainty Expression on User Reliance and Trust},
  author={Kim, Sunnie S. Y. and Liao, Q. Vera and Vorvoreanu, Mihaela and Ballard, Stephanie and Vaughan, Jennifer Wortman},
  booktitle={Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT)},
  year={2024}
}
@inproceedings{goel2025thinkalike,
  title={Great Models Think Alike and this Undermines {AI} Oversight},
  author={Goel, Shashwat and Str{\"u}ber, Joschka and Auzina, Ilze Amanda and Chandra, Karuna K. and Kumaraguru, Ponnurangam and Kiela, Douwe and Prabhu, Ameya and Bethge, Matthias and Geiping, Jonas},
  booktitle={Proceedings of the 42nd International Conference on Machine Learning},
  series={Proceedings of Machine Learning Research}, volume={267},
  pages={19621--19678}, year={2025}
}
@article{hoff2015trust,
  title={Trust in Automation: Integrating Empirical Evidence on Factors That Influence Trust},
  author={Hoff, Kevin Anthony and Bashir, Masooda},
  journal={Human Factors},
  volume={57}, number={3}, pages={407--434}, year={2015},
  doi={10.1177/0018720814547570}
}
```

Hoff & Bashir organizes trust into dispositional, situational and learned layers. It fits the paper's "drivers of trust" framing if there is room.

## Sources checked

- [Dzindolet et al. 2003 (record)](https://scispace.com/papers/the-role-of-trust-in-automation-reliance-a9gwovd6ub)
- [de Visser et al. 2020, with its AFOSR acknowledgment](https://link.springer.com/article/10.1007/s12369-019-00596-x)
- [de Visser, Pak & Shaw 2018 (Crossref)](https://api.crossref.org/works/10.1080/00140139.2018.1457725)
- [Ueno et al. 2023](https://arxiv.org/abs/2304.11279)
- [Yousif et al. 2019 abstract](https://www.psychologicalscience.org/journals/psychological-science/0956797619856844/)
- [Connor Desai et al. 2022 (UNSW summary)](https://www.unsw.edu.au/news/2022/02/how-can-we-get-better-at-telling-misinformation-from-reliable-ex), with the citation confirmed in [Connor Desai et al. 2025](https://escholarship.org/content/qt0th217zh/qt0th217zh.pdf)
- [Whalen et al. 2018](https://bpb-us-w2.wpmucdn.com/sites.brown.edu/dist/3/495/files/2023/03/Sensitivity-to-Shared-Information-in-Social-Learning.pdf)
- [Si et al. 2024](https://aclanthology.org/2024.naacl-long.81/)
- [Kim et al. 2024](https://arxiv.org/abs/2405.00623)
- [Dong et al. 2009](https://lunadong.com/publication/dependence_vldb.pdf)
- [Whitehill et al. 2009](https://papers.nips.cc/paper_files/paper/2009/hash/f899139df5e1059396431415e770c6dd-Abstract.html)
- [Verga et al. 2024](https://arxiv.org/abs/2404.18796)
- [Goel et al. 2025](https://proceedings.mlr.press/v267/goel25b.html)
- [Cohen et al. 2023](https://aclanthology.org/2023.emnlp-main.778/)
- [Laban et al. 2023](https://arxiv.org/abs/2311.08596)
- [Hoff & Bashir 2015](https://experts.illinois.edu/en/publications/trust-in-automation-integrating-empirical-evidence-on-factors-tha/)
