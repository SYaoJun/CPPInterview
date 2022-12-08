## thread
1. pc
2. register
3. stack
## 线程与CPU
1. 一个CPU同一时间只能处理一个线程，但是可以通过调度，让每个线程都得到执行。
## multi-thread
1. event-driven programming
2. state machine
## 线程调度
1. 线程执行完自动让出cpu
2. 定时器中断，线程让出cpu
## 线程状态
- running
- runable
- sleeping
## 线程上下文切换
- 需要保存的数据
  1. 寄存器中的值
  2. PC
## 内核级线程
- 内核级线程可以共享内存