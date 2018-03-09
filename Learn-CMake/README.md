# Learn CMake

使用CMake生成Makefile并编译的流程：

1. 编写CMake配置文件`CMakeLists.txt`
2. 执行命令`cmake PATH`生成Makefile，`PATH`为`CMakeLists.txt`所在的目录
3. 使用`make`命令进行编译

## 简单的`CMakeLists.txt`的实例：

```CMakeLists.txt
# 指定CMake的最低版本号要求
cmake_minimum_required(VERSION 2.8)

# 指定项目名称为Demo1
project (Demo1)

# 指定生成目标
add_executable(Demo main.c)
```

## 如果有多个源文件(在用一个目录下）：

```CMakeLists.txt
# 只加入c或cpp源文件名，头文件不需要
add_executable(Demo main.c func1.c)
```

或者：

```CMakeLists.txt
# 查找当前目录下所以的源文件
aux_source_directory(. DIR_SRCS)

# 指定生成目标
add_executable(Demo ${DIR_SRCS})
```

## 多目录

CMake需要在多个目录中编写`CMakeLists.txt`文件，如果这个文件夹有源代码的话

```CMakeLists.txt
# 首先加入子目录
add_subdirectory(math)

# 添加链接库
target_link_libraries(Demo MathFcuntions)
```

在子目录下：

```CMakeLists.txt
# 查找当前目录下的源文件，并保存名称到DIR_LIB_SRCS
aux_source_directory(. DIR_LIB_SRCS)

# 生成链接库
add_library(MathFunction ${DIR_LIB_SRCS})
```