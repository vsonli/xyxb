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
        cls.request = HTTPRequestSession()
        cls.db = ReadMysqlData()
        my_log.info(NEW_TIME)
        my_log.info('\t\t\t\t\t')

    # *对cases列表进行拆包，获得对象，里面拿到对象.属性去做比较
    @data(*cases)
    def test_01(self,case):
        '''不同的参数导致不同的结果'''

        # if '#register_phone#' in case.data:
        #    while True:
        #        # 替换数据
        #        phone = rand_phone()
        #        sql = 'select * from member where MobilePhone = ' + phone
        #        count = self.db.find_count(sql)
        #        if count == 0:
        #            break
        #    case.data.replace('#register_phone#',phone)
        #替换数据，上面是原有的未封装前的替换数据步骤
        case.data = replace(case.data)

        #判断该条测试数据是否有sql语句
        if case.check_sql:
            sart_money = self.db.find_one(case.check_sql)[0]

        #发送请求获取结果
        url = conf.get('url','url')+case.url
        response = self.request.request(method=case.method, url=url, data=eval(case.data))

        self.db.commit()
        try:
            #校验结果码
            self.assertEqual(str(case.excepted),response.json()['code'])
            #校验数据库
            if case.check_sql:
                #执行sql语句，获取余额
                end_money = self.db.find_one(case.check_sql)[0]
                #本次充值金额
                money = eval(case.data)['amount']
                #因为数据库查的数据是dicimal类型，要强转为浮点类型
                money = decimal.Decimal(str(money))
                #判断是充值接口还是登陆接口
                if case.title == '充值_充值成功':
                    print('充值前金额{},充值后金额{},本次充值金额{}'.format(sart_money,end_money,money))
                    self.assertEqual(money,end_money - sart_money)
                else:
                    print('充值前金额{},充值后金额{},本次提现金额{}'.format(sart_money, end_money, money))
                    self.assertEqual(money,sart_money - end_money)
        except AssertionError as e:
            #测试未通过，输出日志
            my_log.error(e)
            #在excel用例文件中写入日志
            self.wb.write_data(row=case.case_id + 1,column=11,msg='Failed')
            self.wb.write_data(row=case.case_id + 1,column=10,msg=response.text)
            raise e
        else:
            #测试通过，输出日志
            my_log.info('-----测试用例：--{}--已通过----'.format(case.title))
            #在excel用例表格中写入结果
            self.wb.write_data(row=case.case_id + 1, column=11, msg='pass')
            self.wb.write_data(row=case.case_id + 1, column=10, msg=response.text)

    @classmethod
    def tearDownClass(cls):
        my_log.info('接口测试完毕')
        my_log.info('\t\t\t\t\t')
        cls.db.close()
        cls.request.close()