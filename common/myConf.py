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
            self.file_path = os.path.join(CONF_DIR,'local.conf')
            self.read(os.path.join(CONF_DIR,'local.conf'), encoding='utf8')
        else:
            self.file_path = os.path.join(CONF_DIR, 'official.conf')
            self.read(os.path.join(CONF_DIR, 'official.conf'), encoding='utf8')

    def write_data(self,option,select,data):
        '''
        配置文件的写入
        :param uption:
        :param select:
        :param data:    写入数据str类型
        :return:
        '''
        self.set(option,select,data)
        with open(self.file_path,'w') as f :
            self.write(f)
conf = RonfingObj()

# a = 'x'
# #在配置文件中，找到test_data这个类，找到user_num这个键，写入str(a)这个值
# conf.write_data('test_data','user_num',str(a))