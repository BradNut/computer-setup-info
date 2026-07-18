---
id: linux-base-system
title: Linux base system packages
entry_points: linux
execution_mode: automated
provisioning_adapter: environment/SetupLinux.sh
status: current
supported: Ubuntu and Pop!_OS
verified_on: 2026-07-17
source_docs: linux/Environment-Setup.md
---

Install the base packages required by the Linux setup plan: development tools, terminal utilities, Flatpak support, SSH, smart-card support, and Zsh.

## Verification

Confirm `git`, `curl`, `flatpak`, `ssh`, and `zsh` are available after provisioning.
