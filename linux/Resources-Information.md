# Linux Resources

---

## Dual Booting

https://support.system76.com/articles/dual-booting/

### Fixes

#### Fix your clock

Windows and Linux store their time in the BIOS differently, this will cause your clock to be desynchronized when you switch from one OS to the other.

The easiest solution for it is to fix it in Linux, forcing it to work the same way as Windows. You can do this through the terminal:

`timedatectl set-local-rtc 1 --adjust-system-clock`

You can verify if the change has been successful, by running this command:

`timedatectl`

You should see RTC in local TZ: yes. If you need to revert it, just set it to 0:

`timedatectl set-local-rtc 0 --adjust-system-clock`

---

## Useful Packages

- NTFS support: `sudo apt install ntfs-3g`
- Fonts Fira Code: `sudo apt install fonts-firacode`
- Git: `sudo apt install git`
- Curl: `sudo apt install curl`
- Vim: `sudo apt install vim`

---

## Useful Shortcuts

- Open launcher: Super (Windows) key, or Super+/
- Open app library: Super+A
- Open workspace overview: Super+W
- Switch windows: Alt+Tab / Alt+Shift+Tab
- Move/resize focus: Super+Arrows
- Move windows: Super+Shift+Arrows

---

## Gaming Mouse Support

- [Ratbagd DBus Daemon](https://github.com/libratbag/libratbag/blob/master/README.md#running-ratbagd-as-dbus-activated-systemd-service)
- [Piper GUI for Ratbagd](https://github.com/libratbag/piper)

---

## Internal Hard Drives

Internal drives may not auto-mount in COSMIC. For persistent mounts, use `/etc/fstab`:

1. Find the partition UUID:

   ```bash
   lsblk -f
   ```

2. Create a mount point:

   ```bash
   sudo mkdir -p /mnt/<name>
   ```

3. Add a line to `/etc/fstab` (use `ntfs-3g` for NTFS partitions):

   ```fstab
   UUID=<uuid> /mnt/<name> ntfs-3g defaults,uid=$USER,gid=$USER,umask=022 0 0
   ```

4. Test the mount:

   ```bash
   sudo mount -a
   ```

For NTFS dirty-flag or mounting issues, see [COSMIC Files issue #889](https://github.com/pop-os/cosmic-files/issues/889).

---

## Gaming

### Lutris

Install Lutris from the COSMIC Store, as a [Flatpak](https://lutris.net/downloads), or via the [official Lutris instructions](https://lutris.net/downloads).

### Emulation

Use current Flatpak releases or the COSMIC Store instead of old Lutris runner threads. For example:

- PS2: [PCSX2](https://pcsx2.net/downloads/)
