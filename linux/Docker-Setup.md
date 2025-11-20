# Docker Setup on Linux (Ubuntu)

Docker Docs Install Instructions: https://docs.docker.com/engine/install/ubuntu/#prerequisites

- Works for Ubuntu before 20.04
- If on 20.04 use below instructions in conjunction with the docs _until a 20.04 version is released_.

## Ubuntu 20.04

Specifically the add-apt-repository command in the docs does not work because 20.04 focal release is not available.
Follow these instructions: https://askubuntu.com/questions/1230189/how-to-install-docker-community-on-ubuntu-20-04-lts
Instead of:

```
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

use

```
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   bionic \
   stable"
```

### Removing incorrect apt-repository

Use `sudo add-apt-repository -r` to remove:
`sudo add-apt-repository -r "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"`
