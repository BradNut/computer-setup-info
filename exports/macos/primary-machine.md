# Primary macOS Inventory Export

This curated `Inventory Export` captures the current macOS desktop rebuild target represented by the active [macOS Setup Plan](../../plans/macos.md) and [macOS application catalog](../../catalog/macos-application-catalog.md).

## Snapshot metadata

- Entry Point: `macos`
- Snapshot name: `primary-machine`
- Curated on: `2026-08-15`
- Source records:
  - [macOS application catalog](../../catalog/macos-application-catalog.md)
  - [Shared desktop software inventory](../../catalog/shared-desktop-software.md)
  - [Shared coding environment preferences](../../catalog/shared-coding-environment-preferences.md)
  - [Shared terminal preferences](../../catalog/shared-terminal-preferences.md)

## Installed applications

- Bitwarden
- Brave Browser
- DBeaver
- FileZilla
- Firefox
- IntelliJ IDEA
- iTerm2
- Paw
- Plex Media Player
- Postman
- Proton Bridge
- Rectangle
- Signal
- Standard Notes
- Steam
- Sublime Text
- Synology Drive
- Transmission
- Visual Studio Code or VSCodium
- Yubico Authenticator

## Install-channel mix represented by this export

- manual download — current channel recorded for the applications preserved from the legacy macOS notes
- shared follow-up — see the shared desktop records for cross-platform preference and account decisions

## Reconciliation notes

- Use this export to confirm the rebuilt machine still matches the tracked macOS application set without returning to the legacy `macos/` directory.
- If the current machine uses Homebrew-managed formulas or casks that should become canonical, add them to the macOS catalog and refresh this export in the same change.
