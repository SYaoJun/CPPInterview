package main

import (
	"fmt"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"
)

type UserInfo struct {
	Id    int
	Name  string
	Phone int
}

func main() {
	db, err := gorm.Open("mysql", "root:root@(localhost)/yaojun?charset=utf8mb4&parseTime=True&loc=Local")
	if err != nil {
		fmt.Println("未连接成功...")
	} else {
		fmt.Println("连接成功...")
	}
	defer db.Close()
	// 创建表
	db.AutoMigrate(&UserInfo{})

	// 创建数据行
	u1 := UserInfo{1, "yaojun", 121}
	u2 := UserInfo{2, "zhouyuyi", 222}
	db.Create(&u1)
	db.Create(&u2)
}
