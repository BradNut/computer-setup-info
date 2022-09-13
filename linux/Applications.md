# Linux Apps

## Software Applications

- [Anydesk](https://anydesk.com/en/downloads/linux)
- [App Image Launcher](https://github.com/TheAssassin/AppImageLauncher)
- [Bitwarden](https://bitwarden.com/#download)
  - Or using flatpak
- [Brave Browser](https://brave.com/download/)
- Cheese - Picture app
- Cryptomator
- DBeaver
  - Flatpak
- Emoji Picker
  - Deb from App Shop
- [Evolution](https://help.gnome.org/users/evolution/stable/): `sudo apt-get install evolution`
  - _PopOS only integrates Gnome Calendar with Evolution if installed from apt-get_
  - CalDAV Synology link: https://\*.synology.me:38443/caldav.php/USERNAME/eyeewj/
- [FileZilla](https://filezilla-project.org/download.php?type=client)
  - Locally using flatpak
- Firefox and dev variants
  - Install via flatpak or for linux use: https://github.com/Linux-Is-Best/Firefox-automatic-install-for-Linux
- [FreeTube](https://freetubeapp.io/)
  - Flatpak: https://flathub.org/apps/details/io.freetubeapp.FreeTube
- Gnome Tweaks
- [HyperJS Terminal](https://hyper.is/#installation)
- [Lutris](https://lutris.net/downloads/)
- [MegaSync](https://mega.nz/sync)
- [Mullvad](https://mullvad.net/en/download/)
- [NordVPN](https://support.nordvpn.com/Connectivity/Linux/1325531132/Installing-and-using-NordVPN-on-Debian-Ubuntu-Elementary-OS-and-Linux-Mint.htm)
- [Plex Media Player](https://knapsu.eu/plex/)
- Postman
- [Piper](https://github.com/libratbag/piper)
  - [Local Reference](../master/linux/Resources-Information.md)
- [Proton Bridge](https://protonmail.com/bridge/install)
  - [Bridge Setup](https://github.com/BradNut/computer-setup-info/blob/master/linux/Proton-Bridge-Setup.md)
  - _If bridge DEB file fails try installing from [Flathub](https://flathub.org/apps/details/ch.protonmail.protonmail-bridge)_
- [Proton VPN](https://protonvpn.com/support/linux-vpn-tool/)
- qBittorrent
  - Locally using Flatpak
  - Themes:
    - https://github.com/maboroshin/qBittorrentDarktheme
- Thunderbird
  - Flathub or Deb
- [Timeshift](https://github.com/teejee2008/timeshift)
- [Signal](https://signal.org/download/#)
  - Locally using flatpak
- [Standard Notes](https://standardnotes.org/extensions?downloaded=linux)
- Steam
  - Use DEB for supported
  - Locally use flatpak if can't get running: https://flathub.org/apps/details/com.valvesoftware.Steam
- [Sublime Text](https://www.sublimetext.com/docs/linux_repositories.html#apt)
  - Or using flatpak
- [Synology Drive](https://www.synology.com/en-us/support/download/DS918+#utilities)
- [Synology Note Station](https://www.synology.com/en-us/support/download/DS918+#utilities)
- [VLC](https://www.videolan.org/vlc/download-ubuntu.html)
- [VSCode](https://code.visualstudio.com/Download)
- Web
  - Flatpak
  - Browser to test WebKit like functionality
- WoeUSB
- Yubico Authenticator
  - App Image works
  - Flatpak: https://flathub.org/apps/details/com.yubico.yubioath

---

## Flatpak Applications

- [Bitwarden](https://flathub.org/apps/details/com.bitwarden.desktop): `flatpak install flathub com.bitwarden.desktop`
- [Cawbird](https://flathub.org/apps/details/uk.co.ibboard.cawbird): `flatpak install flathub uk.co.ibboard.cawbird`
- [DBeaver](https://flathub.org/apps/details/io.dbeaver.DBeaverCommunity): `flatpak install flathub io.dbeaver.DBeaverCommunity`
- [Evolution](https://flathub.org/apps/details/org.gnome.Evolution): `flatpak install flathub org.gnome.Evolution`
- [FileZilla](https://flathub.org/apps/details/org.filezillaproject.Filezilla): `flatpak install flathub org.filezillaproject.Filezilla`
- [FreeTube](https://flathub.org/apps/details/io.freetubeapp.FreeTube)
- Plex Media Player: `flatpak install https://knapsu.eu/data/plex/tv.plex.PlexMediaPlayer.flatpakref`
- [Postman](https://flathub.org/apps/details/com.getpostman.Postman): `flatpak install flathub com.getpostman.Postman`
- [Piper](https://flathub.org/apps/details/org.freedesktop.Piper): `flatpak install flathub org.freedesktop.Piper`
- [ProtonMail Bridge](https://flathub.org/apps/details/ch.protonmail.protonmail-bridge)
- [Sublime Text](https://flathub.org/apps/details/com.sublimetext.three): `flatpak install flathub com.sublimetext.three`
- [Steam](https://flathub.org/apps/details/com.valvesoftware.Steam): `flatpak install flathub com.valvesoftware.Steam`
- [qBittorrent](https://flathub.org/apps/details/org.qbittorrent.qBittorrent): `flatpak install flathub org.qbittorrent.qBittorrent`
- [Tootle](https://flathub.org/apps/details/com.github.bleakgrey.tootle): `flatpak install flathub com.github.bleakgrey.tootle`
- [Transmission](https://flathub.org/apps/details/com.transmissionbt.Transmission): `flatpak install flathub com.transmissionbt.Transmission`
- [Web](https://flathub.org/apps/details/org.gnome.Epiphany): `flatpak install flathub org.gnome.Epiphany`
- [YubicoAuth](https://flathub.org/apps/details/com.yubico.yubioath)

---

## App Image Applications

- [Plexamp](https://plexamp.com/#downloads)
- [Standard Notes](https://standardnotes.org/extensions?downloaded=linux)
- [Yubico Authenticator](https://www.yubico.com/products/services-software/download/yubico-authenticator/#download_here)

### App Image Instructions

[App Image Launcher](https://github.com/TheAssassin/AppImageLauncher) - Used to automatically link for execution
- Installation: https://github.com/TheAssassin/AppImageLauncher/wiki/Install-on-Ubuntu-or-Debian

OR Manual Install

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

## Yubico Authenticator

Ubuntu 20.04-20.10 does not fully connect to the devices. Extra repositories need installing.

```
$ sudo apt update && sudo apt install -y gnupg2 gnupg-agent scdaemon pcscd
$ gpg --card-status
```

_gpg command should run with no errors_
