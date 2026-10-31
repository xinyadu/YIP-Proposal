# Arena Academic Partnerships Program application answers

## Full name

Xinya Du

## Title / role

Assistant Professor of Computer Science

## University / institution

The University of Texas at Dallas

## U.S. city and state

Richardson, Texas

## Department / lab

Department of Computer Science

## Email

xinya.du@utdallas.edu

## Website / lab page

https://xinyadu.github.io/

## Google Scholar / publications page

https://xinyadu.github.io/publications.html

## Tenure track faculty confirmation

Yes

## Project title

PeerEval: Learning Whose AI Judgments to Trust

## Three to five sentence summary of proposed research

We will extend PRD, our framework in which language models review one another and iteratively update their influence, to learn judge weights directly from peer agreement. Building on PeerEval (https://peereval-ai.github.io/), the method scores each judge's agreement with judges from other model families and updates its weight until the panel stabilizes. We will study convergence, shared biases, and transfer to new questions and models. Arena's human votes will test the results, rather than set the main method's weights. Outputs will include a paper, an open-source tool, and reproducible evaluation reports.

## Which Arena resources or support would be most relevant

Select:

- Access to Arena datasets (subject to agreement and scoped conditions)
- Collaboration with Arena researchers

The core research uses offline evaluations. Platform experiments could be considered later if they are useful and feasible, but the project does not depend on live experimentation.

## Dataset access beyond publicly available datasets

We request up to 10,000 recent, de-identified text battles with prompts, paired responses, model identifiers, preference outcomes including ties and both-bad, coarse timestamps, and per-vote display order. Randomization metadata and repeated independent votes on the same response pairs in both orders, where available, would help separate order effects from preference ambiguity. Recent battles enable tests on new models and changing preferences. Public data support the core study; additional access would follow Arena's agreements.

## Expected outputs

A paper on iterative peer weighting, its assumptions, and failure cases; an open-source PeerEval extension; and reproducible evaluations of preference prediction, model rankings, transfer, stability, and cost. We will release permitted judgments and analysis code, with restricted data governed by the access agreement. We welcome a joint blog post or talk with Arena.

## Expected project duration

12 months from receipt of funding

## Requested funding level

$50,000

## Brief budget explanation

Approximately $36,000 will support graduate research, including applicable fringe and tuition. Model APIs and computing will receive $10,000, with pilot costs determining the final panel and sample size. Independent evaluation annotations will receive $4,000. Allocations will follow UTD requirements; no indirect costs are included unless required by institutional policy.

## Why this work is relevant to Arena

Arena's self-preference findings show why a panel needs more than a simple vote, while its human preferences provide a strong independent test of AI judges. Our project will determine whether models can learn useful evaluation weights from their own peer reviews and when that process reinforces bias. The results could complement AutoEval, support evaluation of newly released models, and identify unstable rankings that warrant further review.

## Program acknowledgments

Select all six acknowledgment statements after reviewing the form's terms.

## Openness to publicizing the research with Arena

Yes

## Link to a two page proposal

https://github.com/xinyadu/YIP-Proposal/blob/main/arena/Arena_Proposal_2page.pdf

The three-page working copy contains the two-page proposal and an additional page of form answers. Use the separate two-page PDF for the form link.

## Source links

- Program call: https://arena.ai/blog/academic-program-fall-2026
- Application form: https://docs.google.com/forms/d/e/1FAIpQLSdKwhGge-qb8MFvpwk93GBgU0XKkqbGpb6Q3-l9oilRcD7JXg/viewform
- PRD paper: https://arxiv.org/abs/2307.02762
- PeerEval project: https://peereval-ai.github.io/
- PeerEval blog: https://peereval-ai.github.io/blog.html
- Arena judge self-preference: https://arena.ai/blog/llm-judge-self-preference
- Arena AutoEval: https://arena.ai/blog/autoeval-scores
- PeerEval pilot summaries: https://github.com/peereval-ai/peereval-ai.github.io/blob/main/figures_modified_du.json
