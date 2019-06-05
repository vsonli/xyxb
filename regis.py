# -*- coding:utf-8 -*-
# @Time   :2019/6/4 18:53
# @File   :regis.py
# @Author :Vsonli
import requests

def register(url,head,data,timeout):
    result = requests.post(url, headers=head, data=data, timeout=timeout).status_code
    return result