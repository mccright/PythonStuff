# Some new laptop setup notes:  

```bash
# Install net-tools for ifconfig
sudo apt install net-tools
#
# Install Python pip
sudo apt install --upgrade build-essential python3-pip libffi-dev python3-dev python3-setuptools libssl-dev -y
# or the short command: sudo apt install python3-pip
# Install the virtual environment to 
# isolate and run Python apps
sudo apt install python3-venv -y
# Clear buffers to disk
sudo sync
sync;sync
# 
# Install Visual Studio Code
sudo snap refresh
sudo snap install code --classic
# 
# Update VS Code periodically
sudo snap refresh code
# 
# Need Flatpak for Github Desktop
# https://www.linuxcapable.com/how-to-install-github-desktop-on-ubuntu-22-04-lts/
# Install Flatpak (once)
sudo apt install flatpak -y
# Before you proceed, reboot your system, 
# or else you will have issues such as 
# applications icons not appearing.
# ...and then reboot
reboot
# Enable Flatpack using the following 
# command in your terminal (once).
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
# 
# Now install Github Desktop with 
# the following flatpak command:
flatpak install flathub io.github.shiftey.Desktop -y
# 
# Launching GitHub Desktop
flatpak run io.github.shiftey.Desktop
# or use your menu 
Activities > Show Applications > Github Desktop
# 
# How to Update/Upgrade Github Desktop
# For Flatpak, run the following command to 
# check in your terminal for upgrades.
flatpak update
# 
# Install SQLite 3
sudo apt update && sudo apt upgrade -y
sudo apt install sqlite3
sqlite3 --version
# 
# Install PyCharm
sudo apt update && sudo apt upgrade -y
sudo snap install pycharm-community --classic
# How to Update/Upgrade Zoom Client
sudo snap refresh
# 
# Install Zoom
sudo apt update && sudo apt upgrade -y
sudo snap install zoom-client
# Clear buffers to disk
sudo sync
sync;sync
# You can run it from the command line: 
# sudo snap run zoom-client
# How to Update/Upgrade Zoom Client
sudo snap refresh
# 
# Install Microsoft fonts
sudo apt update && sudo apt upgrade -y
sudo apt install ttf-mscorefonts-installer -y
# 
# How to Remove (Uninstall) Microsoft Fonts
## sudo apt autoremove ttf-mscorefonts-installer --purge
# 
# Install/Upgrade cURL
sudo apt update && sudo apt upgrade -y
sudo apt install software-properties-common apt-transport-https curl -y
sync;sync
curl --version
# 
# Install KeePass
sudo snap install keepassxc
sync;sync
# If we need to remove it
## sudo snap remove keepassxc
# 
# Install Calibre
sudo apt update && sudo apt upgrade -y
sudo apt install calibre -y
# 
# Install OpenSSH Server
# https://www.linuxcapable.com/install-enable-connect-to-ssh-on-ubuntu-22-04-lts/
sudo apt update && sudo apt upgrade -y
sudo apt install openssh-server -y
# Once installed, enable SSH using the following command.
sudo systemctl enable --now ssh
sudo systemctl status ssh
# Configure UFW Firewall to allow for inbound port 22
sudo ufw allow 22/tcp 
# UFW is installed by default; to 
# enable it use the following command 
# for those that do not have it enabled.
sudo ufw enable
# Get the PC's IP address with ifconfig.
# Connect to SSH Server:
# ssh username@ip-address/hostname
# 
# Install Docker Desktop
sudo apt update && sudo apt upgrade -y
sudo apt install --upgrade ca-certificates gnupg lsb-release
# Add Docker’s official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
# Set up the stable Docker repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# Update sources
sudo apt-get update
# Confirm by listing docker community editions available
apt-cache madison docker-ce
# Download and install the Debian package
curl https://desktop-stage.docker.com/linux/main/amd64/77103/docker-desktop.deb --output docker-desktop.deb
sudo apt install ./docker-desktop.deb
# Search Docker Desktop on the Applications menu, or
systemctl --user start docker-desktop
# if you have not already done so, initialize pass
# http://manpages.ubuntu.com/manpages/trusty/man1/pass.1.html
```
