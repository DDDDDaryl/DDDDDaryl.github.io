---
title: 侯捷cpp内存管理
date: 2020-08-10 23:07:16
categories:
- Cpp
tags:
- 内存管理
---
1. new 和 delete 调用了什么
   ```c++
   Foo *p = new Foo(x);
   /*something to do*/
   delete p;
   ```
   实际上，new 先调用 operator new 分配内存，再调用 placement new 构造对象。
   而 delete 先调用对象析构函数，再调用 operator delete 释放内存。
   ```c++
   Foo *p = (Foo *)operator new(sizeof(Foo)); // 调用 ::operator new(size_t) 全局函数
   new (p) Foo(x);
   /*something to do*/
   p->~Foo();
   operator delete(p); // 调用 ::operator delete(void *) 全局函数
   ```
   而全局函数`::operator new(size_t)`和`::operator delete(void *)`又做了什么呢
   ```c++
   malloc(size_t);
   free(void *);
   ```
   实际上就是调用了`malloc`和`free`。
   很少重载全局 new 和 delete，一般重载成员函数的 operator new 和 operator delete。这四个函数均可重载。
   
2. 如何重载 per-class operator new 和 operator delete 实现内存池