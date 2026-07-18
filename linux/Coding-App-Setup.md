# Coding Applications

For editor configuration links, see [Coding App Configs](../environment/Coding-App-Configs.md).

## Sublime Text

- Install from Flathub: `flatpak install flathub com.sublimetext.three`
- Or use the apt repository configured in [SetupLinux.sh](../environment/SetupLinux.sh)
- [Configuration](https://github.com/BradNut/dotfiles/blob/master/Preferences.sublime-settings)

### Package Control

- [A File Icon](https://packagecontrol.io/packages/A%20File%20Icon)
- [Ayu Theme](https://packagecontrol.io/packages/ayu)
- [Cobalt2 Theme](https://packagecontrol.io/packages/Theme%20-%20Cobalt2)
- [ColorPicker](https://packagecontrol.io/packages/ColorPicker)
- [Gutter Color](https://packagecontrol.io/packages/Gutter%20Color)
- [HTML-CSS-JS Prettify](https://packagecontrol.io/packages/HTML-CSS-JS%20Prettify)
- [Rainbow Brackets](https://github.com/absop/RainbowBrackets)

## VSCode

- Install from Flathub: `flatpak install flathub com.visualstudio.code` or download the `.deb` from the [official site](https://code.visualstudio.com/docs/setup/linux)
- Configuration: [settings.json](https://github.com/BradNut/dotfiles/blob/master/settings.json)
- Packages installed: https://github.com/BradNut/dotfiles/blob/master/vs-code-extensions-i-use.md
- Install Shell Command: Install `code` command in PATH

### Troubleshooting

#### Visual Studio Code is unable to watch for file changes in this large workspace (error ENOSPC)

Docs: https://code.visualstudio.com/docs/setup/linux#_visual-studio-code-is-unable-to-watch-for-file-changes-in-this-large-workspace-error-enospc

> Follow these steps located [here](https://askubuntu.com/questions/776929/how-to-edit-my-etc-sysctl-conf-file).

Steps:

1. Open `/etc/sysctl.conf` in a terminal using `sudo nano /etc/sysctl.conf` or `sudo vim /etc/sysctl.conf`.

   - Scroll to the end and add `fs.inotify.max_user_watches=524288` by hand.
   - Save with `Ctrl+X`, then `Y`, then `Enter`.
   - _Use the same steps to reverse your changes._

2. Or add it directly from the terminal:

   ```bash
   echo "fs.inotify.max_user_watches=524288" | sudo tee -a /etc/sysctl.conf
   ```

   - To reverse this, refer to solution 1.

Then load the new value:

```bash
sudo sysctl -p
```

---

Info from VSCode docs:

When you see this notification, it indicates that the VS Code file watcher is running out of handles because the workspace is large and contains many files. The current limit can be viewed by running:

```bash
cat /proc/sys/fs/inotify/max_user_watches
```

The limit can be increased to its maximum by editing `/etc/sysctl.conf` (except on Arch Linux, read below) and adding this line to the end of the file:

```bash
fs.inotify.max_user_watches=524288
```

The new value can then be loaded in by running `sudo sysctl -p`.

While 524,288 is the maximum number of files that can be watched, if you're in an environment that is particularly memory constrained, you may wish to lower the number. Each file watch takes up 1080 bytes, so assuming that all 524,288 watches are consumed, that results in an upper bound of around 540 MiB.

## Zed

- Install: `flatpak install flathub dev.zed.Zed`
- Config path (Flatpak): `~/.var/app/dev.zed.Zed/config/zed/settings.json`
- For local AI setup, see [Local AI Model Setup for Zed](../environment/Local-AI-Model-Setup.md)

## IntelliJ

### Plugins

See dotfiles: [IntelliJ Plugins](https://github.com/BradNut/dotfiles/blob/master/intellij-plugins.md)
