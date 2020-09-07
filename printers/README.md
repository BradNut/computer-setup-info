# Printers
## Brother 
### Drivers
- [MFC-L3750CDW](https://support.brother.com/g/b/downloadtop.aspx?c=us_ot&lang=en&prod=mfcl3750cdw_us_eu_as)

#### Instructions
* Mac and Windows Download Installer and run
* Linux: One of the following
  * Download and install .deb files
  * Run bash script

##### Bash Script Instructions
1. Download the tool.(linux-brprinter-installer-*.*.*-*.gz)
    - The tool will be downloaded into the default "Download" directory. (The directory location varies depending on your Linux distribution.) e.g. /home/(LoginName)/Download
2. Open a terminal window.
3. Go to the directory you downloaded the file to in the last step. By using the cd command. e.g. cd Downloads
4. Enter this command to extract the downloaded file:
    - Command: gunzip linux-brprinter-installer-*.*.*-*.gz
    - e.g. gunzip linux-brprinter-installer-2.1.1-1.gz
5. Get superuser authorization with the "su" command or "sudo su" command.
6. Run the tool:
    - Command: bash linux-brprinter-installer-*.*.*-* Brother machine name
    - e.g. bash linux-brprinter-installer-2.1.1-1 MFC-J880DW
7. The driver installation will start. Follow the installation screen directions.
    - When you see the message "Will you specify the DeviceURI ?",
    - For USB Users: Choose N(No)
    - For Network Users: Choose Y(Yes) and DeviceURI number.

The install process may take some time. Please wait until it is complete.

### Manuals

# Scanners
## EPSON
### Drivers
- [EPSON Perfection](https://epson.com/Support/Scanners/Perfection-Series/Epson-Perfection-V550-Photo/s/SPT_B11B210201)
### Manuals