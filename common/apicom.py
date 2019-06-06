# -*- coding:utf-8 -*-
# @Time   :2019/6/4 18:44
# @File   :apicom.py
# @Author :Vsonli
import requests
from common.myConf import conf
import os
path1 = os.path.abspath(os.path.dirname(os.getcwd()))+'\\'+'logs\\error.log'
def get_token():
    '''获得督导的token'''
    url = 'https://www.xuegean.com/xyxb/userCenter/login'
    head= {'content-type': 'application/x-www-form-urlencoded'}
    data = {
        'deviceCode': '481D3629d2d7978388365460dC5F91D2',
        'loginType': 1,
        'networkType': 0,
        'smsCode': '081588',
        'userName': '8826'
    }
    result = requests.post(url, headers=head, data=data, timeout=60)
    try:
        sul = result.json()['data']['token']
    except:
        sul = result.text
        try:
            with open(path1, 'w') as f:
                f.write('获取token接口发生了错误'+'            返回结果：'+sul)
        except:
            with open(path1, 'w') as f:
                f.write(Exception)
        print(Exception,'失败啦')
    return sul


def get_student_token():
    '''获得学员的token'''
    url = 'https://www.xuegean.com/xyxb/userCenter/login'
    head = {'content-type': 'application/x-www-form-urlencoded'}
    data = {
        'deviceCode': '481D3629d2d7978388365460dC5F91D2',
        'loginType': 1,
        'networkType': 0,
        'smsCode': '081588',
        'userName': '8830'
    }
    result = requests.post(url, headers=head, data=data, timeout=60)
    try:
        sul = result.json()['data']['token']
    except:
        sul = result.text
    return sul

def get_head(token):
    '''获得带token的Header'''
    heard = {'content-type': 'application/x-www-form-urlencoded', 'cookie': 'AUTH-TOKEN=' + token}
    return heard

def get_send_post(url,head,data,timeout):
    '''发送post请求'''
    try:
        result = requests.post(url, headers=head, data=data, timeout=timeout)
        resu = result.text
        item = url.split('/')[-1]
        response_time = result.elapsed.total_seconds()
    except:
        try:
            with open(path1, 'w') as f:
                f.write(item + '接口发生了错误'+'            返回结果：'+resu)
        except:
            with open(path1, 'w') as f:
                f.write(Exception)
        print(Exception,'失败啦')
    else:
        print(item+'请求参数：'+str(data))
        code = result.status_code
        if int(code) == 200 and result.json()['data'] != None:
            print(item+'接口访问通过','接口响应时间：'+str(response_time)+'秒')
            print('返回结果为：' + resu)
            print('                                ')
        else:
            resu = result.text
            print(item+'接口访问失败','接口响应时间：'+str(response_time)+'秒')
            print('返回结果为：'+resu)
            print('                                ')


def get_course(url,head,data,timeout):
    '''获得课程code'''
    try:
        result = requests.post(url, headers=head, data=data, timeout=timeout)
        item = url.split('/')[-1]
        resu = result.text
        code = result.status_code
        response_time = result.elapsed.total_seconds()
    except:
        try:
            with open(path1, 'w') as f:
                f.write(item + '接口发生了错误'+'            返回结果：'+resu)
        except:
            with open(path1, 'w') as f:
                f.write(Exception)
        print(Exception,'失败啦')
    else:
        if int(code) == 200 and result.json()['data'] != None:
            print(item+'接口访问通过','接口响应时间：'+str(response_time)+'秒',resu)
            print('                                ')
            courseCode = result.json()['data']['courseCode']
            return courseCode
        else:
            resu = result.text
            print(item+'接口访问失败','接口响应时间：'+str(response_time)+'秒',resu)
            print('                                ')