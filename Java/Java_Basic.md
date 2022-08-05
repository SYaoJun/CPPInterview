### ArrayList和LinkedList的区别★★★

-   Arraylist内存地址是连续的，底层是数组。随机访问的速度比较快，是常数时间，删除是线性的复杂度。

-   LinkedList内存地址是不连续的，是单链表。随机访问比较差，是线性的，插入删除比较快是常数时间。



### HashMap原理★★★

HashMap数组+链表或红黑树存储数据，**线程不安全**

**数组容量默认时16，负载因子默认是0.75**

Java 8以后，链表中的元素超过8后，hashmap会将链表结构转换为红黑树的结构提高查询效率。

线程安全版：Hashtable和ConcurrentHashMap

Hashtable并发性不如ConcurrentHashMap，基本弃用了。

ConcurrentHashMap分段锁实现并发操作，线程安全。

ConcurrentHashMap由多个segment组成，segment的数量也是锁的并发度，每个segment均继承自Reentrantlock并单独加锁，所以每次进行加锁操作时锁住的都是一个segment，这样只要保证每个segment都是线程安全的，也就实现了全局的线程安全。

put，get和resize的过程？



### Java的基本类型★★

java有8种基本类型

- Integer 4字节

- Long 8字节

- Double 8字节

- Boolean 1字节

- Short 2字节

- Float 4字节

- Char 2字节

- Byte 1字节  **这个类型容易被忘**



### 什么是反射？★★

反射机制：在运行时动态地创建类的对象，获取一个类的所有成员变量和方法。

反射的作用：

- 得到一个对象所属的类
- 获取一个类的所有成员变量和方法
- 在运行时动态地创建类的对象
- 在运行时动态地调用对象的方法

获取class对象的3种方式：

- 某个对象的getclass
- 类的class属性
- Class.forName("fullpathname")



### 多态★★

父类引用指向子类对象

成员变量：编译看等号左边，运行也看等号左边

成员方法：编译看左边，运行看右边。

父子都有的同名成员，多态时，调用的时父类的成员变量



### String、StringBuilder和StringBuffer★★

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


### final、finally和finalize的区别★★

**final** 关键字主要用在三个地方：变量、方法、类。

- 对于一个 final 变量，如果是基本数据类型的变量，则其数值一旦在初始化之后便不能更改；如果是引用类型的变量，则在对其初始化之后便不能再让其指向另一个对象。
- 当用 final 修饰一个类时，表明这个类不能被继承。final 类中的所有成员方法都会被隐式地指定为 final 方法
- 使用 final 方法的原因有两个。第一个原因是把方法锁定，以防任何继承类修改它的含义；第二个原因是效率。在早期的 Java 实现版本中，会将final 方法转为内嵌调用。但是如果方法过于庞大，可能看不到内嵌调用带来的任何性能提升（现在的 Java 版本已经不需要使用 final 方法进行这些优化了）。类中所有的 private 方法都隐式地指定为 final

**finally**

异常处理时,无论是否抛出异常都会执行的语句块,尽量在finally中避免return语句。

**finalize**

是object类中的方法,在该对象被垃圾回收时调用,一个对象的finalize方法只会被调用一次,被调用不意味着gc会立即回收该对象。



### Java和C++的区别★★

- 都是面向对象的语言，支持封装，继承和多态。
- Java不提供指针来直接访问内存，程序更加安全。
- Java是单继承，C++是多继承，但是Java可以实现多个接口来达到多继承。
- Java有内存管理机制，不需要程序员手动释放。

### Java中的值传递和引用传递

- 值传递被传递了对象的副本，即使副本被改变，也不会影响源对象。
- 引用传递传递的是对象的引用，对引用对象的改变会反应到所有对象上。

### 集合

Map 接口和 Collection 接口是所有集合框架的父接口。

Collection接口的子接口包括List和Set接口

List是有序的，可以重复。Set是无序的，不可以重复。

### 扩容机制★★

- ArrayList初始容量是10，默认扩容原容量的1.5倍。
- Vector是线程安全的List子类，初始容量是10，默认扩容是原容量的2倍。
- Stack是Vector的子类，增加了栈的特性。Vector和Stack都已经过时了，线程安全且高效的，使用Collections.synchronizedList(new ArrayList<>())。
- Map和Set默认容量都是16，加载因子0.75，默认扩容是原来容量的2倍大小。

### Java集合中的快速失败机制fail-fast

它是 java 集合的一种错误检测机制，当多个线程对集合进行结构上的改变的操作时，有可能会产生 fail-fast 机制。

### static

修饰成员变量和方式时，static是对象共享的，可以直接使用类操作静态成员变量和方法。

static优先于非静态加载入内存。

### equals和hashCode的区别★★

都是用来判断两个对象是否相同，两者都是Object中的方法，不同的类可以重写该方法。

按照Java的规范，equals相同的两个对象，hashCode必须相同。hashCode相同的对象，equals不一定相同。同时hashCode的返回结果应该具有稳定性。

一般重写equals方法同时也需要重写hashCode方法。

### 包裹类型

8种基本类型都有相应的包裹类型，包裹类型是一个类，所以创建对象的值放在堆中，而基本类型的值是直接放在栈中，因此基本类型的效率更高。

基本类型和基础类型可以互相转换，集合中只能使用包裹类型。

### 抽象类和接口★★

-   抽象类和接口都不能被实例化
-   抽象类可以没有抽象方法，但是有抽象方法的类必须是抽象类。接口中的方法，必须是抽象方法。
-   抽象类中可以有普通的成员变量；接口中的变量必须是static final类型的，必须被初始化，接口中只有常量，没有变量。
-   抽象类只能单继承，接口可以实现多个父接口。
-   Java8中接口有default方法，即方法可以被实现。

### BIO和NIO和AIO的区别★★★

进程触发IO操作时，自己干就是同步，别人干就是异步。可以不亲自去处理，把它委托给OS处理，自己去做别的事情，IO结束后会得到通知。

进程触发IO操作时，要等着不能做其他事情就是阻塞，不用等可以做其他事就是非阻塞。没办法读写就去做其他事情。

IO模型分为：同步阻塞，同步非阻塞，异步阻塞，异步非阻塞

- BIO同步阻塞，一个连接一个线程。可以引入线程池，减少线程创建和销毁的开销。
- NIO同步非阻塞，一个请求一个线程，单线程轮询。客户端发送的连接请求都会注册到多路复用器上，多路复用器轮询到有IO请求时才启动一个线程进行处理。
- AIO异步非阻塞,一个有效请求一个线程，客户端的IO请求都是由OS先完成了再通知服务器应用去启动线程进行处理。

并发量不多时用BIO,并发量比较大使用NIO和AIO或者直接使用netty。