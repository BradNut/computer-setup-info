# Environment

## Coding Packages

- Git: `sudo apt install git`
- Curl: `sudo apt install curl`
- Docker: [Ubuntu Install](https://docs.docker.com/engine/install/ubuntu/#prerequisites)
  - [Install instructions](../master/linux/Docker-Setup.md)
- [Node Version Manager](https://github.com/nvm-sh/nvm#set-default-node-version)
  - `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash`
  - Use `.nvmrc` from [Dotfiles](../master/linux/Environment-Setup.md#environment-setup##dot-files)
  - Useful install LTS: `nvm install --lts`
- Gatsby CLI: `sudo npm install gatsby-cli -g`
- Heroku CLI: `sudo snap install --classic heroku`
- [PNPM](https://pnpm.io/installation)
  - NPM Install: `npm install -g pnpm`
- Vim: `sudo apt install vim`
- Sanity CLI: `sudo npm install @sanity/cli -g`

## Useful System Packages

- [Neofetch](https://github.com/dylanaraps/neofetch)
  - `sudo apt install neofetch`
- [NPM Check Updates](https://www.npmjs.com/package/npm-check-updates)
- [TLDR Man Pages](https://tldr.sh/)
- [Trash-CLI](https://www.npmjs.com/package/trash-cli)

## [Linux Brew](https://docs.brew.sh/Homebrew-on-Linux)

- Install: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`
- Run for Debian or Ubuntu: `sudo apt-get install build-essential curl file git`

#### Adding Homebrew to your PATH and bash shell (If applicable)

- `test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)`
- `test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)`
- If using bash: `test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >> ~/.bash_profile`
- `echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile`

#### List of installed casks

_NOTE: ZSH and plugins for Ubuntu should be manually installed and not from brew_

_NodeJS: Use Node Version Manager_

- NodeJS: *Use Node Version Manager instead*
- postresql: `brew install postgresql`
- sshpass: `brew install hudochenkov/sshpass/sshpass`
- tmux: `brew install tmux`
- zsh: `brew install zsh`
- zsh-autosuggestions: `brew install zsh-autosuggestions`
- zsh-syntax-highlighting: `brew install zsh-syntax-highlighting`

## Dotfiles

Dotfiles and editor preferences: https://github.com/BradNut/dotfiles

## Git

Edit `.gitconfig` with name and email

```
$ git config --global.name "Your Name"
$ git config --global.email "you@example.com"
```

## Terminal

- See details here: [Terminal Setup](../environment/Terminal.md)
