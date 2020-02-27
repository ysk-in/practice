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
| 2/23(日) | 自宅 | 73   | 128  | 130  | 48   | 2      |
| 2/24(月) | 自宅 | 131  | 160  | 171  | 41   | 11     |
| 2/25(火) | 会社 | 172  | 180  | 193  | 22   | 13     |
| 2/25(火) | 自宅 | 194  | 192  | 205  | 12   | 13     |
| 2/26(水) | 会社 | 206  | 212  | 211  | 6    | -1     |
| 2/26(水) | 自宅 | 212  | 224  | 220  | 9    | -4     |
| 2/27(木) | 会社 | 221  | 244  | 251  | 31   | 7      |
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

### CAST(データ型の変換), BETWEEN

185 Between

DATETIME 型や DATE 型を BETWEEN で比較する場合 CAST()を適切に使うべき

https://dev.mysql.com/doc/refman/5.6/ja/comparison-operators.html#operator_between

> 日付または時間の値とともに BETWEEN を使用したときの結果を最適にするには、CAST() を使用して明示的に値を目的のデータ型に変換します。例 : DATETIME を 2 つの DATE 値と比較する場合は、DATE 値を DATETIME 値に変換します。DATE との比較で '2001-1-1' などの文字列定数を使用する場合は、文字列を DATE にキャストします。

CAST 使用例 `SELECT CAST('2000-01-01' AS DATETIME);`

### IFNULL

204 Left Join

NULL を任意の値で置換する方法  
以下のように total_spent が NULL になるものがあるとき

```
mysql> SELECT
    ->     first_name, last_name, SUM(amount) AS total_spent
    -> FROM
    ->     customers
    ->         LEFT JOIN
    ->     orders ON customers.id = orders.customer_id
    -> GROUP BY customers.id
    -> ORDER BY total_spent;
+------------+-----------+-------------+
| first_name | last_name | total_spent |
+------------+-----------+-------------+
| David      | Bowie     |        NULL |
| Blue       | Steele    |        NULL |
| Boy        | George    |      135.49 |
| Bette      | Davis     |      450.25 |
| George     | Michael   |      813.17 |
+------------+-----------+-------------+
5 rows in set (0.00 sec)

mysql>
```

IFNULL で以下のように置換できる

```
mysql> SELECT
    ->     first_name, last_name, IFNULL(SUM(amount), 0) AS total_spent
    -> FROM
    ->     customers
    ->         LEFT JOIN
    ->     orders ON customers.id = orders.customer_id
    -> GROUP BY customers.id
    -> ORDER BY total_spent;
+------------+-----------+-------------+
| first_name | last_name | total_spent |
+------------+-----------+-------------+
| David      | Bowie     |        0.00 |
| Blue       | Steele    |        0.00 |
| Boy        | George    |      135.49 |
| Bette      | Davis     |      450.25 |
| George     | Michael   |      813.17 |
+------------+-----------+-------------+
5 rows in set (0.00 sec)

mysql>
```

### 主キー id を定義しないケース

243 Cloning Instagram's DB: Likes Schema

いいね の情報を保持するテーブル likes を定義することを考える  
例えば以下のスキーマ定義が考えられる

```
CREATE TABLE likes (
    user_id INT NOT NULL,
    photo_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id)
        REFERENCES users (id)
        ON DELETE CASCADE,
    FOREIGN KEY (photo_id)
        REFERENCES photos (id)
        ON DELETE CASCADE,
    PRIMARY KEY (user_id , photo_id)
);
```

ここで PRIMARY KEY は user_id, photo_id として フィールド id は定義していない  
この理由は ある user がある photo へ いいね をするのは最大 1 回の仕様だから  
つまり user と photo が同じレコードが 2 以上存在してはいけないため

### タグ(Tag)情報の持ち方

248 Cloning Instagram's DB: Hashtags Part 1

例えば Instagram の写真へのタグ (ブログの記事へのタグでもなんでも) のタグ情報の持ち方について  
3 パターンの情報の持ち方を紹介 それぞれのメリット(+), デメリット(-)は以下が挙げられていた

1. photos のテーブルに tags カラムを追加して持つ  
   \+ 実装が簡単  
   \+ ある写真の詳細画面でタグ一覧を表示するみたいなケースでは高速で動作する  
   \- タグ上限数がカラムの最大長に依存する  
   \- タグに追加情報の付与が不可  
   \- タグ検索を実装するのが難しくなる
2. tags テーブルを追加し タグ情報 と 関連する写真の情報を保持する  
    (同名タグであっても 関連する photo が異なれば tags テーブルには 1 レコード追加する)  
   \+ 実装は比較的簡単  
   \- tags テーブルのレコード数が増加し易く性能は劣化しやすい  
   \+ タグ上限数が大きい(無限)  
   \+ タグに追加情報の付与が可能  
   \- タグ検索は容易ではない？
3. tags テーブルを追加しタグ情報を保持 また photo_tags テーブルを追加し photo と tags の関連を保持  
    (同名タグなら tags テーブルには 1 レコードのみ保持  
    同名タグが関連する写真数分 photo_tags テーブルにはレコードが追加される)  
   \- 実装は簡単ではない タグ追加時 tags テーブルへのレコード追加要否の判断が必要, orphan 対策が必要  
   \+ 性能が劣化しづらい photos テーブルに tags カラム追加よりは劣るケースもあると考えられる(と思う)  
   \+ タグ上限数が大きい(無限)  
   \+ タグに追加情報の付与が可能  
   \+ タグ検索が実装しやすい

タグはイメージし易いけど テーブル定義いい加減に考えると 誤って 2 の手法で対応しちゃったみたいなことはありそう
使い方/使われ方でどのパターンが良いかは変わる
