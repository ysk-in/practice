# 達人に学ぶ SQL 徹底指南書 第 2 版 初級者で終わりたくないあなたへ

## SELECT 文の処理順序

SELECT (Transact-SQL)  
https://docs.microsoft.com/en-us/sql/t-sql/queries/select-transact-sql

1. FROM
1. ON
1. JOIN
1. WHERE
1. GROUP BY
1. WITH CUBE or WITH ROLLUP
1. HAVING
1. SELECT
1. DISTINCT
1. ORDER BY
1. TOP

MySQL の公式ドキュメントでは見当たらない

## ユーザ定義変数

9.4 User-Defined Variables  
https://dev.mysql.com/doc/refman/8.0/en/user-variables.html

プログラム乾実行するときは基本プレースホルダー使用するはず(?)なので、使うことないかも。

```sql
SET @head_cnt = 3;

SELECT S1.seat AS start_seat, "〜", S2.seat AS end_seat
FROM Seats AS S1, Seats AS S2
WHERE S2.seat = S1.seat + (@head_cnt -1)
	AND NOT EXISTS(
		SELECT *
        FROM Seats AS S3
        WHERE S3.seat BETWEEN S1.seat AND S2.seat
			AND S3.status <> "空"
    )
;
```

## MySQL カラムの Check 制約

https://dev.mysql.com/doc/refman/8.0/en/create-table-check-constraints.html

8.0.16 以降は CREATE TABLE 時に CHECK 制約指定可能

```sql
CREATE TABLE Seats2 (
    seat INTEGER NOT NULL PRIMARY KEY,
    line_id CHAR(1) NOT NULL,
    status CHAR(2) NOT NULL CHECK (status IN ('空' , '占'))
);
```

status が不正な行を追加しようとするとエラーになる

> mysql> insert into Seats2 values (16, "D", "A");  
> ERROR 3819 (HY000): Check constraint 'seats2_chk_1' is violated.  
> mysql>

8.0.16 より前は CREATE TABLE に CHECK 指定しても無視されてたっぽい  
https://dev.mysql.com/doc/refman/5.6/ja/create-table.html

> CHECK 句は、すべてのストレージエンジンによって解析されますが、無視されます。

## カーディナリティ Cardinality

11 章

https://dev.mysql.com/doc/refman/5.6/ja/show-index.html

> このインデックス内の一意の値の数の推定値

ID は必ず一意になる値を設定するため、カーディナリティが高い。  
性別 は値の種類が少ないため、カーディナリティが低い。

> カーディナリティーが高いほど、MySQL が結合を実行するときにこのインデックスを使用する可能性は高くなります。

カーディナリティが高いカラムはインデックスの効果が高い。

## マテリアライズドビュー Materialized View

11 章

クエリ結果を実在的なデータとして保存(ストレージ容量を使用)するビュー  
性能はテーブルとほとんど同じ  
データの同期に注意が必要

MySQL は未サポート  
PostgreSQL はサポート

## RDB の 課題 と NoSQL

RDB の課題

1. 性能と信頼性のトレードオフ  
   厳密なトランザクションのために、データを一元管理する必要がある。  
   実現するためストレージ を共有する構成をとっている。  
   そのため、スケールアウトできない。
1. データモデルの限界  
   苦手なデータの種類がある。  
   グラフと非構造化データ。

   非構造データの代表例は XML, JSON  
   非構造化データの定義は、もともと RDB のテーブルに格納しやすいデータ(CSV など)を構造化データと呼ぶのに対し、テーブルでは扱いデータをひとまとめに非構造化データと呼ぶ。  
   タグがどのような情報を表すかの規則は定まっているが、どれだけのサイズ情報を持つかが決まっていないもの。

上記課題を RDB と異なるアプローチで解消する NoSQL

NoSQL と言う言葉の定義は RDB とは異なるアーキテクチャやデータモデルに基づくデータベース と言う程度の緩いもの

1. 性能問題の解決: Key Value Store(KVS)  
   厳密なトランザクション制御によるデータ整合性を諦める を実現したのが KVS。  
   非常にシンプルな Key によって一意に決まる Value の構造飲みを持つ。  
   Redis などが KVS の機能を備える。  
   複数のデータベースのインスタンスでクラスタを構成し、スケールアウトによるパフォーマンス向上が可能。
1. 非構造化データの解決:ドキュメント指向型 DB  
   JSON, XML のような自由度の高いデータを RDB のテーブルに変換することなく扱う機能を持つ ドキュメント指向型 DB。  
   MongoDB や CouchDB が該当。

## NULL 排除

22 章

1. デフォルト値を入れられないか検討
1. どうしようもない場合だけ NULL を許可

### コード情報

企業コード, 顧客コード, 県コード, 性別コード など は未コード化用コードを割り振る。  
コードは必ず文字型で宣言する(数値型は使わない)。

- 不明は XXXXX 等で表現する。  
  コードは多くの場合数字が使われる。ありえないと思って 99999 を使うと、現実に出現してしまう可能性があるから。
- ソートを意図通り行いたい場合は適宜 0 埋めして桁数を揃える。
- カラム定義時 `code CHAR(5) DEFAULT "XXXXX"` みたいな感じ

性別をコード化する場合、ISO の性別コードが使える。  
https://ja.wikipedia.org/wiki/ISO_5218  
センシティブな情報を扱う場合、国際規格とか使いたい。

性別コードは以下の記事が面白かった。

システムで「性別」の情報を扱う前に知っておくべきこと
https://qiita.com/aoshirobo/items/32deb45cb8c8b87d65a4

### 数値

0 で代替する を基本と考える  
どうしても 0 と NULL を区別したい場合だけ、NULL を許可する。

### 日付

Kindle のマーカ設定した記載参照

## MySQL vs PostgreSQL
機能的には PostgreSQL の方が MySQL よりも優れている気がする(?)  

PostgreSQL 人気は伸びてるっぽい  
https://db-engines.com/en/ranking_trend  

