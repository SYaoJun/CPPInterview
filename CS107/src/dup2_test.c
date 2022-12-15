#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <semaphore.h>
#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>

int main() {
    /*
     * #include <unistd.h>
     * int dup2(int x, int y) 原来访问y的，现在访问x
     * ref: csapp 10.9
     * */
    int oldfd = open("a.txt", O_CREAT | O_RDWR);
    int res = dup2(oldfd, STDOUT_FILENO);


    return 0;
}