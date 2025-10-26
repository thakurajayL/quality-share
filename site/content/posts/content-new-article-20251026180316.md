---
title: Curated Article from https://aws.amazon.com/message/101925/
date: 2025-10-26T18:03:15.642209
link: https://aws.amazon.com/message/101925/
summary: The Amazon DynamoDB service disruption in the Northern Virginia (US-EAST-1) Region on October 19 and 20, 2025, had three distinct periods of impact on customer applications. The disruption was triggered by a latent defect in the automated DNS management system of DynamoDB, causing increased API error rates. The issue was resolved by restoring DNS information. Additionally, the disruption affected Amazon EC2, resulting in increased API error rates, latencies, and instance launch failures. The issue was caused by failures in the DropletWorkflow Manager and Network Manager subsystems, which were resolved by re-establishing leases with droplets and propagating network configurations. The disruption also impacted the Network Load Balancer service, leading to increased connection errors due to health check failures. Other AWS services like Lambda functions, Amazon Elastic Container Service, and AWS Security Token Service were also affected. AWS is implementing changes to prevent similar events in the future and improve service availability.
tags:
- DynamoDB
- DNS
- Automation
- Race Condition
- Endpoint
- DNS Management
- AWS Services
- API Errors
- Latency
- EC2
- Instance Launches
- Network Manager
- DropletWorkflow Manager
- Network Connectivity
- NLB
- Health Check
- Load Balancer
- Connection Errors
- Availability Zones
- Recovery
- Network State
- Network Propagation
- Network Configuration
- Backlog
- Throttling
- Lambda Functions
- SQS
- Kinesis
- ECS
- EKS
- Fargate
- Redshift
- IAM
- Support Center
- Operational Event
- Recovery Plan
- Incident Analysis.
content_type: ROOT_CAUSE_ANALYSIS
---

