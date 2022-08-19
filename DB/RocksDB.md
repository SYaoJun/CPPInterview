# RocksDB
- RocksDB提供并发读写
### 解决了什么问题
- 写多读少
### 怎么解决的
- LSM Tree：不是一个数据结构，是数据的一种组织方式。
### 写日志
- 追加写，顺序写。
- 内存顺序IO >> 内存随机IO ≈ 磁盘顺序IO >> 磁盘随机IO
- 追加写：有数据重复，冗余。
### 查询
1. 前提是日志有序。
2. 抽象出数据块。
3. 二分查找。
### 数据冗余
1. 文件拆分
2. 压缩：在内存准备一个有序的数据结构，可以原地修改，进行内存随机IO，内存中文件达到一定大小，就dump到磁盘。
3. 合并（会阻塞），内存上数据没有重复，磁盘上的数据才需要去重。
### WAL
- 更改内存数据之前，先写日志WAL，称为预写日志。
### LSM tree
- log-structure merge tree
- 按冷热数据进行分层，热是最近刚刚操作的数据。
- 在内存中原地更新，在磁盘上追加更新。
- 多路归并思想，分治思想。
### LSM关键组件
1. Memtable 用于读写的内存数据块
2. immutable Memtable 只用于读的内存块
3. WAL预写日志
4. SSTable有序字符串表（分层合并）（L0到LN）
### 磁盘分层
1. Level0层中，单个数据块是从内存中导出的，不存在重复，但是数据块间存在重复。
2. Level1到Leveln层中，每一层中没有数据重复。
3. 层与层之间有冗余数据。
4. 在单个层中，每个数据块有序且不重复。
### 内存中采用什么数据结构？
- 跳表（可行）levelDB
- B+树
### RocksDB中的数据结构
1. skiplist
2. hash-skiplist
3. hash-linklist
### RocksDB相对于LevelDB的优化
1. 加速层间的查找，利用指针限定查找的范围。
### Cache
- LRU淘汰策略
- Table Cache：缓存了所有已开开的SSTable的元数据
- Block Cache：缓存SSTable中的data block和index block和filter block
### 磁盘中数据如何存储？
- B+
- SSTable
### 更新方式
- 原地更新
    1. 读优化
    2. 更新引起随机IO
- 异地更新
    1. 顺序IO写
    2. 分离的数据重新组织数据
### 读写放大
- 读放大：查多个表。
- 写放大：merge过程不断引起的重写。

### 跳表
- 多层级有序链表
- 查找：从顶层开始找，从左往右，如果当前值的下一个值比查找值大，则往下跳一层。
- 插入：先随机要索引的层数，然后简历左右节点关联。
- 并发写：高度和节点加了原子锁。
### 参考视频
- [RocksDB基本原理](https://www.bilibili.com/video/BV1RL411w7Pu?spm_id_from=333.337.search-card.all.click&vd_source=e9f1ced96b267a4bc02ec41ca31d850a)