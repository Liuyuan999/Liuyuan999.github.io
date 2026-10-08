# SURF — video narration and storyboard

Narration and storyboard. Approximately 2 minutes.

Paper: https://arxiv.org/abs/2605.20619

## 0:00–0:20

**On screen:** Show eight evenly spaced marks on a weight axis, then eight unevenly spaced solutions on a curve.

**Narration:** If we want an even spread of trade-offs, should we choose optimization weights evenly? That sounds reasonable. But weights are inputs, and solutions are outputs. The map between them can distort spacing.

## 0:20–0:45

**On screen:** Animate a point moving slowly and then quickly along a Pareto front as the weight changes.

**Narration:** As a scalarization weight varies, its solutions trace a path through objective space. The speed along that path is generally uneven. A small change in weight can mean a tiny change in one region and a large change elsewhere.

## 0:45–1:10

**On screen:** Build cumulative distance, normalize it, and connect equal quantiles to unequal weights.

**Narration:** SURF changes coordinates. We measure cumulative arc length, normalize it into a CDF, and invert the map at evenly spaced distance targets. The resulting weights are chosen to spread solutions along the front.

## 1:10–1:35

**On screen:** Alternate boxes labeled solve, reconstruct map, and sample next weights.

**Narration:** For structured problems, the map can be derived analytically. For general problems, SURF alternates optimization and map reconstruction. Under the stated regularity conditions, reconstruction error contracts toward a finite-sampling floor.

## 1:35–2:00

**On screen:** Show the paper’s Table 1 and Table 2 headings, then the project link.

**Narration:** The experiments cover bandits, multi-objective reinforcement learning, and LLM alignment. Read coverage together with solution quality. The takeaway is that preferences need to be translated through geometry when our goal is an evenly spaced set of trade-offs.

## Recording notes

- Keep toy diagrams visibly labeled as illustrative.
- Show paper figure/table identifiers when discussing measured results.
- End with the project URL and a link to the primary paper.
- Record narration, then add figures and captions.
