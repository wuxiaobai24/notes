# MySQL简介

## 2.1什么是MySQL

数据的所以存储、检索、管理和处理实际上是由数据库软件——**DBMS(数据库管理系统)**完成的。

而MySQL是一种DBMS，即它是一种数据库软件。

使用 MySQL 的原因：

- 成本——MySQL是开源的，一般可以免费使用
- 性能——MySQL执行很快
- 可信赖——某些非常重要和声望很高的公司、站点使用MySQL
- 简单——MySQL很容易安装和使用

### 2.1.1 客户机-服务器软件

- DBMS：

  - 基于共享文件系统的DBMS：

    如Microsoft Access和 FileMaker

  - 基于客户机-服务器的DBMS：

    如MySQL、Oracle以及Microsoft SQL Serverd等

    - 服务器部分：

      负责所有数据访问和处理的一个软件，这个软件运行在称为**数据库服务器**的计算机上。

      与数据文件打交道的只有服务器软件。

      关于数据添加、删除和更新的所有请求都由服务器软件完成。而这些请求来自运行客户机软件的计算机。

    - 客户机部分：

      客户机是与用户打交道的软件。

      客户机软件通过网络提交该请求给服务器软件。

    **客户机和服务器软件可能安装在两台或一台计算机上**

所有的活动对用户来说都是透明的。数据存储在别的地方，或者数据库服务器为你完成这个处理这个事实是隐藏的。

对于MySQL：

- 服务器软件为MySQL DBMS。
- 客户机可以是MySQL提供的工具、脚本语言(如Perl)、Web应用开发语言(如ASP、ColdFusion、JSP、PHP) 、程序设计语言(如C、C++、Java)等

### 2.1.2 MySQL版本

MySQL当前版本为版本5，最近版本中主要更改为：

- 4—— InnoDB引擎，增加事务处理，并、改进全文本搜索等的支持。
- 4.1——对函数库、子查询、集成帮助等的重要增加
- 5——存储过程、触发器、游标、视图等

---

## 2.2 MySQL工具

为了使用MySQL，需要有一个客户机，即需要一个用来给MySQL提供要执行的命令的一个应用

### 2.2.1 mysql命令行实用程序

每一个MySQL安装都有一个名为mysql 的简单命令行实用程序。

打开方式为：

```shell
➜  ~ mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 5.7.18-0ubuntu0.16.10.1 (Ubuntu)

Copyright (c) 2000, 2017, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 

```

- 命令用`;`或`\g`结束，即仅按Enter不执行命令
- `help` 和 `\h` 获取帮助
- `quit`和`exit`退出命令实用程序

### 2.2.2 MySQL Administrator 

> MySQL Administrator (MySQL管理器) 是一个图形交互客户机，用来简化MySQL服务器的管理。

2.2.3 MySQL Query Brower

> MySQL Query Brower 为一个图形交互客户机，用来编写和执行MySQL命令行。

---

### 2.3 MySQL的安装

Ubuntu16.10:

安装：

```shell
➜  ~ sudo apt-get install mysql-server
➜  ~ sudo apt-get install mysql-client
➜  ~ sudo apt-get install libmysqlclient-dev
```

测试：

```shell
➜  ~ sudo netstat -tap | grep mysql
tcp        0      0 localhost:mysql         0.0.0.0:*               LISTEN      1043/mysqld 
```

Manjaro or Arch:

```shell
$ sudo pacman -S mariadb mariadb-clients
$ sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
$ sudo systemctl start mysqld.service
$ sudo mysqladmin -u root -h wuxiaobai24-pc password 'wuxiaobai24' 
```

