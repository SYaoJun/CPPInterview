## tinykv
### 前置技能
- makefile
- go_test
- gRPC
### TDD
- 测试驱动开发
### 笔记
```shell
# 执行项目1的测试用例your code here
make project1
```
### Project1
1. raw_api
2. standalone_storage
- 目标很清晰，就是要完成这两个文件中的8个函数。
- 需要思考一下的是，每个函数接口要实现什么功能。为了实现这个功能，函数之间的调用关系是什么样的，结构体的属性应该怎么设计，每个类之间是什么关系。
1. 类与类的关系
2. 函数与函数的关系
3. 属性的定义
4. 函数的功能
5. 逻辑正确性