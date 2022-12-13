/*
调用fork的时候发生了copy on write吗？如何解释文件中写入的顺序？
运行结果：看起来是追加，不是覆盖。
*/

#include <unistd.h>
#include <fcntl.h>
#include <string.h>
 #include <sys/wait.h>

using namespace std;
int main() {
    int fd = open("a.txt", O_WRONLY | O_CREAT);
    int pid = fork();
    if (pid == 0) {
        // 子进程
        char *s = "1111111111111111111111111";
        write(fd, s, strlen(s));
        return 0;
    }else{
        // 父进程
        sleep(1);
        char *s = "222222222222222222222222222";
        write(fd, s, strlen(s));
        wait(0);
    }
    close(fd);
    return 0;
}