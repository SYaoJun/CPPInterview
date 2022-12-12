#include <unistd.h>
#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
const int MAX_BUF = 100;
int num = 0;
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

void *producer(void *){
    while(true){
        pthread_mutex_lock(&mutex);
        while(num >= MAX_BUF){ //由于阻塞解除时，只有一个物品可用 但是却有多个线程解除阻塞 所以需要循环检测一次
            //满了 等待消费者消费
            pthread_cond_wait(&cond, &mutex);
            printf("缓冲区满了 等待消费者消费\n");
        }
        //生产一个物品
        ++num;
        printf("生产一个产品，当前产品数量为：%d\n", num);
        sleep(1);
        pthread_mutex_unlock(&mutex);
        //通知消费者可消费了
        pthread_cond_signal(&cond);
        printf("通知消费者...\n");
        sleep(1);
    }
}
void *comsumer(void*){
    while(true){
        pthread_mutex_lock(&mutex);
        while(num <= 0){
            //缓冲区为空 等待生产者生产
            pthread_cond_wait(&cond, &mutex);
            printf("缓冲区空了 等待生产者生产\n");
        }
        //生产一个物品
        --num;
        printf("消费一个产品，当前产品数量为：%d\n", num);
        sleep(1);
        pthread_mutex_unlock(&mutex);
        //通知消费者可消费了
        pthread_cond_signal(&cond);
        printf("通知生产者...\n");
    }
}
int main(){
    pthread_t th1, th2;
    pthread_create(&th1, NULL, &producer, NULL);
    pthread_create(&th2, NULL, &comsumer, NULL);
    pthread_join(th1, NULL);
    pthread_join(th2, NULL);
    printf("num =  %d\n", num);
    return 0;
}
