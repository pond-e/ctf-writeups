<html>
    <head>
        <title>数列屋</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>レジ</h1>
        <form action="purchase.php" method="post">
            <table>
                <tr>
                    <th>商品名</th>
                    <th>単価</th>
                    <th>個数</th>
                    <th>小計</th>
                </tr>
                <tr>
                    <td>フィボナッチ数列</td>
                    <td>1000</td>
                    <td><?=$_POST["quantity1"]?></td>
                    <td><?=eval('return ' . $_POST["quantity1"] . '*1000;')?></td>
                </tr>
                <tr>
                    <td>素数列</td>
                    <td>2000</td>
                    <td><?=$_POST["quantity2"]?></td>
                    <td><?=eval('return ' . $_POST["quantity2"] . '*2000;')?></td>

                </tr>
                <tr>
                    <td>三角数列</td>
                    <td>1500</td>
                    <td><?=$_POST["quantity3"]?></td>
                    <td><?=eval('return ' . $_POST["quantity3"] . '*1500;')?></td>
                </tr>
            </table>
            <p>合計金額は<?=eval('return ' . $_POST["quantity1"] . '*1000+' . $_POST["quantity2"] . '*2000+' . $_POST["quantity3"] . '*1500;')?>円です。この画面を実店舗の店員にご提示ください。</p>
        </form>
    </body>
</html>