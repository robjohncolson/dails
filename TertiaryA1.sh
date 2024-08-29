#! /bin/bash
# tertiary script A1 : Put debian onto a external nvme with minimal software. 
# Runs all quaternary scripts: A1a, A1b, A1c, etc.

# Run quaternary script A1a: Use debootstrap to install debian onto an external hard drive
./QuaternaryA1a.sh
./QuaternaryA1b.sh