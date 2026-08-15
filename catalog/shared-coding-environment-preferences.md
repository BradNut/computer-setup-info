---
id: shared-coding-environment-preferences
title: Shared coding environment preferences
entry_points: linux, macos
execution_mode: manual
status: current
supported: Linux and macOS coding environment preferences
verified_on: 2026-08-15
source_docs: environment/Shared-Desktop-Setup.md
---

Use this `Inventory Record` for editor, IDE, font, and development-environment preferences that should stay aligned across Linux and macOS.

## Editors and IDEs

- [VS Code](https://code.visualstudio.com/) or [VSCodium](https://vscodium.com/) with settings from the [dotfiles repository](https://github.com/BradNut/dotfiles)
- [Zed](https://zed.dev/) with `auto_install_extensions` configured for fresh-machine recovery
- [Sublime Text](https://www.sublimetext.com/) with Package Control add-ons and synced preferences
- [IntelliJ IDEA](https://www.jetbrains.com/idea/) with the preferred plugin set

## Shared preferences

- Preferred coding fonts: Fira Code and JetBrains Mono with ligatures
- Install editor shell commands where applicable so terminal workflows remain consistent
- Keep editor settings and reusable configuration in the [dotfiles repository](https://github.com/BradNut/dotfiles) when possible

## Related records

- [Shared browser and extension choices](./shared-browser-and-extension-choices.md)
- [Shared terminal preferences](./shared-terminal-preferences.md)
- [Shared desktop software inventory](./shared-desktop-software.md)
