## 操作系统设计
- [课程官网](https://pdos.csail.mit.edu/6.828/2020/schedule.html)
- [B站视频](https://www.bilibili.com/video/BV19k4y1C7kA/?spm_id_from=333.999.0.0&vd_source=e9f1ced96b267a4bc02ec41ca31d850a)

### xv6编程语言
- C语言

### labs
- 我的实验环境macOS
```c
$ gcc --version
Apple clang version 14.0.0 (clang-1400.0.29.202)
```
### qemu
- 纯软件实现的虚拟化模拟器，几乎可以模拟任何硬件设备。
- 负责IO虚拟化
### KVM
- 内核虚拟机，KVM是Linux的一部分。
- 在KVM模型中，虚拟机是一种Linux进程，由内核进行调度和管理。
- 负责CPU和内存虚拟化
### lab0
- 从user/echo.c文件中拷贝过来三个头文件，记住顺序必须保持一致，因为有依赖关系。
- 在Makefile中添加新增的sleep文件。