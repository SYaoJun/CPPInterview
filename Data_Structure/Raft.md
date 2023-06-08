# Raft共识算法
- 基于multi-paxos做了一些简化和限制，日志必须是连续的，只支持三个角色。
### Goal
- replicated log => replicated state machine
### approaches to consensus
- leader-based
### overview
1. leader election 领导者选举
2. replicated log 日志复制
3. member change 成员变更
### 核心
1. 领导人选举
2. 日志一致性复制
### 典型应用
1. etcd
2. consul
3. cockroachDB
### 角色
- leader
- follower
- candidate
### leader 
### rpc
1. request vote 请求投票（候选人发起）
2. append entries 追加日志（领导者发起）
### 任期
- 变成candidate后自动增加一次任期
### Leader
- 周期性向follower发起心跳检测
- 选举无效，等待的时间间隔是随机的。
- 只有leader能写入，先本地写入，未提交，然后同步到follower，follower响应写完成后，leader再提交，leader再让follower提交。
### follower
- 随机超时时间，等待领导者心跳信息超时。
- 节点之间沟通采用的rpc
- 在一次选举中，每一个服务器节点最多会对一个任期编号投出一张选票，并且是先到先投。
### 限制
- 主节点的读写
- 集群扩展主节点
### 参考视频
- [分布式系统之一致性算法Raft](https://www.bilibili.com/video/BV1Db411w7ej/?spm_id_from=333.788.recommend_more_video.2&vd_source=e9f1ced96b267a4bc02ec41ca31d850a)
- [raft一致性算法原理](https://www.bilibili.com/video/BV1eN411Z7KF?spm_id_from=333.337.search-card.all.click&vd_source=e9f1ced96b267a4bc02ec41ca31d850a)