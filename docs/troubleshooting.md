# Troubleshooting Decision Tree

```text
User impact?
  │
  ├─ Yes → stabilize service / reduce blast radius
  │
  └─ No  → preserve evidence and investigate safely
             │
             ├─ Release changed? → compare / rollback criteria
             ├─ Pod unhealthy?   → events / logs / probes / resources
             ├─ Traffic issue?   → DNS / ingress / service / network
             ├─ Capacity issue?  → CPU / memory / HPA / nodes
             └─ IaC issue?       → plan / state / drift / backend
```

## Evidence before action
Capture timestamps, versions, events, logs and relevant metrics before making a recovery change where practical.

## Validate after action
A command completing successfully is not proof of recovery. Validate the user-facing service and its health signals.
