---
title: How OpenAI delivers low-latency voice AI at scale
published_date: 2026-05-04T00:00:00+00:00
link: https://openai.com/index/delivering-low-latency-voice-ai-at-scale
summary: OpenAI has rearchitected their WebRTC stack to deliver low-latency voice AI at scale. They use a transceiver model for efficient signaling and media handling, with a lightweight UDP relay for packet routing. The relay service routes packets based on metadata to the appropriate transceiver, maintaining a normal WebRTC flow for the client. Key design choices include no protocol termination, ephemeral state, and horizontal scalability. The architecture allows for running WebRTC media in Kubernetes without exposing thousands of UDP ports, resulting in deterministic routing and improved infrastructure scalability.
tags:
- voice AI
- low-latency
- scale
- OpenAI
- WebRTC
- real-time
- AI interactions
- infrastructure
- media termination
- ICE
- DTLS
- global routing
- peer-to-peer calling
- codec negotiation
- RTCP
- echo cancellation
- jitter buffering
- transceiver model
- SFU
- signaling
- media termination
- Kubernetes
- UDP port ranges
- TURN relay
- ICE username fragment
- STUN
- relay service
- Global Relay
- Cloudflare
- geo-steered signaling
- Go
- protocol termination
- ephemeral state
- horizontal scalability
content_type: ContentType.BLOG_POST
---

