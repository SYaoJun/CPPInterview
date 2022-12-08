## lab utility
## xv6编程语言
- C语言
## labs
- 我的实验环境macOS
```c
$ gcc --version
Apple clang version 14.0.0 (clang-1400.0.29.202)
```
## qemu
- 纯软件实现的虚拟化模拟器，几乎可以模拟任何硬件设备。
- 负责IO虚拟化
## KVM
- 内核虚拟机，KVM是Linux的一部分。
- 在KVM模型中，虚拟机是一种Linux进程，由内核进行调度和管理。
- 负责CPU和内存虚拟化
- sleep.c
    - 从user/echo.c文件中拷贝过来三个头文件，记住顺序必须保持一致，因为有依赖关系。
    - 在Makefile中添加新增的sleep文件。

```c
#include "kernel/types.h"
#include "kernel/stat.h"
#include "user/user.h"

int main(int argc, char* argv[]) {
	if(argc < 2) {
		printf("usage: need tickles\n");
		exit(0);
	}
	sleep(atoi(argv[1]));
	exit(0);
}

```
- pingpong.c
    - 管道pipe(fd)必须保持0读，1写，类比于标准输入和输出。
```c
#include "kernel/types.h"
#include "kernel/stat.h"
#include "user/user.h"

int main(int argc, char* argv[]) {
    if(argc > 1) {
        exit(1);
    }
    int p1[2]; // 父写子读
    int p2[2];
    pipe(p1);
    pipe(p2);
    int pid = fork();
    if(pid == 0) {
        /*0读，1写*/
        close(p1[1]);
        close(p2[0]);

        char buf[128];
        memset(buf, 0, sizeof(buf));
        read(p1[0], buf, sizeof(buf)); // 2.
        close(p1[0]);

        printf("%d: received ping\n", getpid());
        write(p2[1], buf, strlen(buf));//3.
        close(p2[1]);
        exit(0);
    }else{
        // 父
        close(p1[0]);
        close(p2[1]);
        char buf2[128];
        
        memset(buf2, 0, sizeof(buf2));
        write(p1[1], "!", 1); // 1.
        close(p1[1]);

        read(p2[0], buf2, sizeof(buf2)); //4.
        printf("%d: received pong\n", getpid());

        close(p2[0]);
        wait(0);
    }
    exit(0);
}
```