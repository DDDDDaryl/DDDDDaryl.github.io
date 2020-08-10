---
title: C++视频学习笔记
toc: true
categories: 
- Cpp
- summary
tag: 
- Cpp
---

1. OO思想的特点：
    - 封装
     把对象属性和方法结合成独立的系统单位，并尽可能隐藏实现细节，是面向对象思想描述的基础；   
    - 抽象
     对具体问题进行概括，对某一类公共问题进行同意描述；
    - 继承
     子类对象拥有与基类对象相同的全部属性和方法，称为继承；
    - 多态
    基类中定义的属性和行为被子类继承后，可以具有不同的特性（行为、数据类型），在共性中寻找特性；
   
2. 数组的传递

   ```c++
   int main(){
       int data[] = {1, 2};
       print(sizeof(data));
       // 结果为2*4 Byte=8 Byte
   }
   
   int addArray(int array[]){
       printf(sizeof(array));
       // 结果为指针长度（机器相关）4（32位）或8（64位机器）
   }
   ```

3. `cout`是一个输出流对象，是`console out`的缩写，属于`basic_ostream`类；

4. c语言中，`scanf`从输入流获取值，`getchar`获取字符

   ```c
   scanf("%d", &i); // 将读入的十进制数存入变量i
   ch = getchar(); // 将读入的char类型数据存入ch，此时读入ch的数据不再存在在输入流中
   ungetc(ch, stdin)； // 将ch中的数据退回输入流
   ```

5. `c++`版本的流输入

   `cin`的类型为`istream`；

   用户输入时，对应的字符进入操作系统的键盘缓冲区中；

   输入`enter`时，操作系统把家农安缓冲区的内容传输到`cin`的内部缓冲区，由`>>`操作符从内部缓冲区中提取需要的信息；

   `>>`操作符对所有内建类型都进行了重载；

6. 阻塞性IO、非阻塞、异步

7. `C++`可以在任意位置声明变量，允许我们在实际使用的时候再声明；

8. ```c++
   char buf[20]; // 可存放19个字符
   cin.ignore(n); //忽略n个字符
   cin.getline(buf, 10); // 从cin中读取10个字符存入buf
   while(cin.peek() != '\n'){
       cout<<cin.get();
   }; // 当前字符不为换行符时，将读入字符输出，先读入后放回
   
   const int size = 50;
   int buf[size];
   
   cout << "请输入文本：";
   cin.read(buf, 20);
   
   cout<<"字符串收集到的字符数为："<< cin.gcount() << endl;
   
   cout << "输入的文本信息为：";
   cout.write(buf, 20);
   ```

9. cout

   ```c++
   int main(){
       double result = sqrt(3.0);
       cout << "对3开方保留小数点后0~9位" << endl;
       for(int i=0; i<=9; ++i){
           cout.precision(i);
           cout << result <<endl;
           cout << "当前输入精度： " << cout.precision();
       }
   }
   ```

   ```c++
   int main(){
   	int width = 4;
       char str[20];
       
       cout << "请输入一段文本： \n";
       cin.width(5);// 输入宽度为5
       while(cin >> str){
           cout.width(++width);
           cout << str <<endl; 
           cin.width(5);
       }
       return 0;
   }
   ```
