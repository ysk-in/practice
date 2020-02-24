# The Ultimate MySQL Bootcamp: Go from SQL Beginner to Expert

## 進捗管理

全 320 コース  
10 日で終わらせたい  
1 日 32 コース 進める必要がある  
会社 20, 自宅 12 目標でスケジュールする

| 日付     | 場所 | 開始 | 目標 | 実績 | 進捗 | 目標比 |
| -------- | ---- | ---- | ---- | ---- | ---- | ------ |
| 2/20(木) | 会社 | 1    | 20   | 15   | 15   | -5     |
| 2/20(木) | 自宅 | 16   | 32   | 25   | 25   | -7     |
| 2/21(金) | 会社 | 26   | 52   | 26   | 0    | -26    |
| 2/21(金) | 自宅 | 26   | 64   | 26   | 0    | -38    |
| 2/22(土) | 自宅 | 26   | 96   | 72   | 47   | -24    |
| 2/23(日) | 自宅 | 73   | 128  | 130  | 48   | +2     |
| 2/24(月) | 自宅 | 131  | 160  | 171  | 41   | +11    |
| 2/25(火) | 会社 | TBD  | 180  | TBD  | TBD  | TBD    |
| 2/25(火) | 自宅 | TBD  | 192  | TBD  | TBD  | TBD    |
| 2/26(水) | 会社 | TBD  | 212  | TBD  | TBD  | TBD    |
| 2/26(水) | 自宅 | TBD  | 224  | TBD  | TBD  | TBD    |
| 2/27(木) | 会社 | TBD  | 244  | TBD  | TBD  | TBD    |
| 2/27(木) | 自宅 | TBD  | 256  | TBD  | TBD  | TBD    |
| 2/28(金) | 会社 | TBD  | 276  | TBD  | TBD  | TBD    |
| 2/28(金) | 自宅 | TBD  | 288  | TBD  | TBD  | TBD    |
| 2/29(土) | 自宅 | TBD  | 320  | TBD  | TBD  | TBD    |

## ノート

### VARCHAR vs CHAR

151 Note about CHAR and VARCHAR

基本は VARCHAR 使えば良い  
Lookup 性能あげたいときに CHAR を検討 // IP アドレスなど文字長を固定化しても問題ないカラムに向く

- VARCHAR

  - \+ 可変長:ディスク効率よくデータを保持できる
  - \- 操作が高速ではない: CHAR の方が speed up index lookups by 20%(\*1)

- CHAR
  - \- 固定長: スペース(? なのか、正確にまだ理解できてないけど)パディングされるためディスクを多く使う
  - \+ 操作が高速: speed up index lookups by 20%(\*1)

\*1: MySQL v5.0 等の古いバージョンでの話っぽい 最新バージョンでは少し事情は異なるかも

以下のコースで扱われた話題  
course/the-ultimate-mysql-bootcamp-go-from-sql-beginner-to-expert/learn/lecture/7524618#questions/2559516

以下へのリンクが挙げられている  
https://dba.stackexchange.com/questions/2640/what-is-the-performance-impact-of-using-char-vs-varchar-on-a-fixed-size-field/2643#2643

以下で You could analyze the data being stored to see what MySQL recommends for column definition. らしい  
`SELECT * FROM tblname PROCEDURE ANALYSE();`  
実際どんな感じで使えるかは未把握

### 小数 DECIMAL vs DOUBLE vs FLOAT

155 FLOAT and DOUBLE

基本 DECIMAL を使う  
まだあまりちゃんと理解できていないけれど

- DECIMAL 固定小数点型

  - \- 桁数が固定: 柔軟な値にしづらい
  - \+ 計算が正確: ただ計算速度は DOUBLE/FLOAT と比較して遅い?

- DOUBLE 浮動小数点, 倍精度

  - \+ 桁数が柔軟
  - \+ 計算は近似値: ただ計算速度は DECIMAL 比較で早い?

- FLOAT 浮動小数点, 単精度
  - \* 使うべきでない: MySQL では不動小数点の計算は倍精度で行われるため単精度の FLOAT は意図しない計算結果になり易い

(参考) MySQL マニュアル(v5.6 日本語)  
https://dev.mysql.com/doc/refman/5.6/ja/precision-math-numbers.html

> DECIMAL データ型は固定小数点型で、計算は正確です。MySQL では、DECIMAL 型には、NUMERIC、DEC、FIXED という複数のシノニムがあります。整数型も正確値型です。  
> FLOAT データ型および DOUBLE データ型は浮動小数点型で、計算によって近似値が得られます。MySQL では、FLOAT または DOUBLE のシノニムである型は DOUBLE PRECISION および REAL です。

https://dev.mysql.com/doc/refman/5.6/ja/precision-math-examples.html

> 結果が倍精度値になるのは浮動小数点引数の場合だけです。厳密値型引数の場合は、結果も厳密値型になります。

### DATETIME, TIMESTAMPS, created_at, changed_at

167 Working with TIMESTAMPS

DATETIME と TIMESTAMP はどちらも `YYYY/MM/SS HH:MM:SS` 形式で日時を保持するデータ型

https://dev.mysql.com/doc/refman/5.6/ja/datetime.html

> DATETIME 型は、日付と時間の両方の部分を含む値に使用されます。MySQL では、DATETIME 値の取得と表示は 'YYYY-MM-DD HH:MM:SS' 形式で行われます。サポートしている範囲は '1000-01-01 00:00:00' から '9999-12-31 23:59:59' です。

> TIMESTAMP データ型は、日付と時間の両方の部分を含む値に使用されます。TIMESTAMP には、'1970-01-01 00:00:01' UTC から '2038-01-19 03:14:07' UTC の範囲があります。

TIMESTAMP はレコードの作成日時(created_at)や更新日時(changed_at)を保持するのに主に用いられる

```
CREATE TABLE comments (
    content VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

また TIMESTAMP は 上記 MySQL マニュアル引用にある通り タイムゾーン(TZ) = UTC で保存される

対して DATETIME はタイムゾーンの変換は行われず受け取った情報をそのまま格納する  
そのため タイムゾーン(TZ)を意識してデータを扱う必要がある

```
mysql> SHOW VARIABLES LIKE '%time_zone%';
+------------------+--------+
| Variable_name    | Value  |
+------------------+--------+
| system_time_zone | JST    |
| time_zone        | SYSTEM |
+------------------+--------+
2 rows in set (0.00 sec)
```

TZ 指定なしで作成した Database(? Database 単位で保持される認識だけど未確認) はシステムの TZ が使われているっぽい  
Database は TZ=UTC で作成し プログラムから読み書きするときも TZ=UTC で扱うようにするのが無難な気がする
