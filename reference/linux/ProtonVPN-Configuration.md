# Proton VPN on Linux

## Installation

The official Proton VPN Linux CLI is maintained by Proton. The latest installation instructions and repository setup are on [Proton's Linux support page](https://protonvpn.com/support/linux-vpn-setup). The CLI-specific guide is at [How to use the Proton VPN Linux CLI](https://protonvpn.com/support/linux-cli).

Source code: https://github.com/ProtonVPN/proton-vpn-cli

Notes:

- The CLI is officially supported on Debian, Ubuntu, and Fedora, and is also available on Arch Linux (official support for Arch is in progress).
- It requires `gnome-keyring` (KDE KWallet may work but is not officially supported).
- It does not currently work on headless setups.
- You cannot run the official Proton VPN Linux GUI app and the Linux CLI at the same time.

### Debian / Ubuntu

1. Add the official Proton VPN repository following steps 1 and 2 of Proton's distro-specific guide (linked above). If you already have the official GUI app installed, the repository is already configured.
2. Install the CLI:

   ```bash
   sudo apt install proton-vpn-cli
   ```

### Fedora

1. Add the official Proton VPN repository following steps 1 and 2 of Proton's Fedora guide. If the GUI app is already installed, the repository is already configured.
2. Install the CLI:

   ```bash
   sudo dnf install proton-vpn-cli
   ```

### Arch Linux

```bash
sudo pacman -S proton-vpn-cli
```

## Sign in

After installation, sign in with your Proton account credentials (not OpenVPN credentials):

```bash
protonvpn signin <username>
```

You will be prompted for your Proton password.

## Terminal Commands

| Command | Description |
| ------- | ----------- |
| `protonvpn signin <username>` | Sign in to your Proton VPN account. |
| `protonvpn signout` | Sign out of your Proton VPN account. |
| `protonvpn connect` or `protonvpn c` | Connect to the fastest VPN server. |
| `protonvpn connect --country <code>` | Connect to the fastest server in a country. |
| `protonvpn connect --city <city>` | Connect to the fastest server in a city. |
| `protonvpn connect <server name>` | Connect to a specific server. |
| `protonvpn reconnect` or `protonvpn r` | Reconnect or connect to the last server used. |
| `protonvpn disconnect` or `protonvpn d` | Disconnect the current session. |
| `protonvpn status` or `protonvpn s` | Print connection status. |
| `protonvpn config list` | Show current configuration settings. |
| `protonvpn config set <option> <setting>` | Change a configuration setting. |
| `protonvpn --version` | Display version. |
| `protonvpn --help` | Show help message. |

For an up-to-date list of available settings, run `protonvpn config list`.

## Kill Switch

The kill switch can be configured with the `protonvpn config set` command:

```bash
protonvpn config set kill-switch standard
```

To disable it:

```bash
protonvpn config set kill-switch off
```

## Update

The package manager will update the CLI along with other system packages. For example:

- Debian/Ubuntu: `sudo apt update && sudo apt upgrade`
- Fedora: `sudo dnf upgrade`
- Arch: `sudo pacman -Syu`

## Uninstall

Uninstall with the package manager you used to install it:

- Debian/Ubuntu: `sudo apt remove proton-vpn-cli`
- Fedora: `sudo dnf remove proton-vpn-cli`
- Arch: `sudo pacman -R proton-vpn-cli`
