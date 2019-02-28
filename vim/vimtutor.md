# vimtutor

```
        ^
        k
< h            l >
        j
        V
```

- `x` 删除单个字符
- `dw` 删除单个单词
- `d$` 删除从`cursor`到行尾的所以字符
- `dd` 删除整行

- `i` 在cursor前进行插入
- `A` 在行末进行追加

- `2w` 向前移动两个word,可以理解为执行两次`w`

- `u` undo the last command
- `U` undo in the whole line(例如用多个`x`删除，但又想撤回的时候，就不需要按多下`u`了)

- `p`  put the previously deleted test after the cursor.
- `r<char>` 替换当前字符为`<char>`
- `ce` `c`表示`change`，是一个`operator`,`e`表示直到当前单词的尾部。
- `G` 移动到文件尾部
- `<number>G` 移动到第`number`行
- `gg` 移动到文件开头
- `/` 进行搜索模式
- `%` 将光标移动到任何括号中，按下`%`就会跳转到其对应的另一个括号上,如从`(`跳转到`)`

- `CTRL-R` undo the undo's
- `CTRL-G` show you location in file and the file status

- `:s/old/new/g` `s`表示替换，`g`表示全局，
---

### 许多`command`=`opeartor motion`如：

`d  motion`中`d`表示删除`operator`，`motion`表示`operator`会对什么进行操作。

For example:

- `dw`: `w`表示直到下一个单词的起始位置（不包含起始位置的字符），整个命令就是删除到下一个单词的起始位置。
- `d$`: `$`表示到行尾，因此整个命令就是删除到行尾的所以字符。
- `de`: `e`表示到当前单词的最后一个字符，所以整个命令就是删除到当前单词的下一个字符。

### `motion` = `number motion`

如`2w`就可以理解为执行两次`w`

### `command` = `operator number motion`

## `command` = `number command`

如`2dd`表示为删除两行






