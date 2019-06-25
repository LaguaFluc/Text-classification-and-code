# -*- coding:utf-8 -*-
"""
文档执行步骤：
1、获取数据--将数据向量化--获取需要处理的矩阵--并且与y类别相对应
2、引用knn对象，使用对象自带的分类方法
3、将数据分为训练数据+测试数据（4：1），来检测分类器的分类效果
    （1）要注意归一化处理---我使用的是Minmaxsclaer()---将数据归一化到[0,1]
        开始我觉得这样搞是可以应对bayes中出现的non-negative  的问题，结果还是爆出了这个错误
        注意：这里采用不同的归一化处理的方法对最后分类的影响是不一样的
            举例：假定服从高斯分布，使用z-score归一化变成均值为0，方差为1 ，最后分类得到的accuracy就比较高，关键还是要看不同的分布
                万物都有与相适应的方法嘛
            这里可以有所改进的，如果想要尝试改变不同分类器的分类效果（目的），暂时不对比各种分类器之间的分类效果，
            只考虑如何提供分类器的性能，可以先分析样本的具体特征，结合不同的归一化方法预处理
    （2）使用交叉验证的方法，来使分类器更为精确----在这里我还没有使用，等使用了就将此解释去掉
"""

import jieba
from sklearn import metrics # 评价分类好坏的包
from data_preprocessed_final import get_preprocessed   # 导入预处理得到的数据  
max_f = 200 # 维度控制 max features
"""
这里直接找寻最好的K，有些许的粗暴，不过也能够理解，因为我们无法通过眼睛观察看到找到最好的K是啥
"""
def find_best_k(max_f):
    x_train,x_test,y_train,y_test=get_preprocessed() # 获取数据
    from sklearn.neighbors import KNeighborsClassifier # 引进分类器
    # 寻找最好的k
    best_k=-1 # 初始化K
    best_score=0
    for i in range(1,11):
        knn_clf=KNeighborsClassifier(n_neighbors=i) # 继承一个类，传入参数k值为i
        knn_clf.fit(x_train,y_train) # 调用类中的方法fit----训练模型
        scores=knn_clf.score(x_test,y_test) # 模型得分
        y_pred = knn_clf.predict(x_test) # 应用模型，预测
        if scores>best_score:
            best_score=scores
            best_k=i
            best_y_pred = y_pred
            
    # 评价报告，有accuracy, precision, recall, f1-score
    # 上面是关于正类的评价
    # 下面是关于负类的评价
    print(metrics.classification_report(y_test,best_y_pred))        
    print('最好的k为:%d,最好的得分为:%.4f'%(best_k,best_score)) 
    # 计算分类错误的个数
    def calc_error(y_test,x_predic):
        temp = [y_t for y_t,y_p in zip(y_test,x_predic) if y_t != y_p]
        return len(temp)
    class_error_num_1 = calc_error(y_test,best_y_pred)
    print('Error Num:--------',class_error_num_1)  
    return (best_k,best_score)

find_best_k(max_f)
