---
title: gdb使用
toc: true
categories:
- Linux
tag:
- Linux
- gdb
---

# 基本使用

- 启动gdb

  ```shell
  gdb exe_name
  ```

- gdb中运行程序

  ```
  # 连续运行
  (gdb) run
  (gdb) r
  # 分步调试
  (gdb) start 
  # 向下执行
  (gdb) n(ext) 
  # 单步调试进入函数，不能进入库函数
  (gdb) s(tep) 
  ```

- 退出gdb

  ```
  (gdb) quit
  ```

- 运行中给变量赋值

  ```
  # 设置主函数运行参数
  (gdb) set args param1 param2
  # 调试中变量赋值
  (gdb) set param=val
  ```

- 显示代码

  ```
  (gdb) list
  (gdb) list file_name:line_ID
  ```

- 设置断点

  ```
  (gdb) break line_ID
  (gdb) b func_name
  (gdb) b file_name:line_ID
  ```

- 查看断点

  ```
  (gdb) i(nfo) b
  ```

- 删除断点

  ```
  (gdb) d break_ID
  ```

- 运行到下一个断点

  ```
  (gdb) c(ontinue)
  ```

- 查看变量

  ```
  (gdb) p(rint) var_name
  (gdb) ptype var_name
  # 运行时打印变量，用于追踪变量
  (gdb) display var
  # 查看当前display的变量
  (gdb) info display
  # 取消打印变量
  (gdb) undisplay var_ID
  ```

- 设置条件断点

  ```
  (gdb) b line_ID if condition
  ```

# gdb调试core

- 设置生成 core：

  ```shell
  # 设置生成core
  ulimit -c size
  ulimit -c unlimited
  # 取消生成core
  ulimit -c 0
  ```

  