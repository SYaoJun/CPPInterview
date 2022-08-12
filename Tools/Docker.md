## Docker
- [Docker官网](https://www.docker.com/)
- [Docker hub官网](https://hub.docker.com/)
### 概念
1. 镜像
2. 容器
3. 仓库
### 术语
- 一个镜像可以对应多个不同的容器
### 操作命令
- [菜鸟教程：常用软件的安装命令](https://www.runoob.com/docker/docker-install-ubuntu.html)
- 点击软件Docker，进入启动界面。然后再命令行打印版本号，检测软件是否正常启动。
```shell
docker --version
# 查看镜像
docker images
# 查看正在运行的容器
docker ps 
# 查看所有的容器
docker ps -a 
# 拉取最新的mysql软件包
docker pull mysql
# 启动docker -d是后台运行 -p是指定端口 --name是改名 -e是设置登录密码
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql -d
# 启动已有容器
docker start 995cbe722379
# 通过 exec 命令对指定的容器执行 bash
docker exec -it 995cbe722379 /bin/sh
# 退出
exit
# 进入mysql操作数据库
mysql -uroot -p123456
# 在mysql命令行中查看版本信息
status
# 删容器
docker rm [container_id/container_name]
# 删除镜像: 要把镜像关联的所有容器删完了才能删除这个镜像，否则要用强制删除
docker rmi -f [image_id/image_name]
docker rmi [image_id/image_name] 
docker image rm [image_id/image_name]
# 启动镜像
docker start mysql
# 重名了efeb4214cfc4为hello
docker tag efeb4214cfc4 hello
# 然后将原来的image名称删除
docker rmi hello:1.0
```
- [参考博客](https://blog.csdn.net/shentian885/article/details/106418691/)
### Dockerfile
- 自动化脚本
- 用文件的方式执行脚本命令
- 生成一个定制的镜像
```shell
docker build -t ems
```
### 搭建集群docker-compose.yml
## ubuntu
```shell
docker run -itd --name ubuntu-test ubuntu
docker exec -it ubuntu-test /bin/sh
```
### redis
```shell
docker run -itd --name redis-test -p 6379:6379 redis
docker exec -it redis-test /bin/bash
redis-cli
```
