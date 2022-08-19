# 分布式OLTP数据库
### 2PC
- 两阶段提交：前提是所有节点正常工作。
- 协调者挂掉：系统处于未决策状态，新协调者再次为事务决策收集投票。
- 参与者挂掉：默认为投的反对票。
### 3PC
- propose
- prepare
- commit
- 3PC增加了一个额外的propose阶段，并且双方都具有超时机制。
- 可以解决2PC阻塞问题，却带来了更大的消息开销和网络分区下的不一致性（一些节点提交，一些节点中止）。
### 协调事务
- paxos
- raft
### paxos
- proposer
- acceptor
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
### Federated Database
- 联邦数据库
## 关键技术
- 分布式系统
- 故障转移
- 性能优化

## 数据库的机会

- 场景创新
- 硬件与云计算
- 大数据量
- 多维度实时分析决策系统

## 分布式关键问题
- 存储
  1. 分布式事务实现方式:2pc,3pc,calvin,spanner,percolator
    - 原子提交：2pc和3pc, 2pc：阻塞原子提交算法
    - 共识算法：Calvin和Spanner都适用paxos
    - Percolator（快照隔离，SI）事务模型，快照隔离能避免读倾斜read skew，可能存在写倾斜write skew。
      - 读倾斜：可以理解为读交叉，不能达到串行化。
      - 写倾斜：可以理解为写交叉。
      - 快照读的优势：不需要加锁，读的效率较高。
      - percolator是一个在bigtable数据库上实现事务API的库。
  2. 共识算法（raft，paxos，gossip，zab）
  3. 分片（一致性哈希）分片：将数据切分成较小易管理的段。
  4. 副本
  5. 恢复（WAL）
  6. 缓冲池
  7. 文件格式
  8. 并发控制：MVCC，T/O，OCC
  9. 索引：B+，LSM
- 计算
  1. 算子下推
  2. 查询计划
- 调度

## RocksDB
- LSM
- SSTable
## 现代数据库
1. 存储引擎
2. 分布式系统