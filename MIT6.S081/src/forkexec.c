#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>

int main(int argc, char* argv[]) {
    int pid = fork();
    if(pid == 0) {
        close(1);
        open("output2.txt", O_WRONLY | O_CREAT);
        execlp("echo", "s", argv[1], 0);
        printf("exec failed!\n");
        return 0;
    }else{
        wait((int*)0);
    }

    return 0;
}