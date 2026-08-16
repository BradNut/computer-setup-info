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

Use this as the active Linux setup route. Supporting `Resource Catalog` material lives in [catalog](../catalog/README.md), curated Linux exports live in [exports/linux](../exports/linux/README.md), and historical material belongs in [reference](../reference/README.md).

## 1. Base system — automated

Run the Linux provisioning adapter to apply `linux-base-system`, `linux-terminal-tooling`, `linux-homebrew`, `linux-docker`, `linux-desktop-applications`, and `linux-flatpak-applications`.

```bash
bash environment/SetupLinux.sh
```

## 2. Shared desktop configuration — manual

- Apply [shared terminal preferences](../catalog/shared-terminal-preferences.md).
- Apply [shared coding environment preferences](../catalog/shared-coding-environment-preferences.md).
- Review [shared desktop software inventory](../catalog/shared-desktop-software.md) for applications not fully covered by automated Linux records.
- Review [shared browser and extension choices](../catalog/shared-browser-and-extension-choices.md).
- Review [shared account and privacy decisions](../catalog/shared-account-and-privacy-decisions.md).

## 3. Choose and verify application install channels — manual

Review the canonical [Linux application catalog](../catalog/linux-application-catalog.md) for the install-channel mapping of every shared and Linux-specific application, then compare the chosen set against the latest curated export.

## 4. Reconcile against the latest export — manual

Compare the resulting system state against the latest curated [Primary machine export](../exports/linux/primary-machine.md) before considering the setup complete.

## 5. Historical Linux-specific follow-up — reference only

Legacy platform notes are preserved under [reference/linux](../reference/linux/) for research. Do not rely on them as an active navigation root.

- [Desktop setup](../reference/linux/Desktop-Setup.md)
- [Linux resources](../reference/linux/Resources-Information.md)
- [Proton Bridge](../reference/linux/Proton-Bridge-Setup.md)
- [Proton VPN](../reference/linux/ProtonVPN-Configuration.md)
- [Obsolescence review queue](../review/obsolete-candidates.md)

## Verification

Confirm the verification steps in each automated resource, then start a new terminal session before using Homebrew, Zsh, NVM, or pnpm.
