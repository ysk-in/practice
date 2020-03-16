DROP DATABASE IF EXISTS tatsujin_ensyu5;
CREATE DATABASE tatsujin_ensyu5;
USE tatsujin_ensyu5;

DROP TABLE IF EXISTS arrays2;

-- ENSYU 5-1 PREPARE
CREATE TABLE arrays2 (
    `key` CHAR(1) NOT NULL,
    i INTEGER NOT NULL,
    val INTEGER,
    PRIMARY KEY (`key` , i)
);

INSERT INTO arrays2 VALUES 
('A', 1, NULL),
('A', 2, NULL),
('A', 3, NULL),
('A', 4, NULL),
('A', 5, NULL),
('A', 6, NULL),
('A', 7, NULL),
('A', 8, NULL),
('A', 9, NULL),
('A',10, NULL),
('B', 1, 3),
('B', 2, NULL),
('B', 3, NULL),
('B', 4, NULL),
('B', 5, NULL),
('B', 6, NULL),
('B', 7, NULL),
('B', 8, NULL),
('B', 9, NULL),
('B',10, NULL),
('C', 1, 1),
('C', 2, 1),
('C', 3, 1),
('C', 4, 1),
('C', 5, 1),
('C', 6, 1),
('C', 7, 1),
('C', 8, 1),
('C', 9, 1),
('C',10, 1)
;

-- ENSYU 5-1
-- SELECT DISTINCT
--     `key`
-- FROM
--     arrays2 AS e1
-- WHERE
--     NOT EXISTS( SELECT 
--             COALESCE(val, - 1) AS valnonnull
--         FROM
--             arrays2 AS e2
--         WHERE
--             e1.`key` = e2.`key` AND e1.i = e2.i
--         HAVING valnonnull <> 1)
-- ;
SELECT DISTINCT
    `key`
FROM
    arrays2 AS e1
WHERE
    NOT EXISTS( SELECT 
            val
        FROM
            arrays2 AS e2
        WHERE
            e1.`key` = e2.`key` AND e1.i = e2.i
                AND (val IS NULL OR val <> 1));

-- ENSYU 5-2 PREPARE
DROP TABLE IF EXISTS projects;

CREATE TABLE projects (
    id VARCHAR(32),
    num INTEGER,
    status VARCHAR(32),
    PRIMARY KEY (id , num)
);

INSERT INTO projects VALUES
('AA100', 0, '完了'),
('AA100', 1, '待機'),
('AA100', 2, '待機'),
('B200',  0, '待機'),
('B200',  1, '待機'),
('CS300', 0, '完了'),
('CS300', 1, '完了'),
('CS300', 2, '待機'),
('CS300', 3, '待機'),
('DY400', 0, '完了'),
('DY400', 1, '完了'),
('DY400', 2, '完了');

SELECT 
    *
FROM
    projects p1
WHERE
    NOT EXISTS( SELECT 
            status
        FROM
            projects p2
        WHERE
            p1.id = p2.id
                AND status <> CASE
                WHEN num <= 1 THEN '完了'
                ELSE '待機'
            END);

SELECT 
    *
FROM
    projects p1
WHERE
    NOT EXISTS( SELECT 
            status
        FROM
            projects p2
        WHERE
            p1.id = p2.id
                AND status <> CASE
                WHEN num <= 1 THEN '完了'
                ELSE '待機'
            END);

-- ENSYU 5-2
-- SELECT 
--     *
-- FROM
--     projects p1
-- WHERE
--     '待機' = ALL (SELECT 
--             status
--         FROM
--             projects p2
--         WHERE
--             p1.id = p2.id AND num >= 2)
--         AND '完了' = ALL (SELECT 
--             status
--         FROM
--             projects p2
--         WHERE
--             p1.id = p2.id AND num <= 1);
SELECT 
    *
FROM
    projects p1
WHERE
    'o' = ALL (SELECT 
            CASE
                    WHEN num <= 1 AND p2.status = '完了' THEN 'o'
                    WHEN num > 1 AND p2.status = '待機' THEN 'o'
                    ELSE 'x'
                END
        FROM
            projects p2
        WHERE
            p1.id = p2.id);

-- ENSYU 5-3 PREPARE
DROP TABLE IF EXISTS digits;
CREATE TABLE digits (
    digit INTEGER PRIMARY KEY
);
INSERT INTO digits VALUES
(0),
(1),
(2),
(3),
(4),
(5),
(6),
(7),
(8),
(9);

DROP TABLE IF EXISTS numbers;
CREATE TABLE numbers (
    num INTEGER PRIMARY KEY
);
insert into numbers ()
SELECT d1.digit + (d2.digit * 10)
  FROM digits d1
         JOIN digits d2;

-- ENSYU 5-3
SELECT 
    n1.num
FROM
    numbers AS n1
WHERE
    n1.num > 1
        AND NOT EXISTS( SELECT 
            *
        FROM
            numbers AS n2
        WHERE
            n2.num <> 1 AND n2.num <> n1.num
                AND ((n1.num % n2.num) = 0));
