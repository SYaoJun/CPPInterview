# Database System / 数据库系统

Technical Requirements for C++ Database System Developer

## Core Components / 核心组件

### SQL Engine / SQL引擎
- SQL parser and lexer
- Query analyzer and semantic checker
- Query optimizer (cost-based, rule-based)
- Query execution engine

### Storage Engine / 存储引擎
- B+ tree and LSM-tree implementations
- Buffer pool management
- Page management and eviction strategies
- Write-Ahead Logging (WAL)

## Query Processing / 查询处理

### Operators / 算子
- **Scan Operator / 扫描算子**: Full table scan, index scan
- **Aggregation Operator / 聚集算子**: GROUP BY, DISTINCT, aggregate functions
- **Join Operator**: Nested loop, hash join, merge join
- **Sort Operator**: External sorting for large datasets

### Query Optimization / 查询优化
- **Predicate Pushdown / 谓词下推**: Push filters down to reduce data movement
- **Constant Folding / 常量折叠**: Evaluate constant expressions at compile time
- **Join Reordering**: Find optimal join order
- **Index Selection**: Choose best index for query

## Transaction Management / 事务管理

### Two-Phase Locking / 两阶段锁
- **Strong Two-Phase Locking / 强两阶段锁**: Locks held until transaction commits
- **Strict Two-Phase Locking / 严格两阶段锁**: Write locks held until transaction ends

### MVCC (Multi-Version Concurrency Control)
- **Snapshot Isolation / 快照隔离**: Read consistent snapshot of data
- Version chain management
- Garbage collection of old versions

## Logging and Recovery / 日志与恢复

### Log Types / 日志类型
- **Undo Log**: For rollback and MVCC
- **Redo Log**: For crash recovery
- **Batch Write / 批量写入**: Group commit for performance

### Recovery Mechanisms
- Checkpointing
- ARIES recovery algorithm
- Point-in-time recovery

## Compression / 压缩
- **ZSTD**: Facebook's Zstandard compression
- **Snappy**: Google's fast compression
- Dictionary compression
- Page-level compression

## Replication / 复制
- **Logical Replication**: Row-based or statement-based
- **Physical Replication**: Block-level streaming replication
- Synchronous vs asynchronous replication
- Multi-master replication

## Index Structures / 索引结构

索引是数据库中对表的字段进行排序的一种数据结构。

### Index Types / 索引类型
1. **B+ Tree**: Default balanced tree, efficient for range queries
2. **Hash Index**: O(1) lookup, not suitable for range queries / 哈希表不利于范围查找
3. **AVL Tree**: Self-balancing binary search tree
4. **Red-Black Tree**: Balanced BST, performance degrades with large data / 红黑树在数据量大的时候性能会下降

### Composite Index / 联合索引
- Multiple column indexing
- Leftmost prefix matching
- Index intersection

## C++ Skills Required / C++技能要求

### Language Features
- Modern C++ (C++11/14/17/20)
- Template metaprogramming for type-safe operators
- Lock-free data structures for high concurrency
- Memory pools for buffer management
- Zero-copy I/O techniques

### Performance Optimization
- Cache-friendly data structures
- SIMD vectorization for data processing
- NUMA-aware memory allocation
- Async I/O (io_uring)

## Tools & Technologies
- RocksDB/LevelDB for storage engine reference
- PostgreSQL/MySQL internals study
- Jemalloc/Tcmalloc for memory allocation
- Protocol Buffers for internal communication
