## Buffer Pool
- 内存缓冲池管理
### 局部性原理
- 时间控制
- 空间控制
### Access Time
- L1 Cache 0.5ns
- L2 Cache 7ns
- DRAM 100ns
- SSD 0.15ms
### 页和帧
- Page 页：物理磁盘上的存储单元。
- Frame 帧：内存上的存储单元，跟Page大小相同。
### 页表和页目录
- Page Table 页表：内存池的索引，用于查询对应的Page或Frame。
- Page Directory 页目录：磁盘上的索引，跟页表是同一回事。
### 锁和闩
- Lock 锁：逻辑上，抽象上，high level的。
- Latch 闩：底层实现，粒度较小，如mutex。
### 查询优化策略
- multiple buffer pools 多个缓冲池，如每个数据库分配一个。
- pre-fetching 预处理。
- synchronized scans 多个查询同步进行。

### DB缓冲池和OS缓冲的区别
- 两者都是用来解决内存和磁盘读写速度不匹配的问题。
- DB缓冲池一般会绕过OS page cache，因为DB缓冲池更清楚的知道什么页需要替换出去。
### Buffer Replacement Policy
- 缓冲页替换策略
    - LUR least recently used 最近最少使用
    - Clock 将标记为1的清理出去，指针环形遍历。
    - LRU-K 记录每个页最近K次换入时间，按照估值替换。
### Dirty Page 脏页
- WAL 记录日志
- 定期刷新脏数据
### Memory Pools
- query cache查询缓存
- log buffer
- dictionary cache

    