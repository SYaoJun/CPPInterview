## tar
- 解压命令
`tar -zxvf 压缩文件名.tar.gz`
- 压缩命令
`tar -zcvf 压缩文件夹名 .tar.gz 被压缩文件名`
### 可执行文件
```shell
# 生成可执行文件
gcc hello.cpp -o name_hello 
go run hello.go
# 生成字节码
java hello.java 
```
### ARM和Intel
- 两家CPU供应商，ARM设计了Aarch64，intel设计了x86_64。
### Aarch64和x86_64
- 都是CPU的指令集架构
- 都是针对64位机
- 都是当下使用最多的两个CPU
- 区别：
    1. Aarch64是使用的精简指令集RISC，优点是功耗低，常用来嵌入式，移动设备上。
    2. intel是使用的复杂指令集CISC，优点是性能高，用在高性能计算设备上。
