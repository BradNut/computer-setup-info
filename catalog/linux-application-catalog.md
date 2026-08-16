---
id: linux-application-catalog
title: Linux application catalog
entry_points: linux
execution_mode: manual
status: current
supported: Ubuntu and Pop!_OS application selection and install-channel verification
verified_on: 2026-08-15
source_docs: reference/linux/Applications.md
---

Use this `Inventory Record` as the canonical Linux application catalog. Each application records its agreed `Install Channel` so the active [Linux Setup Plan](../plans/linux.md) no longer relies on the legacy `linux/` directory as a navigation root.

`Install Channel` values used here follow the repository glossary: `apt`, `direct .deb`, `Flatpak`, `Homebrew`, `curl installer`, `AppImage`, and `manual download`. Shared cross-platform application decisions still live in the [shared desktop software inventory](./shared-desktop-software.md) and related shared records; this catalog maps those choices to the Linux channel.

## Shared desktop applications — Linux install channels

| Application | Shared parent record | Install Channel | Notes |
| --- | --- | --- | --- |
| Bitwarden | [Shared desktop software inventory](./shared-desktop-software.md) | Flatpak | `com.bitwarden.desktop` from Flathub. |
| Brave Browser | [Shared desktop software inventory](./shared-desktop-software.md) | apt | Installed from the Brave apt repository configured by the provisioning adapter. |
| DBeaver | [Shared desktop software inventory](./shared-desktop-software.md) | Flatpak | `io.dbeaver.DBeaverCommunity` from Flathub. |
| FileZilla | [Shared desktop software inventory](./shared-desktop-software.md) | Flatpak | `org.filezillaproject.Filezilla` from Flathub. |
| Firefox | [Shared browser and extension choices](./shared-browser-and-extension-choices.md) | apt | Keep the distro-packaged Firefox as the compatibility-check path. |
| Proton Bridge | [Shared account and privacy decisions](./shared-account-and-privacy-decisions.md) | direct `.deb` | Installed from the ProtonMail Bridge `.deb` by the provisioning adapter. |
| Signal | [Shared account and privacy decisions](./shared-account-and-privacy-decisions.md) | apt | Installed from the Signal apt repository configured by the provisioning adapter. |
| Standard Notes | [Shared desktop software inventory](./shared-desktop-software.md) | Flatpak | `org.standardnotes.standardnotes` from Flathub. |
| Sublime Text | [Shared coding environment preferences](./shared-coding-environment-preferences.md) | apt | Installed from the Sublime Text apt repository configured by the provisioning adapter. |
| Synology Drive | [Shared account and privacy decisions](./shared-account-and-privacy-decisions.md) | Flatpak | `com.synology.SynologyDrive` from Flathub. |
| Yubico Authenticator | [Shared account and privacy decisions](./shared-account-and-privacy-decisions.md) | Flatpak | `com.yubico.yubioath` from Flathub. |

## Linux-specific follow-up applications

| Application | Install Channel | Notes |
| --- | --- | --- |
| AppImage Launcher | apt (PPA) | Integrates AppImages into the desktop menu; the provisioning adapter uses the PPA when available. |
| Bruno | Flatpak | `com.usebruno.Bruno` from Flathub. |
| Buckets | Flatpak | `com.budgetwithbuckets.Buckets` from Flathub. |
| Calibre | Flatpak | `com.calibre_ebook.calibre` from Flathub. |
| Cryptomator | manual download | Download the AppImage or `.deb` from the upstream release page. |
| Droidcam | manual download | Use only if phone-as-webcam workflow is needed. |
| Epiphany | Flatpak | `org.gnome.Epiphany` from Flathub; WebKit test browser. |
| Forecast | Flatpak | `com.jwestall.Forecast` from Flathub. |
| Grayjay | Flatpak | `app.grayjay.Grayjay` from Flathub. |
| HandBrake | Flatpak | `fr.handbrake.ghb` from Flathub. |
| Joplin | Flatpak | `net.cozic.joplin_desktop` from Flathub. |
| MegaSync | apt | Installed from the MEGA apt repository configured by the provisioning adapter. |
| Mullvad Browser | apt | Installed from the Mullvad apt repository configured by the provisioning adapter. |
| OBS Studio | Flatpak | `com.obsproject.Studio` from Flathub. |
| Piper | Flatpak | `org.freedesktop.Piper` from Flathub. |
| Plexamp | AppImage | Desktop player; use AppImage Launcher for menu integration. |
| Podman Desktop | Flatpak | `io.podman_desktop.PodmanDesktop` from Flathub. |
| Proton Pass | direct `.deb` | Installed from the Proton Pass desktop `.deb` by the provisioning adapter. |
| Proton Pass CLI | curl installer | Installed via the official Proton pass-cli installer. |
| Proton VPN | apt | Installed from the Proton VPN apt repository configured by the provisioning adapter. |
| qBittorrent | Flatpak | `org.qbittorrent.qBittorrent` from Flathub. |
| Redis Insight | Flatpak | `com.redis.RedisInsight` from Flathub. |
| Shotcut | Flatpak | `org.shotcut.Shotcut` from Flathub. |
| Syncthing | manual download | Use only if Syncthing is needed outside the NAS workflow. |
| Thunderbird | Flatpak | `org.mozilla.Thunderbird` from Flathub. |
| VLC | Flatpak | `org.videolan.VLC` from Flathub. |
| Zed | Flatpak | `dev.zed.Zed` from Flathub; native install preferred where available. |

## Developer tooling and runtimes

| Application / Runtime | Install Channel | Notes |
| --- | --- | --- |
| Docker Engine | apt | Docker apt repository; includes Buildx, Compose, and containerd. |
| GCC | Homebrew | Installed via `brew install gcc` after Homebrew bootstrap. |
| Git | apt | Base system package. |
| Homebrew | curl installer | Linuxbrew bootstrap via the official install script. |
| Node (nvm) | curl installer | Node Version Manager + LTS Node. |
| npm-check-updates | curl installer / npm | Installed globally via npm after nvm. |
| pnpm | curl installer | Official pnpm install script. |
| Starship | curl installer | Official Starship install script. |
| tldr | curl installer / npm | Installed globally via npm. |
| trash-cli | curl installer / npm | Installed globally via npm. |
| Vim | apt | Base system package. |
| zimfw | curl installer | Zsh framework via the official install script. |
| zoxide | curl installer | Official zoxide install script. |
| Zsh | apt | Base system package. |

## Additional source material

- [Legacy Linux application list](../reference/linux/Applications.md)
- [Legacy Linux environment setup](../reference/linux/Environment-Setup.md)
- [Legacy Linux Docker setup](../reference/linux/Docker-Setup.md)

## Related records

- [Linux Setup Plan](../plans/linux.md)
- [Linux Inventory Exports](../exports/linux/README.md)
- [Linux base system](./linux-base-system.md)
- [Linux terminal tooling](./linux-terminal-tooling.md)
- [Linux Homebrew](./linux-homebrew.md)
- [Linux Docker](./linux-docker.md)
- [Linux desktop applications](./linux-desktop-applications.md)
- [Linux Flatpak applications](./linux-flatpak-applications.md)
- [Shared desktop software inventory](./shared-desktop-software.md)
- [Shared coding environment preferences](./shared-coding-environment-preferences.md)
- [Shared terminal preferences](./shared-terminal-preferences.md)
- [Shared browser and extension choices](./shared-browser-and-extension-choices.md)
- [Shared account and privacy decisions](./shared-account-and-privacy-decisions.md)
