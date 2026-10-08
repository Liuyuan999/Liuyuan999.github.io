# Why uniform weights do not give uniform trade-offs

A weight chooses a compromise. SURF asks how far that choice moves us along the Pareto front—and uses the answer to spread solutions more evenly.

## The decision

A summarization system can reward both a useful summary and a faithful one. A weighted loss selects one compromise. A well-spaced collection of models gives users a range of quality–faithfulness balances to choose from.

## The bottleneck

An equal change in the scalarization weight can move the solution a long distance in one region and barely move it in another. Uniform preferences can therefore spend several training slots on similar models while leaving other trade-offs sparsely represented.

## The idea

Measure distance in objective space. SURF estimates how much of the front has been traversed at each weight, inverts that cumulative-distance map, and places training slots at equal distance targets. The scalarized inner solver can remain PPO, Adam, or another suitable solver.

## Source

[SURF: Steering the Scalarization Weight to Uniformly Traverse the Pareto Front](https://arxiv.org/abs/2605.20619)
