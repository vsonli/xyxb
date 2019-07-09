# -*- coding:utf-8 -*-
# @Time   :2019/6/24 16:47
# @File   :otherConfig.py
# @Author :Vsonli
import re
from common.myConf import *

class ConText:
    pass
'''
使用正则表达式替换参数的方法
    替换用例中的参数
    简化替换流程

思路
    获取用例数据
    判断该条数据中是否有需要替换的数据
    调用方法进行替换数据
'''
def replace(data):
    '''
    用例参数的替换
    :param data:用例的参数
    :return:
    '''
    p = r'#(.+?)#'
    data = str(data)
    # 判断该用例参数中是否存在需要替换的数据
    while re.search(p, data):
        # 去配置文件中获取要替换的数据
        key = re.search(p, data).group(1)
        try:
            value = conf.get('test_data', key)
        except:
            # 获得临时生成的数据
            value = getattr(ConText, key)
        # 替换
        data = re.sub(p, value, data, count=1)
    return data

