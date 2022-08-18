# introduction
## 分布式需求
1. 并行计算 parallelism
2. 容错 fault tolerance
3. 物理容量限制
4. 安全隔离
## 挑战
1. 并发
2. 部分错误
3. 性能
## 课程安排
1. lectures
2. papers
3. exams
4. labs
5. projects
## labs
1. mapreduce
2. raft (领导者选举，日志复制)
3. kv server
4. sharding kv service
## debugging
1. time-consuming
## infrastructure for applications 
1. storage
2. computation
3. communication
## implementation
1. rpc
2. thread
3. concurrency control
## 性能
1. 可扩展（多对多的子系统）
2. 容错
3. 可用性
4. 可恢复性（非易失存储器，副本）
5. 一致性consistency（put和get）强一致性，弱一致性
## mapReduce框架
1. 先在每个节点map---task
2. 再集中调用多次reduce---job
3. 管道pipeline