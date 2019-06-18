# -*- coding:utf-8 -*-
# @Time   :2019/6/4 18:53
# @File   :testcase.py
# @Author :Vsonli
import unittest
from common.readExcel import Read_r_excel
from common.logger import my_log
from ddt import ddt,data
from common.apicom import *
from common.constant import *

xlsx_name = conf.get('excels','xlsx_name')
file_name = os.path.join(DATA__DIR,xlsx_name)
sheet_name = conf.get('excels','sheet_name')
read_columns = conf.get('excels','row_num')
wb = Read_r_excel(file_name,sheet_name)
#读取Excel表格，获得里面的数据，然后在data内使用
cases = wb.r_data_obj(eval(read_columns))


'''
ddt是用来放在用例类，data放在测试用例方法上，里面的参数有几个，就代表生成多少条用例
'''
@ddt
class RegisterTestCase(unittest.TestCase):

    # *对cases列表进行拆包，获得对象，里面拿到对象.属性去做比较
    @data(*cases)
    def test_01(self,case):
        '''不同的参数导致不同的结果'''
        tokens = get_token()
        head = get_head(tokens)
        student = get_student_token()
        student_head = get_head(student)
        self.row = case.case_id + 1
        r = case.case_id
        course = {}
        result = ''
        olddata = {'groupCode':'196F0b9C1b282Da069DA0488b64834C0'}
        if (self.row >= 13 and self.row <= 21) or (self.row >= 27 and self.row <= 30):
            '''学员的token'''
            if self.row == 15:
                stu_data = {'useType':2,'groupCode':'196F0b9C1b282Da069DA0488b64834C0'}
                result = get_send_post(case.url, student_head, stu_data, 60)
            elif self.row == 18:
                result = get_send_post(case.url, student_head, course, 60)
            elif self.row == 19:
                stu_data = {'sort':1,'courseCode':course}
                result = get_send_post(case.url, student_head, stu_data, 60)
            elif self.row == 21:
                stu_data = {'status': 1, 'courseCode': course}
                result = get_send_post(case.url, student_head, stu_data, 60)
            elif self.row == 27:
                stu_data = {'courseCode':course,'sort':1}
                result = get_send_post(case.url, student_head, stu_data, 60)
            elif self.row == 28:
                stu_data = {'courseCode': course, 'status': 0}
                result = get_send_post(case.url, student_head, stu_data, 60)
            else:
                result = get_send_post(case.url, student_head, olddata, 60)
        else:
            if self.row == 4:
                couse_data = {'groupCode': '196F0b9C1b282Da069DA0488b64834C0', 'liveStatus': 1}
                course = get_course(case.url,head,couse_data,60)
                if course != None:
                    result = 200
                print(course)
            elif self.row == 7:
                tea_data = {'courseCode':course}
                result = get_send_post(case.url,head,tea_data,60)
            elif self.row == 11:
                tea_data = {'duration':180,'groupCode':'196F0b9C1b282Da069DA0488b64834C0','courseCode':course}
                result = get_send_post(case.url, head, tea_data, 60)
            elif self.row == 12:
                tea_data = course
                result = get_send_post(case.url, head, tea_data, 60)
            elif self.row == 23:
                tea_data = {'courseCode':course,'status':2,'userCode':'48D393a5aBc510B0a9601e3C1A0c9C9A'}
                result = get_send_post(case.url, head, tea_data, 60)
            elif self.row == 25:
                tea_data = {'courseCode': course, 'status': 0, 'userCode': '48D393a5aBc510B0a9601e3C1A0c9C9A'}
                result = get_send_post(case.url, head, tea_data, 60)
            elif self.row == 31:
                tea_data = {'groupCode':'196F0b9C1b282Da069DA0488b64834C0','liveStatus':0}
                result = get_send_post(case.url, head, tea_data, 60)
            elif self.row == 32:
                tea_data = {'groupCode': '196F0b9C1b282Da069DA0488b64834C0', 'duration': 471, 'courseCode': course}
                result = get_send_post(case.url, head, tea_data, 60)
            elif self.row ==2:
                result = get_send_post(case.url, head, olddata, 60)
                print(result)
            else:
                result = get_send_post(case.url,head,olddata,60)
        try:
            self.assertEqual(result,200)
        except AssertionError as e:
            result = '失败'
            my_log.error(e)
            raise e
        else:
            result = 'pass'
            my_log.info('测试结果:{}'.format(result))
            my_log.info('')

        finally:
            # 在excel表格中的第四列写入数据
            wb.write_data(row=self.row, column=4, msg=result)