# -*- coding:utf-8 -*-
# @Time   :2019/6/4 14:43
# @File   :testcase.py
# @Author :Vsonli
import unittest,random,decimal
from common.readExcel import Read_r_excel
from librarys.ddt import ddt,data
from common.http_request import *
from common.operation_mysql import *
from common.otherConfig import *

xlsx_name = conf.get('excels','xlsx_name')
file_name = os.path.join(DATA__DIR,xlsx_name)
sheet_name = conf.get('excels','sheet_name')
read_columns = conf.get('excels','row_num')


def rand_phone():
    phone = '134'
    for i in range(8):
        i = random.randint(0, 9)
        phone += str(i)
    return phone

'''
ddt是用来放在用例类，data放在测试用例方法上，里面的参数有几个，就代表生成多少条用例
'''
@ddt
class RegisterTestCase(unittest.TestCase):
    wb = Read_r_excel(file_name, sheet_name)
    # 读取Excel表格，获得里面的数据，然后在data内使用
    cases = wb.r_data_obj(read_columns)


    @classmethod
    def setUpClass(cls):
        # 只会创建一个request，如果用self的话，就会多少条用例，创建多少个对象，影响性能
        cls.request = HTTPRequest()
        cls.db = ReadMysqlData()
        my_log.info(NEW_TIME)
        my_log.info('\t\t\t\t\t')

    # *对cases列表进行拆包，获得对象，里面拿到对象.属性去做比较

    @data(*cases)
    def test_01(self,case):
        '''准备数据'''
        url = conf.get('url','url') + case.url
        login_url = conf.get('url', 'loginurl')
        tea_name = conf.get('url','tea_name')
        tea_pwd = conf.get('url','tea_pwd')
        stu_name = conf.get('url','stu_name')
        stu_pwd = conf.get('url','stu_pwd')
        tea = self.request.get_head(login_url,uname=tea_name,pwd=tea_pwd)
        stu = self.request.get_head(login_url,uname=stu_name,pwd=stu_pwd)
        setattr(ConText,'tea',tea)
        setattr(ConText,'stu',stu)
        case.data = replace(case.data)
        case.head = replace(case.head)

        '''发送请求获取结果'''
        if self.case_id + 1 == 3:
            course_code = self.request.get_course_code(url=url,head=case.head,data=case.data)
            setattr(ConText,'course_code',course_code)

        response = self.request.request(method=case.method,url=url,data=data)
        code = response.json()['code']

        '''对比结果'''
        try:
            self.assertEqual(str(case.excepted),code)
        except AssertionError as e:
            my_log.error(e)
            self.wb.write_data(row=case.case_id + 1, column=10, msg='error')
            self.wb.write_data(row=case.case_id + 1, column=11, msg=response.text)
            raise e
        else:
            my_log.info('-----测试用例：--{}--已通过----'.format(case.title))
            self.wb.write_data(row=case.case_id + 1, column=10, msg='pass')
            self.wb.write_data(row=case.case_id + 1, column=11, msg=response.text)

    @classmethod
    def tearDownClass(cls):
        my_log.info('接口测试完毕')
        my_log.info('\t\t\t\t\t')
        cls.db.close()
        cls.request.close()