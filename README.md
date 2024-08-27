<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dails Documentation</title>
    <style>
        .tree ul {
            display: none;
            list-style-type: none;
        }
        .tree li {
            cursor: pointer;
            margin: 5px 0;
        }
        .tree li.active > ul {
            display: block;
        }
    </style>
</head>
<body>
    <h1>Dails (<a href="https://github.com/robjohncolson/dogecoin.git">dogecoin</a> on <a href="https://tails.net/">Tails</a>)</h1>
    <p>(8-26-24)</p>
    <p>Goal of dails is to look at some of the software created for <a href="https://github.com/bitcoin/bitcoin.git">bitcoin</a> and port it over to <a href="https://github.com/dogecoin/dogecoin.git">dogecoin</a> from the ground up.</p>
    <p>Inspired by:</p>
    <ul>
        <li><a href="https://github.com/robjohncolson/Bails.git">Bails (Bitcoin on Tails OS)</a> - A secure thumb drive OS with scripts to install bitcoin.</li>
        <li><a href="https://github.com/robjohncolson/seedsigner.git">Seedsigner, a hardware signing device for Bitcoin</a> (and <a href="https://github.com/Monero-HackerIndustrial/MoneroSigner-Project-Tracking">Monero</a>).</li>
    </ul>

        <ul>
            <li>Step A
                <ul>
                    <li>Step A1
                        <ul>
                            <li>Step A1A
                                <ul>
                                    <li>Step A1A1</li>
                                    <li>Step A1A2</li>
                                </ul>
                            </li>
                            <li>Step A1B</li>
                        </ul>
                    </li>
                    <li>Step A2</li>
                </ul>
            </li>
            <li>Step B</li>
            <li>Step C</li>
            <li>Step D</li>
            <li>Step E</li>
        </ul>
   
    <script>
        document.querySelectorAll('.tree li').forEach(function(li) {
            li.addEventListener('click', function() {
                li.classList.toggle('active');
            });
        });
    </script>
</body>
</html>