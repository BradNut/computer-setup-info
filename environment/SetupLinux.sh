#!/bin/bash
set -euo pipefail
umask 022

if [[ ${EUID} -eq 0 ]]; then
  printf '%s\n' 'Run this script as your regular user, not root.' >&2
  exit 1
fi

. /etc/os-release
case "${ID}" in
  pop|ubuntu) ;;
  *)
    printf '%s\n' "Unsupported distribution: ${PRETTY_NAME}" >&2
    exit 1
    ;;
esac

sudo -v

sudo apt update
sudo apt install --yes \
  build-essential \
  ca-certificates \
  curl \
  file \
  flatpak \
  git \
  gnupg \
  gnupg-agent \
  jq \
  htop \
  lsb-release \
  openssh-server \
  pcscd \
  scdaemon \
  sshfs \
  vim \
  xclip \
  zsh

ensure_line() {
  local line="$1"
  local destination="$2"

  touch "${destination}"
  grep --fixed-strings --quiet --line-regexp "${line}" "${destination}" || printf '%s\n' "${line}" >> "${destination}"
}

download_file() {
  curl --fail --silent --show-error --location --proto '=https' --tlsv1.2 --retry 3 --output "$2" "$1"
}

run_installer() {
  local interpreter="$1"
  local url="$2"
  local installer
  local status

  shift 2
  installer="$(mktemp)"
  if ! download_file "${url}" "${installer}"; then
    rm --force "${installer}"
    return 1
  fi
  if "${interpreter}" "${installer}" "$@"; then
    status=0
  else
    status=$?
  fi
  rm --force "${installer}"
  return "${status}"
}

sudo -k

if [[ ! -d "${HOME}/.zim" ]]; then
  run_installer zsh https://raw.githubusercontent.com/zimfw/install/master/install.zsh
fi

if ! command -v zoxide >/dev/null; then
  run_installer sh https://raw.githubusercontent.com/ajeetdsouza/zoxide/main/install.sh
fi
ensure_line 'eval "$(zoxide init zsh)"' "${HOME}/.zshrc"

if ! command -v starship >/dev/null; then
  run_installer sh https://starship.rs/install.sh --yes
fi
ensure_line 'eval "$(starship init zsh)"' "${HOME}/.zshrc"

if ! command -v brew >/dev/null; then
  export NONINTERACTIVE=1
  run_installer /bin/bash https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh
  unset NONINTERACTIVE
fi

brew_bin="$(command -v brew || true)"
if [[ -z "${brew_bin}" ]]; then
  for candidate in "${HOME}/.linuxbrew/bin/brew" /home/linuxbrew/.linuxbrew/bin/brew; do
    if [[ -x "${candidate}" ]]; then
      brew_bin="${candidate}"
      break
    fi
  done
fi
if [[ -z "${brew_bin}" ]]; then
  printf '%s\n' 'Homebrew installation failed.' >&2
  exit 1
fi

brew_prefix="$("${brew_bin}" --prefix)"
ensure_line "eval \"\$(${brew_prefix}/bin/brew shellenv)\"" "${HOME}/.zprofile"
"${brew_bin}" install gcc

if [[ ! -s "${HOME}/.nvm/nvm.sh" ]]; then
  run_installer bash https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh
fi

export NVM_DIR="${HOME}/.nvm"
. "${NVM_DIR}/nvm.sh"
nvm install --lts
nvm alias default 'lts/*'

if ! command -v pnpm >/dev/null; then
  run_installer sh https://get.pnpm.io/install.sh
fi

export PNPM_HOME="${HOME}/.local/share/pnpm"
export PATH="${PNPM_HOME}:${PATH}"
npm install --global npm-check-updates tldr trash-cli

codename="${UBUNTU_CODENAME:-${VERSION_CODENAME}}"
sudo -v
sudo install --directory --mode=0755 /etc/apt/keyrings
sudo curl --fail --silent --show-error --location --proto '=https' --tlsv1.2 --retry 3 https://download.docker.com/linux/ubuntu/gpg --output /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
cat <<EOF | sudo tee /etc/apt/sources.list.d/docker.sources >/dev/null
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: ${codename}
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo curl --fail --silent --show-error --location --proto '=https' --tlsv1.2 --retry 3 https://repository.mullvad.net/deb/mullvad-keyring.asc --output /usr/share/keyrings/mullvad-keyring.asc
printf '%s\n' "deb [signed-by=/usr/share/keyrings/mullvad-keyring.asc arch=$(dpkg --print-architecture)] https://repository.mullvad.net/deb/stable stable main" | sudo tee /etc/apt/sources.list.d/mullvad.list >/dev/null

sudo curl --fail --silent --show-error --location --proto '=https' --tlsv1.2 --retry 3 https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg --output /usr/share/keyrings/brave-browser-archive-keyring.gpg
sudo curl --fail --silent --show-error --location --proto '=https' --tlsv1.2 --retry 3 https://brave-browser-apt-release.s3.brave.com/brave-browser.sources --output /etc/apt/sources.list.d/brave-browser-release.sources

curl --fail --silent --show-error --location --proto '=https' --tlsv1.2 --retry 3 https://updates.signal.org/desktop/apt/keys.asc | gpg --dearmor | sudo tee /usr/share/keyrings/signal-desktop-keyring.gpg >/dev/null
curl --fail --silent --show-error --location --proto '=https' --tlsv1.2 --retry 3 https://updates.signal.org/static/desktop/apt/signal-desktop.sources | sudo tee /etc/apt/sources.list.d/signal-desktop.sources >/dev/null

sudo curl --fail --silent --show-error --location --proto '=https' --tlsv1.2 --retry 3 https://download.sublimetext.com/sublimehq-pub.gpg --output /etc/apt/keyrings/sublimehq-pub.asc
cat <<'EOF' | sudo tee /etc/apt/sources.list.d/sublime-text.sources >/dev/null
Types: deb
URIs: https://download.sublimetext.com/
Suites: apt/stable/
Signed-By: /etc/apt/keyrings/sublimehq-pub.asc
EOF

# MEGAsync
meganz_key=$(mktemp)
download_file 'https://mega.nz/keys/MEGA_signing.key' "${meganz_key}"
gpg --batch --yes --dearmor < "${meganz_key}" | sudo tee /etc/apt/keyrings/meganz-archive-keyring.gpg >/dev/null
rm --force "${meganz_key}"
printf 'Types: deb\nURIs: https://mega.nz/linux/repo/xUbuntu_%s/\nSuites: ./\nSigned-By: /etc/apt/keyrings/meganz-archive-keyring.gpg\n' "${VERSION_ID}" | sudo tee /etc/apt/sources.list.d/megaio.sources >/dev/null

# Proton VPN
protonvpn_release_deb=$(mktemp --suffix=.deb)
download_file 'https://repo.protonvpn.com/debian/dists/stable/main/binary-all/protonvpn-stable-release_1.0.8_all.deb' "${protonvpn_release_deb}"
sudo dpkg -i "${protonvpn_release_deb}"
rm --force "${protonvpn_release_deb}"

sudo apt update
sudo apt install --yes \
  brave-browser \
  docker-buildx-plugin \
  docker-ce \
  docker-ce-cli \
  docker-compose-plugin \
  containerd.io \
  evolution \
  mullvad-browser \
  signal-desktop \
  sublime-text \
  megasync \
  proton-vpn-gnome-desktop

# Proton Pass (desktop app)
proton_pass_json=$(curl -fsSL https://proton.me/download/PassDesktop/linux/x64/version.json)
proton_pass_url=$(printf '%s' "${proton_pass_json}" | jq -r '.Releases[0].File[] | select(.Url | endswith(".deb")) | .Url')
proton_pass_sha512=$(printf '%s' "${proton_pass_json}" | jq -r '.Releases[0].File[] | select(.Url | endswith(".deb")) | .Sha512CheckSum')
proton_pass_deb=$(mktemp --suffix=.deb)
download_file "${proton_pass_url}" "${proton_pass_deb}"
printf '%s  %s\n' "${proton_pass_sha512}" "${proton_pass_deb}" | sha512sum --check -
sudo apt install --yes "${proton_pass_deb}"

# Proton Pass CLI
run_installer bash https://proton.me/download/pass-cli/install.sh

# ProtonMail Bridge
protonmail_bridge_deb=$(mktemp --suffix=.deb)
download_file 'https://proton.me/download/bridge/protonmail-bridge_3.22.0-1_amd64.deb' "${protonmail_bridge_deb}"
sudo apt install --yes "${protonmail_bridge_deb}"

sudo flatpak remote-add --if-not-exists --system flathub https://dl.flathub.org/repo/flathub.flatpakrepo
sudo flatpak install --system --noninteractive --or-update flathub \
  app.grayjay.Grayjay \
  best.ellie.StartupConfiguration \
  com.bitwarden.desktop \
  com.budgetwithbuckets.Buckets \
  com.calibre_ebook.calibre \
  com.jwestall.Forecast \
  com.obsproject.Studio \
  com.plexamp.Plexamp \
  com.redis.RedisInsight \
  com.usebruno.Bruno \
  com.yubico.yubioath \
  dev.deedles.Trayscale \
  dev.edfloreshz.Calculator \
  dev.edfloreshz.CosmicTweaks \
  dev.edfloreshz.Tasks \
  dev.mariinkys.Cedilla \
  dev.zed.Zed \
  fr.handbrake.ghb \
  io.dbeaver.DBeaverCommunity \
  io.github.cosmic_utils.camera \
  io.github.pixeldoted.cosmic-ext-color-picker \
  io.podman_desktop.PodmanDesktop \
  md.obsidian.Obsidian \
  net.cozic.joplin_desktop \
  one.jwr.interstellar \
  org.filezillaproject.Filezilla \
  org.gnome.Epiphany \
  org.qbittorrent.qBittorrent \
  org.shotcut.Shotcut \
  org.standardnotes.standardnotes \
  org.videolan.VLC \
  tv.plex.PlexDesktop \
  com.synology.SynologyDrive
