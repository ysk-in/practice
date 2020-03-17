DROP DATABASE IF EXISTS tatsujin_ensyu8;
CREATE DATABASE tatsujin_ensyu8;
USE tatsujin_ensyu8;

DROP TABLE IF EXISTS Courses;

CREATE TABLE Courses (
    name VARCHAR(32),
    course VARCHAR(32),
    PRIMARY KEY (name , course)
);

INSERT INTO Courses VALUES
    ('赤井', 'SQL入門'),
    ('赤井', 'UNIX基礎'),
    ('鈴木', 'SQL入門'),
    ('工藤', 'SQL入門'),
    ('工藤', 'Java中級'),
    ('吉田', 'UNIX基礎'),
    ('渡辺', 'SQL入門')
;

-- クロス表を求める水平展開：その1　外部結合の利用
SELECT C0.name,
       CASE WHEN C1.name IS NOT NULL THEN '○' ELSE NULL END AS "SQL入門",
       CASE WHEN C2.name IS NOT NULL THEN '○' ELSE NULL END AS "UNIX基礎",
       CASE WHEN C3.name IS NOT NULL THEN '○' ELSE NULL END AS "Java中級"
  FROM (SELECT DISTINCT name FROM Courses) C0
         LEFT OUTER JOIN
          (SELECT name FROM Courses WHERE course = 'SQL入門') C1
           ON C0.name = C1.name
             LEFT OUTER JOIN
              (SELECT name FROM Courses WHERE course = 'UNIX基礎') C2
                ON C0.name = C2.name
                  LEFT OUTER JOIN
                   (SELECT name FROM Courses WHERE course = 'Java中級') C3
                     ON C0.name = C3.name;

-- 水平展開：その2　スカラサブクエリの利用
SELECT C0.name,
       (SELECT '○'
          FROM Courses C1
         WHERE course = 'SQL入門'
           AND C1.name = C0.name) AS "SQL入門",
       (SELECT '○'
          FROM Courses C2
         WHERE course = 'UNIX基礎'
           AND C2.name = C0.name) AS "UNIX基礎",
       (SELECT '○'
          FROM Courses C3
         WHERE course = 'Java中級'
           AND C3.name = C0.name) AS "Java中級"
  FROM (SELECT DISTINCT name FROM Courses) C0;

-- 水平展開：その3　CASE式を入れ子にする
SELECT name,
       CASE WHEN SUM(CASE WHEN course = 'SQL入門' THEN 1 ELSE NULL END) = 1
            THEN '○' ELSE NULL END AS "SQL入門",
       CASE WHEN SUM(CASE WHEN course = 'UNIX基礎' THEN 1 ELSE NULL END) = 1
            THEN '○' ELSE NULL END AS "UNIX基礎",
       CASE WHEN SUM(CASE WHEN course = 'Java中級' THEN 1 ELSE NULL END) = 1
            THEN '○' ELSE NULL END AS "Java中級"
  FROM Courses
 GROUP BY name;
 
 
 -- -----------------------------------------------------------------------------
 DROP TABLE IF EXISTS Personnel;
 
 /* 外部結合で行列変換　その2（列→行）：繰り返し項目を1 列にまとめる */
CREATE TABLE Personnel (
    employee VARCHAR(32),
    child_1 VARCHAR(32),
    child_2 VARCHAR(32),
    child_3 VARCHAR(32),
    PRIMARY KEY (employee)
);

INSERT INTO Personnel VALUES
    ('赤井', '一郎', '二郎', '三郎'),
    ('工藤', '春子', '夏子', NULL),
    ('鈴木', '夏子', NULL,   NULL),
    ('吉田', NULL,   NULL,   NULL)
;

select * from personnel;

-- 列から行への変換：UNION ALLの利用
SELECT employee, child_1 AS child FROM Personnel
UNION ALL
SELECT employee, child_2 AS child FROM Personnel
UNION ALL
SELECT employee, child_3 AS child FROM Personnel
ORDER BY employee DESC;

DROP VIEW IF EXISTS children;

CREATE VIEW Children(child)
AS SELECT child_1 FROM Personnel
UNION
SELECT child_2 FROM Personnel
UNION
SELECT child_3 FROM Personnel;

SELECT * FROM children;

-- SELECT * FROM Personnel;
-- update personnel set child_2 = "夏子" where employee = "吉田";

-- 社員の子どもリストを得るSQL（子どものいない社員も出力する）
SELECT EMP.employee, Children.child
  FROM Personnel EMP
         LEFT OUTER JOIN Children
           ON Children.child IN (EMP.child_1, EMP.child_2, EMP.child_3);

-- -----------------------------------------------------------------------------
DROP TABLE IF EXISTS TblSex;

/* クロス表で入れ子の表側を作る */
CREATE TABLE TblSex (
    sex_cd CHAR(1),
    sex VARCHAR(5),
    PRIMARY KEY (sex_cd)
);

DROP TABLE IF EXISTS TblAge;

CREATE TABLE TblAge (
    age_class CHAR(1),
    age_range VARCHAR(30),
    PRIMARY KEY (age_class)
);

DROP TABLE IF EXISTS TblPop;

CREATE TABLE TblPop (
    pref_name VARCHAR(30),
    age_class CHAR(1),
    sex_cd CHAR(1),
    population INTEGER,
    PRIMARY KEY (pref_name , age_class , sex_cd)
);

INSERT INTO TblSex (sex_cd, sex ) VALUES
	('m',	'男'),
	('f',	'女')
;

INSERT INTO TblAge (age_class, age_range ) VALUES
    ('1',	'21～30歳'),
    ('2',	'31～40歳'),
    ('3',	'41～50歳')
;

INSERT INTO TblPop VALUES
    ('秋田', '1', 'm', 400 ),
    ('秋田', '3', 'm', 1000 ),
    ('秋田', '1', 'f', 800 ),
    ('秋田', '3', 'f', 1000 ),
    ('青森', '1', 'm', 700 ),
    ('青森', '1', 'f', 500 ),
    ('青森', '3', 'f', 800 ),
    ('東京', '1', 'm', 900 ),
    ('東京', '1', 'f', 1500 ),
    ('東京', '3', 'f', 1200 ),
    ('千葉', '1', 'm', 900 ),
    ('千葉', '1', 'f', 1000 ),
    ('千葉', '3', 'f', 900 )
;

-- 外部結合で入れ子の表側を作る：間違ったSQL
SELECT MASTER1.age_class AS age_class,
       MASTER2.sex_cd AS sex_cd,
       DATA.pop_tohoku AS pop_tohoku,
       DATA.pop_kanto AS pop_kanto
  FROM (SELECT age_class, sex_cd,
               SUM(CASE WHEN pref_name IN ('青森', '秋田')
                        THEN population ELSE NULL END) AS pop_tohoku,
               SUM(CASE WHEN pref_name IN ('東京', '千葉')
                        THEN population ELSE NULL END) AS pop_kanto
          FROM TblPop
         GROUP BY age_class, sex_cd) DATA
           RIGHT OUTER JOIN TblAge MASTER1
              ON MASTER1.age_class = DATA.age_class
           RIGHT OUTER JOIN TblSex MASTER2
              ON MASTER2.sex_cd = DATA.sex_cd;

-- 外部結合で入れ子の表側を作る：正しいSQL
SELECT MASTER.age_class AS age_class,
       MASTER.sex_cd AS sex_cd,
       DATA.pop_tohoku AS pop_tohoku,
       DATA.pop_kanto AS pop_kanto
  FROM (SELECT age_class, sex_cd
          FROM TblAge CROSS JOIN TblSex ) MASTER
            LEFT OUTER JOIN
             (SELECT age_class, sex_cd,
                     SUM(CASE WHEN pref_name IN ('青森', '秋田')
                              THEN population ELSE NULL END) AS pop_tohoku,
                     SUM(CASE WHEN pref_name IN ('東京', '千葉')
                              THEN population ELSE NULL END) AS pop_kanto
                FROM TblPop
               GROUP BY age_class, sex_cd) DATA
    ON MASTER.age_class = DATA.age_class
   AND MASTER.sex_cd = DATA.sex_cd;
   