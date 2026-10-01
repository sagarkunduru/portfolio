# Runbook — Terraform State / Lock Issue

## Safety first
Terraform state represents infrastructure ownership. Avoid forceful changes until the cause is understood.

## Triage
1. Confirm backend accessibility.
2. Determine whether a legitimate Terraform operation is still running.
3. Capture the error and current workspace/environment.
4. Verify state backup/versioning where configured.
5. Compare configuration, state and real infrastructure before recovery.

## Rule
Never remove a lock simply because it blocks a pipeline. Confirm it is stale first. Prefer backend recovery/version history and controlled Terraform operations over manual state editing.
