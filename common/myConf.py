# -*- coding:utf-8 -*-
# @Time   :2019/6/4 14:40
# @File   :myConf.py
# @Author :Vsonli
'''配置文件'''


import configparser
from common.constant import *

class RonfingObj(configparser.ConfigParser):
    def __init__(self):
        super().__init__()
        '''读取env，如果是1则读取测试环境的配置，否则就是生产环境'''
        r = configparser.ConfigParser()
        r.read(os.path.join(CONF_DIR, 'env.conf'), encoding='utf8')
        switch = r.get('env','switch')
        if switch == '1':
            self.read(os.path.join(CONF_DIR,'local.conf'), encoding='utf8')
        else:
            self.read(os.path.join(CONF_DIR, 'official.conf'), encoding='utf8')
conf = RonfingObj()