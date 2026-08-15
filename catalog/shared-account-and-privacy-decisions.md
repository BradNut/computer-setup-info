---
id: shared-account-and-privacy-decisions
title: Shared account and privacy decisions
entry_points: linux, macos
execution_mode: manual
status: current
supported: Linux and macOS account-backed and privacy-sensitive choices
verified_on: 2026-08-15
source_docs: environment/Shared-Desktop-Setup.md
---

Use this `Inventory Record` for the account-backed and privacy-sensitive decisions that should stay aligned across Linux and macOS.

## Core services to review

- Bitwarden for passwords and secure-item sync
- Proton services such as Proton Bridge, Proton Pass, and Proton VPN where the current platform record supports them
- Signal for messaging
- Synology Drive for NAS-backed synchronization
- Yubico Authenticator for hardware-token workflows

## Review expectations

- Confirm the intended account is signed in before importing data or secrets
- Re-check any manual download or direct installer path before use
- Keep privacy-sensitive application choices consistent across desktop platforms when practical

## Related records

- [Shared desktop software inventory](./shared-desktop-software.md)
- [Shared terminal preferences](./shared-terminal-preferences.md)
