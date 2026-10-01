# Runbook — Sustained High CPU

## Triage
Confirm duration, affected replicas/nodes, traffic level and whether the condition started after a deployment.

## Investigate
- Request/transaction volume
- Per-pod and node CPU
- Requests and limits
- HPA behavior
- Application errors and latency
- Recent releases/config changes
- Dependency latency/retries

## Recovery
Scale only when it safely addresses capacity pressure. If a release introduced abnormal CPU, evaluate rollback. Validate latency, errors and saturation after mitigation.
