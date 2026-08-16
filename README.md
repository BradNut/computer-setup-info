# Computer Setup Information

This repository is organized around a role-based setup path.

Start here, choose a primary [Setup Plan](plans/README.md), then follow that plan into the relevant [Resource Catalog](catalog/README.md) material and curated [Inventory Export](exports/README.md) snapshots. Historical material belongs in [reference](reference/README.md), not in the active setup path.

## Primary setup plans

- [Linux](plans/linux.md) — automated base provisioning plus manual configuration.
- [macOS](plans/macos.md) — manual application and development-environment setup.
- [Android](plans/android.md) — manual source and privacy decisions.

## Role directories

- [Setup Plans](plans/README.md) — ordered human-facing routes for each active entry point.
- [Resource Catalog](catalog/README.md) — reusable setup resources and inventory records.
- [Inventory Exports](exports/README.md) — curated snapshots of actual machine and device state.
- [Reference material](reference/README.md) — historical or contextual guides that are not part of the active setup path.

## Validation

Run the read-only documentation checks before committing documentation changes:

```bash
python3 scripts/validate_docs.py
```

The validator requires Python 3.9 or newer and takes an optional `--root` for checking a copy of the repo. Its own
test suite runs with:

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
```
