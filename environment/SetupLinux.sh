#!/bin/bash
set -ex

# Ensure repositories are enabled
sudo add-apt-repository universe
sudo add-apt-repository multiverse
sudo add-apt-repository restricted

# Add dell drivers for focal fossa XPS 13

sudo sh -c 'cat > /etc/apt/sources.list.d/focal-dell.list << EOF
deb http://dell.archive.canonical.com/updates/ focal-dell public
# deb-src http://dell.archive.canonical.com/updates/ focal-dell public

deb http://dell.archive.canonical.com/updates/ focal-oem public
# deb-src http://dell.archive.canonical.com/updates/ focal-oem public

deb http://dell.archive.canonical.com/updates/ focal-somerville public
# deb-src http://dell.archive.canonical.com/updates/ focal-somerville public

deb http://dell.archive.canonical.com/updates/ focal-somerville-melisa public
# deb-src http://dell.archive.canonical.com/updates focal-somerville-melisa public
EOF'

sudo apt update -qq

# Install general utilities
sudo apt install git curl xclip htop openssh-server sshfs vim neofetch file gnome-tweaks

sudo apt autoremove

# Setup Development tools

## Add build essentials
sudo apt install build-essential -y

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Install SDK Man
curl -s "https://get.sdkman.io" | bash

# Install ZSH
sudo apt install zsh

# Install zimfw
echo "Check if zimfw is installed"
if [ -d "$HOME/.zim" ]; then
  echo "zimfw is already installed"
else
  echo "Installing zimfw"
  curl -fsSL https://raw.githubusercontent.com/zimfw/install/master/install.zsh | zsh
fi

# Install Linux Brew
echo "Check if brew is installed"
if which brew >/dev/nul; then
  echo "brew is already installed"
else
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
  # Add Homebrew to your PATH in /home/bshellnu/.profile:
  echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> /home/bshellnu/.profile
  eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
  test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
  test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
  test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.bash_profile
  echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile
  brew install gcc
fi

# Install NVM
echo "Check if nvm is installed"
if [ -d "$HOME/.nvm" ]; then
  echo "nvm is already installed"
else
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
fi

# Install Node Versions
if command -v nvm >/dev/null; then
  echo "Installing LTS Node Version"
  nvm install --lts
  nvm use --lts
fi

source ~/.zshrc

# Install NPM Utilities
npm install -g npm-check-updates
npm install -g tldr
npm install -g trash-cli

# Docker
echo "Checking if docker is installed"
if command -v docker >/dev/null; then
  echo "Docker is already installed"
else
  # Add Docker's official GPG key:
  sudo apt-get update
  sudo apt-get install ca-certificates curl
  sudo install -m 0755 -d /etc/apt/keyrings
  sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
  sudo chmod a+r /etc/apt/keyrings/docker.asc

  # Add the repository to Apt sources:
  echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  sudo apt-get update
  sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
fi

# Install Applications

## Coding

### Node Version Manager
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

## Browser
sudo apt install curl
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list
sudo apt update
sudo apt install brave-browser

## Multimedia
flatpak install flathub com.plexamp.Plexamp

## Mail
sudo apt-get install evolution

## Social
### Signal
# 1. Install our official public software signing key:
wget -O- https://updates.signal.org/desktop/apt/keys.asc | gpg --dearmor > signal-desktop-keyring.gpg
cat signal-desktop-keyring.gpg | sudo tee /usr/share/keyrings/signal-desktop-keyring.gpg > /dev/null

# 2. Add our repository to your list of repositories:
echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/signal-desktop-keyring.gpg] https://updates.signal.org/desktop/apt xenial main' |\
  sudo tee /etc/apt/sources.list.d/signal-xenial.list

# 3. Update your package database and install Signal:
sudo apt update && sudo apt install signal-desktop

## Others
flatpak install flathub com.anydesk.Anydesk
flatpak install flathub com.bitwarden.desktop
flatpak install flathub org.filezillaproject.Filezilla
flatpak install flathub org.qbittorrent.qBittorrent

# Yubico
flatpak install flathub com.yubico.yubioath
sudo apt update && sudo apt install -y gnupg2 gnupg-agent scdaemon pcscd

# Sublime Text
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt-get install apt-transport-https
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list


# VS Codium
## Install https://vscodium.com/#install
wget -qO - https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/-/raw/master/pub.gpg | gpg --dearmor | sudo dd of=/etc/apt/trusted.gpg.d/vscodium.gpg
echo 'deb https://paulcarroty.gitlab.io/vscodium-deb-rpm-repo/debs/ vscodium main' | sudo tee --append /etc/apt/sources.list.d/vscodium.list
sudo apt update && sudo apt install codium

## VSCode Extensions

### Auto Complete

codium --install-extension formulahendry.auto-close-tag
codium --install-extension formulahendry.auto-rename-tag

### Debuggers

codium --install-extension msjsdiag.debugger-for-chrome

### Formaters

codium --install-extension aaron-bond.better-comments
codium --install-extension tombonnike.vscode-status-bar-format-toggle
codium --install-extension esbenp.prettier-vscode

### Icons

codium --install-extension vscode-icons-team.vscode-icons

### Linters

codium --install-extension streetsidesoftware.code-spell-checker
codium --install-extension dbaeumer.vscode-eslint

### Other

codium --install-extension CoenraadS.bracket-pair-colorizer-2
codium --install-extension naumovs.color-highlight
codium --install-extension donjayamanne.githistory
codium --install-extension wix.vscode-import-cost
codium --install-extension Orta.vscode-jest
codium --install-extension christian-kohler.npm-intellisense
codium --install-extension techer.open-in-browser
codium --install-extension christian-kohler.path-intellisense
codium --install-extension 2gua.rainbow-brackets
codium --install-extension siegebell.scope-info
codium --install-extension ardenivanov.svelte-intellisense

### Programming Languages

codium --install-extension PeterJausovec.vscode-docker
codium --install-extension mikestead.dotenv
codium --install-extension Prisma.vscode-graphql
codium --install-extension Prisma.prisma
codium --install-extension mechatroner.rainbow-csv
codium --install-extension mrmlnc.vscode-scss
codium --install-extension svelte.svelte-vscode
codium --install-extension jpoissonnier.vscode-styled-components
codium --install-extension redhat.vscode-yaml

### Snippets

codium --install-extension dsznajder.es7-react-js-snippets
codium --install-extension kumar-harsh.graphql-for-vscode
codium --install-extension fivethree.vscode-svelte-snippets

### Themes

codium --install-extension teabyii.ayu
codium --install-extension wesbos.theme-cobalt2
codium --install-extension Loader be5invis.vscode-custom-css
codium --install-extension RobbOwen.synthwave-vscode

# Gotta reboot now:
sudo apt update -qq && sudo apt upgrade -y && sudo apt autoremove -y

echo $'\n'$"Ready for REBOOT"
