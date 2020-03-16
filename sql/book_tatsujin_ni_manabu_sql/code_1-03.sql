USE tatsujin;

DROP TABLE IF EXISTS products;

CREATE TABLE Products (
    `name` VARCHAR(16) NOT NULL,
    price INTEGER NOT NULL
);
 
INSERT INTO products VALUES
	('りんご',	50),
	('みかん',	100),
	('みかん',	100),
	('みかん',	100),
	('バナナ',	80)
;

-- 3-1
SELECT DISTINCT
    p1.name AS name_1, p2.name AS name_2
FROM
    products AS p1
        JOIN
    products AS p2 ON p1.name <= p2.name
ORDER BY name_1;

-- 3-2
-- SELECT DISTINCT
--     name, price
-- FROM
--     products;
DROP TABLE IF EXISTS products_no_redundant;
CREATE TABLE products_no_redundant AS SELECT ROW_NUMBER() OVER (PARTITION BY `name`, price ORDER BY `name`) AS row_num, `name`, price FROM products;

DELETE FROM products_no_redundant 
WHERE
    row_num > 1;

SELECT 
    *
FROM
    products_no_redundant;
