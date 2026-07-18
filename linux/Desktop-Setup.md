# Desktop Setup

## Custom Application Launchers on Pop!_OS COSMIC

Pop!_OS COSMIC does not use GNOME Extensions. It uses standard `.desktop` files in `~/.local/share/applications/` to populate the App Library and Dock.

Create a `~/.local/share/applications/AppName.desktop` file and make it executable:

```sh
chmod +x ~/.local/share/applications/AppName.desktop
```

_Entry should exist in `~/.local/share/applications/`_
_Entry should be `AppName.desktop`_

### Example Entry

```
[Desktop Entry]
Type=Application
Terminal=false
Exec=/path/to/{IMAGE_NAME}.AppImage
Name={DESKTOP_NAME}
Icon={ICON_LOCATION}
```

For `.desktop` files shipped by an installed `.deb` package, use the package's binary and icon name instead of a full path (for example, `Exec=buckets` and `Icon=buckets`).

### Entries Currently Using

1. [Bitwarden](https://vault.bitwarden.com/download/?app=desktop&platform=linux)

```
[Desktop Entry]
Type=Application
Terminal=false
Exec=/home/bshellnu/Bitwarden-1.26.5-x86_64.AppImage
Name=Bitwarden
Icon=/home/bshellnu/Documents/Desktop Icons/Bitwarden.png
MimeType=x-scheme-handler/bitwarden;text/html;
```

- [Bitwarden Icon](https://github.com/BradNut/computer-setup-info/blob/master/linux/images/desktop-images/Bitwarden.png)

2. [Plexamp](https://plexamp.com/#downloads)

```
[Desktop Entry]
Type=Application
Terminal=false
Exec=/home/bshellnu/Plexamp-3.0.2.AppImage --disable-seccomp-filter-sandbox
Name=Plexamp
Icon=/home/bshellnu/Documents/Desktop Icons/plexamp.png
```

- [Plexamp Icon](https://github.com/BradNut/computer-setup-info/blob/master/linux/images/desktop-images/plexamp.png)

3. [Standard Notes](https://standardnotes.org/extensions?downloaded=linux)

```
[Desktop Entry]
Type=Application
Terminal=false
Exec=/home/bshellnu/Standard-Notes-3.3.5.AppImage
Name=Standard Notes
Icon=/home/bshellnu/Documents/Desktop Icons/StandardNotesIcon.png
```

- [Standard Notes Icon](https://github.com/BradNut/computer-setup-info/blob/master/linux/images/desktop-images/StandardNotesIcon.png)

4. [Yubico Authenticator](https://www.yubico.com/products/services-software/download/yubico-authenticator/#download_here)

```
[Desktop Entry]
Type=Application
Terminal=false
Exec=/home/bshellnu/yubioath-desktop-5.0.1-linux.AppImage
Name=Yubico Authenticator
Icon=/home/bshellnu/Documents/Desktop Icons/YubicoAuthIcon.png
```

- [Yubico Auth Icon](https://github.com/BradNut/computer-setup-info/blob/master/linux/images/desktop-images/YubicoAuthIcon.png)

5. [Buckets](https://www.budgetwithbuckets.com/en/download.html)

Buckets is now installed from the `.deb` package, which provides its own `.desktop` file. No manual entry is needed; it will appear in the COSMIC App Library as `buckets`.
