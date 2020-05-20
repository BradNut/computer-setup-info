# Linux Apps

## Software Applications

- [Anydesk](https://anydesk.com/en/downloads/linux)
- [Bitwarden](https://bitwarden.com/#download)
  - Locally using flatpak
- [Brave Browser](https://brave.com/download/)
- [FileZilla](https://filezilla-project.org/download.php?type=client)
  - Locally using flatpak
- Firefox
- [Lutris](https://lutris.net/downloads/)
- [Mulvad](https://mullvad.net/en/download/)
- [NordVPN](https://support.nordvpn.com/Connectivity/Linux/1325531132/Installing-and-using-NordVPN-on-Debian-Ubuntu-Elementary-OS-and-Linux-Mint.htm)
- [Plex Media Player](https://knapsu.eu/plex/)
- Postman
- [Piper](https://github.com/libratbag/piper)
  - [Local Reference](../master/linux/Resources-Information.md)
- [Proton Bridge](https://protonmail.com/bridge/install)
  - [Bridge Setup](../master/linux/Proton-Bridge-Setup.md)
- [Proton VPN](https://protonvpn.com/support/linux-vpn-tool/)
- qBittorrent
  - Locally using flatpak
- Thunderbird
- Transmission
- [Signal](https://signal.org/download/#)
  - Locally using flatpak
- [Standard Notes](https://standardnotes.org/extensions?downloaded=linux)
- Steam
  - Locally using flatpak
- Sublime Text
  - Locally using flatpak
- [Synology Drive](https://www.synology.com/en-us/support/download/DS918+#utilities)
- VSCode
- Yubico Authenticator

---

## Flatpak Applications

- [Bitwarden](https://flathub.org/apps/details/com.bitwarden.desktop): `flatpak install flathub com.bitwarden.desktop`
- [Evolution](https://flathub.org/apps/details/org.gnome.Evolution): `flatpak install flathub org.gnome.Evolution` 
- [FileZilla](https://flathub.org/apps/details/org.filezillaproject.Filezilla): `flatpak install flathub org.filezillaproject.Filezilla`
- Plex Media Player: `flatpak install https://knapsu.eu/data/plex/tv.plex.PlexMediaPlayer.flatpakref`
- [Postman](https://flathub.org/apps/details/com.getpostman.Postman): `flatpak install flathub com.getpostman.Postman`
- [Piper](https://flathub.org/apps/details/org.freedesktop.Piper): `flatpak install flathub org.freedesktop.Piper`
- [Sublime Text](https://flathub.org/apps/details/com.sublimetext.three): `flatpak install flathub com.sublimetext.three`
- [Steam](https://flathub.org/apps/details/com.valvesoftware.Steam): `flatpak install flathub com.valvesoftware.Steam`
- [qBittorrent](https://flathub.org/apps/details/org.qbittorrent.qBittorrent): `flatpak install flathub org.qbittorrent.qBittorrent`
- [Transmission](https://flathub.org/apps/details/com.transmissionbt.Transmission): `flatpak install flathub com.transmissionbt.Transmission`

---

## App Image Applications

- [Plexamp](https://plexamp.com/#downloads)
- [Standard Notes](https://standardnotes.org/extensions?downloaded=linux)
- [Yubico Authenticator](https://www.yubico.com/products/services-software/download/yubico-authenticator/#download_here)

### App Image Instructions

Linux AppImage Instructions:

An AppImage is a self-contained instance of the application. Upon download, please move this file to a more permanent location on your system. You will need to keep this file for as long as you intend to use Standard Notes.

We'll move this file from your downloads to your home directory:
- `mv ~/Downloads/{APP_IMAGE.AppImage} ~/{APP_IMAGE}.AppImage`
- `cd ~`

Now, make the file executable:
- `chmod a+x {APP_IMAGE}.AppImage`

Finally, run the application:
- `./{APP_IMAGE}.AppImage`

If you're prompted to create desktop shortcuts, choose Yes.

---

## Specific App Install Instructions

## Signal Install
### Linux (Debian-based) Install Instructions
1. `curl -s https://updates.signal.org/desktop/apt/keys.asc | sudo apt-key add -`
2. `echo "deb [arch=amd64] https://updates.signal.org/desktop/apt xenial main" | sudo tee -a /etc/apt/sources.list.d/signal-xenial.list`
3. `sudo apt update && sudo apt install signal-desktop`