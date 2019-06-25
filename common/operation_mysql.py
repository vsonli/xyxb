# -*- coding:utf-8 -*-
# @Time   :2019/6/19 11:46
# @File   :operation_mysql.py
# @Author :Vsonli
'''
操作mysql
    方便读取数据
    方便管理测试环境
'''
import pymysql
from common.myConf import conf

class ReadMysqlData(object):
    def __init__(self):
        self.con = pymysql.connect(
            host=conf.get('sql', 'host'),
            user=conf.get('sql', 'user'),
            password=conf.get('sql', 'password'),
            port=3306,
            database=conf.get('sql', 'database'),
            charset='utf8'
        )
        self.cur = self.con.cursor()

    def find_one(self,sql):
        '''查找并返回找到的第一条数据'''
        self.cur.execute(sql)
        return self.cur.fetchone()

    def find_all(self,sql):
        '''查找并返回所有数据'''
        self.cur.execute(sql)
        return self.cur.fetchone()

    def commit(self):
        self.con.commit()

    def find_count(self,sql):
        '''查找数据存在的条数'''
        count = self.cur.execute(sql)
        return count

    def close(self):
        '''断开连接'''
        self.cur.close()
        self.con.close()

if __name__ == '__main__':
    db = ReadMysqlData()
    sql = 'SELECT LeaveAmount FROM member WHERE MobilePhone = 13059285932'
    rs = db.find_one(sql)
    print(rs[0])