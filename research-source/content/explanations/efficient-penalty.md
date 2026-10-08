# Reduced curvature and value-function removal under constraints

A reduced penalty formulation admits outer step sizes independent of the penalty. Flatness then controls the bias of removing one lower-level response computation, with distinct algorithms for fixed and coupled constraints.

## The curvature of an alternating update

The lower variable is optimized before the outer step. The relevant objective is therefore a difference between nearby lower-level value functions. Its curvature can stay bounded even as the joint penalty objective becomes steeper.

## The cost of the value-function correction

The full outer gradient combines two response estimates. Dropping the original-response correction saves a computation, but introduces a bias that need not vanish as the penalty grows.

## Flatness and moving constraints

Upper-level flatness bounds this omission bias. Coupled constraints require a separate analysis because multipliers encode the effect of moving the lower-level feasible boundary.

## Source

[Efficient Penalty-Based Bilevel Methods: Improved Analysis, Novel Updates, and Flatness Condition](https://arxiv.org/abs/2511.16796)
