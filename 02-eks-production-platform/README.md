# Lab 02 — Production-Minded Amazon EKS

## Problem
Running a container is easy; operating a Kubernetes workload safely requires health checks, scaling, rollout controls, observability and recovery.

## Platform concerns
- Namespace and workload organization
- Deployments and Services
- Readiness/liveness probes
- Requests and limits
- Horizontal Pod Autoscaling
- ConfigMaps and Secrets
- Helm packaging
- Ingress
- Rolling releases and rollback
- Metrics and logs

## Deployment lifecycle
```text
Commit → CI checks → Image → Registry → Helm release → EKS
                                             │
                                      readiness check
                                             │
                                  healthy ────┴──── unhealthy
                                     │                 │
                                   serve            rollback
```

## Operational questions
A production engineer should be able to answer: Is the pod scheduled? Is the container healthy? Is the service routing? Is DNS working? Are resource limits causing pressure? Did the latest release introduce the failure?

See [CrashLoopBackOff runbook](../docs/runbooks/eks-crashloopbackoff.md).
