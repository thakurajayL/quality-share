---
title: Modernizing the Meta Ads Service With an Open-Source Kernel Scheduler
published_date: 2026-07-13T16:00:50+00:00
link: https://engineering.fb.com/2026/07/13/ml-applications/modernizing-the-meta-ads-service-with-an-open-source-kernel-scheduler/
summary: Meta implemented a customized scheduling policy using sched_ext to address latency issues caused by a Linux kernel upgrade in their ads serving fleet. This resulted in a 28% reduction in latency, 3.28 MW power savings, and a 1.1% increase in ads ranked. The approach allows for workload-specific optimization, leading to improved performance and business value. sched_ext is an open-source, BPF-based scheduler framework deployed at Meta, offering benefits such as independent deployment, reduced overheads, and shared industry asset. Future plans include further improvements in ads performance by giving more control over scheduler behavior.
tags:
- Meta
- ads performance
- latency
- scheduling
- Linux kernel
- sched_ext
- BPF
- optimization
- workload-specific
- ads delivery
- ROI
- fleet
- requests
- p99 latency
- power saving
- ads ranking
- scheduler framework
- CPU
- cache
- DRAM
- user-space
- performance optimization
- service latency
- timeout errors
- strategic asset
- deployment
- industry asset
- future plans.
content_type: ContentType.BLOG_POST
---

