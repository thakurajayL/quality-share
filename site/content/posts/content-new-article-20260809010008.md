---
title: GEM Training: How Meta Doubled the Efficiency of Its LLM-Scale Ads Foundation Model
published_date: 2026-08-03T18:00:17+00:00
link: https://engineering.fb.com/2026/08/03/ml-applications/training-gem-at-llm-scale-meta-ads-recommendation-foundation-model/
summary: Meta's Generative Ads Recommendation Model (GEM) has been optimized for training efficiency on thousands of GPUs, doubling end-to-end training efficiency and scaling training FLOPs 4x in 12 months. The challenges of training GEM were addressed through customized recommendation kernels and ultra-low-precision training. The text discusses optimizations in parallelization, kernel specialization, and low-precision training for deep learning models, focusing on attention mechanisms. Strategies for handling quantization overhead, numerical stability, and scaling efficiency in large-scale distributed training were also highlighted. The team used Compiler-based Automatic Activation Checkpointing and Activation Quantization techniques to optimize memory usage and efficiency, leading to a 2x efficiency gain. Co-design across software, hardware, and networking layers was emphasized for further advancements in compute and scaling efficiency.
tags:
- recommendation systems
- LLM
- training efficiency
- FLOPs
- GPUs
- parallelism
- networking
- memory
- AI infrastructure
- scaling efficiency
- compute efficiency
- kernel library
- attention mechanisms
- precision
- numerical sensitivity
- scaling
- distributed training
- communication overhead
- load balancing
- architecture
- sequences
- data characteristics
- user engagement
- model parameters
- attention mechanisms
- FlashAttention
- GDPA
- BlockAttention
- ultra-low precision training
- Triton Low-Level Extensions
- TFLOPS
- Tensor Core utilization
- sliding-window attention
- block-aligned attention
- RoPE
- low-precision training
- MXFP8
- FP16
- FP8
- FP4
- numerical stability
- quantization overhead.
content_type: ContentType.BLOG_POST
---

