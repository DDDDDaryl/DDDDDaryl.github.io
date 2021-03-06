---
title: new和malloc的区别
date: 2020-05-26 21:33:25
categories:
- Cpp
tags:
- Cpp
- new
---

# 细节

1. 申请的内存所在位置  
   new 操作符从**自由存储区**上为对象动态分配存储空间；
   malloc 函数在运行时堆上动态分配存储空间。
   自由存储区是**基于 new 操作符的概念**，凡是通过 new 操作符进行内存申请，那么该内存就是动态存储区；
   堆是操作系统虚拟内存系统在一个进程的私有虚拟空间中维护的一个区域，用于程序的动态内存分配。

   **自由存储区能否是堆**取决于 new 操作符的具体实现。

2. 返回类型安全性  
   new 分配成功时返回一个类型与其指向对象类型严格匹配的指针，**无需进行类型转换**，因此是符合**类型安全性的**操作符；

   而 malloc 返回 void*，需要强制转换成相应的对象类型。

   类型安全的代码不会试图访问禁止访问的内存区域，因此是内存安全的。

3. 内存返回失败时的返回值  
   new 分配内存失败时，**抛出 bad_alloc 异常**，不会返回NULL；

   malloc 分配内存失败时，返回 NULL；
   new 分配失败时使用 catch 捕获异常。

4. 是否需要指定内存大小  
   new 无需指定大小，**编译器**会根据其类型信息计算；
   malloc 需要显式指定内存大小；

5. 是否调用构造函数/析构函数  
   使用 new 时会经历三个步骤：

    - 调用 operator new 函数，分配一块足够大的，原始的，未命名的内存空间以便存储特定类型对象；
    - 调用相应**构造函数**以构造对象，并为其传入初值；
    - 对象构造完成后，返回一个指向该对象的指针；

   使用 delete 操作符来释放对象内存时：

    - 调用对象析构函数；
    - 调用operator delete 函数释放内存空间；

6. 对数组的处理 

   C++ 提供了 new[] 和 delete[] 来专门处理数组类型

   ```c++
   T* ptr = new T[10]; // 分配一个10个T类型元素的数组
   delete [] ptr;
   ```

   new[] 会分别调用构造函数初始化每一个数组元素，释放对象时为每个对象调用析构函数；

   malloc 仅仅分配一块内存，并返回一个指向首地址的指针。

7. new 和 malloc 是否可以相互调用  
   new/delete 可以基于 malloc/free 实现，反之不行；因为 new 本身比 malloc 更复杂，无法用高级功能体现低级特性。

8. 是否可以被重载  
   operator new / operator delete 可以被重载。
   malloc / free 不允许重载。

9. 能否重新分配内存  
   malloc 可以使用 realloc 进行内存重新分配；
   new 没有扩充内存的工具；

10. 客户处理内存分配不足  
    operator new 分配内存失败抛出一个异常之前，会先调用一个用户指定的异常处理函数 new-handler，用户使用 set_new_handler 函数指定异常处理函数。

    其实就是设置了用户定义的异常处理函数，使用了标准库包装的系统调用进行设置（个人理解，有待考证）。

# 总结

区别在于：

- 物理位置
- 输入输出，是否安全
- 如何实现
- 有何功能

几个方面的差异。