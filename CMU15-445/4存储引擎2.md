# 存储引擎II
### log-structured file organization
- tuple存的不是数据本身，而是日志记录。
- 将随机写转换为顺序写，读和压缩的开销。
1. 删除。新增一条删除日志。
2. 更新。新增一条更新日志。
- 常用在KV数据库
### 读数据
1. 从后往前找，重新构建实际数据。
2. 也可以建索引。
3. 周期性地压缩日志。
### log-structured compaction
- level compaction。当前层的两个块合并到下一层。基于多路归并的思路。
### rocksdb
- 最多可以压缩到第7层
### big decimal
- 以字符串的形式存数据
### large values
- overflow page 溢出页存超长数据
### system catalogs
- 以表的形式存储自己的元数据
- information schema
### 分离架构
1. TP
2. ETL
3. AP
### NSM 行存
- tuple 
- index
### DSM 列存
- 点查很差
- 分开存储维护成本
## Buffer Pool and Memory Management
- On-Line Analytical Processing(OLAP)
- On-Line Transaction Processing(OLTP)
- Hybrid Transaction + Analytical Processing(HTAP)
## Database Storage
- Problem #1: how to 
- Problem #2: disk page to memory
## Policy
- buffer-replacement strategies
  - LRU
  - LFU
  - MRU
  - CLOCK
  - LRU-K
## Algorithm Implement in Go
- LUR
- MRU
## Column-Oriented Database
- Frame
- Page
- Block
## Terms
- Lock
- Latch

