# Lab 07 — Operations Automation

## Philosophy
Automate repetitive operational work, but keep automation observable, idempotent where practical, and safe to rerun.

## Portfolio automation ideas
- AWS resource inventory
- Tag compliance checks
- Stale-resource reporting
- Deployment health checks
- Log cleanup/retention helpers
- Kubernetes status reporting

## Safety pattern
```text
discover → validate → preview → execute → verify → report
```

Scripts in this portfolio should default to read-only/dry-run behavior for potentially destructive workflows and should never contain credentials.
