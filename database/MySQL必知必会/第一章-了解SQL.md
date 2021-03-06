# 第一章-了解SQL

## 1.1 数据库基础

### 1.1.1 什么是数据库

> *数据库(database)* :
>
> ​	保存有组织的数据的容器（通常是一个文件或一组文件）。 

### 1.1.2 表

> *表(table)*:
>
> ​	某种特定类型数据的结构化清单。

表是一种结构话的文件，可用来存储某种特定类型的数据。

关键点在于，存储在表中的数据是一种类型的数据或一个清单，不能将两种不同类型的清单或数据存储在同一个表中，这样会使得以后的检索和访问变得困难。

**每个表都有一个名字，用来表示自己，这个名字是唯一的**

即**同一个数据不应出现相同的表名，但不同数据库可以使用相同的表名。**

表具有一些特性，这些特性定义了数据在表中如何存储，如存储什么数据，数据如何分解，各部分信息如何命名等等，而**模式**就是用来描述这些特性的信息的，描述数据库中特定的表以及整个数据库（和其中表的关系）

> *模式(schema):*
>
> ​	关于数据库和表的布局及特性的信息。

### 1.1.3 列和数据类型

表由列组成，而列存储着表中某部分的信息。

> *列(column):*
>
> ​	表中的一个字段。所以表都是由一个或多个列组成的。

数据库中每个列都有相应的数据类型。数据类型定义列可以存储的数据种类。

> *数据类型(datatype):*
>
> ​	所容许的数据的类型。每个表列都有相应的数据类型，它限制（或容许）该列中存储的数据。

### 1.1.4 列

表中数据是按行存储的，所保存的每个记录存储在自己的行内。

> 行(row):
>
> ​	表中的一个记录。

### 1.1.5 主键

表中每一行都应该有一个可以唯一标识自己的一列（或一组列）。如订单表中的订单ID。

> *主键( primary key ):*
>
> ​	一列（或一组列），其值能够唯一区分表中每一行。

没有主键，更新或删除表中特定行很困难，因为没有安全的方法保证涉及相关的行。

**应该总是定义主键**

表中任意的列都可以成为主键

主键应满足一下条件：

- 任意两行都不具有相同的主键值
- 每一行都必须具有一个主键值（主键列不允许出现NULL值）

主键通常定义在表的一列上，但是不是必需的，也可以一起使用多个列作为主键。这时单个列的值可以不唯一，但是其组合必须唯一。

主键的最好习惯：

- 不更新主键列中的值
- 不重用主键列的值
- 不在主键列中使用可能会更改的值

---

## 什么是SQL

> SQL是结构化查询语言（ Structured Query Language )的缩写。
>
> SQL 是一种专门用来与数据库通信的语言。

其优点：

- SQL 不是某个特定数据库供应商专有的语言。
- SQL易学简单
- SQL是一门强有力的语言，灵活使用其语言元素，可以进行非常复杂和高级的数据库操作。

