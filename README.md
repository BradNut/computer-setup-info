# Computer Setup Information

## Setup catalog

Use a setup plan for the entry point you are configuring. Each plan orders manual, automated, and hybrid work. Reusable resources live in the [catalog](catalog/README.md); items that need a keep, archive, or removal decision are in the [obsolescence review queue](review/obsolete-candidates.md).

## Setup plans

- [Linux](plans/linux.md) — automated base provisioning plus manual configuration.
- [macOS](plans/osx.md) — manual application and development-environment setup.
- [Android](plans/android.md) — manual source and privacy decisions.
- [Windows](plans/windows.md) — manual application and device setup.
- [Synology](plans/synology.md) — manual NAS and container configuration.
- [Printers and scanners](plans/printers.md) — device-specific driver setup.
- [Self-hosting](plans/self-hosting.md) — workload selection and verification.

## Direct guides

- [Linux applications](linux/Applications.md)
- [Linux terminal](environment/Terminal.md)
- [Linux desktop](linux/Desktop-Setup.md)
- [Coding application configuration](environment/Coding-App-Configs.md)
- [macOS applications](osx/Applications.md)
- [Android applications](android/Applications.md)
- [Windows applications](windows/Applications.md)
- [Synology applications](synology/Applications.md)
- [Printer and scanner drivers](printers/README.md)

## Validation

Run the read-only documentation checks before committing documentation changes:

```bash
python3 scripts/validate-docs.py
```
