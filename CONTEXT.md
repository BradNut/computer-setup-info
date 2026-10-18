# Setup Catalog Glossary

## Entry Point

A platform, device, or environment a person sets up through this repository, such as Linux, macOS, Android, Synology, a printer, or self-hosting.

Each Entry Point has exactly one Setup Plan at `plans/<entry-point>.md`. The plan's `status` decides whether the Entry Point is **active** (`current`) or **retired** (`reference`). Active Entry Points get role navigation, a curated Inventory Export, and links to current Inventory Records; retired Entry Points must not be linked from active navigation.

## Setup Plan

The ordered route for configuring one Entry Point. It includes manual, automated, and hybrid steps in the order they must occur.
_Avoid_: Master checklist, platform notes

## Resource Catalog

A collection of reusable setup records that Setup Plans point to.
_Avoid_: App list, random notes

## Inventory Record

The canonical record for one installable or configurable thing you intentionally keep track of, such as an application, package group, or setup resource. Inventory Records are grouped into Resource Catalogs and carry structured metadata plus short human guidance.
_Avoid_: Blob, freeform list item

## Application Source

The authority from which an Android application is obtained, such as Play Store via Aurora, F-Droid, or Accrescent.
_Avoid_: Repo, store, source of truth

## Install Channel

The delivery mechanism used to install an Inventory Record on a specific platform, such as apt, Flatpak, Homebrew, direct `.deb`, AppImage, App Store, or manual download.
_Avoid_: Just source

## Inventory Export

A machine-generated snapshot of what is currently installed on a device or host, used to compare actual state against curated Inventory Records.
_Avoid_: Backup, canonical inventory

## Execution Mode

How a Resource is applied: `manual` for human guidance, `automated` for a platform-specific provisioning adapter, or `hybrid` when automation and human actions both apply.

## Provisioning Adapter

A platform-specific mechanism that applies automated Resource steps. An adapter is optional; a Resource or Setup Plan remains useful without one.

## Current Guide

A guide verified for an explicitly supported platform or version and marked with the verification date.

## Reference Guide

Historical or contextual material retained for research or recovery. It is not a supported setup path.

## Review Candidate

A potentially obsolete Resource or guide awaiting a decision to keep current, archive as reference, or remove.
