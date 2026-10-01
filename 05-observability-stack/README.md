# Lab 05 — Observability & MTTR

## Objective
Design monitoring around questions operators need to answer during an incident.

## Signal model
**Metrics:** saturation, latency, error rate, throughput, Kubernetes resource health.  
**Logs:** application errors, platform events, deployment events and audit context.  
**Alerts:** actionable symptoms with ownership and a linked runbook.  
**Dashboards:** service health first; infrastructure detail second.

## Tool mapping
- CloudWatch — AWS metrics/logs/alarms
- Prometheus — Kubernetes/application metrics
- Grafana — visualization
- Splunk / ELK — centralized log analysis

## Alert quality rule
An alert should tell the responder **what is unhealthy, how severe it is, where to investigate, and what runbook to open**. More alerts do not automatically mean better observability.
