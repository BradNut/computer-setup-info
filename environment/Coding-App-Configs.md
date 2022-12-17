# Coding App Configs

## HyperJS

- [Configuration](https://github.com/BradNut/dotfiles/blob/master/.hyper.js)

## Sublime Text

- [Configuration](https://github.com/BradNut/dotfiles/blob/master/Preferences.sublime-settings)
- [Packages](https://github.com/BradNut/dotfiles/blob/master/sublime-text-extensions-i-use.md)

## VSCode

- Configuration: [settings.js](https://github.com/BradNut/dotfiles/blob/master/settings.json)
- Packages: https://github.com/BradNut/dotfiles/blob/master/vs-code-extensions-i-use.md
- Install Shell Command: Install `code` command in PATH

## IntelliJ

### Plugins

- [GitToolBox](https://plugins.jetbrains.com/plugin/7499-gittoolbox)
- [Kotlin](https://plugins.jetbrains.com/plugin/6954-kotlin)
- [Lombok](https://plugins.jetbrains.com/plugin/6317-lombok)
- [Material Theme UI](https://plugins.jetbrains.com/plugin/8006-material-theme-ui)
  - Using Material Darker
- [One Dark Theme](https://plugins.jetbrains.com/plugin/11938-one-dark-theme)
- [Prettier](https://plugins.jetbrains.com/plugin/10456-prettier)
- [Save Actions](https://plugins.jetbrains.com/plugin/7642-save-actions)
- [Sonar Lint](https://plugins.jetbrains.com/plugin/7973-sonarlint)
- [Svelte](https://plugins.jetbrains.com/plugin/12375-svelte)
- [Visual Studio Code Dark Plus Theme](https://plugins.jetbrains.com/plugin/12255-visual-studio-code-dark-plus-theme)

### Troubleshooting

#### Docs: https://code.visualstudio.com/docs/setup/linux#_visual-studio-code-is-unable-to-watch-for-file-changes-in-this-large-workspace-error-enospc

#### Visual Studio Code is unable to watch for file changes in this large workspace" (error ENOSPC)

_Follow these steps located [here](https://askubuntu.com/questions/776929/how-to-edit-my-etc-sysctl-conf-file)_
Steps:

1. You can add this line using nano or vim from terminal (ctrl+alt+t): `sudo nano /etc/sysctl.conf` or `sudo vim /etc/sysctl.conf`

   - Where you then scroll down and add the line by hand then press ctrl+x to end editing. You will be asked if you want to save, confirm that by pressing y and then once return to save.
   - _Same way you can reverse your changes._

2. You can add it as well this way: `echo "net.ipv4.icmp_echo_ignore_all=1" | sudo tee -a /etc/sysctl.conf`

   - For reversing this refer to solution 1.

---

Info from VSCode docs:

When you see this notification, it indicates that the VS Code file watcher is running out of handles because the workspace is large and contains many files. The current limit can be viewed by running:

`cat /proc/sys/fs/inotify/max_user_watches`

The limit can be increased to its maximum by editing /etc/sysctl.conf (except on Arch Linux, read below) and adding this line to the end of the file:

`fs.inotify.max_user_watches=524288`

The new value can then be loaded in by running sudo sysctl -p.

While 524,288 is the maximum number of files that can be watched, if you're in an environment that is particularly memory constrained, you may wish to lower the number. Each file watch takes up 1080 bytes, so assuming that all 524,288 watches are consumed, that results in an upper bound of around 540 MiB.
