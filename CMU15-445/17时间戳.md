# 时间戳顺序并发控制 Timestamp ordering
- 锁必然带来性能上的开销，无锁是最好的并发
### 悲观锁和乐观锁
- 悲观锁2PL
- 乐观锁T/O
### 时间戳分配
1. 系统时钟system clock：每隔一段时间会自动校准
2. 逻辑计数器logical counter：递增计数
3. hybrid
###  today's agenda
- basic T/O protocol
- optimistic concurrency control
- isolation levels
### 隔离级别
- 读未提交
- 读提交
- 可重复读
- 可串行化
### snapshot isolation快照隔离
- 1995年提出

