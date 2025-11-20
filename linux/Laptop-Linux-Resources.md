# Setup Dell XPS 13 PopOS/Ubuntu

## Install Dell Drivers

```
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
```

Clean setup of PopOS resources:

```
#!/bin/bash
set -ex

# Add dell drivers for focal fossa

sudo sh -c 'cat > /etc/apt/sources.list.d/focal-dell.list << EOF
deb http://dell.archive.canonical.com/updates/ focal-dell public
# deb-src http://dell.archive.canonical.com/updates/ focal-dell public

deb http://dell.archive.canonical.com/updates/ focal-oem public
# deb-src http://dell.archive.canonical.com/updates/ focal-oem public
EOF'

sudo apt update -q

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
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/agkozak/zsh-z $ZSH_CUSTOM/plugins/zsh-z
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# Install Linux Brew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
# Add Homebrew to your PATH in /home/bshellnu/.profile:
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> /home/bshellnu/.profile
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
# Run `brew help` to get started
sudo apt-get install build-essential
brew install gcc

test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.bash_profile
echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile

# Install Casks
brew install node
brew install postgresql
brew install hudochenkov/sshpass/sshpass

# Install NPM Utilities
npm install -g npm-check-updates
npm install -g tldr
npm install --global trash-cli

# Install Battery Life Improvements https://support.system76.com/articles/battery/
sudo apt install tlp tlp-rdw --no-install-recommends

# Install trackpad gestures
mkdir trackpad-gestures
cd trackpad-gestures
sudo gpasswd -a $USER input
sudo apt-get install libinput-tools xdotool
git clone https://github.com/bulletmark/libinput-gestures.git
cd libinput-gestures
sudo make install
sudo ./libinput-gestures-setup install
libinput-gestures-setup autostart
libinput-gestures-setup start
cd ..

## Install UI tool
flatpak install flathub com.gitlab.cunidev.Gestures

# Docker
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get update
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

# CLIs
npm install gatsby-cli -g
# sudo apt install snapd
# sudo snap install --classic heroku
npm install @sanity/cli -g

# Install fonts
sudo apt install fonts-firacode fonts-open-sans -y -q

# Install Applications

## Coding
flatpak install flathub io.dbeaver.DBeaverCommunity

## Browser
sudo apt install apt-transport-https curl
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list
sudo apt update
sudo apt install brave-browser

## Chat
sudo flatpak install discord -y

## Multimedia
sudo apt install -y gimp
flatpak install flathub com.plexamp.Plexamp

## Mail
sudo apt-get install evolution

## Social
flatpak install flathub uk.co.ibboard.cawbird
flatpak install flathub com.github.bleakgrey.tootle
flatpak install flathub org.signal.Signal

## Others
flatpak install flathub com.anydesk.Anydesk
flatpak install flathub com.bitwarden.desktop
flatpak install flathub org.filezillaproject.Filezilla
flatpak install flathub com.getpostman.Postman
flatpak install flathub org.qbittorrent.qBittorrent
flatpak install flathub org.standardnotes.standardnotes

# Yubico
flatpak install flathub com.yubico.yubioath
sudo apt update && sudo apt install -y gnupg2 gnupg-agent scdaemon pcscd

# Sublime Text
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt-get install apt-transport-https
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

# VSCode Extensions

## Auto Complete

code --install-extension formulahendry.auto-close-tag
code --install-extension formulahendry.auto-rename-tag

## Debuggers

code --install-extension msjsdiag.debugger-for-chrome

## Formaters

code --install-extension aaron-bond.better-comments
code --install-extension tombonnike.vscode-status-bar-format-toggle
code --install-extension esbenp.prettier-vscode

## Icons

code --install-extension vscode-icons-team.vscode-icons

## Linters

code --install-extension streetsidesoftware.code-spell-checker
code --install-extension dbaeumer.vscode-eslint

## Other

code --install-extension CoenraadS.bracket-pair-colorizer-2
code --install-extension naumovs.color-highlight
code --install-extension donjayamanne.githistory
code --install-extension wix.vscode-import-cost
code --install-extension Orta.vscode-jest
code --install-extension christian-kohler.npm-intellisense
code --install-extension techer.open-in-browser
code --install-extension christian-kohler.path-intellisense
code --install-extension 2gua.rainbow-brackets
code --install-extension siegebell.scope-info
code --install-extension ardenivanov.svelte-intellisense

## Programming Languages

code --install-extension PeterJausovec.vscode-docker
code --install-extension mikestead.dotenv
code --install-extension Prisma.vscode-graphql
code --install-extension Prisma.prisma
code --install-extension mechatroner.rainbow-csv
code --install-extension mrmlnc.vscode-scss
code --install-extension svelte.svelte-vscode
code --install-extension jpoissonnier.vscode-styled-components
code --install-extension redhat.vscode-yaml

## Snippets

code --install-extension dsznajder.es7-react-js-snippets
code --install-extension kumar-harsh.graphql-for-vscode
code --install-extension fivethree.vscode-svelte-snippets

## Themes

code --install-extension teabyii.ayu
code --install-extension wesbos.theme-cobalt2
code --install-extension Loader be5invis.vscode-custom-css
code --install-extension RobbOwen.synthwave-vscode

# Gotta reboot now:
sudo apt update -qq && sudo apt upgrade -y && sudo apt autoremove -y

echo $'\n'$"Ready for REBOOT"
```

Reference bash script here: https://github.com/jules-ch/Ubuntu20-Setup-XPS13/blob/master/setup.sh
