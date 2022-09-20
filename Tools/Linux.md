# Linux
## Linux命令
1. find命令，用来查找文件。常用的按照名字查找-name，按照文件类型查找-type，linux常用的文件类型有七种，普通文件，目录文件，管道，套接字，软链接，块设备，字符设备。还可以按照文件大小查询-size。
2. grep命令，按照文件内容来查找。使用规则是grep option pattern file
3. ps aux
4. curl命令 访问一个网页
5. df 查看磁盘大小
6. du 查看目录大小
7. free -h 查看内存大小和使用情况
8. top 查看系统的实时负载
9. netstat -ta 查看监听的TCP
10. stat 获取文件属性
11. file 查看文件类型
12. sudo iptables -L 查看防火墙状态
13. sudo vim etc/sysctl.conf 查看TCP属性
14. touch yao.txt 创建文件
15. echo >> jun.txt 追加 >是重写
16. cat/less/more/tail/head yao.txt 查看文件类型
17. chmod修改文件权限
18. tar/zip
19. kill
### 特殊工具
- vim
- gdb
- perf
- strace
### 常用命令
```shell 
# 多个目录
mkdir -p lover/zyy
# 当前路径
pwd
# 以树形结构查看目录
tree -L 2
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
## linux常用命令
-   awk 参数 脚本 文件
```shell
     awk '{print  NR NF "\t"  $0, $1 }'
```
-   wc -c 字符数 -l 行数 -w 单词数
-   sort
```shell
    sort -r coin.txt 逆序
    sort -n coin.txt 数值
```