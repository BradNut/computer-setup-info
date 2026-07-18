# Docker Setup on Linux

Docker is now installed automatically by `environment/SetupLinux.sh` as part of the Linux setup plan. The provisioning adapter configures the official Docker apt repository and installs:

- `docker-ce`
- `docker-ce-cli`
- `docker-buildx-plugin`
- `docker-compose-plugin`
- `containerd.io`

For details, see the catalog entry [`catalog/linux-docker.md`](../catalog/linux-docker.md).

## Verification

Run `docker --version` to confirm the installation. Group membership and daemon access are manual follow-up steps if needed.
