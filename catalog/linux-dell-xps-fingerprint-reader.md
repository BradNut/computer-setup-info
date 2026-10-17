---
id: linux-dell-xps-fingerprint-reader
title: Dell XPS fingerprint reader on Pop!_OS COSMIC
entry_points: linux
execution_mode: manual
status: current
supported: Dell XPS with Goodix 27c6:633c on Pop!_OS COSMIC
verified_on: 2026-10-16
source_docs: catalog/linux-dell-xps-fingerprint-reader.md
---

# Fingerprint login on Pop!_OS COSMIC (Dell XPS) — Runbook

Written 2026-10-16. Reconstructed from the setup sessions and the system's state at that time.

## Hardware / software
- Laptop: Dell XPS, Pop!_OS with COSMIC
- Reader: Goodix MOC Fingerprint Sensor, USB ID `27c6:633c`
- libfprint from the Pop!_OS repos (1.94.7) supports it; the `libfprint-2-tod1` package is also installed.

## Setup steps (what was done)
```bash
lsusb | grep -i 27c6                      # confirm the reader is visible
sudo apt install fprintd libpam-fprintd   # install the daemon and PAM module
fprintd-enroll                            # run as your normal user, not sudo; repeat the touch until enroll-completed
                                          # (specific finger: fprintd-enroll -f right-index-finger)
fprintd-verify                            # expect: verify-match
sudo pam-auth-update --enable fprintd     # adds pam_fprintd.so to /etc/pam.d/common-auth
sudo -k; sudo true                        # test: should ask for the finger, then fall back to password
```
- Enrolled finger: right index.
- COSMIC Settings has no fingerprint page, so enrollment is terminal-only.

## Optional GUI for enrollment (not yet tested)
[Enroll](https://github.com/cosmic-utils/enroll) is a community COSMIC-style app on Flathub. It registers, verifies and deletes prints per finger. It does not configure PAM, so you still use `pam-auth-update` for that.
```bash
flatpak install flathub org.cosmic_utils.enroll
flatpak run org.cosmic_utils.enroll
```
Untested with the Goodix reader or the Flatpak sandbox's access to `fprintd`. If it fails, use `fprintd-enroll` instead.

## Resulting PAM config (`/etc/pam.d/common-auth`)
```
auth [success=2 default=ignore] pam_fprintd.so max-tries=1 timeout=10
auth [success=1 default=ignore] pam_unix.so nullok try_first_pass
auth requisite pam_deny.so
auth required pam_permit.so
```
`sudo`, polkit and `/etc/pam.d/cosmic-greeter` all `@include common-auth`, so each asks for the finger first and falls through to the password.

## Known behaviour / problems
1. **Greeter shows only the fingerprint prompt.** The password prompt appears after about 10 s (`timeout=10`) or after one failed swipe (`max-tries=1`). Workaround reported upstream: submit an empty password to trigger the other method.
2. **Keyring is locked after a fingerprint login.** The keyring is encrypted with your password, and a fingerprint login never gives PAM the password. This is not specific to COSMIC. Logging in with the password unlocks it.

## Options for the greeter
1. Leave as is (fingerprint at the greeter, keyring password prompt after login).
2. **Recommended:** greeter password-only, fingerprint for sudo only.
   - Run `sudo pam-auth-update` and untick "Fingerprint authentication".
   - Add `auth sufficient pam_fprintd.so` near the top of `/etc/pam.d/sudo`.
   - Password login then unlocks the keyring.
3. Blank keyring password in Seahorse. Not recommended: secrets end up unencrypted on disk.

**Safety:** keep a spare TTY or root shell open while editing `/etc/pam.d`.

## Rollback
```bash
sudo pam-auth-update            # untick Fingerprint authentication
fprintd-delete "$USER"          # remove enrolled prints
sudo apt remove fprintd libpam-fprintd
```

## Upstream status (GitHub searched 2026-10-16)

**Settings page for fingerprint: requested, no plan from System76 visible.**
- [cosmic-settings#1396](https://github.com/pop-os/cosmic-settings/issues/1396) "Fingerprint Settings": open since 2025-09-25, no labels, no maintainer reply. Comments are +1s from Framework and ThinkPad users, plus a wish for one fingerprint use across disk unlock, login and keyring.
- [cosmic-settings PR#862](https://github.com/pop-os/cosmic-settings/pull/862) "feat: add fprint support": open, by a community contributor (Jan 2025), last updated 2025-02-14, no reviews. A maintainer said it needs design input, and the author raised security concerns about fingerprint login on Linux. It looks stalled.
- [cosmic-epoch#1365](https://github.com/pop-os/cosmic-epoch/issues/1365) and [#2405](https://github.com/pop-os/cosmic-epoch/issues/2405) "Add fingerprint sensor support": both closed (Oct–Nov 2025). Commenters say it works via PAM but still needs a GUI.

**Greeter and lock screen behaviour (open issues in pop-os/cosmic-greeter)**
- [#173](https://github.com/pop-os/cosmic-greeter/issues/173): password not accepted while the fingerprint prompt is active (your symptom). Related: [#413](https://github.com/pop-os/cosmic-greeter/issues/413) accept all login methods at once; [#429](https://github.com/pop-os/cosmic-greeter/issues/429) defaults to password after boot.
  - [PR #493](https://github.com/pop-os/cosmic-greeter/pull/493) restarts the PAM conversation after a timeout.
  - [PR #480](https://github.com/pop-os/cosmic-greeter/pull/480) is a draft for parallel password and fingerprint auth.
- Suspend/resume and reader races: [#538](https://github.com/pop-os/cosmic-greeter/issues/538), [#507](https://github.com/pop-os/cosmic-greeter/issues/507) (fprintd device claim race).
- Timeout and retries: [#99](https://github.com/pop-os/cosmic-greeter/issues/99) (timeout too short), [epoch#3131](https://github.com/pop-os/cosmic-epoch/issues/3131) (multiple attempts), [epoch#2519](https://github.com/pop-os/cosmic-epoch/issues/2519), [#547](https://github.com/pop-os/cosmic-greeter/issues/547) (delay PAM conversation until user interacts).
- [epoch#2719](https://github.com/pop-os/cosmic-epoch/issues/2719) (closed): stuck on lock screen after reboot when adding fingerprint support. Keep a TTY handy.
