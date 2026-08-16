# Primary Android Inventory Export

This curated `Inventory Export` captures the current Android application target represented by the active [Android Setup Plan](../../plans/android.md) and [Android application catalog](../../catalog/android-application-catalog.md).

## Snapshot metadata

- Entry Point: `android`
- Snapshot name: `primary-device`
- Curated on: `2026-08-15`
- Source records:
  - [Android application catalog](../../catalog/android-application-catalog.md)

## Installed applications

- Aegis Authenticator
- AnonAddy
- AntennaPod
- Aurora Store
- Bitwarden
- DAVx⁵
- Droid-ify
- F-Droid
- Feeder
- FUTO Keyboard
- FUTO Voice Input
- Gadgetbridge
- HERE WeGo
- IronFox
- KOReader
- LibreTorrent
- List My Apps
- Loyalty Card Keychain
- Magic Earth
- Material Files
- Mullvad VPN
- OpenTasks
- PipePipe
- Plex
- Plexamp
- Port Authority
- Proton Drive
- Proton Mail
- Proton Pass
- ProtonVPN
- RedReader
- Scarlet Notes FD
- S. Notes
- SeedVault
- Shopping List
- Shattered Pixel Dungeon
- Signal
- Simple Calendar
- SQLiteViewer
- Steam
- Stocks Widget
- Syncthing-Fork
- Synology Drive
- TIDAL
- Tutanota
- Untappd
- Untracker
- VLC
- Voice Recorder
- wallabag
- Wikipedia
- Yubico Authenticator

## Application source mix represented by this export

- F-Droid — primary source for open-source apps.
- Play Store via Aurora — for apps with no tracked F-Droid build or proprietary dependencies.
- Manual repo (IzzyOnDroid, Bitwarden F-Droid) — when the primary source is a third-party repository.

## Reconciliation notes

- Use this export to confirm a rebuilt or freshly configured Android device still matches the tracked application set without returning to the legacy `android/` directory.
- If an app switches to a new primary source, update the [Android application catalog](../../catalog/android-application-catalog.md) first, then refresh this export.
