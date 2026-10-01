# Runbook — Failed Production Deployment

## Trigger
Deployment does not become healthy or service health degrades immediately after release.

## Response
1. Establish release timestamp and changed version.
2. Check rollout status and readiness.
3. Compare error/latency signals before and after release.
4. Inspect deployment events and application logs.
5. Stop further promotion.
6. Roll back when the release is the likely cause and rollback is safe.
7. Validate service health after recovery.
8. Preserve logs and timeline for follow-up.

A successful rollback ends the outage; it does not end the investigation.
