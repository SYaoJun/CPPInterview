package main

import "fmt"

func main() {
	str2int := make(map[string]int)
	/*go中map的使用和C++的map几乎一样*/
	str2int["hello"] = 1
	str2int["world"] = 2
	fmt.Printf("output = %d\n", str2int["hello"])
	/*唯一不同 TODO: 判断是否存在*/
	if res, ok := str2int["hello"]; ok {
		fmt.Println(res)
	}
}
