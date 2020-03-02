USE book_shop;

DROP TABLE inventory;
CREATE TABLE inventory (
    item_name VARCHAR(100),
    price DECIMAL(8 , 2 ),
    quantity INT
);

SELECT CURTIME();

SELECT CURDATE();

SELECT DATE_FORMAT(NOW(), '%w');

SELECT DATE_FORMAT(NOW(), '%W');

SELECT DATE_FORMAT(NOW(), '%m/%d/%Y');

SELECT DATE_FORMAT(NOW(), '%M %D at %H:%i');

DROP TABLE tweets;
CREATE TABLE tweets (
    tweet VARCHAR(140),
    username VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
