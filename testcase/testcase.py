# -*- coding:utf-8 -*-
# @Time   :2019/6/4 18:53
# @File   :testcase.py
# @Author :Vsonli
import unittest
from regis import register as reg
from common.readExcel import Read_r_excel
from common.myConf import conf
from common.logger import my_log
from ddt import ddt,data

xlsx_name = conf.get('excels','xlsx_name')
file_name = conf.path1+'data\\'+xlsx_name
sheet_name = conf.get('excels','sheet_name')
read_columns = conf.get('excels','row_num')
wb = Read_r_excel(file_name,sheet_name)
#读取Excel表格，获得里面的数据，然后在data内使用
cases = wb.r_data_obj(read_columns)

'''
ddt是用来放在用例类，data放在测试用例方法上，里面的参数有几个，就代表生成多少条用例
'''
@ddt
class RegisterTestCase(unittest.TestCase):

    def setUp(self):
        print('开始执行单元测试')

    def tearDown(self):
        print('单元测试结束运行')

    # *对cases列表进行拆包，获得对象，里面拿到对象.属性去做比较
    @data(*cases)
    def test_01(self,case):
        '''不同的参数导致不同的结果'''
        self.row = case.case_id + 1
        res = reg(*eval(case.data))
        print(res)
        try:
            self.assertEqual(eval(case.expected),res)
        except AssertionError as e:
            res = '失败'
            my_log.error(e)
            raise e
        else:
            res = 'pass'
            my_log.info('测试结果:{}'.format(res))
        finally:
            # 在excel表格中的第四列写入数据
            wb.write_data(row=self.row, column=4, msg=res)