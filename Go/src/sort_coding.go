/*
牛客网考研题[成绩排序](https://www.nowcoder.com/practice/3f27a0a5a59643a8abf0140b9a8cf1f7?tpId=40&&tqId=21340&rp=1&ru=/activity/oj&qru=/ta/kaoyan/question-ranking)
*/
package main

import (
	"fmt"
	"sort"
)

type Student struct {
	id    int
	score int
}

func main() {
	var n int
	_, err := fmt.Scanf("%d", &n)
	if err != nil {
		return
	}
	ss := make([]Student, n)
	for i := 0; i < n; i++ {
		var x, y int
		_, err = fmt.Scanf("%d %d", &x, &y)
		if err != nil {
			return
		}
		ss[i] = Student{x, y}
	}
	sort.Slice(ss, func(i, j int) bool {
		if ss[i].score != ss[j].score {
			return ss[i].score < ss[j].score
		}
		return ss[i].id < ss[j].id
	})
	// 输出
	for i := 0; i < n; i++ {
		fmt.Println(ss[i].id, ss[i].score)
	}
}