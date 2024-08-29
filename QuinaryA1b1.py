import sys
import subprocess

def get_free_space(device):
    # Get the partition information using the 'parted' command
    output = subprocess.check_output(['sudo', 'parted', device, 'unit', 'MB', 'print']).decode()
    lines = output.splitlines()

    total_size_mb = 0
    used_size_mb = 0

    for line in lines:
        print(f"Parsing line: {line}")  # Debugging output
        if line.startswith("Disk "):
            parts = line.split()
            if len(parts) >= 3:
                try:
                    total_size_mb = float(parts[2].strip('MB'))
                except ValueError:
                    print(f"Warning: Unable to parse total size from line: {line}")
                    continue
        elif "MB" in line and len(line.split()) >= 4:
            parts = line.split()
            try:
                size = float(parts[3].strip('MB'))
                used_size_mb += size
            except ValueError:
                print(f"Warning: Unable to parse used size from line: {line}")
                continue

    # Calculate free space
    free_space_mb = total_size_mb - used_size_mb

    # Debugging output to verify calculations
    print(f"Total size: {total_size_mb} MB, Used size: {used_size_mb} MB, Free space: {free_space_mb} MB")
    
    return free_space_mb

def suggest_partition_table(total_size):
    # Calculate partition sizes based on total size
    alignment = 4  # 4MiB alignment
    efi_size = 512  # MB
    swap_size = min(8192, 4096)  # MB (max 8GB, default 4GB)
    root_size = min(total_size - efi_size - swap_size, 20480)  # MB (remaining space or max 20GB)
    
    # Adjust sizes to align with 4MiB
    efi_size = ((efi_size + alignment - 1) // alignment) * alignment
    root_size = ((root_size + alignment - 1) // alignment) * alignment
    swap_size = ((swap_size + alignment - 1) // alignment) * alignment
    
    # Check if there is enough space for the partitions
    if total_size < (efi_size + root_size + swap_size):
        print("Error: Not enough space for the suggested partitions.")
        return None

    print("Suggested Partition Table for Debian Installation:")
    print(f"1. EFI System Partition: {efi_size}MB (FAT32)")
    print(f"2. Root Partition: {root_size}MB (ext4)")
    print(f"3. Swap Partition: {swap_size}MB (swap)")

    # Create command string for partitioning
    partition_cmd = (
        "sudo parted -s {device} mkpart primary fat32 4MiB {efi_end}MiB && "
        "sudo parted -s {device} set 1 esp on && "
        "sudo parted -s {device} mkpart primary ext4 {efi_end}MiB {root_end}MiB && "
        "sudo parted -s {device} mkpart primary linux-swap {root_end}MiB 100%"
    ).format(device="{device}", efi_end=efi_size+4, root_end=efi_size+root_size+4)

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

    print(partition_cmd)
    #pause script
    input("Executing the following command to create the partition table:)
    # Here you would execute the command using subprocess if needed
    subprocess.run(partition_cmd, shell=True)

# Entry point of the script
if __name__ == "__main__":
    main()