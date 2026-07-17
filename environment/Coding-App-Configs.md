# Coding App Configs

## Sublime Text

- [Configuration](https://github.com/BradNut/dotfiles/blob/master/Preferences.sublime-settings)
- [Packages](https://github.com/BradNut/dotfiles/blob/master/sublime-text-extensions-i-use.md)

## VSCode

- **Configuration:** [settings.json](https://github.com/BradNut/dotfiles/blob/master/settings.json)
- **Packages:** [VS Code Extensions](https://github.com/BradNut/dotfiles/blob/master/vs-code-extensions-i-use.md)
- **Shell Command:** Install `code` in PATH

### VSCode Troubleshooting

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

While 524,288 is the maximum number of files that can be watched, if you're in an environment that is particularly memory constrained, you may wish to lower the number. Each file watch takes up 1080 bytes, so assuming that all 524,288 watches are consumed, that results in an upper bound of around 540 MiB.

## IntelliJ

### Plugins

See dotfiles: [IntelliJ Plugins](https://github.com/BradNut/dotfiles/blob/master/intellij-plugins.md)
