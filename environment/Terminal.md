# Terminal

## Vim

- Configuration: [.vimrc](https://github.com/BradNut/dotfiles/blob/master/.vimrc)
- Install:
- Linux: `sudo apt install vim`
- OSX: `brew install vim`

### Things to look into for vim

- Package manager
- [Rainbow Parentheses](https://github.com/frazrepo/vim-rainbow)

## Zsh

_Currently using zsh_

- Install if not there
  - Linux/Ubuntu: `sudo apt install zsh`
  - OSX: `brew install zsh`

### Configuration

- [.zshrc](https://github.com/BradNut/dotfiles/blob/master/.zshrc)
- [Oh My Zsh](https://ohmyzsh.sh)
  -- Install: `sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`

#### Oh My Zsh Plugins

- [Z](https://github.com/agkozak/zsh-z)
  - Install: `git clone https://github.com/agkozak/zsh-z $ZSH_CUSTOM/plugins/zsh-z`
- [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
  - Install: `git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions`
- [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)
  - Install: `git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting`

## Bash

- Not using at the moment

### Configuration

- [Bash profile](https://github.com/BradNut/dotfiles/blob/master/.bash_profile)
- [.bashrc](https://github.com/BradNut/dotfiles/blob/master/.bashrc)

## SSH

### Enable

```
$ sudo apt update
$ sudo apt install openssh-server
```

Verify SSH is running:

```
$ sudo systemctl status ssh
```

### Generating SSH Keys

Step by step: [Generating New SSH Key and adding to the SSH Agent](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
