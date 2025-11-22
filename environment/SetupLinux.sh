#!/bin/bash
set -ex

# Ensure repositories are enabled
sudo add-apt-repository universe
sudo add-apt-repository multiverse
sudo add-apt-repository restricted

# Add Dell drivers for jammy jellyfish XPS 13
sudo mkdir -p /usr/share/keyrings
curl -fsSL 'https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xF9FDA6BED73CDC22' \
  | gpg --dearmor \
  | sudo tee /usr/share/keyrings/canonical-archive-keyring.gpg >/dev/null
curl -fsSL 'https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xD4D1EAED36962F69' \
  | gpg --dearmor \
  | sudo tee -a /usr/share/keyrings/canonical-archive-keyring.gpg >/dev/null

sudo sh -c 'cat > /etc/apt/sources.list.d/jammy-dell.list << EOF
# deb [signed-by=/usr/share/keyrings/canonical-archive-keyring.gpg] http://dell.archive.canonical.com/updates/ jammy public
deb [signed-by=/usr/share/keyrings/canonical-archive-keyring.gpg] http://dell.archive.canonical.com/updates/ jammy-oem public
deb [signed-by=/usr/share/keyrings/canonical-archive-keyring.gpg] http://dell.archive.canonical.com/updates/ jammy-somerville public
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
# curl -s "https://get.sdkman.io" | bash

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

# Install starship.rs
curl -sS https://starship.rs/install.sh | sh

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

# Install PNPM
curl -fsSL https://get.pnpm.io/install.sh | sh -

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
  sudo apt update
  sudo apt install ca-certificates curl
  sudo install -m 0755 -d /etc/apt/keyrings
  sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
  sudo chmod a+r /etc/apt/keyrings/docker.asc

  # Add the repository to Apt sources:
  sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF

  sudo apt update
  sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
fi

# Install Applications

## Coding

## Browser

### Mullvad

#### Download the Mullvad signing key
sudo curl -fsSLo /usr/share/keyrings/mullvad-keyring.asc https://repository.mullvad.net/deb/mullvad-keyring.asc

#### Add the Mullvad repository server to apt
echo "deb [signed-by=/usr/share/keyrings/mullvad-keyring.asc arch=$( dpkg --print-architecture )] https://repository.mullvad.net/deb/stable stable main" | sudo tee /etc/apt/sources.list.d/mullvad.list

#### Install the package
sudo apt update
sudo apt install mullvad-browser

### Brave
sudo apt install curl

sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg

sudo curl -fsSLo /etc/apt/sources.list.d/brave-browser-release.sources https://brave-browser-apt-release.s3.brave.com/brave-browser.sources

sudo apt update

sudo apt install brave-browser

## Multimedia
flatpak install flathub com.plexamp.Plexamp

## Mail
sudo apt install evolution

## Social
### Signal
#### NOTE: These instructions only work for 64-bit Debian-based
#### Linux distributions such as Ubuntu, Mint etc.

#### 1. Install our official public software signing key:
wget -O- https://updates.signal.org/desktop/apt/keys.asc | gpg --dearmor > signal-desktop-keyring.gpg;
cat signal-desktop-keyring.gpg | sudo tee /usr/share/keyrings/signal-desktop-keyring.gpg > /dev/null

#### 2. Add our repository to your list of repositories:
wget -O signal-desktop.sources https://updates.signal.org/static/desktop/apt/signal-desktop.sources;
cat signal-desktop.sources | sudo tee /etc/apt/sources.list.d/signal-desktop.sources > /dev/null

#### 3. Update your package database and install Signal:
sudo apt update && sudo apt install signal-desktop

## Others
flatpak install flathub com.bitwarden.desktop
flatpak install flathub org.filezillaproject.Filezilla
flatpak install flathub org.qbittorrent.qBittorrent
flatpak install flathub org.shotcut.Shotcut
flatpak install flathub fr.handbrake.ghb
flatpak install flathub com.obsproject.Studio
flatpak install flathub org.videolan.VLC
flatpak install flathub md.obsidian.Obsidian
flatpak install flathub tv.plex.PlexDesktop
flatpak install flathub com.calibre_ebook.calibre
flatpak install flathub org.gnome.Epiphany
flatpak install flathub dev.deedles.Trayscale

# Yubico
flatpak install flathub com.yubico.yubioath
sudo apt update && sudo apt install -y gnupg2 gnupg-agent scdaemon pcscd

# Sublime Text
wget -qO- https://download.sublimetext.com/sublimehq-pub.gpg \
  | gpg --dearmor \
  | sudo tee /usr/share/keyrings/sublimehq-archive-keyring.gpg >/dev/null

sudo apt-get install apt-transport-https
echo "deb [signed-by=/usr/share/keyrings/sublimehq-archive-keyring.gpg] https://download.sublimetext.com/ apt/stable/" \
  | sudo tee /etc/apt/sources.list.d/sublime-text.list


# VS Codium

## VSCode Extensions

### Auto Complete

# codium --install-extension formulahendry.auto-close-tag
# codium --install-extension formulahendry.auto-rename-tag

### Debuggers

# codium --install-extension msjsdiag.debugger-for-chrome

### Formaters

# codium --install-extension aaron-bond.better-comments
# codium --install-extension tombonnike.vscode-status-bar-format-toggle
# codium --install-extension esbenp.prettier-vscode

### Icons

# codium --install-extension vscode-icons-team.vscode-icons

### Linters

# codium --install-extension streetsidesoftware.code-spell-checker
# codium --install-extension dbaeumer.vscode-eslint

### Other

# codium --install-extension CoenraadS.bracket-pair-colorizer-2
# codium --install-extension naumovs.color-highlight
# codium --install-extension donjayamanne.githistory
# codium --install-extension wix.vscode-import-cost
# codium --install-extension Orta.vscode-jest
# codium --install-extension christian-kohler.npm-intellisense
# codium --install-extension techer.open-in-browser
# codium --install-extension christian-kohler.path-intellisense
# codium --install-extension 2gua.rainbow-brackets
# codium --install-extension siegebell.scope-info
# codium --install-extension ardenivanov.svelte-intellisense

### Programming Languages

# codium --install-extension PeterJausovec.vscode-docker
# codium --install-extension mikestead.dotenv
# codium --install-extension Prisma.vscode-graphql
# codium --install-extension Prisma.prisma
# codium --install-extension mechatroner.rainbow-csv
# codium --install-extension mrmlnc.vscode-scss
# codium --install-extension svelte.svelte-vscode
# codium --install-extension jpoissonnier.vscode-styled-components
# codium --install-extension redhat.vscode-yaml

### Snippets

# codium --install-extension dsznajder.es7-react-js-snippets
# codium --install-extension kumar-harsh.graphql-for-vscode
# codium --install-extension fivethree.vscode-svelte-snippets

### Themes

# codium --install-extension teabyii.ayu
# codium --install-extension wesbos.theme-cobalt2
# codium --install-extension Loader be5invis.vscode-custom-css
# codium --install-extension RobbOwen.synthwave-vscode

# Gotta reboot now:
sudo apt update -qq && sudo apt upgrade -y && sudo apt autoremove -y

echo $'\n'$"Ready for REBOOT"
