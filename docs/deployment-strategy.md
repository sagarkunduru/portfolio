# Deployment Strategy

## Before release
Define the artifact version, change scope, expected health signals and rollback trigger.

## During release
Watch readiness, errors, latency and saturation. Avoid changing multiple unrelated variables during the same production event.

## After release
Validate application and platform health, record the deployed version and close the release only after the observation window.

## Rollback
Rollback is a designed capability, not an improvised incident action. The previous known-good artifact and configuration must remain identifiable.
