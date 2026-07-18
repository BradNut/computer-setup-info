---
id: linux-flatpak-applications
title: Linux Flatpak application set
entry_points: linux
execution_mode: automated
provisioning_adapter: environment/SetupLinux.sh
status: current
supported: Flatpak with Flathub on Ubuntu and Pop!_OS
verified_on: 2026-07-17
source_docs: linux/Applications.md
---

Enable Flathub and install the selected desktop application set.

## Verification

Run `flatpak list` and launch the applications you intend to use.
