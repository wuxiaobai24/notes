# Python Tutorial Reading Notes

###  Source Code Encoding

- By default, Python sources files are treated as encoded in UTF-8.

- using some other encoding

  ```python
  # -*- coding: cp-1252 -*-
  ```

- With that declaration, everything in the source file will be treated as having the encoding instead of UTF-8.

  ```python
  # -*- conding: endcoding -*-
  ```


### Comment

- Comment in Python start with the hash character #, and extend to the end of the physical line.

  ```python
  spam = 1 # this is a comment
  ```

- But the hash character just a hash character.

  ```pytho
  text = '# this is not a comment'
  ```


### Using Python as a Calculator

- Division(`/`) always returns a float, but you can use the `//` operator to get an integer result.

  ```python
  In [1]: 17/3
  Out[1]: 5

  In [2]: 17.1/3
  Out[2]: 5.7

  In [3]: 17.1//3
  Out[3]: 5.0
  ```

- use `**` operator to calculate powers. ** has higher precedence than `-`.

  ```pyt
  In [4]: 5**2
  Out[4]: 25

  In [67]: -3**2
  Out[67]: -9
  ```

- In interactive mode, the last printed expression is assigned to the variable _.

  ```python
  In [5]: 1+1
  Out[5]: 2

  In [6]: _
  Out[6]: 2

  In [7]: _ + 1
  Out[7]: 3
  ```

- complex number uses the `j` or `J` suffix to indicate the imaginary part.

  ```python
  In [8]: 1 + 2J
  Out[8]: (1+2j)
  ```

### String

- String can be enclosed in single quotes`'string'` or double quotes `"string"` ,`\` can be used to escape quotes.

  ```python
  In [9]: 'some string'
  Out[9]: 'some string'

  In [10]: "some string"
  Out[10]: 'some string'

  In [11]: 'I\'am a boy.'
  Out[11]: "I'am a boy."

  In [12]: "\"Yes\", he said"
  Out[12]: '"Yes", he said'
  ```

- The `print()` function produces a more readable output, by omitting the enclosing quotes and by printing escaped the special characters.

  ```python
  In [13]: print(_)
  "Yes", he said
  ```

- If you don't want characters prefaced by `\` to be interpreted as special characters, you can use __raw strings __ by adding an `r` before the first quote.

  ```python
  In [14]: print('C:\some\name')
  C:\some
  ame

  In [15]: print(r'C:\some\name')
  C:\some\name
  ```

- Using triple-quotes:`"""..."""` or `'''...'''` can span multiple lines,and the end of lines are automatically included in the string, but it's possible to prevent this by adding a `\` at the end of the line.

  ```python
  In [18]: print('''\
  Usage thinge [OPTIONS]
          -h
          -H 
  ''')
  Usage thinge [OPTIONS]
  	-h
  	-H 
  In [19]: print(''' 
  Usage thinge [OPTIONS]
          -h
          -H 
  ''')
  								# you can find the different.
  Usage thinge [OPTIONS]
  	-h
  	-H
  ```

- Strings can be concatenated with  `+` operator,and repeated with `*`.

  ```python
  In [20]: 3 * 'ha'
  Out[20]: 'hahaha'

  In [21]: 'Hello '+'World'
  Out[21]: 'Hello World'
  ```

- Two or more string literals next to each other are automatically concatenated,but this only works with two literals, if you want to concatenate variables or a variables and a literal,you can use `+`

  ```python
  In [22]: 'Hello ''world'
  Out[22]: 'Hello world'

  In [23]: hello = 'Hello '

  In [24]: hello 'world'
    File "<ipython-input-24-b24c7c763f33>", line 1
      hello 'world'
                  ^
  SyntaxError: invalid syntax
  ```

- Strings can be **indexed(subscripted)**  with the first character having index 0. **a character is simply a string of size one**. Index may be negative numbers, to start counting from the right.`-0` is the same as `0`.

  ```python
  In [28]: word = 'Python'

  In [29]: word[0]
  Out[29]: 'P'

  In [30]: word[2]
  Out[30]: 't'

  In [31]: word[-1]
  Out[31]: 'n'

  In [32]: word[-0]
  Out[32]: 'P'
  ```

- **Slicing** is also supported.

  ```python
  In [33]: word[:2]
  Out[33]: 'Py'

  In [34]: word[2:]
  Out[34]: 'thon'

  In [35]: word[:]
  Out[35]: 'Python'

  In [36]: word[-2:]
  Out[36]: 'on'
  ```

- Attempting to use an index that is too large will result in an error.but out of range slice indexes are handled gracefully when used for slicing

  ```python
  In [37]: word[8]
  ---------------------------------------------------------------------------
  IndexError                                Traceback (most recent call last)
  <ipython-input-37-40f1e8b7180a> in <module>()
  ----> 1 word[8]

  IndexError: string index out of range
      
  In [38]: word[2:8]
  Out[38]: 'thon'

  In [39]: word[8:]
  Out[39]: ''
  ```

- Python strings cannot be changed,they are **immutable**.

  ```python
  In [40]: word[0] = 'j'
  ---------------------------------------------------------------------------
  TypeError                                 Traceback (most recent call last)
  <ipython-input-40-f14cc6f14a36> in <module>()
  ----> 1 word[0] = 'j'

  TypeError: 'str' object does not support item assignment

  In [41]: word[:2] = 'py'
  ---------------------------------------------------------------------------
  TypeError                                 Traceback (most recent call last)
  <ipython-input-41-029b668e1114> in <module>()
  ----> 1 word[:2] = 'py'

  TypeError: 'str' object does not support item assignment
  ```

- The built-in function `len()` returns the length of a string

  ```python
  In [42]: s = 'hello world'

  In [43]: len(s)
  Out[43]: 11
  ```

### Lists

- Lists might contain items of different types,but usually the items all have the same type,List can be **indexed and sliced**, All slice operator return a new list containing the requested elements,this mean that **the following slice return a new copy of the list**.And they can be concatenation by using operator `+`.

  ```python
  In [44]: squares = [1,4,9,16,25]

  In [46]: squares
  Out[46]: [1, 4, 9, 16, 25]

  In [47]: squares[0]
  Out[47]: 1

  In [48]: squares[-1]
  Out[48]: 25

  In [49]: squares[-3:]
  Out[49]: [9, 16, 25]

  In [50]: squares[:]
  Out[50]: [1, 4, 9, 16, 25]

  In [51]: squares + [1,2,3]
  Out[51]: [1, 4, 9, 16, 25, 1, 2, 3]
  ```

- LIsts are a **mutable** type , and you can add new items at the end of the list by using the `append()`

  ```python
  In [52]: squares
  Out[52]: [1, 4, 9, 16, 25]

  In [53]: squares[2] = 2

  In [54]: squares
  Out[54]: [1, 4, 2, 16, 25]

  In [55]: squares.append(99)

  In [56]: squares
  Out[56]: [1, 4, 2, 16, 25, 99]
  ```

- Assignments to slices is also possible, and **this can even change the size of the list or clear it entirely**.

  ```python
  In [56]: squares
  Out[56]: [1, 4, 2, 16, 25, 99]

  In [57]: squares[1:2] = [0,0]

  In [58]: squares
  Out[58]: [1, 0, 0, 2, 16, 25, 99]

  In [59]: squares[1:3] = []

  In [60]: squares
  Out[60]: [1, 2, 16, 25, 99]

  ```

- The built-in function `len()` also applies to lists

  ```python
  In [61]: len(squares)
  Out[61]: 5
  ```

- It is possible to **nest lists**:

  ```python
  In [62]: a = ['a','b','c']

  In [63]: n = [1,2,3]

  In [64]: x=[a,n]

  In [65]: x
  Out[65]: [['a', 'b', 'c'], [1, 2, 3]]

  In [66]: x[0]
  Out[66]: ['a', 'b', 'c']
  ```




### First Steps Towards Programming

```python
In [1]: a,b = 0,1

In [2]: while b < 10:
   ...:     print(b)
   ...:     a,b = b,a+b
   ...:     
1
1
2
3
5
8
```

- **multiple assignment** is ok!,for example ,`a,b = 0,1`

- In Python ,any non-zero integer value is true,zero is false, and anything with a non-zero length is true,empty sequences are false.

- **Indentation is Python' way of grouping statements**.and each line within a basic block must be indented by **the same amount.**

- The `print()` function has a keyword argument `end` can be used to avoid the newline after the output,  or end the output with a different string

  ```python 
  >>> a = 1
  >>> while a < 10:
  ...     print(a,end=', ')
  ...     a = a + 1
  ... 
  1, 2, 3, 4, 5, 6, 7, 8, 9, >>> 
  ```


### `if` Statements

The keyword `elif` is short for `else if`,and `if` ... `elif` ... `else` ... sequence is a substitute for the `switch` or `case` statements found in other languages.

```python
In [1]: x = 1

In [2]: if x == 0:
   ...:     print('0')
   ...: elif x == 1:
   ...:     print('1')
   ...: else:
   ...:     pass
   ...: 
1
```

### for Statements

Python's `for` statement iterates over the item of any sequence(a list or string), in the order that they appear in the sequence:

```python
In [1]: word = ['a','b','c']

In [2]: for w in word[:]:
   ...:     print(w)
   ...:     
a
b
c

```

If you do need to iterate over a sequence of numbers, the built-in-function `range()` comes in handy.and it's possible to let the range start at another number, or to specify a different increment.

```python
In [3]: for i in range(5):
   ...:     print(i)
   ...:     
0
1
2
3
4

In [4]: for i in range(5,10):
   ...:         print(i)
   ...:             
5
6
7
8
9

In [5]: for i in range(10,20,2):
   ...:         print(i)
   ...:                     
10
12
14
16
18

In [6]: for i in range(10,0,-1):
   ...:         print(i)
   ...:         
10
9
8
7
6
5
4
3
2
1
```

You can combine `range()` and `len()` to iterate over the indices of a sequence:

```python
In [7]: a = ['Wu','Xiao','Bai']

In [8]: for i in range(len(a)):
   ...:     print(i,a[i])
   ...:     
0 Wu
1 Xiao
2 Bai

In [10]: list(enumerate(a))
Out[10]: [(0, 'Wu'), (1, 'Xiao'), (2, 'Bai')]

```

In many ways the object return by  `range()` behaves as if it is a list, but in fact it isn't. **It is an object which return the successive items of the desired sequence when you iterate over it**,We say such an object is **iterable**,and creates lists from iterables by `list()`

```python
In [11]: range(10)
Out[11]: range(0, 10)

In [12]: list(range(10))
Out[12]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```

### `break` and `continue` Statement, and `else` Clauses on Loops

- `break` statement break outs of the innermost enclosing `for` or `while` loop.
- Loop statements may have an `else` clauses,it is executed when the loop terminates through exhaustion of the list(with `for`) or when the condition becomes false(with `while`)