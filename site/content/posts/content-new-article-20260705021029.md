---
title: Core dump epidemiology: fixing an 18-year-old bug
published_date: 2026-06-30T00:00:00+00:00
link: https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug
summary: OpenAI experienced crashes in their data infrastructure service Rockset due to an 18-year-old bug in GNU libunwind and silent hardware corruption on an Azure host. They used population-level analysis and core dumps to identify and fix the crashes, shifting to a broader epidemiological perspective. Two separate crash populations were identified, one caused by a bad physical host and the other by the libunwind bug. The bug was triggered by high exception and signal rates, leading to frequent crashes. The team traced the issue to a race condition in the libunwind code and made adjustments to fix it. Lessons learned from the investigation emphasize the importance of deep instrumentation and continual improvements in operational tooling for reliability in infrastructure systems.
tags:
- bug fixing
- epidemiology
- core dump
- data infrastructure
- C++
- memory safety
- crashes
- Rockset service
- ChatGPT
- debugging
- population analysis
- OpenAI
- scalability
- memory usage
- low-level control
- performance
- memory corruption
- race condition
- GNU libunwind
- hardware corruption
- software bug
- misaligned stack
- signal handler
- stack trace
- reliability
- quality
- debugging process
- hypothesis
- kernel
- CPU
- stack pointer
- crash analysis
- data set
- Rockset
- cloud-native data system
- real-time analytics
- sync connectors
- streaming updates
- memory accesses
- segfaults
- folly's fatal signal handler
- core dumps
- debugging approach
- epidemiologist
- population data
- Kubernetes nodes
- misaligned-stack crashes
- physical host
- bad hardware
- exception unwinding
- C++ exception
- libgcc
- GNU libunwind
- ucontext_t
- _Ux86_64_setcontext
- register state
- assembly routine
- stack frames
- vulnerability
- clobbered
content_type: ContentType.BLOG_POST
---

