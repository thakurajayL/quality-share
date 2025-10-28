---
title: In Search of an Understandable Consensus Algorithm (Extended Version)
published_date: 2025-10-28T16:34:46.349757
link: https://raft.github.io/raft.pdf
summary: Raft is a consensus algorithm developed as an alternative to Paxos, focusing on simplicity and understandability while providing equivalent results and efficiency. It simplifies the consensus problem into leader election, log replication, and safety, ensuring safety and consistency in distributed systems. Raft handles cluster membership changes efficiently and uses a strong leadership approach to simplify the algorithm. It has been shown to be easier to learn and implement compared to Paxos, with open-source implementations used by several companies. The algorithm ensures log entries are safely replicated and committed, handles leader election, and supports safe configuration changes. Raft's approach prioritizes understandability, correctness, and performance, making it a practical foundation for system building.
authors: ["Diego Ongaro", "John Ousterhout"]
tags:
- consensus algorithm
- Raft
- Paxos
- leader election
- log replication
- RESEARCH_PAPER
content_type: RESEARCH_PAPER
---

