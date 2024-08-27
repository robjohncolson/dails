#! /bin/bash
# A1a: Use debootstrap to install debian onto an external hard drive

# prompt1: step me through using debootstrap to install debian onto an external hard drive
# prompt2: can you collate these steps into a bash script and have it ask the user for input when necessary?

#!/bin/bash

set -e

# Function to prompt for user input with a default value
prompt() {
    local prompt_message="$1"
    local default_value="$2"
    local user_input

    read -r -p "$prompt_message [$default_value]: " user_input
    echo "${user_input:-$default_value}"
}

# Ask for external drive and partition information
echo "This script will install Debian onto an external hard drive."
echo "Please make sure the external hard drive is plugged in."

# Identify external hard drive
DEVICE=$(prompt "Enter the device name for your external hard drive (e.g., /dev/sdb)" "/dev/sdb")
PARTITION="${DEVICE}1"

# Confirm with user
echo "You have chosen the device: $DEVICE with partition: $PARTITION"
confirm=$(prompt "Is this correct? (yes/no)" "yes")

if [[ "$confirm" != "yes" ]]; then
    echo "Exiting script."
    exit 1
fi

# Format and mount the partition
echo "Formatting the partition $PARTITION with ext4 filesystem..."
sudo mkfs.ext4 "$PARTITION"

echo "Creating mount point and mounting the partition..."
sudo mkdir -p /mnt/external
sudo mount "$PARTITION" /mnt/external

# Prompt for Debian release and mirror
RELEASE=$(prompt "Enter the Debian release to install (e.g., bullseye)" "bullseye")
MIRROR=$(prompt "Enter the Debian mirror URL (e.g., http://deb.debian.org/debian)" "http://deb.debian.org/debian")

# Install Debian base system with debootstrap
echo "Installing Debian base system..."
sudo debootstrap --arch amd64 "$RELEASE" /mnt/external "$MIRROR"

# Configure the new system
echo "Entering the chroot environment to configure the new system..."

# Mount necessary filesystems and enter chroot
sudo mount --bind /dev /mnt/external/dev
sudo mount --bind /proc /mnt/external/proc
sudo mount --bind /sys /mnt/external/sys

# Enter chroot
sudo chroot /mnt/external <<EOF
# Configure the system inside chroot
echo "Configuring the system..."
dpkg-reconfigure tzdata
dpkg-reconfigure locales

# Set the root password
echo "Setting the root password..."
passwd

# Install and configure GRUB bootloader
echo "Installing and configuring GRUB bootloader..."
apt update
apt install -y grub-pc
grub-install $DEVICE
update-grub

# Exit chroot
exit
EOF

# Unmount filesystems
echo "Unmounting filesystems..."
sudo umount /mnt/external/dev
sudo umount /mnt/external/proc
sudo umount /mnt/external/sys
sudo umount /mnt/external

# Done
echo "Debian installation completed successfully on $PARTITION."
