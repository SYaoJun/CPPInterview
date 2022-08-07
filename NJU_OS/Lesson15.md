## fork的应用
- C标准库是线程安全的！
- 生产者-消费者
- 延迟队列
### fork
- 父进程返回子进程的PID
- 子进程返回0
- 写时复制 copy on write
- 父子进程共享打开的文件描述符，偏移量也共享
```shell
#include <unistd.h>
#include <fcntl.h>
using namespace std;
int main() {
    int fd = open("../config/a.txt", O_WRONLY | O_CREAT);
    int pid = fork();
    if (pid == 0) {
        // 子进程
        write(fd, "hello", 5);
    }else{
        // 父进程
        sleep(1);
        write(fd, "world", 5);
    }
    close(fd);
    return 0;
}
// helloword 输出的顺序随机 不会覆盖 而是追加 共享
```
### 文件描述符
- 整数
- open
- 一个指向操作系统内对象的指针
### open
- 偏移量
### 管道
- pipe
### 零拷贝

### dup
- 复制一个文件描述符
- 