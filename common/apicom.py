# -*- coding:utf-8 -*-
# @Time   :2019/6/4 18:44
# @File   :apicom.py
# @Author :Vsonli
import requests
from common.myConf import conf

def get_token():
    url = 'http://192.168.0.207:8081/xyxb/userCenter/login'
    head= {'content-type': 'application/x-www-form-urlencoded'}
    data = {
        'deviceCode': '481D3629d2d7978388365460dC5F91D2',
        'loginType': 1,
        'networkType': 0,
        'smsCode': '081588',
        'userName': '8826'
    }
    timeout = 0.5
    result = requests.post(url, headers=head, data=data, timeout=0.5)
    try:
        sul = result.json()['data']['token']
    except:
        sul = result.text
    return sul


def get_student_token():
    url = 'http://192.168.0.207:8081/xyxb/userCenter/login'
    head = {'content-type': 'application/x-www-form-urlencoded'}
    data = {
        'deviceCode': '481D3629d2d7978388365460dC5F91D2',
        'loginType': 1,
        'networkType': 0,
        'smsCode': '081588',
        'userName': '8826'
    }
    timeout = 0.5
    result = requests.post(url, headers=head, data=data, timeout=0.5)
    try:
        sul = result.json()['data']['token']
    except:
        sul = result.text
    return sul
def get_head(token):
    heard = {'content-type': 'application/x-www-form-urlencoded', 'cookie': 'AUTH-TOKEN=' + token}
    return heard

def get_send_post(url,head,data,timeout):
    try:
        result = requests.post(url, headers=head, data=data, timeout=timeout)
    except:
        print(Exception,'失败啦')
    else:
        item = url.split('/')[-1]
        code = result.status_code
        if int(code) == 200 and result.json()['data'] != None:
            resu = result.text
            print(item+'接口通过',resu)
        else:
            resu = result.text
            print(item+'接口失败',resu)

def get_course(url,head,data,timeout):
    try:
        result = requests.post(url, headers=head, data=data, timeout=timeout)
        code = result.status_code
    except:
        print(Exception)
        print('失败啦')
    else:
        item = url.split('/')[-1]
        if int(code) == 200 and result.json()['data'] != None:
            resu = result.text
            print(item+'接口通过',resu)
            courseCode = result.json()['data']['courseCode']
            return courseCode
        else:
            resu = result.text
            print(item+'接口失败',resu)