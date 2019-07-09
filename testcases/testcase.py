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


@ddt
class RegisterTestCase(unittest.TestCase):
    wb = Read_r_excel(file_name, sheet_name)
    cases = wb.r_data_obj(read_columns)


    @classmethod
    def setUpClass(cls):
        cls.request = HTTPRequest()
        cls.db = ReadMysqlData()
        login_url = conf.get('url', 'loginurl')
        tea_name = conf.get('url', 'tea_name')
        tea_pwd = conf.get('url', 'tea_pwd')
        stu_name = conf.get('url', 'stu_name')
        stu_pwd = conf.get('url', 'stu_pwd')
        cls.url = conf.get('url','url')
        tea = cls.request.get_head(login_url, uname=tea_name, pwd=tea_pwd)
        stu = cls.request.get_head(login_url, uname=stu_name, pwd=stu_pwd)
        course_code = cls.request.get_course_code(url=cls.url+'specialColumnCenter/setLiveStatus', head=tea, data={'groupCode':'196F0b9C1b282Da069DA0488b64834C0','liveStatus':1})
        setattr(ConText, 'tea', str(tea))
        setattr(ConText, 'stu', str(stu))
        try:
            setattr(ConText, 'course_code', str(course_code))
        except Exception as e:
            my_log.info('拿不到课程，结果为：', str(course_code))
        my_log.info(NEW_TIME)
        my_log.info('\t\t\t\t\t')


    @data(*cases)
    def test_01(self,case):
        '''准备数据'''
        url = str(conf.get('url','url')) + str(case.url)
        case.data = replace(case.data)
        case.head = replace(case.head)
        case_id  = case.case_id
        case_id = case_id + 1

        '''发送请求获取结果'''
        response = self.request.request(method=case.method, url=url,headers=eval(case.head), data=eval(case.data))
        print('返回的数据：'+str(response.text))
        code = response.json()['code']

        '''对比结果'''
        try:
            self.assertEqual(str(case.excepted),str(code))
            print('当前行号：'+str(case_id))
        except AssertionError as e:
            my_log.error(e)
            self.wb.write_data(row=case_id, column=10, msg='error')
            self.wb.write_data(row=case_id, column=11, msg=response.text)
            raise e
        else:
            my_log.info('-----测试用例：--{}--已通过----'.format(case.title))
            self.wb.write_data(row=case_id, column=10, msg='pass')
            self.wb.write_data(row=case_id, column=11, msg=response.text)

    @classmethod
    def tearDownClass(cls):
        my_log.info('接口测试完毕')
        my_log.info('\t\t\t\t\t')
        cls.db.close()
        # cls.request.close()