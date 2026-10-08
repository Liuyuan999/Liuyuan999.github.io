# When an outer decision changes what the inner problem can do

In a coupled bilevel problem, the outer decision changes the inner feasible set. BLOCC uses primal-dual information to keep that moving boundary in the optimization.

## The decision

A network operator chooses infrastructure; passengers respond within the resulting network. In a constrained SVM, outer hyperparameters set violation limits and the inner model learns within those limits. Both are bilevel problems with a feasible set that changes with x.

## The bottleneck

The lower-level value changes through the objective and through active constraints. An objective-only gradient can point in the wrong direction. A joint projection onto the full coupled feasible set can also become costly at large dimensions.

## The idea

Use primal-dual responses to estimate the moving-boundary contribution. BLOCC combines them with a penalty reformulation and first-order updates, avoiding the full joint projection used by a direct constrained formulation.

## Source

[A Primal-Dual-Assisted Penalty Approach to Bilevel Optimization with Coupled Constraints](https://arxiv.org/abs/2406.10148)
