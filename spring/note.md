# SpringBoot 復習

## MySQL TCP ポート確認

```
mysql> SHOW VARIABLES LIKE 'port';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| port          | 3306  |
+---------------+-------+
1 row in set (0.04 sec)
```

## MySQL ユーザ作成

```
DROP DATABASE IF EXISTS tracker_dev;
DROP DATABASE IF EXISTS tracker_test;

CREATE DATABASE tracker_dev;
CREATE DATABASE tracker_test;

CREATE USER IF NOT EXISTS 'tracker'@'%'
  IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON tracker_dev.* TO 'tracker' @'%';
GRANT ALL PRIVILEGES ON tracker_test.* TO 'tracker' @'%';
```

ROLE は未だよく理解できていない v8 で追加されたっぽい

```
CREATE USER [IF NOT EXISTS]
    user [auth_option] [, user [auth_option]] ...
    DEFAULT ROLE role [, role ] ...
    [REQUIRE {NONE | tls_option [[AND] tls_option] ...}]
    [WITH resource_option [resource_option] ...]
    [password_option | lock_option] ...
```

## MySQL Database 作成

```
CREATE TABLE time_entries (
  id         BIGINT NOT NULL AUTO_INCREMENT,
  project_id BIGINT,
  user_id    BIGINT,
  date       DATE,
  hours      INT,

  PRIMARY KEY (id)
)
  ENGINE = innodb
  DEFAULT CHARSET = UTF8MB4;
```
