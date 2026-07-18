# Printers and Scanners

## Printers

### Brother

#### Drivers

- [MFC-L3750CDW](https://support.brother.com/g/b/downloadtop.aspx?c=us_ot&lang=en&prod=mfcl3750cdw_us_eu_as)

#### Instructions

- **Mac and Windows:** Download the installer and run.
- **Linux:** Use one of the following methods:
  - Download and install the `.deb` files from the Brother download page.
  - Run the bash Driver Install Tool (see below).

##### Bash Script Instructions

1. Download the Brother Driver Install Tool (`linux-brprinter-installer-*.gz`) from the [MFC-L3750CDW downloads page](https://support.brother.com/g/b/downloadlist.aspx?c=us&lang=en&os=128&prod=mfcl3750cdw_us_eu_as). As of 2026, the tool is at version 2.2.6-0.
   - It will be saved to your default Downloads directory (location varies by distribution, e.g. `/home/(LoginName)/Download`).
2. Open a terminal window.
3. Change to the download directory, e.g. `cd Downloads`.
4. Extract the downloaded file:
   ```sh
   gunzip linux-brprinter-installer-*.gz
   # e.g. gunzip linux-brprinter-installer-2.2.6-0.gz
   ```
5. Get superuser authorization with `su` or `sudo su`.
6. Run the tool:
   ```sh
   bash linux-brprinter-installer-* Brother machine name
   # e.g. bash linux-brprinter-installer-2.2.6-0 MFC-L3750CDW
   ```
7. Follow the installation prompts.
   - When asked "Will you specify the DeviceURI?":
     - **USB users:** choose `N` (No).
     - **Network users:** choose `Y` (Yes) and select the DeviceURI number.

The install process may take some time. Wait until it is complete.

## Scanners

### EPSON Perfection V550 Photo

#### Drivers

- [EPSON Perfection V550 Photo support](https://epson.com/Support/Scanners/Perfection-Series/Epson-Perfection-V550-Photo/s/SPT_B11B210201)
- [Epson Linux iScan downloads](http://support.epson.net/linux/en/iscan.php?model=perfection-v550)

#### Instructions

- **Mac and Windows:** Download the installer from Epson's support page and run.
- **Linux:** Epson does not officially support Linux drivers, but the scanner usually works with the iScan bundle or SANE.
  - **iScan bundle:** download the `iscan-perfection-v550-bundle` `.deb.tar.gz` from Epson's Linux download page, extract it, and run `sudo sh install.sh`.
  - **SANE:** install `sane` and `simple-scan` (`sudo apt install sane sane-utils simple-scan`). If `scanimage -L` does not list the scanner, symlink the Epson backend libraries:
    ```sh
    sudo ln -sfr /usr/lib/sane/libsane-epkowa* /usr/lib/x86_64-linux-gnu/sane/
    ```
