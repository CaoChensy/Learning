## python 内置模块

### pip 清华镜像配置

```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```
> 官方镜像 https://pypi.python.org/pypi

> 微软 Windows pkg [windows package site](https://www.lfd.uci.edu/~gohlke/pythonlibs/)

### ast 模块

```python
# 使用Python的ast模块(抽象语法树)将其转换为有用的内容
import ast

# literal_eval() 允许您计算包含Python文字或生成器的字符串
ast.literal_eval('[1, 2, 3]')
```

### pickle 模块

```python
import pickle

class Pk:
    
    def __init__(self):
        self.name = 'Pickle File'
    
    def saveDB(self, filename, data):
        with open(filename, 'wb+') as f:
            pickle.dump(data, f)

    def loadDB(self, filename):
        with open(filename, 'rb') as f:
            data = pickle.load(f, encoding='gbk')
        return data
```

### re 正则表达式

```python
# 匹配全部中文
import re
m = re.findall('[\u4e00-\u9fa5]+', content)
```

