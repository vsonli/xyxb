# -*- coding:utf-8 -*-
# @Time   :2019/6/4 14:41
# @File   :logger.py
# @Author :Vsonli
import logging
from common.myConf import conf
from common.constant import *


log_name = conf.get('logs','logs_name')
level = conf.get('logs','level')
sh_level = conf.get('logs','sh_level')
fh_level = conf.get('logs','fh_level')
path_name = conf.get('logs','log_path_name')
log_file_path = os.path.join(LOG_DIR,path_name)
class MyLogging(object):
    def __new__(cls, *args, **kwargs):
        my_log = logging.getLogger(log_name)
        my_log.setLevel(level)

        l_s = logging.StreamHandler()
        l_s.setLevel(sh_level)  # INFO等级以上的都输出到控制台...

        l_f = logging.FileHandler(log_file_path, encoding='utf-8')
        l_f.setLevel(fh_level)  # DEBUG等级以上的都输出到日志文件

        my_log.addHandler(l_s)
        my_log.addHandler(l_f)

        format = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        format = logging.Formatter(format)
        l_s.setFormatter(format)
        l_f.setFormatter(format)
        return my_log

    def debug(self,msg):
        self.my_log.debug(msg)

    def info(self,msg):
        self.my_log.info(msg)

    def warning(self,msg):
        self.my_log.warning(msg)

    def error(self,msg):
        self.my_log.error(msg)

    def critical(self,msg):
        self.my_log.critical(msg)

    def exception(self,msg):
        '''异常信息收集'''
        self.my_log.exception(msg)
my_log = MyLogging()
