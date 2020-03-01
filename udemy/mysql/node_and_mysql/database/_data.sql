DROP DATABASE IF EXISTS join_us;
CREATE DATABASE join_us;
USE join_us;

-- DROP USER 'dbuser'@'localhost';
-- CREATE USER 'dbuser'@'localhost' IDENTIFIED WITH mysql_native_password BY 'dbuser' PASSWORD EXPIRE NEVER;
-- SELECT host, user, plugin FROM mysql.user;

-- GRANT ALL ON join_us.* TO 'dbuser'@'localhost';
-- SHOW GRANTS FOR dbuser@localhost;

CREATE TABLE users (
    email VARCHAR(255) PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
