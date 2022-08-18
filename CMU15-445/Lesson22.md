# 分布式OLTP数据库

### 2PC
- 两阶段提交：所有节点正常工作。

### 协调事务
- paxos
- raft
### paxos
- proposer
- acceptor
### multi-paxos

### replica
- 架构配置
- 同步策略（同步/异步）
  - 同步：主prepare，flush从，从ACK，主commit。
  - 异步：主commit，自己再去同步。
  - 折中：受到大多数的ACK后，则直接提交。
- 同步的时机
- 同步数据
  - 原生SQL
  - 解析优化后的SQL
  - 混合型
### CAP Theorem
- Consistency 
- Availability 服务器挂了
- Partition Tolerance 网络挂了，双主，允许分区容错，则失去一致性
### 思考
- 组一个多种数据库系统的集群，mysql、tidb、Oracle，需要提供统一的接口——联邦数据库。