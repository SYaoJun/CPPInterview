# Linux
## Linux命令
1.  find命令，用来查找文件。常用的按照名字查找-name，按照文件类型查找-type，linux常用的文件类型有七种，普通文件，目录文件，管道，套接字，软链接，块设备，字符设备。还可以按照文件大小查询-size。
2.  grep命令，按照文件内容来查找。使用规则是grep option pattern file
3.  ps aux
4.  curl命令 访问一个网页
6.  df查看磁盘大小
7.  du查看目录大小
8.  free -h 查看内存大小和使用情况
9.  top查看系统的实时负载
10.  netstat -ta 查看监听的TCP
12.  stat 获取文件属性
11.  file 查看文件类型
12.  sudo iptables -L 查看防火墙状态
13.  sudo vim etc/sysctl.conf 查看TCP属性
### 常用命令
```shell
cat hello.cpp
tail -1000f logger.log
mkdir -r hello/world
grep
find
chmod
chown
awk
sed
stat
fcntl
scp
netstat -anp | grep python //查看网络连接状态
cat /proc/meminfo // 查看内存信息
cat /proc/cpuinfo //查看cpu信息
free //查看磁盘信息
top //动态查看cpu信息 %cpu %mem pid
df //查看磁盘
tailf -1000 //查看日志
ulimit -a //显示目前资源限制的设定
echo $? //查看进程退出状态
sort -r //逆序 从大到小
sort -n //从小到大 数字
du hello.c //显示目录或文件的大小
file hello.c //识别文件类型
# 生成可执行文件
gcc hello.cpp -o name_hello 
go run hello.go
# 生成字节码
java hello.java 
# 压缩
tar -zcvf 压缩文件夹名 .tar.gz 被压缩文件名
# 解压
tar -zxvf 压缩文件名.tar.gz
```
### Aarch64和x86_64
- ARM和Intel：两家CPU供应商，ARM设计了Aarch64，intel设计了x86_64。
- 都是CPU的指令集架构
- 都是针对64位机
- 都是当下使用最多的两个CPU
- 区别：
    1. Aarch64是使用的精简指令集RISC，优点是功耗低，常用来嵌入式，移动设备上。
    2. intel是使用的复杂指令集CISC，优点是性能高，用在高性能计算设备上。
