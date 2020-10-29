# Coding Applications

## Sublime Text 3

- [Install](https://flathub.org/apps/details/com.sublimetext.three): `flatpak install flathub com.sublimetext.three`
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

- Configuration: [settings.js](https://github.com/BradNut/dotfiles/blob/master/settings.json)
- Packages installed: https://github.com/BradNut/dotfiles/blob/master/vs-code-extensions-i-use.md
- Install Shell Command: Install ‘code’ command in PATH

### Troubleshooting

#### Visual Studio Code is unable to watch for file changes in this large workspace" (error ENOSPC)

When you see this notification, it indicates that the VS Code file watcher is running out of handles because the workspace is large and contains many files. The current limit can be viewed by running:

`cat /proc/sys/fs/inotify/max_user_watches`

The limit can be increased to its maximum by editing /etc/sysctl.conf (except on Arch Linux, read below) and adding this line to the end of the file:

`fs.inotify.max_user_watches=524288`

The new value can then be loaded in by running sudo sysctl -p.

While 524,288 is the maximum number of files that can be watched, if you're in an environment that is particularly memory constrained, you may wish to lower the number. Each file watch takes up 1080 bytes, so assuming that all 524,288 watches are consumed, that results in an upper bound of around 540 MiB.
