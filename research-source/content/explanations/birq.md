# Target refinement within a shared speech encoder

BiRQ refines speech pretraining targets using intermediate features of the acoustic encoder, with a fixed raw-input labeling task as an anchor.

## From fixed labels to learned representations

BEST-RQ turns unmasked audio features into pseudo-labels using a fixed random projection and codebook, then trains an encoder to predict those labels from masked audio. The targets remain unchanged as the encoder learns. HuBERT-style relabeling uses learned features to refine targets through separate labeling stages.

## A target generator inside the prediction model

BiRQ reuses the first part of the acoustic encoder to generate targets from unmasked speech. Normalized intermediate features pass through a fixed random projection and a Gumbel-softmax quantizer. The resulting enhanced targets depend differentiably on the same encoder parameters used for masked prediction.

## An anchoring task for joint learning

The raw-input targets are retained as a reference task independent of the encoder parameters. BiRQ minimizes the enhanced-target loss while requiring the anchoring loss to stay near its minimum. The penalty implementation brings both tasks into one training loop, with gradients through target construction as well as prediction.

## Source

[BiRQ: Bi-Level Self-Labeling Random Quantization for Self-Supervised Speech Recognition](https://arxiv.org/abs/2509.15430)
