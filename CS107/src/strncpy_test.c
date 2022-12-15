#include <string.h>
#include <stdio.h>
int main() {
    char s[] = "hello\0world\n";
    char buf[1024];
    memset(buf, 0, sizeof buf);
//    char src[1024]="hello world";
//    strcpy(buf, s); // 搞清楚，是否strncpy也是遇到\0结束
    strncpy(buf, s, 11);
    for(int i = 0; i < 11; i++) {
        printf("%c", buf[i]);
    }
    printf("\n");
}