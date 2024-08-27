#! /usr/bin/env python3
# quinary script A1a1: python script gets info from lsblk and writes to file.

import subprocess

def get_block_device_info():
    # Get information about all block devices
    lsblk_output = subprocess.check_output(['lsblk', '-o', 'NAME,SIZE,TYPE,MOUNTPOINT']).decode('utf-8')
    return lsblk_output

def write_to_file(info):
    # Write the information to a file
    with open('block_device_info.txt', 'w') as file:
        file.write(info)

if __name__ == "__main__":