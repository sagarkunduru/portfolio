# Lab 01 — Terraform AWS Platform Foundation

## Problem
Teams need a repeatable AWS landing foundation without manually creating networking and security resources.

## Design
The lab models a multi-AZ VPC with public/private tiers, controlled routing, security groups and reusable Terraform modules.

## Planned implementation
```text
VPC
├── Public subnets (AZ-A / AZ-B)
│   └── Load-balancer tier
├── Private application subnets
│   └── EKS worker/application tier
└── Private data subnets
    └── Database tier
```

## Production considerations
- Remote Terraform state and locking
- Environment-specific variables
- NAT and egress strategy
- Least-privilege IAM
- Encryption and tagging
- Module versioning
- Plan review before apply
- No credentials committed to Git

## Validation
A completed implementation should validate formatting, Terraform configuration, plans, network paths and expected resource tags.

## Failure thinking
Before changing routes, subnets or state, capture the current plan/state and understand blast radius. Recovery should favor version-controlled configuration over console drift.
