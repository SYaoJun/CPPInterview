package main

import (
	"fmt"
	"time"
)

func main(){
	go spinner(100*time.Microsecond)
	const n = 45
	fibN := fib(n)
	fmt.Printf("\rfib(%d) = %d\n", n, fibN)
}
func spinner(delay time.Duration){
	for {
		for _,r := range `-\|/`{
			fmt.Printf("\r%c",r)
			time.Sleep(delay)
		}
	}
}
func fib(n int)int{
	if n < 2{
		return 1
	}else{
		return fib(n-1)+fib(n-2)
	}
}