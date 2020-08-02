---
title: Git-Please commit your changes or stash them before you merge.
date: 2020-06-09 16:58:28
categories:
- techissue
tags:
- git
---

当我们把工程从远程仓库 clone 到本地并且做了部分修改之后，此时如果想要从远端用 git pull 获取新的版本时，因为直接 pull 会覆盖本地项目，因此 git 要求我们先 commit changes，避免数据丢失。

当然，如果我们要丢弃改动，强行覆盖，可以

```shell
git reset --hard
git pull
```

如果不想丢弃手头已做的修改，又需要获取远程仓库的一个版本，那么使用

```shell
git stash
git pull
git stash pop # 出栈，删除存档
git stash apply # 不删除存档
git stash list # 查看现有stash
```

stash 将当前所有未提交的修改保存在本地，意为储藏。