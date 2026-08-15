# Spec Draft: Reorganize setup docs and software inventories for Linux, macOS, and Android

Suggested issue title: `Reorganize setup docs into role-based navigation and inventory catalogs`

## Problem Statement

The setup documentation is currently scattered across multiple competing structures, which makes it hard to traverse, hard to trust, and hard to update. The repository has human-facing `Setup Plan` documents, older platform-specific guides, and `Resource Catalog` entries, but they do not yet form a coherent navigation path. Linux, macOS, and Android information is split between active and legacy locations, and Windows is still present in active navigation even though it is no longer an active `Entry Point`.

From the user's perspective, the current problems are:

- there is no single README-first path through the repository
- Linux, macOS, and Android setup guidance is duplicated or cross-linked inconsistently
- older platform folders compete with `plans/` and `catalog/` as navigation roots
- some `Resource Catalog` entries are canonical in theory but only stub back to older freeform documents in practice
- software inventories drift from the applications and tools the user actually uses
- Android application source decisions are embedded in prose instead of modeled explicitly
- Linux install methods span multiple `Install Channel` types, but the documentation does not treat them consistently
- stale links, legacy routes, and inactive Windows content make the docs harder to maintain

The result is a repo that is harder to rebuild from, harder to review for drift, and harder to extend without creating more documentation sprawl.

## Solution

Reorganize the repository around a role-based documentation architecture that is easy to traverse from `README.md` and easy to maintain over time.

The new shape should make `README.md` the front door, then route readers to active `Setup Plan` documents for Linux, macOS, and Android. Each `Setup Plan` should link onward to the relevant `Resource Catalog` material and the latest curated `Inventory Export` for that platform or device. The `Resource Catalog` becomes the canonical source of structured `Inventory Record` data, while older platform-specific Markdown content is either promoted into the new structure, moved into `reference/`, or deleted if it no longer belongs in the active repo.

This solution should:

- keep Linux, macOS, and Android as the only active `Entry Point` values in the main navigation path
- remove Windows from active docs and active navigation
- keep separate Linux and macOS `Setup Plan` documents while consolidating shared concerns into reusable shared `Resource Catalog` material
- model software as shared parent records plus platform-specific child records where install truth diverges
- explicitly model Android `Application Source` and Linux/macOS `Install Channel`
- support curated `Inventory Export` snapshots so actual machine state can be compared against curated `Inventory Record` data
- make navigation link-first instead of directory-first
- extend the existing validation tooling so the role-based docs architecture can be checked automatically

## User Stories

1. As the repo owner, I want `README.md` to be the required starting point, so that I can re-enter the repo later without remembering its directory layout.
2. As the repo owner, I want active setup guidance to be grouped by role, so that plans, catalogs, exports, and reference material do not compete with each other.
3. As the repo owner, I want a Linux `Setup Plan`, so that I can follow one ordered route for rebuilding a Linux machine.
4. As the repo owner, I want a macOS `Setup Plan`, so that I can follow one ordered route for rebuilding a macOS machine.
5. As the repo owner, I want an Android `Setup Plan`, so that I can review application and privacy choices in one place.
6. As the repo owner, I want Linux and macOS plans to remain separate, so that platform-specific system steps do not get buried in a merged desktop guide.
7. As the repo owner, I want shared cross-platform concerns to live in reusable `Resource Catalog` material, so that Linux and macOS docs do not drift independently.
8. As the repo owner, I want software inventory records to be structured, so that I can update one item without rewriting a whole platform list.
9. As the repo owner, I want each `Inventory Record` to carry core metadata, so that I can review and sort software decisions consistently.
10. As the repo owner, I want shared software to have a stable shared identity with platform-specific child records, so that cross-platform tools can stay conceptually grouped while install details stay accurate.
11. As the repo owner, I want Android applications to record a primary `Application Source`, so that I can remember where each app should come from.
12. As the repo owner, I want Android applications to allow alternate sources when needed, so that I can keep fallbacks without losing a preferred default.
13. As the repo owner, I want Android source values to be normalized to Aurora / Play Store, F-Droid, and Accrescent, so that source decisions are explicit and searchable.
14. As the repo owner, I want Linux applications to record their `Install Channel`, so that I can tell whether a tool comes from apt, a vendor repo, a direct `.deb`, Flatpak, Homebrew, AppImage, or manual install.
15. As the repo owner, I want direct `.deb` installs to be modeled distinctly, so that vendor downloads do not get collapsed into generic manual notes.
16. As the repo owner, I want macOS records to distinguish platform-specific install truth, so that Homebrew, App Store, and manual installs can be represented cleanly.
17. As the repo owner, I want shared records to live separately from platform records, so that the repository structure itself communicates what is shared and what is platform-specific.
18. As the repo owner, I want `catalog/shared/`, `catalog/linux/`, `catalog/macos/`, and `catalog/android/` style organization, so that catalog traversal matches the conceptual model.
19. As the repo owner, I want each major role directory to have its own README, so that navigation remains obvious even when opening a subdirectory directly.
20. As the repo owner, I want every active `Setup Plan` to link to its relevant shared resources, so that I never need to browse blindly for the next step.
21. As the repo owner, I want every active `Setup Plan` to link to its platform-specific resources, so that detailed records stay discoverable from the plan.
22. As the repo owner, I want every active `Setup Plan` to link to the latest curated `Inventory Export`, so that I can compare intended state to actual state.
23. As the repo owner, I want `Resource Catalog` records to link back to their relevant `Setup Plan` documents, so that records remain usable in context.
24. As the repo owner, I want sibling and parent-child catalog relationships to be navigable by links, so that I can move between shared and platform-specific records without searching.
25. As the repo owner, I want old platform directories to stop acting as active navigation roots, so that readers are not split between new and legacy pathways.
26. As the repo owner, I want still-useful legacy material moved into `reference/`, so that historical notes remain available without pretending to be current guidance.
27. As the repo owner, I want clearly obsolete active Windows content removed, so that inactive work does not pollute the repo’s main path.
28. As the repo owner, I want curated `Inventory Export` snapshots committed to the repo, so that I have durable history without committing every noisy machine-state run.
29. As the repo owner, I want exports grouped by platform and device, so that multiple machines or phones can coexist cleanly in the repo.
30. As the repo owner, I want Linux exports to include apt, Flatpak, Homebrew, direct `.deb` installs, and local launcher/AppImage state where practical, so that the snapshot reflects how Linux software is actually installed.
31. As the repo owner, I want macOS exports to include Homebrew and installed applications, so that my Mac inventory can be reconciled against curated records.
32. As the repo owner, I want Android exports to capture installed package data while source mapping remains curated, so that machine state and human decisions are both preserved.
33. As the repo owner, I want a hybrid review workflow, so that I can update records when software changes while still getting stale-item prompts later.
34. As the repo owner, I want review dates on records, so that I can see which items are likely stale.
35. As the repo owner, I want automation to validate navigation and metadata, so that a docs refactor does not silently break the setup path.
36. As the repo owner, I want the validation tooling to reject broken local links, so that README-first traversal remains trustworthy.
37. As the repo owner, I want validation to confirm required active plans and catalogs exist, so that role-based structure remains enforced.
38. As the repo owner, I want validation to understand the new catalog hierarchy, so that structured `Inventory Record` material can evolve safely.
39. As the repo owner, I want validation to ensure Windows is not present in active navigation, so that removed scope does not creep back in accidentally.
40. As the repo owner, I want the repo’s domain language to stay consistent, so that `Entry Point`, `Setup Plan`, `Resource Catalog`, `Inventory Record`, `Application Source`, `Install Channel`, and `Inventory Export` remain the stable vocabulary.

## Implementation Decisions

- The repository will be reorganized around four active roles: `Setup Plan`, `Resource Catalog`, `Inventory Export`, and `reference` material.
- `README.md` becomes the primary navigation contract for the repository and must link to all active `Setup Plan` surfaces.
- Linux, macOS, and Android remain the only active `Entry Point` values in the main setup path.
- Windows is removed from active navigation and active documentation scope rather than archived as a current path.
- Human-facing platform traversal remains separate per platform, with one `Setup Plan` per active `Entry Point`.
- Shared desktop and software concerns are consolidated into reusable `Resource Catalog` material rather than merged into a single cross-platform plan.
- Shared software is modeled as a shared parent record plus platform-specific child records where install or source truth differs by platform.
- Shared and platform-specific catalog material are separated structurally, with dedicated shared and per-platform catalog groupings.
- The canonical tracked unit is the `Inventory Record`, not a freeform bullet in a platform list.
- `Inventory Record` metadata uses a mandatory core and optional extensions. The mandatory core includes identity, category, platform coverage, kind, status, and last review date. Optional metadata includes source information, install channel, usage state, related documents, and notes.
- Categories are controlled at the top level, with optional tags for additional nuance.
- Linux `Install Channel` values are normalized to: `apt`, `apt-vendor`, `deb`, `flatpak`, `homebrew`, `appimage`, and `manual`.
- Android `Application Source` uses one primary source plus optional alternate sources.
- Android `Application Source` values are normalized to Aurora / Play Store, F-Droid, and Accrescent.
- Curated `Inventory Export` snapshots are part of the repository and grouped first by platform, then by named device.
- The repo’s upkeep model is hybrid: update `Inventory Record` material when the underlying software changes, but also review stale records periodically.
- Legacy platform Markdown is not left in place as an active navigation surface. Useful content is promoted into plans or catalogs, historical leftovers move into `reference/`, and obsolete material is deleted.
- Active directories should each provide their own README so link-first traversal continues to work from any point of entry.
- The repository keeps a single-context domain documentation model with one root glossary and ADRs under the standard decision directory.
- The existing documentation validator is the highest preferred implementation seam and should be extended instead of replaced. It remains the main automated contract for documentation architecture correctness.
- Validation should move beyond front matter and broken-link checking to also enforce the role-based structure and navigation contract.

## Testing Decisions

- Good tests should assert externally visible documentation behavior, not implementation details of how files are discovered or parsed.
- The highest automated seam is the documentation validation command. It should be treated as the primary correctness boundary for the migration.
- Validation tests or checks should verify outcomes such as: active navigation surfaces exist, required metadata is present, local links resolve, expected active `Entry Point` surfaces are present, and removed Windows navigation does not reappear.
- The modules to test are the documentation validation workflow and the documentation structure it validates.
- Manual acceptance testing should follow the README-first traversal path and confirm that a reader can reach each active `Setup Plan`, then its relevant `Resource Catalog` material, then the latest curated `Inventory Export`, without directory hunting.
- When validating catalogs, test behavior should focus on whether an `Inventory Record` is accepted or rejected correctly according to the schema and navigation rules, not on internal parsing implementation.
- Prior art for testing is the current documentation validation command, which already verifies resource metadata, plan metadata, known resource references, and broken local links. The new work should extend that seam rather than creating an unrelated second validator.

## Out of Scope

- Full live version-monitoring across Linux, macOS, and Android app ecosystems.
- Automatic discovery of trustworthy Android application source data from external stores.
- Broad changes to non-target `Entry Point` areas such as Synology, printers, or self-hosting beyond navigation impact caused by the top-level README cleanup.
- Rewriting every historical note into polished current guidance during the first migration.
- Turning machine exports into the canonical source of truth; curated `Inventory Record` material remains canonical.
- Implementing provisioning automation for macOS or Android as part of this documentation architecture change.

## Further Notes

- The repo currently has the beginnings of a `Setup Plan` plus `Resource Catalog` architecture, but several areas still route users back into older freeform source documents. The migration should finish that architectural shift instead of layering a third structure on top.
- The current Linux setup automation already demonstrates why `Install Channel` must be modeled explicitly: it mixes distro packages, vendor repos, direct `.deb` installs, Flatpak, Homebrew, and local/manual cases.
- The current Android application guide demonstrates why `Application Source` must become structured metadata instead of prose headings.
- The migration should preserve useful historical knowledge while making active setup routes unmistakably current.
- Before actual GitHub issue publication can succeed from this clone, the local `gh` authentication must be refreshed.
