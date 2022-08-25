# 存储引擎I
- 随机存取转化为磁盘中的顺序存取
### system design goals
- 管理超过内存的大小
### today's agenda
1. file storage
2. file layout
3. tuple layout
### file storage
- 基于空间和时间局部性进行调度
### pages
- hardware page(4K)
- os page (4K)
- database page (512B-16KB)：postgreSQL(8K) mysql(16K)
1. header
2. data
### page header
- 每个页包含一个保存元数据的header
1. page size
2. checksum
3. DBMS version
4. transaction visibility
5. compression information
### file layout
1. tuple-storage
2. log-structure
### 直接存tuple存在的问题
- 数据是变长的，删除了某个page如何处理？
### slotted pages
1. header后面放的是定长的slot array，从前往后分配。
2. page从后往前分配实际的数据内容，通过slot指针指向实际内容，可以通过整理消除空闲空间的碎片。
3. 标记：page_id + offset/slot_id
### tuple layout
1. header：
    - visibility info
    - bitmap for null values
2. attribute data
