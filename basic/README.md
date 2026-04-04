<p align='center'>
<a href="https://github.com/syaojun/cppinterview" target="_blank"><img alt="GitHub" src="https://img.shields.io/github/stars/syaojun/cppinterview?label=Stars&style=flat-square&logo=GitHub"></a>
<a href="https://mp.weixin.qq.com/s/YeyAgD52zCadtrdXLxrT9A" target="_blank"><img src="https://img.shields.io/badge/%E5%85%AC%E4%BC%97%E5%8F%B7-@%E6%88%91%E4%B8%8D%E6%98%AF%E5%8C%A0%E4%BA%BA-000000.svg?style=flat-square&logo=WeChat">
<a href="https://www.zhihu.com/people/wan-yi-er-89" target="_blank"><img src="https://img.shields.io/badge/%E7%9F%A5%E4%B9%8E-@姚军-000000.svg?style=flat-square&logo=Zhihu"></a>

</p>

# C/C++基础面试问题
## 类中成员函数有两个`void hello()`和`void hello() const`，怎么在调用是区分调的哪一个？
根据创建的实例对象而决定，如果实例对象是const则自动调第二个，如果非const调用第一个。

## 析构函数是否可以重载？析构函数是否可以是虚函数？如果不是虚函数会产生什么问题？举个例子
析构函数不可以重载。
析构函数不重载，可能导致父类资源无法释放。
构造函数的调用顺序是，先构造父类，再构造子类。析构函数的顺序是反过来的，先析构子类，再析构父类。
```c++
#include <iostream>

class Base {
public:
    Base() {
        std::cout << "Base constructor called." << std::endl;
    }

    // 注意：这里没有将析构函数声明为虚函数
    ~Base() {
        std::cout << "Base destructor called." << std::endl;
    }
};

class Derived : public Base {
public:
    Derived() {
        std::cout << "Derived constructor called." << std::endl;
    }

    ~Derived() {
        std::cout << "Derived destructor called." << std::endl;
    }
};

int main() {
    Base* ptr = new Derived();  // 创建一个Derived对象，并用Base指针指向它
    delete ptr;  // 通过基类指针删除对象

    return 0;
}
// 如果析构不是虚函数，那么只会释放父类的资源，而泄露了子类的资源
```

## 什么场景需要用dynamic_cast？
如果想要将父类转换为子类，需要父类中至少有一个虚函数，dynmic_cast依赖于运行时类型信息（RTTI），因此需要虚函数的存在。
```c++

## #include <iostream>
#include <exception>

class Base {
public:
    virtual ~Base() {}  // 基类需要至少一个虚函数（通常是析构函数），以支持RTTI
};

class Derived1 : public Base {
public:
    void derived1Function() {
        std::cout << "Derived1 function called." << std::endl;
    }
};

class Derived2 : public Base {
public:
    void derived2Function() {
        std::cout << "Derived2 function called." << std::endl;
    }
};

int main() {
    Base* basePtr1 = new Derived1();
    Base* basePtr2 = new Derived2();

    // 尝试将 basePtr1 转换为 Derived1*
    Derived1* derivedPtr1 = dynamic_cast<Derived1*>(basePtr1);
    if (derivedPtr1) {
        derivedPtr1->derived1Function();
    } else {
        std::cout << "Conversion to Derived1 failed." << std::endl;
    }

    // 尝试将 basePtr2 转换为 Derived1*（应该失败）
    Derived1* derivedPtr2 = dynamic_cast<Derived1*>(basePtr2);
    if (derivedPtr2) {
        derivedPtr2->derived1Function();
    } else {
        std::cout << "Conversion to Derived1 failed (as expected)." << std::endl;
    }

    // 清理内存
    delete basePtr1;
    delete basePtr2;

    return 0;
}
```

## 什么是柔性数组？有什么用处？
柔性数组（Flexible Array Member）是C99引入的特性，允许结构体的最后一个成员是未知大小的数组。
```c
typedef struct {
    int length;
    char data[];  // 柔性数组，不占用结构体大小
} Buffer;
```
用处：
1. 减少内存分配次数（只需一次malloc）
2. 内存连续，提高缓存命中率
3. 灵活处理变长数据

## 什么是大小端？如何用代码判断大小端？
- 大端（Big-Endian）：高位字节存储在低地址
- 小端（Little-Endian）：低位字节存储在低地址

判断代码：
```c++
bool isLittleEndian() {
    int num = 1;
    return *(char*)&num == 1;
}
```

## 如何定位内存泄露问题？
1. **Valgrind**: `valgrind --leak-check=full ./program`
2. **AddressSanitizer**: 编译时加 `-fsanitize=address`
3. **mtrace**: 使用 `mtrace()` 和 `muntrace()`
4. **智能指针**: 使用 `std::shared_ptr`/`std::unique_ptr`
5. **自定义内存分配器**: 重载 `new`/`delete` 追踪分配

## 如何使用perf分析程序性能？
```bash
# 记录性能数据
perf record -g ./program

# 查看报告
perf report

# 查看热点函数
perf top

# 统计缓存未命中
perf stat -e cache-misses ./program
```

## C/C++内存模型
- **栈区**：局部变量、函数参数，自动管理
- **堆区**：动态分配（malloc/new），手动管理
- **全局/静态区**：全局变量、静态变量
- **代码区**：程序指令
- **常量区**：字符串常量、const变量

C++11内存模型还定义了：
- 原子操作的内存序（memory_order_relaxed/acquire/release/seq_cst）
- happens-before关系

## 什么是内存对齐？为什么内存要对齐？
内存对齐：数据存储在地址为数据大小整数倍的内存位置。

原因：
1. **硬件要求**：某些架构只能访问对齐地址
2. **性能优化**：未对齐访问需要多次内存读取
3. **原子操作保证**：对齐地址上的操作是原子的

## 提高C/C++程序性能的技巧？
1. **减少内存分配**：使用内存池、对象池
2. **缓存友好**：数据局部性，避免伪共享
3. **SIMD指令**：使用AVX/SSE向量化
4. **预取**：`__builtin_prefetch` 预加载数据
5. **内联函数**：减少函数调用开销
6. **编译器优化**：`-O3`, LTO链接时优化
7. **无锁编程**：CAS操作代替锁
8. **分支预测**： likely/unlikely 提示

## C/C++互相调用通常在头文件中做什么处理？
```c++
#ifdef __cplusplus
extern "C" {
#endif

// C兼容的声明
void c_function(void);

#ifdef __cplusplus
}
#endif
```
- `extern "C"` 禁用C++名称修饰，确保C能链接

## static在类成员变量和类成员函数中有什么作用？
静态成员函数只能访问静态成员变量。静态成员变量在所有对象中共享。
## 如何实现类的单例模式？
```c++
class Singleton {
public:
    static Singleton& getInstance() {
        static Singleton instance;  // C++11保证线程安全
        return instance;
    }
    
    // 禁止拷贝和赋值
    Singleton(const Singleton&) = delete;
    Singleton& operator=(const Singleton&) = delete;

private:
    Singleton() = default;
};
```

## 如何判断链表是否有环？如何找到链表的中点？如何对链表排序？如何对二叉树做层序遍历？给定四个坐标如何判断是否是正方形？
**判断链表有环**：快慢指针（Floyd判圈算法）
```c++
bool hasCycle(ListNode* head) {
    ListNode *slow = head, *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}
```

**链表排序**：归并排序（O(n log n)，稳定）

**二叉树层序遍历**：BFS使用队列

**判断正方形**：
1. 四条边相等，两条对角线相等
2. 或对角线相等且互相垂直平分

## 如何提高TLB缓存命中率？
1. **大页内存**：使用HugePage（2MB/1GB）减少页表项
2. **数据局部性**：连续访问内存，减少页切换
3. **减少工作集**：只保留必要数据在内存
4. **预映射**：`mlock`锁定关键页面
5. **NUMA优化**：线程绑定本地内存

## 什么时候需要用虚函数？
1. **多态场景**：通过基类指针调用派生类实现
2. **接口设计**：抽象基类定义接口
3. **运行时类型判断**：配合 `dynamic_cast` 使用
4. **析构函数**：有继承关系的类必须虚析构

## 什么时候需要用智能指针？
想要malloc和new时，不用显式分配内存和管理内存，就可以使用智能指针。

## 移动语义与完美转发
**移动语义**：转移资源所有权，避免深拷贝
```c++
std::vector<int> v1 = {1,2,3};
std::vector<int> v2 = std::move(v1);  // 移动构造
```

**完美转发**：保持值的类别（左值/右值）传递参数
```c++
template<typename T>
void wrapper(T&& arg) {
    func(std::forward<T>(arg));  // 完美转发
}
```
- 使用 `std::forward` 和万能引用 `T&&`

## C++20协程
协程是挂起/恢复执行的函数，包含三个关键字：
- `co_await`：挂起等待结果
- `co_yield`：生成值并挂起
- `co_return`：返回并结束

```c++
std::generator<int> range(int n) {
    for (int i = 0; i < n; ++i)
        co_yield i;
}
```
应用场景：异步I/O、生成器、状态机

## 源文件生成可执行文件的过程
1. **预处理**（Preprocessing）：宏展开、头文件包含、条件编译
2. **编译**（Compilation）：生成汇编代码
3. **汇编**（Assembly）：生成目标文件（.o/.obj）
4. **链接**（Linking）：合并目标文件和库，解析符号引用

## 内存管理？如何避免内存碎片？
**内存分配器**：
- ptmalloc（glibc默认）
- jemalloc（多线程友好）
- tcmalloc（Google）

**避免碎片**：
1. **内存池**：预分配固定大小块
2. **对象池**：复用对象
3. **伙伴系统**：分配2^n大小块
4. ** slab分配器**：按大小分类缓存

## 线程上下文切换会做哪些工作？
1. 保存当前线程的寄存器状态（PC、SP、通用寄存器）
2. 保存线程的虚拟内存映射（页表指针）
3. 选择下一个执行的线程（调度器）
4. 恢复新线程的寄存器状态
5. 刷新TLB（如果是进程切换）
6. 跳转到新线程的程序计数器继续执行

开销：几十微秒到几百微秒，涉及内核态切换

## 虚拟地址空间到物理地址空间的流程说一下
1. CPU发出虚拟地址
2. MMU查询TLB缓存：命中则直接得到物理地址
3. TLB未命中：查询页表（多级页表遍历）
4. 页表项有效：更新TLB，转换为物理地址
5. 页表项无效：触发缺页中断，从磁盘加载页面
6. 物理地址发送到内存总线访问数据

## 如何减小锁的粒度？如何避免死锁？
**减小粒度**：
1. **分段锁**：将大锁拆分为多个小锁
2. **读写锁**：`std::shared_mutex` 区分读写
3. **无锁数据结构**：CAS操作
4. **Thread-Local**：每个线程独立数据

**避免死锁**：
1. **锁顺序一致**：所有线程按相同顺序获取锁
2. **超时机制**：`std::try_lock_for`
3. **死锁检测**：资源分配图检测循环
4. **避免持有锁时调用外部代码**

## 如何保证程序是线程安全的？
1. **不可变数据**：const数据天然线程安全
2. **原子操作**：`std::atomic` 对基本类型
3. **互斥锁**：`std::mutex` 保护临界区
4. **条件变量**：`std::condition_variable` 同步
5. **线程局部存储**：`thread_local` 变量
6. **无锁设计**：消息队列、RCU机制

## 如何实现一个线程安全的延迟队列？
使用优先队列 + 条件变量：
```c++
class DelayedQueue {
    std::priority_queue<Task> pq;
    std::mutex mtx;
    std::condition_variable cv;
    
public:
    void push(Task task) {
        std::lock_guard<std::mutex> lock(mtx);
        pq.push(task);
        cv.notify_one();
    }
    
    Task pop() {
        std::unique_lock<std::mutex> lock(mtx);
        cv.wait(lock, [this]{ return !pq.empty() && pq.top().ready(); });
        Task t = pq.top(); pq.pop();
        return t;
    }
};
```

## 如何实现原子操作CAS
**CAS**（Compare-And-Swap）：比较内存值与预期值，相等则更新
```c++
std::atomic<int> value;
int expected = old_val;
bool success = value.compare_exchange_strong(expected, new_val);
```

**ABA问题解决**：
- 使用带版本号的指针（Tagged Pointer）
- `std::atomic` 的 compare_exchange 自动处理

**自旋锁实现**：
```c++
class SpinLock {
    std::atomic<bool> flag{false};
public:
    void lock() {
        while (flag.exchange(true, std::memory_order_acquire));
    }
    void unlock() {
        flag.store(false, std::memory_order_release);
    }
};
```

## 你技术上最大的优势是什么？你最擅长什么技术？C/C++功能实现，算法与数据结构，linux内核，操作系统，还是协作沟通，英语等？
（请根据个人实际情况填写）

---

# Career Directions / 就业方向

This repository also contains technical requirements for various C++ career directions:

- [autonomous_driving](./autonomous_driving) - Autonomous Driving / 自动驾驶
- [audio_video](./audio_video) - Audio-Video Processing / 音视频
- [game_development](./game_development) - Game Development / 游戏开发
- [server_development](./server_development) - Server Development / 服务器开发
- [live_streaming](./live_streaming) - Live Streaming / 直播推流
- [search_ads_rec](./search_ads_rec) - Search, Ads, Recommendation / 搜广推
- [compiler](./compiler) - Compiler Development / 编译器开发
- [database_system](./database_system) - Database System / 数据库系统
- [storage_system](./storage_system) - Storage System / 存储系统