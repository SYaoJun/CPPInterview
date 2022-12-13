/*
函数指针本身是指针变量，指向某个函数的入口地址。
*/
#include <stdio.h>
#include <unistd.h>

/*回调函数的传参是声明的格式*/
int run(void(*step)(int var)){
    int cnt = 0;
    while(1){
        if(step != NULL) step(cnt);
        cnt++;
        sleep(1);
    }
    return 0;
}

void cb(){  /*回调函数*/
    puts("几秒到时");
}

void cb2(int cnt){
    printf("how long %d\n", cnt);
}
int main(){
    /*传给它一个函数名，函数名本身是一个指针*/
    run(cb2);
    return 0;
}