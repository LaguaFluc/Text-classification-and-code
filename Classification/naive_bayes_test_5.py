"""
跟KNN一样，有以下几个步骤：
1、导入数据： 训练数据 + 测试数据
2、将训练数据放进训练中训练，得到模型
3、将测试数据放进模型中，得到结果
4、评估结果，混淆矩阵
"""

import re,jieba
import numpy as np
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB 
# 朴素贝叶斯下面又有三个不同的分类器，他们之间的差异为：分别假设不同的数据服从高斯（正态分布）、多项式分布、伯努利分布
from sklearn import metrics # 分类评价
from data_preprocessed_final import get_preprocessed # 获取预处理得到的数据

# 导入数据
x_train,x_test,y_train,y_test=get_preprocessed()
clf_1 = GaussianNB()# 继承类
# clf_2 = MultinomialNB() # 这里会出现一个错误，说是不能为负，按照网上的方法，直接注释掉了
clf_3 = BernoulliNB()


clf_1 = clf_1.fit(x_train, y_train) # 进行拟合，训练得到模型
# clf_2 = clf_2.fit(x_train, y_train) # 进行拟合
clf_3 = clf_3.fit(x_train, y_train) # 进行拟合

y_pred_1=clf_1.predict(x_test)# 进行预测
# y_pred_2=clf_2.predict(x_test)# 进行预测
y_pred_3=clf_3.predict(x_test)# 进行预测

print(metrics.classification_report(y_test,y_pred_1))
# print(metrics.classification_report(y_test,y_pred_2))
print(metrics.classification_report(y_test,y_pred_3))
def calc_error(y_test,x_predic):
    temp = [y_t for y_t,y_p in zip(y_test,x_predic) if y_t != y_p]
    return len(temp)

print(metrics.confusion_matrix(y_test,y_pred_1))
# print(metrics.confusion_matrix(y_test,y_pred_2))
print(metrics.confusion_matrix(y_test,y_pred_3))
"""
confusion的形式为：
分类错误数量error_num = FP + FN
[[TN FP]
[FN TP]]
"""
