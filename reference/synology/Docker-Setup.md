# Docker / Container Manager Apps and Configuration

> **2026 update:** In DSM 7.2 and later, the Docker package has been renamed **Container Manager** and now supports Docker Compose projects from the UI. Command-line `docker` and `docker compose` still work via SSH for advanced use.

## Container Manager

- Search for **Container Manager** in Package Center (DSM 7.2+). For earlier DSM versions the package is still called **Docker**.
- Container Manager supports `docker-compose.yml` projects in the Project tab.

## Transmission

The original Haugene `transmission-openvpn` image is now archived/unmaintained. Current 2026 options:

- [haugene/docker-transmission-openvpn](https://github.com/haugene/docker-transmission-openvpn) (archived; reference only)
- [linuxserver/transmission](https://github.com/linuxserver/docker-transmission) or [linuxserver/qbittorrent](https://github.com/linuxserver/docker-qbittorrent), typically paired with a separate VPN container such as [Gluetun](https://github.com/qdm12/gluetun) or a VPN router.

## Legacy Advanced Media Setup

The older Plex/Sonarr/Radarr/SABnzbd/Transmission walkthrough is in [Advanded-Media-Setup.md](./Advanded-Media-Setup.md). It was last updated in 2019 and many details (Docker package name, image tags, and Plex installation) have changed.
