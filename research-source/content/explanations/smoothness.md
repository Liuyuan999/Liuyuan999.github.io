# Reduced smoothness in constrained bilevel optimization

A large penalty need not make the outer objective harder to optimize. This paper proves a penalty-independent smoothness bound for the reduced formulation of constrained bilevel optimization.

## The smoothness bound that controls the step

The joint penalty objective Hγ(x, y) measures changes in both variables. Its O(γ) smoothness bound leads to a penalty-dependent step size. ALT-PBGD and BLOCC instead update the upper variable using the reduced objective Fγ(x), after estimating the lower responses.

## Cancellation between constrained value functions

The reduced objective is γ times the difference between two related lower-level minimum values. Strong convexity controls the change in the lower response, and Hessian regularity controls the resulting change in directional curvature. Analyzing the difference preserves the cancellation of the penalty factor.

## From smoothness to complexity

The O(1) reduced bound permits a step-size order independent of γ. This gives O(ε⁻¹) outer iterations for the squared projected-gradient criterion. The lower-level solver determines the additional cost within each iteration.

## Source

[Improved Analysis of Penalty-Based Methods for Bilevel Optimization with Coupled Constraints](https://eurasip.org/Proceedings/Eusipco/Eusipco2025/pdfs/0001183.pdf)
