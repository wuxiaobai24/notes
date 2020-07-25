# vimtutor

> `vimtutor`的简单记录

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
- `a` 在cursor后进行插入
- `A` 在行末进行追加
- `o` 在当前行下方插入一行
- `O` 在当前行上方插入一行

- `2w` 向前移动两个word,可以理解为执行两次`w`

- `u` undo the last command
- `U` undo in the whole line(例如用多个`x`删除，但又想撤回的时候，就不需要按多下`u`了)

- `p`  put the previously deleted test after the cursor.
- `r<char>` 替换当前字符为`<char>`
- `R` 进入替换模式
- `ce` `c`表示`change`，是一个`operator`,`e`表示直到当前单词的尾部。
- `G` 移动到文件尾部
- `<number>G` 移动到第`number`行
- `gg` 移动到文件开头
- `/` 向下进行搜索
- `?` 向上进行搜索
- `%` 将光标移动到任何括号中，按下`%`就会跳转到其对应的另一个括号上,如从`(`跳转到`)`

- `CTRL-R` undo the undo's
- `CTRL-G` show you location in file and the file status
- `CTRL-O` take you back the older postion
- `CTRL-I` take you back the newer postion

- `:s/old/new/` 替换当前行出现的第一个`old`为`new`
- `:s/old/new/g` 替换当前行所有的`old`为`new`
- `:#,#s/old/new/g` 这里的`#,#`用来行数范围，修改这些行的所有`old`为`new`
- `:%s/old/new/g` 修改整个文件中的`old`为`new`
- `:%s/old/new/gc` 修改整个文件中的`old`为`new`,并给出提示

- `:w test` 另存为`test`

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

## 执行外部命令

`:!<cmd>` 如`!ls`

## `v`进行可视模式

可视模式下`:w TEST`可以将选中的文件剪切到`TEST`文件中

`:r TEST` 恢复`TEST`文件到当前位置（即从TEST中读取文本并写入）
`:r ls` 将ls的输出写入到当前位置


## use `y` operator to copy it and `p` paste it.

- 可以使用可视模式来选中要复制的文本
- 也可以把`y`当成`operator`来选，如`yw`
- 用`p`粘贴

# 搜索
- `/` 向下进行搜索
- `?` 向上进行搜索

`set ic` 设置搜索忽略大小写（如搜索`ignore`，设置后可以匹配`Ignore`), `set noic`取消
`set hls` 设置搜索结果高亮，`nohlsearch`取消高亮
`set ic` partical matches for a search pharse

# `:help`帮助系统

`:help w`
`:`后`CTRL-D`可以看所有候选命令，用`tab`进行切换选择
