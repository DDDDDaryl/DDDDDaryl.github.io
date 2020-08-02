---
title: Anaconda常用指令整理
toc: true
categories:
- python
tag:
- Anaconda
- python
---

# 创建、删除、激活、退出环境

1. 首先查看环境

   ```shell
   conda env list
   ```

2. 创建环境

   ```shell
   conda create -n env_name python=3.x
   ```

3. 删除环境

   ```shell
   conda remove -n env_name --all
   ```

4. 激活环境

   ```shell
   source activate env_name
   ```

5. 退出当前环境回到base

   ```shell
   source deactivate
   ```

# 包管理





