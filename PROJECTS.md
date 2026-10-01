# Portfolio Project Map

This portfolio is designed as one connected engineering story rather than a list of unrelated tutorials.

| Stage | Project | Evidence |
|---|---|---|
| Foundation | AWS Terraform Platform | VPC/subnets, variables, outputs, IaC validation |
| Runtime | EKS Platform | Deployment, Service, HPA, probes and resources |
| Delivery | CI/CD | Automated Terraform/Kubernetes/Python validation |
| Release | Deployment Strategies | Rolling, blue/green, canary and rollback thinking |
| Operations | Observability | Signal model and alert design |
| Security | Guardrails | Least privilege, network, secrets, encryption and review checklist |
| Automation | Python | Read-only AWS inventory example |
| Multi-cloud | Azure/AKS | Azure platform design and regulated-environment mindset |
| Reliability | Runbooks | CrashLoopBackOff, failed deployment, high CPU and Terraform state recovery |

## Reviewer path
For a 5-minute review: README → architecture → Terraform → EKS → CI workflow → one runbook.

For a reliability-focused review: architecture → observability → runbooks → incident response.

For a security-focused review: architecture → cloud security → security checklist → IaC.
