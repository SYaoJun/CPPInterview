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

### ArrayList和LinkedList的区别

-   Arraylist内存地址是连续的，底层是数组。随机访问的速度比较快，是常数时间，删除是线性的复杂度。

-   LinkedList内存地址是不连续的，是单链表。随机访问比较差，是线性的，插入删除比较快是常数时间。

### Java的基本类型

java有8种基本类型

- Integer 4字节

- Long 8字节

- Double 8字节

- Boolean 1字节

- Short 2字节

- Float 4字节

- Char 2字节

- Byte 1字节  


### 反射机制

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

### final、finally和finalize的区别★★

**final** 关键字主要用在三个地方：变量、方法、类。

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