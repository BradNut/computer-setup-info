# Coding Environment Setup

## Packages

- Git: `sudo apt install git`
- Curl: `sudo apt install curl`
- Docker: [Ubuntu Install](https://docs.docker.com/engine/install/ubuntu/#prerequisites)
  - [Install instructions](../master/linux/Docker-Setup.md)

### [Linux Brew](https://docs.brew.sh/Homebrew-on-Linux)

- Install: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`
- Run for Debian or Ubuntu: `sudo apt-get install build-essential curl file git`

#### Adding Homebrew to your PATH and bash shell (If applicable)

- `test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)`
- `test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)`
- If using bash: `test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.bash_profile`
- `echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile`

## Git

Edit .gitconfig with name and email
`git config --global.name "Your Name"`
`git config --global.email "you@example.com"`

## Dotfiles

Dotfiles and editor preferences: https://github.com/BradNut/dotfiles

## Terminal

### Vim

- If not installed: `sudo apt install vim`
- Configuration: [.vimrc](https://github.com/BradNut/dotfiles/blob/master/.vimrc)

#### Things to look into for vim

- Package manager
- [Rainbow Parentheses](https://github.com/frazrepo/vim-rainbow)

### Zsh

Currently using zsh.

- Install if not there: `sudo apt install zsh`

#### Configuration

- [.zshrc](https://github.com/BradNut/dotfiles/blob/master/.zshrc)
- [Oh My Zsh](https://ohmyzsh.sh)
  -- Install: `sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`

##### Oh My Zsh Plugins

- [Z](https://github.com/agkozak/zsh-z)
    * Install: `git clone https://github.com/agkozak/zsh-z $ZSH_CUSTOM/plugins/zsh-z`
- [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
    * Install: `git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions`
- [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)
    * Install: `git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting`

### Bash

- Not using at the moment

#### Configuration

- [Bash profile](https://github.com/BradNut/dotfiles/blob/master/.bash_profile)
- [.bashrc](https://github.com/BradNut/dotfiles/blob/master/.bashrc)
