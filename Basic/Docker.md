## Docker
- 部署工具
### 概念
1. 镜像
2. 容器
3. 仓库
### 操作命令
- 点击软件Docker，进入启动界面。然后再命令行打印版本号，检测软件是否正常启动。
```shell
docker --version
# 查看镜像
docker images
# 查看容器
docker ps
# 拉取最新的mysql软件包
docker pull mysql
# 启动docker -d是后台运行 -p是指定端口 --name是改名 -e是设置登录密码
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql -d

# 通过 exec 命令对指定的容器执行 bash
docker exec -it 995cbe722379 /bin/sh
# 进入mysql操作数据库
mysql -uroot -p123456
```
- [参考博客](https://blog.csdn.net/shentian885/article/details/106418691/)
### Dockerfile
- 用文件的方式执行脚本命令
- 生成一个定制的镜像
```shell
docker build -t ems
```
