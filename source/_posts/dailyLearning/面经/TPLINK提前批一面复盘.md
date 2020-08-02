---
title: TPLINK提前批一面复盘
date: 2020-06-17 11:03:40
categories:
- 面经
tags:
- TP
---

# 一面

- strcpy 和 memcpy

  ```c++
  char *strcpy(char *dest, const char *src);
  
  void *memcpy(void *dest, const void *src, size_t n);
  ```

  strcpy 只能拷贝字符串；memcpy 可以拷贝任何类型的数据，但是需要指定以字节为单位的拷贝长度；

- traits

  1. `iterator_traits`，迭代器特性萃取器，用于萃取迭代器类型  

     ```c++
     template <typename Iterator>
     struct iterator_traits {
         typedef typename Iterator::iterator_category;
         typedef typename Iterator::value_type value_type;
         typedef typename Iterator::difference_type difference_type;
         typedef typename Iterator::pointer pointer;
         typedef typename Iterator::reference reference;
     }
     
     ```

     

  2. `__type_traits`  
     其双下划线代表 SGI 内部使用。
     什么是`trivial`？

     > In simple words a "trivial" special member function literally means a member function that does its job in a very straightforward manner. The "straightforward manner" means different thing for different kinds of special member functions.
     >
     > For a default constructor and destructor being "trivial" means literally "do nothing at all". For copy-constructor and copy-assignment operator, being "trivial" means literally "be equivalent to simple raw memory copying" (like copy with `memcpy`).
     >
     > If you define a constructor yourself, it is considered non-trivial, even if it doesn't do anything, so a trivial constructor must be implicitly defined by the compiler.
     >
     > In order for a special member function to satisfy the above requirements, the class must have a very simplistic structure, it must not require any hidden initializations when an object is being created or destroyed, or any hidden additional internal manipulations when it is being copied.
     >
     > For example, if class has virtual functions, it will require some extra hidden initializations when objects of this class are being created (initialize virtual method table and such), so the constructor for this class will not qualify as trivial.
     >
     > For another example, if a class has virtual base classes, then each object of this class might contain hidden pointers that point to other parts of the very same object. Such a self-referential object cannot be copied by a simple raw memory copy routine (like `memcpy`). Extra manipulations will be necessary to properly re-initialize the hidden pointers in the copy. For this reason the copy constructor and copy-assignment operator for this class will not qualify as trivial.
     >
     > For obvious reasons, this requirement is recursive: all subobjects of the class (bases and non-static members) must also have trivial constructors.
     >
     > -----摘自https://stackoverflow.com/questions/3899223/what-is-a-non-trivial-constructor-in-c

     也就是说`trivial ctor`就是不做任何操作的构造函数，构造时没有任何隐式初始化，比如含有虚函数的类，在初始化时需要隐式初始化虚函数表以及虚表指针，不满足`trivial`的定义，因此不能直接简单地拷贝内存`memcpy`。

     `__type_traits`用于萃取型别特性，而这些型别特性包括：

     - `has_non_trivial_default_constructor`
     - `has_trivial_copy_constructor`
     - `has_trivial_assignment_operator`
     - `has_trivial_destructor`
     - `is_POD_type`

     当一个类型是`trivial`的，意味着可以直接使用内存操作进行构造，以提升效率。

     而当一个类型具有指针成员，其指向动态分配内存，那么就必须定义`non-trivial ctor`等。

- 链表是否有环

  快慢指针

- TCP/IP 层次结构

  1. OSI 七层协议

     > 应用层
     >
     > 表示层
     >
     > 会话层
     >
     > 运输层
     >
     > 网络层
     >
     > 数据链路层
     >
     > 物理层

  2. TCP/IP 四层协议

     > 应用层：TELNET, FTP, SMTP, DNS, HTTP。通过应用进程间交互来完成特定网络应用。
     >
     > 运输层：TCP, UDP。负责向两台主机中的进程间通信提供通用的数据传输服务。
     >
     > 网际层：IP。负责为分组交换网上的不同主机提供通信服务，并进行路由选择。
     >
     > 网络接口层：ICMP, ARP。

- 进程间通信方式

  1. 管道/匿名管道

     > 半双工，数据只能向一个方向流动
     >
     > 只能用于父子进程或者兄弟进程之间通信
     >
     > 可以理解为循环数组实现的队列，FIFO
     >
     > 实质上是一个内核缓冲区，以 FIFO 方式存取数据，缓冲区读空或者写满时，相应进程进入等待队列，可读或可写是唤醒相应进程
  2. 有名管道

     > 不同于匿名管道，以有名管道文件形式存在于文件系统中，实现了无亲缘关系进程间的通信
     >
     > 名字存在内存系统，而内容存在内存中，相当于两个进程做了相同的虚拟地址映射，
  3. 信号

     > 进程间相互通信的机制
     >
     > 信号是软件层次上对中断机制的模拟，是一种异步通信方式
  4. 消息队列

     > 存放在内核中的消息链表，每个消息队列由消息队列标识符表示
     >
     > 允许多个进程 FIFO 读写
     >
     > 可实现随即查询
  5. 共享内存

     > 将不同进程的某个虚拟内存区域映射到磁盘中同一个共享对象上，避免数据拷贝
     >
     > 需要进程同步机制来同步进程
     >
     > `mmap()`
  6. 信号量

     > 是一个计数器，用于多进程对共享数据的访问，实现进程间/线程间同步
  7. 套接字

- 讲讲项目

- 爱好

- 成绩