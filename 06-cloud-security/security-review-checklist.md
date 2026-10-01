# Platform Security Review Checklist

## Identity
- Workload and human identities are separated.
- Permissions follow least privilege.
- Privileged access is explicit and auditable.

## Network
- Public exposure has a documented reason.
- Application/data tiers are isolated where appropriate.
- Ingress and egress rules are narrowly scoped.

## Secrets and encryption
- Credentials are not stored in source.
- Secret access is identity-controlled.
- Encryption requirements are defined for data at rest and in transit.

## Delivery
- Changes are version controlled and reviewed.
- CI/CD secrets are protected.
- Deployment artifacts are identifiable and reproducible.

## Operations
- Security-relevant logs are retained centrally.
- Alerts have owners and response procedures.
- Recovery procedures do not bypass security controls without an explicit emergency process.
