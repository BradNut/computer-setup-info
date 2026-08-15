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

## 3. Linux-specific follow-up — manual

- Review [desktop setup](../linux/Desktop-Setup.md).
- Review [Linux resources](../linux/Resources-Information.md).
- Review [Proton Bridge](../linux/Proton-Bridge-Setup.md) and [Proton VPN](../linux/ProtonVPN-Configuration.md) before use.
- Decide on every candidate in the [obsolescence review queue](../review/obsolete-candidates.md) before relying on it.

## Verification

Confirm the verification steps in each automated resource, then start a new terminal session before using Homebrew, Zsh, NVM, or pnpm.
