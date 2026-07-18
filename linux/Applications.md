# Linux Apps

## Software Applications

- [App Image Launcher](https://github.com/TheAssassin/AppImageLauncher)
- [Bitwarden](https://bitwarden.com/#download)
- [Brave Browser](https://brave.com/download/)
- Cryptomator
- DBeaver
- [Evolution](https://help.gnome.org/evolution/): `sudo apt-get install evolution`
  - _PopOS only integrates Gnome Calendar with Evolution if installed from apt-get_
  - CalDAV Synology link: https://\*.synology.me:38443/caldav.php/USERNAME/eyeewj/
- [FileZilla](https://filezilla-project.org/download.php?type=client)
- Firefox and dev variants
  - Install for linux use: https://www.mozilla.org/firefox/linux/
- [Grayjay](https://grayjay.app/)
- [MegaSync](https://mega.io/desktop)
- [Plex HTPC](https://flathub.org/en/apps/tv.plex.PlexHTPC)
- [Bruno](https://www.usebruno.com/)
- [Piper](https://github.com/libratbag/piper)
  - [Local Reference](Resources-Information.md)
- [Proton Bridge](https://proton.me/mail/bridge)
  - [Bridge Setup](https://github.com/BradNut/computer-setup-info/blob/master/linux/Proton-Bridge-Setup.md)
  - _If bridge DEB file fails try installing from [Flathub](https://flathub.org/en/apps/ch.protonmail.protonmail-bridge)_
- [Proton VPN](https://protonvpn.com/support/linux-vpn-setup)
- [Proton Pass](https://proton.me/pass): Download the .deb from the [Linux setup guide](https://proton.me/support/set-up-proton-pass-linux)
- Proton Pass CLI: `curl -fsSL https://proton.me/download/pass-cli/install.sh | bash`
- qBittorrent
- Thunderbird
- [Signal](https://signal.org/download/)
- [Standard Notes](https://standardnotes.com/download/linux)
- Steam
  - Use DEB for supported
- [Sublime Text](https://www.sublimetext.com/docs/linux_repositories.html#apt)
- [Synology Drive](https://www.synology.com/en-us/support/download/DS918+#utilities)
- [Synology Note Station](https://www.synology.com/en-us/support/download/DS918+#utilities)
- [VLC](https://www.videolan.org/vlc/download-ubuntu.html)
- [Epiphany](https://flathub.org/en/apps/org.gnome.Epiphany)
  - Browser to test WebKit like functionality
- Yubico Authenticator
  - App Image works

---

## Flatpak Applications

- [Bitwarden](https://flathub.org/en/apps/com.bitwarden.desktop): `flatpak install flathub com.bitwarden.desktop`
- [DBeaver](https://flathub.org/en/apps/io.dbeaver.DBeaverCommunity): `flatpak install flathub io.dbeaver.DBeaverCommunity`
- [Evolution](https://flathub.org/en/apps/org.gnome.Evolution): `flatpak install flathub org.gnome.Evolution`
- [FileZilla](https://flathub.org/en/apps/org.filezillaproject.Filezilla): `flatpak install flathub org.filezillaproject.Filezilla`
- Plex HTPC: `flatpak install flathub tv.plex.PlexHTPC`
- [Bruno](https://flathub.org/en/apps/com.usebruno.Bruno): `flatpak install flathub com.usebruno.Bruno`
- [Piper](https://flathub.org/en/apps/org.freedesktop.Piper): `flatpak install flathub org.freedesktop.Piper`
- [ProtonMail Bridge](https://flathub.org/en/apps/ch.protonmail.protonmail-bridge)
- [Sublime Text](https://flathub.org/en/apps/com.sublimetext.three): `flatpak install flathub com.sublimetext.three`
- [Steam](https://flathub.org/en/apps/com.valvesoftware.Steam): `flatpak install flathub com.valvesoftware.Steam`
- [qBittorrent](https://flathub.org/en/apps/org.qbittorrent.qBittorrent): `flatpak install flathub org.qbittorrent.qBittorrent`
- [Thunderbird](https://flathub.org/en/apps/org.mozilla.Thunderbird): `flatpak install flathub org.mozilla.Thunderbird`
- [Epiphany](https://flathub.org/en/apps/org.gnome.Epiphany): `flatpak install flathub org.gnome.Epiphany`
- [YubicoAuth](https://flathub.org/en/apps/com.yubico.yubioath): `flatpak install flathub com.yubico.yubioath`
- [Grayjay](https://grayjay.app/): `flatpak install flathub app.grayjay.Grayjay`

---

## App Image Applications

- [Plexamp](https://plexamp.com/#downloads)
- [Standard Notes](https://standardnotes.com/download/linux)
- [Yubico Authenticator](https://www.yubico.com/products/yubico-authenticator/)

### App Image Launcher install

[App Image Launcher](https://github.com/TheAssassin/AppImageLauncher) automatically integrates AppImages into the desktop menu and launcher.

**Recommended install (PPA):**

```bash
sudo add-apt-repository ppa:appimagelauncher-team/stable
sudo apt update
sudo apt install appimagelauncher
```

Or download the latest `.deb` from the [GitHub releases](https://github.com/TheAssassin/AppImageLauncher/releases).

**Using App Image Launcher:**

After installing, double-click any `.AppImage` and choose *Integrate and run* when prompted. You can also right-click an AppImage and select *Integrate and run*.

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
