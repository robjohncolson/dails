# Dails (dogecoin on Tails)

(8-26-24)
Goal of dails is to look at some of the software created for bitcoin and port it over to dogecoin from the ground up.

Inspired by:
Bails (Bitcoin on Tails OS) - A secure thumb drive OS with scripts to instlal bitcoin.
Seedsigner, a hardware signing device for Bitcoin (and most recently Monero).


Initial plan:
Put debian onto a external nvme with minimal software.  EFI boot from USB stick and then finish on a partition on the 1TB NVMe.  Setup dogecoin following the tutorial on <a href="https://raspibolt.org/">raspibolt</a> and adapt toward dogecoin.