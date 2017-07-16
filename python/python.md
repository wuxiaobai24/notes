# About Python
---

## Python 中 is 和 ==

> #### 在编写python的程序是一直有点困惑is和==的区别，好吧，我已经连续两次因为没弄清这个两个的区别而浪费了找bug找了很久了，所以我觉得做下总结。

我们可以在 [python文档](https://docs.python.org/3.4/reference/)中找到一些可以解释这个的东西。

比如[这个](https://docs.python.org/3.4/reference/datamodel.html)

虽然这个挺长的，**3.1 Objects,Values and Types** 中我们就可以找到我们需要的东西：

> #### Every object has an identity, a type and a value.* An object’s identity never changes once it has been created; you may think of it as the object’s address in memory.*  The ‘is‘ operator compares the identity of two objects; the id() function returns an integer representing its identity.

从上面可以看出，**is** 是比较两个对象的id的，而你可以认为id是两个对象的所在的地址

那么 **==** 又是比较什么的呢？

显而易见，**==** 是在比较两个对象是否相等？

我们来试验一下：

```python
In [1]: a = []

In [2]: b = []

In [3]: id(a)
Out[3]: 140463615001232

In [4]: id(b)
Out[4]: 140463615032856

In [5]: a is b
Out[5]: False

In [6]: a == b
Out[6]: True

In [7]: c = d =[]
```

从上面我们可以对 **is** 和 **==** 做个大概的区分：

- is 是在比较两个的对象的id，我们可以认为id就是对象所在的内存地址
- == 是在比较两个对象的值，会调用 \_\_eq\_\_ 方法

但是在接下来的试验中，又出现了一下奇怪的东西：

```python
In [9]: a = 1

In [10]: b = 1

In [11]: id(a)
Out[11]: 94795567313240

In [12]: id(b)
Out[12]: 94795567313240

In [13]: a is b
Out[13]: True
```

上面的试验一开始让我很困惑，但是仔细想想好像是因为思维定式而导致了这些不必要的困惑，在C++和C中，甚至是Java中常量数字应该是没有地址的，但是在python中却出现了的id，这是不是有点问题呢？

- 首先我们知道在python中所有的变量都是指向某个对象的引用（Java中不是，Java中int类型变量就是一个值，这也导致了Integer等类的出现）
- 而Number也是一个类，一个mutable类，一旦出现，他的id就不会改变

所以刚才的困惑也就解决了，当然，如果你没有使用1这个常量，那么他就不会被创建出来.

写于2017.7.16--深大南图

---
