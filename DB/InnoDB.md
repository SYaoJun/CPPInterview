# MySQL
- 关系型数据库
### 参考书籍
- 《MySQL技术内幕：InnoDB存储引擎》
### myISAM和InnoDB的区别
- InnoDB引擎：
  1. 支持事务
  2. 行锁（适合高并发）
  3. 支持外键
  4. MySQL 5.5版本后的默认存储引擎
- MyISAM引擎：
  1. 不支持事务
  2. 不支持外键
  3. 支持表锁。优势是访问的速度快。
  4. MySQL 5.5版本前的默认存储引擎。
  5. myISAM索引文件和数据文件是分离的，查询较多的更新较少的情况下优先使用。

### Clustered Index 聚集索引
- [参考视频](https://www.bilibili.com/video/BV1Er4y1572y?spm_id_from=333.337.search-card.all.click&vd_source=e9f1ced96b267a4bc02ec41ca31d850a)
- [参考文档](https://zhuanlan.zhihu.com/p/401198674)
- 聚集索引，又称为主键索引，如果没有主键，innodb会默认选择或添加一个主键。
- 聚集索引的存储并不是物理上连续的，而是逻辑上连续的。
- 叶子节点中存放的即为整张表的行记录数据。
- InnoDB是索引组织表，表中数据按照主键顺序存放。
- 聚集索引是按照每张表的主键，构造一颗B+树，同时叶子节点中存放的即为整张表的行记录数据，也将聚集索引的叶子节点称为数据页data page。
- 每张表只能拥有一个聚集索引。
- 对name建立了索引，查询到name=yaojun这条数据，yaojun所在的行中，主键是id=26，所以拿着id=26去主键索引里面查这一行的全部数据。
- 回表：通过辅助索引找到了主键值，在通过主键索引获取到这个主键值所对应的行记录。
### Secondary Index 辅助索引
- 辅助索引，又称为非聚集索引，或者二级索引。
- 辅助索引是指叶子节点并不包含行记录的全部数据。
- 通过辅助索引叶节点指针获得指向主键索引的主键，然后通过主键索引来找到一个完整的行记录。
- 聚集索引和辅助索引的区别在于叶子节点存放的是否是一整行的信息。
- 所有辅助索引的叶子节点都引用主键索引，过长的主索引会使得辅助索引变得过大。
- 唯一索引，普通索引，前缀索引都是二级索引
> 思考：为什么辅助索引叶子节点不直接存行记录的指针，而要存主键索引的值？
### Undo log
- 记录每个操作对应的回滚操作，比如插入一条数据时，就在对应的undo log中记录一条删除命令。
- 每当我们对一条记录做改动insert/delete/update时，都需要把以后回滚的东西记录下来。
- 所有的改动形成一个版本链，版本链的头节点就是当前记录的最新的值。
- undo log删除时机：没有比这个undo log更早的read view时，undo log就会被删除。
### redo log
- [redo log刷盘规则](https://www.bilibili.com/video/BV1M3411G7uw?spm_id_from=333.999.header_right.history_list.click&vd_source=e9f1ced96b267a4bc02ec41ca31d850a)
- redo log结构

| redo_log_type |space|page_no|redo_log_body|
|---|---|---|---|
| 类型 |表空间ID|页的偏移量|数据部分|

- 物理日志。记录每个page更改的物理情况。
- 先写入redo log buffer（内存）, 然后按一定的条件顺序写入redo log files（磁盘）。可以配置innodb_flush_log_at_trx_commit的值，决定同步还是异步，性能和完整性的trade off。
- 用于恢复已提交事务修改的页操作。
- commit的时候，刷新脏页到缓冲池，而不是刷到磁盘，借助redo log保证变更持久化。
- 记录数据的逻辑修改。
  - 更新buffer pool页里面的数据
  - 生成一个redo log对象
  - commit后，持久化这个redo log对象到磁盘
- 出于事务的考虑以及顺序IO比随机IO效率更高。
- 当达到checkPoint后，即log满了以后，就将数据更新到磁盘上。
- redo log有两个文件，循环写入。为什么redo log要有两个文件，因为checkpoint和write position有一定间隔。
- 写入数据流程。buffer pool -> redo log buffer -> os buffer -> redo log file
- redo log 刷盘规则
  1. commit时刷
  2. 周期间隔刷
  3. 容量大小过半刷
  4. checkpoint到达检查点时刷
### binlog和redo log的区别
- 首先，二进制日志会记录所有与MySQL数据库有关的日志记录，包括InnoDB、MyISAM、Heap等其他存储引擎的日志。而InnoDB存储引擎的重做日志只记录有关该存储引擎本身的事务日志。
- 其次，记录的内容不同，无论用户将二进制日志文件记录的格式设为STATEMENT还是ROW，又或者是MIXED，其记录的都是关于一个事务的具体操作内容，即该日志是逻辑日志。而InnoDB存储引擎的重做日志文件记录的是关于每个页（Page）的更改的物理情况。
- 此外，写入的时间也不同，二进制日志文件仅在事务提交前进行提交，即只写磁盘一次，不论这时该事务多大。而在事务进行的过程中，却不断有重做日志条目（redo entry）被写入到重做日志文件中。
### binlog
[链接](https://blog.csdn.net/eagle89/article/details/107959587?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_baidulandingword-1&spm=1001.2101.3001.4242)
- 以二进制的形式记录了数据库的变更操作，MySQL从5.1版本引入了binlog_format参数，该参数可设的值有三种格式
  1. statement记录逻辑SQL语句
  2. row记录表的行更改情况`update t2 set username = UPPER(username)`，有些语句下row可能需要更大的容量
  3. mixed混合
- 主要流程
  1. slave订阅了master的binlog
  2. 通过slave的IO线程和master的dump线程通信，同步binlog。
  3. IO线程读取到binlog后，写入到relay log中准备重放。
  4. slave通过SQL线程读取到relay log重新执行响应的操作。
- 三个关键线程
  1. slave的IO thread
  2. master的dump thread
  3. sql线程从relay log中重放数据
- 主从复制不是强一致性，而是最终一致性。
- master配合binlog会影响性能。
### 节点
- 节点大小16k
- 磁盘页4k
- 就地写：在原来存在的位置进行更新
