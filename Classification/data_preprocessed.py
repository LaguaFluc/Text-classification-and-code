# 文件目标：
# 1、拿出由数据清洗得到的数据
# 2、将文本数据转化为分类器可以识别的形式，即可以使用数值向量化程序将文本数据转化为数值数据。eg: ['你', '今天', ‘很’, '好看']---->「你 今天 很 好看」，两个文本单词之间用单词隔开
# 3、将已有的数据切分为训练数据和测试数据
# 4、数据标准化，将数据通过变换，映射到一定的范围之内，消除不同的量纲对分类性能产生影响。

import jieba
import numpy as np

def get_preprocessed(): 
    max_f = 200  
    """步骤1"""
    from last_process_2 import noStopWord_comments,noStopWord_class # import评论数据所在的模块
    import re 
    from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer # 将文本数据转化为数值数据的模块
    from sklearn.decomposition import PCA # 以后尝试使用pca降维
    from sklearn.model_selection import train_test_split # 将已有数据转切分为：训练集 + 测试集
    from sklearn import preprocessing # 数据的标准化
    # 将开始的字符串用空格隔开
    def get_split(x):
        temp = [v for v in re.split(' ',x) if v is not '']
        return temp
    def joinData(data_to_join):# 空字符串将文本隔开
        temp = [' '.join(x) for x in data_to_join]
        return temp    
    """步骤2"""
    corpus = joinData([get_split(v) for v in noStopWord_comments]) # 得到的是一个列表
    tfidf = TfidfVectorizer()
    retfidf = tfidf.fit_transform(corpus)

    
    input_data_matrix = retfidf.toarray() # 提取出上一步得到的数值矩阵
    """步骤3"""
    x_train,x_test,y_train,y_test=train_test_split(input_data_matrix,noStopWord_class,test_size=0.2,random_state=400)
    """
    """
    # 将上面的数据标准化处理
    # -----------------------
    # stander=preprocessing.StandardScaler()
    # x_train = stander.fit_transform(x_train)
    # x_test = stander.fit_transform(x_test)
    """步骤4"""
    max_min=preprocessing.MinMaxScaler()
    x_train = max_min.fit_transform(x_train)
    x_test = max_min.fit_transform(x_test)
    # ---------------------
    # 主成分降维
    pca = PCA(n_components=0.9)
    x_train,x_test = pca.fit_transform(x_train),pca.transform(x_test)
    # 对前面的一个进行拟合，后面直接引用前面拟合得到的参数进行调配
    # input_data_matrix=pca.fit_transform(input_data_matrix)
    # train_data = input_data_matrix
    # train_target = noStopWord_class
    # x=train_data
    # y=train_target


    return x_train,x_test,y_train,y_test 
