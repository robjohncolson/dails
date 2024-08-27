<!DOCTYPE html>
<html lang="en">
<body>
    <h1>Dails (<a href="https://github.com/robjohncolson/dogecoin.git">dogecoin</a> on <a href="https://tails.net/">Tails</a>)</h1>
   
<li>Create a secure OS with minimal software.
    <ul>
        <li>A: Put debian onto a external nvme with minimal software. EFI boot from USB flash drive. Setup dogecoin following the tutorial on raspibolt and adapt toward dogecoin.</li>
        <ul>
            <li>A1: <a href="https://github.com/robjohncolson/dails/blob/main/TertiaryA1.sh">Setup debian on external nvme</a>.</li>
            <ul>
                <li>A1a: <a href="https://github.com/robjohncolson/dails/blob/main/QuaternaryA1a.sh">Use debootstrap</a>.</li>
            </ul>
            <li>A2: Setup EFI boot from USB flash drive.</li>
            <li>A3: Use the bitcoin tutorial given on the raspibolt github and adapt it for dogecoin.</li>
        </ul>
    </ul>
</li>

<p>Inspired by:</p>
    <ul>
        <li><a href="https://github.com/robjohncolson/Bails.git">Bails (Bitcoin on Tails OS)</a> - A secure thumb drive OS with scripts to install bitcoin.</li>
        <li><a href="https://github.com/robjohncolson/seedsigner.git">Seedsigner, a hardware signing device for Bitcoin</a> (and <a href="https://github.com/Monero-HackerIndustrial/MoneroSigner-Project-Tracking">Monero</a>).</li>
    </ul>

</body>
</html>