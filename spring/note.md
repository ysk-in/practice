# SpringBoot 復習

**TODO つづき ここから**

https://spring.pleiades.io/spring-boot/docs/current/reference/html/using-spring-boot.html#using-boot-whats-next

- https://courses.education.pivotal.io/c/349803561/
- https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#using-boot-starter
- https://spring.pleiades.io/spring-boot/docs/current/reference/html/using-spring-boot.html#using-boot-starter

## Structuring

ファイル(ソースコード)の典型的なレイアウトについて  
https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#using-boot-structuring-your-code

## i18n 対応 messages ファイル

未だ読めていない 参考になりそう

https://github.com/tokuhirom/java-handbook/blob/master/spring/i18n.md

## Spring Boot のスターター

spring-boot-starter-\*
PAL で使用した JDBC のスターターは spring-boot-starter-jdbc  
jooq のスターター spring-boot-starter-jooq が気になる

https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#using-boot-starter

和訳版  
https://spring.pleiades.io/spring-boot/docs/current/reference/html/using-spring-boot.html#using-boot-starter

理解しておきたい TODO

- spring-boot-starter-test
- spring-boot-starter-security

# (参考) MySQL

以降 Spring Boot とは直接無関係  
MySQL について

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
