#! /bin/bash
# quaternary script A1a: Use debootstrap to install debian onto an external hard drive

# prompt1: step me through using debootstrap to install debian onto an external hard drive
# prompt2: can you collate these steps into a bash script and have it ask the user for input when necessary?

set -e

#The command `set -e` in a bash script instructs the 
#shell to immediately exit the script if any command 
#within it returns a non-zero exit status (indicating an error). 
#This helps prevent the script from continuing to execute subsequent 
#commands when an error occurs, ensuring that issues are caught early.

# Function to prompt for user input with a default value
prompt() {
    local prompt_message="$1"
    local default_value="$2"
    local user_input

    read -r -p "$prompt_message [$default_value]: " user_input
    echo "${user_input:-$default_value}"
}
#claude opus prompt: explain this function to me like im 5
#The function `prompt` is designed to ask the user for input on a specific topic, 
#providing a default value that will be used if the user doesn't enter anything. 
#It uses the `read` command to get user input, with a prompt message that includes 
#the default value in square brackets. If the user doesn't enter anything, the 
#default value is used. The function then returns the user's input, which can be 
#used in the script.

#show all partitions
clear
sudo -S blkid | sed -E 's|(/dev/[^ :]+)|\x1b[31m\1\x1b[0m|g'
#sudo -S is needed to run blkid, otherwise the script will bork.
#sed -E 's|(/dev/[^ :]+)|\x1b[31m\1\x1b[0m|g' is used to color the output in red.


# Ask for external drive and partition information
echo -e "\n"
echo "This script will install Debian onto an external hard drive."
echo "Please make sure the external hard drive is plugged in."
echo -e "\n"


# User already has seen all hard drives which are nvme.  This might be incorrect because 
# the user might have a usb adaptor.
# script should pause right about here.
# Function to pause the script execution
pause() {
    read -n 1 -s -r -p "Press any key to continue..."
    #claude opus prompt: explain this function to me like im 5
    #The `pause` function in the script uses the `read` command with specific options:

    #`-n 1` limits the input to a single character.
    #`-s` makes the input silent, so it doesn't echo to the terminal.
    #`-r` preserves special characters (like backslashes).
    #`-p "Press any key to continue..."` provides a prompt message to the user.
    #`echo` is used to ensure the prompt is displayed before the script pauses.
    echo
}
# Call the pause function
pause

DEVICE=$(prompt "Enter the device name for your external hard drive (e.g., /dev/sdb)" "/dev/sdb")
PARTITION="${DEVICE}1"
clear
sudo -S blkid | sed -E "s|($DEVICE[^ :]*)|\\x1b[31m\\1\\x1b[0m|g"
#claude opus prompt: explain this to me like im 5
#The command `sudo -S blkid | sed -E "s|($DEVICE[^ :]*)|\\x1b[31m\\1\\x1b[0m|g"` is used to display the list of block devices and their UUIDs, 
#with the specified device highlighted in red. Here's a breakdown of the command:

#`sudo -S blkid`: Runs the `blkid` command with superuser privileges. The `-S` option suppresses prompting for a password.
#`| sed -E "s|($DEVICE[^ :]*)|\\x1b[31m\\1\\x1b[0m|g"`: Pipes the output of `blkid` to `sed`. The `sed` command is used to search for the specified device 
#in the output and highlight it by wrapping it in ANSI escape codes for red color.



# Confirm with user
echo "You have chosen the device: $DEVICE"

# Check if the device exists
if [ ! -b "$DEVICE" ]; then
    echo "Error: Device $DEVICE does not exist."
    exit 1
fi

#claude opus prompt: explain this to me like im 5
#The script checks if the specified device exists using the `-b` flag, 
#which is used to check if a block device exists. If the device does not 
#exist, it prints an error message and exits the script with a status of 1.
#parted -s /dev/sdX -- mklabel msdos \
#    mkpart primary fat32 64s 4MiB \
#    mkpart primary fat32 4MiB -1s
#The above command is considered best practice for creating partitions on a cheap flash drive.
#https://www.gnu.org/software/parted/manual/html_node/mkpart.html
echo "let's look at the partitions on this drive."
sudo -S parted "$DEVICE" print
python3 QuinaryA1b1.py
echo "if you want to partition this drive, lets do it now."
pause
sudo -S parted "$DEVICE"
echo "let's take a break before we go on."
pause



# Format and mount the partition
echo "Formatting the partition $PARTITION with ext4 filesystem..."
sudo mkfs.ext4 "$PARTITION"

echo "Creating mount point and mounting the partition..."
sudo mkdir -p /mnt/external
sudo mount "$PARTITION" /mnt/external

# Prompt for Debian release and mirror
RELEASE=$(prompt "Enter the Debian release to install (e.g., bullseye)" "bullseye")
MIRROR=$(prompt "Enter the Debian mirror URL" "http://deb.debian.org/debian")

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
sudo umount /mnt/external/sys
sudo umount /mnt/external/proc
sudo umount /mnt/external/dev
sudo umount /mnt/external

# Done
echo "Debian installation completed successfully on $PARTITION."