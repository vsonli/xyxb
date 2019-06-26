# -*- coding:utf-8 -*-
# @Time   :2019/6/26 16:43
# @File   :apicom.py
# @Author :Vsonli
import requests
from common.myConf import conf
import os
# path1 = os.path.abspath(os.path.dirname(os.getcwd()))+'\\'+'logs\\error.log'
def get_token():
    '''获得督导的token'''
    url = 'https://www.xuegean.com/xyxb/userCenter/login'
    head= {'content-type': 'application/x-www-form-urlencoded', 'Connection': 'close'}
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
        code = 0
        result = requests.post(url, headers=head, data=data, timeout=timeout)
        resu = result.text
        item = url.split('/')[-1]
        response_time = result.elapsed.total_seconds()
        if response_time >= 1:
            with open('timelog.log','a+') as f:
                f.write(item+'接口时间大于1秒，实际时间'+response_time+'\n')
    except Exception as e:
        print(e)
    else:
        print(item+'请求参数：'+str(data))
        code = result.status_code
        if int(code) == 200 and result.json()['data'] != None:
            print('返回结果为：' + resu)
            print(item+'接口访问通过','接口响应时间：'+str(response_time)+'秒')
            print('                                ')
        elif int(code) == 200 and result.json() ['data'] == None:
            print(item + '接口访问通过,data数据为空', '接口响应时间：' + str(response_time) + '秒', resu)
            print('                                ')
        else:
            resu = result.text
            print('返回结果为：' + resu)
            print(item+'接口访问失败','接口响应时间：'+str(response_time)+'秒')
            print('                                ')
        return int(code)


def get_course(url,head,data,timeout):
    '''获得课程code'''
    try:
        result = requests.post(url, headers=head, data=data, timeout=timeout)
        item = url.split('/')[-1]
        resu = result.text
        code = result.status_code
        response_time = result.elapsed.total_seconds()
        if response_time >= 1:
            with open('timelog.log','a+') as f:
                f.write(item+'接口时间大于1秒，实际时间'+response_time+'\n')
    except Exception as e:
        # print(item,'失败了')
        print(e)
    else:
        if int(code) == 200 and result.json()['data'] != None:
            print(item+'接口访问通过','接口响应时间：'+str(response_time)+'秒',resu)
            print('                                ')
            courseCode = result.json()['data']['courseCode']
            return courseCode
        elif int(code) == 200 and result.json() ['data'] == None:
            print(item + '接口访问通过,data数据为空', '接口响应时间：' + str(response_time) + '秒', resu)
            print('                                ')
        elif int(code) == 400:
            resu = result.text
            print(item+'接口访问失败','接口响应时间：'+str(response_time)+'秒',resu)
            print('                                ')
            return result.json()['data']['courseCode']
        else:
            return result.text