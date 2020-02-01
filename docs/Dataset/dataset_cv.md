### Mnist 手写数字数据集

> 简介

- 数据来源：
- 数据规模：

> 导入方式

```python
from data_oil import load_data

data = load_data(tag='cv', file_name='mnist')
(x_train, y_train), (x_test, y_test) = data.mnist()
```

> 展示方式

```python
data.show()
```

> 可用基本模型

```python
data.mnist.model()
```

### Fashion-Mnist 数据集

> 简介

> 导入方式

```python
from data_oil import load_data

data = load_data(tag='cv', file_name='fashion_mnist')
(x_train, y_train), (x_test, y_test) = data.fashion_mnist()
```

> 展示方式

```python
data.show()
```

> 可用基本模型

```python
data.mnist.model()
```
