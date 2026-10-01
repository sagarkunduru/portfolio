# Alert Design Examples

## High error rate
**Signal:** sustained application error ratio above an agreed service threshold.  
**Responder needs:** affected service, environment, start time, dashboard and runbook.  
**Avoid:** alerting on isolated errors without user impact.

## Kubernetes saturation
**Signal:** sustained CPU/memory pressure plus workload impact.  
**Correlate:** HPA state, node capacity, throttling, latency and recent deployments.

## Deployment health
After a release, compare readiness, error rate and latency with the pre-release baseline. A failed readiness condition should block promotion.

## Principle
Page on symptoms requiring action; use dashboards/logs for diagnosis.
