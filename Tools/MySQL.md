## MySQL
- 关系型数据库
### 参考博客
- [数据库入门](https://blog.csdn.net/SYaoJun/article/details/99733053)
### 插入SQL
```shell
# 建库
create database mysql_shiyan
# 建表
create table department(id int, name varchar(20), phone int);
# 插入数据
insert into department(id, name, phone) values(01, 'Tom','1316631327');
insert into department(id, name, phone) values(02, 'jerry','2020');
# 删库
drop database shiyan
# 删表
drop table department
# 主键
create table user(id int primary key, name varchar(20));
# 自增
create table user(id int primary key auto_increment, name varchar(20));
```
### 查看SQL
- 注意有分号
- SQL关键字忽略大小写
```shell
# 查看数据库
show databases;
# 使用数据库 
use shiyan
# 查看表名列表
show tables;
# 查看表的具体内容, 前100条
select * from department limit 100;
# 查看表结构
describe department
desc department
```
### 设置隔离级别
```sql
set global transaction isolation level read committed # 修改隔离级别
select @@x_isolation  # 查看隔离级别
```
### 常用CRUD
1. from
2. where
3. group by
4. having
5. order by 
6. limit
7. select
- 上述是sql语句关键字的执行顺序。