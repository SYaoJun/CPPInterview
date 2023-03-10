# 分布式系统distributed system
- 更大的操作系统
### CAP理论
- Consistency
- Availability
- Partial Tolerance
### 共识算法
- paxos
- multi-paxos
- raft
- zab
- gossip
### 分布式事务
- Two-Phase Committed (2PC)
- Three-Phase Committed (3PC)
### 分布式锁
- 分布式锁实现原理：多进程可见，互斥，可重入，高并发，高可用。
- 常见的分布式锁实现方案：基于数据库实现，基于缓存实现，基于zookeeper实现
- 分布式锁实现方式
    1. redis：setnx或者redission库
    2. mysql
    3. zk
    4. etcd
    5. chubby
### 分布式ID
- uuid
- 数据库自增ID
- 基于数据库的号段
- 雪花算法snowflake
- 百度uid-generator
- 美团leaf
- 滴滴Tinyid
### 网络
- DNS
- TCP
- HTTP
### 挑战
1. 网络延迟
2. 单机故障
### 分布式核心问题
1. 海量数据的存储（更难），本质：CAP理论。参考：hdfs
2. 计算：函数式编程，参考：mapreduce/hadoop
