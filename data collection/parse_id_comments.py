# -*- coding: utf-8 -*-
# __author__ = "zok"  362416272@qq.com
# Date: 2019-04-17  Python: 3.7
"""
这是上面一个大神的代码，我拿来自己使用的
他的GitHub地址为：https://github.com/wkunzhi/SpiderCrackDemo/tree/master/MeiTuan
-------
目标：
根据店铺获取评论
局限性：一个店铺只能获取10条评论
"""
import requests
import json
import time
import csv
import sys
# 当引用模块和当前模块不再同一个目录下时，要将引入的模块添加进来
from urllib import parse

sys.path.append(r'D:\lagua\study\coding\pythonPractice\meituanComment\meituanComment\spiders\parse_restaurant_id.py')
from parse_restaurant_id import ParseId
# 创造解析类，用来提取用户评论
class ParseComments(object):
    def __init__(self, shop_id):
        self.shop_id = shop_id# 从具有这个属性，实例需要有具体的shop_id
        self.get_data()# 规定类自带的属性
        self.coms_ = self.get_data()
   
    # 获取数据---从网页上下载数据
    def get_data(self):
        url_code = self.get_originUrl() # 获取原始的url
        # 我的ssl证书有问题，访问https会出现问题，美团支持http和https，所以最后改为http没有问题
        url = 'http://www.meituan.com/meishi/api/poi/getMerchantComment?'
        params = {  # 利用字典传入参数
            'platform': '1',
            'partner': '126',
            'originUrl': url_code, # 是字典中的一个必须的关键url
            'riskLevel': '1',
            'optimusCode': '1',
            'id': self.shop_id,  # 从终端传入的商品id
            'offset': '0',
            'pageSize': '10',
            'sortType': '1',
        }
        # 加入请求头，模拟浏览器
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        }
        response = requests.get(url=url, params=params, headers=headers) # 获得requests对象，发送网页请求，并且获得响应
        data = response.text # 我们所需要分析的数据
        self.parse(data)  # 交给下面的parse函数解析
        return self.parse(data)

    ## 获得不同商品对应的url
    def get_originUrl(self): # 获取某个餐馆的具体url----与某一家餐馆一一对应
        """编码解码
        """
        needParse = ('http://www.meituan.com/meishi/' + '%s'+ '/')%self.shop_id
        return parse.quote_plus(needParse)
        # quote_plus 函数用加号来代替URL中的空格-----构造某个商品的url

    # 对某个网页下的数据进行解析，提取出我们所想要的数据
    def parse(self, data):
        """解析数据
        """
        data_dict = json.loads(data) #是Json格式的数据 将json字符串--->json对象  
        print('parse is running....')   
        try:
            coms = [] # 某个店铺的评论，一个店铺会有 10 条
            for item in data_dict.get('data').get('comments'): # 获取数据字典中的data数据，data中也含有comments的数据             
                coms.append(item.get('comment'))                          
        except:
            print('Error!!!!!!!!!!!!!')
            print('%s'%self.shop_id)
        return coms # 将从每个店铺中获取到的评论返回，作为类的一个元素可以传到相应实例中  
        
    @staticmethod # python返回函数的静态方法，不强制传递参数
    # 函数的执行，可以不用创造实例
    def parse_time(timeStamp): # 解析时间戳，备用---
        """13位 解码时间
        """
        time_stamp = float(int(timeStamp) / 1000)
        time_array = time.localtime(time_stamp)
        return time.strftime("%Y-%m-%d %H:%M:%S", time_array)

# 数据已经在另一个文件中被解析，只需要拿出来就可以，不必自己执行函数获取
# 要在ParseId后面加上(),因为这是调用的一个类，需要继承这个类，，之后再继承这个类的属性，执行函数
ids = ParseId().getId()

# 创建实例---将数据写进csv文件中
special_shops = []
comments_ = []# 存放所有店铺的coms
for shop_id in ids:
    pc = ParseComments(shop_id)
    special_shops.append(pc)
    for v in pc.coms_:# coms是类中的一个变量，在执行parse函数时我返回了，并且将其作为这个类的一个属性，在创建实例时继承了下来
        comments_.append(v)

"""
这是改变之后的:
在写进文件夹之后直接根据相应的评论长度建立一个index，将它与相应的comments写入到csv文件中
"""
# 底下是将数据写入到csv文件中，要指明为utf-8，否则会出现乱码
with open(r'D:\lagua\study\coding\pythonPractice\MT_test.csv', 'w+', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    to_be_write = []
    index_= list(range(len(comments_))) # 序列号
    for v1,v2 in zip(index_, comments_):# 将两个列表打包
        to_be_write.append([v1, v2]) # 最后得到的是[[1,'a'],[2,'b'],[3,'c']]这样的形式，可以用writerows写进csv文件中
    writer.writerows(to_be_write)##### 注意此处写入是用的元组---用元组形式写入，事实上得到的是列表
