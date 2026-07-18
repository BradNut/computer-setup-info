---
id: linux-setup-plan
title: Linux setup plan
entry_point: linux
status: current
supported: Ubuntu and Pop!_OS
verified_on: 2026-07-17
provisioning_adapter: ../environment/SetupLinux.sh
---

# Linux Setup Plan

## 1. Base system — automated

Run the Linux provisioning adapter to apply `linux-base-system`, `linux-terminal-tooling`, `linux-homebrew`, `linux-docker`, `linux-desktop-applications`, and `linux-flatpak-applications`.

```bash
bash environment/SetupLinux.sh
```

## 2. Configuration — manual

- Apply [terminal and shell preferences](../environment/Terminal.md).
- Configure [coding applications](../environment/Coding-App-Configs.md).
- Review [desktop setup](../linux/Desktop-Setup.md).

## 3. Optional or device-specific work — manual

- Review [Linux resources](../linux/Resources-Information.md).
- Review [Proton Bridge](../linux/Proton-Bridge-Setup.md) and [Proton VPN](../linux/ProtonVPN-Configuration.md) before use.
- Decide on every candidate in the [obsolescence review queue](../review/obsolete-candidates.md) before relying on it.

## Verification

Confirm the verification steps in each automated resource, then start a new terminal session before using Homebrew, Zsh, NVM, or pnpm.
