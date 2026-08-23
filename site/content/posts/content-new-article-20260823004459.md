---
title: A Tale of Two Flink Autoscalers
published_date: 2026-08-21T16:01:01+00:00
link: https://netflixtechblog.com/a-tale-of-two-flink-autoscalers-e9f6a1b1492b?source=rss----2615bd06b42e---4
summary: Netflix uses two Flink autoscalers, one in-house and one from the Apache Flink community. The in-house autoscaler had limitations, leading Netflix to adopt the open-source autoscaler, which optimizes resource allocation by estimating each operator's processing rate. Modifications were made to the open-source autoscaler to work at Netflix's scale, resulting in cost savings and efficiency improvements. Challenges of scaling down systems too eagerly are discussed, emphasizing stability over efficiency. The focus is on improving state restoration performance in Flink 2 to reduce bottlenecks in scaling stateful jobs. Lessons learned include the importance of metric choice, setting sensible defaults, and extending existing solutions. Contributions from various teams and individuals are acknowledged.
tags:
- Flink
- Autoscaler
- Netflix
- Apache Flink
- stream processing
- scaling
- metrics
- cost
- infrastructure
- open-source
- jobs
- provisioning
- workload
- stateful
- DAGs
- Kubernetes
- Spring Boot
- Temporal
- workflow
- parallelism
- bottleneck
- metrics collection
- forward chaining
- sink limits
- safety checks
- efficiency
- stability
- state recovery
- Flink 2
- operational
- metric choice
- algorithm
- defaults
- tuning
- adoption
- extension.
content_type: ContentType.BLOG_POST
---

