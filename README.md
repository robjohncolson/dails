# Dails (<a href="https://github.com/robjohncolson/dogecoin.git">dogecoin</a> on <a href="https://tails.net/">Tails</a>)

(8-26-24)
Goal of dails is to look at some of the software created for <a href="https://github.com/bitcoin/bitcoin.git">bitcoin</a> and port it over to <a href="https://github.com/dogecoin/dogecoin.git">dogecoin</a> from the ground up.

Inspired by:
<a href="https://github.com/robjohncolson/Bails.git">Bails (Bitcoin on Tails OS)</a> - A secure thumb drive OS with scripts to instlal bitcoin.
<a href="https://github.com/robjohncolson/seedsigner.git">Seedsigner, a hardware signing device for Bitcoin </a>(and most recently Monero).


step a:
Put <a href="https://cdimage.debian.org/debian-cd/current-live/amd64/bt-hybrid/">debian</a> onto a external nvme with minimal software.  EFI boot from USB stick and then finish on a partition on the 1TB NVMe.  Setup dogecoin following the tutorial on <a href="https://raspibolt.org/">raspibolt</a> and adapt toward dogecoin.