# Environment Setup

## Coding Packages

- Git: `sudo apt install git`
- Curl: `sudo apt install curl`
- Docker: [Ubuntu Install](https://docs.docker.com/engine/install/ubuntu/#prerequisites)
  - [Install instructions](../master/linux/Docker-Setup.md)
- Gatsby CLI: `sudo npm install gatsby-cli -g`
- Heroku CLI: `sudo snap install --classic heroku`
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
- If using bash: `test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.bash_profile`
- `echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile`

#### List of installed casks

_NOTE: ZSH and plugins for Ubuntu should be manually installed and not from brew_

- nodeJS: `brew install node`
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
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```

## Terminal

- See details here: [Terminal Setup](../environment/Terminal.md)

## Caddy Server

Install: [Ubuntu/Debian/Raspbian](https://caddyserver.com/docs/install#debian-ubuntu-raspbian)

```
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo apt-key add -
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee -a /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
sudo apt install caddy
```

### Running Caddyfiles Directly

Disable the systemctl service: `sudo systemctl disable caddy`
Otherwise error of address in use for `:2019`

### If bind address in use error for port 443

Looks here: https://superuser.com/questions/710253/allow-non-root-process-to-bind-to-port-80-and-443/892391#892391

Option 1 which worked on PopOS: `sudo setcap CAP_NET_BIND_SERVICE=+eip $(which caddy)`

### Firewall

Possibly need to allow port `:443` and `:80` in Linux firewall
`sudo ufw allow 443/tcp`
`sudo ufw allow 80/tcp`

### NET::ERR_CERT_AUTHORITY_INVALID or SEC_ERROR_UNKNOWN_ISSUER Browser Errors

Pre-requisite for trust/untrust:

1. Install Java (Might not be needed, using SDKMan): `sdk install java`
2. Install certutil: `sudo apt install libss3-tools`

3. Run `caddy trust`
4. If still does not work then untrust and re-trust:

```
  caddy untrust && caddy trust
```

### Firefox Root Certs

Enable the about:config property `security.enterprise_roots.enabled` to true.
