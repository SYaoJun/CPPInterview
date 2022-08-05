# Basic Go
- 数组
- map
- string
- 方法
- 结构体
- 接口
## 数组

```go
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
```

## golang的坑
1. 同一个结构体可以实现多个接口
2. 子类接口可以转换为父类接口，反之不行。
3. slice传参数时新增失败

```go
package main

import "fmt"

func modifySlice(s []string){ //切片新增无效
	s[0] = "modify 123"
	s = append(s, "456")
}
func modifySliceNew(s []string)[]string{  //切片新增生效
	s[0] = "modify 123"
	s = append(s, "456")
	return s
}
func main(){
	s := []string{"123"}
	modifySlice(s)
	fmt.Println(s) //返回结果 [modify 123] 新增的数据没有生效 原因是传入的参数是指针的拷贝 但是新增数据是修改指针
	s = modifySliceNew(s)
	fmt.Printf("%v",s) //必须重新接收返回值 此时生效 因为修改的指针返回了
}
```
4. golang中的new和make区别。make是用来初始化map，slice，chan的。

```go
package main

import "fmt"

func main(){
	var a = new(int) // 得到一个int类型的指针
	*a = 10
	fmt.Println(*a)
	var c = new([10]int) // 创建一个数组
	c[0] = 11
	for _, v:= range c{
		fmt.Println(v)
	}
} 
```

## golang编程
1. fmt.Scanf() 只能读一行中的数据，遇到换行就结束。

2. 强类型语言。使用math库的时候必须把整型转换为浮点型，不能够隐式转换。
3. golang中不存在while循环，使用for循环代替
 ```go
   for i < 10{
     //当作while循环使用
   }
   for index, value := range(lst){
     	//index表示下标
       //value表示lst中具体的值 可以用到数组 切片 map 
   }
   //读入一行数据
   bf := bufio.NewReader(os.Stdin)
   s, _ := bf.ReadString('\n')
   fmt.Println(s)
   //最大值 最小值 取根号
   math.Max(a, b)
   math.Min(a, b)
   math.Sqrt(x)
   ```

4. rune可变，按照unicode输出

```go
s := "hello 中国"
a := []rune(s)
for c, v  := range(a){ //按照unicode编码 汉字也是对应一个rune
	fmt.Printf("%d %c\n", c, v)
	/*
	0 h
	1 e
	2 l
	3 l
	4 o
	5
	6 中
	7 国
	*/
}
```

5. byte可变，按照utf-8输出

```go
s := "hello 中国"
a := []byte(s)
for c, v  := range a { 
	fmt.Printf("%d %d\n", c, v)
	/*
	byte中的汉字被解码为3个字节
	0 104
	1 101
	2 108
	3 108
	4 111
	5 32
	6 228
	7 184
	8 173
	9 229
	10 155
	11 189
	*/
}
```

6. string不可变，当使用range遍历时，自动转换为[]rune

```go
s := "hello 中国"
for c, v  := range s {
	fmt.Printf("%d %c\n", c, v)
	/*
	string不可变，自动转换为[]rune但是下标按照汉字3个字节，没有改变。
	0 h
	1 e
	2 l
	3 l
	4 o
	5
	6 中
	9 国
	*/
}
```

7. golang中的交换很好用

```go
s[i], s[j] = s[j], s[i] 
```

8. golang自带的排序int和string，其他类型的结构体需要自己实现less, map,len三个函数。

```go
package main

import (
	"fmt"
	"sort"
)

type Student struct {
	name string
	age int
}
type stuSlice []Student
func (s stuSlice) Len() int{  //为什么这里需要重新取名
	return len(s)
}
func (s stuSlice) Less(i, j int) bool{
	return s[i].age < s[j].age
}

func (s stuSlice) Swap(i, j int){
	s[i], s[j] = s[j], s[i]
}
func main(){
	students := []Student{{"mike",16},{"jane",22},{"Ben",19}}
	sort.Sort(stuSlice(students))
	for k,v := range students{
		fmt.Println(k, v)
	}
	names := []string{"hello", "world", "yao", "jun"}
	sort.Strings(names)
	for k, v:= range names{
		fmt.Println(k, v)
	}
	ints := []int{1, 8, 4, 5}
	sort.Ints(ints)
	for k, v := range ints{
		fmt.Println(k, v)
	}
}
```

9. golang对slice逆序

```go
sort.Sort(sort.Reverse(stuSlice(students)))
```

10. rune和byte对应的关系

```go
rune = int32
byte = uint8
```

11. 字符串排序，注意需要把rune也即是int32的类型转换为char输出。

```go
package main

import (
	"fmt"
	"sort"
)
type runes []rune
func (r runes) Len()int{
	return len(r)
}
func (r runes) Swap(i, j int) {
	r[i], r[j] = r[j], r[i]
}
func (r runes) Less(i, j int)bool{
	return r[i] < r[j]
}
func main(){
	s := "bdca"
	ss := []rune(s)
	sort.Sort(runes(ss))
	for _,v := range ss{
		fmt.Printf("%c", v)
	}
}
```
12. map转换为json的序列化和反序列化
```go
package main

import (
	"encoding/json"
	"fmt"
)

func main(){
	//创建一个map
	mp := make(map[string]interface{})
	mp["company"] = "itcast"
	mp["subjects"] = []string{"C++", "python", "java", "go"}
	mp["isok"] = true
	mp["price"] = 998
	//编码成json
	//res, _ := json.Marshal(mp)
	res, _ := json.MarshalIndent(mp, ""," ")
	fmt.Println(string(res))
	//把string类型的json转换为map
	m := make(map[string]interface{}, 4)
	err := json.Unmarshal(res, &m)
	if err != nil{
		fmt.Println("err")
	}
	fmt.Println(m) //map[company:itcast isok:true price:998 subjects:[C++ python java go]]
	for k, v := range m{
		fmt.Printf("%s : %v\n", k, v) //map是无序的，如何做到让每次结果输出的顺序相同呢
	}

}
```
13. 常用的占位符
```go
%v    值的默认格式表示。当输出结构体时，扩展标志（%+v）会添加字段名
%#v   值的Go语法表示
%t    单词true或false
%c    该值对应的unicode码值
%q    该值对应的单引号括起来的go语法字符字面值，必要时会采用安全的转义表示
%p    表示为十六进制，并加上前导的0x
```
14. map的删除，delete函数
```go
package main

import "fmt"

func main(){
	//创建一个map
	mp := make(map[string]interface{})
	mp["company"] = "itcast"
	mp["subjects"] = []string{"C++", "python", "java", "go"}
	mp["isok"] = true
	mp["price"] = 998
	//map的删除 delete函数
	delete(mp, "price")
	for k, v:=range mp{
		fmt.Println(k, v)
	}
}
```
15. slice的删除三种方式
```go
package main

import (
	"fmt"
)

func main(){
	//创建一个map
	sliceU := []int{1, 0, 1, 1, 0, 1, 0, 1, 1}
	//slice的删除方式1  效率巨低
	//删除剩余的元素往前移动 
	for i, v := range sliceU{
		if v == 0 {
			sliceU = append(sliceU[:i], sliceU[i+1:]...)
		}
	}
	fmt.Println(sliceU)
	//slice的删除方式2 效率次之
	//重新开一个数组，把满足条件的往新数组中写入
	var newSliceU []int
	for _, v := range sliceU{
		if v != 0 {
			newSliceU = append(newSliceU, v)
		}
	}
	fmt.Println(newSliceU)
	// slice的删除方式3 效率最高
	// 索引累计 最后切片
	index := 0
	for _, v := range sliceU{
		if v != 0 {
			sliceU[index] = v
			index++
		}
	}
	fmt.Println(newSliceU[:index])
}
```
## goroot和gopath
1. Goroot是存放go编译器的位置
2. Gopath是存放源代码的位置。gopath下必须有三个目录，src, pkg, bin如果是从外部导入的代码，需要放在src目录下，比如$gopath/src/github.com
## go面向对象

- 封装
- 继承
- 多态

匿名字段：只提供类型，而不写字段名的字段

## http服务器
```go
package main

import "net/http"

func HandleCon(w http.ResponseWriter, req *http.Request){
	w.Write([]byte("hello go"))
}
func main(){
	http.HandleFunc("/", HandleCon)  //注册回调函数
	http.ListenAndServe(":8000",nil)  //绑定端口

}
```

在服务端打断点才能看到实际运行
## init函数
init函数有一下几点特性:

- init函数在main执行之前，自动被调用执行的，不能显示调用
- 每个包的init函数在包被引用时，自动被调用
- 每个包可以有多个init函数
- 同一个文件中可定义多个init()函数

## map转json

```go
//map转json
	m := map[string][]string{
		"level":{"debug"},
		"message":{"File not found", "stack overflow"},
	}
	//将map解析成Json格式
	if data, err := json.Marshal(m); err == nil{
		fmt.Printf("%s\n",data)
	}
```

## 结构体转json

```go
package main

import (
	"encoding/json"
	"fmt"
)
//变量名必须大写
type IT struct {
	Company string `json:"company"`
	Subject []string`json:"subjects"`
	Isok bool `json:"-"`  //不输出
	Price float64 `json:",string"`
}

func main() {
	//定义一个结构体变量 同时初始化
	s :=IT{"itcast", []string{"GO","C++","Python","Java"}, true, 666.66}
	//编码 根据内容生成Json文本
	//buf, err := json.Marshal(s)
	buf, err := json.MarshalIndent(s,"","	")

	if err != nil{
		fmt.Printf("error ", err)
	}
	fmt.Printf("%+v", string(buf))
}
```

## map转json

```go
func main() {
	//创建一个map
	m := make(map[string]interface{}, 4)
	m["company"]="itcast"
	m["subjects"]=[]string{"GO","C++","Java"}
	m["isok"]=true
	m["price"]=666.666

	//编码成json
	//result, err := json.Marshal(m)
	result, err := json.MarshalIndent(m,"","	")
	if err != nil{
		fmt.Printf("error",err)
		return
	}
	fmt.Printf("result = %v", string(result))
}
```
## 方法和函数
[黑马视频](https://www.bilibili.com/video/BV1P4411M7Pt?p=148)
方法是一个包含了接收者的函数，指定了调用者，对象或指针，方法的名字可以相同，但是接收者必须不同。

>对比函数：
A：意义
方法：某个类别的行为功能，需要指定的接收者调用。
函数：一段独立功能的代码，可以直接调用。
B：语法：
方法：方法名可以相同，只要接收者不同。
函数：命名不能冲突

```go
package main

import "fmt"
//定义结构体
type Worker struct{
	name string
	age int
	sex string
}
//定义结构体
type Cat struct{
	name string
	age int
}
//定义方法
func (w Worker) work(){
	fmt.Println(w.name, "在工作")
}
//定义方法
func (p *Worker) rest(){
	fmt.Println(p.name, "在休息")
}

func(p * Worker) printInfo(){
	fmt.Printf( "%+v\n",p)
}
func(p * Cat) printInfo(){
	fmt.Printf( "%+v\n",p)
}
func main() {
	w := Worker{name: "yao jun", age: 14, sex: "male"}
	w.work()
	w.rest()
	w.printInfo()
	c := Cat{"tian tian", 18}
	c.printInfo()
}

```

## 继承

使用结构体嵌套，模拟继承。

```go
package main

import "fmt"

//1. 父类
type Person struct{
	name string
	age int
}
//2. 子类
type Student struct{
	Person //结构体嵌套 模拟继承性
	school string
}
//3. 父类方法
func (p *Person) eat(){
	fmt.Println("父类吃窝窝头...")
}
//4. 子类新增方法
func (s *Student) study(){
	fmt.Println("子类学习...")
}
//5. 子类重写父类方法
func (s *Student) eat(){
	fmt.Println("子类吃炸鸡...")
}
func main(){
	p := Person{"yao jun", 19}
	p.eat()

	s := Student{p, "重庆大学"}
	s.eat() //重写父类方法
	fmt.Println(s.name) //s.Person.name 子类直接访问父类的字段 提升字段
	s.study()
}
```



## 接口

功能的定义和实现分类，解耦合。

```go
package main

import "fmt"
//1. 定义接口
type USB interface {
   start()
   end()
}
//2. 定义实现类
type Mouse struct{
   name string
}
type FlaskDisk struct{
   name string
}
//这里只能是对象 不能是指针
func (m Mouse) start(){
   fmt.Println("鼠标开始")
}
func (m Mouse) end(){
   fmt.Println("鼠标结束")
}
func (f FlaskDisk) start(){
   fmt.Println("U盘开始")
}
func (f FlaskDisk) end(){
   fmt.Println("U盘结束")
}
//3. 测试方法
func testInterface(usb USB){
   usb.start()
   usb.end()
}
func main(){
   m := Mouse{"罗技"}
   f := FlaskDisk{"闪迪"}
   m.start()
   m.end()

   f.start()
   f.end()
   fmt.Println(m.name)
   testInterface(m)
   testInterface(f)
   var usb USB
   usb = m
   testInterface(usb)
   usb.start()
   usb.end()
   //fmt.Println(usb.name) 接口对象不能方位实现类中的属性
}
```



## 多态

1.  子类是一个特殊的父类类型，可以看作父类对象
2.  子类可以看作子类对象

一个函数如果接受接口类型作为参数，那么实际上可以传入接口的任意实现类型对象作为参数。定义一个类型为接口类型，实际上可以赋值为任意实现类的对象。

鸭子类型：dock type

www.json.cn检查json格式

1.  通过结构体生成json
2.  通过map生成json

结构体变量名首字母必须大写

## 函数

```go
package main

import "fmt"
//不定参  函数
func ff(args ...int){
	for i := 0; i < len(args); i++{
		fmt.Printf("args[%d] = %d\n", i, args[i])
	}
}
func main(){
	ff(1,3,5)
}
```

println和printf的区别

```go
a := 100
fmt.Println("a = ",a) //一段一段处理 自动换行
fmt.Printf("a = %d\n", a) //格式化处理
```

匿名变量 配合函数返回值 才有优势

函数类型（对应于C函数指针）

```go
package main

import "fmt"

func add(a, b int) int{
	return a+b
}
func sub(a, b int) int{
	return a - b
}
type FuncType func(a, b int) int
func main(){
	//函数也是一种数据类型，通过type给一个函数类型起名 必须要有同样的参数和返回值
	var fTest FuncType //声明一个函数类型的变量
	//指向加法
	fTest = add
	res := fTest(4, 6)
	fmt.Println(res)
	//指向减法  实现多态
	fTest = sub
	res = fTest(88,66)
	fmt.Println(res)
}
```

回调函数：函数有一个参数是函数类型

```go
package main

import (
	"fmt"
)

func add(a, b int) int{
	return a+b
}
func sub(a, b int) int{
	return a - b
}
type FuncType func(a, b int) int
func calc(a, b int, fTest FuncType)(result int){
	fmt.Printf("calc = ")
	result = fTest(a, b)
	fmt.Println(result)
	return
}
func mul(a, b int)int{
	return a*b
}
func div(a, b int)int{
	if b==0{
		panic("除数为0")
	}
	return a/b
}
func main(){
	calc(5,6,add)
	calc(5,2, sub)
	calc(4,3, mul)
	calc(6,2, div)
}
```

匿名函数：不需要定义函数名的一种函数实现

闭包：一个函数捕获了和它在同一作用域的其他常量和变量。

```go
func main(){
	a := 10
	b := 20
	//匿名函数
	f := func()int {
		fmt.Println(a+b)
		return a+b
	}
	f()
	//定义匿名函数 同时调用
	func(c int) int{
		fmt.Println(a-b+c)
		return a - b + c
	}(5)      //立即执行函数
}
```

闭包以引用方式捕获外部变量 内部变 外部也跟着变。只要闭包还在使用，捕获的变量就会一直存在，闭包里面变量的生命周期不是由它的作用域决定的。

```go
package main

import "fmt"

func test() func()int{
	var x int
	return func() int {
		x++
		return x*x
	}
}
func main(){
	f := test()
	fmt.Println(f())
	fmt.Println(f())
	fmt.Println(f())
	fmt.Println(f())
}
```

## 字符串常用API

```go
package main

import (
	"fmt"
	"strings"
)

func main(){
	//Contains包含
	fmt.Println(strings.Contains("hellogo", "hello")) //判断是否包含
	//Join拼接
	s := []string{"abc", "hello", "world", "go"}
	fmt.Println(strings.Join(s, "_"))
	//Index索引
	fmt.Println(strings.Index("helloWorld","World"))
	//Repeat重复拼接
	fmt.Println(strings.Repeat("abc", 3))
	//Split分割
	fmt.Println(strings.Split("hello go world"," "))
	//Trim去掉两头空格
	fmt.Println(strings.Trim("   hello world  ", " "))
	//Fields提取单词 空格分割
	fmt.Println(strings.Fields("hello world are you ok!"))
}
```

其他类型转换为字符串

```go
package main

import (
	"fmt"
	"strconv"
)

func main(){
	var str string
	str = strconv.FormatInt(44,32)
	fmt.Println(str)
	//整型转字符串
	str = strconv.Itoa(19)
	fmt.Println(str)
	//字符串转整形
	a,_ := strconv.Atoi("234")
	fmt.Println(a)
}
```

## 正则表达式

```go
package main

import (
	"fmt"
	"regexp"
)

func main(){
	buf := "abc azc atc a2c a4c at"
	//解释器
	reg := regexp.MustCompile(`a.c`)
	if reg == nil{
		panic("reg error")
	}
	//根据规则提取信息
	res := reg.FindAllStringSubmatch(buf,-1)
	fmt.Println(res)
}
```

## 反转字符串

```go
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main(){
	//反转字符串
	bf := bufio.NewReader(os.Stdin)
	ss, _ := bf.ReadString('\n')
	res := strings.Fields(ss)
	n := len(res)
	for i := 0; i < n/2; i++{
		res[i], res[n-1-i] = res[n-1-i], res[i]
	}
	for i := 0; i < n; i++{
		if i!= n-1{
			fmt.Printf("%s ", res[i])
		}else{
			fmt.Printf("%s\n", res[i])
		}
	}
}
```
资源管理和出错处理
defer是一个栈，后出现的defer先执行，先进后出。

## 测试
go test .
```go
package awesomeProject

import "testing"

/*传统测试
1. 测试数据和测试逻辑混在一起
2. 出错信息不明确

表格驱动测试
1. 测试数据和逻辑分离
2. 明确的出错信息
3. 可以部分失败
4. GO语言的语法使表格驱动测试更适合
*/
func TestAdd(t *testing.T){
	tests := [] struct{a, b, c int}{
		{3, 4, 7},
		{5, 7, 12},
		{8, 11, 19},
	}

	for _, tt := range tests{
		if actual := add(tt.a, tt.b); actual != tt.c{
			t.Errorf("add(%d, %d); actual is %d, expected %d\n", tt.a, tt.b, actual,tt.c)
		}
	}
}

//同目录下的函数
package awesomeProject
func add(a, b int)int{
	return a+b
}
```

## duck typing
描述事物的外部行为而非内部结构。像鸭子走路，长得像鸭子，那就是鸭子。
接口由使用者定义。使用者download，实现者retriever。实现者不需要说我实现了哪个接口，只要实现接口里的方法。由使用者规定实现者必须有某个方法。

```go
package main

import (
	"fmt"
	"net/http"
	"net/http/httputil"
)

type Retriever interface {  //定义一个接口 和一个方法
	Get(url string) string
}
func download(r Retriever) string{ //这是一个函数 参数是接口 必须要事先实现接口中的方法
	return r.Get("http://www.imooc.com")
}
type Retrieve struct { //这是一个结构体 让这个结构体来实现接口中的方法
	content string
}

func (r Retrieve) Get(url string) string{ //实现的方法
	resp, err := http.Get(url)
	if err != nil{
		panic(err)
	}
	result, err := httputil.DumpResponse(resp, true)
	defer resp.Body.Close()
	if err!= nil{
		panic(err)
	}
	return string(result[:100])
}

func main() {
	var r Retrieve
	r = Retrieve{"fasdf"}
	fmt.Println(download(r))
}
```

可以把实现类结构体赋值给对应的接口。即使实现的方法是值类型，但是传递的时候可以传值也可以传指针，语法糖。但是指针类型实现的方法，不能传值类型。
接口是种类型。任何类型都实现了空接口。
子类接口可以转换为父类接口，反之不行。

```go
package main

import (

	"fmt"
)

type Human interface {  //父
	hello()
}

type Person interface { //子
	Human
	sing(lrc string)
}

type Student struct {
	name string
	age int
}

func main() {
	var ip Person
	var ih Human
	ih = ip //子接口 可以转换为 父接口
	fmt.Println(ih)
}
```

## 空接口的类型断言

### if断言

```go
package main

import "fmt"

type Student struct {
	name string
	age int
}

func main() {
	m := make([] interface{}, 3)
	m[0] = 1 //int
	m[1] = "hello go" // string
	m[2] = Student{"mike", 666} //Student
	//类型断言 第一个返回下标 第二个返回下标对应的值
	for index, data := range m{
		//第一个返回值 本身
		//第二个返回值 真假
		if value, ok := data.(int); ok==true{
			fmt.Printf("m[%d] = %d\n", index, value)
		} else if value, ok := data.(string); ok==true{
			fmt.Printf("m[%d] = %s\n", index, value)
		} else if value, ok := data.(Student); ok{
			fmt.Printf("m[%d] = %v\n", index, value)
		}
	}

}
```

### switch断言

```go
package main

import "fmt"

type Student struct {
	name string
	age int
}

func main() {
	m := make([] interface{}, 3)
	m[0] = 1 //int
	m[1] = "hello go" // string
	m[2] = Student{"mike", 666} //Student
	//类型断言 第一个返回下标 第二个返回下标对应的值
	for index, data := range m{
		switch value := data.(type) {
		case  int:
				fmt.Printf("m[%d] = %d\n", index, value)
		case string:
			fmt.Printf("m[%d] = %s\n", index, value)
		case Student:
			fmt.Printf("m[%d] = %v\n", index, value)
		}

	}

}
```

## 实现接口

同一个结构体可以实现多个接口

接口可以嵌套

```go
package main

import "fmt"

type animal interface {
	mover
	eater
}
type mover interface {
	move()
}
type eater interface {
	eat()
}
type Cat struct {
	name string
	feet int8
}
//Cat实现了mover接口
func (c *Cat) move(){
	fmt.Printf("走猫步...")
}
//Cat实现了eater接口
func (c * Cat) eat(){
	fmt.Println("猫吃鱼...")
}

func main() {
	
}
```

go语言的接口的独特之处在于，它是隐式实现。对于一个具体的类型，无须声明它实现了哪些接口，只要提供接口所必须的方法即可。

如果一个类型实现了一个接口要求的所有方法，那么这个类型实现了这个接口。

接口赋值：仅当一个表达式实现了一个接口， 这个表达式才可以赋给该接口。

Go语言中，还可以使用new关键字对类型（包括结构体、整型、浮点数、字符串等）进行实例化，结构体在实例化后会形成指针类型的结构体。

我们在实现File的时候，可能并不知道上面4个接口的存在，但不管怎样，File实现了上面所有的4个接口。我们可以将File对象赋值给上面任何一个接口。

File在实现的时候，并不需要指定实现了哪个接口，它甚至根本不知道这4个接口的存在。

我们可以将一个实现接口的对象实例赋值给接口，也可以将另外一个接口赋值给接口。

## sort自定义排序

1. 排序字符串数组string

```go
package main

import (
	"fmt"
	"sort"
)

type StringSlice []string
func(p StringSlice) Len()int{
	return len(p)
}
func(p StringSlice) Less(i, j int)bool{
	return p[i] < p[j]
}

func(p StringSlice) Swap(i, j int){
	p[i],p[j] = p[j],p[i]
}
func main(){
	names :=[]string{"yao","jun","ni","hao"}
	//sort.Sort(StringSlice(names))
	sort.Strings(names)  //字符串slice的排序
	fmt.Println(names)
}
```

2. 排序整型数组int

```go
package main

import (
	"fmt"
	"sort"
)

type intSlice []int
func(p intSlice) Len()int{
	return len(p)
}
func(p intSlice) Less(i, j int)bool{
	return p[i] < p[j]
}

func(p intSlice) Swap(i, j int){
	p[i],p[j] = p[j],p[i]
}
func main(){
	ints := []int{1,4,3,2,3,6,9,10}
	//sort.Ints(ints) ^^+R
	sort.Sort(intSlice(ints))
	fmt.Println(ints)
}
```

3. 结构体排序struct

最核心是实现比较函数

```go
package main

import (
	"fmt"
	"sort"
)
type Student struct{
	name string
	age int
}
type stuSlice []Student
func(p stuSlice) Len()int{
	return len(p)
}
func(p stuSlice) Less(i, j int)bool{
	return  p[i].age < p[j].age || p[i].age==p[j].age && p[i].name < p[j].name
}

func(p stuSlice) Swap(i, j int){
	p[i],p[j] = p[j],p[i]
}
func main(){
	students := []Student{{"mike",16},{"jane",22},{"Ben",19}}
	sort.Sort(stuSlice(students))
	fmt.Println(students)
}
```
- 切片重载Less匿名函数排序

```go
package main

import (
	"fmt"
	"sort"
)

type Stu struct {
	Age int
}

func main() {
	// 对整数排序
	intSlice := []int{1, 4, 3, 2, 3, 6, 9, 10}
	sort.Ints(intSlice)
	fmt.Println(intSlice)
	// 对字符串排序
	names := []string{"yao", "jun", "ni", "hao"}
	sort.Strings(names)
	fmt.Println(names)
	// 对自定义类型排序 切片可以直接赋值
	stuSlice := make([]Stu, 5)
	stuSlice[0] = Stu{19}
	stuSlice[1] = Stu{11}
	// 传入匿名比较函数
	sort.Slice(stuSlice, func(i, j int) bool {
		return stuSlice[i].Age < stuSlice[j].Age
	})
	fmt.Println(stuSlice)

}

```

4. 牛客网考研题[成绩排序](https://www.nowcoder.com/practice/3f27a0a5a59643a8abf0140b9a8cf1f7?tpId=40&&tqId=21340&rp=1&ru=/activity/oj&qru=/ta/kaoyan/question-ranking)

```go
package main

import (
	"fmt"
	"sort"
)
type Student struct{
	id int
	score int
}
type stuSlice []Student
func(p stuSlice) Len()int{
	return len(p)
}
func(p stuSlice) Less(i, j int)bool{
	return  p[i].score < p[j].score || p[i].score==p[j].score && p[i].id < p[j].id
}

func(p stuSlice) Swap(i, j int){
	p[i],p[j] = p[j],p[i]
}
func main(){
	var a,b,n int
	fmt.Scanf("%d", &n)
	var students []Student
	for i:= 0;i < n ;i++{
		fmt.Scanf("%d %d", &a, &b)
		students = append(students, Student{a,b})
	}
	sort.Sort(stuSlice(students))
	for i:= 0; i < n; i++{
		fmt.Printf("%d %d\n", students[i].id, students[i].score)
	}
}
```
- 另外一种解法

```go
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

```

5. 逆序操作

```go
sort.Sort(sort.Reverse(stuSlice(students)))
```

## goroutine并发

1.计算和动画同时执行

```go
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
```

2. 打印数字和字母

当新的goroutine开始时，goroutine调用立即返回。与函数不同，go不等待goroutine执行结束，当goroutine调用，并且goroutine的任何返回值被忽略之后，go立即执行到下一行代码。

main的goroutine应该为其他的goroutines执行，如果main的goroutine终止了，程序将被终止，而其他goroutine将不会继续执行。

goroutine在64位计算机申请栈空间1GB

多个goroutine可以使用睡眠时长来人工设定goroutine顺序执行

```go 
package main

import (
	"fmt"
	"time"
)

func main(){
	go hello()
	for i := 0; i < 100; i++{
		fmt.Printf("In main A %d\n", i)
	}
	//等待go协程执行完毕 两个协程交替执行 没有顺序限制
	time.Sleep(time.Second*1)
	fmt.Println("main over...")
}
func hello(){
	for i := 0; i < 100; i++{
		fmt.Printf("In hello %d\n", i)
	}
}
```

3. 并发调度

g-p-m模型 runtime.h

Sched   proc.c

Goroutine machine processor

如果两个M在同一个CPU上运行就是并发，如果在不同CPU上运行就是并行。

4. chan通道

```go
package main

import (
	"fmt"
)

func main(){
	var ch chan bool
	ch = make(chan bool)
	go func() {
		for i := 0; i < 10; i++{
			fmt.Printf("in goroutine %d \n", i)
		}
		ch<-true //写入通道
		fmt.Println("in goroutine over...")
	}()
	data := <-ch  //读出通道的值
	fmt.Println("main over...", data)
}
```

5. chan阻塞读取

```go
package main

import (
	"fmt"
)

func main(){
	ch := make(chan int)
	go func() {
		for i := 0; i < 10; i++{
			fmt.Printf("in goroutine %d \n", i)
		}
		data := <- ch //从ch中读入数据
		fmt.Println("in goroutine over...", data)
	}()
	ch <- 10
	fmt.Println("main over...")
}
```

## select语句

```go
package main

import (
	"fmt"
	"time"
)
//每个case都必须是一个通信
//所有Chanel表达式都会被求值
//所有被发送的表达式都会被求值
//如果有多个表达式可以运行，select会随机公平地选出一个执行，其他不会执行。
//否则：如果有default子句，则执行该语句。如果没有default子句，select将阻塞，直到某个通信可以运行，go不会重新对channel或值进行求值。
func main(){
	ch1 := make(chan int)
	ch2 := make(chan int)
	go func() {
		time.Sleep(3*time.Second)
		ch1<-100
	}()
	go func() {
		time.Sleep(3*time.Second)
		ch2<-200
	}()
	select {
	case num1 := <-ch1:
		fmt.Println("ch1中获取到的数据...",num1)
		case num2, ok := <-ch2:
			if ok{
				fmt.Println("ch2中读取的数据...",num2)
			}else{
				fmt.Println("ch2通道已关闭...")
			}
	default:
		fmt.Println("default语句...")
	}
	fmt.Println("main over...")
}
```


## ID生成 雪花算法

https://github.com/bwmarrin/snowflake

```
package main

import (
	"fmt"
	"snowflake"
)

func main(){
	var n, _ = snowflake.NewNode(1)

	for i := 0; i < 3; i++{
		id := n.Generate()
		fmt.Println("id = ", id)
		fmt.Println(
			"node:", id.Node(),
			"step:", id.Step(),
			"time:", id.Time(),
			)
	}
}
```

## 注意点

1. 数组是值传递

```go 
package main

import "fmt"
//数组是值传递，无法通过修改数组类型的参数返回结果
func main(){
	x := [3]int{1,2,3}
	func(arr [3]int){
		arr[0] = 7
		fmt.Println(arr)
	}(x)
	fmt.Println(x)
}
```

2. map遍历时顺序不固定，是哈希表。

3. recover必须在defer函数中运行
4. main函数提前退出，无法保证后台的goroutine正常完成。
5. Goroutine是协作式抢占调度，Goroutine本身不会主动放弃CPU，可能会有goroutine独占CPU导致其他goroutine饿死。
6. Go语言带有内存自动回收的特性，因此内存一般不会泄漏。但是Goroutine确实存在泄漏的情况，同时泄漏的Goroutine引用的内存同样无法被回收。

## 自重写

```go
/*Go quine */
package main

import "fmt"

func main(){
	fmt.Printf("%s%c%s%c\n",q,0x60,q,0x60)
}
var q = `/* Go quine */
package main
import "fmt"
func main(){
	fmt.Printf("%s%c%s%c\n",q,0x60,q,0x60)
}
var q=`
```

## RPC

满足Go语言的RPC规则：方法只能有两个可序列化的参数，其中第二个参数是指针类型，并且返回一个error类型，同时必须是公开的方法。

array的长度是类型的一部分

[3]int 和 [4]int 是不同的类型

slice 本质也是传值，但看起来像传递了底层数组的引用
## 协程 corotine

1. 轻量级“线程”

2. 非抢占式多任务处理，由协程主动交出控制权

3. 编译器/解释器/虚拟机层面的多任务

4. 多个协程可能在一个或多个线程上运行

   ```go
   runtime.Gosched() //主动交出协程的控制权
   ```

   main函数也是一个协程

   main 和 dowork双向通信

   python 3.5 加入了async def对协程原生支持。使用yield关键字实现协程。

## goroutine的定义

1. 任何函数只需加上go就能送给调度器运行
2. 不需要在定义时区分是否是异步函数
3. 调度器在合适的点进行切换
4. 使用-race来检测数据访问冲突

## goroutine可能的切换点

1. IO和select
2. channel
3. 等待锁
4. 函数调用（有时）
5. Runtime.Gosched()

[视频链接](https://www.bilibili.com/video/BV1XA411q7sd?p=43)

## package

包内的函数必须首字母大写才可以被外部的包调用到，小写是调用不到的。

## init方法

- 在main函数被执行之前，所有依赖package的init方法都会被执行

- 不同包的init函数按照包导入的依赖关系决定执行顺序
- 每个包可以有多个init函数
- 包的每个源文件也可以有多个init函数，这点比较特殊。按照init的先后顺序执行。

## 协程

Thread VS Coroutine

1. 创建时默认的stack的大小

- JDK5以后Java Thread stack 默认为1M
- Goroutine的stack初始化大小为2K

2. 和KSE(kernel space entity)的对应关系

- java thread 是1:1
- Goroutine是M:N

[协程机制](https://www.bilibili.com/video/BV1RE411g7Ku?p=23)

## Go Test

通常test文件的命名规范是xxx_test.go

test case的函数命名为TestXxx形式 否则go test会跳过该test不执行

- t *testing.T 普通测试函数

- b*testing.B benchMark测试

```go
go test -v 输出test的详细信息
go test hello_test.go 输入某个特定的test
```

新建一个工程 使用go mod管理 初始化一个mod

```go
go mod init
```

三个文件

```shell
haha.go
haha_test.go
go.mod
```

```go
//haha.go
package main

func F(a,b int)int{
	return a+b
}
//haha_test.go
package main

import (
	"testing"
)

func TestF(t *testing.T){
	res := F(3,4)
	if res != 7{
		t.Errorf("add wrong!")
	}
}
//go.mod
module code.byted.org/ee/test

go 1.14
```

t.SkipNow()为跳过当前test，并且直接按pass处理继续下一个testcase

```go
func TestF(t *testing.T){
	t.SkipNow() //直接跳过这个test case的测试 并PASS
	res := F(3,4)
	if res != 20{
		t.Errorf("add wrong!")
	}
}
```

Go test不保证多个test按照顺序执行，但是我们通常会要求按照顺序执行。

使用t.Run来执行subtests可以做到控制test执行的顺序

```go
func TestF(t *testing.T){
	t.Run("a1", func(t *testing.T) {fmt.Println("a1")})
	t.Run("a2", func(t *testing.T) {fmt.Println("a2")})
	t.Run("a3", func(t *testing.T) {fmt.Println("a3")})
}
```



使用TestMain作为初始化test，并且使用m.Run()来调用其他tests可以完成一些需要初始化操作的testing，比如数据库连接，文件打开，rest服务登录等。

如果没有在TestMain中调用m.Run()则除了TestMain以外的其他tests都不会被执行

```go
func TestMain(m *testing.M){
	fmt.Println("test main first")
	m.Run()
}
```

## benchmark

benchmark函数一般以BenchMark开头

benchmark函数的case一般会跑b.N次，而且每次执行都会如此

在执行过程中会根据实际case的执行时间是否稳定会增加b.N的次数以达到稳态

```go
go test -bench=.  //命令行
```

```go
func BenchmarkF(b *testing.B) {
	for i:=0; i < b.N; i++{
		F(100,10)
	}
}
```

benchmark也会受限于m.Run()

如果benchmark测试的函数执行时间始终无法趋于稳态 则永远无法执行完

```go
func unstable(n int){
	for n > 0{
		n--
	}
}
func BenchmarkF(b *testing.B) {
	for i:=0; i < b.N; i++{
		unstable(i)  //如果benchmark测试的函数执行时间始终无法趋于稳态 则永远无法执行完
	}
}
```

## http server

[视频链接](https://www.bilibili.com/video/BV1T5411x7Uf?p=169)

```go
package main

import (
	"net/http"
)
//w 写回给客户端的数据  r 从客户端读入的数据
func handler(w http.ResponseWriter, r *http.Request){
	w.Write([]byte("hello world"))
}
func main(){
	//注册回调函数
	http.HandleFunc("/hello", handler)
	//绑定监听地址
	http.ListenAndServe("127.0.0.1:8000", nil)

}

```
## 切片
为什么用切片？

- 数组的容量固定，不能自动拓展。
- 值传递。数组作为函数参数时，将整个数组值拷贝一份给形参。


## 1、python2和python3的bytes
```py
if __name__ == '__main__':
	ss = 'terry0609_08\x04\x04\x04\x04'
		print(type(ss))
	 	print(ss[-1])
	 	print(ss[-2]) 	
```
python3中bytes可以是任何二进制数据，文本/图片/视频/音频等等。str就是文本数据。

	python2中把b'abcd'视为str，对str的切片是把\x04当作1位，数字8被视为unicode即char，输出的就是'8'。
	python3中对bytes的切片是把\x04当作1位，数字8被视为utf-8的int，输出的都是数值56。

**出错的代码**


```python
def  unpadding(self, s):
	return s[0:-ord(s[-1])]
```

出错代码原因分析：

      没有注明类型，不能进行类型的判读，代码的写法比较trick。

python3中bytes和str的转换


```python
b = b"example" # bytes object  
s = "example"  # str object  
s2b = bytes(s, encoding = "utf8")    # str to bytes 
s2b = str.encode(s) # str to bytes 
s2b = s.encode("utf8") # str to bytes 
b2s = str(b, encoding = "utf8")      # bytes to str  
b2s = bytes.decode(b) #  bytes to str  
b2s = b.decode("utf8") #  bytes to str  
```

*   bytes不一定能变成str,当bytes是图片，视频等非文本的二进制内容时，bytes就不能decode成str了。

## 2、typing标注类型和类型别名

python3.5 以后的新特性

​typing​模块的作用：

*   类型检查，防止运行时传入参数不符合。

*   作为开发文档附加说明，方便使用者调用传入和返回类型。

*   如果传入参数类型不匹配会报错【IDE层面的报错】。


```python
def  func(name: str) -> str:
	return  "Hello"  + name
if  __name__ == '__main__':
	print(func(123))
```

使用标注前首先需要导入typing标注库, 常用的标注

```python
from typing import List, Dict, Tuple
	List[str]
	Dict[str, str]
	Dict[List[str], str]
	Tuple[str, str]
```

注意：解释器不会对返回类型做检查，比如实际返回是一个dict，但是标注的是str，程序可以正常运行。

## 3、 golang的string，byte和rune

> 中文字符在unicode下占2个字节，在utf-8编码下占3个字节，而golang默认编码正好是utf-8。

*   **string不可变，当使用range遍历时，自动转换为[]rune**


```go
s := "hello 中国"
for c, v  := range s {
     fmt.Printf("%d %c\n", c, v)
}
```
**输出结果**
可以发现输出的序号跟预期不太符合
```go
0 h
1 e
2 l
3 l
4 o
5  
6 中
9 国
```

*   **byte可变，按照utf-8输出**

```go
package main

import "fmt"

func main() {
	s := "hello 中国"
	a := []byte(s)
	for c, v  := range a {
		fmt.Printf("%d %d\n", c, v)
	}
}
```

byte中的汉字被解码为3个字节

```go
0 104
1 101
2 108
3 108
4 111
5 32
6 228
7 184
8 173
9 229
10 155
11 189
```
如果想要输出可以识别的字符，通常使用string转换一下


**rune可变，按照unicode输出**

*   **rune=int32** 四个字节

*   **byte=int8** 1个字节

```go
package main

import "fmt"

func main() {
	s := "hello 中国"
	a := []rune(s)
	for c, v  := range a {
		fmt.Printf("%d %s\n", c, string(v))
	}
}
```

输出结果
```go
0 h
1 e
2 l
3 l
4 o
5  
6 中
7 国
```

## 4、 json与map之间的相互转换

*   **map转json**

```go
package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	//创建一个map
	m := make(map[string]interface{}, 4)
	m["company"] = "byte"
	m["subjects"] = []string{"GO", "C++", "Java"}
	m["ok"] = true
	m["price"] = 666.666
	//编码成json
	//result, err := json.Marshal(m)
	result, err := json.MarshalIndent(m, "", "  ")
	if err != nil {
		fmt.Printf("error: %s", err)
		return
	}
	fmt.Printf("result = %v", string(result))

}

```

因为map是无序的，所以不能保证每次输出的顺序相同。

**json转map**


```go
package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	//创建一个json
	result := `{
		 "company": "bytedance",
		 "isok": true,
		 "price": 666.666,
		 "subjects": ["GO","C++","Java"]
   	}`
	//创建一个用于接收的map
	mp := make(map[string]interface{}, 99)
	json.Unmarshal([]byte(result), &mp)
	fmt.Println(mp)
}

```

**输出的结果**

> map[company:bytedance isok:true price:666.666 subjects:[GO C++ Java]]

## 5、 json与结构体之间的转换

**json转结构体**


```go
package main

import (
	"encoding/json"
	"fmt"
)

//变量名必须大写
type IT struct {
	Company string   `json:"company"`
	Subject []string `json:"subjects"`
	Isok    bool     `json:"-"` //不输出
	Price   float64  `json:",string"`
}

func main() {
	//定义一个结构体变量 同时初始化
	s := IT{"bytedance", []string{"GO", "C++", "Python", "Java"}, true, 666.66}
	//编码 根据内容生成Json文本
	//buf, err := json.Marshal(s)
	buf, err := json.MarshalIndent(s, "", "        ")
	if err != nil {
		fmt.Printf("error %s", err)
	}
	fmt.Printf("%+v", string(buf))
}

```



**结构体转json**


```go
package main

import (
	"encoding/json"
	"fmt"
)

//变量名必须大写
type IT struct {
	Company string
	Subject []string
	Price   float64
}

func main() {
	result := `{
		 "Company": "bytedance",
		 "Subject": ["GO","C++","Python","Java"],
		 "Price": 666.66
   }`
	/*创建一个结构体变量*/
	var it IT
	err := json.Unmarshal([]byte(result), &it)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Printf("%#v\n", it)

}

```

> main.IT{Company:"bytedance", Subject:[]string{"GO", "C++", "Python", "Java"}, Price:666.66}

6.  golang中的自定义排序

golang内置了一些基础数据类型的排序，如int，string，float等，其他类型的结构体需要自己实现less, map,len三个函数。

**内置排序**

```go
package main

import (
	"fmt"
	"sort"
)

func main() {
	// int排序
	ints := []int{1, 8, 4, 5}
	sort.Ints(ints)
	fmt.Println(ints)
	// string排序
	names := []string{"hello", "world", "yao", "jun"}
	sort.Strings(names)
	fmt.Println(names)
}

```


**自定义排序**


```go
package main

import (
	"fmt"
	"sort"
)

type Student struct {
	name string
	age  int
}

type stuSlice []Student
func (s stuSlice) Len() int {
	return len(s)
}

func (s stuSlice) Less(i, j int) bool {
	return s[i].age < s[j].age
}
func (s stuSlice) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func main() {
	students := []Student{{"mike", 16}, {"jane", 22}, {"Ben", 19}}
	sort.Sort(stuSlice(students))
	for k, v := range students {
		fmt.Println(k, v)
	}
}

```
输出结果

```go
0 {mike 16}
1 {Ben 19}
2 {jane 22}
```

## 7、golang中的单元测试

*   t  *testing.T   普通测试函数

*   b *testing.B   benchMark测试

**普通测试函数**

通常test文件的命名规范是xxx_test.go

test case的函数命名为TestXxx形式 否则go test会跳过该test不执行

```go

func  F(a,b int)int{
	return a+b
}

```
测试代码

```go
package main

import "testing"

func TestF(t *testing.T) {
	res := F(3, 4)
	if res != 7 {
		t.Errorf("add wrong!")
	}
}
```

Go test不保证多个test按照顺序执行，但是我们通常会要求按照顺序执行。

使用t.Run来执行subtests可以做到控制test执行的顺序


```go
package main

import (
	"fmt"
	"testing"
)

func TestF(t *testing.T) {
	t.Run("a1", func(t *testing.T) { fmt.Println("a1") })
	t.Run("a2", func(t *testing.T) { fmt.Println("a2") })
	t.Run("a3", func(t *testing.T) { fmt.Println("a3") })
}

```

使用TestMain作为初始化test，并且使用m.Run()来调用其他tests可以完成一些需要初始化操作的testing，比如数据库连接，文件打开，rest服务登录等。如果没有在TestMain中调用m.Run()则除了TestMain以外的其他tests都不会被执行。


```go
func  TestMain(m *testing.M){
	fmt.Println("test main first")
	m.Run()
}
```

**benchmark测试**

benchmark函数一般以BenchMark开头

benchmark函数的case一般会跑b.N次，而且每次执行都会如此

在执行过程中会根据实际case的执行时间是否稳定会增加b.N的次数以达到稳态


```go
go test -bench =. //命令行
func BenchmarkF(b *testing.B) {
for i := 0; i < b.N; i++{
	F(100, 10)
	}
}
func F(a, b int)int{
	return a+b
}
```

如果benchmark测试的函数执行时间始终无法趋于稳态 则永远无法执行完


```go
func  unstable(n int){
	for n > 0{
		n--
	}
}
func BenchmarkF(b *testing.B)
	for i := 0; i < b.N; i++{
		unstable(i) //如果benchmark测试的函数执行时间始终无法趋于稳态 则永远无法执行完
	}
}
```

## 8、golang中切片的坑

**slice传参数时新增失败**


```go
package main
import "fmt"
func modifySlice(s []string) { //切片新增无效
	s[0] = "modify 123"
	s = append(s, "456")
}

func main() {
	s := []string{"123"}
	modifySlice(s)
	fmt.Println(s) //返回结果 [modify 123] 新增的数据没有生效
	s = modifySliceNew(s)
	fmt.Printf("%v", s) //必须重新接收返回值 此时生效 因为修改的指针返回了

}
```

**正确使用方式**

`原因是传入的参数是指针的拷贝 但是新增数据是修改的指针`


```go
func  modifySliceNew(s []string)[]string{  //切片新增生效
    s[0] = "modify 123"
	s = append(s, "456")
	return s
}
```

## 9、golang中删除切片中某个元素

> *   方法1:  删除某个元素后，剩余的元素往前移动
> *   方法2: 重新开一个切片，把满足条件的往新切片中放入
> *   方法3: 索引累计，如果是删除的元素索引就不加1，最后根据累计的索引进行切片


```go
package main

import (
	"fmt"
)

func main() {
	//创建一个slice
	sliceU := []int{1, 0, 1, 1, 0, 1, 0, 1, 1}
	// 要求：把切片中所有的0删除掉
	//slice的删除方式1
	//删除剩余的元素往前移动
	for i, v := range sliceU {
		if v == 0 {
			sliceU = append(sliceU[:i], sliceU[i+1:]...)
		}
	}
	fmt.Println(sliceU)
	//slice的删除方式2
	//重新开一个数组，把满足条件的往新数组中写入
	var newSliceU []int
	for _, v := range sliceU {
		if v != 0 {
			newSliceU = append(newSliceU, v)
		}
	}
	fmt.Println(newSliceU)
	// slice的删除方式3
	// 索引累计 最后切片
	index := 0
	for _, v := range sliceU {
		if v != 0 {
			sliceU[index] = v
			index++
		}
	}
	fmt.Println(newSliceU[:index])
}

```
从上面的结果可以看出，数据范围较小时，方法2和方法3性能差不多，数据量大以后，方法1总体上要差于其他两个策略。

方法1

> 时间复杂度：O(n^2)

> 空间复杂度：O(n)

方法2

> 时间复杂度：O(n)

> 空间复杂度：O(n)

方法3

> 时间复杂度：O(n)

> 空间复杂度：O(1)

## 10、数组传参
```go
package main

import "fmt"
func f(arr [10]int){  //不仅是数组还必须长度一致
	arr[1] = 100
	fmt.Println(arr)
}
func main(){
	/*
	数组：类型和长度确定。
	值类型：传递参数时，进行值拷贝。
	*/
	var arr [10]int
	arr[1] = 2
	arr[2] = 3
	f(arr)
	fmt.Println(arr)
	arr2 := arr
	arr2[1] = 100  //拷贝以后改变 没影响
	fmt.Println(arr2)
	fmt.Println(arr)

}
```
## 11、深浅拷贝
```go
package main

import "fmt"
func f(arr [10]int){  //不仅是数组还必须长度一致
	arr[1] = 100
	fmt.Println(arr)
}
func main(){
	/*
	切片：slice是对底层数组一段内容的引用，slice是一个fat pointer存储的是实际数组的地址，切片的长度，最大容量
	注意：应该避免在两个变量中修改同一个底层数组
	data[low:high:max]high和max都是不包含当前下标的。
	len()
	cap()
	append()
	copy() 可以实现对切片的深拷贝 切片间的直接赋值是浅拷贝，只是赋值了共同的底层数组地址
	对同一个数组进行的不同切片，对某个切片进行操作，对其他切片是没有感知的，但是如果是对底层数组修改，两者都有感知。

	引用类型都是浅拷贝
	操作切片也是操作底层数组，slice采用两倍扩容机制，一旦扩容就重新指向一个新的底层数组。
	cap是切片开始位置到数组末尾的长度

	*/
	var arr [10]int
	arr[0] = 100
	arr[1] = 200
	arr[2] = 300
	slice1 := arr[0:2]
	slice2 := arr[1:5]
	fmt.Println(cap(slice1))
	fmt.Println(cap(slice2))

	slice3 := slice2
	arr[1] = 20000
	fmt.Println("_______")
	fmt.Println(slice1)
	fmt.Println(slice2)
	fmt.Println(slice3)

}

```

## 12、golang常用操作
1. strings.Contains(str, "hello") 是否包含某个字符串
2. strings.Count(str, "hello") 字符串数量统计
3. 字符串拆分为数组strings.Split(s, sep)，sep表示以什么什么来拆分s字符串。
4. 字符串大小写转换，strings.ToUpper(s)转大写，strings.ToLower(s)转小写
5. strings.Trim(s, cutset)，cutset代表要去除的两边字符。strings.TrimLeft(s, cutset)。
6. strings.HasPrefix(s, prefix)。判断字符串是否以什么开头。


### 13、字符串转整形

```go
val, typeErr := strconv.Atoi(myStr2)
b2, errs:= strconv.ParseInt(s2, 2, 64) //把字符串二进制转换为十进制整数
```

### 14、整型转字符串



```go
value := strconv.Itoa(myInt)
ss2 := strconv.FormatInt(b2, 2) //把整数以二进制转换为字符串
```

### 15、字符串转[]byte

```go
myByte := []byte(myStr3)
```

### 16、编码

一个英文字符对应一个byte，一个中文字符对应三个byte。

一个rune对应一个UTF-8字符，所以一个中文字符对应一个rune。%c输出对应的字符和汉字。

rune相当于go的char。

byte=uint8

rune=uint32

### 17、时间

```go
t:= time.Now() //当前时间
```

### 18、读一行

```go
bf := bufio.NewReader(os.Stdin)
ss, errs := bf.ReadString('\n')
lst := string.Field(ss) //按照空格切分字符串
```

### 19、数组初始化

```go
cities := [...]string{"北京", "上海","深圳"}
cities := []string{"上海", "成都"}
	for index,value := range cities{
		fmt.Println(index, value)
	}
```









