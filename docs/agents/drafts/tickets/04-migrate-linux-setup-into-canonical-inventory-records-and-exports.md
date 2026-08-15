## What to build

Move Linux setup onto canonical Inventory Records and curated Inventory Exports. This slice should make the Linux Setup Plan point to canonical shared and Linux-specific records, normalize Linux Install Channel usage, and expose the latest curated Linux Inventory Export through the active navigation path.

## Acceptance criteria

- [ ] The Linux Setup Plan links to canonical shared and Linux-specific inventory material.
- [ ] Linux software install truth is represented using the agreed Install Channel values, including direct deb installs.
- [ ] The latest curated Linux Inventory Export is reachable from the Linux Setup Plan.
- [ ] A Linux rebuild path can be followed without relying on legacy Linux navigation roots.

## Blocked by

- #1 — Establish the role-based documentation skeleton
- #2 — Enforce the navigation contract in documentation validation
- #3 — Migrate shared desktop resources into canonical Resource Catalog records
