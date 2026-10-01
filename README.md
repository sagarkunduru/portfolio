# Sagar Kundur — Production Cloud Engineering Lab

**Senior DevOps & Cloud Engineer | AWS • Azure • Kubernetes • Terraform • CI/CD • Platform Reliability**

This repository is not a collection of disconnected tutorials. It is a **production-minded cloud engineering portfolio** showing how I approach infrastructure, delivery, operations, security, and troubleshooting as one platform.

> **Design principle:** build it repeatably, deploy it safely, observe it continuously, and document how to recover it.

## Platform Story

```text
Developer → GitHub → CI/CD → Container Registry → Kubernetes
                         │                    │
                         │                    ├─ EKS / AKS
                         │                    ├─ Helm
                         │                    └─ Safe rollout patterns
                         │
                         └─ Terraform → Network / IAM / Compute / Platform

Runtime → CloudWatch / Prometheus / Grafana / Splunk-style operations
Security → IAM / RBAC / Secrets / policy controls
Operations → Runbooks / incident response / rollback / recovery
Automation → Python / Bash / PowerShell
```

## Engineering Tracks

| Track | What it demonstrates |
|---|---|
| [AWS Platform](01-terraform-aws-platform/) | Reusable Terraform, VPC design, security boundaries, scalable AWS foundations |
| [EKS Platform](02-eks-production-platform/) | Kubernetes workload patterns, Helm, health checks, scaling and operations |
| [CI/CD](03-cicd-github-actions/) | Build, test, scan, package and deployment workflow design |
| [Safe Releases](04-kubernetes-deployment-strategies/) | Rolling, blue/green and canary deployment thinking with rollback |
| [Observability](05-observability-stack/) | Metrics, logs, dashboards, alerting and MTTR-focused operations |
| [Cloud Security](06-cloud-security/) | IAM, RBAC, secrets, encryption and governance patterns |
| [Automation](07-python-automation/) | Practical Python/Bash automation for platform operations |
| [Azure / AKS](azure/aks-terraform-platform/) | Azure IaC, AKS, identity, networking and governance patterns |
| [Runbooks](docs/runbooks/) | Production troubleshooting and recovery playbooks |

## What makes this portfolio different

Each lab is documented like production engineering work: **problem → design → implementation → validation → failure modes → recovery**. The goal is not to claim a live production system, but to demonstrate the engineering decisions and operational habits behind one.

## Core Toolkit

**Cloud:** AWS, Microsoft Azure  
**Containers:** Kubernetes, Amazon EKS, Azure AKS, Docker, Helm  
**Infrastructure as Code:** Terraform, CloudFormation, ARM Templates  
**CI/CD:** Jenkins, GitHub Actions, Azure DevOps, GitLab CI/CD  
**Automation:** Python, Bash/Shell, PowerShell  
**Observability:** CloudWatch, Prometheus, Grafana, Splunk, ELK  
**Security:** IAM, RBAC, Key Vault, encryption, Azure Policy, security groups  
**Build/Quality:** Maven, SonarQube, Artifactory/Nexus

## Experience Lens

The labs are modeled from technology patterns I have worked with across enterprise, financial, telecom, public-sector and regulated environments. All examples are sanitized and contain **no employer source code, credentials, customer data, proprietary architecture, or confidential configuration**.

## Certifications

- AWS Certified Solutions Architect — Associate
- Microsoft Certified: Azure Solutions Architect Expert (AZ-305)

## How to explore

Start with [Architecture](architecture/platform-architecture.md), then follow the numbered engineering tracks. For an operations-focused view, go directly to the [runbook index](docs/runbooks/README.md).

---
**Sagar Kundur** · Senior DevOps & Cloud Engineer
