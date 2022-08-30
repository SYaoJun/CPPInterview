# TIDB
- 主要学习PingCAP的TiBD的源码，可以关注公司官网的博客。
### 优势
- 传统数据库容量有限，mysql超过5000万以后，性能开始下降。
- 分库分表，分布式事务复杂，sql语法受限，如join。
- 简化OLTP和OLAP，消除复杂的ETL流程。
### 整体架构
- 三个核心：
  1. 存储
  2. 计算
  3. 调度
- PD server：集群管理，存元数据，负载均衡，分配全局唯一的事务ID。region为单位调度。
- TiDB server：负责接收sql请求。
- TiKV：存储引擎，RocksDB支持TB级别存储，LSM tree数据结构，参考HBASE。
### 核心特性
1. 水平扩展（计算和存储能力）
2. 高可用（raft）
3. 高度兼容mysql
4. 分布式事务
5. HTAP解决方案
6. 云原生（TiDB operator）
### 存储方式
1. 键值对map
2. 按照key的二进制排序
### RocksDB
- 开源单机存储引擎，FaceBook在维护
- 基于LSM Tree
### NoSQL
- Redis
- MongoDB
### NewSQL
- TiDB
- Azure
- OceanBase
- PolarDB
- ClickHouse
- CockRoach
- GreenPlum
- Apache Doris
### 数据库选型
- 功能
- 性能
- 高可用
- 社区活跃度
- 维护成本
- 结合原有某块的复杂度
### 数据中台
- 数据库
- 中间件
- 存储
### 业务线
- 房地产（贝壳找房）国内或国外
- 人工智能（涂鸦）ToB或ToC
- 物流（顺丰快递）
- 爱奇艺（视频，会员）