# Desktop Setup

## Gnome Extensions

- [Arc Menu](https://extensions.gnome.org/extension/3628/arcmenu/)
  - If error restart UI and/or check if installed: `sudo apt-get install gir1.2-gmenu-3.0` and `sudo apt-get install gnome-menus`
- [Blyr](https://extensions.gnome.org/extension/1251/blyr/)
- [Caffeine](https://extensions.gnome.org/extension/517/caffeine/)
- [Dash to Dock](https://micheleg.github.io/dash-to-dock/)
- [Dash to Panel](https://extensions.gnome.org/extension/1160/dash-to-panel/)
- [gTile](https://github.com/gTile)
- [OpenWeather](https://extensions.gnome.org/extension/750/openweather/)
- [Panel OSD](https://extensions.gnome.org/extension/708/panel-osd/)
- [Removable Drive Menu](https://extensions.gnome.org/extension/7/removable-drive-menu/)
- [User Themes](https://extensions.gnome.org/extension/19/user-themes/)
- [Workspace Matrix](https://extensions.gnome.org/extension/1485/workspace-matrix/)

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

1. [Plexamp](https://plexamp.com/#downloads)

```
[Desktop Entry]
Encoding=UTF-8
Version=1.0
Type=Application
Terminal=false
Exec=/home/bshellnu/Plexamp-3.0.2.AppImage --disable-seccomp-filter-sandbox
Name=Plexamp
Icon=/home/bshellnu/Documents/Desktop Icons/plexamp.png
MimeType=x-scheme-handler/xxx;text/html;
```

- [Plexamp Icon](https://github.com/BradNut/computer-setup-info/blob/master/linux/images/desktop-images/plexamp.png)

2. [Standard Notes](https://standardnotes.org/extensions?downloaded=linux)

```
[Desktop Entry]
Encoding=UTF-8
Version=1.0
Type=Application
Terminal=false
Exec=/home/bshellnu/Standard-Notes-3.3.5.AppImage
Name=Standard Notes
Icon=/home/bshellnu/Documents/Desktop Icons/StandardNotesIcon.png
```

- [Standard Notes Icon](https://github.com/BradNut/computer-setup-info/blob/master/linux/images/desktop-images/StandardNotesIcon.png)

3. [Yubico Authenticator](https://www.yubico.com/products/services-software/download/yubico-authenticator/#download_here)

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
