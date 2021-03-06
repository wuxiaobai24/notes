# 使用MySQL

## 3.0 建立一个数据库:

```shell
$ mysqladmin -u root -p create mydatabase 
```



## 3.1 连接

MySQL与所以客户机-服务器DBMS一样，要求在能执行命令前登录到DBMS。

MySQL在内部保存自己的用户列表。并且吧每个用户与各种权限关联起来。

连接到MySQL需要一下信息：

- 主机名
- 端口（默认个端口是3306）
- 一个合法的用户名
- 用户口令

用mysql命令行实用程序连接本地的服务器：

```shell
➜  ~ mysql -u root -p 
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 16
Server version: 5.7.18-0ubuntu0.16.10.1 (Ubuntu)

Copyright (c) 2000, 2017, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
```

---

## 3.2 选择数据库

在对某个数据库进行操作前，需要先选择这个数据库。

选择数据库使用`USE`关键词。

**必须先实用`USE`打开数据库，才能读取其中的数据。**

```mysql
mysql> USE tests
Database changed
mysql> 

```

---

## 3.3 了解数据库和表

### 3.3.1 显示数据库名：

使用`SHOW DATABASES`显示数据库名。

其返回的是可用数据库的一个列表。这个列表可能包含MySQL内部使用的数据库（如mysql等)

```mysql
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| tests              |
+--------------------+
5 rows in set (0.00 sec)

```

### 3.3.2 获取数据库中表的列表

使用`SHOW TABLES`，需先选择数据库，即使用`USE`

```mysql
mysql> SHOW TABLES;
+-----------------+
| Tables_in_tests |
+-----------------+
| areas           |
| cities          |
| provinces       |
| zipcode         |
+-----------------+
4 rows in set (0.00 sec)
```

### 3.3.3 显示表列

使用`SHOW COLUMNS`来显示表列，其要求给出一个表名。

它为每个字段返回一行，行中包含字段名( Field )、数据类型( Type ) 、是否允许你NULL ( Null )、键信息( Key )、默认值( Default )以及其他信息( Extra )。

可以使用`DESCRIBE` 代替，如

```mysql
mysql> describe db;
```



```mysql
mysql> SHOW COLUMNS FROM areas;
+--------+-------------+------+-----+---------+----------------+
| Field  | Type        | Null | Key | Default | Extra          |
+--------+-------------+------+-----+---------+----------------+
| id     | int(11)     | NO   | PRI | NULL    | auto_increment |
| areaid | varchar(20) | NO   |     | NULL    |                |
| area   | varchar(50) | NO   |     | NULL    |                |
| cityid | varchar(20) | NO   |     | NULL    |                |
+--------+-------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)


```

### 3.3.4 自动增量

> *自动增量( auto_increment )*
>
> 某些表列需要唯一值，如雇员ID，在每个行添加到表中时，MySQL可以自动地为每个行分配下一个可用的编号，不需要在添加一行的时候手动的分配唯一的值。

### 3.3.5 `SHOW`的其他用法：

- `SHOW STATUS` 用于显示广泛的服务器状态信息
- ` SHOW CREATE DATABASE`和`SHOW CREATE TABLE` 分别用来显示创建特定数据库或表
- `SHOW GRANTS` 显示授权用户的安全权限
- `SHOW ERRORS `和`SHOW WARNINGS` 显示服务器错误或警告



