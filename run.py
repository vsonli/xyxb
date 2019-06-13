# -*- coding:utf-8 -*-
# @Time   :2019/6/4 18:54
# @File   :run.py
# @Author :Vsonli
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from testcase.testcase import RegisterTestCase
from common.myConf import conf

path = conf.path1+'xyxbs\\reports\\report.html'
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(RegisterTestCase))


with open(path,'wb') as f:
    '''写入的文件名，写入的等级（2是最高的，0，1，2），报告名称，报告相关描述，测试者名称'''
    runner = HTMLTestRunner(
                            stream=f,
                            verbosity=2,
                            title='test_report',
                            description='直播相关接口的测试',
                            tester='Vson')
    runner.run(suite)