# Separating exposure from the timing of sequential decisions

RetailAgent studies the timing of sequential LLM decisions on anonymized intraday equity paths. Its exposure-matched metric separates how often an agent holds a stock from whether it holds during favorable intervals.

## The evaluation question

A stock’s rise can give a long-only policy positive return even when its entries and exits are poorly timed. RetailAgent compares the saved schedule with constant exposure on the same stock-day to isolate interval selection.

## A recursive decision policy

The agent’s account state and self-authored notes depend on its earlier actions. RetailAgent records that state alongside the observation, binary decision, and subsequent return, so sequential conditioning can be studied at the trajectory level.

## Evidence from action sequences

Exposure-matched timing is negative across the evaluated standard configurations. Shuffling saved actions substantially attenuates it. The memory comparisons then examine persistence and timing among trajectories that contain both long and flat actions.

## Source

[RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents](https://arxiv.org/abs/2608.28399)
