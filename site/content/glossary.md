---
title: "Glossary"
date: 2025-10-20T16:00:00-04:00
draft: false
---

This page will contain a glossary of common terms used in the project. More content will be added here soon.

## Choosing a Client-Server Communication Mode

### Polling

Polling is a technique where a client repeatedly sends requests to a server at regular intervals to check for new data. If there is no new data, the server sends an empty response. This is a simple but inefficient method, as it can generate a lot of unnecessary network traffic.

### Long Polling

Long polling is a more efficient version of polling. The client sends a request to the server, and the server holds the connection open until it has new data to send. Once the data is sent, the connection is closed, and the client immediately opens a new connection. This reduces the number of empty responses and is more efficient than traditional polling.

### WebSocket

WebSocket is a communication protocol that provides full-duplex communication channels over a single TCP connection. It allows for real-time, two-way communication between a client and a server. Unlike polling, where the client has to repeatedly ask for data, with WebSockets, the server can push data to the client as soon as it's available. This makes it very efficient for applications that require real-time data updates, such as chat applications and online games.