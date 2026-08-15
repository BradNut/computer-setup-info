## What to build

Extend documentation validation so the new role-based navigation contract is enforced automatically. This slice should make it safe to evolve the documentation architecture by rejecting missing navigation surfaces, broken role-based traversal, and accidental reintroduction of removed active paths.

## Acceptance criteria

- [ ] The documentation validation flow rejects broken role-based navigation changes.
- [ ] Validation checks the required active navigation surfaces for the role-based architecture.
- [ ] Validation catches accidental reintroduction of Windows into active navigation.
- [ ] Validation still confirms local documentation links resolve correctly.

## Blocked by

- #1 — Establish the role-based documentation skeleton
