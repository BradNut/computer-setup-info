# Resource Catalog

The `Resource Catalog` is the reusable layer of the repository. Active [Setup Plans](../plans/README.md) point here for canonical setup resources and `Inventory Record` material.

## Role in the active setup path

Use a `Setup Plan` as the starting point for active Linux, macOS, and Android setup work. From there, follow links into the catalog for reusable guidance and structured records.

## Shared desktop records

Use these shared records before platform-specific follow-up when working through the Linux or macOS `Setup Plan`.

- [Shared desktop software inventory](./shared-desktop-software.md)
- [Shared coding environment preferences](./shared-coding-environment-preferences.md)
- [Shared terminal preferences](./shared-terminal-preferences.md)
- [Shared browser and extension choices](./shared-browser-and-extension-choices.md)
- [Shared account and privacy decisions](./shared-account-and-privacy-decisions.md)

## Platform-specific records

- Linux automation and install-channel records stay in the Linux catalog entries such as `linux-base-system`, `linux-terminal-tooling`, `linux-desktop-applications`, and `linux-flatpak-applications`.
- macOS-specific application follow-up currently lives in [macOS application catalog](./macos-application-catalog.md) until the dedicated macOS migration slice lands.

## Related directories

- [Setup Plans](../plans/README.md)
- [Inventory Exports](../exports/README.md)
- [Reference material](../reference/README.md)

## Required metadata

```yaml
---
id: unique-resource-id
title: Human-readable title
entry_points: linux
execution_mode: manual
status: current
supported: Platform or device version
verified_on: YYYY-MM-DD
source_docs: linux/Source.md
---
```

`source_docs` is a path relative to the repository root. Automated resources add `provisioning_adapter`, also relative to the repository root.

Use `manual`, `automated`, or `hybrid` for `execution_mode`. Automated resources also declare a platform-specific `provisioning_adapter`. `status: current` requires an ISO `verified_on` date; use `status: reference` and `verified_on: pending` for material awaiting re-verification. Do not make destructive changes from this catalog without a confirmed setup plan.
