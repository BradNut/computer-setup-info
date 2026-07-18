# Proton Bridge Setup

[Proton Mail Bridge](https://proton.me/mail/bridge) for Linux lets you use Proton Mail with IMAP/SMTP email clients such as Thunderbird and Evolution. A Proton Mail paid plan is required.

## Requirements

- 64-bit Linux (DEB, RPM, or PKGBUILD-based distribution)
- A secret-service password manager such as [GNOME Keyring](https://wiki.gnome.org/Projects/GnomeKeyring) or [Pass](https://www.passwordstore.org/)
- See the [official system requirements](https://proton.me/support/operating-systems-supported-bridge) for the current list of supported operating systems

## Installation

Download the appropriate package from the [Bridge homepage](https://proton.me/mail/bridge) or use the distribution-specific guides below.

### Debian/Ubuntu (DEB)

```bash
cd ~/Downloads
wget https://proton.me/download/bridge/protonmail-bridge_3.22.0-1_amd64.deb
sudo apt install ./protonmail-bridge_3.22.0-1_amd64.deb
```

Replace the version in the filename with the latest if necessary; Bridge auto-updates after launch.

### RPM-based (Fedora/RHEL/CentOS)

Follow the [RPM installation guide](https://proton.me/support/install-bridge-linux-rpm-file).

### Arch-based (PKGBUILD)

Follow the [PKGBUILD installation guide](https://proton.me/support/install-bridge-linux-pkgbuild-file).

### Verification

For security, verify the package after downloading: [Verifying the Proton Mail Bridge package for Linux](https://proton.me/support/verifying-bridge-package).

## Running and Updating

1. Launch `proton-mail` / `protonmail-bridge` from your applications menu.
2. Sign in with your Proton Mail account credentials.
3. Bridge runs a local IMAP/SMTP server and usually updates automatically; auto-update and autostart-on-login can be changed in the app settings.

## Thunderbird Configuration

1. In Thunderbird, disable the Account Hub (Menu → Settings → General → Account Hub → uncheck **Create accounts in the new Account Hub**).
2. Add a new account: Menu → New Account → Email.
3. Enter your name, email address, and the **Bridge mailbox password** shown in the Bridge app (not your regular Proton Mail password).
4. Thunderbird should detect the server settings automatically. If you use a custom domain, enter the IMAP/SMTP details shown in Bridge manually.
5. Accept the local security certificate exceptions when prompted for IMAP and SMTP.
6. To send from aliases, go to Account Settings → **Manage Identities** → **Add**.

Full Thunderbird guide: [Proton Mail Bridge Thunderbird setup guide](https://proton.me/support/protonmail-bridge-clients-windows-thunderbird).

## References

- [Bridge homepage](https://proton.me/mail/bridge)
- [Proton Mail Bridge for Linux support](https://proton.me/support/bridge-for-linux)
- [DEB installation guide](https://proton.me/support/installing-bridge-linux-deb-file)
- [RPM installation guide](https://proton.me/support/install-bridge-linux-rpm-file)
- [PKGBUILD installation guide](https://proton.me/support/install-bridge-linux-pkgbuild-file)
- [Package verification guide](https://proton.me/support/verifying-bridge-package)
- [Thunderbird setup guide](https://proton.me/support/protonmail-bridge-clients-windows-thunderbird)
