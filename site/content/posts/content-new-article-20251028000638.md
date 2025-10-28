---
title: Curated Article from https://aws.amazon.com/message/101925/
published_date: 2025-10-28T00:06:38.273237
link: https://aws.amazon.com/message/101925/
summary: The Amazon DynamoDB service disruption in the Northern Virginia (US-EAST-1) Region on October 19 and 20, 2025, had three distinct periods of impact on customer applications. The disruption was triggered by a latent defect in the automated DNS management system of DynamoDB, causing increased API error rates. The issue was resolved by restoring DNS information. Additionally, the disruption affected Amazon EC2 instance launches, which experienced increased errors and latencies due to failures in the DropletWorkflow Manager system. Recovery involved re-establishing leases with droplets and propagating network configurations. The Network Load Balancer service also experienced connection errors due to health check failures, which were resolved by disabling automatic health check failovers. Other AWS services like Lambda functions, Amazon Elastic Container Service, and AWS Security Token Service were also impacted but recovered by addressing specific issues. AWS is implementing changes to prevent similar events in the future and improve service availability.
tags:
- DynamoDB
- DNS
- Automation
- Race Condition
- Endpoint
- Load Balancer
- EC2
- Instance Launch
- Network Manager
- DropletWorkflow Manager
- Lease
- Recovery
- Network Connectivity
- NLB
- Health Check
- API Errors
- Latency
- Lambda
- SQS
- Kinesis
- ECS
- EKS
- Fargate
- Connect
- STS
- IAM
- Redshift
- Support Center
- Incident Response
- AWS Services
content_type: ROOT_CAUSE_ANALYSIS
---

