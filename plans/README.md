# Setup Plans

Each file in this directory is the ordered human-facing route for one `Entry Point`. A `Setup Plan` is the authoritative path a person follows; supporting `Resource Catalog` material and `Inventory Export` snapshots hang off that path.

A plan with `status: current` makes its `Entry Point` active; `status: reference` retires it. The validator derives the required navigation links from these statuses, so activating or retiring an Entry Point starts with this front matter.

Provisioning adapters execute only automated steps. The plan remains the authoritative route for a human completing the setup.

## Primary setup plans

- [Linux](./linux.md) — automated base provisioning plus manual configuration.
- [macOS](./macos.md) — manual application and development-environment setup.
- [Android](./android.md) — manual source and privacy decisions.

## Related directories

- [Resource Catalog](../catalog/README.md)
- [Inventory Exports](../exports/README.md)
- [Reference material](../reference/README.md)
