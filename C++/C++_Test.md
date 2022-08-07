# C/C++基础测试框架
## Developer Test, DT
- UT
- Alpha
- Beta
- Gamma
- Product
## gtest
- [官网传送门](https://github.com/google/googletest)
- 可移植性好
- 强大的断言系统
- 社区活跃度高

## gtest事件机制
- 全局级别
- TestSuite
- TestCase
## gmock
- [参考博客](https://www.cnblogs.com/huaibin/p/15400562.html)
- 模拟未实现的类方法
## gdb
- gdb可以用于分析coredump文件，coredump文件中含有当进程被终止时内存，cpu寄存器和各种函数堆栈信息等。
1. 设置断点 b 120
2. 运行 r
3. 打印遍历p  number
4. 查看堆栈bt
5. 查看循环中的变量 i
6. 单步运行n
## 实践篇
## MAC安装gtest
```shell
# 克隆仓库
git clone https://github.com/google/googletest.git
cd googletest
mkdir build && cd build
cmake -DCMAKE_CXX_STANDARD=17 ..
make
sudo make install
```
### TDD 测试驱动开发
- 先写测试
- 再写源代码