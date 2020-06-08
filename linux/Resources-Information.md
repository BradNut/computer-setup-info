# Linux Resources

## Useful Packages

- Gnome Tweaks: `sudo apt install gnome-tweaks`
- Fonts Fira Code: `sudo apt install fonts-firacode`
- Git: `sudo apt install git`
- Curl: `sudo apt install curl`
- Vim: `sudo apt install vim`

---

## GUI Setup

Ubuntu 20.04 Gnome dark mode work for all except do not disturb or right click menu

- Fix is that Gnome Shell is on "Default"
- Install Gnome Tweaks: `sudo apt install gnome-tweaks`
- Select "Appearance" and change Shell to "Yaru-dark" or whatever you want

---

## Gaming Mouse Support

- [Ratbagd DBus Daemon](https://github.com/libratbag/libratbag/blob/master/README.md#running-ratbagd-as-dbus-activated-systemd-service)
- [Piper GUI for Ratbagd](https://github.com/libratbag/piper)

---

## Laptop Power Saver

### TLP
Documentation: https://linrunner.de/tlp/index.html
Installation: https://linrunner.de/tlp/installation/index.html


---

## Trackpad Gestures
*Working on Dell XPS 13*

Following Medium article: [Mac-like Gestures on Ubuntu 20.04 Dell XPS 15](https://medium.com/@kaigo/mac-like-gestures-on-ubuntu-20-04-dell-xps-15-7ea6e3be7f76)

Add your user to the input group:
`sudo gpasswd -a $USER input`

Install dependencies:
`sudo apt-get install libinput-tools xdotool`

Install libinput gestures:
`git clone https://github.com/bulletmark/libinput-gestures.git`
`cd libinput-gestures`
`sudo make install`
`sudo ./libinput-gestures-setup install`

Start the software and allow it to run at startup.
`libinput-gestures-setup autostart`
`libinput-gestures-setup start`

Next install a UI tool to make adding and editing gestures easier.
`git clone https://gitlab.com/cunidev/gestures`
`cd gestures`
`sudo python3 setup.py install`

Open the new program called *‘gestures’* from your activities menu.

These are the gestures you will need to emulate a mac-like experience.

Configuration file in dotfiles: [Gestures.conf](https://github.com/BradNut/dotfiles/blob/master/Linux%20Settings/Gesture%20Settings/Gestures.conf)
- 3-finger swipe up
  - xdotool key super
- 3-finger swipe down
  - xdotool key Escape
- 3-finger swipe right
  - xdotool key 'ctrl+alt+Left'
- 3-finger swipe left
  - xdotool key 'ctrl+alt+Right'
- 3-finger pinch out
  - xdotool key 'ctrl+plus'
- 3-finger ping in
  - xdotool key 'ctrl+minus'
- 4-finger swipe left
  - xdotool key 'alt+Left'
- 4-finger swipe right
  - xdotool key 'alt+Right'

Next you may notice the workspaces are ontop of each other instead of side-by-side like MacOS. To fix this we will need to install a gnome extension named workspace matrix available [here](https://extensions.gnome.org/extension/1485/workspace-matrix/).

Now restart your system and you should be able to move workspaces, left and right using the three finger gesture or *ctrl+alt + left or right arrows*.

---

## Internal Hard Drives

- [Auto-mounting on boot](https://www.liberiangeek.net/2012/04/auto-mount-windows-ntfs-partitions-in-ubuntu-12-04-precise-pangolin/)

---

## Gaming

## Lutris

- https://www.linuxuprising.com/2018/09/how-to-use-lutris-to-play-windows-games.html

### Emulation

#### PS2

- https://forums.lutris.net/t/citra-and-pcsx2-runners-problem/8297
- https://forums.lutris.net/t/where-do-i-put-ps2-bios/4874
