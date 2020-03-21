DROP DATABASE IF EXISTS tatsujin_ensyu10;
CREATE DATABASE tatsujin_ensyu10;
USE tatsujin_ensyu10;

DROP TABLE IF EXISTS Digits;

CREATE TABLE Digits (
    digit INTEGER PRIMARY KEY
);

INSERT INTO Digits VALUES
    (0),
    (1),
    (2),
    (3),
    (4),
    (5),
    (6),
    (7),
    (8),
    (9)
;

SELECT D1.digit + (D2.digit * 10) AS seq
FROM Digits AS D1 JOIN Digits AS D2
ORDER BY seq;

SELECT D1.digit + (D2.digit * 10) + (D3.digit * 100) AS seq
FROM Digits AS D1
	JOIN Digits AS D2
    JOIN Digits AS D3
WHERE D1.digit + (D2.digit * 10) + (D3.digit * 100)
	BETWEEN 1 AND 542
-- HAVING seq BETWEEN 1 AND 542
ORDER BY seq;

DROP VIEW IF EXISTS Sequence;

CREATE VIEW Sequence (seq) AS
SELECT D1.digit + (D2.digit * 10) + (D3.digit * 100)
FROM Digits AS D1
	JOIN Digits AS D2
    JOIN Digits AS D3;

SELECT seq
FROM Sequence
WHERE seq BETWEEN 1 AND 100
ORDER BY seq;


DROP TABLE IF EXISTS SeqTbl;

CREATE TABLE SeqTbl (
    seq INTEGER PRIMARY KEY
);

INSERT INTO SeqTbl VALUES
    (1),
    (2),
    (4),
    (5),
    (6),
    (7),
    (8),
    (11),
    (12)
;

SELECT seq
FROM Sequence
WHERE seq BETWEEN 1 AND 12
	AND seq NOT IN (SELECT seq FROM SeqTbl);


DROP TABLE IF EXISTS Seats;

CREATE TABLE Seats (
    seat INTEGER NOT NULL PRIMARY KEY,
    `status` CHAR(2) NOT NULL CHECK (status IN ('空' , '占'))
);

INSERT INTO Seats VALUES
    (1,  '占'),
    (2,  '占'),
    (3,  '空'),
    (4,  '空'),
    (5,  '空'),
    (6,  '占'),
    (7,  '空'),
    (8,  '空'),
    (9,  '空'),
    (10, '空'),
    (11, '空'),
    (12, '占'),
    (13, '占'),
    (14, '空'),
    (15, '空')
;

SET @head_cnt = 3;

SELECT S1.seat AS start_seat, "〜", S2.seat AS end_seat
FROM Seats AS S1, Seats AS S2
WHERE S2.seat = S1.seat + (@head_cnt -1)
	AND NOT EXISTS(
		SELECT *
        FROM Seats AS S3
        WHERE S3.seat BETWEEN S1.seat AND S2.seat
			AND S3.`status` <> "空"
    )
;

SELECT seat, "〜", seat + (@head_cnt - 1)
FROM (
	SELECT seat, MAX(seat) OVER(
		ORDER BY seat
--         ROWS BETWEEN (@head_cnt - 1) FOLLOWING
-- 			AND (@head_cnt - 1) FOLLOWING
        ROWS BETWEEN 2 FOLLOWING AND 2 FOLLOWING
	) AS end_seat
    FROM Seats
    WHERE `status` = "空"
)　tmp
WHERE end_seat - seat = (@head_cnt -1)
;

DROP TABLE IF EXISTS Seats2;

CREATE TABLE Seats2 (
    seat INTEGER NOT NULL PRIMARY KEY,
    line_id CHAR(1) NOT NULL,
    `status` CHAR(2) NOT NULL CHECK (status IN ('空' , '占'))
);

INSERT INTO Seats2 VALUES
    (1, 'A', '占'),
    (2, 'A', '占'),
    (3, 'A', '空'),
    (4, 'A', '空'),
    (5, 'A', '空'),
    (6, 'B', '占'),
    (7, 'B', '占'),
    (8, 'B', '空'),
    (9, 'B', '空'),
    (10,'B', '空'),
    (11,'C', '空'),
    (12,'C', '空'),
    (13,'C', '空'),
    (14,'C', '占'),
    (15,'C', '空')
;

SELECT S1.seat AS start_seat, "〜", S2.seat AS end_seat
FROM Seats2 AS S1, Seats2 AS S2
WHERE S2.seat = S1.seat + (@head_cnt -1)
	AND NOT EXISTS(
		SELECT *
        FROM Seats2 AS S3
        WHERE S3.seat BETWEEN S1.seat AND S2.seat
			AND (
				S3.`status` <> "空"
                OR S3.line_id <> S1.line_id
			)
    )
;


SELECT seat, "〜", seat + (@head_cnt - 1)
FROM (
	SELECT seat, MAX(seat) OVER(
		PARTITION BY line_id
		ORDER BY seat
--         ROWS BETWEEN (@head_cnt - 1) FOLLOWING
-- 			AND (@head_cnt - 1) FOLLOWING
        ROWS BETWEEN 2 FOLLOWING AND 2 FOLLOWING
	) AS end_seat
    FROM Seats2
    WHERE `status` = "空"
)　tmp
WHERE end_seat - seat = (@head_cnt -1)
;

DROP TABLE IF EXISTS MyStock;

CREATE TABLE MyStock (
    deal_date DATE PRIMARY KEY,
    price INTEGER
); 

INSERT INTO MyStock VALUES
    ('2018-01-06', 1000),
    ('2018-01-08', 1050),
    ('2018-01-09', 1050),
    ('2018-01-12', 900),
    ('2018-01-13', 880),
    ('2018-01-14', 870),
    ('2018-01-16', 920),
    ('2018-01-17', 1000),
    ('2018-01-18', 2000)
;

CREATE VIEW MyStockUpSeq(deal_date, price, row_num)
AS
SELECT deal_date, price, row_num
FROM(
	SELECT deal_date, price,
	CASE SIGN(
		price - MAX(price) OVER(
			ORDER BY deal_date
			ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING)
        )
		WHEN 1 THEN "up"
		WHEN 0 THEN "stay"
		WHEN -1 THEN "down"
		ELSE NULL
	END AS diff,
    ROW_NUMBER() OVER (ORDER BY deal_date) AS row_num
	FROM MyStock
) tmp
WHERE diff = "up";

-- gap が何を示す列なのか理解できていない...
SELECT MIN(deal_date) AS start_date, "〜", MAX(deal_date) AS end_date
FROM (
	SELECT M1.deal_date,
		COUNT(M2.row_num) - CAST(MIN(M1.row_num) AS SIGNED) AS gap
    FROM MyStockUpSeq AS M1
	JOIN MyStockUpSeq AS M2
		ON M2.row_num <= M1.row_num
	GROUP BY M1.deal_date
) tmp
GROUP BY gap
;


-- ENSYU 10-1
SELECT s.seq
FROM Sequence AS s
WHERE s.seq BETWEEN 1 AND 12
	AND NOT EXISTS(
		SELECT seq
        FROM SeqTbl
        WHERE s.seq = seq
	)
;

-- ENSYU 10-2
SELECT S1.seat AS start_seat, "〜", S2.seat AS end_seat
FROM Seats AS S1, Seats AS S2
WHERE S2.seat = S1.seat + (@head_cnt -1)
	AND NOT EXISTS(
		SELECT *
        FROM Seats AS S3
        WHERE S3.seat BETWEEN S1.seat AND S2.seat
			AND S3.`status` <> "空"
    )
;

SELECT S1.seat AS start_seat, "〜", S2.seat AS end_seat
FROM Seats AS S1, Seats AS S2, Seats AS S3
WHERE S2.seat = S1.seat + (@head_cnt -1)
	AND S3.seat BETWEEN S1.seat AND S2.seat
GROUP BY S1.seat, S2.seat
HAVING COUNT(*) = SUM(
	CASE
		WHEN S3.`status` = "空" THEN 1
        ELSE 0
	END
)
;


SELECT S1.seat AS start_seat, "〜", S2.seat AS end_seat
FROM Seats2 AS S1, Seats2 AS S2, Seats2 AS S3
WHERE S2.seat = S1.seat + (@head_cnt -1)
	AND S3.seat BETWEEN S1.seat AND S2.seat
GROUP BY S1.seat, S2.seat
HAVING COUNT(*) = SUM(
	CASE
		WHEN S3.`status` = "空"
			AND S3.line_id = S1.line_id THEN 1
        ELSE 0
	END
)
;

