# Gin
- 高性能Web服务器

```go
package main

import ("github.com/gin-gonic/gin"
	"log"
)

func main() {
	r := gin.Default()
	r.GET("/hello", func(context *gin.Context) {
		context.Writer.Write([]byte("hello gin!"))
	})

	if err:=r.Run(":9898"); err != nil{
		log.Fatal(err.Error())
	}
}
```
## 浏览器端输入

```go
http://localhost:9898/hello
```
就可以看到

```go
hello gin!
```
## redisgo
1. 对set的操作
```go
package main
import (
	"fmt"
	"github.com/garyburd/redigo/redis"
)

func main() {
	//连接服务器
	conn, err := redis.Dial("tcp","127.0.0.1:6379")
	if err != nil {
		fmt.Println("redis.Dial err=", err)
		return
	}
	//连接成功
	fmt.Println("connect success!")
	//set操作
	_,err = conn.Do("set","name","ming")
	if err!=nil{
		fmt.Println("set err= ",err)
		return
	}
	fmt.Println("operation success!")
	//get操作
	r, err := redis.String(conn.Do("Get","name"))
	if err!= nil {
		fmt.Println("get err=", err)
		return
	}
	fmt.Println(r)
	defer conn.Close()
}


```
2. 对hash的操作

```go
package main

import ("fmt"
"github.com/garyburd/redigo/redis"
)

func main() {
	//连接redis服务器 本地必须事先启动redis服务器
	conn, err := redis.Dial("tcp","127.0.0.1:6379")
	if err != nil {
		fmt.Println("redis.Dial err=", err)
		return
	}
	//向redis中写入数据 HSet
	_,err = conn.Do("HSet","user1","age",18)
	if err != nil{
		fmt.Println("set err=",err)
		return
	}
	//向redis中写入数据 HSet
	_,err = conn.Do("HSet","user1","name","yaojun")
	if err != nil{
		fmt.Println("set err=",err)
		return
	}
	//从redis中获取数据
	var r string
	r,err = redis.String(conn.Do("HGet","user1","name",))
	if err != nil{
		fmt.Println("get err=",err)
		return
	}
	fmt.Println("name = ",r)
	var a int
	a,err = redis.Int(conn.Do("HGet","user1","age",))
	if err != nil{
		fmt.Println("get err=",err)
		return
	}
	fmt.Println("age = ",a)
	defer conn.Close()
}
```
## Iris服务器

```go
package main

import (
	"github.com/kataras/iris"
	"github.com/kataras/iris/context"
)

func main() {
	app := iris.New() // 实例一个iris对象

	/*
	app.Get("/hello", func(ctx iris.Context) {
		//获取路径
		path := ctx.Path()
		app.Logger().Info(path)
		//获取名字
		username := ctx.URLParam("username")
		app.Logger().Info(username)
		//密码
		pwd := ctx.URLParam("pwd")
		app.Logger().Info(pwd)
		//返回html 自动渲染 http://localhost:8080/hello?username=yaojun&pwd=helloworld
		ctx.HTML("<h1>"+username+","+pwd+"</h1>")
	})
	*/
	app.Post("login", func(ctx context.Context){
		path := ctx.Path()
		app.Logger().Info("请求url:",path)
		//postValue获取post提交的表单数据
		name := ctx.PostValue("name")
		age:= ctx.PostValue("age")
		ctx.HTML("<h1>"+name+" , "+age+"</h1>")
		//ctx.JSON(iris,Map{"massage":"hello"})
		//读取浏览器传来的json 使用readJSON()
		//读取浏览器传来的XML  使用readXML()
	})
	app.Run(iris.Addr(":8080"),iris.WithCharset("UTF-8"))

}

```
