### 逻辑回归

* 建立逻辑回归模型
* 对模型进行评分映射

> 逻辑回归表达式

$$
y = \frac{1}{1 + e^{-\theta}} \\\\
\theta = WX + B
$$

> sigmoid函数

$$
sigmoid(x) = \frac{1}{1 + e^{-x}}
$$

> sigmoid函数的导数

$$
\begin{aligned}
\delta sigmoid(x) & = \delta{\frac{1}{1 + e^{-x}}} \\\\
& = \delta{\frac{e^{-x}}{(1 + e^{-x})^2}} \\\\
& = \delta{\frac{1}{1 + e^{-x}} * \frac{e^{-x}}{1 + e^{-x}}} \\\\
& = sigmoid(x) * \frac{1 + e^{-x} - 1}{1 + e^{-x}} \\\\
& = sigmoid(x) * (1 - sigmoid(x))
\end{aligned}
$$

> 损失函数(Cross-entropy, 交叉熵损失函数)

`信息熵:` $-PlogP$(P是概率, 小于1, 取反之后就是正数了), 
这个值代表的是信息量, 如果值越大代表对当前情况越不确定, 信息不足. 


$$
loss = -\sum{{y_t}log{y_p} + (1 - y_t)log{(1 - y_p)}}
$$

$y_t$: 真实的Y值, 需要进行独热编码

$y_p$: 预测的Y值

> 交叉熵求导

$$
\frac{\delta loss}{\delta Y_p} 
= -\frac{\delta Y_tlogY_p}{\delta Y_p} 
= \sum_n^N{-\frac{Y_i}{P_i} + \frac{1 - Y_i}{1 - P_i}}
$$

> 准确率计算

`混淆矩阵`

| T\Pre | Positive | Negative |
| :---: | :---: | :---: |
| Positive | TP | FN |
| Negative | FP | TN |

> 评估指标

`召回率计算`

$$
recall = \frac{TP}{TP + FP}
$$

`精准率计算`

$$
precision = \frac{TP}{TP + FN}
$$

### 模型评价
- KS值
- ROC曲线

描绘的是不同的截断点时，并以FPR和TPR为横纵坐标轴，描述随着截断点的变小，TPR随着FPR的变化。   
纵轴：TPR=正例分对的概率 = TP/(TP+FN)，其实就是查全率   
横轴：FPR=负例分错的概率 = FP/(FP+TN)

作图步骤：

根据学习器的预测结果（注意，是正例的概率值，非0/1变量）对样本进行排序（从大到小）
-----这就是截断点依次选取的顺序
按顺序选取截断点，并计算TPR和FPR---也可以只选取n个截断点，分别在1/n，2/n，3/n等位置
连接所有的点（TPR，FPR）即为ROC图  

### KS值

作图步骤：

根据学习器的预测结果（注意，是正例的概率值，非0/1变量）对样本进行排序（从大到小）
-----这就是截断点依次选取的顺序  
按顺序选取截断点，并计算TPR和FPR ---也可以只选取n个截断点，分别在1/n，2/n，3/n等位置  
横轴为样本的占比百分比（最大100%），纵轴分别为TPR和FPR，可以得到KS曲线  
TPR和FPR曲线分隔最开的位置就是最好的”截断点“，最大间隔距离就是KS值，
通常>0.2即可认为模型有比较好偶的预测准确性  

### 分数映射

逻辑回归方程

$$
ln\frac{p}{1-p} = w_1x_1 + w_2x_2 + ... + w_nx_n
$$

- 基础分650分
    - 好坏概率为2倍时，加50分
    - 好坏概率为4倍时，加100分
    - 好坏概率为8倍时，加150分

$$
Score = 650 + 50 log_2(\frac{1-p}{p})
$$

> 报告

- 系数、截距、变量名称
- 排序好坏捕捉率
- 分数分布、模型(变量)PSI、低分的原因、捕获率、模型KS

