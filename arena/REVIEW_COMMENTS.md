# Review comments — Arena Fall 2026 proposal

Reviewed `Arena_Proposal.tex`, `Arena_Application_Answers.md`, and both PDFs against the program call,
the application form, and Arena's published research.

**Compliance checks pass.** `Arena_Proposal_2page.pdf` is exactly two pages. The summary is five
sentences and the budget explanation four, both inside the 3–5 guidance. Eligibility, funding ceiling,
and duration are all answered. Form field 12 is multi-select and the answer deliberately omits platform
experimentation, which is defensible given the offline design.

**One timing issue.** The call states submissions were due **October 30, 2026**. If this has not been
submitted, it is late; the form showed no closure notice as of October 31, so a late submission may
still transmit, but the next clean cycle is Spring 2027.

---

## The main gap: the proposal has preliminary results and does not use them

We have already run the central experiment on 1,179 real Arena votes (794 crowd, 385 expert) with four
judges scoring every battle blind to the human vote. Nothing in the proposal mentions this. Reviewers
fund demonstrated capability, and these numbers also pre-empt the two objections a referee is most
likely to raise.

Suggested insertion after the first paragraph of **Research objective and foundation**, roughly 90 words:

> In preliminary work we scored four judges against 1,179 Arena battles. Weighting judges by answer
> competence, as PRD does, is uninformative on this data: competence correlates **−0.17** with
> agreement with humans, and PRD's rescaling zeroes the judge with the best recovery of the human model
> ranking (Spearman 0.882) while giving a quarter of the weight to the judge that agrees with humans
> least (0.545). Weighting instead by inter-judge agreement raises panel agreement from 0.657 to
> **0.679** (+0.022, 95% CI [+0.009, +0.034]) and cuts the panel's family bias from +9.2 to +3.1
> percentage points.

That last result is the strongest card in the application, because it **contradicts the prior drawn
from Arena's own data.** Arena found judges agree with each other 79.4% of the time but with people only
56.9%, and that on the 393 unanimous battles humans concurred just 60.6%. By that logic, weighting on
mutual agreement should amplify shared taste. It did the reverse, and we cannot yet explain why. A
funder's unexplained anomaly in their own data is a better hook than a promised improvement.

---

## Substantive comments, in priority order

### 1. The competence prior is assumed sound; our data says it is not

Aim 1 constructs "normalized peer weights, which measure answer competence before any human labels are
used," and Aim 2 shrinks the fitted weights toward that prior with "a regularizer." The proposal never
asks whether the prior is any good.

On our measurements it is not. Competence-to-judging correlation is **−0.17** (crowd) and **−0.11**
(expert). PRD assigns `grok-4.6` a weight of exactly **0.000** in 100% of 600 bootstrap resamples,
because min–max rescaling zeroes the weakest contestant and grok trails the next-worst by 0.39 in
contestant score. Grok is simultaneously the best single judge at ranking recovery. Meanwhile
`gpt-6-astra` holds 0.259 (crowd) and 0.334 (expert) while scoring worst on every metric we measure.

Shrinking toward a prior that is anti-correlated with the target will cost sample efficiency, which is
exactly the quantity Aim 2's label-budget curves are meant to demonstrate. Two options:

- **Reframe the prior as a hypothesis.** State that competence-based weighting is being tested, not
  assumed, and that the regularizer's selected strength is itself a finding: if calibration drives
  shrinkage to zero, the prior is worthless and that is publishable.
- **Carry two priors.** Competence (PRD) and mutual agreement, with the comparison as a stated
  deliverable. We have the agreement implementation working and validated under 5-fold cross-fitting.

The second is stronger and costs the proposal almost nothing, since Aim 3 already builds the co-error
machinery that agreement weighting needs.

### 2. The dataset request omits the one field we most need

The request asks for "prompts, paired responses, stable model identifiers, human preference outcomes
(including ties and both-bad), and coarse timestamps." It does not ask for **per-vote display order**.

That omission forfeits a result nobody else can get. Public battles carry one vote in one order, so
human position bias is *mathematically unidentifiable* — we can bound its net effect at roughly ±3.5pp
from the marginal split, but cannot separate "no bias" from "bias offset by quality imbalance."
Meanwhile our judges are position-corrected by construction, since every pair is judged both ways and
averaged. We are therefore scoring a corrected instrument against a possibly uncorrected label, which
imposes an unknown ceiling on achievable judge–human agreement that the field implicitly treats as 1.0.

Add display order to the request and the project gains a headline deliverable: **the first corrected
ceiling for judge–human agreement.** It is a small ask, it is unique to Arena, and it directly serves
AutoEval's validity.

### 3. The primary outcome metric rewards the bias the project is about

Primary outcomes are "held-out preference log loss, Kendall correlation with human model rankings, and
total evaluation cost." Crowd voters prefer the longer answer **65.8%** of the time (60.5% on expert
votes). A rule reading "pick the longer answer" scores **0.658**, against the best single judge's 0.690.

So log loss against human votes partly rewards verbosity alignment. A method can improve it by becoming
more length-biased, and the one judge in our panel near length-indifference (44.6% versus the human
65.8%) scores worst on every metric we report — it is penalised for resisting the confound.

Recommend adding a length-controlled primary outcome. The cheapest version is stratified: score
separately on battles where the human picked the longer answer and where they picked the shorter, then
average with equal weight, which makes the length heuristic score exactly 0.500 by construction. We
have this implemented.

### 4. State the effect size the study is powered to detect

"We target improved calibration at equal cost and at least 25% fewer judge calls than a complete panel
at matched ranking agreement." The 25% is concrete and falsifiable, which is good.

The calibration half needs a number, because the available headroom may be very small. Grid-searching
every possible weighting of our four-judge panel gives a ceiling of **0.6958** against the best single
judge's **0.6895** — **+0.006**. If that holds at 10,000 battles, then no weighting scheme, ours or an
oracle's, can show much on crowd votes, and a reviewer who works this out will read "improved
calibration" as unfalsifiable. Either name the minimum detectable effect, or say explicitly that the
headroom measurement is itself an Aim 1 deliverable.

### 5. Use Arena's specific numbers where they motivate a design choice

Aim 3's "covariance penalty that discourages redundant judge influence" is well-motivated, but the
motivation is left implicit. Arena measured the three OpenAI judges rating each other **+37 points**
above human ratings while outside judges gave those same models only **+6**. Citing that converts the
penalty from a reasonable precaution into a response to a measured effect of known size.

Similarly, our independent replication is worth one sentence: we measure `gpt-6-astra` self-preference
at **+54pp** against Arena's **+55.3pp**, on a different corpus with a different question distribution.
Agreement to 1.3 points is evidence the effect generalises beyond Arena's distribution, and it shows our
measurements are comparable to theirs rather than merely similar.

### 6. Scope risk across four aims

Aim 4 alone — uncertainty-driven acquisition with logged selection probabilities, inverse-probability
weighting, frozen thresholds, and a minimum exploration rate — is a paper. Four aims on partial support
for one graduate student over twelve months is ambitious, and the months 1–3 / 4–6 / 7–9 / 10–12 split
leaves no slack.

The methodological hygiene here is genuinely strong and worth keeping: order reversals surfacing
unstable judgments, self-exclusion, family balancing, prompt-disjoint audits, audit labels never
entering weight fitting, and separate accounting for dollars, model calls and human votes so that
"savings in calls accompanied by disproportionate human effort will not count as an efficiency gain."
That last line is the kind of thing that earns reviewer trust.

Consider marking Aim 4 as a stretch goal, or stating that Aims 1–3 are the committed deliverables. A
proposal that lands three aims beats one that reports four partially.

### 7. Budget sanity

$10,000 for model APIs should be checked against the design. Our four-judge, 1,179-battle meta-evaluation
consumed roughly **9,600 judging calls**. Scaling to eight judges across 10,000 battles in both display
orders is about **160,000 calls**, plus the peer-judgment matrix for the prior, which is O(N²) in panel
size per question. At frontier per-token pricing on long prompts, $10,000 is plausible but not
comfortable, and the judging budget is what determines statistical power. Worth one sentence showing the
calculation, which also demonstrates the costs are understood.

$4,000 for human annotation covers the stated 0–500 label budgets comfortably. The open-ended "acquired
human votes" in Aim 4 is the item that could overrun.

---

## Smaller notes

- **Kendall over Spearman is the right call** for ranking agreement at this model count; worth keeping.
  We used Spearman, and with 15 models it is coarse enough that one model displaced two places moves it
  about 0.02.
- **Panel size.** "Six to eight judges" is well chosen. Our four-judge results fit four weights from
  four models, which is the main reason we cannot claim the agreement result is established.
- **Naming.** The proposal says "our PRD method" and cites Li, Patel & Du (TMLR 2024). If the PeerEval
  site is renaming the agreement-weighted variant to PRD, the proposal and the blog need to agree, since
  the blog's method description, formulas, leaderboard weights, and "repeat until weights converge"
  pipeline all describe the original contestant-skill algorithm.
- **Missing limitations paragraph.** "Failures and uncertainty will be reported alongside gains" is good
  but generic. Two concrete pre-registered limitations would read better: that the agreement advantage
  disappears under length control, and that our best single judge beats our panel on one of two
  datasets. Stating known negatives up front is the strongest available signal of calibration.
- Both PDFs render cleanly and the working copy's third page of form answers is a sensible convenience.

---

## Summary

The design is sound and the methodological care is above the norm for this kind of application. The
single highest-value edit is adding the preliminary results, because they turn an interesting question
into a question the team has already partly answered, and because the agreement-weighting anomaly
engages Arena's own findings more directly than anything currently in the text. The second is adding
per-vote display order to the dataset request, which is the one input that cannot be substituted and
which yields a deliverable no one else can produce.

The one claim I would soften is any promise of improved calibration, until the headroom on the target is
measured. On our data that headroom is +0.006, and a reviewer who notices will discount the rest.
