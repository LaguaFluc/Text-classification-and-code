这是关于文本分类的一个纪念。
# 文件内容简介
文件流程：[data collection](./data%20collection) --> [data process](./data%20process) --> [Classification](./Classification)


具体每个文件下的文件：

1-[data collection](./data%20collection):

[parase_id_comments.py](./data%20collection/parse_id_comments.py)获取店铺ID，方便下一步[parase_restaurant_id.py](./data%20collection/parse_restaurant_id.py)根据店铺ID来获取评论。


2-[data process](./data%20process):

[final_process_1.py](./data%20process/final_process_1.py)初步处理数据。
1. 去重，作为初始数据处理。
2. 去空tag【】【】。
3. 去除空字符串''。
得到我想要的数据，进行人工标记。

[final_process_2.py](./data%20process/final_process_2.py)数据第二步清洗。
1. 读取文本数据+相应类别，各自分别放进comments和class_的列表中。
2. 使用正则表达式去除其他符号。
3. 从停用词列表中读取数据，去除停用词，每个文本得到的剩下单词用' '空格连接起来。
4. 将分类所得到的正负文本放进不同的文档中，自己检查看大体上是否分类正确。


3-[Classification](./Classification):

[data_preprocessed.py](./Classification/data_preprocessed.py)
文件目标：拿出数据，文本数据向量化，方便放进分类器中训练。
1. 拿出由数据清洗得到的数据
2. 将文本数据转化为分类器可以识别的形式，即可以使用数值向量化程序将文本数据转化为数值数据。eg: ['你', '今天', ‘很’, '好看']---->「你 今天 很 好看」，两个文本单词之间用单词隔开.
3. 将已有的数据切分为训练数据和测试数据.
4. 数据标准化，将数据通过变换，映射到一定的范围之内，消除不同的量纲对分类性能产生影响。


[k_neighbors_test_5.py](./Classification/k_neighbors_test_5.py)
文档执行步骤：
1. 获取数据--将数据向量化--获取需要处理的矩阵--并且与y类别相对应
2. 引用knn对象，使用对象自带的分类方法
3. 将数据分为训练数据+测试数据（4：1），来检测分类器的分类效果
    - 要注意归一化处理---我使用的是Minmaxsclaer()---将数据归一化到[0,1]
        开始我觉得这样搞是可以应对bayes中出现的non-negative  的问题，结果还是爆出了这个错误。
        
        注意：这里采用不同的归一化处理的方法对最后分类的影响是不一样的。
        
        举例：假定服从高斯分布，使用z-score归一化变成均值为0，方差为1 ，最后分类得到的accuracy就比较高，关键还是要看不同的分布
            万物都有与相适应的方法嘛

        这里可以有所改进的，如果想要尝试改变不同分类器的分类效果（目的），暂时不对比各种分类器之间的分类效果，
        只考虑如何提供分类器的性能，可以先分析样本的具体特征，结合不同的归一化方法预处理
    - 使用交叉验证的方法，来使分类器更为精确----在这里我还没有使用，等使用了就将此解释去掉。


[naive_bayes_test_5.py](./Classification/naive_bayes_test_5.py)
跟KNN一样，有以下几个步骤：
1. 导入数据： 训练数据 + 测试数据
2. 将训练数据放进训练中训练，得到模型
3. 将测试数据放进模型中，得到结果
4. 评估结果，混淆矩阵。


[svm_test_4.py](./Classification/svm_test_4.py)
1. 导入数据
2. 数据放进训练器中，训练得到模型
3. 运用模型，将测试数据放进模型中，预测新输入的数据是正类还是负类。
4. 评估模型.

[Related Files](./Related%20Files):

[poId.csv](./Related%20Files/poId.csv)店铺的ID.

[MeiTuan.csv](./Related%20Files/MeiTuan.csv)根据店铺ID获取的店铺评论。

[neg_newMeiTuan.txt](./Related%20Files/neg_newMeiTuan.txt)手工标记得到的正类文本的文档。

[posi_newMeiTuan.txt](./Related%20Files/posi_newMeiTuan.txt_newMeiTuan.txt)手工标记得到的负类文本的文档。

[stopWords.txt](./Related%20Files/stopWords_3.txt)停用词文档。其中去除了一些停用词，例如不，因为如果是不好吃，去掉不就变成了好吃了。这会影响到文本的正面和负面情感，故删去。





# 论文所包含的内容
## 1、绪论背景方面的撰写
## 2、数据获取
主要参考Zok代码
## 3、数据预处理
沙漏给了我很大的帮助，再次感谢
## 4、训练数据
感谢学长们的帮助
## 5、结果评估
感谢网上提供无限资源的不知名网友们。  

---  
论文撰写：
感谢老师啊，感谢学长们啊  
最后我也谢谢自己嘿嘿。
- [x] 20 May, 2019撰写完毕
- [x] 22 May, 2019修改完毕  
- [x] 26 May, 2019CSDN记录完毕
- [x] 25 June, 2019代码提交完毕
- [x] 21 June, 2020修改部分代码规范细节，给所有文档一个解释(README.md).
- [ ] future 待继续完善  
END
