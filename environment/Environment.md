# Environment Setup

This guide summarizes the core Linux development environment. The canonical automated installer is [SetupLinux.sh](./SetupLinux.sh); run it on a fresh Ubuntu/Pop!_OS machine and then finish the manual steps below.

For platform-specific notes see [Linux Environment Setup](../linux/Environment-Setup.md) and [Terminal Setup](./Terminal.md).

## What the automated setup installs

- Base apt packages such as `build-essential`, `git`, `curl`, `vim`, `zsh`, `jq`, `htop`, and `openssh-server`
- Shell customizations: [zimfw](https://github.com/zsh-users/zimfw), [zoxide](https://github.com/ajeetdsouza/zoxide), and [Starship](https://starship.rs/)
- Node via [nvm](https://github.com/nvm-sh/nvm) (LTS), [pnpm](https://pnpm.io/installation), plus `npm-check-updates`, `tldr`, and `trash-cli`
- [Docker Engine and Compose plugins](https://docs.docker.com/engine/install/ubuntu/) — see [Docker Setup](../linux/Docker-Setup.md)
- [Homebrew on Linux](https://docs.brew.sh/Homebrew-on-Linux) (used for `gcc` and other formulae)
- Third-party repositories: Brave, Mullvad, Signal, Sublime Text, MEGAsync, Proton VPN, Proton Pass, and ProtonMail Bridge
- Flatpak apps from Flathub

## Dotfiles

Editor preferences and shell dotfiles live in <https://github.com/BradNut/dotfiles>.

## Git

Configure your Git identity after installation:

```sh
$ git config --global user.name "Your Name"
$ git config --global user.email "you@example.com"
```

## Terminal

See [Terminal Setup](./Terminal.md) for shell, prompt, SSH, and related configuration.
