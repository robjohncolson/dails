#!/usr/bin/env python3

# python script to continue giving commands to the console across the chroot.
# QuinaryA1b2.py
#Initial code from chatgpt.

import os
import subprocess

chroot_dir = "/mnt/debian_chroot"

# Mount file systems
os.system(f"sudo mount --bind /dev {chroot_dir}/dev")
os.system(f"sudo mount --bind /dev/pts {chroot_dir}/dev/pts")
os.system(f"sudo mount --bind /proc {chroot_dir}/proc")
os.system(f"sudo mount --bind /sys {chroot_dir}/sys")

# Run a command in the chroot environment
subprocess.run(['sudo', 'chroot', chroot_dir, '/bin/bash', '-c', 'apt-get update'])

# Unmount file systems after use
os.system(f"sudo umount {chroot_dir}/dev/pts")
os.system(f"sudo umount {chroot_dir}/dev")
os.system(f"sudo umount {chroot_dir}/proc")
os.system(f"sudo umount {chroot_dir}/sys")

# End of initial code from chatgpt.
