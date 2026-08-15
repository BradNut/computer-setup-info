---
id: shared-terminal-preferences
title: Shared terminal preferences
entry_points: linux, macos
execution_mode: manual
status: current
supported: Linux and macOS terminal preferences
verified_on: 2026-08-15
source_docs: environment/Shared-Desktop-Setup.md
---

Use this `Inventory Record` for shell, prompt, terminal, and SSH preferences shared across desktop setups.

## Shell and prompt

- Zsh is the preferred interactive shell
- Starship provides the prompt, using the Nerd Font preset with Fira Code Nerd Font
- Keep shell settings such as [.zshrc](https://github.com/BradNut/dotfiles/blob/master/.zshrc) in the [dotfiles repository](https://github.com/BradNut/dotfiles) when possible

## Terminal tools and habits

- Keep [Vim](https://www.vim.org/) available with the tracked [.vimrc configuration](https://github.com/BradNut/dotfiles/blob/master/.vimrc)
- Use terminal shell integrations or shell commands for GUI editors when needed
- Confirm SSH is enabled and a current keypair is available before cloning private repositories

## Linux-specific automation

Linux base provisioning already applies the automated portions of this record through [Linux terminal tooling](./linux-terminal-tooling.md).

## Related records

- [Shared coding environment preferences](./shared-coding-environment-preferences.md)
- [Shared account and privacy decisions](./shared-account-and-privacy-decisions.md)
