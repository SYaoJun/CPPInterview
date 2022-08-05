切片中存储map类型

```go
slice1 :=make([]map[string][string])
```

CSP: communicating  sequential process通信顺序进程

一种并发编程模型

goroutine和channel是golang并发编程的两大基石

不要通过共享内存来通信，而要通过通信来实现共享内存。

> Do not communicate by sharing memory; instead, share memory by communicating.

Go并发模型：G-P-M
## 1、同步等待组

```go
package main
/*
同步等待组：WaitGroup
*/
import (
	"fmt"
	"sync"
)
var wg sync.WaitGroup
func f1(){
	for i := 1; i < 10; i ++{
		fmt.Println(i)
	}
	wg.Done()
}
func f2(){
	for c :='a'; c < 'f'; c++{
		fmt.Printf("%c\n",c)
	}
	wg.Done()
}
func main(){
	wg.Add(2)
	go f1()
	go f2()
	wg.Wait()

}


```
## 2、通道

```go
package main

import "fmt"

/*
发送和接收默认是阻塞
  读：
	data, ok := <- ch
  写：
	ch <- data
*/
func main(){
	var ch chan bool
	ch = make(chan bool)
	go func(){
		for i := 0; i < 10; i ++{
			fmt.Println(i)
		}
		ch <- true
		fmt.Println("goroutine over...")
	}()
	data, ok := <- ch
	if !ok{
		fmt.Println("error")
	}
	fmt.Printf("main over...%t",data)

}


```
## 互斥锁

```go
package main

import (
	"fmt"
	"sync"
	"time"
)

var ticket int = 10
var wg sync.WaitGroup
var mutex sync.Mutex
func main(){
	wg.Add(4)
	go saleTicket("售票口1")
	go saleTicket("售票口2")
	go saleTicket("售票口3")
	go saleTicket("售票口4")
	wg.Wait()
}

func saleTicket(name string){
	defer wg.Done()
	for{
		mutex.Lock()
		if ticket > 0{
			time.Sleep(500*time.Millisecond)
			fmt.Println(name, ticket)
			ticket--
		}else{
			fmt.Println("卖完了...")
			mutex.Unlock()
			break
		}
		mutex.Unlock()
	}
}
```
## 4、range遍历通道

```go
package  main

import "fmt"

/*
	通过range访问通道
	goroutine执行完毕以后必须要关闭通道，不然会造成死锁
*/
func main(){
	ch := make(chan int)
	go sendData(ch)
	for value := range ch{
		fmt.Println(value)
	}
}

func sendData(ch chan int){
	for i:= 0; i < 10; i++{
		ch <- i
	}
	close(ch)
}
```
## 带缓冲区的通道

```go
package  main

import (
	"fmt"
	"time"
)

func main(){
	ch := make(chan int, 5) //带缓冲区的通道
	go sendData(ch)
	for value := range ch{
		fmt.Println("已经读取的数据",value)
		time.Sleep(1*time.Second)
	}

}

func sendData(ch chan int){
	for i:= 0; i < 10; i++{
		ch <- i
		fmt.Println("发送了数据",i)
	}
	close(ch)
}
```
## 5、定向通道

```go
package  main

import (
	"fmt"
)
/*
单向通道：即定向通道，只能发送或者接收数据。通常在创建类型时还是创建双向通道，
但是可以在函数内部限制只读和只写，用于保护数据。

*/
func main(){
	ch1 := make(chan int) //双向 可读 可写
	//ch2 := make(chan <- int) //单向 可写
	//ch3 := make(<-chan int) //单向 可读
	go sendData(ch1)
	for value := range ch1{
		fmt.Println(value)
	}
}

func sendData(ch chan <-int){ //函数内部可写
	for i:= 0; i < 10; i++{
		fmt.Println("发送了数据",i)
		ch <- i
	}
	close(ch)
}
```
## 6、定时器

```go
package  main

import (
	"fmt"
	"time"
)

func main(){
	// 1. 新建定时器
	timer := time.NewTimer(3*time.Second) //创建一个定时器 3秒之后触发
	//2020-07-24 16:09:02.555776 +0800 CST m=+0.000094274

	fmt.Println(time.Now())
	ch := timer.C
	// 阻塞3秒 打印时间
	fmt.Println(<-ch)
	// 2020-07-24 16:09:05.5563 +0800 CST m=+3.000641547

	// 2.在定时期间可以终止
	timer2 := time.NewTimer(5*time.Second)
	go func(){
		<-timer2.C
		fmt.Println("到时执行...goroutine")
	}()
	time.Sleep(3*time.Second)
	flag := timer2.Stop() //终止
	if flag{
		fmt.Println("timer2 终止了...")
	}
	// 3. 定时之后的时间NewTimer(d).C
	ch2 := time.After(2*time.Second)
	fmt.Println(<-ch2)

}


```
## 7、select语句

```go
package  main

import (
	"fmt"
)
//如果有多个可执行的select case则随机选
func main(){
	ch := make(chan int)
	ch2 := make(chan int)
	go func() {
		ch <- 100
	}()
	select {
	case num1 := <- ch:
		fmt.Println(num1)
	case num2 := <-ch2:
		fmt.Println(num2)
	default:
			fmt.Println("default...")
	}
}


```
