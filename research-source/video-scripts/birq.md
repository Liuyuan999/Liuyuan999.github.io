# BiRQ — video narration and storyboard

Narration and storyboard. Approximately 2 minutes.

Paper: https://arxiv.org/abs/2509.15430

## 0:00–0:20

**On screen:** Show an unlabeled recording and a masked audio segment.

**Narration:** Self-supervised speech learning uses audio without a transcript for every recording. But the learner still needs a target. The way we create that target matters.

## 0:20–0:45

**On screen:** Compare raw-input quantization with intermediate-representation quantization.

**Narration:** BiRQ creates enhanced labels from intermediate representations inside the speech model. Random-projection quantization turns those evolving features into training targets.

## 0:45–1:10

**On screen:** Show anchor and enhanced target branches meeting at the learner.

**Narration:** Raw-input labels provide an anchor alongside enhanced labels. The anchor helps stabilize learning when the model’s own representations are changing.

## 1:10–1:35

**On screen:** Display bilevel roles and differentiable Gumbel-softmax selection.

**Narration:** BiRQ formulates this interaction as bilevel learning and trains end-to-end with differentiable selection. The method section specifies the losses and updates.

## 1:35–2:00

**On screen:** Show the LibriSpeech WER bars, labeled Table 2, and the AMI table reference.

**Narration:** With a 155-million-parameter Conformer pretrained on 960 hours of LibriSpeech and fine-tuned on 100 labeled hours, test-other word error rate is 12.6 percent for BiRQ and 19.6 percent for BEST-RQ. The result shows how learned representations can improve the model’s own targets.

## Recording notes

- Keep toy diagrams visibly labeled as illustrative.
- Show paper figure/table identifiers when discussing measured results.
- End with the project URL and a link to the primary paper.
- Record narration, then add figures and captions.
