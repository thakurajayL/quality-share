---
title: In-House LLM Serving at Netflix
published_date: 2026-07-17T21:32:39+00:00
link: https://netflixtechblog.com/in-house-llm-serving-at-netflix-a5a8e799ea2c?source=rss----2615bd06b42e---4
summary: Netflix has developed an in-house system for serving Large Language Models (LLMs) within their production environment, including a JVM-based serving system, a shared inference backend, and a Java control plane. The platform uses vLLM as the inference engine, integrates with Triton, and offers an OpenAI-compatible API. Deployment strategies include Red-Black and Versioned approaches, with operational details such as model caching and boot sequence. Challenges in scaling and transitioning versions are discussed, with future investments in prompt compression and lower-precision models. The system aims to provide low latency, customization, and integration with existing infrastructure for ML practitioners.
tags:
- LLM
- Netflix
- AI Platform
- Model Runtime
- Inference
- engine selection
- model packaging
- API surface design
- deployment strategy
- output constraints enforcement
- JVM-based serving system
- real-time
- cached batch paths
- gRPC
- HTTP
- GPUs
- Model Scoring Service
- Triton Inference Server
- Java control plane
- deployment
- versioning
- health checking
- autoscaling
- multi-region rollout
- vLLM
- TensorRT-LLM
- XGBoost
- TensorFlow
- PyTorch
- Triton
- packaging
- Python backend
- JSON config
- OpenAI-compatible API
- HTTP Frontend
- gRPC
- Red-Black deploys
- Versioned
- operational
- boot sequence
- metrics
- Prometheus
- constrained decoding
- token generation
- scalability
- V0
- V1
- batch-level design
- performance
- asynchronous scheduling
- GPU kernels
- lower-precision model variants
- contributions.
content_type: ContentType.BLOG_POST
---

