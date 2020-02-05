# itertools 高效迭代

> 迭代器

```python
# 返回累加和或其他二元函数的累加结果
accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
# 链式迭代
chain('ABC', 'DEF') --> A B C D E F
# Mark
compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
# 首次真值测试失败开始迭代
dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
# 为假值的元素
filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
# 根据key(v)值分组的迭代器
groupby()
# seq[start:stop:step]中的元素
islice('ABCDEFG', 2, None) --> C D E F G
# 某种map运算 
starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
# 为真时停止
takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
# it1, it2, ... itn 将一个迭代器拆分为n个迭代器
tee()
# 某种匹配
zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
```

> 无穷迭代（字面意思）
```python
count()
cycle()
repeat()
```

> 排列组合

```python
import itertools
# 有重复的排列
print(list(itertools.product('1234', repeat = 2))) 
# 无重复的排列
print(list(itertools.permutations('1234', 2))) 
# 无重复的组合
print(list(itertools.combinations('1234', 2))) 
# 有重复的组合
print(list(itertools.combinations_with_replacement('1234', 2))) 
```

--- 
> 📚 reference

[1] [Python 官网](https://docs.python.org/zh-cn/3.7/library/itertools.html#itertools.count)
