# Python Basic

> 变量

### 快速交换

```python
a, b = 1, 2
a, b = b, a
print(a, b)
```


> 函数

### 自定义函数

```python
def fun():
    print('hello word!')

fun()
```

### 函数参数
```python
def fun(arg, *args, **kwargs):
    print(arg)
    print(args)
    print(kwargs)


fun(1, 2, 3, 2, 3, name='cao', email='chensy@qq.com')
```

> 高级函数

### `filter`
```python
ls = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x % 2 == 0, ls)))
```


> 类

### `__var__` 前后双下划线 魔法方法


### `__call__` 可调用对象

```python
class C():

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('This is class C')


print(callable(C))
c = C()
print(callable(c), c())
```
### 装饰器

```python
import time

def CalTime(fun):
    def In(x, y):
        start = time.clock()
        fun(x, y)
        end = time.clock()
        print(f'函数运行时间：{str(end - start)}')
    return In

@CalTime
def add(x, y):
    print(x + y)
add(1, 2)
```

### 类装饰器
```python
import time


class Decorator:

    def __init__(self, fun):
        self._fun = fun

    def __call__(self, *args, **kwargs):
        start = time.clock()
        self._fun(*args)
        end = time.clock()
        print(f'函数的运行时间为{str(end - start)}')


@Decorator
def add(*args):
    print(sum(args))


add(1, 2, 5, 3, 7, 4, 5)


# 等价于
add = Decorator(add)
add(1, 2, 5, 3, 7, 4, 5)
```

### 装饰器 - 类
```python
def decorator(cls):
    cls.a = 1
    cls.b = 2
    return cls

@decorator
class C:
    pass

print(C.__dict__)
```
