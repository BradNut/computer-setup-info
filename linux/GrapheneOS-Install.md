# Graphene OS

## Install

- https://grapheneos.org/install/cli

## Obtaining fastboot

You need an updated copy of the `fastboot` tool and the directory containing it needs to be included in the `PATH` environment variable. You can run `fastboot --version` to determine the current version. It must be at least `29.0.6`. You can use a distribution package for this, but most of them mistakenly package development snapshots of fastboot, clobber the standard version scheme for platform-tools (adb, fastboot, etc.) with their own scheme and don't keep it up-to-date despite that being crucial.

On Arch Linux, install `android-tools` and skip the section below on using the standalone release of platform-tools from Android:

`sudo pacman -S android-tools`

Debian and Ubuntu do not have a usable package for fastboot. Their packages for these tools are both broken and many years out-of-date. Follow the instructions below for platforms without a proper package.

### Standalone platform-tools

If your operating system doesn't include a usable version of fastboot, you can use the official standalone releases of platform-tools. This is our recommendation for most users. The flashing process won't work unless you follow these instructions including setting up PATH.

To download, verify and extract the standalone platform-tools on Debian and Ubuntu:

```
sudo apt install libarchive-tools
curl -O https://dl.google.com/android/repository/platform-tools_r30.0.5-linux.zip
echo 'd6d72d006c03bd55d49b6cef9f00295db02f0a31da10e121427e1f4cb43e7cb9  platform-tools_r30.0.5-linux.zip' | sha256sum -c
bsdtar xvf platform-tools_r30.0.5-linux.zip
```

To download, verify and extract the standalone platform-tools on macOS:

```
curl -O https://dl.google.com/android/repository/eabcd8b4b7ab518c6af9c941af8494072f17ec4b.platform-tools_r30.0.5-darwin.zip
echo 'SHA256 (eabcd8b4b7ab518c6af9c941af8494072f17ec4b.platform-tools_r30.0.5-darwin.zip) = e5780bad71a53cf9d693e1053a0748f49e4a67cc1f71d16a94ab4c943af3345f' | shasum -c
tar xvf eabcd8b4b7ab518c6af9c941af8494072f17ec4b.platform-tools_r30.0.5-darwin.zip
```

To download, verify and extract the standalone platform-tools on Windows:

```
curl -O https://dl.google.com/android/repository/platform-tools_r30.0.5-windows.zip
(Get-FileHash platform-tools_r30.0.5-windows.zip).hash -eq "549ba2bdc31f335eb8a504f005f77606a479cc216d6b64a3e8b64c780003661f"
tar xvf platform-tools_r30.0.5-windows.zip
```

Next, add the tools to your `PATH` in the current shell so they can be used without referencing them by file path, enabling usage by the flashing script.

On Debian, Ubuntu and macOS:

`export PATH="$PWD/platform-tools:$PATH"`

On Windows:

`$env:Path = "$pwd\platform-tools;$env:Path"`
