# Lab 04 — Kubernetes Safe Release Strategies

## Rolling
Replace replicas gradually. Good default when old/new versions can coexist and fast automated rollback is available.

## Blue/Green
Maintain old and new environments simultaneously and switch traffic after validation. Useful when a clear cutover and rapid switch-back are valuable.

## Canary
Expose a limited portion of traffic to the new version, observe health signals, then increase exposure.

## Release decision matrix
| Question | Why it matters |
|---|---|
| Can old and new versions coexist? | Determines rolling compatibility |
| Can traffic be split safely? | Enables canary validation |
| Is duplicate capacity acceptable? | Affects blue/green cost |
| What proves the release is healthy? | Defines promotion gates |
| What is the rollback trigger? | Prevents subjective incident decisions |

A deployment strategy is incomplete without measurable health criteria and a tested rollback path.
