

# Dails ([dogecoin](https://github.com/robjohncolson/dogecoin.git) on
[Tails](https://tails.net/))

* Create a secure OS with minimal software. 

  * A: [Put debian onto a external nvme with minimal software. EFI boot from USB flash drive. Setup dogecoin following the tutorial on raspibolt and adapt toward dogecoin.](https://github.com/robjohncolson/dails/blob/main/SecondaryA.sh).
    * A1: [Setup debian on external nvme](https://github.com/robjohncolson/dails/blob/main/TertiaryA1.sh).
      * A1a: [Get info from shell for variables to use when setting up debian on external nvme.](https://github.com/robjohncolson/dails/blob/main/QuaternaryA1a.sh).
        * A1a1: [Python script gets info from lsblk and writes to file.](https://github.com/robjohncolson/dails/blob/main/QuinaryA1a1.py)
      * A1b: [Use debootstrap to install debian onto an external hard drive](https://github.com/robjohncolson/dails/blob/main/QuaternaryA1b.sh).
        * A1b1: [Python script to suggest partition table and create partitions.](https://github.com/robjohncolson/dails/blob/main/QuinaryA1b1.py)
        * A1b2: Python script to continue giving commands to the console across the chroot (not implemented yet).
    * A2: Setup EFI boot from USB flash drive (not implemented yet).
    * A3: Follow the [RaspiBolt guide](https://raspibolt.org/guide/raspberry-pi/) for Bitcoin and adapt it for Dogecoin (not implemented yet).
  * B: Add clonezilla to the OS (not implemented yet).

Inspired by:

  * [Bails (Bitcoin on Tails OS)](https://github.com/robjohncolson/Bails.git) \- A secure thumb drive OS with scripts to install bitcoin.
  * [Seedsigner, a hardware signing device for Bitcoin](https://github.com/robjohncolson/seedsigner.git) (and [Monero](https://github.com/Monero-HackerIndustrial/MoneroSigner-Project-Tracking)).



## Script List
