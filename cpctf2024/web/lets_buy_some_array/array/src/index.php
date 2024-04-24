
<!DOCTYPE HTML>
<html>
    <head>
        <title>数列屋</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>数列屋へようこそ</h1>
        <form action="purchase.php" method="post">
            <table>
                <tr>
                    <th>商品名</th>
                    <th>単価</th>
                    <th>個数</th>
                </tr>
                <tr>
                    <td>フィボナッチ数列</td>
                    <td>1000</td>
                    <td><input type="number" name="quantity1" value=""></td>
                </tr>
                <tr>
                    <td>素数列</td>
                    <td>2000</td>
                    <td><input type="number" name="quantity2" value=""></td>
                </tr>
                <tr>
                    <td>三角数列</td>
                    <td>1500</td>
                    <td><input type="number" name="quantity3" value=""></td>
                </tr>
            </table>
            <input type="submit" value="確認">
        </form>
    </body>
</html>