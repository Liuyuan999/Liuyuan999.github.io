# Value-function removal under upper-level flatness

PBGD-Free removes the original lower-level response from a penalty-gradient update. Upper-level flatness controls the resulting bias and permits one first-order update per level.

## Two responses in the penalty gradient

The original response minimizes g. The perturbed response minimizes the lower-variable part of f + γg. The reduced penalty gradient combines the upper partial gradient with the γ-scaled difference between lower-loss gradients at these responses.

## One response in PBGD-Free

PBGD-Free tracks the perturbed response and uses the upper partial gradient for x. This removes the original-response estimate. Proposition 2 shows that the resulting bias can persist under ordinary Lipschitz regularity.

## Upper-level flatness

Definition 1 bounds the difference in upper loss between an original lower minimizer and any lower variable. The distance exponent and residual determine how accurately the simplified direction represents the reduced penalty gradient.

## Source

[Beyond Value Functions: Single-Loop Bilevel Optimization under Flatness Conditions](https://arxiv.org/abs/2507.20400)
