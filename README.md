# Dails (dogecoin on Tails)

(8-26-24)
Goal of dails is to look at some of the software created for bitcoin and port it over to dogecoin from the ground up.

Inspired by:
<a href="https://github.com/robjohncolson/Bails.git">Bails (Bitcoin on Tails OS)</a> - A secure thumb drive OS with scripts to instlal bitcoin.
<a href="https://github.com/robjohncolson/seedsigner.git">Seedsigner, a hardware signing device for Bitcoin </a>(and most recently Monero).


Initial plan:
Put debian onto a external nvme with minimal software.  EFI boot from USB stick and then finish on a partition on the 1TB NVMe.  Setup dogecoin following the tutorial on <a href="https://raspibolt.org/">raspibolt</a> and adapt toward dogecoin.