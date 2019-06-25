"""
1、导入数据
2、数据放进训练器中，训练得到模型
3、运用模型，将测试数据放进模型中，预测新输入的数据是正类还是负类。
4、评估模型
"""
from data_preprocessed_final import get_preprocessed # 输入数据
from sklearn import svm # 分类器
from sklearn import metrics  # 模型评价， 混淆矩阵
# 导入数据
x_train,x_test,y_train,y_test=get_preprocessed()
# 继承类，传入不同的核函数
clf_1 = svm.SVC(C=1, kernel='rbf', gamma=20, decision_function_shape='ovr') # 使用rbf径向基函数来讲低维数据转化为高维数据，使其可分
clf_2 = svm.SVC(C=1, kernel='linear', gamma=20, decision_function_shape='ovr')
clf_3 = svm.SVC(C=1, kernel='poly', gamma=20, decision_function_shape='ovr')
clf_4 = svm.SVC(C=1, kernel='sigmoid', gamma=20, decision_function_shape='ovr')

# 对应不同的核函数， 拟合
clf_1.fit(x_train, y_train)
clf_2.fit(x_train, y_train)
clf_3.fit(x_train, y_train)
clf_4.fit(x_train, y_train)

# 预测
y_pred_1 = clf_1.predict(x_test)
y_pred_2 = clf_2.predict(x_test)
y_pred_3 = clf_3.predict(x_test)
y_pred_4 = clf_4.predict(x_test)

# 分类评估
print(metrics.classification_report(y_test,y_pred_1))
print(metrics.classification_report(y_test,y_pred_2))
print(metrics.classification_report(y_test,y_pred_3))
print(metrics.classification_report(y_test,y_pred_4))

# 混淆矩阵
print(metrics.confusion_matrix(y_test,y_pred_1))
print(metrics.confusion_matrix(y_test,y_pred_2))
print(metrics.confusion_matrix(y_test,y_pred_3))
print(metrics.confusion_matrix(y_test,y_pred_4))
