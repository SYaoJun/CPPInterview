package main

import "fmt"

func main(){
	/*数组*/
	var team = [...]string{"string", "solider", "mum"}
	for k, v:= range team{
		fmt.Println(k, v)
	}
	/*切片 动态分配大小的连续空间*/
	var strList [] string
	strList = append(strList, "hello")
	fmt.Println(strList)

}