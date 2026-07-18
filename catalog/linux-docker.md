---
id: linux-docker
title: Docker Engine on Linux
entry_points: linux
execution_mode: automated
provisioning_adapter: environment/SetupLinux.sh
status: current
supported: Ubuntu and Pop!_OS using the Docker apt repository
verified_on: 2026-07-17
source_docs: linux/Docker-Setup.md
---

Configure Docker's apt repository and install Docker Engine, Buildx, Compose, and containerd.

## Verification

Run `docker --version` after completing the plan. Group membership and daemon access remain a manual follow-up if required.
