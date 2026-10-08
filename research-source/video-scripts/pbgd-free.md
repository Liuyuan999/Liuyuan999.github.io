# PBGD-Free — video narration and storyboard

Narration and storyboard. Approximately 2 minutes.

Paper: https://arxiv.org/abs/2507.20400

## 0:00–0:20

**On screen:** Show an outer update waiting for a sequence of inner updates.

**Narration:** Bilevel learning puts one optimization problem inside another. The outer decision depends on a response learned at the inner level. That dependence makes a single outer step surprisingly expensive.

## 0:20–0:45

**On screen:** Add a second lower-level response labeled value-function tracking.

**Narration:** Penalty methods use first-order information, but a lower-level value-function correction can still require an extra solve. PBGD-Free asks when we can remove that component.

## 0:45–1:10

**On screen:** Switch to one lower-level update followed by one upper-level update.

**Narration:** The method maintains one lower-level iterate and alternates gradient updates. Removing the correction creates bias, so the paper analyzes when that bias is controlled.

## 1:10–1:35

**On screen:** Show the flatness inequality and a shallow upper-level objective in the lower-level direction.

**Narration:** Flatness bounds how much the upper-level objective changes around a lower-level optimum. Together with the paper’s regularity assumptions, this condition gives the simplified updates a convergence regime.

## 1:35–2:00

**On screen:** Show backbone and head roles, then link to the paper.

**Narration:** The LLM post-training experiments learn a preference backbone with an SFT head, then evaluate the backbone again after adapting the head. Flatness connects this learning structure to the simplified optimization loop.

## Recording notes

- Keep toy diagrams visibly labeled as illustrative.
- Show paper figure/table identifiers when discussing measured results.
- End with the project URL and a link to the primary paper.
- Record narration, then add figures and captions.
