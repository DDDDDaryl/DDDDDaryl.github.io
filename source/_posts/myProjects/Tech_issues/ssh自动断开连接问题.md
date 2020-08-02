---
title: 解决：ssh长时间无操作服务器断开会话的问题
categories:
- Linux
tag:
- Linux
- ssh
---

# 修改服务器端参数

修改服务器端的ssh设置：找到

```shell
$ cd /etc/ssh
$ vim sshd_config
```

添加如下设置：

```
ClientAliveInterval  60
```

该设置意为服务器会每60秒向client发送一次保持连接的信号。如果还要定时断开连接：

```
ClientAliveCountMax  60
```

# 修改客户端参数

与修改服务器参数类似，只不过需要修改的文件为`ssh_config`。

# 使用ssh登陆前用参数配置

```shell
ssh -o ServerAliveInterval=30 root@192.168.1.1
```

# Reference

1. [ssh连接远程服务器自动断开解决](https://blog.csdn.net/hustcw98/article/details/79325878)