---
title: Building a safe, effective sandbox to enable Codex on Windows
published_date: 2026-05-13T11:00:00+00:00
link: https://openai.com/index/building-codex-windows-sandbox
summary: The Codex engineering team developed a sandbox environment for Codex on Windows using synthetic SIDs and write-restricted tokens to limit file writes and network access. The setup involved creating custom users, firewall rules, and an elevated setup step to ensure a secure coding environment for autonomous coding agents. The final design balanced compatibility with security to allow agents to work independently while maintaining safety and usefulness.
tags:
- sandbox
- Codex
- Windows
- isolation
- security
- permissions
- operating system
- environment
- constraints
- implementation
- AppContainer
- Windows Sandbox
- Mandatory Integrity Control
- MIC
- integrity labeling
- SIDs
- security identifier
- process tokens
- write-restricted tokens
- network access
- ACLs
- synthetic SIDs
- Windows Firewall
- elevated sandbox
- CodexSandboxOffline
- CodexSandboxOnline
- firewall rules
- setup
- execution
- implementation drawbacks
- network suppression
- security implications
- Windows Data Protection API
- DPAPI.
content_type: ContentType.BLOG_POST
---

