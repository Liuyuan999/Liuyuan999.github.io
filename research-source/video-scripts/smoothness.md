# Rethinking smoothness — video narration and storyboard

Narration and storyboard. Approximately 2 minutes.

Paper: https://eurasip.org/Proceedings/Eusipco/Eusipco2025/pdfs/0001183.pdf

## 0:00–0:20

**On screen:** Show a large penalty followed by a short gradient step.

**Narration:** A large penalty often leads to a large smoothness bound and a small step size. But which objective is that bound describing?

## 0:20–0:45

**On screen:** Reduce a two-variable surface to a one-variable curve following the inner optimum.

**Narration:** A joint objective and a reduced outer objective have different geometries. An alternating method follows the second, after accounting for the lower-level response.

## 0:45–1:10

**On screen:** Show two value functions and their scaled difference.

**Narration:** The paper analyzes a difference of value functions. Their directional curvatures can cancel in a way that a generic joint bound misses.

## 1:10–1:35

**On screen:** Display O(1) smoothness and the improved outer iteration exponent.

**Narration:** Under the paper’s assumptions, this gives a penalty-independent smoothness order and improves the outer iteration rate for the compared methods. The stationarity metric is the squared generalized-gradient criterion.

## 1:35–2:00

**On screen:** Add the cost of the inner solves to an outer-loop diagram.

**Narration:** The fixed, general coupled, and affine constraint regimes use different lower-level solvers. Combining their inner work with the improved outer rate gives the full complexity of each method.

## Recording notes

- Keep toy diagrams visibly labeled as illustrative.
- Show paper figure/table identifiers when discussing measured results.
- End with the project URL and a link to the primary paper.
- Record narration, then add figures and captions.
