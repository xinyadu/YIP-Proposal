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

PeerEval: Aligning LLM Peer Judgments with Human Preferences

## Three to five sentence summary of proposed research

We propose human-calibrated peer evaluation to produce reliable LLM rankings from multiple model judges and limited human feedback. Building on PRD and PeerEval, we will calibrate peer competence weights against human preferences while correcting self-preference and correlated errors. A sequential policy will request additional model or human judgments when uncertainty could change a ranking. Using Arena battles, we will test preference prediction, ranking validity, and cost under shifts in time and model families. We will release methods, code, and reproducible audits showing when peer evaluation can complement human votes and AutoEval.

## Which Arena resources or support would be most relevant

Select:

- Access to Arena datasets (subject to agreement and scoped conditions)
- Collaboration with Arena researchers

The core research uses offline evaluations. Platform experiments could be considered later if they are useful and feasible, but the project does not depend on live experimentation.

## Dataset access beyond publicly available datasets

We request approximately 10,000 de-identified recent text battles containing prompts, paired responses, stable model identifiers, human preference outcomes (including ties and both-bad), and coarse timestamps. Domain tags and repeated votes would support subgroup and ambiguity analyses. Recent battles enable transfer tests on new models and changing preferences. Public data support the core study; additional access would follow Arena's agreements and scoped research conditions.

## Expected outputs

A research paper; an open-source PeerEval extension for calibrated judge weighting and sequential evaluation; and a reproducible benchmark report on preference prediction, rankings, bias, uncertainty, and costs. We will release permitted judgments, configurations, and analysis scripts. Restricted data will remain subject to its access agreement. We welcome a joint blog post or talk with Arena.

## Expected project duration

12 months from receipt of funding

## Requested funding level

$50,000

## Brief budget explanation

Approximately $36,000 will provide partial graduate research support, including applicable fringe and tuition, for method development, experiments, and the code release. Model API access and computing will receive $10,000. The remaining $4,000 will support repeated human annotations and targeted audits. Allocations will follow UTD requirements; no indirect costs are included unless required by institutional policy.

## Why this work is relevant to Arena

Arena needs scalable automated evaluations grounded in human preferences. Our project tests how to combine model judges without amplifying shared biases, and how limited human feedback can improve ranking reliability per dollar. Transfer experiments will test usefulness for new models and changing tasks. The methods and audits could inform when peer judgments should supplement human votes and AutoEval, and when more human review is needed.

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
