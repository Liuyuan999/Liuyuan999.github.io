# BLOCC — video narration and storyboard

Narration and storyboard. Approximately 2 minutes.

Paper: https://arxiv.org/abs/2406.10148

## 0:00–0:20

**On screen:** Show an operator changing a network, then users selecting routes.

**Narration:** Some decisions change what other decision-makers are allowed to do. A network design determines which routes users can choose. This is a natural bilevel problem with coupled constraints.

## 0:20–0:45

**On screen:** Move the bound y ≤ x and the constrained optimum in the toy example.

**Narration:** The outer variable changes the inner feasible set. We need to account for a moving boundary, including cases where the lower-level optimum lies on that boundary.

## 0:45–1:10

**On screen:** Add primal variables and dual multipliers to a constraint box.

**Narration:** BLOCC uses a primal-dual-assisted penalty formulation. Dual information captures the role of lower-level constraints, while the algorithm uses first-order updates.

## 1:10–1:35

**On screen:** Display the lower-level strong convexity, constraint convexity, and regularity assumptions.

**Narration:** The approximation and convergence results rely on a specific regime: a strongly convex lower-level objective, convex lower-level constraints, feasible domains, and the stated regularity conditions.

## 1:35–2:00

**On screen:** Show SVM and Seville transportation headings from Section 4.

**Narration:** The experiments study constrained SVM hyperparameter optimization and transportation planning. The takeaway is to model the changing feasible set explicitly when the outer decision reshapes the inner problem.

## Recording notes

- Keep toy diagrams visibly labeled as illustrative.
- Show paper figure/table identifiers when discussing measured results.
- End with the project URL and a link to the primary paper.
- Record narration, then add figures and captions.
