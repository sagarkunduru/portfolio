# Operations Runbook Index

A portfolio that only shows the happy path is incomplete. These runbooks document how I reason about common platform failures.

| Runbook | First question |
|---|---|
| [EKS CrashLoopBackOff](eks-crashloopbackoff.md) | Why is the container repeatedly exiting? |
| [Failed Deployment](failed-deployment.md) | Did the release cause service degradation? |
| [High CPU](high-cpu.md) | Is load, code, sizing or a dependency driving saturation? |
| [Terraform State Recovery](terraform-state-recovery.md) | Is state inconsistent, unavailable or simply locked? |

**Incident pattern:** stabilize → establish timeline → inspect signals → reduce blast radius → recover → validate → document.
