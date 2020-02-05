# Python 3.8 新特性

## 海象运算符

> 描述: 用于赋值表达中，一次用于判断、另一次用于计算的情况，减少计算量。

> 示例: 赋值表达式可以避免调用 len() 两次:

```python
a = [1] * 20
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
```

## 仅限位置形参

```python
def f(a, b, /, c, d, *, e, f):
    """
    a 和 b 为仅限位置形参
    c 或 d 可以是位置形参或关键字形参
    e 或 f 要求为关键字形参
    """
    print(a, b, c, d, e, f)
```