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

> python 静态方法

```python
class C(object):
    @staticmethod
    def f():
        print('runoob')


print(C.f())  # 静态方法无需实例化
cobj = C()
print(cobj.f())  # 也可以实例化后调用
```

```python
# staticmethod 参数要求是 Callable, 也就是说 Class 也是可以的：
class C1(object):
    @staticmethod
    class C2(object):
        def __init__(self, val = 1):
            self.val = val
        def shout(self):
            print("Python世界第%d!"%self.val)
tmp = C1.C2(0)
print(type(tmp))    # 输出 : <class '__main__.C1.C2'>
tmp.shout()         # 输出 : Python世界第0!
```

> classmethod

- classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，
类的方法，实例化对象等。

```python
class A(object):
    bar = 1
    def func1(self):  
        print ('foo') 
    @classmethod
    def func2(cls):
        print ('func2')
        print (cls.bar)
        cls().func1()   # 调用 foo 方法
 
A.func2()               # 不需要实例化
```

```python
class A(object):

    # 属性默认为类属性（可以给直接被类本身调用）
    num = "类属性"

    # 实例化方法（必须实例化类之后才能被调用）
    def func1(self): # self : 表示实例化类后的地址id
        print("func1")
        print(self)

    # 类方法（不需要实例化类就可以被类本身调用）
    @classmethod
    def func2(cls):  # cls : 表示没用被实例化的类本身
        print("func2")
        print(cls)
        print(cls.num)
        cls().func1()

    # 不传递传递默认self参数的方法（该方法也是可以直接被类调用的，但是这样做不标准）
    def func3():
        print("func3")
        print(A.num) # 属性是可以直接用类本身调用的
    
# A.func1() 这样调用是会报错：因为func1()调用时需要默认传递实例化类后的地址id参数，如果不实例化类是无法调用的
A.func2()
A.func3()
```