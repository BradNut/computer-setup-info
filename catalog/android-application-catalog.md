---
id: android-application-catalog
title: Android application catalog
entry_points: android
execution_mode: manual
status: current
supported: Android application selection and source verification
verified_on: 2026-08-15
source_docs: reference/android/Applications.md
---

Use this `Inventory Record` as the canonical Android application catalog. Each application records a primary `Application Source` and optional alternate sources so the active [Android Setup Plan](../plans/android.md) no longer relies on the legacy Android directory as a navigation root.

Source conventions:

- **Play Store via Aurora** — Google Play package obtained through the [Aurora Store](https://f-droid.org/en/packages/com.aurora.store/) frontend, used when no fully open-source build is tracked.
- **F-Droid** — upstream open-source build distributed through F-Droid.
- **GitHub / direct** — upstream binary or repository not distributed through a store frontend.
- **Manual repo** — third-party F-Droid repository such as Bitwarden F-Droid or IzzyOnDroid.

## System-level utilities

| Application | Primary Source | Alternate Source(s) | Notes |
| --- | --- | --- | --- |
| SeedVault | F-Droid | — | Non-Google backup solution built into some ROMs; also available via F-Droid. |

## App-store frontends and repositories

| Application | Primary Source | Alternate Source(s) | Notes |
| --- | --- | --- | --- |
| Aurora Store | F-Droid | — | Anonymous Google Play client for apps without a tracked open-source build. |
| F-Droid | F-Droid | — | Primary open-source app repository. |
| Droid-ify | F-Droid | — | Alternative F-Droid client. |
| IzzyOnDroid repository | Manual repo | — | Add via `https://apt.izzysoft.de/fdroid/` for apps not in the main F-Droid repo. |

## Productivity, privacy, and accounts

| Application | Primary Source | Alternate Source(s) | Notes |
| --- | --- | --- | --- |
| Bitwarden | Manual repo (Bitwarden F-Droid) | Play Store via Aurora | Use the [Bitwarden F-Droid repo](https://mobileapp.bitwarden.com/fdroid/) for the official F-Droid build. |
| Proton Drive | Play Store via Aurora | — | Install only if the Proton account workflow requires it. |
| Proton Mail | Play Store via Aurora | — | Verify the account before restoring data. |
| Proton Pass | Play Store via Aurora | — | Password-manager follow-up if Bitwarden is not used. |
| Signal | Play Store via Aurora | — | Confirm safety-number / desktop linking after install. |
| Synology Drive | Play Store via Aurora | — | Connect to the intended NAS profile only. |

## Browsers

| Application | Primary Source | Alternate Source(s) | Notes |
| --- | --- | --- | --- |
| IronFox | F-Droid | — | Privacy-hardened Firefox fork. |

## Media and entertainment

| Application | Primary Source | Alternate Source(s) | Notes |
| --- | --- | --- | --- |
| Plex | Play Store via Aurora | — | Streaming server client. |
| Plexamp | Play Store via Aurora | — | Plex music player. |
| TIDAL | Play Store via Aurora | — | Subscription streaming service. |
| Untappd | Play Store via Aurora | — | Beer check-in and discovery. |
| VLC | F-Droid | Play Store via Aurora | Versatile media player. |

## Maps and navigation

| Application | Primary Source | Alternate Source(s) | Notes |
| --- | --- | --- | --- |
| HERE WeGo | Play Store via Aurora | — | Offline maps and navigation. |
| Magic Earth | Play Store via Aurora | — | Privacy-oriented maps app. |

## System tools and utilities

| Application | Primary Source | Alternate Source(s) | Notes |
| --- | --- | --- | --- |
| FUTO Keyboard | GitHub / direct | — | Open-source keyboard from [keyboard.futo.org](https://keyboard.futo.org/). |
| FUTO Voice Input | GitHub / direct | — | Voice input from [voiceinput.futo.org](https://voiceinput.futo.org/). |
| Gadgetbridge | F-Droid | — | FOSS fitness-device companion. |
| List My Apps | F-Droid | — | Export installed-app metadata. |
| Material Files | F-Droid | — | Material Design file manager. |
| Port Authority | F-Droid | — | Network port scanner. |
| SQLiteViewer | F-Droid | — | Lightweight SQLite viewer. |
| Untracker | F-Droid | — | Link tracking removal. |
| Voice Recorder | F-Droid | — | Simple audio recorder. |
| wallabag | F-Droid | — | Self-hosted bookmark archive; requires a wallabag instance. |

## Calendar, contacts, and sync

| Application | Primary Source | Alternate Source(s) | Notes |
| --- | --- | --- | --- |
| DAVx⁵ | F-Droid | Play Store via Aurora | CalDAV/CardDAV sync. |
| Simple Calendar | F-Droid | — | Offline calendar app. |

## Notes, tasks, and reading

| Application | Primary Source | Alternate Source(s) | Notes |
| --- | --- | --- | --- |
| Feeder | F-Droid | — | RSS/Atom feed reader. |
| KOReader | F-Droid | — | E-ink focused e-book reader. |
| Scarlet Notes FD | F-Droid | — | Free note-taking app. |
| S. Notes | F-Droid | — | Standard Notes client; subscription service. |
| Shopping List | F-Droid | — | Privacy-friendly shopping list. |
| Habits | F-Droid | — | Habit tracker. |
| OpenTasks | F-Droid | — | Task manager. |

## Authentication

| Application | Primary Source | Alternate Source(s) | Notes |
| --- | --- | --- | --- |
| Aegis Authenticator | F-Droid | — | TOTP / 2FA token manager. |
| Yubico Authenticator | F-Droid | — | Hardware-token OATH codes. |

## Games

| Application | Primary Source | Alternate Source(s) | Notes |
| --- | --- | --- | --- |
| Shattered Pixel Dungeon | F-Droid | — | Roguelike adventure game. |
| Minesweeper - Antimine | F-Droid | — | Minesweeper clone. |
| UnCiv | F-Droid | — | Open-source Civilization-style game. |
| Lexica | F-Droid | — | Word game. |

## Media tracking and finance

| Application | Primary Source | Alternate Source(s) | Notes |
| --- | --- | --- | --- |
| AntennaPod | F-Droid | — | Podcast player and manager. |
| LibreTorrent | F-Droid | — | Torrent client. |
| Loyalty Card Keychain | F-Droid | — | Gift-card and loyalty-card manager. |
| RedReader | F-Droid | — | Reddit client. |
| PipePipe | F-Droid | — | YouTube/NewPipe fork. |
| Stocks Widget | F-Droid | — | Stock tracker widget. |
| Wikipedia | F-Droid | — | Offline-capable Wikipedia reader. |

## Privacy and VPN

| Application | Primary Source | Alternate Source(s) | Notes |
| --- | --- | --- | --- |
| Mullvad VPN | F-Droid | — | VPN subscription; verify account before connecting. |
| ProtonVPN | F-Droid | Play Store via Aurora | VPN tied to Proton account. |

## Social and communication

| Application | Primary Source | Alternate Source(s) | Notes |
| --- | --- | --- | --- |
| Steam | Play Store via Aurora | — | Steam mobile client. |
| Syncthing-Fork | F-Droid | — | Peer-to-peer sync; requires a paired Syncthing instance. |

## Email aliasing

| Application | Primary Source | Alternate Source(s) | Notes |
| --- | --- | --- | --- |
| AnonAddy | F-Droid | — | Email aliasing service client. |
| Tutanota | F-Droid | — | Encrypted email service. |

## Additional source material

- [Legacy Android application list](../reference/android/Applications.md)

## Related records

- [Android Setup Plan](../plans/android.md)
- [Android Inventory Exports](../exports/android/README.md)
