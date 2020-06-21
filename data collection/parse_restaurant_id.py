# -*- coding: utf-8 -*-
# __author__ = "zok"  362416272@qq.com
# Date: 2019-04-17  Python: 3.7
"""
这是上面一个大神的代码，我拿来自己使用的
他的GitHub地址为：https://github.com/wkunzhi/SpiderCrackDemo/tree/master/MeiTuan
-------
创建一个类，获取店铺id使用
在之后餐馆解析时，继承此类，使用getId获取店铺Id
"""
import requests
import json
import re
import csv
# 目标：创建一个类，其中有一个属性，是一个函数，可以提取餐馆的id
class ParseId(object):
    # 设置请求头
    def __init__(self):
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        }
        self.urls = self.getUrl()
        self.headers = headers
    # 获取这些网页
    def getUrl(self):
        urls = []
        for i in range(1,60):
            urls.append(('https://yt.meituan.com/meishi/c17/pn'+'%s'+"/")%(i))
        return urls    
    def getId(self):
        id_list = []
        k = 1
        for v in self.urls:
            html = requests.get(v, headers = self.headers)
            # 进行正则匹配，寻求店铺id信息
            re_info = re.compile(r'\"poiId\":(\d{4,})')
            id = re_info.findall(html.text)# 获得的是列表            
            # 想利用writerows将列表添加到csv文件中
            for v in id:
                id_list.append((k, v))
                k+=1
        # 将店铺ID保存到CSV文件中
        with open(r'D:\lagua\study\coding\pythonPractice\meituanComment\poId.csv', 'w+', newline="") as f:
            writer = csv.writer(f)          
            writer.writerows(id_list)        
        temp_id = []
        for il in id_list:
            temp_id.append(il[1])
        return temp_id

# @staticmethod

############ 测试 ################
# a = ParseId()
# print(a.getId())

            

            # 先生成标题
            # 第一个是索引
            # 第二个是店铺id
            # 再加上内容
        
