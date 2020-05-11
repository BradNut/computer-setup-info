# Haugene Transmission Synology Instructions

## Instructions

_Reddit Link_: https://www.reddit.com/r/VPNTorrents/comments/900w78/xpost_rsynology_setting_up_the/?utm_source=reddit&utm_medium=usertext&utm_name=synology&utm_content=t3_fg61l7

### Installing Docker on Your Synology NAS

Login to your Synology NAS through your web browser.

Open the _Package Center_. If you own one of the more recent "+" models, you should find Docker in your installable packages. If so, install it.

Otherwise, if, like me, you own a Synology NAS which doesn't officially support the Docker app, there's a way to install it manually. Needless to say, installing Docker on your officially unsupported Synology NAS has its own set of risks. Do your homework, evaluate those risks and, if you choose to proceed, do so with caution.

To install Docker on an unsupported Synology NAS, you must download a compatible version of the Docker app for Synology NAS from the [Synology website](https://usdl.synology.com/download/Package/spk/Docker/).

Next, manually install the package through _Package Manager_.

If everything works, you should find _Docker_ in your installed packages. If you run it, it should look like this.

Now that Docker's installed on your Synology NAS, time to create and configure a container with the _haugene-transmission-openvpn_ image.

### Downloading the Image and Creating the Docker Container

In the Synology Docker app, under the Registry tab, search for _"haugene"_ and the first result should be _"haugene-transmission-openvpn"_. Download this image.

When it's downloaded, you'll have an option to run the container directly. It'll run, but only briefly before it crashes. The container requires additional configuration before it'll run correctly.

### Enabling SSH on your Synology NAS

Open your Synology's Control Panel through your browser. Enable "Advanced Mode" in the top right corner.

Click on _Terminal & SNMP_ under _Applications_ at the bottom of the screen. On the next window, click on _"Activate SSH Service"_, under _port 22_ for now. You can change this later, as Synology's Security Advisor will warn that keeping the default port 22 for SSH is a security risk.

### Create directories

Next, create a _"docker"_ directory on your NAS where you will put the configuration files.

Also create a _"transmission-openvpn"_ subdirectory within your new "docker" directory.

While we're at it, since you will want to download some files through torrent with your new container, create a new directory for those downloads. Something like _"transmission-downloads"_. My personal recommendation: put this folder outside your /docker/transmission-openvpn/ directory.

Ensure that your user with administrative privileges has read/write access for these newly created directories.

### Create the Prelaunch Script (TUN.sh) and the Configuration file (resolv.conf) and

### -TUN.sh

On your Windows machine, open notepad, save the file as "TUN.sh" and and paste the following script from [haugene's readme on GitHub (credit to timkelty)](https://github.com/haugene/docker-transmission-openvpn/blob/master/README.md#make-it-work-on-synology-nas):

```
#!/bin/sh

# Create the necessary file structure for /dev/net/tun

if ( [ ! -c /dev/net/tun ] ); then
if ( [ ! -d /dev/net ] ); then
mkdir -m 755 /dev/net
fi
mknod /dev/net/tun c 10 200
fi

# Load the tun module if not already loaded

if ( !(lsmod | grep -q "^tun\s") ); then
insmod /lib/modules/tun.ko

fi
```

### -resolv.conf

On your Windows machine, open notepad, save the file as "resolv.conf" and and paste the following script from [haugene's readme on GitHub](https://github.com/haugene/docker-transmission-openvpn/blob/master/README.md#make-it-work-on-synology-nas):

```
nameserver 8.8.8.8
nameserver 8.8.4.4
```

If you'd prefer to use a different Domain Name Server, you're free to change the IP addresses above. If you use these settings, they are set to [Google's public DNS](https://developers.google.com/speed/public-dns/). Note: you must manually specify a DNS, otherwise you will run into errors.

### Move These Files to Your /docker/transmission-openvpn/ Directory

You can move these files to your `/docker/transmission-openvpn/` directory using your File Station on your Synology's page on your browser or using CygWin (& OpenSSH through the Terminal) and/or WinSCP (using a GUI).

### Run TUN.sh and Set it to Run After a Reboot

On your Synology's page in your browser, open up _Control Panel_ and click on _Task Scheduler_ under _System_. Create and save the following scheduled task:

- Task name: "Run TUN.sh"
- User: `root`
- Event: `Boot-up`
- Run command: `bash /volume1/docker/transmission-openvpn TUN.sh`

In the task scheduler, click on the newly created task and hit "Run".

Now, back to the Docker app for the final configuration.

### Final Docker Container Configuration

Open Docker on your Synology page through your web browser. Select the _haugene-transmission-openvpn_ container and click _Edit_.

On the _Volume_ tab, mount the following folder and file:
| File/Folder | Mount Path | Read only |
| ----------- | ---------- | --------- |
| [your-path-here]/docker/transmission-downloads | /data/completed | no |
| [your-path-here]/docker/transmission-openvpn/resolv.conf | /etc/resolv.conf | yes |

On the _Port Settings_ tab, specify the following:
| Local Port | Container Port | Type |
| ---------- | -------------- | ---- |
| [your first port here. Ex: 32770] | 8888 | TCP |
| [your second port here. Ex: 32771] | 9091 | TCP |

On the _Environment_ tab, specify the following variables and leave the rest as default for now:
| Variable | Value |
| `OPENVPN_CONFIG` | Check [haugene's GitHub](https://github.com/haugene/docker-transmission-openvpn/tree/master/openvpn) and take down how the .ovpn file is named. Ex: if you use Private Internet Access, click on the "pia" directory. If you want to use the AU Melbourne VPN server, write "AU Melbourne" |
| `OPENVPN_USERNAME` | Self explanatory |
| `OPENVPN_PASSWORD`| Self explanatory |
| `OPENVPN_PROVIDER` | Check [haugene's GitHub](https://github.com/haugene/docker-transmission-openvpn/tree/master/openvpn) and take down how the folder for your provider is named. Ex: if you use _Private Internet Access_, type _"PIA"_ |

Hit apply.

### Run Your New Container

Hit the toggle switch on the right of your new container.

If you made a mistake or skipped steps, it will crash in under a minute. Check that your TUN.sh script ran successfully. If you're in doubt, `sudo` run the script through SSH (if you're on Windows, you will need CygWin and OpenSSH - bin and src - installed).

If you followed the instructions, the container will run. Try the following link in your browser: http://[yournas]:32771 (or whichever port you set) and you should see the transmission web UI.

If you encounter any errors, consult your container log.

### Confirm the VPN is Working

To confirm the VPN is working, you can use one of the following tools:

- http://ipmagnet.services.cbcdn.com/
- https://torguard.net/checkmytorrentipaddress.php
- https://ipleak.net/

Excuse me if I skipped a couple of steps, I wrote this guide from memory nearly one month after receiving my NAS and getting this setup. If anyone has any corrections for me, I'd be happy to edit this post. Hopefully this can help someone else get it running more simply.

Good luck and enjoy.
