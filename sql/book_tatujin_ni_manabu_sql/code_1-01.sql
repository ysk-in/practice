DROP DATABASE IF EXISTS tatujin;
CREATE DATABASE tatujin;
USE tatujin;

-- 日本語使うため utf8mb4 に設定しておきたい 予期しない動作防止するため
-- SHOW VARIABLES like 'char%';

CREATE TABLE pop (
    pref_name VARCHAR(32) PRIMARY KEY,
    population INTEGER NOT NULL
);

INSERT INTO pop(pref_name, population) VALUES('徳島', 100), ('香川', 200) , ('愛媛', 150) , ('高知', 200) , ('福岡', 300) , ('佐賀', 100) , ('長崎', 200) , ('東京', 400) , ('群馬', 50);

CREATE TABLE pop2 (
    pref_name VARCHAR(32),
    sex CHAR(1) NOT NULL,
    population INTEGER NOT NULL,
    PRIMARY KEY (pref_name , sex)
);

INSERT INTO pop2(pref_name, sex, population) VALUES('徳島', '1',	60 ), ('徳島', '2', 40 ), ('香川', '1', 100), ('香川', '2', 100), ('愛媛', '1', 100), ('愛媛', '2', 50 ), ('高知', '1', 100), ('高知', '2', 100), ('福岡', '1', 100), ('福岡', '2', 200), ('佐賀', '1', 20 ), ('佐賀', '2', 80 ), ('長崎', '1', 125), ('長崎', '2', 125), ('東京', '1', 250), ('東京', '2', 150);


SELECT 
    pref_name,
    SUM(CASE
        WHEN sex = '1' THEN population
        ELSE 0
    END) AS cnt_m,
    SUM(CASE
        WHEN sex = '2' THEN population
        ELSE 0
    END) AS cnt_f
FROM
    pop2
GROUP BY pref_name;

-- exercise 1-1
CREATE TABLE greatests (
    `key` char(1) primary key not null,
    x int,
    y int,
    z int
);
INSERT INTO greatests VALUES("A", 1, 2, 3), ("B", 5, 5, 2), ("C", 4, 7, 1), ("D", 3, 3, 8);

SELECT 
    `key`,
    CASE
        WHEN x >= y THEN x
        ELSE y
    END AS greatest
FROM
    greatests;

SELECT 
    `key`,
    CASE
        WHEN x >= y && x >= z THEN x
        WHEN y >= x && y >= z THEN y
        ELSE z
    END AS greatest
FROM
    greatests;

-- exercise 1-2
SELECT 
    CASE
        WHEN sex = 1 THEN '男'
        WHEN sex = 2 THEN '女'
        ELSE NULL
    END AS '性別',
    SUM(population) AS '全国',
    SUM(CASE
        WHEN pref_name = '徳島' THEN population
    END) AS '徳島',
        SUM(CASE
        WHEN pref_name = '香川' THEN population
    END) AS '香川',
    -- 省略
    SUM(CASE
        WHEN pref_name IN ('徳島' , '香川', '高知', '愛媛') THEN population
    END) AS '四国(再掲)'
FROM
    pop2
GROUP BY sex;

-- exercise 1-3
SELECT 
    `key`
FROM
    greatests
ORDER BY CASE `key`
    WHEN 'B' THEN 1
    WHEN 'A' THEN 2
    WHEN 'D' THEN 3
    WHEN 'C' THEN 4
    ELSE NULL
END
;
