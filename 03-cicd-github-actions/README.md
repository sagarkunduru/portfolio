# Lab 03 — CI/CD Delivery Pipeline

## Objective
Model a controlled delivery path that produces a versioned artifact and promotes it only after validation.

## Pipeline
```text
Pull Request
   ↓
Lint / Unit Test / IaC Validation
   ↓
Security & Quality Checks
   ↓
Build Container
   ↓
Publish Versioned Image
   ↓
Deploy
   ↓
Health Validation
   ↓
Promote or Roll Back
```

## Controls
- Pull-request review
- Reproducible builds
- No plaintext secrets
- Artifact/image versioning
- Quality gates
- Deployment approvals where appropriate
- Post-deployment health validation
- Documented rollback

The emphasis is not a specific CI product; it is the release control model that can be implemented with GitHub Actions, Jenkins, Azure DevOps or GitLab CI/CD.
