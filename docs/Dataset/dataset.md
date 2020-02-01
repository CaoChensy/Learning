# 数据原油计划

> Python Package: [data_oil](https://gitee.com/chensy_cao/data_oil.git) 😳

> 此项目旨在收集各种类型的数据集，提供给数据学习者进行使用。

> 🔨 希望各位大佬提供优质数据源，典型数据案例。

## 安装

```bash
pip install data_oil -i https://pypi.python.org/pypi
```

## 基本使用方法

```python
from data_oil import load_data

data = load_data()
(x_train, y_train), (x_test, y_test) = data.mnist()
print(x_test.shape)
```