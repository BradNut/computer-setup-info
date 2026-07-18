---
id: synology-setup-plan
title: Synology setup plan
entry_point: synology
status: reference
supported: Synology DSM guidance awaits re-verification
verified_on: pending
---

# Synology Setup Plan

## 1. Base NAS configuration — manual

Apply `synology-base-configuration` using [configuration guidance](../synology/Configuration-Environment-Setup.md). Confirm account, group, and security decisions for this NAS.

## 2. Packages and containers — manual

Review `synology-application-catalog` in [Synology applications](../synology/Applications.md). Use [Docker setup](../synology/Docker-Setup.md) only after reviewing its pending status in the [review queue](../review/obsolete-candidates.md).

## 3. Media automation — reference pending review

The advanced media guide is not a current setup path. See the [review queue](../review/obsolete-candidates.md) before using it.

## Verification

Confirm DSM security configuration, package state, and each container's current image documentation.
