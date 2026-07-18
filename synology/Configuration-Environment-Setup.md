# Configuration Setup

> **2026 update:** Current DSM release line is DSM 7.2 / 7.3. Docker has been renamed **Container Manager** in DSM 7.2+. New Plus-series NAS models (DS225+, DS425+, DS925+, DS1525+, DS1825+) and the BeeStation personal cloud line are widely available.

## How to Set up and Configure a Synology NAS

- Official first-time setup documentation: https://www.synology.com/en-us/knowledgebase/DSM/tutorial
- Legacy video walkthrough: https://www.youtube.com/playlist?list=PLVvGujxCZRD6H6rlpMfaNMmFpmZJ1wYwo

## Security

[Securing Your NAS](https://www.synology.com/en-us/knowledgebase/DSM/help/DSM/Tutorial/secure_your_nas)

Additional 2026 recommendations:

- Keep DSM and all packages updated.
- Enable Adaptive Multi-Factor Authentication (AMFA) for admin accounts (DSM 7.2+).
- Use Snapshot Replication with immutable snapshots and WriteOnce shared folders for ransomware protection.
- Configure firewall rules and Auto Block to limit external access.
- Disable default admin account and use strong, unique passwords.

## Tips

1. Set up new users and/or groups for Container Manager / Docker images

- This will allow you to get the user ID (UID) and group ID (GID) for use in Container Manager / Docker configs
  - Run: `id <username>`

2. Container Manager (DSM 7.2+)

- In DSM 7.2 and later, the Docker package is named **Container Manager** and supports Docker Compose projects from the UI.
- Legacy command-line usage remains available via SSH with `docker` and `docker-compose`/`docker compose`.
