#include <stdbool.h> // c不是有布尔嘛
#include <stdio.h>
void func(char* s) {
    char* tt = "world";
    s = tt;
    printf("in function = %s\n", s);
    char temp[1024];
    s = temp; // char*是常量指针，指向一个字符串
    // char []是栈数组，可以随时修改，可以让另一个指针指向该数组
}
int main() {
    // 是有bool类型的
    bool res = true;
    char* p = "hello";
    char q[1024] = "world";

    func(p);
    return 0;
}