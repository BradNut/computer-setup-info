# Resource Catalog

Each file in this directory is one reusable setup resource. Its YAML front matter is the resource interface; its body is the human guidance.

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
