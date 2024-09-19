# Advanced Setup Guide

_Note: Haven't been able to get everything working but documenting_

tl;dr: A step-by-step guide to setting up Sonarr, Radarr, Sabnzbd, and Transmission in Docker on a Synology NAS. Last Updated: Dec 13, 2019

A guide covering a basic setup using Plex, Download Station, and ShowRSS is also available.

Full Description: This setup will install and configure Transmission using OpenVPN, Sabnzbd, Sonarr, and Radarr in Docker. It will also cover optionally setting up a proxy server for easy access to these apps.

The steps in this guide are based off pieces of many different sources and guides, hopefully updated and all combined to provide a step-by-step guide.

Covered:

- Plex
- Docker
- Usenet with Sabnzbd
- Torrents with Transmission and OpenVPN
- Sonarr
- Radarr
- Proxy Setup

Not Covered:

- Remote Access
- Jackett

YMMW. Many of the configurations detailed below are subjective, so I am not claiming that these are the only or best way, just one way. When there is a reason why, I try to detail it. These steps are working in a test case of one. Any errors or additions/suggestions are welcome, and I'll update this as possible.
Sonarr/Radarr/Usenet/Torrent Setup

Important*: Any site specific input will be shown as <some_info> and should be replaced with the information specific to your setup.*

Prerequisites

There's a few pieces of information you'll need to have handy during the setup. Depending on the services/apps used, some of them are not free.

    The name of your Synology. Found in DSM --> Control Panel --> Info Center--> Server Name.
    Synology IP. Found in DSM --> Control Panel --> Network --> Network Interface
        Your Synology should have a static IP on your local (home) network. This can often be done using DHCP on your router, but this is not covered in this guide.
    Local network subnet. Probably 172.x.x.x or 10.x.x.x
    Your timezone in TZ Database format

    SSH access to your Synology NAS makes things much easier, especially when troubleshooting.
    VPN provider, account info, and config name
    Disconnect VPN in DSM.
    Disable "Allow multiple Gateways" in Control Panel --> Network --> Advanced Settings.
    Torrents: any private servers or trackers account info.
    Usenet:
    usenet server account (host, username, password, port, number of connections)
    indexer account (api key)

Note: If one app isn't desired, it should be straightforward to skip the sections related to that app, ie all usenet sections.

File Structure

The file structure described below follows the best practices for Plex and other media apps. You can choose your own name, just remember to substitute throughout the instructions.

    In Synology DSM, open Control Panel --> Shared Folder
    Create shared folder "Data"
    In DSM open File Station
    in Shared Folder "Data" create folders: "Downloads", "Movies", "TV Shows", and any other libraries you will want in Plex. You can always add others later
    Under Downloads, create folders "Download Station", "Torrents", and "Usenet"
    In "Download Station", create folders "Movies", "ToFetch", "TV Shows"
    In "Torrents", create folders "InProgress", "Movies", "ToFetch", "TV Shows"
    In "Usenet", create folders "InProgress", "Movies", "TV Shows"

The folder structure should now look like:

```
Data/
    /Downloads
        /Download Station
            /Movies
            /ToFetch
            /TV Shows
        /Torrents
            /InProgress
            /Movies
            /ToFetch
            /TV Shows
        /Usenet
            /InProgress
            /Movies
            /TV Shows
    /Movies
    /TV Shows
```

Note: I choose to name folders throughout this guide using Capitals. This helps me know which folders I have created vs something created via another app or package since they tend to NOT use capitals. A personal preference.

Plex - Native Install

Note: These steps might not be as thorough as they are from memory, but installing Plex is straight forward and the available resources are excellent.

    Download the spk file from plex.tv. (the version in the Synology Package Center is not kept up to date)
    Open Package Center in Synology DSM
    Add the Synology Certificate
    Click Manual Install in Package Center and select the spk downloaded earlier.
    In DSM, open Control Panel --> Shared Folder
    Select "Data" share and click Edit.
    On Permissions tab, give plex user Read-Only access. Why
        If you really care, you could even remove access for the Data/Download folder.
    Open Plex via the Package Center or directly (http://local.nas.ip.address:32400/web)
    Configure Plex
        Add Movie library with location: Data/Movies
        Add TV Shows library with location: Data/TV Shows

Users and Groups

Permission problems are a common problem when setting up these apps. I have chosen to create different users for each app for greater control, but it would also be possible to set them up to all use the same user account.

    In DSM, open Control Panel --> User
    Create the following users:
        transmission
        sabnzbd
        sonarr
        radarr
    In Control Panel --> Group, create "MediaUsers"
    Add four new accounts and to MediaUsers group.
        Optional: add your administrator account. (You did disable the default "admin" account right?) This just simplifies things from the command line at times.
    Give MediaUsers group read/write permissions to the Data shared folder.
    Using SSH, log into your Synology
    Run command "id <username>" to get the user ID (UID) for each new user.
    Also note the ID for the MediaUsers group (it will be included with each user).

​

Docker

Docker is a containered environment. Similar to, but lighter weight, than virtualization. Many different apps are available as docker images.

Tip: Don't won't start if a VPN is running. Thanks to Synology Support!

    In DSM, open Package Center and install Docker
    Open Docker and go to Network.
    Click Add, enter "mediaNet" as Network Name and click Add.
    Disclose mediaNet and save the subnet info
    In DSM open File Station
    In share "docker", create folders "radarr", "sabnzbd", "sonarrv3", "transmission"
    One at a time, select each new folder, choose Action --> Permissions.
        Change owner to user created for each app and select "Apply to this folder, sub-folders and files"

​

Transmission

    In Docker, go to Registry
    Search for and download "Haugene Transmission-openvpn" - latest
    In Docker, go to Image
    Select "Haugene/Transmission-openvpn:latest" and click Launch
    Name container "transmission" (this will be used as the host name, so if you choose something different write it down).
    Check "Execute container using high privilege".
        Why: Transmission needs access to a tunnel device on the Synology that requires higher privilege. This container can be run from the command line with more limited privileges, but the Synology GUI doesn't provide an interface for those settings.
    Click Advanced Settings
        Check "Enable Auto-Restart"
        In Volume Tab, click Add Folder
            Select /Data/Downloads/Torrents
            Enter "/Data/Downloads/Torrents" as mount point
        In Volume Tab, click Add Folder
            Select /docker/transmission
            Enter "/config" as mount point
        In Network, add "mediaNet" and remove "bridge"
        In Port Settings
            Remove 8888 line
            Change Local Port from "Auto" to "9091". Why: If set to auto, the port used to connect to the app would be assigned a random number every time the container restarted.
        Environment Tab. Add or Set the following:
            PUID=<transmission\_uid>
            PGID=<MediaUsers\_id>
            OPENVPN_USERNAME=<vpn\_username>
            OPENVPN_PASSWORD=<vpn\_password>
            OPENVPN_PROVIDER=<vpn\_provider>
            OPENVPN_CONFIG=<vpn\_config\_name>
            TRANSMISSION_HOME=/config
            TRANSMISSION_WATCH_DIR=/Data/Downloads/Torrents/ToFetch
            TRANSMISSION_WATCH_DIR_ENABLED=true
            TRANSMISSION_UMASK=002
            TRANSMISSION_INCOMPLETE_DIR=/Data/Downloads/Torrents/InProgress
            TRANSMISSION_DOWNLOAD_DIR=/Data/Downloads/Torrents/Movies
            OPENVPN_OPTS=--inactive 3600 --ping 10 --ping-exit 60
            LOCAL_NETWORK=<mediaNet\_subnet>,<local\_network\_subnet>
            Optional: Other container settings you want.
            Optional: Other transmission settings you want. Note: No settings changed in Transmission webUI will be saved between container restarts.
        Click Next Button
        Click Apply button. Container should start up
    In Docker, go to Container. Transmission container should be running
    In browser, goto <nas\_IP>:9091 and you should see Transmission webUI
        Note: There are multiple webUIs included by default
    Test Transmission and VPN. Or here.
    If container doesn't start or keeps restarting, select and click Details, then look in the logs. Make sure your OPENVPN_CONFIG setting matches one of the ones in Github.

Note: Several guides, including the one from the container maintainer, include a shell script and a resolv.conf in the setup instructions for Synology. I found that everything the script did was already done/running on my Synology (DSM v6.2.2-24922 Update 4) (you always check what scripts that you copy off the internet do before running them as root right?) As for resolv.conf, it's possible the built-in DNS resolver in the mediaNet created in Docker removed the need the specific file. If you have problems, I would suggest looking at these two guides.

​

Sabnzbd

    In Docker, go to Registry
    Search for and download "linuxserver sabnzbd" - latest
    In Docker, go to Image
    Select "linuxserver/sabnzbd:latest" and click Launch
    Name container "sabnzbd"
    Click Advanced Settings
        Check "Enable Auto-Restart"
        In Volume Tab, click Add Folder
            Select /Data/Downloads/Usenet
            Enter "/Data/Downloads/Usenet" as mount point
        In Volume Tab, click Add Folder
            Select /docker/sabnzbd
            Enter "/config" as mount point
        In Network, add "mediaNet" and remove "bridge"
        In Port Settings
            Remove 9090 line
            Change Local Port from "Auto" to "8080"
        Environment Tab. Add or Set the following:
            PUID=<sabnzbd\_uid>
            PGID=<MediaUsers\_id>
            TZ=<timezone>
        Click Next Button
        Click Apply button. Container should start up
    In Docker, go to Container. Sabnzbd container should be running
    In browser, goto <nas\_IP>:8080 and you'll see setup wizard
        Select Langauge
        Enter Usenet Server Details
            Host
            Username
            Password
            Check "SSL" box
            In Advanced Settings
            Confirm port(s) match those given by your usenet provider
            Connections: Don't just set to max from usenet provider
        Test - should succeed
        Completed Download Folder=/Data/Downloads/Usenet/Movies
        Temporary Download Folder=/Data/Downloads/Usenet/InProgress
    Go to General Tab
        Setup security (user/pass) if you want
        Copy the API key and save for later
    Go to Folders Tab
    Set "Permissions for completed downloads"=775
    Go to Categories Tab
    in "tv" category
    Processing=+Delete
    Folder/Path=/Data/Downloads/Usenet/TV Shows
    Click Save on the tv line
    in movies category
    Processing=+Delete
    Note: will use server default which is correct for movies
    Click Save on movie line
    Delete software and audio if desired
    Go to Switches Tab
    Queue Section
    "Action when encrypted RAR is downloaded"=Abort
    "Unwanted Extensions"="exe, com"
    "Action when unwanted extensions detected"=Abort
    Click Save Changes button in that section
    Post Processing Section
    Check "Ignore Samples"
    Click Save Changes button in that section
    Optional: Set up schedule, anything else desired.

​

Sonarr

    In Docker, go to Registry
    Search for and download "linuxserver sonarr" - preview
        Decided on v3 based on discussion
    In Docker, go to Image
    Select "linuxserver/sonarr:preview" and click Launch
    Name container "sonarrv3"
    Click Advanced Settings
        Check "Enable Auto-Restart"
        In Volume Tab, click Add Folder
            Select /Data
            Enter "/Data" as mount point
        In Volume Tab, click Add Folder
            Select /docker/sonarr
            Enter "/config" as mount point
        In Network, add "mediaNet" and remove "bridge"
        In Port Settings
            Change Local Port from "Auto" to "8989"
        Environment Tab. Add or Set the following:
            PUID=<sonarr\_uid>
            PGID=<MediaUsers\_id>
            TZ=<timezone>
            UMASK-SET=022
        Click Next Button
        Click Apply button. Container should start up
    In Docker, go to Container. Sonarrv3 container should be running
    Go to <nas\_IP>:8989
    Click on System
        Three warnings that things aren't set up yet.
    Click Settings --> Media Management
    Click "Show Advanced"
    Episode Naming section
    Check "Rename Episodes"
    Standard Episode Format = "{Series Title} - S{season:00}E{episode:00} - {Episode Title} - {Quality Title}.{MediaInfo AudioCodec}.{MediaInfo VideoCodec}"
    Daily Episode Format = "{Series Title} - {Air-Date} - {Episode Title} - {Quality Title}.{MediaInfo AudioCodec}.{MediaInfo VideoCodec}"
    Series Folder Format = "{Series Title}"
    Season Folder Format = "Season {season:00}"
    Multi-Episode Style = Prefixed Range
    Importing Section
    Optional: Check "Import Extra Files"
    File Management Section
    Uncheck: Ignore Deleted Episodes
    Permissions Section
    Check "Set Permissions"
    File chmod mode = "0664"
    Folder chmod mode = "0775"
    Save Settings
    Settings --> Profiles
    Optional Delay Profile - If you want to prefer one download protocol vs another
    Click wrench and enter 180 for torrent delay
    Optional: Release Profiles - Add filters for things you specifically want or don't want
    Ex: Must Not Contain: "xvid, divx, avi, wma"
    Settings --> Indexers
    Click Plus
    Ex: NZBgeek
    Click Presets under Newznab
    Select NZBGeek
    Paste in <api\_key>
    Click Test
    Set RSS Sync Interval: 20min
    Save Changes
    Settings --> Download Clients
    Click Plus Button
    Click SABnzbd
    Enter Name "Sabnzbd"
    Host: "sabnzbd". Note: this needs to match the container name used earlier. Why? because it's using the DSN on the Docker mediaNet network.
    Enter <sabnzbd\_api\_key> saved earlier. (or go back to Sabnzbd and copy again)
    Test
    Click Plus Button
    Click Transmission
    Name: "Transmission"
    Host: "transmission". Again, must match container name.
    Test
    Series (at top)
    Add New or Import (if you have existing media)
    Import
    Select /Data/TV Shows as location
    Click on link to that path
    Let Sonarr check series' for a while
    Check matches
    Import All
    Note: Suggest not changing quality settings before Import all or it will start trying to download a lot of things. Instead adjust on a series by series basis later as needed.
    Optional: To test, you can add a new series or click on one with missing media or one you want at a higher quality. You should see activity in Sonarr and your download clients. Check System --> logs if you are having problems.

​

Radarr

Note: Radarr is based off of Sonarr, but the v3 branch isn't considered usable yet. So the interface will be a bit different, unless you chose to use the v2 branch of Sonarr.

    In Docker, go to Registry
    Search for and download "linuxserver radarr" - preview
        Decided on v2 based on discussion
    In Docker, go to Image
    Select "linuxserver/radarr:latest" and click Launch
    Name container "radarr"
    Click Advanced Settings
        Check "Enable Auto-Restart"
        In Volume Tab, click Add Folder
            Select /Data
            Enter "/Data" as mount point
        In Volume Tab, click Add Folder
            Select /docker/radarr
            Enter "/config" as mount point
        In Network, add "mediaNet" and remove "bridge"
        In Port Settings
            Change Local Port from "Auto" to "7878"
        Environment Tab. Add or Set the following:
            PUID=<sonarr\_uid>
            PGID=<MediaUsers\_id>
            TZ=<timezone>
            UMASK-SET=022
        Click Next Button
        Click Apply button. Container should start up
    In Docker, go to Container. Sonarrv3 container should be running
    Go to <nas\_IP>:7878
    Settings --> Media Management
        Change Advanced Settings to "Shown"
        Movie Naming Section
            Rename Movies: "Yes"
            Colon Replacement: "Replace with space Dash" (most similar to plex)
            Standard Movie Format = "{Movie Title} ({Release Year}) - {Quality Title}.{MediaInfo AudioCodec}.{MediaInfo VideoCodec}"
            Movie Folder Format = "{Movie Title} ({Release Year})"
        Importing Section
            Import Extra Files: Yes
            Extra File Extensions: "srt, sub"
        File Management Section
            Unmonitor Deleted Movies: "Yes" Why? I choose to set this differently than in Sonarr, because if I delete a movie I probably want it to go away unlike a TV episode
            Analyze Video File: Decide if you want to spend the processing cycles
        Permissions Section
            Set Permissions: "Yes"
            File chmod mask: "0664"
            Folder chmod mask: "0775"
        Save Changes
    Settings --> Profiles
    Optional Delay Profile - If you want to prefer one download protocol vs another
    Click wrench and enter 180 for torrent delay
    Settings --> Quality
    Enter defaults that work for you. ex: Do you want Blu-ray (1080p) movies that are 10GB or is 4-5GB good enough quality for you? Feel free to debate YTS quality somewhere else.
    Settings --> Indexers
    Click Plus - ex NZBGeek
    Click presets under Newznab
    Select NZBgeek
    Paste in <api\_key>
    Click Test
    Click Save
    RSS Sync Interval: 60min
    Optional: Restrictions - add filters for things you specifically want or don't want
    Ex: Must Not Contain: "xvid, divx, avi, wma"
    Click Save
    Settings -->Download Clients
    Click Plus Button
    Enter Name "Sabnzbd"
    Host: "sabnzbd". Note: this needs to match the container name used earlier. Why? because it's using the DSN on the Docker mediaNet network.
    Enter <sabnzbd\_api\_key> saved earlier. (or go back to Sabnzbd and copy again)
    Test
    Click Plus Button
    Click Transmission
    Name: "Transmission"
    Host: "transmission". Again, must match container name.
    Test
    Completed Download Handling Section
    Check for Finished Downloads Interval: 5min
    Save Settings
    Note: You may still see 3 warnings on System, but you've fixed everything.
    Click Add Movies
    Bulk Import Movies - if you have existing movies to import
    Optional - change number of movies displayed
    Change monitored and profile
    (if you already have them do need radarr to monitor them? Unless you want a higher quality, probably no)
    Click checkmark to select all
    Click Add All
    When finished, repeat as needed with additional pages to import
    Test adding a new movie
    Click Add Movie at Top
    Click Discover New Movies
    Click Green magnifying glass on a movie you want
    Click Activity
    If Queue is empty, click on history as it might already be in progress
    Should also start downloading in a client if it was found.

​

Proxy Setup (optional)

Instead of having to remember all the port numbers you used for each app, it's possible to set up a proxy to access all of the different webUIs through one url. For example, instead of

`http://<nas_ip>:8989`

you could access Sonarr at

`http://<nas_server_name>/sonarr/`

and likewise for /radarr, /transmission, etc.

    In Sonarr Settings --> General
        Set URL Base to "/sonarr"
    In Radarr Settings --> General
        Set URL Base to "/radarr"
    SSH into Synology NAS
    Create a new file at /usr/local/etc/nginx/sites-enabled/mediaProxy.conf
        sudo vi /usr/local/etc/nginx/sites-enabled/mediaProxy.conf
        Press "I"
        Enter text below
        Press Esc
        Press ":wq" and then enter.
    Restart nginx (web server)
        sudo synoservicecfg -restart nginx

​```
server {
listen 80;
listen [::]:80;
server_name <nas_server_name>.local;
location /plex {
proxy_pass http://localhost:32400/web/;
proxy_redirect off;
proxy_set_header Host $host;
  }
  location /web {
    proxy_pass          http://localhost:32400;
    proxy_redirect      off;
    proxy_set_header    Host $host;
}
location /sonarr {
proxy_pass http://localhost:8989;
proxy_redirect off;
proxy_set_header Host $host;
  }
  location /radarr {
    proxy_pass          http://localhost:7878;
    proxy_redirect      off;
    proxy_set_header    Host $host;
}
location /sabnzbd {
proxy_pass http://localhost:8080;
proxy_redirect off;
proxy_set_header Host $host;
  }
  location /transmission {
    proxy_pass          http://localhost:9091;
    proxy_redirect      off;
    proxy_set_header    Host $host;
proxy_pass_header X-Transmission-Session-Id;
}
}

```

Now you can access all of the apps by going to
`http://<nas_ip>/app`

Even better, because Synology does mDNS registration, on your local network you can actually use the server name instead of the IP address:
`http://<nas-server-name>.local/sonarr`

nas-server-name.local works for network shares as well. Think of it as ad-hoc DNS.

While this guide does not cover enabling remote access (or security in such as using ssl or even user/pass), setting up a proxy would be a step towards providing a single point of access, which would be easier to secure. For example, the Synology firewall could be configured block access to port 8989 except from localhost, which would be from the proxy.

### Useful Commands

Check your public IP:
`wget -qO- http://ipecho.net/plain ; echo`

Get the IP of a running container:
`docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name_or_id>`

Attach network troubleshooting image (after downloading):
`docker run -it --rm --network container:sonarrv3 nicolaka/netshoot`

Note: Some containers are so "lean" they don't have many standard commands, like looking dns info etc.

Get docker cmd line arguments used by GUI (after downloading):
`docker run -v /var/run/docker.sock:/var/run/docker.sock assaflavie/runlike <container_name>`

Thanks to all the resources I linked above and a few more:
* https://www.reddit.com/r/usenet/wiki/docker
* https://www.cuttingcords.com/home/ultimate-server/setting-up-sonarr
* https://github.com/Radarr/Radarr/wiki/Setup-Guide
* https://blog.pavelsklenar.com/how-to-install-and-use-docker-on-synology/
* https://docs.docker.com/engine/reference/commandline/run/
```
