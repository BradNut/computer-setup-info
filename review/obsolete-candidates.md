# Obsolescence Review Queue

Items here require an explicit decision before they are kept current, archived as reference, or removed.

| Candidate | Evidence | Recommendation | Decision |
| --- | --- | --- | --- |
| `linux/Laptop-Linux-Resources.md` | Ubuntu 20.04 and `Pop!_OS`-specific commands; repeated legacy setup script; deprecated `apt-key` examples | Archive as reference after extracting still-used manual guidance | Pending |
| `linux/Docker-Setup.md` | States a 20.04 Docker repository limitation that no longer matches the current Linux adapter | Replace with the current Docker resource or archive | Pending |
| `linux/ProtonVPN-Configuration.md` | Uses the legacy Python CLI and `pip3`; repeats initialization guidance | Re-verify against current Proton VPN guidance before retaining | Pending |
| `synology/Advanded-Media-Setup.md` | Declares a 2019 update date and refers to legacy Synology Docker UI, image tags, and system commands | Archive as reference unless re-validated section by section | Pending |
| `self-hosting/Haugene-Synology.md` | Depends on old Synology Docker behavior and a manual TUN script | Re-verify the supported image and Synology Container Manager workflow | Pending |
| `android/Applications.md` | Contains stale app sources and malformed `hhttps` links | Re-validate sources and repair accepted entries | Pending |
| `README.md` legacy routes | Uses `../master/` paths and targets removed or misspelled files | Replace with the setup-plan interface | Addressed by this migration |
