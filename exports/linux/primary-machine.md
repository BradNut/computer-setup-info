# Primary Linux Inventory Export

This curated `Inventory Export` captures the current Ubuntu/Pop!_OS desktop rebuild target represented by the active [Linux Setup Plan](../../plans/linux.md) and the Linux `Resource Catalog` records.

## Snapshot metadata

- Entry Point: `linux`
- Snapshot name: `primary-machine`
- Curated on: `2026-08-15`
- Source records:
  - [Linux Setup Plan](../../plans/linux.md)
  - [Linux base system](../../catalog/linux-base-system.md)
  - [Linux terminal tooling](../../catalog/linux-terminal-tooling.md)
  - [Linux Homebrew](../../catalog/linux-homebrew.md)
  - [Linux Docker](../../catalog/linux-docker.md)
  - [Linux desktop applications](../../catalog/linux-desktop-applications.md)
  - [Linux Flatpak applications](../../catalog/linux-flatpak-applications.md)
  - [Shared desktop software inventory](../../catalog/shared-desktop-software.md)
  - [Shared coding environment preferences](../../catalog/shared-coding-environment-preferences.md)
  - [Shared terminal preferences](../../catalog/shared-terminal-preferences.md)
  - [Shared browser and extension choices](../../catalog/shared-browser-and-extension-choices.md)
  - [Shared account and privacy decisions](../../catalog/shared-account-and-privacy-decisions.md)

## Base system packages

- build-essential
- ca-certificates
- containerd.io
- curl
- docker-buildx-plugin
- docker-ce
- docker-ce-cli
- docker-compose-plugin
- file
- flatpak
- git
- gnupg
- gnupg-agent
- htop
- jq
- lsb-release
- megasync
- mullvad-browser
- openssh-server
- pcscd
- proton-vpn-gnome-desktop
- scdaemon
- signal-desktop
- sshfs
- sublime-text
- vim
- xclip
- zsh

## Terminal tooling and runtimes

- Homebrew
- nvm + Node LTS
- npm-check-updates
- pnpm
- Starship
- tldr
- trash-cli
- zimfw
- zoxide

## Shared desktop applications

- Bitwarden
- Brave Browser
- DBeaver
- FileZilla
- Firefox
- Proton Bridge
- Signal
- Standard Notes
- Sublime Text
- Synology Drive
- Yubico Authenticator

## Flatpak applications

- app.grayjay.Grayjay
- best.ellie.StartupConfiguration
- com.bitwarden.desktop
- com.budgetwithbuckets.Buckets
- com.calibre_ebook.calibre
- com.jwestall.Forecast
- com.obsproject.Studio
- com.plexamp.Plexamp
- com.redis.RedisInsight
- com.synology.SynologyDrive
- com.usebruno.Bruno
- com.yubico.yubioath
- dev.deedles.Trayscale
- dev.edfloreshz.Calculator
- dev.edfloreshz.CosmicTweaks
- dev.edfloreshz.Tasks
- dev.mariinkys.Cedilla
- dev.zed.Zed
- fr.handbrake.ghb
- io.dbeaver.DBeaverCommunity
- io.github.cosmic_utils.camera
- io.github.pixeldotted.cosmic-ext-color-picker
- io.podman_desktop.PodmanDesktop
- md.obsidian.Obsidian
- net.cozic.joplin_desktop
- one.jwr.interstellar
- org.filezillaproject.Filezilla
- org.gnome.Epiphany
- org.qbittorrent.qBittorrent
- org.shotcut.Shotcut
- org.standardnotes.standardnotes
- org.videolan.VLC
- tv.plex.PlexDesktop

## Install-channel mix represented by this export

- `apt` — base system, Brave, Docker tools, Evolution, Mullvad Browser, Signal, Sublime Text, MEGAsync, Proton VPN desktop.
- `direct .deb` — Proton Pass desktop, ProtonMail Bridge.
- `Homebrew` — GCC and any future Linuxbrew formulae.
- `Flatpak` — desktop applications from Flathub.
- `curl installer` — Homebrew, nvm, pnpm, zimfw, zoxide, Starship.

## Reconciliation notes

- Use this export to confirm a rebuilt machine still matches the tracked Linux application set without returning to the legacy `linux/` directory.
- If the provisioning adapter (`environment/SetupLinux.sh`) changes, refresh this export and verify the `verified_on` dates in the Linux catalog records stay in sync.
