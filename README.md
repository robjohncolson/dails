<!DOCTYPE html>
<html lang="en">
<body>
    <h1>Dails (<a href="https://github.com/robjohncolson/dogecoin.git">dogecoin</a> on <a href="https://tails.net/">Tails</a>)</h1>
    <p>Goal of dails is to look at some of the software created for <a href="https://github.com/bitcoin/bitcoin.git">bitcoin</a> and port it over to <a href="https://github.com/dogecoin/dogecoin.git">dogecoin</a> from the ground up.</p>
    <p>Inspired by:</p>
    <ul>
        <li><a href="https://github.com/robjohncolson/Bails.git">Bails (Bitcoin on Tails OS)</a> - A secure thumb drive OS with scripts to install bitcoin.</li>
        <li><a href="https://github.com/robjohncolson/seedsigner.git">Seedsigner, a hardware signing device for Bitcoin</a> (and <a href="https://github.com/Monero-HackerIndustrial/MoneroSigner-Project-Tracking">Monero</a>).</li>
    </ul>

<li>Create a secure OS with minimal software.
    <ul>
        <li>A: Put debian onto a external nvme with minimal software. EFI boot from USB flash drive. Setup dogecoin following the tutorial on raspibolt and adapt toward dogecoin.</li>
        <ul>
            <li>A1: <a href="https://github.com/robjohncolson/dails/blob/main/stepa1.sh">Setup debian on external nvme</a>.</li>
            <ul>
                <li>A1a: <a href="https://github.com/robjohncolson/dails/blob/main/stepa1a.sh">Use debootstrap</a>.</li>
                <li>A1b: ...</li>
                <li>A1c: ...</li>
            </ul>
            <li>A2: <a href="https://github.com/robjohncolson/dails/blob/main/stepa2.sh">Setup EFI boot from USB flash drive</a>.</li>
            <li>A3: <a href="https://github.com/robjohncolson/dails/blob/main/stepa3.sh">Setup dogecoin</a></li>
        </ul>
        <li>B: ...</li>
    </ul>
</li>
</body>
</html>