# 这里是机器学习专辑



## Scikit-learn

> 模型选择

```python
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.3)
```

> 混淆矩阵：

```python
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)
```

> 评估方法：

```python
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
```

> imbalanced-learn

imbalanced-learn（imblearn）提供了多种方法来进行欠采样和过采样。
- 使用 Tomek Links 进行欠采样：
imbalanced-learn 提供的一种方法叫做 Tomek Links。
Tomek Links 是邻近的两个相反类的例子。
在这个算法中，我们最终从 Tomek Links 中删除了边界大多数元素，这为分类器提供了一个更好的决策边界。

```python
from imblearn.under_sampling import TomekLinks

tl = TomekLinks(return_indices=True, ratio= majority )
X_tl, y_tl, id_tl = tl.fit_sample(X, y)
```

- 使用 SMOTE 进行过采样：
在 SMOE（Synthetic Minority Oversampling Technique）中，
我们在现有元素附近合并少数类的元素。

```python
from imblearn.over_sampling import SMOTE

smote = SMOTE(ratio=minority )
X_sm, y_sm = smote.fit_sample(X, y)
```

> 采样率与模型评估指标

```python
# 引入 TLGloun 模块
from TLGloun.TLGloun import LoadData
from collections import defaultdict
from TLGloun.TLGloun.DataPreparing import upsampling
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import *
import numpy as np


# 载入 测试数据
load_data = LoadData()
df_bank = load_data.BankData()

df_bank = df_bank.select_dtypes(int)

test = df_bank[df_bank.target == 0].sample(frac=0.2)
test = test.append(df_bank[df_bank.target == 1].sample(frac=0.2))
test_y = test.pop('target')

df_bank.drop(test.index, axis=0, inplace=True)

res = defaultdict(list)
for rate in np.arange(0.1, 1.1, 0.1):
    df = upsampling(df=df_bank.copy(), up_rate=rate)
    y = df.pop('target')
    model = LogisticRegression(C=0.1, solver='newton-cg')
    model = model.fit(df, y)
    
    predict_binary = model.predict(test)
    predict_proba = model.predict_proba(test)
    
    res['upsampling_rate'].append(rate)
    res['accuracy'].append(accuracy_score(test_y, predict_binary))
    res['auc'].append(roc_auc_score(test_y, predict_proba[:, 1]))
    res['recall'].append(recall_score(test_y, predict_binary))
    
    fpr, tpr, _ = roc_curve(test_y, predict_proba[:, 1])
    model_ks = abs(fpr - tpr).max()
    res['ks'].append(model_ks)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.title('Effect of upsampling rate on model results.')

for item in res.items():
    if item[0] != 'upsampling_rate':
        plt.plot(res['upsampling_rate'], item[1], label=item[0])

plt.xlabel('upsampling rate')
plt.ylabel('metrcs')
plt.legend()
plt.show()
```