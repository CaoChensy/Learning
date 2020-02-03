# 这里是机器学习专辑
> 等待建设……

# Scikit-learn

### 模型选择

```python
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.3)
```

### 混淆矩阵：

```python
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)
```

### 评估方法：

```python
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
```







