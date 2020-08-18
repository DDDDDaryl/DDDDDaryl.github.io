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
   `placement new` 的第一个参数必须为 `size_t`，否则编译器报错。  
   在构造函数内抛出异常时，调用 `operator delete`。（旧版本行为，新版本并没有调用 `operator delete`)  
   
3. 内存管理的目的：  
   提高速度，降低内存消耗（尤其指 cookie，每个 array new 会分配 8 字节的 cookie） 
   ```c++
   class Foo {
    int a;
   public:
       Foo() = default;
       explicit Foo(int aa) : a(aa) {};
   };
   int main() {
       const int N = 100;
       Foo *p[N];
       for (int i = 0; i < N; ++i) {
           p[i] = new Foo(i);
       }
       for (int i = 0; i < 10; ++i)
           cout << p[i] <<endl;
       for (int i = 0; i < N; ++i)
           delete p[i];
       return 0;
   }
   ```
   以上程序的输出：
   ```
   F:\c++prj\prac\cmake-build-debug\prac.exe
   0x731750
   0x731770
   0x731ac0
   0x731ae0
   0x731b00
   0x735c60
   0x735c80
   0x735ca0
   0x735cc0
   0x735ce0
   Process finished with exit code 0
   ```
   说明每个 Foo 对象确实是 16 字节，含有 4 字节的 int，8 字节的 cookie，以及 4 字节的 padding。
   
4. 用一个内存池来管理一个类的对象时，若使用自由链表（单链表），那么每个对象会有 4 字节（64 位操作系统 8 字节）的开销，与每个对象 8 字节的 cookie 开销相比，并无太大收益，唯一的收益是减少了 malloc 的调用次数。  
   使用内嵌指针 (embedded pointer) 的概念来优化这一点:  
   ```c++
class Airplane {
   private:
       struct AirplaneRep {
           unsigned long miles;
           char type;
       };    
   private:
       union {
           AirplaneRep rep; // 此为使用中的objects
           Airplane *next; // 此指针为embedded ptr，指向内存池中的objects
       }
   public:
       static void *operator new(size_t size); // 重载 operator new，此函数申请一大块内存并插入空闲链表
       static void operator delete(void *deadObject, size_t size);
   };
   ```
   在所有的内存池中都使用这种形式来减少开销，也就是 CSAPP 里面所提到的思想，用链表中空闲内存来存储链表指针。

