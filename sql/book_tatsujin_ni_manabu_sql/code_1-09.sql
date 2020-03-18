DROP DATABASE IF EXISTS tatsujin_ensyu9;
CREATE DATABASE tatsujin_ensyu9;
USE tatsujin_ensyu9;

/* 3. 差集合で関係除算を表現する */
DROP TABLE IF EXISTS Skills;

CREATE TABLE Skills (
    skill VARCHAR(32),
    PRIMARY KEY (skill)
);

DROP TABLE IF EXISTS EmpSkills;

CREATE TABLE EmpSkills (
    emp VARCHAR(32),
    skill VARCHAR(32),
    PRIMARY KEY (emp , skill)
);

INSERT INTO Skills VALUES
    ('Oracle'),
    ('UNIX'),
    ('Java')
;

INSERT INTO EmpSkills VALUES
    ('相田', 'Oracle'),
    ('相田', 'UNIX'),
    ('相田', 'Java'),
    ('相田', 'C#'),
    ('神崎', 'Oracle'),
    ('神崎', 'UNIX'),
    ('神崎', 'Java'),
    ('平井', 'UNIX'),
    ('平井', 'Oracle'),
    ('平井', 'PHP'),
    ('平井', 'Perl'),
    ('平井', 'C++'),
    ('若田部', 'Perl'),
    ('渡来', 'Oracle')
;

-- MySQL は EXCEPT 未サポート
-- SELECT DISTINCT emp
-- FROM EmpSkills ES1
-- WHERE NOT EXISTS (
-- 	SELECT skill FROM Skills
--  	EXCEPT SELECT skill FROM EmpSkills ES2
-- 	WHERE ES1.emp = ES2.emp
-- );

-- ENSYU 9-1 PREPARE
/* テーブル同士のコンペア　集合の相等性チェック */
DROP TABLE IF EXISTS Tbl_A;

CREATE TABLE Tbl_A (
    keycol CHAR(1) PRIMARY KEY,
    col_1 INTEGER,
    col_2 INTEGER,
    col_3 INTEGER
);

DROP TABLE IF EXISTS Tbl_B;

CREATE TABLE Tbl_B (
    keycol CHAR(1) PRIMARY KEY,
    col_1 INTEGER,
    col_2 INTEGER,
    col_3 INTEGER
);

INSERT INTO Tbl_A VALUES
    ('A', 2, 3, 4),
    ('B', 0, 7, 9),
    ('C', 5, 1, 6)
;

INSERT INTO Tbl_B VALUES
    ('A', 2, 3, 4),
    ('B', 0, 7, 9),
    ('C', 5, 1, 6)
;

SELECT COUNT(*) AS row_cnt
FROM (
	SELECT * FROM Tbl_A
    UNION SELECT * FROM Tbl_B
) as TMP;

-- ENSYU 9-1
SELECT COUNT(*) AS row_cnt
FROM (
	SELECT * FROM Tbl_A
    UNION ALL SELECT * FROM Tbl_B
) as TMP;

