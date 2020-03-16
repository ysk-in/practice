DROP DATABASE IF EXISTS tatsujin_ensyu6;
CREATE DATABASE tatsujin_ensyu6;
USE tatsujin_ensyu6;

-- SeqTbl
DROP TABLE IF EXISTS SeqTbl;

CREATE TABLE SeqTbl (
    seq INTEGER PRIMARY KEY,
    name VARCHAR(16) NOT NULL
);

INSERT INTO SeqTbl VALUES
    (1,	'ディック'),
    (2,	'アン'),
    (3,	'ライル'),
    (5,	'カー'),
    (6,	'マリー'),
    (8,	'ベン')
;

SELECT 
    CASE
        WHEN COUNT(*) = 0 OR MIN(seq) > 1 THEN 1
        ELSE (SELECT 
                MIN(seq + 1)
            FROM
                SeqTbl s1
            WHERE
                NOT EXISTS( SELECT 
                        *
                    FROM
                        SeqTbl s2
                    WHERE
                        s2.seq = s1.seq + 1))
    END AS a
FROM
    SeqTbl;

-- TestResults
DROP TABLE IF EXISTS TestResults;

CREATE TABLE TestResults (
    student_id CHAR(12) NOT NULL PRIMARY KEY,
    class CHAR(1) NOT NULL,
    sex CHAR(1) NOT NULL,
    score INTEGER NOT NULL
);

INSERT INTO TestResults VALUES
	('001', 'A', '男', 100),
	('002', 'A', '女', 100),
	('003', 'A', '女',  49),
	('004', 'A', '男',  30),
	('005', 'B', '女', 100),
	('006', 'B', '男',  92),
	('007', 'B', '男',  80),
	('008', 'B', '男',  80),
	('009', 'B', '女',  10),
	('010', 'C', '男',  92),
	('011', 'C', '男',  80),
	('012', 'C', '女',  21),
	('013', 'D', '女', 100),
	('014', 'D', '女',   0),
	('015', 'D', '女',   0)
;

-- TestResults Q.1
SELECT 
    class
FROM
    TestResults
GROUP BY class
HAVING COUNT(*) * 0.75 <= SUM(CASE
    WHEN score >= 80 THEN 1
    ELSE 0
END);

-- TestResults Q.2
SELECT
    class
FROM
    TestResults
GROUP BY class
HAVING SUM(CASE
    WHEN sex = '男' AND score >= 50 THEN 1
    ELSE 0
END) > SUM(CASE
    WHEN sex = '女' AND score >= 50 THEN 1
    ELSE 0
END);

-- TestResults Q.3
SELECT 
    class
FROM
    TestResults
GROUP BY class
HAVING AVG(CASE
    WHEN sex = '女' THEN score
END) > AVG(CASE
    WHEN sex = '男' THEN score
END);

-- ENSYU 6-1
INSERT INTO SeqTbl VALUES
    (4,	'AAA'),
    (7,	'BBB') 
;

SELECT 
    CASE
        WHEN COUNT(*) = 0 OR MIN(seq) > 1 THEN '歯抜けあり'
        WHEN COUNT(*) = MAX(seq) - MIN(seq) + 1 THEN '歯抜けなし'
        WHEN (SELECT COUNT(seq)
            FROM
                SeqTbl s1
            WHERE
                NOT EXISTS( SELECT 
                        *
                    FROM
                        SeqTbl s2
                    WHERE
                        s2.seq = s1.seq + 1)
        ) > 0 THEN '歯抜けあり'
        ELSE '歯抜けなし'
    END AS a
FROM
    SeqTbl
;

SELECT 
    *
FROM
    SeqTbl;

DELETE FROM SeqTbl 
WHERE
    seq = 4;


-- ENSYU 6-2 PREPARE
DROP TABLE IF EXISTS Students;

CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    dpt VARCHAR(16) NOT NULL,
    sbmt_date DATE
);

INSERT INTO Students VALUES
    (100,  '理学部',   '2018-10-10'),
    (101,  '理学部',   '2018-09-22'),
    (102,  '文学部',   NULL),
    (103,  '文学部',   '2018-09-10'),
    (200,  '文学部',   '2018-09-22'),
    (201,  '工学部',   NULL),
    (202,  '経済学部', '2018-09-25')
;

-- ENSYU 6-2
SELECT 
    dpt
FROM
    students
GROUP BY dpt
HAVING COUNT(*) = SUM(CASE
    WHEN sbmt_date BETWEEN '2018-09-01' AND '2018-09-30' THEN 1
    ELSE 0
END);
--     WHEN DATE_FORMAT(sbmt_date, '%Y%m') <= 201809 THEN 1

-- ENSYU 6-3 PREPARE
DROP TABLE IF EXISTS Items;

CREATE TABLE Items (
    item VARCHAR(16) PRIMARY KEY
);

INSERT INTO Items VALUES
    ('ビール'),
    ('紙オムツ'),
    ('自転車')
;

DROP TABLE IF EXISTS ShopItems;
 
CREATE TABLE ShopItems (
    shop VARCHAR(16),
    item VARCHAR(16),
    PRIMARY KEY (shop , item)
);

INSERT INTO ShopItems VALUES
    ('仙台',  'ビール'),
    ('仙台',  '紙オムツ'),
    ('仙台',  '自転車'),
    ('仙台',  'カーテン'),
    ('東京',  'ビール'),
    ('東京',  '紙オムツ'),
    ('東京',  '自転車'),
    ('大阪',  'テレビ'),
    ('大阪',  '紙オムツ'),
    ('大阪',  '自転車')
;

-- ENSYU 6-3
SELECT 
    shop,
    COUNT(si.item) AS my_item_cnt,
    (SELECT 
            COUNT(item)
        FROM
            items) - COUNT(si.item) AS diff_cnt
FROM
    shopitems AS si
        INNER JOIN
    items AS i ON si.item = i.item
GROUP BY si.shop;
