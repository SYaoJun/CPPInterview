# CPPInterview - C++ 面试与学习指南

<p align='center'>
<a href="https://github.com/syaojun/cppinterview" target="_blank"><img alt="GitHub" src="https://img.shields.io/github/stars/syaojun/cppinterview?label=Stars&style=flat-square&logo=GitHub"></a>
<a href="https://mp.weixin.qq.com/s/YeyAgD52zCadtrdXLxrT9A" target="_blank"><img src="https://img.shields.io/badge/%E5%85%AC%E4%BC%97%E5%8F%B7-@%E6%88%91%E4%B8%8D%E6%98%AF%E5%8C%A0%E4%BA%BA-000000.svg?style=flat-square&logo=WeChat">


本仓库整理了 C++ 相关的面试问题与各个就业方向的技术要求，帮助开发者系统学习 C++ 并准备面试。

---

## 目录结构 / Repository Structure

### 基础面试问题 / Basic Interview Questions
📁 **[basic/](./basic)** - C/C++ 基础面试问题与答案
- 面向对象：类、继承、多态、虚函数、智能指针
- 内存管理：内存模型、对齐、泄露检测
- 并发编程：线程、锁、原子操作、CAS
- 性能优化：perf分析、SIMD、缓存优化
- 数据结构与算法：链表、树、排序

### 就业方向 / Career Directions

| 目录 | 方向 | 核心技术 |
|------|------|---------|
| [autonomous_driving/](./autonomous_driving) | **自动驾驶** | ROS/ROS2, SLAM, 传感器融合, 路径规划, OpenCV, Cyber RT |
| [audio_video/](./audio_video) | **音视频处理** | FFmpeg, H.264/HEVC, 编解码, RTMP/HLS, WebRTC, 流媒体协议 |
| [game_development/](./game_development) | **游戏开发** | Unreal/Unity, 图形渲染, 物理引擎, ECS架构, 游戏网络 |
| [server_development/](./server_development) | **服务器开发** | 高并发网络编程, 分布式系统, RPC, 微服务, 数据库连接池 |
| [live_streaming/](./live_streaming) | **直播推流** | RTMP/WebRTC,  CDN, 转码, 低延迟优化, SRS |
| [search_ads_rec/](./search_ads_rec) | **搜广推** | 推荐系统, 向量检索, 倒排索引, 实时竞价, 机器学习工程 |
| [compiler/](./compiler) | **编译器开发** | LLVM/Clang, 词法/语法分析, AST/IR, 优化Pass, JIT |
| [database_system/](./database_system) | **数据库系统** | 存储引擎, SQL解析, 事务(MVCC/2PL), 查询优化, B+树/LSM |
| [storage_system/](./storage_system) | **存储系统** | 分布式文件系统, 对象存储, io_uring, Ceph/MinIO, RDMA |

---

## C++ 技术技能图谱 / C++ Skills Map

### 基础技能 / Foundation Skills

#### 语言基础
- **Modern C++**: C++11/14/17/20 特性
  - auto, lambda, range-based for
  - constexpr, consteval
  - fold expressions (C++17)
  - concepts (C++20)
  
- **面向对象**
  - 封装、继承、多态
  - 虚函数与虚表
  - 虚析构函数
  - 抽象类与接口
  
- **内存管理**
  - 栈 vs 堆
  - new/delete, malloc/free
  - 智能指针 (unique_ptr, shared_ptr, weak_ptr)
  - 内存对齐与填充
  - 内存泄露检测 (Valgrind, ASan)

- **模板与泛型**
  - 函数模板、类模板
  - 模板特化与偏特化
  - SFINAE
  - 模板元编程

#### 标准库 (STL)
- **容器**: vector, list, deque, map, unordered_map, set
- **算法**: sort, find, lower_bound, transform
- **迭代器**: 各种迭代器类型与 Traits
- **函数对象与谓词**: std::function, std::bind
- **Allocator**: 自定义分配器

#### 并发编程
- **线程管理**: std::thread, std::jthread (C++20)
- **同步原语**: mutex, shared_mutex, condition_variable, semaphore
- **原子操作**: std::atomic, memory_order
- **异步**: std::async, std::future, std::promise
- **无锁编程**: CAS, lock-free data structures

### 高级技能 / Advanced Skills

#### 系统编程
- **Linux系统调用**: fork, exec, mmap, epoll
- **网络编程**: socket, TCP/UDP, io_uring, DPDK
- **文件I/O**: 同步/异步, 内存映射, 直接I/O
- **进程间通信**: pipe, shared memory, message queue
- **信号处理**: signal, sigaction

#### 性能优化
- **编译器优化**: -O3, LTO, PGO
- **缓存优化**: 数据局部性, 伪共享避免, cache line对齐
- **SIMD**: SSE/AVX/NEON 向量化
- **内存优化**: memory pool, allocator, zero-copy
- **Profiling**: perf, Intel VTune, gprof

#### 调试与工具
- **调试器**: GDB, LLDB
- **静态分析**: Clang Static Analyzer, cppcheck
- **构建系统**: CMake, Bazel, Makefile
- **版本控制**: Git高级操作

---

## 领域专项技能 / Domain-Specific Skills

### 高性能计算 (HPC)
- 并行计算 (OpenMP, MPI)
- GPU编程 (CUDA, OpenCL)
- 数值计算库 (Eigen, BLAS, LAPACK)

### 嵌入式开发
- 实时操作系统 (FreeRTOS, RT-Thread)
- 裸机编程
- 交叉编译
- 硬件接口 (SPI, I2C, UART)

### 安全与密码学
- 内存安全 (Rust-style ownership concepts)
- 缓冲区溢出防护
- OpenSSL/LibreSSL使用
- 安全编码实践

### 云原生与容器
- Docker容器化
- Kubernetes调度
- Service Mesh
- eBPF编程

---

## 学习路径建议 / Study Path

### 初级开发者
1. 掌握 C++ 基础语法与面向对象
2. 熟悉 STL 容器与算法
3. 理解内存管理与指针
4. 学习基础数据结构与算法

### 中级开发者
1. 深入 Modern C++ 特性
2. 掌握并发与多线程编程
3. 学习 Linux 系统编程
4. 了解编译原理与链接过程
5. 选择一个就业方向深入

### 高级开发者
1. 模板元编程与设计模式
2. 性能优化与 profiling
3. 分布式系统设计
4. 领域专家级深度 (数据库/编译器/存储等)

---

## 贡献 / Contribution

欢迎提交 Issue 和 PR 补充更多面试问题与技术文档！

---

## License

MIT License
