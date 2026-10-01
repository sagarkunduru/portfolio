# Runbook — EKS Pod CrashLoopBackOff

## Goal
Restore service safely while preserving evidence needed to find the cause.

## Triage
1. Confirm affected namespace, deployment and start time.
2. Inspect pod status, events and previous container logs.
3. Compare the failing image/configuration with the last healthy release.
4. Check probes, secrets/config, dependencies and resource limits.
5. Determine whether the issue is isolated or service-wide.

## Useful commands
```bash
kubectl get pods -n <namespace>
kubectl describe pod <pod> -n <namespace>
kubectl logs <pod> -n <namespace> --previous
kubectl get events -n <namespace> --sort-by=.lastTimestamp
kubectl rollout history deployment/<deployment> -n <namespace>
```

## Recovery
If a recent release is the confirmed trigger and rollback is safe, return to the last known-good release, then validate readiness, error rate and service traffic.

## Do not
Do not repeatedly restart workloads without understanding the failure; that can destroy useful evidence and hide the actual cause.
