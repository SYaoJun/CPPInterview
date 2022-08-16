### 创建线程的方式★★★

- 继承Thread类
- 实现Runnable接口
- 实现Callable接口

通过实现Runnable接口的特点

-   资源类是一个单独的类，线程和资源类解耦。

通过实现Callable接口的特点

- 有返回值，会阻塞
- 可抛出异常
- 有缓存



### Synchronized和lock的区别

1. synchronized时Java内置的关键字，lock是一个接口
2. synchronized会自动释放锁，lock需要手动释放。
3. synchronized线程获取方式是阻塞等待，而lock可以尝试获取锁。
4. synchronized是非公平锁，Lock可以设置公平与非公平
5. synchronized适合锁少量的同步代码，lock适合锁大量的同步代码。

**Lock的主要特性**

- 尝试非阻塞地获取锁
- 能被中断地获取锁
- 超时获取锁



### Java的BIO，NIO和AIO★★

- BIO：blocking IO 同步阻塞I/O模式，数据的读取写入必须阻塞在一个线程内等待其完成。

- NIO：non-blocking IO 是一种同步非阻塞的I/O模型，在Java 1.4 中引入了NIO框架，对应 java.nio 包，提供了 Channel , Selector，Buffer等抽象。 它支持面向缓冲的，基于通道的I/O操作方法。

- AIO：asynchronous IO 它是异步非阻塞的IO模型。 异步IO 是基于事件和回调机制实现的，也就是应用操作之后会直接返回，不会堵塞在那里，当后台处理完成，操作系统会通知相应的线程进行后续的操作。

### 线程的状态★★

- New
- Runtime
- Blocked
- Waiting
- Timed_waiting
- Terminated

### volatile

- 保证可见性
- 不保证原子性
- 禁止指令重排

volatile是如何保证的可见性？

- 线程会拷贝内存中的值到工作内存中。
- 读取：read / load/ use/ assign
- 写入：store/write/lock/unlock

线程B修改了值，但是线程A不能立即可见。需要让线程A知道内存中的值发生了变化



### BlockingQueue★★

阻塞队列

- 写入：满了，阻塞
- 取出：空了，阻塞

使用场景：多线程并发处理，线程池

**四组API**

1. 抛出异常
2. 不抛出异常
3. 阻塞等待
4. 超时等待

| 方式·        | 抛出异常    | 有返回值，不抛出异常 | 阻塞等待· | 等待超时退出      |
| ------------ | ----------- | -------------------- | --------- | ----------------- |
| 添加         | boolean add | boolean offer(数值)  | void put  | offer(数值，时间) |
| 移除         | T remove    | T poll(数值)         | void take | poll(数值，时间)  |
| 检测队首元素 | T element   | T peek               | -         | -                 |



### 线程池★★★

3大方法，7个参数，4种拒绝策略

[视频链接](https://www.bilibili.com/video/BV1B7411L7tE?p=23)

线程池，连接池，内存池，对象池

线程池的好处：降低资源效率，提高相应速度，方便管理

- 线程复用
- 可以控制最大并发数
- 管理线程

线程池不允许使用Executors去创建，而是通过ThreadPoolExecutor的方式，这样的处理方式让写的同学更加明确线程池的运行规则，避免资源耗尽的风险。

说明：Executors创建线程池对象的弊端如下

- FixedThreadPool和SingleThreadPoll：允许的请求队列长度为Integer.MAX_VALUE，可能会堆积大量的请求，从而导致OOM
- CachedThreadPool和ScheduledThreadPool：允许的创建线程数量为Integer.MAX_VALUE，可能会创建大量的线程，从而导致OOM

本质是：ThreadPoolExecutor()

**7大线程参数**

1. 核心线程数
2. 最大线程数
3. 超时时间
4. 超时单位
5. 阻塞队列
6. 线程工厂
7. 拒绝策略

```java
new ThreadPoolExecutor(1, 1,0L, TimeUnit.MILLISECONDS,new LinkedBlockingQueue<Runnable>())
```



**４种拒绝策略**

- AbortPolicy：直接抛出异常
- CallerRunsPolicy：调用者线程来运行该任务
- DiscardPolicy：不处理，直接丢弃。
- DiscardOldPolicy：尝试与最早的任务任务竞争



**最大的线程如何去设置**

- CPU密集型：与电脑核数相同
- IO密集型：大于耗时IO的数量即可，通常设为耗时IO的两倍。

向线程池提交任务：

- execute()用于提交不需要返回值的任务，无法判断任务是否被线程池执行成功。
- submit()用于提交需要返回值的任务，线程池会返回一个future类型的对象，通过这个future对象可以判断任务是否执行成功，并可以通过get方法获取返回值。



### ThreadLocal

作用：提供线程内的局部变量，不同的线程之间不会相互干扰，这种变量在线程的生命周期内起作用，减少同一个线程内多个函数或组件之间一些公共变量传递的复杂性。

总结：

- 线程并发：在多线程并发的场景下
- 传递数据：我们可以通过ThreadLocal在同一线程，不同组件中传递公共变量
- 线程隔离：**每个线程的变量都是独立的，不会相互影响**

ThreadLocal如何解决内存泄漏问题？每次使用完ThreadLocal，都调用它的remove()方法，清除数据。



### AQS同步器

同步器是实现Lock锁的关键。许多同步类的实现都依赖于AQS，如Reentrantlock, Semaphore, CountDownLatch

锁是面向使用者，同步器是面向锁的实现者。

AQS为每个共享资源都设置了一个共享资源锁，线程在需要访问共享资源时首先需要获取**共享资源锁**，如果获取到了共享资源锁，便可以在当前线程中使用该共享资源，如果获取不到，则将线程放入线程等待队列，等待下一次调度。

AQS维护了一个**volatile int类型的变量state**，用于表示当前的**同步状态**。
state的访问方式有三种：getState() setState() compareAndSetState()均是原子操作。

AQS共享资源的方式：

- 独占式
- 共享式

AQS只是一个框架，自定义同步器需要重写**获取和释放**方法

- tryAcquire()
- tryRelease()
- isHeldExclusively()
- tryAcquireShared()
- tryReleaseShared()



### 锁的四种状态和升级过程★★

并且四种状态会随着竞争的情况逐渐升级，而且是不可逆的过程，即不可降级，也就是说只能进行锁升级（从低级别到高级别），不能锁降级（高级别到低级别）

- 无锁
- 偏向锁(默认锁)：适用于只有一个线程访问同步块场景
- 轻量级锁(有线程竞争时，自旋10次后升级)
- 重量级锁(synchronized)



### CAS的ABA问题如何解决★★

CAS: Compare and Set 比较交换

使用版本号机制，每次更新数据前，先判断当前版本号是否和预期的版本号一致，如果不一致则不更新。



### Fork/Join

Fork/Join框架是Java 7提供的一个用于并行执行任务的框架，是一个把大任务分割成若干个小任务，最终汇总每个小任务结果得到大任务结果的框架。

工作窃取work-stealing：是指某个线程从其他线程队列中窃取任务来执行。



### happens-before

- as-if-serial语义保证单线程内程序的执行结果不改变
- happens-before关系保证正确同步的多线程程序的执行结果不改变

如果A happens-before B，那么Java内存模型向程序员保证，A操作的结果将对B可见，且A的执行顺序排在B之前。

as-if-serial语义和happens-before这样做的目的，都是为了在不改变程序执行结果的前提下，尽可能地提高程序执行的并行度。



### 四种引用

- 强引用：把一个对象赋值给一个引用变量时，这个引用变量就是强引用。有强引用的对象一定为可达性状态，所以不会被垃圾回收机制回收。
- 软引用：如果一个对象只有软引用，则在系统内存空间不足时该对象将被回收
- 弱引用：如果一个对象只有弱引用，则在垃圾回收时一定会被回收
- 虚引用：虚引用和引用队列联合使用，主要用于跟踪对象的垃圾回收状态。



### wait和sleep

1. 来自不同的类。wait来自object； sleep来自thread。
2. 关于锁的释放。wait会释放锁，sleep不会释放。
3. 使用的范围不同。wait必须在同步代码块中，sleep可以在任何地方。
4. 是否需要捕获异常。wait不需要，sleep必须要。



### 常用的并发接口★

condition的优势：精准的通知和唤醒线程。

CountDownLatch：计数，等待完成

CyclicBarrier：加法计数器

Semaphore：信号量 限流

SynchronousQueue：同步队列，最多放一个元素



### List线程不安全

如何改为线程安全的呢？

- vector
- synchronizedList
- CopyOnWriteArrayList 写入时复制

```
List<String> list = new Vector<>();
List<String> list = Collections.synchronizedList(new ArrayList<>());
List<String> list = new CopyOnWriteArrayList<>();
```
### Future
```
package com.example.demo.controller;

import java.util.Random;
import java.util.concurrent.*;

public class FutureTest {
    public static void main(String[] args) throws ExecutionException, InterruptedException, TimeoutException {
        ExecutorService exec = Executors.newFixedThreadPool(2);
        FutureTask<String> future1 = new FutureTask<String>(() -> {
            Thread.sleep(new Random().nextInt(5000));
            return "future1 success";
        });

        FutureTask<String> future2 = new FutureTask<>(() -> {
            Thread.sleep(new Random().nextInt(10000));
            return "future2 success";
        });

        // 两个任务交给别人去执行
        exec.execute(future1);
        exec.execute(future2);

        // 我干我自己的事
        Thread.sleep(new Random().nextInt(1000));
        System.out.println("myself success");

        /** 先问,而且不停的问 */
        while(true){
            if(future1.isDone()){
                System.out.println(future1.get());
                break;
            }
            Thread.sleep(new Random().nextInt(1000));
        }

        // 我自己的事干完了,我需要你们的返回结果了
//        System.out.println(future1.get(2, TimeUnit.SECONDS));// 这个时候可能future1的数据还没有准备好，阻塞等待
//        System.out.println(future2.get(6, TimeUnit.SECONDS));// 这个时候可能future2的数据还没有准备好，阻塞等待
        exec.shutdown();
    }
}

```
### HashSet线程不安全

线程安全版

- Collections.synchronizedSet
- CopyOnWriteArraySet

```java
Set<String> set = Collections.synchronizedSet(new HashSet<>());
Set<String> set = new CopyOnWriteArraySet();
```

hashset的本质是Hashmap，key不重复，value放入了一个固定的常量

```java
public HashSet() {
   map = new HashMap<>();
}
```