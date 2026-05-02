---
title: "Attention Is All You Need"
description: "Original transformer paper by Vaswani et al., foundational for modern LLMs"
created: 2026-01-01
tags:
  - type/resource
  - ai
  - "#status/done"
source: "https://arxiv.org/abs/1706.03762"
---

## Summary

The 2017 paper that introduced the Transformer architecture, replacing recurrence and convolutions with pure self-attention. It became the foundation for GPT, BERT, and virtually every modern large language model. Essential reading for understanding why LLMs work the way they do.

## Key Takeaways

- Self-attention allows each token to attend to every other token in the sequence, enabling better long-range dependency capture than RNNs
- The encoder-decoder architecture with multi-head attention became the dominant paradigm for sequence-to-sequence tasks
- Positional encodings replace sequential ordering — the model has no inherent notion of position without them

## Related

[[retrieval-augmented-generation]] · [[embeddings]]
