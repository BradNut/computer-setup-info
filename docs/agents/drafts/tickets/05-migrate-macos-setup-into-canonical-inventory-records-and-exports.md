## What to build

Move macOS setup onto canonical Inventory Records and curated Inventory Exports. This slice should make the macOS Setup Plan point to canonical shared and macOS-specific records, represent macOS install truth through platform-specific child records, and expose the latest curated macOS Inventory Export through the active navigation path.

## Acceptance criteria

- [ ] The macOS Setup Plan links to canonical shared and macOS-specific inventory material.
- [ ] macOS software install truth is represented through canonical platform-specific records.
- [ ] The latest curated macOS Inventory Export is reachable from the macOS Setup Plan.
- [ ] A macOS rebuild path can be followed without relying on legacy macOS navigation roots.

## Blocked by

- #1 — Establish the role-based documentation skeleton
- #2 — Enforce the navigation contract in documentation validation
- #3 — Migrate shared desktop resources into canonical Resource Catalog records
