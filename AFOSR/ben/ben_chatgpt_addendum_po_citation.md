# Addendum for ChatGPT — Ben Robinson (CCMI) white paper: citing the program officer's work

**How to use:** paste this together with the existing review (`ben/Review AFOSR YIP White Paper for the CCMI Portfolio_Ben.md`) when you ask ChatGPT to revise `ben/main.tex`. The same hard constraints apply: stay within 5 narrative pages, invent nothing, change only what's asked.

---

### Item 6. Cite the program officer's work once, where it does real work

**Background.**
- **Who he is.** Dr. Benjamin Robinson manages the CCMI portfolio. Before AFOSR he worked at the AFRL Sensors Directorate on radar methods that reduce false alarms by combining two covariance-estimation approaches (DAF Technology Transfer and Transition success story).
- **Matching papers.** Two arXiv papers by a Benjamin D. Robinson match that work: high-dimensional covariance shrinkage for signal detection (with Malinas and Hero, 2021), and for Hotelling's T² (with Latimer, 2025).
- **Identity.** It is inferred from the shared topic, not stated on the papers. `[AUTHOR: confirm these are the program officer's papers before citing]`

**Where it genuinely connects.** Aim 2 says the acceptance procedure is fixed on development data and its reliability is then assessed. That is a detection problem:
- accepting an unsupported answer is a false alarm
- accepting a supported answer is a detection

Robinson, Malinas & Hero give consistent estimates of a data-adapted detector's *conditional* false-alarm and detection rates. That is, they estimate the rates given the training data used to build the detector, which is the same logic as assessing an acceptance policy fixed on development data.

**Change.** In Aim 2's reliability paragraph, after the sentence "Reliability will be assessed for the complete acceptance procedure", add one sentence. For example:

> "We treat acceptance as detection: accepting an unsupported answer is a false alarm and accepting a supported one a detection, and we report both rates for the procedure as fixed on development data, analogous to conditional false-alarm and detection rates of data-adapted detectors [Robinson et al. 2021]."

Present it as an analogy; do not claim to use their estimator. If the sentence reads as forced after editing, drop it. The program description's own wording, which items 1–2 of the review already align with, matters more than this citation.

```bibtex
@article{robinson2021shrinkage,
  title={High-Dimensional Covariance Shrinkage for Signal Detection},
  author={Robinson, Benjamin D. and Malinas, Robert and Hero, Alfred O.},
  journal={arXiv preprint arXiv:2103.11830}, year={2021}
}
```

**Sources:**
- [DAF T3 success story](https://www.aft3.af.mil/Success-Stories/Article/4520413/combination-of-old-and-new-methods-improves-radar-operation/)
- [Robinson, Malinas & Hero (arXiv 2103.11830)](https://arxiv.org/abs/2103.11830)
- [Robinson & Latimer (arXiv 2502.02006)](https://arxiv.org/abs/2502.02006)
