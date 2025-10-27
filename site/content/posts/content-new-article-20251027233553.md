---
title: Curated Article from https://aws.amazon.com/message/101925/
date: 2025-10-27T23:35:52.967393
link: https://aws.amazon.com/message/101925/
summary: The Amazon DynamoDB service disruption in the Northern Virginia (US-EAST-1) Region on October 19 and 20, 2025, had three distinct periods of impact on customer applications. The disruption was triggered by a latent defect in the automated DNS management system of DynamoDB, causing increased API error rates. The issue also affected Amazon EC2 instance launches, leading to increased errors and latencies. Additionally, the Network Load Balancer (NLB) experienced connection errors due to health check failures. Various AWS services were impacted, including Lambda functions, Amazon Elastic Container Service (ECS), Elastic Kubernetes Service (EKS), Fargate, Amazon Connect, AWS Security Token Service (STS), Redshift, and the AWS Support Console and API. Measures are being taken to prevent similar events in the future, such as disabling the DynamoDB DNS Planner and Enactor automation and adding protections to prevent incorrect DNS plans.
tags:
- Amazon DynamoDB
- DNS management
- automation
- race condition
- endpoint resolution
- DNS Planner
- DNS Enactor
- Availability Zones
- load balancers
- Route53
- EC2 instance launches
- DNS records
- API errors
- latency
- Network Load Balancer
- health check failures
- NLB nodes
- backend targets
- network state propagation
- droplets
- DWFM
- Network Manager
- leases
- EC2 fleet
- request throttling
- network configuration
- AWS services
- Lambda functions
- SQS
- Kinesis
- ECS
- EKS
- Fargate
- Amazon Connect
- STS
- IAM user
- Redshift clusters
- support cases
- DynamoDB DNS Planner
- DynamoDB DNS Enactor
- NLB velocity control mechanism
- EC2 test suite
- DWFM recovery workflow
- EC2 data propagation systems
- time to recovery.
content_type: ROOT_CAUSE_ANALYSIS
---

