#! /bin/python
#python3 QuinaryA1b1.py

import sys  # Ensure this import is present
import subprocess  # Import subprocess for command execution

def get_free_space(device):
    # Get the partition information using the 'parted' command
    output = subprocess.check_output(['sudo', 'parted', device, 'unit', 'MB', 'print']).decode()
    lines = output.splitlines()

    total_size_mb = 0
    used_size_mb = 0

    for line in lines:
        print(f"Parsing line: {line}")  # Debugging output

        if "MB" in line:
            parts = line.split()
            if len(parts) >= 3:
                try:
                    size = float(parts[1].strip('MB'))
                    if parts[0].isdigit():  # If first part is a number (partition number)
                        total_size_mb += size
                    elif 'used' in line.lower():  # Check for used space keyword
                        used_size_mb += size
                except ValueError:
                    continue  # Skip lines that don't contain relevant numeric data

    # Calculate free space
    free_space_mb = total_size_mb - used_size_mb

    # Debugging output to verify calculations
    print(f"Total size: {total_size_mb} MB, Used size: {used_size_mb} MB, Free space: {free_space_mb} MB")
    
    return free_space_mb


def suggest_partition_table(total_size):
    # Calculate partition sizes based on total size
    efi_size = 512  # MB
    root_size = 20480  # MB (20GB)
    swap_size = 4096  # MB (4GB)
    
    # Check if there is enough space for the partitions
    if total_size < (efi_size + root_size + swap_size):
        print("Error: Not enough space for the suggested partitions.")
        return None

    print("Suggested Partition Table for Debian Installation:")
    print(f"1. EFI System Partition: {efi_size}MB (FAT32)")
    print(f"2. Root Partition: {root_size // 1024}GB (ext4)")
    print(f"3. Swap Partition: {swap_size}MB (swap)")

    # Create command string for partitioning
    partition_cmd = (
        "sudo parted {device} mklabel msdos && "
        "sudo parted -s {device} mkpart primary fat32 1MiB {efi_size}MiB && "
        "sudo parted -s {device} mkpart primary ext4 {efi_size}MiB {root_size}MiB && "
        "sudo parted -s {device} mkpart primary linux-swap {root_size}MiB {swap_size}MiB"
    ).format(efi_size=efi_size, root_size=root_size, swap_size=swap_size)

    return partition_cmd

def main():
    # Get the device name from user input
    device = input("Enter the device name for your external hard drive (e.g., /dev/sdb): ")

    # Get the available free space on the device
    total_size = get_free_space(device)

    print(f"Available free space on {device}: {total_size}MB")

    partition_cmd = suggest_partition_table(total_size)  # Call the function to suggest partition table

    if partition_cmd is None:
        return  # Exit if there was an error

    # Ask for user agreement
    agree = input("Do you agree with the suggested partition table? (y/n): ")
    if agree.lower() != 'y':
        print("Exiting script.")
        return

    partition_cmd = partition_cmd.format(device=device)

    print("Executing the following command to create the partition table:")
    print(partition_cmd)
    # Here you would execute the command using subprocess if needed
    # subprocess.run(partition_cmd, shell=True)

# Entry point of the script
if __name__ == "__main__":
    main()