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

## 什么是大小端？如何用代码判断大小端？

## 如何定位内存泄露问题？

## 如何使用perf分析程序性能？

## C/C++内存模型

## 什么是内存对齐？为什么内存要对齐？

## 提高C/C++程序性能的技巧？

## C/C++互相调用通常在头文件中做什么处理？

## static在类成员变量和类成员函数中有什么作用？
静态成员函数只能访问静态成员变量。静态成员变量在所有对象中共享。
## 如何实现类的单例模式？

## 如何判断链表是否有环？如何找到链表的中点？如何对链表排序？如何对二叉树做层序遍历？给定四个坐标如何判断是否是正方形？

## 如何提高TLB缓存命中率？

## 什么时候需要用虚函数？

## 什么时候需要用智能指针？
想要malloc和new时，不用显式分配内存和管理内存，就可以使用智能指针。

## 移动语义与完美转发

## C++20协程

## 源文件生成可执行文件的过程

## 内存管理？如何避免内存碎片？

## 线程上下文切换会做哪些工作？

## 虚拟地址空间到物理地址空间的流程说一下

## 如何减小锁的粒度？如何避免死锁？

## 如何保证程序是线程安全的？

## 如何实现一个线程安全的延迟队列？

## 如何实现原子操作CAS

## 你技术上最大的优势是什么？你最擅长什么技术？C/C++功能实现，算法与数据结构，linux内核，操作系统，还是协作沟通，英语等？