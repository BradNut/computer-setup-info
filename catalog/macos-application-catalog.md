---
id: macos-application-catalog
title: macOS application catalog
entry_points: macos
execution_mode: manual
status: current
supported: macOS desktop rebuild path
verified_on: 2026-08-15
source_docs: reference/macos/Applications.md
---

Use this `Inventory Record` as the macOS-specific follow-up to the shared desktop records. It captures the macOS application set and the preferred `Install Channel` for each app so the active [macOS Setup Plan](../plans/macos.md) no longer needs the legacy macOS directory as a navigation root.

## Shared application child records

These applications come from the shared desktop inventory but keep macOS-specific install truth here.

| Application | Shared parent record | Install Channel | Notes |
| --- | --- | --- | --- |
| Bitwarden | [Shared desktop software inventory](./shared-desktop-software.md) | manual download | Install the macOS desktop app before signing in and syncing secrets. |
| Brave Browser | [Shared desktop software inventory](./shared-desktop-software.md) | manual download | Primary Chromium-based browser choice on macOS. |
| DBeaver | [Shared desktop software inventory](./shared-desktop-software.md) | manual download | Database client for shared workstation workflows. |
| FileZilla | [Shared desktop software inventory](./shared-desktop-software.md) | manual download | Use when an SFTP-capable GUI transfer client is still needed. |
| Firefox | [Shared browser and extension choices](./shared-browser-and-extension-choices.md) | manual download | Mozilla-based browser and compatibility-check path. |
| Proton Bridge | [Shared account and privacy decisions](./shared-account-and-privacy-decisions.md) | manual download | Review account details before connecting a mail client. |
| Signal | [Shared account and privacy decisions](./shared-account-and-privacy-decisions.md) | manual download | Confirm desktop linking after install. |
| Standard Notes | [Shared desktop software inventory](./shared-desktop-software.md) | manual download | Confirm the intended account before syncing notes. |
| Sublime Text | [Shared coding environment preferences](./shared-coding-environment-preferences.md) | manual download | Reapply Package Control add-ons and synced preferences after install. |
| Synology Drive | [Shared account and privacy decisions](./shared-account-and-privacy-decisions.md) | manual download | Reconnect to the intended NAS profile only. |
| Yubico Authenticator | [Shared account and privacy decisions](./shared-account-and-privacy-decisions.md) | manual download | Verify hardware-token access before relying on 2FA workflows. |

## macOS-specific follow-up applications

These applications do not belong in the shared parent inventory but remain part of the current macOS rebuild path.

| Application | Install Channel | Notes |
| --- | --- | --- |
| IntelliJ IDEA | manual download | Reapply the preferred plugin set from the shared coding preferences. |
| iTerm2 | manual download | Use the settings preserved in `reference/macos/Coding-App-Setup.md` together with [shared terminal preferences](./shared-terminal-preferences.md). |
| Paw | manual download | Legacy API-client preference for macOS. |
| Plex Media Player | manual download | Keep only if the current playback workflow still depends on it. |
| Postman | manual download | Install only when the workflow specifically needs Postman rather than Bruno or another tracked client. |
| Rectangle | manual download | Window-management utility for the current macOS desktop layout. |
| Steam | manual download | Gaming follow-up; install only if the current Mac is used for it. |
| Transmission | manual download | BitTorrent client for the current macOS workflow. |
| Visual Studio Code or VSCodium | manual download | Reapply the shared editor-extension inventory after install. |

## Additional source material

- [Legacy macOS application list](../reference/macos/Applications.md)
- [Legacy macOS coding app setup](../reference/macos/Coding-App-Setup.md)

## Related records

- [macOS Setup Plan](../plans/macos.md)
- [macOS Inventory Exports](../exports/macos/README.md)
- [Shared desktop software inventory](./shared-desktop-software.md)
- [Shared coding environment preferences](./shared-coding-environment-preferences.md)
- [Shared terminal preferences](./shared-terminal-preferences.md)
- [Shared browser and extension choices](./shared-browser-and-extension-choices.md)
- [Shared account and privacy decisions](./shared-account-and-privacy-decisions.md)
