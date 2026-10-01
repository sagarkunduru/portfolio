# Lab 06 — Cloud Security Guardrails

## Security model
Security is applied throughout the delivery path rather than added after deployment.

| Layer | Example control |
|---|---|
| Identity | Least-privilege IAM / RBAC |
| Network | Private subnets, security groups, controlled ingress/egress |
| Secrets | Secret stores; never commit credentials |
| Data | Encryption at rest/in transit |
| Pipeline | Protected secrets, review and validation |
| Kubernetes | RBAC, namespace boundaries, controlled configuration |
| Governance | Policy, tagging, logging and auditable changes |

## Review checklist
- Who can assume this identity?
- What exact actions are allowed?
- Is public exposure required?
- Where is the secret stored and rotated?
- Is sensitive data encrypted?
- Are configuration changes auditable?
- Can the team detect policy drift?
