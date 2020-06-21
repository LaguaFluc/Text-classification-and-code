"""
1、去重，作为初始数据处理
2、去空tag【】【】
3、去除空字符串''
得到我想要的数据，进行人工标记
————————————————————
"""
import csv
import re
# 将数据全部都存放再一个列表中

class InitialProcess(object):
    path_initial = r'D:\lagua\study\coding\pythonPractice\DataProcess\MT.csv' # 从美团上获取的初始文本---经过修改，得到也是带有index的文本
    path_meituan = r'D:\lagua\study\coding\pythonPractice\DataProcess\MeiTuan.csv'# 数据处理第一道得到的index文本
    # 去重
    def noRepeat(self, x):
        uni = []
        for v in x:
            if v not in uni:
                uni.append(v)
        return uni
    # 去除只带有标签的评论
    def noTags(self, x):
        def f_replace(x):
            temp =  x.replace('【口味】','').replace('【环境】','').replace('【服务】','').replace('【等位】','').replace('\n','').strip()
            return temp
        return [f_replace(v) for v in x]
    # 将空字符串去掉
    def noVocant(self, x):
        temp = [v for v in x if v is not '']
        return temp
    # 读取之前获取的数据
    def getData(self, path):
        seg_all = []
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for line in reader:
                seg_all.append(line[1])
        print("列表说：我将csv中的数据搞到手啦") # 仅仅获取评论文本内容，在csv文件每一行的第二列
        return self.noRepeat(seg_all)
    
    def get_index(self, x):
        temp = [i for i,v in enumerate(x) if v=='']
        return temp

    # 将文件写进csv文件中
    def writeCSV(self, path2, data):
        with open(path2, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            for k,v in enumerate(data):
                writer.writerow([k,v])

    def do_thisMethod(self):
        data = self.getData(self.path_initial)# 获取数据，顺便去重
        data_noTag = self.noTags(data)# 去除标签
        data_noVocant = self.noVocant(data_noTag) # 去除上一步可能得到的空字符串
        self.writeCSV(self.path_meituan,data_noVocant) # 写进文档存储，以后就在这里面提取数据，进一步处理
IniPro = InitialProcess()# 继承类
IniPro.do_thisMethod()# 实例化之后使用类中的方法
