DROP DATABASE IF EXISTS tatsujin_ensyu7;
CREATE DATABASE tatsujin_ensyu7;
USE tatsujin_ensyu7;

DROP TABLE IF EXISTS shohin;

CREATE TABLE shohin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `type` VARCHAR(100) NOT NULL,
    price INT NOT NULL
);

INSERT shohin (`name`, `type`, price) VALUES
	("Tシャツ", "衣服", 1000),
	("穴あけパンチ", "事務用品", 500),
	("カッターシャツ", "衣服", 4000),
	("包丁", "キッチン用品", 3000),
	("圧力鍋", "キッチン用品", 6800),
	("フォーク", "キッチン用品", 500),
	("おろしがね", "キッチン用品", 880),
	("ボールペン", "事務用品", 100)
;

SELECT `name`, `type`, price FROM (
	SELECT `name`, `type`, price, AVG(price) OVER (PARTITION BY `type`) AS avg_price FROM shohin
)  as tmp WHERE price > avg_price;


DROP TABLE IF EXISTS Reservations;

CREATE TABLE Reservations (
    reserver VARCHAR(30) PRIMARY KEY,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

INSERT INTO Reservations VALUES
    ('木村', '2018-10-26', '2018-10-27'),
    ('荒木', '2018-10-28', '2018-10-31'),
    ('堀',   '2018-10-31', '2018-11-01'),
    ('山本', '2018-11-03', '2018-11-04'),
    ('内田', '2018-11-03', '2018-11-05'),
    ('水谷', '2018-11-06', '2018-11-06')
;

SELECT reserver, next_reserver
  FROM (SELECT reserver,
               start_date,
               end_date,
               MAX(start_date) OVER (ORDER BY start_date
                                      ROWS BETWEEN 1 FOLLOWING 
                                               AND 1 FOLLOWING) AS next_start_date,
               MAX(reserver)   OVER (ORDER BY start_date
                                      ROWS BETWEEN 1 FOLLOWING 
                                               AND 1 FOLLOWING) AS next_reserver
          FROM Reservations) TMP
 WHERE next_start_date BETWEEN start_date AND end_date;

-- SELECT reserver,
--                start_date,
--                end_date,
--                MAX(start_date) OVER (ORDER BY start_date
--                                       ROWS BETWEEN 1 FOLLOWING 
--                                                AND 1 FOLLOWING) AS next_start_date,
--                MAX(reserver)   OVER (ORDER BY start_date
--                                       ROWS BETWEEN 1 FOLLOWING 
--                                                AND 1 FOLLOWING) AS next_reserver
--           FROM Reservations;


-- ENSYU 7-1 PREPARE
DROP TABLE IF EXISTS accounts;

CREATE TABLE Accounts (
    prc_date DATE NOT NULL,
    prc_amt INTEGER NOT NULL,
    PRIMARY KEY (prc_date)
);

INSERT INTO Accounts VALUES
    ('2018-10-26',  12000 ),
    ('2018-10-28',   2500 ),
    ('2018-10-31', -15000 ),
    ('2018-11-03',  34000 ),
    ('2018-11-04',  -5000 ),
    ('2018-11-06',   7200 ),
    ('2018-11-11',  11000 )
;

SELECT 
    *
FROM
    accounts;

select prc_date, prc_amt, avg(prc_amt) over (order by prc_date rows between 2 preceding and current row) as mov_avg from accounts;

-- ENSYU 7-1 難しい...
SELECT 
    prc_date,
    a1.prc_amt,
    (SELECT 
            AVG(prc_amt)
        FROM
            accounts a2
        WHERE
            a1.prc_date >= a2.prc_date
                AND (SELECT 
                    COUNT(*)
                FROM
                    accounts a3
                WHERE
                    a3.prc_date BETWEEN a2.prc_date AND a1.prc_date) <= 3) AS mvg_sum
FROM
    accounts a1
ORDER BY prc_date;

-- ENSYU 7-2
-- select prc_date, prc_amt, 
-- case
--  when count(*) over (order by prc_date rows between 2 preceding and current row) >= 3
-- 	then avg(prc_amt) over (order by prc_date rows between 2 preceding and current row)
-- else null
-- end as mov_avg from accounts;

select prc_date, prc_amt, 
case
	when cnt >=3 then mov_avg
    else NULL
end as mov_avg 
from (select prc_date, prc_amt, avg(prc_amt) over (order by prc_date rows between 2 preceding and current row) as mov_avg, 
count(*) over (order by prc_date rows between 2 preceding and current row) as cnt from accounts) as tmp;

