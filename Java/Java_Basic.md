# Java Basic
### HashMap原理
- HashMap数组和链表或红黑树存储数据，线程不安全。
1. 数组容量默认是16，负载因子默认是0.75。
2. Java8以后，链表中的元素超过8后，hashmap会将链表结构转换为红黑树的结构提高查询效率。
- put方法
    1. 通过哈希函数获得hashKey。
        - 哈希函数的实现：
          1. key == null，则hashKey=0
          2. key != null，则key.hashCode ^ (key.hashCode >>> 16) 逻辑右移，将高16位移到低16位
        - 使用异或的原因：异或能更好的保留高16位和低16位的特征，或|会向1靠近，与&会向0靠近。
    2. 元素存取位置
        - hashKey & (n - 1) ：其中n是2的幂次，位运算比取余速度更快。
- resize方法
    - 二倍扩容
### ConcurrentHashMap
- 线程安全：Hashtable和ConcurrentHashMap
- Hashtable并发性不如ConcurrentHashMap，Hashtable全部方法都使用了Synchronized锁来保证并发冲突。
- CHM原理：ConcurrentHashMap分段锁实现并发操作，锁的粒度更小。
- ConcurrentHashMap由多个segment组成，segment的数量也是锁的并发度，每个segment均继承自Reentrantlock并单独加锁，所以每次进行加锁操作时锁住的都是一个segment，这样只要保证每个segment都是线程安全的，也就实现了全局的线程安全。
- 哈希函数为什么要加个与操作呢？
  - `(h ^ (h >>> 16)) & HASH_BITS`
- 使用CAS的方式获取每个table elements
### 异常

- throwable
    - exception
        - checked exception
        - runtime exception
    - error

- checked exception指在编译阶段Java编译器会检查CheckedException异常，并强制程序捕获和处理此类异常。
- Runtime Exception及其子类都是unchecked exception。
### unchecked exception
- ArithmeticException 算术异常
- ClassCastException 类转换异常
- IllegalArgumentException 非法参数异常
- IndexOutOfBoundsException 索引越界异常
- NullPointerException 空指针异常
### 抽象类
[参考视频](https://www.bilibili.com/video/BV1sZ4y1H7gV?p=185)
- 抽象类是对事物的抽象，而接口是对行为的抽象。
1. 抽象类中可以有构造方法，但只供子类调用。
2. 抽象类中不一定有抽象方法。
3. 抽象类中非抽象方法可以有函数体。
4. 抽象方法可以被public, protected和private修饰。

### 接口
[参考视频](https://www.bilibili.com/video/BV1T7411m7Ta?p=182)
1. 成员变量，格式：[public] [static] [final] 数据类型 常量名称 = 初始值；
    - 常量必须进行赋值，一旦赋值不能被修改。
    - 常量名称完全大写，用下划线分割。
2. 抽象方法，格式：[public] [abstract] 返回值类型 方法名称(参数列表)；
3. 默认方法(java 8)，格式：[public] default 返回值类型 方法名称(参数列表){方法体}
    - 也可以被覆盖重写（提供这种访问方式的目的是什么呢？）
4. 静态方法(java 8)，格式: [public] static 返回值类型 方法名称(参数列表){方法体}
    - 应该通过接口名称进行调用，不能通过实现类对象调用静态方法
    - `MyInterfaceStatic.methodStatic();`
      ```java
      public interface MyInterfaceStatic {
          static void methodStatic(){
              System.out.println("这是接口的静态方法");
          }
      }
      ```
5. 私有方法(java 9), 格式:

    - 普通私有方法：private 返回值类型 方法名称(参数列表){方法体}
    - 静态私有方法：private static 返回值类型 方法名称(参数列表){方法体}
    - private方法只有接口自己才能调用，不能被实现类或别人使用。

### 子父类加载顺序
- 父类静态属性和静态初始化块，按在代码中出现的顺序依次执行。
- 子类静态属性和静态初始化块，按在代码中出现的顺序依次执行。
- 父类的实例属性和实例初始化块，按在代码中出现的顺序依次执行。执行父类的构造方法。
- 子类实例成员和实例初始化块，按在代码中出现的顺序依次执行。执行子类构造方法。
- 特殊情况：静态，final且值确定是常量，是编译时确定，不会加载类。
```java
public final static int  staticData = 4 + new Random().nextInt(10) ; //需要加载类
public final static int  staticData = 4 ; //不需要加载类，直接去常量池取
```

### Java的基本类型

- java有8种基本类型
- Integer 4字节
- Long 8字节
- Double 8字节
- Boolean 1字节
- Short 2字节
- Float 4字节
- Char 2字节
- Byte 1字节  

### 反射机制
- 反射机制：在运行时动态地创建类的对象，获取一个类的所有成员变量和方法。
反射的作用：
- 得到一个对象所属的类
- 获取一个类的所有成员变量和方法
- 在运行时动态地创建类的对象
- 在运行时动态地调用对象的方法
获取class对象的3种方式：
- 某个对象的getclass
- 类的class属性
- Class.forName("fullpathname")

### 多态
- 父类引用指向子类对象
- 成员变量：编译看等号左边，运行也看等号左边
- 成员方法：编译看左边，运行看右边。
- 父子都有的同名成员，多态时，调用的时父类的成员变量


### String 
- 不可变
- 线程安全
### StringBuilder
- 非线程安全
- 效率高
### StringBuffer
- 加了synchronized同步锁，所以是线程安全的。
### String、StringBuilder和StringBuffer的区别

**可变性**
简单的来说：`String`类中使用`final`关键字字符数组保存字符串，`private final char value[]`，所以`String`对象是不可变的。而`StringBuilder`与`StringBuffer`都继承自`AbstractStringBuilder`类，在`AbstractStringBuilder`中也是使用字符数组保存字串`char[]value`但是没有用`final`关键字修饰，所以这两种对象都是可变的。
**线程安全性**
`String`中的对象是不可变的，也就可以理解为常量，线程安全。
`AbstractStringBuilder`是`StringBuilder`与`StringBuffer`的公共父类，定义了一些字符串的基本操作，如`expandCapacity、append、insert、indexOf`等公共方法。`StringBuffer`对方法加了同步锁或者对调用的方法加了同步锁，所以是线程安全的`StringBuilder`并没有对方法进行加同步锁，所以是非线程安全的。
**性能**
每次对`String`类型进行改变的时候，都会生成一个新的`String`对象，然后将指针指向新的`String`对象。`StringBuffer`每次都会对`StringBuffer`对象本身进行操作，而不是生成新的对象并改变对象引用。相同情况下使用`StringBuilder`相比使用`StringBuffer`仅能获得 10%~15% 左右的性能提升，但却要冒多线程不安全的风险。
**使用总结**

- 操作少量的数据 = String
- 单线程操作字符串缓冲区下操作大量数据 = StringBuilder
- 多线程操作字符串缓冲区下操作大量数据 = StringBuffer
- 安全性
    1. String和StringBuffer线程安全。
    2. StringBuilder非线程安全。

### final、finally和finalize的区别

final关键字主要用在三个地方：变量、方法、类。

- 对于一个 final 变量，如果是基本数据类型的变量，则其数值一旦在初始化之后便不能更改；如果是引用类型的变量，则在对其初始化之后便不能再让其指向另一个对象。
- 当用 final 修饰一个类时，表明这个类不能被继承。final 类中的所有成员方法都会被隐式地指定为 final 方法
- 使用 final 方法的原因有两个。第一个原因是把方法锁定，以防任何继承类修改它的含义；第二个原因是效率。在早期的 Java 实现版本中，会将final 方法转为内嵌调用。但是如果方法过于庞大，可能看不到内嵌调用带来的任何性能提升（现在的 Java 版本已经不需要使用 final 方法进行这些优化了）。类中所有的 private 方法都隐式地指定为 final

- finally

异常处理时,无论是否抛出异常都会执行的语句块,尽量在finally中避免return语句。

- finalize

是object类中的方法,在该对象被垃圾回收时调用,一个对象的finalize方法只会被调用一次,被调用不意味着gc会立即回收该对象。



### Java和C++的区别

共同点：都是面向对象的语言，支持封装，继承和多态。
不同点：
    - 内存上：C++提供指针直接访问内存，没有垃圾回收机制。
    - 继承上：Java是单继承，C++是多继承，但是Java可以实现多个接口来达到多继承。- 

### Java中的值传递和引用传递

- 值传递被传递了对象的副本，即使副本被改变，也不会影响源对象。
- 引用传递传递的是对象的引用，对引用对象的改变会反应到所有对象上。

### 集合

- Map接口和Collection 接口是所有集合框架的父接口。

- Collection接口的子接口包括List和Set接口


### 集合扩容机制

- ArrayList初始容量是10，默认扩容原容量的1.5倍。
- Vector是线程安全的List子类，初始容量是10，默认扩容是原容量的2倍。
- Stack是Vector的子类，增加了栈的特性。Vector和Stack都已经过时了，线程安全且高效的，使用Collections.synchronizedList(new ArrayList<>())。
- Map和Set默认容量都是16，加载因子0.75，默认扩容是原来容量的2倍大小。

### static

- 修饰成员变量和方式时，static是对象共享的，可以直接使用类操作静态成员变量和方法。

- static优先于非静态加载入内存。

### equals和hashCode的区别

- 都是用来判断两个对象是否相同，两者都是Object中的方法，不同的类可以重写该方法。

- 按照Java的规范，equals相同的两个对象，hashCode必须相同。hashCode相同的对象，equals不一定相同。同时hashCode的返回结果应该具有稳定性。

- 一般重写equals方法同时也需要重写hashCode方法。

### 包裹类型

- 8种基本类型都有相应的包裹类型，包裹类型是一个类，所以创建对象的值放在堆中，而基本类型的值是直接放在栈中，因此基本类型的效率更高。

- 基本类型和基础类型可以互相转换，集合中只能使用包裹类型。

### 抽象类和接口★★

-   抽象类和接口都不能被实例化
-   抽象类可以没有抽象方法，但是有抽象方法的类必须是抽象类。接口中的方法，必须是抽象方法。
-   抽象类中可以有普通的成员变量；接口中的变量必须是static final类型的，必须被初始化，接口中只有常量，没有变量。
-   抽象类只能单继承，接口可以实现多个父接口。
-   Java8中接口有default方法，即方法可以被实现。

### BIO和NIO和AIO的区别

进程触发IO操作时，自己干就是同步，别人干就是异步。可以不亲自去处理，把它委托给OS处理，自己去做别的事情，IO结束后会得到通知。

进程触发IO操作时，要等着不能做其他事情就是阻塞，不用等可以做其他事就是非阻塞。没办法读写就去做其他事情。

IO模型分为：同步阻塞，同步非阻塞，异步阻塞，异步非阻塞

- BIO同步阻塞，一个连接一个线程。可以引入线程池，减少线程创建和销毁的开销。
- NIO同步非阻塞，一个请求一个线程，单线程轮询。客户端发送的连接请求都会注册到多路复用器上，多路复用器轮询到有IO请求时才启动一个线程进行处理。
- AIO异步非阻塞,一个有效请求一个线程，客户端的IO请求都是由OS先完成了再通知服务器应用去启动线程进行处理。

并发量不多时用BIO,并发量比较大使用NIO和AIO或者直接使用netty。
## comparator和comparable的区别

- comparator比较器，它的名字也已经表明了它的作用：用作比较，它与原有类的逻辑没有关系，只是实现两个类的比较逻辑。
- comparable可比较的，实现了Comparable接口的类表明自身是可比较的，有了比较才能进行排序。
- 区别
    - Comparable接口可以作为实现类的默认排序法，Comparator接口则是一个类的扩展排序工具。
- 排序工具：
    - `Collections.sort`

> 个人建议，多用comparator

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Student s = new Student("yaojun",19);
        List<Student> ss = new ArrayList<>();
        /*arrayList默认长度是10，2倍扩容。*/

        ss.add(new Student("yaojun", 19));
        ss.add(new Student("yaojun", 20));
        Collections.sort(ss, (a, b)->{
            return b.age - a.age; // 从大到小
        });

        for (Student student : ss) {
            System.out.println(student.name + " " + student.age);
        }
    }
}

class Student{
    String name;
    int age;
    Student(String name, int age){
        this.name = name;
        this.age = age;
    }
}

```
## 缓存数据一致性

- 缓存
- 持久化

## 异常分类

- Throwable
    - Error
    - Exception
        - checked exception
        - unchecked exception=runtime exception
            - 空指针异常
            - 数组越界
            - 算术异常
            - 非法参数

## 常用的设计模式

- 模板方法
- 工厂模式
- 单例模式
- 代理模式

## 动态代理

- 动态的在内存中创建代理对象，依赖于反射机制和newProxyInstance

## 事务传播行为

- A事务调用B事务后，B事务的执行方式
- required 没有才创建新的事务
- required_new 每次创建新的事务

## 事务失效

- 不带事务的方法掉用带事务的方法，不会回滚。
- 带事务的方法A，调用带事务的方法B，B抛出异常，事务失效不会回滚。
- 本质是动态代理

## HashMap

- 链表数量达到8个，数组长度小于64时会进行扩容。
- 桶的数量超过负载因子*数组容量时会进行扩容。
- 扩容原理
    - 两个索引都为5，扩容后可能变成一个仍然为5，一个为5+16
        - 新的索引高位是0，保留在原位置5
        - 新的索引高位是1，迁移到新位置21【原索引+旧容量】
    - 扩容是不需要重新rehash，只需要看索引的高位是0还是1。
    - **省去了重新计算哈希值的时间，由于新增的1bit是0还是1可以认为是随机的，在resize的过程中保证了rehash之后每个桶的上的节点数一定小于等于原来桶上的节点数，保证了rehash之后不会出现更严重的哈希冲突，均匀的把之前冲突的节点分散到新的桶中。**

## ConcurrentHashMap

[链接](https://blog.csdn.net/qq_40826814/article/details/115328565)

- jdk1.7采用了分段锁segment，并发度就是锁的数量。每个segment有n个hashEntry。segment继承reentrantlock，是可重入锁。
- jdk1.8采用了hashmap的结构，数组+链表+红黑树，采用CAS和synchronized替代segemnt。**实现了更加细粒度的锁，将锁的级别控制在了哈希桶数组元素级别，只用锁住链表头节点，或者红黑树数根。**
- 为什么要用synchronized替换掉reentrantlock锁呢？
    - jdk1.6对synchronized做了很多优化，通过锁升级机制，逐步转换为重量级锁。
    - 减少内存开销。使用reentrantlock每个节点都需要继承AQS来获得同步支持，**实际只有链表头节点需要同步支持**，存在内存浪费。
    - 定位到node后，判断f头节点。
        - 为Null，通过CAS尝试添加。
        - 如果f.hash=moved=-1说明在扩容，参与一起库容。
        - 如果是synchronized锁住f节点，遍历插入。

## ThreadLocal

[黑马链接](https://www.bilibili.com/video/BV1N741127FH?p=11)
[freecoder链接](https://www.bilibili.com/video/BV1SJ41157oF?from=search&seid=2503862003293010990)

- 每个thread中有个threadlocals，这个threadlocals是threadlocalmap，key是threadlocal，value是变量副本值。
- 线程隔离：将变量绑定到当前线程中。
- threadlocal使用空间换时间，每个线程都有一份变量的副本。
- ThreadLocalMap中的key使用了弱引用，也会出现内存泄露。value内存不会回收。
- 弱引用
    - 只要没有remove这个entry都会有内存泄露的问题。
    - set和getEntry方法中，会对key为null也就是threadlocal为null进行判断，如果key为null，则将value也置为null。就算忘记了remove，弱引用比强引用多一层保障，对应的value在下一次调用set，get，remove任意方法会被清楚，从而避免内存泄露。
- 内存泄露的真正原因
    - 没有手动删除entry
    - Thread仍然在运行
- 哈希冲突
    - 环形数组，线性探测法，哈希数组而不是链表和红黑树。
### 线程池原理

- 线程复用，方便管理，提高响应速度。
- 尽量使用ThreadPoolExecutor创建
- 第一阶段：工作线程+阻塞队列
- 第二阶段：最大线程+阻塞队列+拒绝策略

## lambda表达式

- 针对函数式接口
- ( ) -> { }

## 线程六种状态

- 阻塞 等待 运行
- new
- waiting
- timed_waiting
- runnable
- blocked
- terminated

## sleep()和wait()的区别

- sleep不会释放锁，“抱着锁睡觉”，**wait会释放锁。**
- sleep来自Thread类，wait来自Object类。
- sleep可以在任何地方使用，**wait只能在同步代码块中使用。**
- **sleep必须捕获异常**，wait不用捕获异常。
- wait是进入线程池等待，让出系统资源，其他线程可以占用CPU。每个对象都有一个锁来控制同步访问。

## synchronized和lock的区别

- synchronized是关键字，lock是接口。
- synchronized可以锁对象和类，一般处理小块代码，lock通常用来锁大块代码。
- synchronized是阻塞等待获取锁，lock可以调用trylock超时等待获取锁。
- synchronized自动释放锁，lock需要手动释放。
- synchronized是非公平锁，可重锁，不可中断。lock可以设置公平与非公平，也可重入，可以获取锁的状态。

## volatile

- 声明volatile的变量，编译器不再进行优化，它要求系统每次都是**直接从对应的内存中读取数据**，而不是用cache中的值。
- 保证操作的可见性和有序性

## fail-fast

- 当多个线程对同一个集合的内容进行操作时，就可能会产生fail-fast事件。
- 多线程并发修改时，**抛出异常ConcurrentModificationException**。

## fail-safe

- 任何对集合结构的修改都会在一个复制的集合上进行修改，因此不会抛出并发修改异常。
- fail-safe存在的两个问题。
    - 需要复制集合，产生大量的无效对象，开销大。
    - 无法保证读取的数据是目前原始结构中的最新数据。

## Vector和ArrayList

- Vector是线程安全的List，它的public方法都加了Sychronized关键字。
- Stack是Vector的子类，也是线程安全的。
- Stack和Vector都是过时的容器，线程安全的容器可以使用SynchronizedList或者ConcurrentHashMap。

## AQS

- **抽象队列同步器**AbstractQueueSynchronizer，只是一个接口。
- AQS是一个同步器+阻塞锁的基本架构，用于控制加锁和释放锁，并在内部维护一个FIFO的线程等待队列。
- AQS内部使用链表的结构
- AQS维护了**一个共享资源状态**volatile int state和**一个FIFO线程等待队列**（使用双向链表实现的，当多线程争用资源被阻塞时就会进入此队列）
    - 一个共享资源状态state
    - 一个双向链表实现的线程等待队列
- state的访问方式有三种原子操作
    - getState()
    - setState()
    - compareAndSetState()
- AQS定义了两种共享资源的方式
    - 独占式
    - 共享式
- 自定义同步器只需要实现
    - tryAcquire()
    - tryRelease()
    - tryAcquireShared()
    - tryReleaseShared()

## CAS

- compareAndSet()依赖于unsafe类的compareAndSwapInt()
- 每次从内存中读取数据**current**然后将此数据加一**next**，然后调用CAS判断**current和next是否成功**，一直循环重试，直到成功。
- ABA问题
    - 部分乐观锁是通过**版本号**version来解决ABA问题的。
    - 预期的版本号和数据的版本号一致的时候，才可以进行修改操作。
    - 版本号只会增加不会减少。

## 进程调度算法

- 先来先服务
- 短作业优先
- 优先级调度算法【抢占式和非抢占式】
- 时间片轮转算法
- 多级反馈调度算法

## HashMap

- resize过程
- 2倍扩容机制

## ConcurrentHashMap
- CAS
- 分段锁
- synchronized

## 线程上下文切换

- 指线程切换时CPU寄存器和程序计数器所保存的当前线程的信息。
- 上下文切换的信息会被保存在进程控制块PCB中，直到被再次使用。
- 切换流程
    - 挂起一个进程，将这个进程在CPU的状态存储于内存的PCB中。
    - 在PCB中检索下一个进程的上下文将其在CPU的寄存器中恢复。
    - 跳转到程序计数器所指向的位置，即被中断时的代码行，并恢复该进程。

## 引起上下文切换的原因

- CPU正常调度下一个任务
- 正在执行的任务遇到IO阻塞操作，调度器挂起此任务，继续调度下一个任务。
- 多任务并发抢占锁资源，当前任务没有抢到，被调度器挂起。
- 硬件中断。
- 线程执行sleep让出CPU。

## Synchronized

- 偏向锁
- 轻量级锁
- 重量级锁

## 线程池原理

- 线程复用
- 高并发
- 主要流程
    - 核心线程，阻塞队列，拒绝
- 七个核心参数
    - 核心线程数
    - 总线程数
    - 线程保持活跃的时间
    - 时间单位
    - 阻塞队列
    - 线程工厂
    - 拒绝策略
- 四个拒接策略
    - abortPolicy
    - callRunnerPolicy
    - discardPolicy
    - discardOldestPolicy

## 待解决的问题

- HashMap中为什么不直接用红黑树，而要等链表长度达到了8才用？
    - 红黑树需要左旋转和右旋，而单链表不需要。
    - 主要是从查询成本上做的一个权衡。
- 如何解决幻读，是用的哪种锁？
    - InnoDB是使用Next-Key Lock来解决幻读问题的。
- 行锁的类型
    - Record Lock：行锁，锁住记录本身。
    - Gap Lock：间隙锁，锁住某个范围。
    - Next-Key Lock：既锁范围，又锁记录。
- MVCC底层实现原理
    - 快照读
- 如何实现可重复读
    - MVCC
- MVCC底层实现 undo调用链？
- Java中HashTable、HashMap、ConcurrentHashMap的区别？
    - HashTable和ConcurrentHashMap是线程安全的。HashMap是非线程安全的。
- ConcurrentHashMap是怎么实现线程安全的
- hashMap插入过程
- 跳表原理
    - 时间复杂度：O(logn)
- 分布式锁setnx
    - 如何实现
- redis持久化
    - AOF
    - RDB
- 连接
    - left join
    - right join
    - full join
- binlog


### 关键字
- instanceOf 判断一个对象是否是某个类的对象
- final 成员变量不可变，成员方法不可重写，类不可继承
- finalize 主动触发垃圾回收
- finally 不管抛出异常与否都需要执行
- clone 深拷贝

## HashMap

- 线程不安全
- 数组+红黑树+链表
- **扩容原理：**每个数组下面接一个链表，当链表的长度大于8时，增加数组的大小，**当数组的大小超过64时**，将链表变成红黑树存储。
- 线程不安全，**key和value都可以为null。**链表是为了解决哈希冲突，可能存在两个对象调用的hashcode结果一致。
- **put方法：**key与其高16位异或，尽可能减少碰撞。如果key为空则直接返回0。`(n - 1) & hash `计算出数组的下标，位运算比取余更快。

## 集合

- Collection
    - List
        - ArrayList
        - Vector[线程安全]
            - Stack[线程安全]
        - LinkedList
    - Set
        - HashSet
        - SortedSet
            - TreeSet
    - Queue
        - PriorityQueue
- Map
    - HashMap
        - LinkedHashMap
    - SortedMap
        - TreeMap
    - HashTable[线程安全]

int long short 2
float double
char 2
boolean 1
byte 1

## 包裹类
- 包裹类型是一个类，创建的对象放在堆中。
- 基本类型的值是直接放在栈中，效率更高。
- 集合只能使用包裹类。
### 思考：为什么要有primitive类型？
- int相对于integer的优势是什么？
## 反射
- 动态地获取类的属性和方法的机制。
- 三种方式获取到类对象
    - instance.getClass()
    - Class.class
    - Class.forName("")
    
## 异常

- **Throwable**
    - **Exception**
        - CheckedException 检查型异常【编译器检查】
        - RuntimeException 运行时异常【运行时检查】
    - **Error**

Checked Exception指在编译阶段Java编译器会检查CheckedException异常，并强制程序捕获和处理此类异常。
**RuntimeException**及其子类都是unchecked exception。
不可查异常

- ArithmeticException 算术异常
- ClassCastException类转换异常
- IllegalArgumentException非法参数异常
- **IndexOutOfBoundsException**索引越界异常
- **NullPointerException**空指针异常

## 抽象类

- 可以有构造方法。
- **不一定有抽象方法。**
- 抽象类中非抽象方法可以有函数体。
- 抽象方法可以被public, protected和private修饰。

## 接口

- **常量必须进行赋值，**一旦赋值不能被修改 。格式：**[public] [static] [final]** 数据类型 常量名称 = 初始值；
- 抽象方法，格式：**[public] [abstract] **返回值类型 方法名称(参数列表)；
- 静态方法(java 8)，格式: [public] static 返回值类型 方法名称(参数列表)**{方法体}**应该通过接口名称进行调用

## equals

- equals默认的方式是判断两个引用是否指向内存中的同一个对象。
- **如果你重写了equls方法，一定要记得重写hashcode方法。**
- **equals和hashcode的区别**：重写equals必须重写hashcode。equals相等则hashcode必须相等。hashcode是内存地址的值，在hashmap中为了快速查找，给多个对象设定了相同的hashcode，即放在同一个数组下标中。

## Maven依赖冲突

- 使用exclusions排除冲突

### 多态

- 父类引用指向子类对象，根据运行时的语义产生不同的行为。

### 序列化

- 序列化就是把对象写入到磁盘文件中。
- **被static修饰的成员变量不能被序列化**。
- **transient修饰的成员变量不能被序列化。**

## JVM参数

- -Xms程序启动时初始内存大小
- -Xmx最大可用内存
- -Xmn年轻代大小
- -Xss每个线程的栈大小

## 命令

- jstack 检查是否有死锁
- jstat监控Java进程
- jmap定位内存问题，比如进程频繁GC

## 正则

- * 可不出现
- + 至少一次

## JVM考点

- Java内存结构
- 垃圾收集算法【标记清除，标记整理，复制】
- 垃圾收集器【CMS，G1，ZGC】
- 年轻代和老年代的比例和转移流程
- GC Roots
- 四种引用
- 双亲委派机制
- 栈溢出和堆溢出

### CMS垃圾回收器

[参考视频](https://www.bilibili.com/video/BV1dt411u7wi)
参考书籍：《深入理解Java虚拟机》周志明
优点：并发收集，低停顿。
缺点：**内存碎片，无法处理浮动垃圾，导致并发失败，最后STW。**
concurrent mark sweep 是一种以获取最短停顿时间为目标的收集器
Java垃圾回收是由一个守护线程完成的。

- serial和serial old  串行清除
- Parallel Scavenge和Parallel Old  并行清除
- ParNew和CMS 并发清除

CMS四个步骤

- 初始标记STW
- 并发标记【并发，耗时较长】
- 重新标记STW【停顿稍长】
- 并发清除【并发，耗时较长】

初始标记：标记gc roots直接关联到的对象，速度很快。
并发标记：从gc roots直接关联对象开始遍历整个对象图的过程。
重新标记：修正并发标记期间，因用户程序继续运作而导致标记产生变动的那一部分对象的标记。
并发清除：清理删除掉标记阶段判断的已经死亡的对象。

### G1收集器

- 标记整理算法【没有内存碎片】
- 可以指定最大停顿时间
- 划分成region的堆内存布局
- 按收益动态确定回收集
- 在最终标记阶段采用SATB原始快照算法
- H区专门存储大对象

G1运作过程的四个步骤

- 初始标记STW
- 并发标记
- 最终标记STW
- 筛选回收STW

mixed gc
优先处理回收价值收益最大的那些region
G1开创了基于region的堆内存布局，把堆划分为多个大小相等的独立区域region，每个region都可以根据需要，扮演新生代的eden，servivor和老年代空间。
region中有一类特殊的区域H专门用来存储大对象。
超过region容量一半的对象就是大对象。
将region作为单次回收的最小单元
哪块内存中存放的垃圾数量最多，回收收益最大，就回收那一块。
zgc染色指针/内存多重映射/读屏障

### 类加载器

- 启动类加载器Bootstrap ClassLoader
- 扩展类加载器Extension ClassLoader
- 应用程序类加载器Application ClassLoader
- 自定义加载器

### JVM

组成部分：类加载子系统， 运行时数据区，垃圾回收器，执行引擎，本地方法接口，本地方法库。
jdk1.7开始，字符串常量池已经被移到堆区。
堆：通过new操作创建出来的对象实例都存储在堆区。

### 哪些对象可以作为GCroot

- 在虚拟机栈中引用对象
- 在方法区中常量引用的对象
- 在本地方法栈中JNI引用的对象
- Java虚拟机内部的引用
- 所有被同步锁（synchronized关键字）持有的对象

### Java内存结构
1. 程序计数器
2. 虚拟机栈
3. 本地方法栈
4. 堆
5. 方法区
- 线程私有：程序计数器，虚拟机栈，本地方法栈。
- 线程共享：堆，方法区。

> 程序计数器可以看作是当前线程锁执行的字节码的行号提示器。

### 虚拟机栈

栈：线程运行时需要的内存空间，由多个栈帧组成。
栈帧：每个方法运行时需要的内存。(局部变量，返回地址)
活动栈帧：每个线程只能由一个活动栈帧，对应着当前正在执行的那个方法。(在栈顶)
设置栈大小：-Xss
linux/macOS下栈内存默认大小为1M
windows下取决于虚拟内存大小
栈内存溢出：栈帧过多(递归调用过深)，栈帧过大。
查看占用CPU过高的线程：
ps H -eo pid,tid,%cpu | grep 32655

### 堆

通过new创建的对象都会使用堆内存
特点：线程共享，堆中对象都需要考虑线程安全的问题。有垃圾回收机制。
堆内存设置：-Xmx8m 默认时4G

### 方法区

jdk1.8中stringTable放在堆中，其他放在本地内存。

### 垃圾回收

如何判断对象可以回收：

1. 引用计数(循环引用问题)
1. 可达性分析

Java虚拟机中的垃圾回收器采用可达性分析来探索所有存活的对象。
扫描堆中的对象，看是否能够沿着gc root对象为起点的引用链找到该对象，找不到，表示不可回收。

### 垃圾回收算法

- 标记清除Mark-Sweep
- 标记整理 Mark-Compact
- 复制copying

### 分代

年轻代：Eden from_servivor to_servivor 8:1:1

### 垃圾回收器

1. serial 串行GC
1. PS 并行GC **jdk1.8默认**
1. CMS 并行执行垃圾回收同时不阻塞应用程序(STW=200ms)
1. G1(STW=10ms)  **jdk1.9默认**
1. ZGC(STW=1ms)

### Java内存模型

Java memory model = JMM
其实Java线程内存模型，是基于cpu缓存模型建立起来的。
线程有独占的工作内存，是共享内存的副本拷贝。
volatile保证多个线程之间变量的可见性。
数据原子操作。read/write/load/store/assign/use/lock/unlock

### 双亲委派机制

当某个类加载器需要加载某个`.class`文件时，它首先把这个任务委托给他的上级类加载器，递归这个操作，如果上级的类加载器没有加载，自己才会去加载这个类。
类加载器的类别：

- 启动类加载器BootstrapClassLoader(C++编写) rt.jar
- 扩展类加载器ExtClassLoader jre/lib/ext
- 应用类加载器AppClassLoader classpath
- 自定义加载器CustomClassLoader

如果都没加载成功，抛出异常**Class Not Found**
作用：

- 防止重复加载同一个`.class`。通过委托去向上面问一问，加载过了，就不用再加载一遍。保证数据安全。
- 保证核心`.class`不能被篡改。通过委托方式，不会去篡改核心`.clas`，即使篡改也不会去加载，即使加载也不会是同一个`.class`对象了。不同的加载器加载同一个`.class`也不是同一个`Class`对象。这样保证了`Class`执行安全。


## 最困难最有挑战的事情

- 实现从0到1搭建微服务工程

## Cookie和Session的区别

- 都是用来保存用户的信息。
- Cookie是存于浏览器端，Session是存于服务端的文件中。
- Session的运行依赖于Session id，Session id是存在cookie中的。如果浏览器禁用了cookie，同时session也会失效。
- 安全性：session更安全，session在分布式场景下失效，基于JWT的token

## 传输层和网络层主要功能

- 传输层提供进程到进程的服务 封装了源端口和目的目的端口
- 网络层提供主机到主机的服务 封装了源IP和目的IP

## IP是怎么寻址的

- 二层交换机经过ARP广播自己的mac地址，具有该地址的，具有对应IP的主机，就会响应这个请求。然后将目标mac和mac地址表对比，发现对应的端口，
- ARP协议是属于网络层的吗
    - 是的
- 了解syn泛洪攻击吗
    - syn队列和accpet队列
    - 主要是通过大量无效的连接，把syn队列快速占满。可以通过syn+cookie的形式去解决。
- 写socket连接时，哪个参数是控制连接队列大小的？

- DNS是哪一层协议
    - 应用层
- 说一下DNS的解析过程
    - 迭代式
    - 递归式
- 操作系统进程的内核态、用户态有什么不一样
    - 内核态执行特权指令，通常是系统调用，内存分配，进程管理，IO管理
    - 用户态是用户可以直接操作的内容
- 为什么要有内核态
    - 提高系统的执行效率
    - 某些程序可靠性和安全性不高，如果这些程序执行了 cpu 的某些指令，会导致系统崩溃，如：设置时钟、清理内存、调整网络等
    - 保证系统的稳定性和安全性
- TCP四次挥手
- TCP挥手为什么需要四次
- 说一下对称加密和非对称加密
- 介绍一下HTTPS原理

## 用户态如何切换到内核态？
- 用户态程序陷入到内核态有 3 种方法：
1. 系统调用：使用的是操作系统为用户开发的一个中断
1. 外围设备中断：网卡、打印机等
1. 异常：应用程序执行过程中的除零，越界

### http1和http2的区别

- 头部压缩
- 二进制分帧
- 服务端推送
- 多路复用

## TCP的特点

- 面向连接
- 字节流
- 可靠
- 传输层协议

## 拥塞控制

- 慢启动
- 快开始
- 拥塞避免
- 快恢复

## HTTPS

- 简单来说就是http的安全版。提供了SSL层安全加密组件。
- 端口443
- 证书
- 非对称加密算法和对称加密算法

### 1、状态码

301 move permanently
302 found POST方法的重定向在未询问用户的情况下就变成GET
303 see other  POST重定向为GET
307 temporary redirect  当客户端的POST请求收到服务端307状态码响应时，需要跟用户询问是否应该在新URI上发起POST方法，也就是说，307是不会把POST转为GET的。

### 2、TCP拥塞控制

- 慢开始：初始窗口，每个往返事件RTT增加一倍的窗口，呈现指数增长。
- 拥塞避免：当窗口大小达到阈值以后，每个RTT增加一个窗口的大小。
- 超时后，进行阈值变为当前窗口的一半，窗口大小从1进行慢启动
- 重复确认：阈值和窗口同时变为当前窗口的一半，进行拥塞避免，称为快恢复。

### 3、TCP状态转换

- close_wait半关闭的被动关闭方
- time_wait被动关闭方，等待2MSL的时间，保证ACK可以顺利送达。使用端口复用可以消除time_wait，修改TCP的参数可以增大或减少这个时间长度。

### 4、http2.0和http3.0

http2.0 spdy

- **首部压缩 hpack  哈弗曼编码**
- 多路复用
- **服务器推送**

http3.0 quic+udp

- **0 RTT**
- 前向纠错
- **没有队头阻塞的多路复用**

## 预演

- TCP和UDP的区别说一下
    - TCP是面向连接的，可靠的，字节流。
- TCP为什么不能两次握手
- hashmap和concurrenthashmap
- 垃圾回收算法
    - 复制：对半分 **占用双倍内存空间** 不会有内存碎片
    - 标记整理：将活跃对象进行整理，是空间更紧实 **速度慢 **不会有内存碎片
    - 标记清除：将活跃对象进行标记 清除不活跃的对象 **速度快 会造成内部碎片**
- IOC和AOP
    - IOC是控制反转，意思是把原来由程序员自己创建对象的权利，交给了IOC容器去管理。
    - AOP是面向切面编程，意识是在可以在某个功能上便捷地增强和扩展功能。
- String和StringBuffer和StringBuilder的区别
- Synchronized
    - 互斥锁
    - 锁对象、锁类
    - 记录锁的对象和重入的次数
- Lock
    - 非租塞获取锁
    - 手动释放
    - 可以设置公平和非公平
- volatile
    - 保证可见性
    - 禁止指令重排
    - 不保证原子性
- 悲观锁
    - Lock和Synchronized
- 乐观锁
    - CAS比较和交换
        - ABA问题可以用版本号机制解决
- 线程池
    - 七大核心参数
        - 核心线程数
        - 最大线程数
        - 连接的活跃时间
        - 时间单位
        - 阻塞队列
        - 线程工厂
        - 拒绝策略
    - 四大拒绝策略
        - abort policy 默认 不处理 抛出异常
        - callerrunspolicy 调用者执行
        - discard policy 直接丢弃 不抛异常
        - discard old policy 尝试与最早的任务竞争，竞争失败就丢弃，不抛出异常
- CMS标记流程
    - 初始标记STW
    - 并发标记
    - 重新标记STW
    - 并发清理

## 面试高频

- **ES项目遇到的问题**
    - 多音字，王重阳，新增一个字段，记录所有拼音的多音字笛卡尔积
    - 深度分页
        - scroll
        - search after
    - 排序问题
        - sort排序时尽量增加id否则，具有相同值的key会随机返回，导致两次查询的结果不一致。
    - order by与limit的问题
        - 同样的也是这个问题，增加一个字段排序。
- **Mysql如何做的优化**
    - explain执行计划
        - type
        - len
        - extra
        - id
    - show profile慢日志
        - CPU瓶颈
        - IO瓶颈
- **HashMap**
    - 链表采用头插法还是尾插法
    - 为什么要2倍扩容
- ConcurrentHashMap
    - CAS
- java中的锁
    - synchronized
    - lock
- Threadlocal
    - 哈希冲突如何解决的
- **JVM的垃圾回收器CMS和G1和ZGC**
    - G1
        - 棋盘状
        - 按照收益值大小进行垃圾回收
- 代理模式、观察者模式、工厂模式
    - spring事务失效
    - 事务传播属性
- 锁升级
    - 无锁
    - 偏向锁
    - 轻量级锁
    - 重量级锁
- IOC
    - 对象的创建维护交给IOC容器
- AOP
    - 动态增强功能
- 幻读
    - MVCC
    - next-key lock
- redo log/ undo log/ binary log

## HashMap的特点

1. 是一个键值对映射的集合，非线程安全。
1. 可以存取空值。
1. jdk1.7采用数组和链表，jdk1.8采用数组、链表、红黑树实现。
1. 数组的初始容量为16，负载因子为0.75，采用两倍扩容。
1. 当链表的容量超过8以后变为红黑树。
1. **使用尾插法**

## CHM的特点

- 线程安全
- jdk1.7采用的是分段锁，每次锁住一个segment，这个segment继承自ReentrantLock，锁的粒度更小，并发性就更高。
- jdk1.8以后采用CAS和synchronized。

## synchronized特点

1. 是一个关键字
1. 同步锁，可以锁对象，可以锁类。
1. 可重入锁
1. **不可中断**
1. **自动释放锁**
1. **非公平**

## Lock锁

1. 是一个接口
1. 实现类有可重入锁，读写锁。
1. 可以让等待锁的线程响应中断
1. 需要手动解锁
1. 可以自定义公平和非公平
1. **可以获取锁的状态**

## 线程的创建方式

1. 继承Thread类
1. 实现Runnable接口
1. 实现Callable接口
1. 线程池创建

## volatile关键字

1. 每个线程会将内存中的值拷贝一份到本地缓存，volatile是为了保证数据的一致性。
1. **保证可见性**
1. **禁止指令重排**
1. 不保证原子性

## Java中的锁

- 互斥锁synchronized 适合并发竞争低的情况，在竞争高的场景下synchronized很容易升级为重量级锁，而且不可消除，这意味着每次都要向CPU申请锁资源。
- 可重入锁reentrantlock提供了**阻塞的能力**，在高并发线程下，对没有获取到锁的线程进行挂起，来减少竞争提高并发能力。
- 读写锁，读时共享，写时互斥，提高并发性。
- 悲观锁，每次都认为有其他线程同步修改资源，所以获取资源时始终加锁。
- 乐观锁，每次获取资源时都认为没有其他资源与之竞争，再修改时才进行判断。ABA可以通过版本号机制解决。
- 非公平锁
- 公平锁

## 数据库中的锁

- 行锁
    - 记录锁 record lock
    - 间隙锁 gap lock
    - 间隙记录锁 next-key lock
- 表锁
    - 意向锁
    - 自增锁
- 共享锁
    - select
    - for shared
- 排它锁
    - update  insert delete
    - for update

## JVM内存分布

- 程序计数器
- 栈
- 堆
- 本地方法栈
- 方法区

## 垃圾回收算法

- 复制算法
- 标记整理
- 标记清除

## 双亲委派机制

- 启动类
- 扩展类
- 应用类
- 自定义类
    - 加载类时如果有父类加载器，总是交给父类去加载，父类无法加载时，再自己加载。
- 目的
    - 保护系统核心类的安全
    - 避免一个类重复加载。

## 类加载流程

- 加载
- 链接
- 初始化

## CMS执行流程

- 初始标记
- 并发标记
- 重新标记
- 清理标记

## G1特点

- 内存按照棋盘庄分割，每个region的大小为1M
- 可以按照收益大的优先级进行回收内存
- STW停顿时间更短

## GMP调度流程

- G：gorutine 协程
- M：machine 内核级线程
- P：processor 调度器
    - 每次M从P中取本地队列中取协程进行调度。
    - 本地队列没有了，从全局队列中取，全局没有了从其他P偷一半协程过来执行。
    - 新建的G优先放入本地队列，满了再放入全局队列。
- 为什么P层的逻辑不直接加在M上？
    - 因为M是内核层，P和G都在用户层。内核层不应该感知用户层的这些操作。

## TCP三次握手

- SYN=1 seq=x
- SYN=1 ACK=1 seq =y
- ACK=1
- time_wait：确保最后一个ack能被对方收到。
    - 可以修改TCP的等待时间参数
    - 可以设置端口复用

## 拥塞避免

- 慢启动
- 拥塞避免
- 快重传
- 快恢复

## TLS握手机制

- 三个RTT
- 第一个RTT：TCP前两次握手
- 第二个RTT：加密套件和数字证书
- 第三个RTT：非加密协商公共的秘钥

## HTTPS的特点

- TCP上增加了一层TLS
- 安全性：使用对称和非对称加密算法，确保信息在网络中是密文传输。
- 可靠性：使用数字证书，确保服务器的身份是可靠的。
- 端口：443
- 资源开销：CPU和内存处理解密时需要大量计算
- 数字证书找权威机构背书需要给钱，成本提高。

## B和B+树的区别

- 都是多路平衡树
- B+树比B树的key多存储一个key。
- B+在叶子节点上使用指针将左右的节点相连，方便范围查询。
- B+树在非叶子节点只存储索引，不存储数据。

## 隔离级别

- 读未提交
- 读提交
- 不可重复读
- 串行化

## 状态码类型

- 100：正在处理
- 200：成功
- 300：重定向
    - 301：永久重定向
    - 302：临时重定向
- 400：客户端错误
    - 499：nginx自定义的状态码，表示服务器端处理时间过长，客户端主动关闭了连接。
    - 403：forbiden 禁止访问
    - 404：not found 页面没找到
    - 408：request timeout 请求超时
- 500：服务器端错误
    - 502：bad gateway 无效的响应
    - 504：gateway time out 服务器超时

## IO多路复用

- select
    - 数组
- poll
    - 链表
- epoll
    - 红黑树，查找效率更高。
    - 内存映射，mmap
    - 边沿触发和水平触发

## Redis数据结构

- list
- string
- hash
- set
- zset 排行榜

## 缓存穿透

- 大量不存在的key
- 解决方案
    - redis中存空key
    - 布隆过滤器

## 缓存击穿

- 某个热点key失效
    - 多级缓存
    - 随机失效
    - 服务监控

## 缓存雪崩

- 大量key同时失效
    - 多级缓存
    - 服务监控
    - 限流降级
    - 永久key 定期维护

## 大key问题

- 拆分成多个小的key，使用multiget获取值，将操作压力平摊到多个redis实例中。

## Redis持久化

- RDB
- AOF

## Redis哨兵

- 自动选择master，监控master是否存活。

## ES写流程

- 路由分片
- 主从同步
- 返回

## ES搜索流程

- query
- fetch

## ES索引

- 倒排索引
- 前缀树
- 5个主分片
- 不删除，只新增。
- 索引切换
- 打分算法TF/IDF
- DSL语句

## 进程间通信方式

- 管道
- 信号量
- 信号
- 套接字
- 共享内存
- 消息队列

## 线程间通信

- 条件变量
- 互斥锁
- 信号量
- 信号
- 读写锁

## 线程共享

- 打开文件描述符表
- 进程ID和组ID
- 进程内存空间
- 信号的处理方式

## 线程独享

- 栈
- 寄存器
- 线程优先级
- 线程ID
- 信号屏蔽字

## 上下文切换

- 切换页表全局目录
- 切换内核态堆栈
- 保存寄存器中的值
- 刷新TLB
- 多级缓存间接失效

## 一面重要问题

- select的1024限制如何被epoll解决的。
    - 单进程打开的文件描述符限制是1024？epoll中难道用的不是进程吗？
    - 早期的数组限制
- **http2的多路复用是怎么实现的**
    - http1.1传输request和response是基于文本的，所有数据必须按顺序传输。
    - **HTTP/2对同一域名下所有请求都是基于流，也就是说同一域名不管访问多少文件，也只建立一条连接。**
    - 对发送的数据进行二进制编码，一个域名建立一个TCP请求，切成了stream流，**每个流由header帧和data帧组成，多个流可以同时发送。**
- **http1.1长连接的问题**
    - 串行的文件传输
    - 浏览器同域名请求的最大并发数限制
- ES查询三个数据，1,2,3查询到2时，如何找出1,3这两条数据。
    - 没看懂
- Java中的锁
    - 同步锁
    - 互斥锁
    - 悲观锁
    - 乐观锁
- 常用的IO调度算法
    - NOOP
    - CFQ
    - Deadline
    - AS
- 编程题：水域中的岛

## 零拷贝技术

- 零拷贝并不是不需要拷贝，只是减少不必要的拷贝次数与线程上下文切换次数。
- mmap
- sendfile
- splice

## 内核态和用户态的区别

- 系统调用
- 异常
- 外围设备中断

## DMA

1. DMA等待数据准备好，把磁盘数据读取到操作系统内核缓冲区。
1. 用户进程将内核缓冲区的数据拷贝到用户空间缓冲区。

## poll的优缺点

- 优点
    - 自带数组结构，可以将**监听事件集合**和**返回事件集合**分离。
    - **拓展监听上限。超出1024限制。**
- 缺点
    - 无法直接定位满足监听事件的文件描述符。

## 测试驱动开发

- 测试先于开发，由测试代码确定编写的产品代码。
- 红绿绿：**写最少的代码让测试通过。**
- red-green-refractor
- **TDD偏向于开发**
- BDD偏向于设计  行为驱动开发

#### 优缺点

- bug更少，代码覆盖率更高。
- 单元测试替代接口文档，代码可读性更强。
- 解耦合，有利于代码复用。
- 可以有效地避免过度设计。

#### 缺点

- 代码量增加，开发时间变长。

## 领域驱动模型

- 2004年Evans在他的著作中提出的概念，简称DDD，**我理解的是一套解决业务的模型。**
- 他提出了**战略设计和战术设计**。
- 战略设计方面提出了：域 子域 限界上下文
- 战术设计方面提出了：实体 值对象 聚合 工厂 资源库 领域服务 领域事件
- **分层模型：用户接口层---应用层----领域层----基础设施层**
- 设计领域模型时不能以用户作为出发点去思考问题，而应该从一个客观的角度，根据用户需求挖掘领域内相关事物的本质关联。提高可用性，可维护性。
- 类似的架构设计：**六边形架构，洋葱架构，整洁架构。**

## MVC框架

- M是Model业务层
- V是View视图层
- C是Controller控制层
- **使用MVC的目的是将业务层和视图层的代码分离，从而使同一个程序有不同的表现形式。Controller是用来确保业务层和视图层的同步。**

#### 优缺点

- 视图层和业务层分离，降低耦合。
- 复用性强。

## Spring MVC 主要流程

- dispatcherServlet查找handlerMaping找到controller
- **controller调用service层**
- 通过controller返回modelandview到dispatcherServlet上
- **viewResolver**处理视图映射
- 将model传递给view显示

## Spring Boot 常用注解

- AutoWired按照类型查找可用的bean，如果没有再按照名称查找。Spring
- Resource按照名称查找可用的bean，如果没有再按类型查找。JDK
- ComponentScan()同目录下包和子包中的bean都会被扫描进到。
- @Configuration配置类，用来创建bean。
- Repository = Service = Controller = component
- @Controller返回的是字符串或者字符串匹配的模板名称。
- @RestController返回的是对象或者json字符串。前端利用json字符串进行渲染。

## TCP拥塞控制

- 慢启动
- 拥塞避免
- 快恢复

## 输入URL后发生的事情

- 第一步，**对URL进行编码，生成http请求，有对应的请求方法和HTTP版本号。其中URL分为两个部分，域名和资源路径。**
- 第二步，**域名需要转换为IP，需要经过DNS解析，如果本地有就从本地缓存中获取，如果没有就需要使用DNS迭代式或者递归式获取对应的IP，递归式代替请求方转发到父节点进行获取，迭代式是告诉你获取到正确IP的位置，自己去请求。**
- 第三步，建立TCP连接，三次握手，如果是HTTPS，需要建立TLS的两轮握手机制。
- 第四部，HTTP将数据发送到服务端，服务端进行响应，然后客户端进行页面渲染。

## 进程线程

- 进程是资源分配的基本单位。
- 线程是CPU调度的基本的单位。

## HashMap

- 可以存储key和value为null的情况
- 线程不安全
- 数组 链表 红黑树
- 初始容量是16
- 负载因子是0.75
- 采用2倍扩容
- 尾插法插入链表。

## Spring循环依赖

- 三级缓存解决单例
- 一级缓存存储的是实例化完成且初始化完成的对象。
- 二级缓存存储的是实例化好且未初始化完成的对象。
- 三级缓存是对象工厂
- 为什么只能用set而不能用构造方法
    - 因为set可以将实例化对象和初始化对象进行分离，而构造方法做不到。

## ConcurrentHashMap

- jdk1.7采用分段锁，每次锁住一个segment，这个segment是继承的reentrantlock，锁的粒度是一个段，所以并发度比hashtable要高。
- jdk.18采用了synchronized加上CAS来实现。

## ThreadLocal

- 哈希表

## AQS

- 同步器

## MTV框架

- Django所用的框架。Model定义业务，Template定义模板，View定义视图。

## 一致性哈希

- 处理负载均衡。
- 哈希环。
- 虚拟节点处理节点较少时的分配不均。

## Shiro框架
- 四大核心功能：认证、授权、加密、会话管理。
- 三大核心组件：subject（主体，用户的信息） 、securityManager（安全管理者，过滤器）、realm（自定义的认证授权模块）
- 主要流程：用户信息封装成token提交给subject，subject提交给securityManager，securityManager提交到realm，realm调用DAO层。
- shiro是一款简单灵活的安全框架
- subject.login()

## ES框架

- 分布式、近实时的全文搜索引擎，Java编写，基于luence。
- 倒排索引：单词到文档的映射关系。
- 前缀树：公共前缀查询。
- 读写流程：
- 集群分片：
- 索引创建默认5个主分片，每个主分片有一个副本分片，共10个分片。
- 健康状态：
    - red: 至少有一个主分片运行异常。
    - yellow：主分片运行正常，至少有一个副分片运行异常。
    - green: 所有主副分片都运行正常。
- 并发控制：
    - 乐观锁，ES的索引不会修改，只会新建相同内容并将版本号加1，通过比较序列号来判断是否更新。
- 分布式搜索流程：**在搜索的时候，coordinating node 接受请求的节点将请求通过路由算法，路由算法采用hash值对主分片数取模，转发到一组包含所有数据的分片data node。**ES使用轮询机制选择可用的主/副分片，并将搜索请求转发过去。ES从这些每个分片返回的部分结果，聚集成完整的结果，返回给调用方。

## 快照读和当前读

- 快照读：读取的是记录数据的可见版本，可能是过期的数据，不用加锁。只要当前事务还未提交，读取的数据就是可见版本，不会受其他事务提交与否的影响。快照是在你开启事务后，第一次用select时生成的。
- 当前读：读取的是记录数据的最新版本，并且当前读返回的数据会加上锁，保证其他的事务不会再并发地修改这条记录。
- select 是快照读
- update insert delete 是当前读
- MVCC不能从根本上解决幻读
- 快照读是通过undo log + MVCC 来实现的

## MVCC怎么实现
- MVCC是通过保存数据在某个时间点的快照来实现的。
- read view概念

## redo log和undo log的区别
- redo log提供前滚操作。通常是物理日志，记录的是数据页的物理修改。
- undo log提供回滚操作。通常是逻辑日志，回滚行记录到某个版本。

## 布隆过滤器的实现原理

- 建立一个位数组和k个哈希函数。哈希函数将存在的元素对应的k个元素设置为1，如果查询时某个位不为1，说明这个查询肯定不在容器中，如果全为1，可能在容器中。

## 海量数据和位图

- 分治思想+归并+堆

## 平衡树和红黑树的区别
- 平衡树是严格的左右子树高度差不超过1
- 红黑树在平衡性上做了妥协，自定义了四条规则
    - 所有的根节点都是黑色
    - 红色的孩子是黑色
    - 任意节点到叶子节点的路径上黑色节点的数目相同
    - 所有叶子节点都是黑色
- 红黑树牺牲查找的效率，换取了插入和删除的效率，但是平均时间复杂度还是logn

## B树和B+树的优势

- B树是一种多路平衡树，所有叶子节点在同一层。**B树最快可以O(1)时间复杂度查询到。**
- 对于m叉B+树每个节点最多有m个key。**B+树非叶子节点只存储索引，因此单一节点存储的元素更多，使得IO查询的次数更少。**
- B+树所有的数据都放在叶子节点，所以查询性能稳定。
- **B+树叶子节点使用指针相连，方便进行范围查询。**

## 跳表的原理和实现

- logn的时间复杂度查询有序链表中的元素。
- 有1/2的概率把下一层元素移动到上一层去。
- 从顶层往下查询，最底层包含所有的元素，元素的数量呈三角形。

## 缓存雪崩

- **短时间内，大量key过期。**
- 解决方案
    - **多级缓存，设置不同的失效时间。**
    - Redis监控预警
    - **限流，降级**
    - 永久key+定期维护

## 缓存击穿

- **短时间内，某个热点key过期。**
- 解决方案
    - **多级缓存**
    - 永久key+定期维护

## 缓存穿透

- **短时间，大量redis和mysql都不存在的key。**
- 解决方案
    - **存储短时效的空值在redis中**
    - 使用布隆过滤器

## 聚集索引

- 索引和数据没有分离。

## 共享锁和排它锁

[行锁和表锁讲解](https://www.bilibili.com/video/BV1AE411a7rv?from=search&seid=6023900352334983316)

- 行锁和表锁是粒度概念，共享锁和排它锁是具体实现。
- 共享锁：**读锁**  能写不能写
- 排它锁：**写锁  **不能读也不能写
- **表锁**
    - 意向锁
    - 自增锁
- **行锁**
    - record lock
    - gap lock
    - next-key lock
- **无锁**

```sql
select * from user; 
```

- **共享锁**

```sql
select ... lock in share mode;
select ... for share;  MySQL 8.0
```

- **排它锁**

```sql
update ...
delete ...
insert ...
select ... for update
```

- **注意**
    - **某个事务获取数据的排它锁，其他事务不能获取该数据的任何锁，并不代表其他事务不能无锁读取该数据。**
    - 简单来说：**加了排它锁的数据，其他事务还可以用无锁读取数据。**

### 隔离级别

- 读未提交  有脏读的问题  A的数据未提交就被B读到了
- 读提交  解决了脏读 可能产生不可重复读  两次读取的结果不一致
- 可重复读  解决了不可重复读   可能产生幻读 幻读就是B提交事务以后，A查看自己开启事务中的数据，没有更新，但是插入对应的数据就报错说重复插入了。
- 串行化 解决幻读

## 事务

- 一组操作，要么同时成功，要么同时失败。

## 事务特性

- 原子性：事务是不可分割的。
- 一致性：事务操作前后的总量保持不变。
- 隔离性：事务操作间应该互不影响。
- 持久性：事务提交后改变是永久的。

### Mysql分库分表

读写分离：解决高并发。
分库分表：解决高可用。
分库：**减少并发问题**
分表：**降低了分布式事务**
垂直分表：一个表，列比较多，把不同的字段分到不同的表中，降低单表大小来提高性能。
水平分表：**以某个字段按照一定的规则，将一个表的数据分到多个表中。特点是表结构一样。**
分表策略

- hash取模
- range范围区分
- list预定义

### 左右联接

[学习视频](https://www.bilibili.com/video/BV1Vt411z7wy?p=55)

- inner join： **只保留两表完全匹配的结果集。**
- left join: 返回左表所有的行，右表中没有返回为null
- full join: **全外联接 ，返回左表和右表中所有没有匹配的行。**mysql不支持 full join，使用left join union right join来实现。

联接练习题

- 组合两个表
- 部门工资最高的员工
- 从不订购的客户

alter table 表名 alter column 字段名 set default 默认值;

### 隔离级别

- 读未提交【脏读】
- 读提交 【不可重复读】
- 可重复读【幻读】
- 串行化

### 事务特性

- 原子性：事务是不可分割的。
- 一致性：事务操作前后总量不变。
- 隔离性：事物之间不产生影响
- 持久性：一旦提交事务，改变是永久的。

开启事务

- set autocommit = 0
- begin
- start transaction

### 关键字

- group by 分组
- having作用于组
- order by对某一列进行排序
- where后不能有聚合
- limit row: offset


### SQL执行顺序

- from
- on
- join/where
- group by
- having
- select
- order by
- limit

### 数据库优化

- explain执行计划
- limit优化
- 性能监控show profile

### Mysql主从复制和读写分离

提高数据库的并发性能。
一个master负责写操作，两台slave负责读操作。
主从复制的原理master-slave

- 当主库进行增删改操作时，**会按顺序写入到binlog中**。
- 每个从库创建binlog dump线程**连接到主库**。
- 当master节点的binlog有变化时，**binlog dump线程会通知所有slave节点，并将相应的binlog内容推送给slave节点。**
- slave的IO线程收到binlog内容后，**将内容写入到本地的relay-log**
- sql线程读取本地的relay-log重新在从库中复现主库的增删改的操作。

读写分离存在的问题：

- 数据不一致问题

## 分库分表

数据库的IO瓶颈和CPU瓶颈都会导致数据库活跃连接数增加，进而逼近数据库可承载连接数的最大值。
IO瓶颈：磁盘读IO瓶颈，**热点数据太多，数据库缓存放不下**，每次查询时产生大量的IO，降低查询数据。解决方案【**分库和垂直分表**】
CPU瓶颈：SQL问题，包含join，group by，order by，非索引字段查询等，增加CPU运算的操作。解决方案【SQL优化，**建立适当的索引，在业务Service层进行业务计算**】单表数据量太大，**查询时扫描的行太多**，SQL效率低，CPU率先出现瓶颈。解决方案【水平分表】
分库分表工具：

- **mycat**
- sharding-sphere
- TDDL

分库分表总结：

- 分库分表首先要知道瓶颈在哪儿，才能合理地拆分。
- 选key很重要，既要考虑到拆分均匀，也要考虑到非patition key的查询。

#### 总结

- IO瓶颈：热点数据太多，缓存放不下。
    - **考虑分库，按照表的类别分。**
- CPU瓶颈：计算太慢，
    - SQL优化，建立复合索引。
    - 在业务层进行计算。
    - 扫描的行太多，**水平分表。**

## LFU

- 2个哈希表 + 2个双向链表。
- 最不经常使用，使用频次最低。
- 双向链表中套双向链表，外层的节点记录频次，内层的节点相同频次的时间顺序。
- 每次外层节点加1，内层节点删除，并插入右边外层的左边。
- 满了以后删除外层最左边的内层最右边节点。

### Redis的理解

- 五种数据结构：**string hash list set zset**
- 三种特殊数据类型：geo/hyperloglog/bitmap
- **持久化：AOF日志和RDB快照**
- 事务：multi exec watch
- 过期删除：expire key ttl   定期删除(100ms随机) + 惰性删除
- 集群：主从同步，哨兵(自动选举master)
- 解决方案：缓存穿透/击穿/雪崩
- 分布式锁setnx

分布式锁实现原理：多进程可见，互斥，可重入，高并发，高可用。
常见的分布式锁实现方案：基于数据库实现，基于缓存实现，基于zookeeper实现
原子性：要么同时成功，要么同时失败。
redis单条命令是保证原子性的，但是redis的事务是不保证原子性。
**事务的本质：一组命令的集合。**

redis事务没有隔离级别的概念，一个事务的所有命令都会被序列化，在事务执行过程中，按照顺序执行。所有的命令在事务中，并没有直接执行，只有发起执行命令的时候才执行，Exec。

redis事务

- 监控字段watch
- 开启事务multi
- 命令入队
- 执行事务exec

必须在事务开启之前watch，也就是不能再事务中间开启监控。
对key添加监视锁watch
分布式锁
**setnx **lock_key value
使用setnx设置一个公共锁，利用setnx命令的返回值特征，有值则返回设置失败0，无值则返回设置成功1。

- 成功。拥有控制权，执行下一步业务，用完后del释放锁。
- 失败。不具有控制权，排队等待。

如果释放锁之前宕机，就会导致死锁，可以设置锁的过期时间来解决。
set num 666 nx ex 100
误删锁问题：如何得知获取的锁是否是自己的锁。设置锁的名字，删除之前先对比。
重入性问题：获取锁之后，执行代码的过程中，尝试再次获取锁。记录锁的名称，比较一下，如果相同就继续让执行，再释放锁时记录调用层数，在最外层释放锁。使用hash来实现。
hset user name jack
hset user age 21
取消或放弃事务discard
一旦事务执行成功后，监控自动取消掉。如果想手动关闭监控使用unwatch。
exec返回nil表示事务执行失败
**redis可以实现乐观锁**
乐观锁：不加锁，更新数据时才去判断，获取version，然后比较version，监控某个值，执行事务之前，另一个线程修改了这个值，就会导致事务执行失败。
悲观锁：总是加锁。
事务执行中的错误：

- 语法错误：exec时，所有事务都不会执行。
- 运行时错误：比如对一个字符串自增，incr str 其他事务正常执行，只有出错的命令执行失败。



## RDB

RDB快照模式：默认
优点：适合大规模的数据恢复，对数据的完成性要求不高。
缺点：**最后一次持久化的数据可能丢失，fork子进程占用内存空间**。
触发机制

- Sava配置中的条件
- flushall
- 退出redis

恢复dump.rdb文件，只需将rdb文件放入redis启动目录下

## AOF

AOF日志模式：**将所有命令都记录下来，恢复的时候把这个文件全部再执行一遍。**
appendonly.aof
默认是不开启的，手动开启`appendonly yes`
默认每秒修改存储一次，重启后生效。
修复aof文件`redis-check-aof --fix appendonly.aof`
优点：每次修改都同步，文件的完整性更好。每秒同步一次，可能会丢失一秒的数据。
缺点：**aof文件大小远远大于rdb,修复速度也比rdb慢。**

## SDS

Redis使用SDS(simple dynamic string)简单动态字符串作为字符串表示

- 常数复杂度获取字符串长度。
- 杜绝缓冲区溢出。
- 减少修改字符串长度时所需的内存重分配次数。
- 二进制安全。
- 兼容部分C字符串函数

## 五种基本数据结构

- string SDS 字符串长度 缓冲区长度 当前使用长度
- list  双向链表
- set  红黑树
- hash 字典实现
- zset 跳跃表实现

## redis的功能

- **缓存**
- **持久化**
- **事务**
- **分布式锁**

## redis过期删除策略

1. **定期删除：**redis默认是每隔 100ms 就**随机抽取**一些设置了过期时间的key，检查其是否过期，如果过期就删除。
1. **惰性删除**：查询的时候再删。

## redis内存淘汰机制

1. Volatile-lru
1. volatile-ttl
1. volatile-random
1. allkeys-lru
1. allkeys-random
1. no-eviction


## Redis

- 五种数据类型：string list hash set zset
- 两种持久化：RDB和AOF
    - RDB可能丢失最近一次操作的数据。
    - AOF恢复较慢。
- 缓存穿透
    - 大量无效的key打到了数据库上
        - key=null的有效过期时间
        - 布隆过滤器
- 缓存击穿
    - 某个热key失效，大量请求打到mysql
        - 多级缓存
        - 随机过期
        - 监控
- 缓存雪崩
    - 大量key，集中失效。
        - 多级缓存
        - 随机过期
        - 永不过期
        - 监控
        - 降级限流
- 过期删除策略
    - 定期删除100ms
    - 惰性删除 查到了再删除
- 事务
    - multi 开启事务
    - exec 执行
    - watch 监控
- 分布式锁
    - setnx
- 过期
    - expire

## MySQL

- 事务
    - 一组操作，要么同时成功，要么同时失败。
- 事务四个特性
    - ACID
- 事务四种隔离级别
    - 读未提交
    - 不可重复读
    - 可重复读
    - 串行化
- 索引
    - 一种高效查询和排序的数据结构。
- MyISAM和InnoDB的区别
    - 不支持事务，行锁，外键，支持读多写少。
    - 支持事务，行锁，外键，适合高并发。
- B+树和B树
    - B树中索引和数据保存在一起，m叉B树最多有m-1个key
    - B+树非叶子节点只保留索引，叶子节点使用指针连接，叶子节点保存所有的索引和数据。
        - 单个阶段存储的索引增加。
        - 数据需要查询到叶子节点，查询效率稳定。
        - 有助于范围查询。
- 复合索引
    - 多个字段的索引
- 什么时候适合建索引
    - 排序的字段
    - 频繁作为查询条件的字段
- **什么情况不适合建索引**
    - 平均却单一的字段
    - 经常更改的字段
    - **百万数据一下不要建索引**
- SQL优化
    - select*少用
    - **对where和order by中的字段建索引**
    - 不要使用!=和or和函数在where中查询
    - **不要处理大的事务**
- redo log和undo log
    - redo是物理日志，常常用来对改数据页的物理修改，重新执行一遍。
    - undo是逻辑日志，用于回滚到某个版本，修改某几行。
- **当前读和快照读**
    - 当前读是最新版本。
    - 快照读是历史版本，可能过期。
- **MVCC**
    - 多版本并发机制，某个时间段的快照。
- 索引失效
    - 范围查询右边的失效
    - substring字符串
    - 字符串不加单引号
    - not in索引失效
    - 模糊查询失效

## 范围查询索引不会失效

## ES

- 倒排索引
    - 根据单词映射到文档
- 前缀树
    - 单词的公共前缀
- 健康状态
    - green：主副分片运行正常
    - yellow：主分片运行正常，至少有一个副分片运行不正常。
    - green：至少有一个主分片运行异常
- 写流程
    - coordinating node根据文档id和路由算法计算出对应的分片，
    - 转发对应的主分片data node上，主分片更新
    - 副分片同步
    - data node返回给coordinating node
    - coordinating node返回给客户端
- 读流程
    - coordinating node查询文档对应的分片，转发到各个分片上。
    - 各分片查询结果再汇总到coordinating node上，
    - coordinating node聚合完成后再返回给客户端
- 选主算法
    - bully算法
- 打分机制
    - TF/IDF 词频
    - BM25概率打分
- mapping
    - 默认主分片是5个，每个主分片有1个副本分片，共10个分片
    - ES每个索引由多个分片组成
    - 文档根据路由规则分配到不同的分片上
- 调优
    - JVM堆分配一半给ES
    - 打开进程文件描述符上限，**/etc/security/limits.conf** 从1024改成65535

