# Linux Apps

## Software Applications

- Bitwarden
- Brave Browser
- FileZilla
- Firefox
- Lutris
- [Plex Media Player](https://knapsu.eu/plex/)
- Postman
- Piper
- Proton Bridge
- qBittorrent
- Transmission
- Signal
- Standard Notes
- Steam
- Sublime Text
- Synology Drive
- VSCode
- Yubico Authenticator

## Flatpak Applications

- [Bitwarden](https://flathub.org/apps/details/com.bitwarden.desktop): `flatpak install flathub com.bitwarden.desktop`
- [FileZilla](https://flathub.org/apps/details/org.filezillaproject.Filezilla): `flatpak install flathub org.filezillaproject.Filezilla`
- Plex Media Player: `flatpak install https://knapsu.eu/data/plex/tv.plex.PlexMediaPlayer.flatpakref`
- [Postman](https://flathub.org/apps/details/com.getpostman.Postman): `flatpak install flathub com.getpostman.Postman`
- [Piper](https://flathub.org/apps/details/org.freedesktop.Piper): `flatpak install flathub org.freedesktop.Piper`
- [qBittorrent](https://flathub.org/apps/details/org.qbittorrent.qBittorrent): `flatpak install flathub org.qbittorrent.qBittorrent`
- [Transmission](https://flathub.org/apps/details/com.transmissionbt.Transmission): `flatpak install flathub com.transmissionbt.Transmission`

## App Image Applications

- Plexamp
- Standard Notes
- Yubico Authenticator

### App Image Instructions

Linux AppImage Instructions:

An AppImage is a self-contained instance of the application. Upon download, please move this file to a more permanent location on your system. You will need to keep this file for as long as you intend to use Standard Notes.

We'll move this file from your downloads to your home directory:

    mv ~/Downloads/Standard-Notes-3.4.1.AppImage ~/Standard-Notes-3.4.1.AppImage

    cd ~

Now, make the file executable:

    chmod a+x Standard-Notes-3.4.1.AppImage

Finally, run the application:

    ./Standard-Notes-3.4.1.AppImage

If you're prompted to create desktop shortcuts, choose Yes.