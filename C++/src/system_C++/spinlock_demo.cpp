/*
 * 线程同步的一种方式。使用自旋锁的线程会反复检查锁变量是否可用。自旋锁不会让出CPU，一种忙等待状态。死循环等待锁被释放。自旋锁避免了进程或线程上下文的开销。自旋锁不适合在单CPU中使用。
 *
 * */
#include <unistd.h>
#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
const int N = 1e7;
int num = 0;
pthread_spinlock_t spin_lock;
void *producer(void *){
    int times = N;
    while(times--){
        pthread_spin_lock(&spin_lock);
        ++num;
        pthread_spin_unlock(&spin_lock);
    }
}
void *comsumer(void*){
    int times = N;
    while(times--){
        pthread_spin_lock(&spin_lock);
        --num;
        pthread_spin_unlock(&spin_lock);
    }
}
int main(){
    pthread_spin_init(&spin_lock, 0);
    pthread_t th1, th2;
    pthread_create(&th1, NULL, &producer, NULL);
    pthread_create(&th2, NULL, &comsumer, NULL);
    pthread_join(th1, NULL);
    pthread_join(th2, NULL);
    printf("num =  %d\n", num);
    return 0;
}
