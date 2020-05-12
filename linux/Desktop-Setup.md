# Desktop Setup

## Gnome Extensions

- [Dash to Dock](https://micheleg.github.io/dash-to-dock/)
- [gTile](https://github.com/gTile)

## Desktop Icon Creation

_Entry should exist in ~/.local/share/applications/_
_Entry should be AppName.desktop_

### Example Entry

```
[Desktop Entry]
Encoding=UTF-8
Version=1.0
Type=Application
Terminal=false
Exec=~/{IMAGE_NAME}.AppImage
Name={DESKTOP_NAME}
Icon={IMAGE_LOCATION}
MimeType=x-scheme-handler/xxx;text/html;
```

### Entries Currently Using

- [Plexamp](https://plexamp.com/#downloads)

```
[Desktop Entry]
Encoding=UTF-8
Version=1.0
Type=Application
Terminal=false
Exec=/home/bshellnu/Plexamp-3.0.2.AppImage
Name=Plexamp
Icon=/home/bshellnu/Documents/Desktop Icons/plexamp.png
MimeType=x-scheme-handler/xxx;text/html;
```

- [Plexamp Icon](https://github.com/BradNut/computer-setup-info/blob/master/linux/images/desktop-images/plexamp.png)

- [Standard Notes](https://standardnotes.org/extensions?downloaded=linux)

```
[Desktop Entry]
Encoding=UTF-8
Version=1.0
Type=Application
Terminal=false
Exec=/home/bshellnu/Standard-Notes-3.3.5.AppImage
Name=Standard Notes
Icon=/home/bshellnu/Documents/Desktop
Icons/StandardNotesIcon.png
```

- [Standard Notes Icon](https://github.com/BradNut/computer-setup-info/blob/master/linux/images/desktop-images/StandardNotesIcon.png)

- [Yubico Authenticator](https://www.yubico.com/products/services-software/download/yubico-authenticator/#download_here)

```
[Desktop Entry]
Encoding=UTF-8
Version=1.0
Type=Application
Terminal=false
Exec=/home/bshellnu/yubioath-desktop-5.0.1-linux.AppImage
Name=Yubico Authenticator
Icon=/home/bshellnu/Documents/Desktop Icons/YubicoAuthIcon.png
```

- [Yubico Auth Icon](https://github.com/BradNut/computer-setup-info/blob/master/linux/images/desktop-images/YubicoAuthIcon.png)
