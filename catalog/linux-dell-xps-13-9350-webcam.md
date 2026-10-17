---
id: linux-dell-xps-13-9350-webcam
title: Dell XPS 13 9350 webcam on Pop!_OS COSMIC
entry_points: linux
execution_mode: manual
status: current
supported: Dell XPS 13 9350 (Lunar Lake) on Pop!_OS 24.04 COSMIC
verified_on: 2026-10-16
source_docs: catalog/linux-dell-xps-13-9350-webcam.md
---

# Dell XPS 13 9350 webcam on Pop!_OS COSMIC: runbook

Written 2026-10-16. Hardware: Dell XPS 13 9350 (Lunar Lake), OV02C10 sensor behind an Intel IPU7.
Kernel at the time: 7.2.6-76070206-generic. Pop!_OS 24.04 base.

## Summary: how the camera works now

The camera is a raw sensor, so everything goes through libcamera's software ISP. Two paths exist:

```
OV02C10 -> IPU7 kernel driver -> libcamera 0.7 (/usr/local, software ISP)
              |-> PipeWire libcamera plugin -> PipeWire apps (Snapshot, browsers)
              |-> Flatpak apps with their own bundled libcamera (Cosmic camera app)
              '-> PipeWire -> v4l2loopback bridge (/dev/video40, "XPS Camera") -> V4L2-only apps (Zoom)
```

| App | Status | How |
|---|---|---|
| GNOME Snapshot (Flatpak) | Works, upright | PipeWire libcamera plugin (steps 1-3) |
| Cosmic camera app (Flatpak) | Works, but upside down | Bundled libcamera, app rotates twice. Issue #719 |
| Zoom (deb) | Works | Bridge, choose "XPS Camera" (step 5, auto-started by the launcher) |
| Signal Desktop (deb) | Untested, probably works | Start bridge by hand, choose "XPS Camera" |
| Browsers (Firefox/Chrome) | Untested | Use PipeWire camera if enabled, else need the bridge |

Quick health check (run in order, stop at the first failure):
1. `lsmod | grep -E 'ipu7|ov02c10'` : kernel drivers loaded.
2. `id | grep video` and `ls -l /dev/dma_heap/system` : permissions (step 2).
3. `cam -l` : libcamera sees `\_SB_.LNK1`.
4. `pw-cli ls Node | grep libcamera_input` : PipeWire sees the camera (step 3).
5. `lsmod | grep v4l2loopback` and `ls /dev/video40` : bridge device (step 5).

## Symptoms (before the fix)
- No usable camera: `/dev/video0..31` exist, but they are raw IPU7 nodes. Apps show black or nothing.
- After the libcamera fix: the Cosmic camera app showed the image upside down.
- Zoom showed a black preview.

## Root cause
- The sensor outputs raw Bayer data. It needs libcamera's software ISP, which first supports this camera in libcamera 0.6+.
- Pop!_OS repos ship libcamera 0.2.0 and the PipeWire libcamera plugin built against it, so PipeWire never saw a working camera.
- The kernel side was fine: `intel_ipu7`, `intel_ipu7_isys` and `ov02c10` load, and the firmware is present.
- Apps that read `/dev/video*` directly (Zoom, and likely other V4L2-only apps) only ever see the raw nodes, so they need a bridge on top of the camera fix.

## What was done

### 1. Build libcamera 0.7.2+ into /usr/local
Build deps (sudo):
```
sudo apt install -y meson ninja-build git pkg-config python3-yaml python3-ply python3-jinja2 libyaml-dev libgnutls28-dev libudev-dev libevent-dev libdrm-dev libjpeg-dev libsdl2-dev libtiff-dev libglib2.0-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libpipewire-0.3-dev openssl cmake libepoxy-dev qt6-base-dev v4l-utils pipewire-libcamera
```
Build (source in `~/build/libcamera-src`, git master `a92285e`; build dir `~/build/libcamera-build`):
```
cd ~/build/libcamera-src
PATH=/usr/bin:$PATH meson setup ../libcamera-build --prefix=/usr/local \
  -Dpipelines=simple,uvcvideo -Dipas=softisp -Dgstreamer=enabled -Dcam=enabled \
  -Dqcam=disabled -Dtest=false -Ddocumentation=disabled -Dbuildtype=release
PATH=/usr/bin:$PATH ninja -C ../libcamera-build
sudo ninja -C ../libcamera-build install && sudo ldconfig
```
Gotcha: Meson picked up the Linuxbrew Python, which has no jinja2. Putting `/usr/bin` first in `PATH` fixes it.

Note: I also patched `camera_sensor_legacy.cpp` to assume 180° for the ov02c10 when the kernel gives no rotation. This turned out to be unnecessary, because the kernel does report `camera_sensor_rotation = 180`. A plain build of libcamera is enough.

### 2. dma-heap permission (the software ISP needs `/dev/dma_heap/system`)
```
sudo cp ~/build/60-dma-heap.rules /etc/udev/rules.d/
sudo usermod -aG video $USER
sudo udevadm control --reload && sudo udevadm trigger --action=add --subsystem-match=dma_heap
```
Rule contents: `SUBSYSTEM=="dma_heap", KERNEL=="system", TAG+="uaccess", GROUP="video", MODE="0660"`.
Log out and back in (or reboot) so the `video` group applies. Check with `id` and `ls -l /dev/dma_heap/system`.

### 3. PipeWire libcamera plugin built against libcamera 0.7
Source in `~/build/pipewire-src` (tag 1.6.8). Build dir `~/build/pipewire-build`.
```
cd ~/build/pipewire-src
# 1.6.8 needs a small patch for libcamera 0.7 (libcamera::Span -> std::span). Already fixed upstream
# (PipeWire MR 2766/2768), so a newer PipeWire probably needs no patch:
sed -i 's/libcamera::Span</std::span</' spa/plugins/libcamera/libcamera-source.cpp
sed -i '0,/#include/s//#include <span>\n#include/' spa/plugins/libcamera/libcamera-source.cpp
PATH=/usr/bin:$PATH meson setup ../pipewire-build --prefix=/usr/local -Dlibcamera=enabled \
  -Dexamples=disabled -Dtests=disabled -Ddocs=disabled -Dman=disabled -Dbluez5=disabled \
  -Dalsa=disabled -Dv4l2=disabled -Dvulkan=disabled -Dpipewire-alsa=disabled \
  -Dpipewire-jack=disabled -Djack=disabled -Dgstreamer=disabled -Dsdl2=disabled -Dlibusb=disabled
PATH=/usr/bin:$PATH ninja -C ../pipewire-build spa/plugins/libcamera/libspa-libcamera.so
D=/usr/lib/x86_64-linux-gnu/spa-0.2/libcamera
sudo cp -n $D/libspa-libcamera.so $D/libspa-libcamera.so.orig      # backup of the original
sudo install -m755 ~/build/pipewire-build/spa/plugins/libcamera/libspa-libcamera.so $D/libspa-libcamera.so
systemctl --user restart pipewire wireplumber
```

### 4. Verify the camera
- `ldd $D/libspa-libcamera.so | grep camera` should show `/usr/local/lib/x86_64-linux-gnu/libcamera.so.0.7`.
- `pw-cli ls Node | grep libcamera` should show `libcamera_input.__SB_.LNK1`.
- `cam -l` and `cam -c1 --capture=10 --file='/tmp/f-#.ppm'` should capture frames (about 30 fps).
- GNOME Snapshot (Flatpak) shows the camera upright.
- `cam` may log many `Unable to get rectangle` and `No static properties for 'ov02c10'` warnings. These are harmless.

### 5. Virtual webcam for V4L2-only apps (Zoom, maybe Signal): v4l2loopback
Steps 1-4 fix the camera for every PipeWire/libcamera-aware app. Apps that read `/dev/video*` directly (Zoom, possibly Electron apps like Signal) still only see the raw sensor nodes ("ipu7") and show black. A loopback device carries the processed video to them.
```
sudo apt install -y v4l2loopback-dkms v4l2loopback-utils gstreamer1.0-plugins-good
echo 'options v4l2loopback devices=1 video_nr=40 card_label="XPS Camera" exclusive_caps=1' | sudo tee /etc/modprobe.d/v4l2loopback.conf
echo v4l2loopback | sudo tee /etc/modules-load.d/v4l2loopback.conf
sudo modprobe v4l2loopback devices=1 video_nr=40 card_label="XPS Camera" exclusive_caps=1
```
User service `~/.config/systemd/user/zoom-camera.service` (not enabled; started on demand):
```
[Unit]
Description=Virtual webcam (/dev/video40) fed from the libcamera camera, for V4L2-only apps like Zoom
After=pipewire.service wireplumber.service

[Service]
ExecStart=/usr/bin/bash -o pipefail -c 'gst-launch-1.0 -q pipewiresrc target-object=libcamera_input.__SB_.LNK1 ! video/x-raw,width=1280,height=720 ! videoconvert ! videorate ! video/x-raw,format=YUY2,framerate=30/1 ! fdsink fd=1 | /home/linuxbrew/.linuxbrew/bin/ffmpeg -loglevel warning -f rawvideo -pix_fmt yuyv422 -video_size 1280x720 -framerate 30 -i - -f v4l2 -pix_fmt yuyv422 /dev/video40'
Restart=on-failure
RestartSec=3
```
(`ffmpeg` is the Linuxbrew one. Use `/usr/bin/ffmpeg` if you install it with apt.)

Launcher `~/.local/bin/zoom-with-camera` (chmod +x) starts the bridge, runs Zoom, and stops the bridge after the last Zoom process exits:
```
#!/usr/bin/bash
systemctl --user start zoom-camera
/usr/bin/zoom "$@"
while pgrep -f '^/opt/zoom/zoom' >/dev/null; do sleep 5; done
systemctl --user stop zoom-camera
```
`~/.local/share/applications/Zoom.desktop` is a copy of `/usr/share/applications/Zoom.desktop` with `Exec=$HOME/.local/bin/zoom-with-camera %U`.
In Zoom, choose **XPS Camera** (not "ipu7") under Settings, Video & effects.

## Things that did not work (so you don't repeat them)
- **WirePlumber rule** overriding `api.libcamera.rotation` to 0: it had no effect on the Cosmic camera app, which uses its own bundled libcamera. Removed.
- **GStreamer `v4l2sink` into v4l2loopback:** fails with `buffer 0 was not queued, this indicate a driver bug` in mmap mode. With `io-mode=rw` no frames reach the device. Piping `fdsink` into `ffmpeg -f v4l2` works.
- **Zoom Flatpak vs deb:** the deb behaves the same as the Flatpak. Both need the bridge.
- **`sudo` chains with `&&`:** the chain stopped silently at the libcamera install step once. Run steps separately or use `;`.

## Known issue: Cosmic camera app is upside down
- The Cosmic camera app (`io.github.cosmic_utils.camera` 1.3.7) uses its own bundled libcamera 0.7.2. It reads the sensor's `Rotation = 180` and rotates the preview and photos itself, on top of libcamera's own correction.
- Reported as https://github.com/cosmic-utils/cosmic-ext-camera/issues/719.
- Workaround: use GNOME Snapshot, which is correct.

## Maintenance and gotchas
- **`apt upgrade` of `pipewire-libcamera`** overwrites the patched plugin. Camera in PipeWire apps (Snapshot, browsers) stops working. Redo step 3. The original plugin is saved as `libspa-libcamera.so.orig`.
- **Kernel updates:** v4l2loopback is built by DKMS. If the build fails, `/dev/video40` disappears and Zoom goes black. Check `dkms status`.
- **The bridge holds the camera:** while it runs, the camera light is on and other camera apps can't open it. Start it only when needed (`systemctl --user start|stop zoom-camera`).
- **Secure Boot:** v4l2loopback is an unsigned DKMS module. It loaded fine here. If Secure Boot is enabled elsewhere, the module may be refused.
- **Signal Desktop (8.31.0, deb):** probably works with the bridge running and "XPS Camera" selected, but this has not been tested. Start the bridge by hand.
- **Rebuild source:** keep `~/build/` (libcamera-src, libcamera-build, pipewire-src, pipewire-build, 60-dma-heap.rules). Needed for reinstalls.

## Undo
```
D=/usr/lib/x86_64-linux-gnu/spa-0.2/libcamera
sudo cp $D/libspa-libcamera.so.orig $D/libspa-libcamera.so
sudo rm /etc/udev/rules.d/60-dma-heap.rules /etc/modprobe.d/v4l2loopback.conf /etc/modules-load.d/v4l2loopback.conf
sudo rm -r /usr/local/lib/x86_64-linux-gnu/libcamera* /usr/local/bin/cam   # libcamera from /usr/local
sudo ldconfig
systemctl --user disable --now zoom-camera 2>/dev/null; rm ~/.config/systemd/user/zoom-camera.service ~/.local/bin/zoom-with-camera ~/.local/share/applications/Zoom.desktop
```

## Reference
- libcamera Arch Wiki page: https://wiki.archlinux.org/title/Libcamera
- Zoom community thread on the same class of problem (IPU6): https://community.zoom.com/meetings-2/ipu6-support-on-linux-15985
- PipeWire fix for libcamera 0.6+ (`std::span`): merge requests 2766 and 2768 on gitlab.freedesktop.org/pipewire/pipewire
