---
id: linux-homebrew
title: Homebrew on Linux
entry_points: linux
execution_mode: automated
provisioning_adapter: environment/SetupLinux.sh
status: current
supported: Ubuntu and Pop!_OS
verified_on: 2026-07-17
source_docs: linux/Environment-Setup.md
---

Install Homebrew, add its shell environment to `.zprofile`, and install GCC.

## Verification

Open a new shell and run `brew --prefix`.
