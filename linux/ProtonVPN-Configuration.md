# Proton VPN Documentation on Linux
## Installation
Install docs: https://protonvpn.com/support/linux-vpn-tool/

Link to the GitHub repository – https://github.com/ProtonVPN/linux-cli

For more extensive information about the features and how to use the VPN client, read the Usage Guide.

You will need the latest updates of the following dependencies installed on your Linux repository:
- openvpn
- python3.5+
- dialog (optional, needed for interactive selection)
- pip for python3 (pip3)

## Instructions for installing these packages on different distributions:

### On Archlinux/ Manjaro, please use:

`sudo pacman -S openvpn dialog python-pip python-setuptools`

`sudo pip3 install protonvpn-cli`

Make sure to run pip as sudo, so it installs globally and recognizes the command with sudo

### On SUSE, please use:

`sudo zypper in -y openvpn dialog python3-pip python3-setuptools`

`sudo pip3 install protonvpn-cli`

### On Fedora / CentOS / RHEL, please use:

`sudo dnf install -y openvpn dialog python3-pip python3-setuptools`

`sudo pip3 install protonvpn-cli`

### On Debian / Ubuntu / Linux Mint and other derivatives, please use:

`sudo apt install -y openvpn dialog python3-pip python3-setuptools`

`sudo pip3 install protonvpn-cli`

### Manual installation from source

To perform a manual installation from source, visit the ProtonVPN Linux client project page on GitHub.
Initialization

Once you have installed the client, you will need to initialize your ProtonVPN profile so you can connect it to a VPN server. You can do this by using the sudo protonvpn init command. This will bring up the screen below.

## Initialization

Once you have installed the client, you will need to initialize your ProtonVPN profile so you can connect it to a VPN server. You can do this by using the `sudo protonvpn init` command. This will bring up the screen below.

When you are asked for your *Username* and *Password* on this screen, it is referring to your *OpenVPN credentials*, not your ProtonVPN login credentials.

Learn [how to find your OpenVPN credentials.](https://protonvpn.com/support/vpn-login/)

## Terminal Commands
List of all Commands
| Command |	Description |
| ----------- | ---------- |
| protonvpn init | Initialize ProtonVPN profile. |
| protonvpn connect, c | Select a ProtonVPN server and connect to it. |
| protonvpn c [servername] | Connect to a specified server. |
| protonvpn c -r | Connect to a random server. |
| protonvpn c -f | Connect to the fastest server. |
| protonvpn c --p2p | Connect to the fastest P2P server. |
| protonvpn c --cc [countrycode] | Connect to the fastest server in a specified country. |
| protonvpn c --sc | Connect to the fastest Secure Core server. |
| protonvpn reconnect, r | Reconnect or connect to the last server used. |
| protonvpn disconnect, d |	Disconnect the current session. |
| protonvpn status, s |	Print connection status. |
| protonvpn configure |	Change CLI configuration. |
| protonvpn refresh |	Refresh OpenVPN configuration and server data. |
| protonvpn examples | Print example commands. |
| protonvpn --version | Display version. |
| protonvpn --help | Show help message. |

All connect options can be used with the -p flag to explicitly specify which transmission protocol is used for that connection (either udp or tcp).
Kill Switch

ProtonVPN-CLI has a built-in Kill Switch that protects your data in case your VPN connection is interrupted or cut unexpectedly.

## Enabling Kill Switch

To enable Kill Switch, open the configuration menu with protonvpn configure, then select 5 for Kill Switch and confirm the activation with either 1 or 2, depending on your preference.

1 will block access from your directly connected network (e.g. public WiFi) and is recommended for laptops that may connect to untrusted networks.

2 will allow access from your directly connected network and is for computers that don’t leave a secure and trusted LAN, like your home network.

On the next connection Kill Switch will be enabled.

## Update

We will periodically update the ProtonVPN-CLI to deal with bugs or to introduce new features.

The command to update ProtonVPN-CLI is: sudo pip3 install protonvpn-cli --upgrade.

## Uninstall

If you want to uninstall ProtonVPN-CLI, run configure first and purge the configuration. Then uninstall through the package manager you used for installation.

For PIP this would be:
`sudo pip3 uninstall protonvpn-cli`