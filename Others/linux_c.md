## webbench 
- 测压软件
- 最高并发3W 
> 注意：webbench做测试时自身也会消耗CPU和内存资源。为了测试准确，需要将webbench安装在别的服务器上。
```shell
tar -xzvf webbench-1.5.tar.gz
cd webbench-1.5
apt-get install ctags
make && make install
```

测试

``` shell
webbench -c 1000 -t 5 http://127.0.0.1:9999/index.html //1000个客户端 5秒钟时间
```

## 信号函数

```c
raise(SIGSEGV) //自己给自己进程发送信号 11
abort() //终止当前进程
```

测试1s打印多少个数

alarm函数

```c
#include <unistd.h>
#include <stdio.h>
int main(){
    alarm(1); //计时1s 到时后内核发送一个sigalarm信号终止
    for(int i = 0;;i++) printf("%d\n", i);
    return 0;
}
```

setitimer函数

```c
#include <unistd.h>
#include <stdio.h>
#include <sys/time.h>
#include <stdlib.h>
int my_alarm(int sec){
    struct itimerval it, oldit;
    it.it_value.tv_sec = sec; //定时长度
    it.it_value.tv_usec = 0; //微秒
    it.it_interval.tv_sec = 0; //周期定时
    it.it_interval.tv_usec = 0;
    int ret = setitimer(ITIMER_REAL, &it, &oldit);
    if(ret == -1){
        perror("setitimer error");
        exit(1);
    }
    return oldit.it_value.tv_sec;
}
int main(){
    my_alarm(1); //计时1s 到时后内核发送一个sigalarm信号终止
    for(int i = 0;;i++) printf("%d\n", i);
    return 0;
}
```

## 创建线程

[视频](https://www.bilibili.com/video/BV1dt411f7TZ?p=183)

```c
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <stdlib.h>
void* func(void* arg){ //必须为这种类型
    printf("in thread : thread id: %lu, process id: %u\n", pthread_self(), getpid());
}
int main(void){
    //创建线程 
    pthread_t tid; //重命名的unsigned long 类型
    //创建线程API pthread_create(arg1, agr2, arg3, arg4) 
    //arg1: 传入的线程tid地址 
    //arg2: 线程属性 通常设置为NULL
    //arg3: 线程执行的任务 函数指针 
    //arg4: 参数3传递的参数
    printf("in main 1 : thread id: %lu, process id: %u\n", pthread_self(), getpid());
    int ret = pthread_create(&tid, NULL, func, NULL); 
    if(ret != 0){
        perror("pthread_create error");
        exit(1);
    }
    sleep(1); //主线程 等待子线程执行完毕
    printf("in main 2 : thread id: %lu, process id: %u\n", pthread_self(), getpid());
    return 0;
}
```

## 创建多个子线程

[视频](https://www.bilibili.com/video/BV1dt411f7TZ?p=184)

```c
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <stdlib.h>
#include <string.h>
void* func(void* arg){ //必须为这种类型
    int i = (int)arg;
    printf("%dth thread id: %lu, process id: %u\n", i, pthread_self(), getpid());
}
int main(void){
    //创建线程 
    pthread_t tid; //重命名的unsigned long 类型
    //创建线程API pthread_create(arg1, agr2, arg3, arg4) 
    //arg1: 传入的线程tid地址 
    //arg2: 线程属性 通常设置为NULL
    //arg3: 线程执行的任务 函数指针 
    //arg4: 参数3传递的参数
    int n = 5, ret;
    for(int i = 0; i < n; i++){
        ret = pthread_create(&tid, NULL, func, (void*)i); 
            if(ret != 0){
                fprintf(stderr, "%s pthread_create error", strerror(ret));
                exit(1);
            }
        pthread_detach(tid);
    }
    sleep(n); //主线程 等待子线程执行完毕
    return 0;
}
```

## mysql使用

mysql在linux环境下结合C语言的使用

```shell
sudo apt-get install mysql-client mysql-server //先安装mysql
sudo apt-get install libmysql++-dev //安装库
```

先启动mysql库 设置好密码 然后使用c程序连接

```c
#include <stdio.h>
#include <string.h>
#include <mysql/mysql.h>
int main(){
	MYSQL mysql;
	MYSQL_RES *res;
	MYSQL_ROW row;
	int i, j;
	char *query = "select * from people;";
	mysql_init(&mysql); //初始化
	if(!mysql_real_connect(&mysql,"localhost","root","password","yaojun",3306,NULL,0)){ //连接数据库
    	printf("Error in connecting");
	}
	if(mysql_query(&mysql,query)){ //查询数据库
    	printf("Error in querying");
	}
	res = mysql_store_result(&mysql);
	while(row = mysql_fetch_row(res)){ //读取数据库中的一行
    	for(i=0;i<mysql_num_fields(res);i++){
        	fprintf(stdout,"%s ",row[i]);
    	}
    	printf("\n");
	}
	mysql_free_result(res); //释放
	mysql_close(&mysql); //关闭
    return 0;
}
```

编译的命令

``` shell
gcc sql.c -lmysqlclient //生成a.out文件 执行
```

## 指针和数组

```c
char str[]="hello"; //字符串含\0   6字节
char *url ="hello"; //指针64位机   8字节
cout<<sizeof(str)<<" "<<sizeof(url)<<endl;
```

## CGI服务器

原理：输出到某个文件描述符上的内容直接发送到客户端连接对应的socket上，此处我们模拟了把服务器端输出到标准输出的内容，直接发送给客户端。

测试

```c
telnet 127.0.0.1 6666
```

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <ctype.h>
#include <assert.h>
#include <netinet/in.h>
#include <errno.h>
#include <string.h>
//命令行参数指定IP和端口
int main(int argc, char *argv[]){ 
    if(argc <= 2){
        printf("at least 3 arguments: file ip port, but you give %d\n", argc);
        return 1;
    }
    const char* ip = argv[1];
    int port = atoi(argv[2]);

	int lfd, cfd, ret;
	struct sockaddr_in serv_addr, clie_addr;
	lfd = socket(AF_INET, SOCK_STREAM, 0); //创建套接字
    assert(lfd >= 0);
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(port);
    inet_pton(AF_INET, ip, &serv_addr.sin_addr);
    //端口复用 此处没有卵用
    int opt = 1;
    setsockopt(lfd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt)); 
	
    ret = bind(lfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr) );
    assert(ret != -1);
	ret = listen(lfd, 128); //最大同时连接数
    assert(ret != -1);
	socklen_t clie_addr_len; //套接字长度
	clie_addr_len = sizeof(clie_addr);
	cfd = accept(lfd, (struct sockaddr*)&clie_addr, &clie_addr_len );
    if(cfd < 0){
        printf("accept error: %d", errno);
    }else{
        close(STDOUT_FILENO);
        dup(cfd); //创建一个新的文件描述符 该文件描述符和原文件描述符指向相同的文件 管道和网络连接
        printf("good night! daisy!\n");
        close(cfd);
    }
	close(lfd);
	return 0;
}
```

## EPOLLONESHOT事件

一个socket上的某个事件被触发多次，可能产生2个不同的线程处理同一个socket。我们期望的是一个socket在任一时刻都只被一个线程处理。对于注册了EPOLLONESHOT事件的文件描述符，操做系统最多触发其上注册的一个可读可写或者异常事件一次。注册了EPOLLONESHOT事件的socket一旦被某个线程处理完毕，应立即重置这个socket上的EPOLLONESHOT事件。

监听socket不应设置为EPOLLONESHOT。

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <ctype.h>
#include <assert.h>
#include <netinet/in.h>
#include <errno.h>
#include <string.h>
#include <pthread.h>
#include <fcntl.h>
#include <sys/epoll.h>
#define MAX_SIZE 1024
//自定义的结构体
struct fds{
    int epollfd;
    int sockfd;
};
//设置文件描述符为非阻塞
void setnonblocking(int fd){
    int old_option = fcntl(fd, F_GETFL);
    int new_option = old_option | O_NONBLOCK;
    fcntl(fd, F_SETFL, new_option);
}
//添加到epoll内核事件表中
void addfd(int epollfd, int fd, bool oneshot){
    epoll_event event;
    event.data.fd = fd;
    event.events = EPOLLIN | EPOLLET;
    if(oneshot){
        event.events |= EPOLLONESHOT;
    }
    epoll_ctl(epollfd, EPOLL_CTL_ADD, fd, &event); //挂到红黑树上
    setnonblocking(fd); //设置非阻塞 主要用在读写上
}
//重置EPOLLONESHOT事件
void reset_oneshot(int epollfd, int fd){
    epoll_event event;
    event.data.fd = fd;
    event.events = EPOLLIN | EPOLLET | EPOLLONESHOT;
    epoll_ctl(epollfd, EPOLL_CTL_MOD, fd, &event); //修改注册事件
}
//工作线程
void* worker(void* arg){
    int sockfd = ((fds*)arg)->sockfd;
    int epollfd = ((fds*)arg)->epollfd;
    printf("start new thread to receive data on fd: %d\n", sockfd);
    char buf[MAX_SIZE];
    memset(buf, '\0', MAX_SIZE);
    //循环读取sockfd上的数据 直到收到EAGAIN
    while(1){
        int ret = recv(sockfd, buf, MAX_SIZE-1, 0);
        if(ret == 0){
            close(sockfd);
            printf("foreiner closed the connection\n");
            break;
        }else if(ret < 0){
            if(errno == EAGAIN){
                reset_oneshot(epollfd ,sockfd);
                printf("read later\n");
                break;
            }
        }else{
            printf("get connection: %s\n", buf);
            //休眠5s模拟数据处理过程
            sleep(5);
        }
    }
    printf("end thread receiving data on fd: %d\n", sockfd);
}
//命令行参数指定IP和端口
int main(int argc, char *argv[]){ 
    if(argc <= 2){
        printf("at least 3 arguments: file ip port, but you give %d\n", argc);
        return 1;
    }
    const char* ip = argv[1];
    int port = atoi(argv[2]);

	int lfd, cfd, ret;
	struct sockaddr_in serv_addr, clie_addr;
	lfd = socket(AF_INET, SOCK_STREAM, 0); //创建套接字
    assert(lfd >= 0);
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(port);
    inet_pton(AF_INET, ip, &serv_addr.sin_addr);
    //端口复用 此处没有卵用
    int opt = 1;
    setsockopt(lfd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt)); 
	
    ret = bind(lfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr) );
    assert(ret != -1);
	ret = listen(lfd, 128); //最大同时连接数
    assert(ret != -1);
    epoll_event events[MAX_SIZE]; //返回的数组上限
    int epollfd = epoll_create(10);
    assert(epollfd != -1);
    //注意监听的套接字不能设置为oneshot
    addfd(epollfd, lfd, false); //挂上红黑树监听
    printf("addfd\n");
    while(1){
        ret = epoll_wait(epollfd, events, MAX_SIZE, -1); //永远不超时
        if(ret < 0){
            printf("epoll failure\n");
            break;
        }
        for(int i = 0; i < ret; i++){ //循环处理有响应的事件
            int sockfd = events[i].data.fd;
            if(sockfd == lfd){ //如果是监听事件则建立新的连接
                printf("lfd\n");
                socklen_t clie_addr_len; //套接字长度
                clie_addr_len = sizeof(clie_addr);
                cfd = accept(lfd, (struct sockaddr*)&clie_addr, &clie_addr_len );
                assert(cfd >= 0);
                //注册为oneshot事件
                addfd(epollfd, cfd, true); //刚刚这里加入的事件加错了
            }else if(events[i].events & EPOLLIN){
                pthread_t tid;
                fds fds_for_new_worker;
                fds_for_new_worker.epollfd = epollfd;
                fds_for_new_worker.sockfd = sockfd;
                //新启动一个线程为sockfd服务
                pthread_create(&tid, NULL, worker, (void*)&fds_for_new_worker);
                // pthread_detach(tid); //线程分离
            }
        }
    }
	close(lfd);
	return 0;
}

```

## 信号屏蔽字

主要函数

```c
sigaddset()
sigprocmask()
sigpending()
```

使用kill发送信号

```c
kill -6 PID
```

测试程序

```c
#include <unistd.h>
#include <stdio.h>
#include <signal.h>
void print(sigset_t* ped){
    for(int i = 0; i < 32; i++){
        if(sigismember(ped, i)==1){
            putchar('1');
        }else putchar('0');
    }
    printf("\n");
}
int main(void){
    sigset_t myset, oldset, ped;
    sigemptyset(&myset);
    //设置自定义信号集
    sigaddset(&myset, SIGINT);
    sigaddset(&myset, SIGSEGV);
    sigaddset(&myset, SIGQUIT);
    sigaddset(&myset, SIGABRT);
    //设置信号屏蔽字
    sigprocmask(SIG_BLOCK, &myset, &oldset);
    while(1){
        sigpending(&ped);
        print(&ped);
        sleep(2);
    }
    return 0;
}

```

## sigaction信号捕捉函数

```c
#include <unistd.h>
#include <stdio.h>
#include <signal.h>
void docatch(int signo){
    printf("%d signal has been catched!\n", signo);
}
int main(void){
   
    struct sigaction act;
    act.sa_handler = docatch;
    sigemptyset(&act.sa_mask);
    sigaddset(&act.sa_mask, SIGINT);
    
    sigaddset(&act.sa_mask, SIGSEGV);
    sigaddset(&act.sa_mask, SIGQUIT);
    act.sa_flags = 0; //默认属性 在信号函数处理期间 本信号再次到达默认屏蔽
    sigaction(SIGINT, &act, NULL);
    while(1);
    return 0;
}

```

## 统一事件源

把信号事件的处理放到epoll监听事件中去处理，统一了事件源。当调用信号处理函数时，信号处理函数通过管道将信息传达给epoll上的读端监听事件，再在主循环中处理事件。

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <ctype.h>
#include <assert.h>
#include <netinet/in.h>
#include <errno.h>
#include <string.h>
#include <pthread.h>
#include <fcntl.h>
#include <sys/epoll.h>
#include <signal.h>
#define MAX_SIZE 1024
//自定义的结构体
static int pipefd[2];

struct fds{
    int epollfd;
    int sockfd;
};
//设置文件描述符为非阻塞
void setnonblocking(int fd){
    int old_option = fcntl(fd, F_GETFL);
    int new_option = old_option | O_NONBLOCK;
    fcntl(fd, F_SETFL, new_option);
}
//添加到epoll内核事件表中
void addfd(int epollfd, int fd, bool oneshot){
    epoll_event event;
    event.data.fd = fd;
    event.events = EPOLLIN | EPOLLET;
    if(oneshot){
        event.events |= EPOLLONESHOT;
    }
    epoll_ctl(epollfd, EPOLL_CTL_ADD, fd, &event); //挂到红黑树上
    setnonblocking(fd); //设置非阻塞 主要用在读写上
}
//信号处理函数
void sig_handler(int sig){
    int save_errno = errno;
    int msg = sig; //我猜想这里重新定义变量的原因在于传的是指针 同时为了保证可重入
    send(pipefd[1], (char*)&msg, 1, 0); //pipefd[1]是非阻塞的如果发不出去直接返回
    errno = save_errno;
}
//设置信号处理
void addsig(int sig){
    struct sigaction sa;
    memset(&sa, '\0', sizeof(sa));
    sa.sa_handler = sig_handler;
    sa.sa_flags |= SA_RESTART;
    sigfillset(&sa.sa_mask);
    // sigaddset(&sa.sa_mask, SIGSEGV);
    assert(sigaction(sig, &sa, NULL) != -1); //注册监听的信号
}

//命令行参数指定IP和端口
int main(int argc, char *argv[]){ 
    if(argc <= 2){
        printf("at least 3 arguments: file ip port, but you give %d\n", argc);
        return 1;
    }
    const char* ip = argv[1];
    int port = atoi(argv[2]);

	int lfd, cfd, ret;
	struct sockaddr_in serv_addr, clie_addr;
	lfd = socket(AF_INET, SOCK_STREAM, 0); //创建套接字
    assert(lfd >= 0);
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(port);
    inet_pton(AF_INET, ip, &serv_addr.sin_addr);
    //端口复用 此处没有卵用
    int opt = 1;
    setsockopt(lfd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt)); 
	//忽略SIGPIPE信号
    signal(SIGPIPE, SIG_IGN);
    ret = bind(lfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr) );
    assert(ret != -1);
	ret = listen(lfd, 128); //最大同时连接数
    assert(ret != -1);
    epoll_event events[MAX_SIZE]; //返回的数组上限
    int epollfd = epoll_create(10);
    assert(epollfd != -1);
    //注意监听的套接字不能设置为oneshot
    addfd(epollfd, lfd, false); //挂上红黑树监听
    
    /*使用socketpair创建全双工的管道*/
    ret = socketpair(PF_UNIX, SOCK_STREAM, 0, pipefd);
    assert(ret != -1);
    setnonblocking(pipefd[1]); //把写入的管道端置为非阻塞
    addfd( epollfd, pipefd[0], false); //设置为oneshot

    /*设置一些信号的处理函数*/
    addsig(SIGHUP);
    addsig(SIGCHLD);
    addsig(SIGTERM);
    addsig(SIGINT);
    addsig(SIGSEGV);
    
    bool stop_server = false;
    while(!stop_server){
        printf("epoll_wait...\n");
        ret = epoll_wait(epollfd, events, MAX_SIZE, -1); //永远不超时
        if((ret < 0) && (errno != EINTR)){ //这里要设置 被系统调用打断的不算失败 errno不是ret
            perror("epoll failure");
            exit(1);
        }
        for(int i = 0; i < ret; i++){ //循环处理有响应的事件
            int sockfd = events[i].data.fd;
            if(sockfd == lfd){ //如果是监听事件则建立新的连接
                
                socklen_t clie_addr_len; //套接字长度
                clie_addr_len = sizeof(clie_addr);
                cfd = accept(lfd, (struct sockaddr*)&clie_addr, &clie_addr_len );
                assert(cfd >= 0);
                //注册为oneshot事件
                addfd(epollfd, cfd, true); 

                /*如果就绪的文件描述符是pipefd[0],就处理信号*/
            }else if((sockfd == pipefd[0]) &&(events[i].events & EPOLLIN)){
                char buf[MAX_SIZE];
                int num = recv(pipefd[0], buf, sizeof(buf), 0);
                if(num == -1) continue;
                else if(num == 0) continue;
                else{
                    //可能管道有多个信号满足 每次读出一个字符进行处理
                    for(int j = 0; j < num; j++){
                        switch(buf[j]){
                            case SIGSEGV: puts("段错误信号已处理，收到请回答！"); break;
                            case SIGCHLD:
                            case SIGHUP: continue;
                            case SIGTERM:
                            case SIGINT: stop_server = true;break;
                        }
                    }
                }
            }else{}
        }
    }
	printf("close fds\n");
    close(lfd);
    close(pipefd[0]);
    close(pipefd[1]);
	return 0;
}

```

## 单例模式

```c
#include <iostream>
#include <atomic>
#include <mutex>
using namespace std;
class Singleton{
    private: //无法调用构造函数
        Singleton();
        Singleton(const Singleton& other);
    public:
        static Singleton* getInstance();
        static Singleton* m_instance;
}
Singleton* Singleton::m_instance = nullptr;
//懒汉式 单线程版
Singleton* Singleton::getInstance(){
    if(m_instance == nullptr){
        m_instance = new Singleton();
    }
    return m_instance;
}
//多线程版
Singleton* Singleton::getInstance(){
    LOCK lock;
    if(m_instance == nullptr){
        m_instance = new Singleton();
    }
    return m_instance;
}
```

## 当前时间

```c
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
int main(void){
    time_t tm;
    time(&tm);
    char time_string[128];
    ctime_r(&tm, time_string);
    printf("%s", time_string);
    return 0;
}
```
## 主线程测试

```c
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <stdlib.h>
#include <string.h>
#include "logger.h"
void* func(void* arg){
    char buf[1024];
    sprintf(buf, "thread id: %lu, process id: %u\n", pthread_self(), getpid());
    Logger::log->write_log(2, buf);
}
int main(void){
    pthread_t tid; //重命名的unsigned long 类型
    Logger::log->create_file();
    int n = 5, ret;
    for(int i = 0; i < n; i++){
        // int t = i;
        ret = pthread_create(&tid, NULL, func, NULL); 
            if(ret != 0){
                fprintf(stderr, "%s pthread_create error", strerror(ret));
                exit(1);
            }
        pthread_detach(tid);
    }
    sleep(n-4); //主线程 等待子线程执行完毕
    return 0;
}
```

## 时间堆

把监听文件描述符加入后，就启动定时器。

## exec函数族

在一个程序中运行另一个程序。当进程调用exec函数时，该进程的用户空间代码和数据完全被新程序替换。调用exec并不创建新进程，所以调用exec前后进程的ID并不改变。

```c
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
int main(){
    pid_t pid = fork();
    if(pid == -1){
        perror("fork error!");
        exit(-1);
    }else if(pid == 0){
        execlp("ls", "anythingok", "-l", "-a", NULL);
    }else if(pid > 0){
        sleep(1);
        puts("parent over!");
    }
    return 0;
}
```

## 管道

```c
#include <unistd.h>
#include <stdio.h>
#include <string.h>
int main(){
    pid_t fd[2];
    pipe(fd); //创建管道
    int ret = fork();
    if(ret > 0){ //父进程 父写 fd[0]读 fd[1]写
        close(fd[0]);
        char *str ="hello world\n";
        write(fd[1], str, strlen(str));
        sleep(1);
    }else if(ret == 0){ //子进程 子读 fd[1]关闭
        close(fd[1]);
        char buf[1024];
        int n = read(fd[0], buf, sizeof(buf));
        //写到显示器上
        write(1, buf, n);
    }
    return 0;
}
```

## CGI使用管道和exec实现

hello里面的输入和输出都被重定向了

```c
#include<stdio.h>
#include<stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
int main(int agrc, char* argv[]){
    char bf[100];
    read(STDIN_FILENO, bf, sizeof(bf));
    sprintf(bf, "Content-Type:text/html;\r\n\r\nhello world, 你好!");
    printf("%s", bf);
    return 0;
}
```

主进程调用已经编译完毕的hello可执行文件

```c
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
int main(){
    pid_t pid; 
    int status;
    int cgi_input[2];
    int cgi_output[2];
    char buf[1024];
    /*创建输入管道*/
    if(pipe(cgi_input) < 0){
        perror("pipe error");
        exit(1);
    }
    /*创建输出管道*/
    if(pipe(cgi_output) < 0){
        perror("pipe error");
        exit(1);
    }
    /*创建子进程*/
    if((pid = fork()) < 0){
        perror("fork error!");
        exit(-1);
    }
    
    if(pid == 0){ 
        dup2(cgi_input[0], 0); /*将子进程的STDIN重定向到cgi_input[0]*/
        dup2(cgi_output[1], 1); /*将子进程的STDOUT重定向到cgi_output[1]*/
        /*关闭剩余的两端*/
        close(cgi_input[1]);
        close(cgi_output[0]);
        /*执行exec文件 即cgi*/
        execl("hello", "anythingok", NULL);
        exit(0);
    }else if(pid > 0){  /*父进程先给子进程发送数据 然后等待子进程执行完 再读数据*/
        /*关闭不用的两个端口*/
        close(cgi_input[0]); 
        close(cgi_output[1]);
        char tmp[100]="hello child process";
        int len = strlen(tmp);
        /*父进程先写数据*/
        write(cgi_input[1], tmp, len);
        /*父进程阻塞等待读入*/
        int n = read(cgi_output[0], buf, sizeof(buf));
        int ret = write(STDOUT_FILENO, buf, n);
        /*关闭管道*/
        close(cgi_input[1]);
        close(cgi_output[0]);
        waitpid(pid, &status, 0);
    }
    return 0;
}
```

## 多线程服务器

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <ctype.h>
#include <sys/epoll.h>
#include <errno.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <signal.h>
#include <dirent.h>
#include <sys/types.h>
#include <sys/wait.h>
#define SERV_PORT 9999
#define MAXSIZE 2048
void wait_child(int signo){
    while(waitpid(0, NULL, WNOHANG) > 0);
    return;
}
int createlistenfd(){
    struct sockaddr_in servaddr;
    int ret;
    int fd = socket(AF_INET, SOCK_STREAM, 0); //创建套接字
    if(fd == -1){
        perror("socket error");
        exit(1);
    }
    //初始化servaddr结构体
    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(SERV_PORT);
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    //端口复用
    int opt = 1;
    setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
    //绑定端口
    ret = bind(fd, (struct sockaddr *)&servaddr, sizeof(servaddr));
    if (ret == -1){
        perror("bind error");
        exit(1);
    }
    //设置监听上限
    ret = listen(fd, 128);
    if(ret==-1){
        perror("listen error");
        exit(1);
    }
    return fd;
}
void work(int cfd, char* s){
    char filename[100]={0};
    sscanf(s, "GET /%s", filename);
    char *mime;
    if(strstr(s, ".html")) mime = "text/html";
    else if(strstr(s, ".jpg")) mime="image/jpeg";
    //构建响应头 发给客户端
    // printf("%s\n", filename);
    char response[MAXSIZE];
    sprintf(response, "HTTP/1.1 200 OK\r\nContent-Type: %s\r\n\r\n", mime);
    //读取具体的文件内容
    int filefd = open(filename, O_RDONLY);
    if(filefd == -1){
        perror("open error");
        sleep(0.5);
        filefd = open(filename, O_RDONLY); //很奇怪 为什么睡几秒钟之后再打开就不会出错了
        if(filefd == -1) exit(1);
    }
    int len = strlen(response);
    int n = read(filefd, response+len, sizeof(response)-len); 
    write(cfd, response, len+n);
    close(filefd);
}
int main(void){
    int lfd = createlistenfd();
    struct sockaddr_in clientaddr;
    socklen_t clientaddrlen = sizeof(clientaddr); //这是一个传出参数
    //accept接受连接请求
    pid_t pid;
    int cfd;
    while(1){
        cfd = accept(lfd, (struct sockaddr *)&clientaddr, &clientaddrlen);
        if (cfd == -1){
            perror("accept error");
            exit(1);
        }
        //创建子线程 主线程负责监听和回收子进程
        pid = fork(); 
        if(pid < 0){
            perror("fork error");
            exit(1);
        }
        else if(pid == 0) break;
        else{
            close(cfd); //关闭接收文件描述符
            signal(SIGCHLD, wait_child);
        }
    }
    if(pid == 0){
        close(lfd); //关闭监听文件描述符
        //打印客户端IP和port
        char buf[MAXSIZE] = {0};
        printf("client IP: %s, client port: %d\n",
            inet_ntop(AF_INET, &clientaddr.sin_addr, buf, sizeof(buf)),
            ntohs(clientaddr.sin_port));
        int n = read(cfd, buf, sizeof(buf));
        if(n==0){
            close(cfd);
        }
        // write(1, buf, n);
        else work(cfd, buf);
    }
    return 0;
}
```

## 处理客户端注册信息的cgi

-   存在一些问题，每个网页好像没有传输完成，浏览器总是转圈。
-   需要结合上面hello程序查询数据库，hello程序的注册还没完善，只能做到查询。等以后有空再做吧。

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <ctype.h>
#include <assert.h>
#include <netinet/in.h>
#include <errno.h>
#include <string.h>
#include <pthread.h>
#include <fcntl.h>
#include <sys/epoll.h>
#include <sys/types.h>
#include <sys/wait.h>

#define MAX_SIZE 1024
//自定义的结构体
struct fds{
    int epollfd;
    int sockfd;
};
//设置文件描述符为非阻塞
void setnonblocking(int fd){
    int old_option = fcntl(fd, F_GETFL);
    int new_option = old_option | O_NONBLOCK;
    fcntl(fd, F_SETFL, new_option);
}
//添加到epoll内核事件表中
void addfd(int epollfd, int fd, bool oneshot){
    epoll_event event;
    event.data.fd = fd;
    event.events = EPOLLIN | EPOLLET;
    if(oneshot){
        event.events |= EPOLLONESHOT;
    }
    epoll_ctl(epollfd, EPOLL_CTL_ADD, fd, &event); //挂到红黑树上
    setnonblocking(fd); //设置非阻塞 主要用在读写上
}
//移除epoll事件
void removefd(int epollfd, int fd){
    epoll_ctl(epollfd, EPOLL_CTL_DEL, fd, NULL);
    close(fd);
}
//重置EPOLLONESHOT事件
void reset_oneshot(int epollfd, int fd){
    epoll_event event;
    event.data.fd = fd;
    event.events = EPOLLIN | EPOLLET | EPOLLONESHOT;
    epoll_ctl(epollfd, EPOLL_CTL_MOD, fd, &event); //修改注册事件
}
void accept_request(int epollfd, int sockfd, char *s){
    char method[32], filename[32], account[32], password[32], phone[32];
    sscanf(s, "%s /%s", method, filename);
    if(strcasecmp(method, "POST") == 0){
        int len = strlen(s);
        int i;
        for(i = 0; i < len; i++){
            if(i+2<len && s[i]=='\n' && s[i+1]=='\r') break;
        }
        int j;
        i=i+12;
        for(j = 0; s[i+j]!='&'; j++) account[j] = s[j+i];
        i = i+j+6;
        for(j = 0; s[i+j]!='&'; j++) password[j] = s[j+i];
        /*2020.4.7成功解析出来账号和密码*/
        pid_t pid; 
        int status;
        int cgi_input[2];
        int cgi_output[2];
        char buff[1024];
        /*创建输入管道*/
        if(pipe(cgi_input) < 0){
            perror("pipe error");
            exit(1);
        }
        /*创建输出管道*/
        if(pipe(cgi_output) < 0){
            perror("pipe error");
            exit(1);
        }
        /*创建子进程*/
        if((pid = fork()) < 0){
            perror("fork error!");
            exit(-1);
        }
        
        if(pid == 0){ 
            dup2(cgi_input[0], 0); /*将子进程的STDIN重定向到cgi_input[0]*/
            dup2(cgi_output[1], 1); /*将子进程的STDOUT重定向到cgi_output[1]*/
            /*关闭剩余的两端*/
            close(cgi_input[1]);
            close(cgi_output[0]);
            /*执行exec文件 即cgi*/
            execl("hello", "anythingok", NULL);
            exit(0);
        }else if(pid > 0){  /*父进程先给子进程发送数据 然后等待子进程执行完 再读数据*/
            /*关闭不用的两个端口*/
            close(cgi_input[0]); 
            close(cgi_output[1]);
            /*父进程先写数据*/
            int len = strlen(account);
            write(cgi_input[1], account, len);
            /*父进程阻塞等待读入*/
            int n = read(cgi_output[0], buff, sizeof(buff));
            if(strcmp(buff, password)==0&&strlen(password) != 0){
                puts("密码正确");
            }else{
                puts("密码错误");
                strcpy(filename, "register.html");
            }
            // int ret = write(STDOUT_FILENO, buf, n);
            /*关闭管道*/
            close(cgi_input[1]);
            close(cgi_output[0]);
            waitpid(pid, &status, 0);
        }


     }
    puts(filename);
    char mime[64];
    if(strstr(s, ".html")) strcpy(mime,"text/html");
    else if(strstr(s, ".jpg")) strcpy(mime,"image/jpeg");
    char response[MAX_SIZE+MAX_SIZE];
    sprintf(response, "HTTP/1.1 200 OK\r\nContent-Type: %s\r\n\r\n", mime);
    int filefd = open(filename, O_RDONLY);
    if(filefd == -1){
        perror("open error");
        exit(1);
    }
    int len = strlen(response);
    int n = read(filefd, response+len, sizeof(response)-len); 
    write(sockfd, response, len+n);
    close(filefd);
}

//工作线程
void* worker(void* arg){
    int sockfd = ((fds*)arg)->sockfd;
    int epollfd = ((fds*)arg)->epollfd;
    char buf[MAX_SIZE];
    memset(buf, '\0', MAX_SIZE);
    //循环读取sockfd上的数据 直到收到EAGAIN
    while(1){
        int ret = recv(sockfd, buf, MAX_SIZE-1, 0);
        if(ret == 0){
            removefd(epollfd, sockfd);
            printf("foreiner closed the connection\n");
            break;
        }else if(ret < 0){
            if(errno == EAGAIN){
                // reset_oneshot(epollfd ,sockfd);
                printf("read later\n");
                break;
            }
        }else{
            printf("get connection:\n");
            //休眠5s模拟数据处理过程
            accept_request(epollfd, sockfd, buf);
            sleep(5);
            break;
        }
    }
}
//命令行参数指定IP和端口
int main(int argc, char *argv[]){ 
    if(argc < 2){
        printf("at least 2 arguments: file port, but you give %d\n", argc);
        return 1;
    }
    int port = atoi(argv[1]);
	int lfd, cfd, ret;
	struct sockaddr_in serv_addr, clie_addr;
	lfd = socket(AF_INET, SOCK_STREAM, 0); //创建套接字
    assert(lfd >= 0);
	 /*初始化服务器端的套接字地址*/
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(port);
    serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    //端口复用 此处没有卵用
    int opt = 1;
    setsockopt(lfd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt)); 
	
    ret = bind(lfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr) );
    assert(ret != -1);
	ret = listen(lfd, 128); //最大同时连接数
    assert(ret != -1);
    epoll_event events[MAX_SIZE]; //返回的数组上限
    int epollfd = epoll_create(10);
    assert(epollfd != -1);
    //注意监听的套接字不能设置为oneshot
    addfd(epollfd, lfd, false); //挂上红黑树监听
    while(1){
        ret = epoll_wait(epollfd, events, MAX_SIZE, -1); //永远不超时
        if(ret < 0){
            printf("epoll failure\n");
            break;
        }
        for(int i = 0; i < ret; i++){ //循环处理有响应的事件
            int sockfd = events[i].data.fd;
            if(sockfd == lfd){ //如果是监听事件则建立新的连接
                socklen_t clie_addr_len; //套接字长度
                clie_addr_len = sizeof(clie_addr);
                cfd = accept(lfd, (struct sockaddr*)&clie_addr, &clie_addr_len );
                assert(cfd >= 0);
                //注册为oneshot事件
                addfd(epollfd, cfd, false); //刚刚这里加入的事件加错了
            }else if(events[i].events & EPOLLIN){
                pthread_t tid;
                fds fds_for_new_worker;
                fds_for_new_worker.epollfd = epollfd;
                fds_for_new_worker.sockfd = sockfd;
                //新启动一个线程为sockfd服务
                pthread_create(&tid, NULL, worker, (void*)&fds_for_new_worker);
                // pthread_detach(tid); //线程分离
            }
        }
    }
	close(lfd);
	return 0;
}

```

## 线程中调用fork函数

pthread_atfork函数确保fork调用后父进程和子进程都拥有一个清楚的锁状态。每个线程都可以独立的设置信号掩码。

## waitpid回收子进程

```c
#include <unistd.h>
#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
void sigchild_handler(int sig){
    //在执行SIGCHLD信号期间 可能有多个SIGCHLD到达，但是未决信号集只记录一次。
    //所以需要调用while循环回收再退出
    while(waitpid(-1, NULL, WNOHANG) > 0){
        puts("回收成功");
    }
    return;
}
int main(){
    pid_t pid;
    int n = 5, i;
    signal(SIGCHLD, sigchild_handler);
    for(i = 0; i < n; i++){
        pid = fork();
        if(pid < 0){
            perror("fork error");
            exit(1);
        }else if(pid == 0) break; //子进程 直接退出
    }
    if(i < n){ //子进程
        sleep(i);
        printf("I am %dth child.\n", i);
    }else{
        while(1){ //父进程不退出
            sleep(1);
            printf("I am parent %u\n", getpid());
        }
    }
    return 0;
}

```


## 条件变量
- 条件变量本身不是锁，但它可以造成线程阻塞。通常与互斥锁配合使用。给多线程提供一个汇合的场所。
```c
pthread_cond_wait(&cond, &mutex)
1. 阻塞等待该条件变量直到满足 
2. 释放已经掌握的互斥锁 
3. 满足条件后重新拿锁
```

