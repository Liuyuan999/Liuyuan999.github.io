# Efficient penalty methods — video narration and storyboard

Narration and storyboard. Approximately 2 minutes.

Paper: https://arxiv.org/abs/2511.16796

## 0:00–0:20

**On screen:** Show three cost labels: outer step, inner tracking, constraints.

**Narration:** Penalty-based bilevel learning can be expensive for different reasons. Large penalties affect curvature. Tracking a response requires updates. Moving constraints add another dependence.

## 0:20–0:45

**On screen:** Contrast a steep joint surface with a smoother reduced curve.

**Narration:** An alternating method follows a reduced objective after accounting for the inner response. The paper sharpens the smoothness analysis of that objective, supporting larger outer steps under its assumptions.

## 0:45–1:10

**On screen:** Show a fixed feasible interval beside a moving feasible interval.

**Narration:** The distinction between uncoupled and coupled constraints matters. In the coupled case, the outer decision changes the lower-level feasible set.

## 1:10–1:35

**On screen:** Show two schedules: one lower update; several constrained inner updates.

**Narration:** PBGD-Free is fully single-loop with uncoupled constraints. The coupled extension retains an inner solve and reduces its complexity. Its total computation includes both the inner and outer updates.

## 1:35–2:00

**On screen:** Show SVM and LLM application labels and the related-paper links.

**Narration:** The experiments include hyperparameter optimization and LLM fine-tuning. The central lesson is to separate the sources of cost and match each algorithmic simplification to the structure that justifies it.

## Recording notes

- Keep toy diagrams visibly labeled as illustrative.
- Show paper figure/table identifiers when discussing measured results.
- End with the project URL and a link to the primary paper.
- Record narration, then add figures and captions.
