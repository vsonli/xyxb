# -*- coding:utf-8 -*-
# @Time   :2019/6/12 18:53
# @File   :constant.py
# @Author :Vsonli
'''常量配置'''

import os

#获取项目目录的根路径(获得当前文件的上级再上级目录)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#获取配置文件存放的目录路径
CONF_DIR = os.path.join(BASE_DIR,'CONF')

#日志存放的文件目录路径
LOG_DIR = os.path.join(BASE_DIR,'logs')

#excel数据存放的目录路径
DATA__DIR = os.path.join(BASE_DIR,'data')

#测试用例存放的目录路径
CASE_DIR = os.path.join(BASE_DIR,'testcases')

#测试报告存放的目录路径
REPORT_DIR = os.path.join(BASE_DIR,'reports')