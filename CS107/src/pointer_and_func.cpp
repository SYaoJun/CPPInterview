#include <stdio.h>
#include <stdlib.h>
// 函数指针
int* sub(int a, int b) {
    int *t = (int*)malloc(sizeof(int));
    *t = a - b;
    return t;
}

int main() {
    // 函数指针
    int* (*f)(int, int);
    f = sub;
    int* res = f(2, 3);
    printf("res = %d\n", *res);
    return 0;
}