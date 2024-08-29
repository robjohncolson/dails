<!DOCTYPE html>

<html lang="en">

<body>

    <h1>Dails (<a href="https://github.com/robjohncolson/dogecoin.git">dogecoin</a> on <a href="https://tails.net/">Tails</a>)</h1>

   

<li>Create a secure OS with minimal software.

    <ul>

        <li>A: <a href="https://github.com/robjohncolson/dails/blob/main/SecondaryA.sh">Put debian onto a external nvme with minimal software. EFI boot from USB flash drive. Setup dogecoin following the tutorial on raspibolt and adapt toward dogecoin.</a>.</li>

        <ul>

            <li>A1: <a href="https://github.com/robjohncolson/dails/blob/main/TertiaryA1.sh">Setup debian on external nvme</a>.</li>

            <ul>

                <li>A1a: <a href="https://github.com/robjohncolson/dails/blob/main/QuaternaryA1a.sh">Get info from shell for variables to use when setting up debian on external nvme.</a>.</li>

                <ul>

                    <li>A1a1: <a href="https://github.com/robjohncolson/dails/blob/main/QuinaryA1a1.py">Python script gets info from lsblk and writes to file.</a></li>

                </ul>

                <li>A1b: <a href="https://github.com/robjohncolson/dails/blob/main/QuaternaryA1b.sh">Use debootstrap to install debian onto an external hard drive</a>.</li>

                <ul>

                    <li>A1b1: <a href="https://github.com/robjohncolson/dails/blob/main/QuinaryA1b1.py">Python script to suggest partition table and create partitions.</a></li>

                    <li>A1b2: Python script to continue giving commands to the console across the chroot (not implemented yet).</li>

                </ul>

            </ul>

            <li>A2: Setup EFI boot from USB flash drive (not implemented yet).</li>

            <li>A3: Follow the <a href="https://raspibolt.org/guide/raspberry-pi/">RaspiBolt guide</a> for Bitcoin and adapt it for Dogecoin (not implemented yet).</li>

        </ul>

        <li>B: Add clonezilla to the OS (not implemented yet).</li>

    </ul>

</li>



<p>Inspired by:</p>

    <ul>

        <li><a href="https://github.com/robjohncolson/Bails.git">Bails (Bitcoin on Tails OS)</a> - A secure thumb drive OS with scripts to install bitcoin.</li>

        <li><a href="https://github.com/robjohncolson/seedsigner.git">Seedsigner, a hardware signing device for Bitcoin</a> (and <a href="https://github.com/Monero-HackerIndustrial/MoneroSigner-Project-Tracking">Monero</a>).</li>

    </ul>



</body>

</html>