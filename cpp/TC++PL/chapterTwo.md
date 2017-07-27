- ### 声明是一条语句，负责为程序引入一个新的名字：
  - **类型(type)** 定义了一组可能的值以及一组（对象上的）操作
  - **对象(object)** 是存放了某个类型值得内存地址
  - **值(value)** 是一组二进制位，具体的含义由其类型决定
  - **变量(variable)** 是一个命名的对象

- ### 初始化器列表

  - 相比于`=` ，`{}`是一种更通用的形式。

  ```C++
  double d1 {2.3};
  double d2 = {1.1};	//使用初始化器列表时可以省略'='号
  complex<double> c {d1,d2};
  vector<int> v {1,2,3,4};
  ```

  - 使用初始化器列表的形式可以确保不会发生某些可能导致信息丢失的类型转换（窄式类型转换）

  ```C++
  int i1 = 7.2; //发生窄式类型转换，i1变成7
  int i2 {7.2}; //编译器会报错
  int i3 = {7.2};	//同样会报错,这里的`=`号是多余的
  ```

- ### auto

  - 在定义一个变量时，如果变量的类型可以由初始化器推断出来，我们可以使用`auto`而不显式地指定类型。

  ```c++
  auto b = true;
  auto ch = 'x';
  auto i = 123;
  auto z = sqrt(y);	//是sqrt(y)的返回类型
  ```

  - 当我们没有明显的理由需要显式指定数据类型时，一般使用`auto`,明显的理由包括：
    - 该定义位于一个较大的作用域，我们希望读代码的人清楚的知道其类型。
    - 我们希望明确规定某个变量的范围和精度（如希望使用double而不是float）

- ### 常量

  - `const` 

    > “我承诺不改变这个值”。

    主要用于说明接口。

    编译器负责确认并执行这个承认。

  - `constexpr`：

    > “在编译时求值”。

    主要用于说明常量。

    作用是允许数据置于只读内存中以及提高性能。

  ```c++
  const int dmv = 17; //dmv 是一个命名的常量
  int var = 17;	
  constexpr double max1 = 1.4*square(dmv);	//如果square(17)是一个常量表达式的话，则正确
  constexpr double max2 = 1.4*square(var);	//错误，var是个变量
  const double max3 = 1.4*square(var);	//正确,const 可以在运行时求值

  //如果某个函数用在常量表达式中，即该表达式在编译时求值，则函数必须为constexpr:
  //要想定义成constexpr,函数必须非常简单：函数中只能有一条用于计算某个值得return语句。
  //constexpr函数可以接受非常量参数，但此时返回值将不会是一个常量表达式，所以max2才会错。
  constexpr double square(double x) { return x*x; }

  ```

- ### 范围for语句：

  > 遍历一个序列的最简单方法。

  ```c++
  vector<int> v{1,2,3,4};
  for(int i : v)
    cout<<i<<endl;

  //通常和auto一起使用
  for(auto i : v)
    cout<<i<<endl;

  //要改变序列中的值的话，需要用&
  for(auto & i: v)
    i++;

  //不加&，则表示i是v中某个值的一个拷贝，这样无法改变v中的值
  ```

- ### 枚举类

  > 枚举类型用于描述规模较小的整数值集合，通过使用有指代意义的枚举值名称可以提高代码可读性，降低出错的风险。

  ```c++
  enum class Color {red,blue,green };
  enum class Traffic_light {green,yellow,red}
  ```

  - enum后面的class指明了枚举是**强类型**的，且它的枚举值位于指定的作用域中。不同的enum class 是不同的类型，这样有助于防止常量的意外误用。

  ```c++
  Color x = red;	//错误
  Color y = Traffic_light::red; 	//错误
  Color z = Color::red;	//正确
  int i = Color::red;		//错误
  Color c = 2;	//错误
  ```

  - 默认情况下，enum class 只定义了赋值初始化和比较（即`==`和`<` ），我们也可以为它定义别的运算符：

    ```c++
    Traffic_light& operator++(Traffic_light &t){
      switch(t){
        case Traffic_light::green : return t=Traffic_light::yellow;
        case Traffic_light::yellow : return t=Traffic_light::red;
        case Traffic_light::red : return t=Traffic_light::green;
      }
    }
    ```

  - C++ 也提供了次强类型的“普通”的enum

- ### 静态断言

  > `static_assert`机制能用于任何可以表示为**常量表达式**的检查，并以编译器错误消息的形式报告错误，最重要的用途就是为泛型编程中作为形参的类型设置断言。

  ```c++
  static_assert(8 == sizeof(int), "integers are too big.");
  // error C2338: integers are too big.
  ```

  ​