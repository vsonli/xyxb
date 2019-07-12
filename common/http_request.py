# -*- coding:utf-8 -*-
# @Time   :2019/6/13 11:34
# @File   :http_request.py
# @Author :Vsonli
'''
request的封装类
1.根据用例中的请求方法，来决定发起请求的模式
2.输出日志
'''
import requests
from common.logger import *

class HTTPRequest(object):
    '''不记录cookies信息'''
    def request(self,method,url,params=None,data=None,headers=None,cookies=None,json=None,verify=False):
        method = method.lower() #转为小写
        print('传进来的参数：  ',data)
        # print('传进来的head：  ',headers)
        if method == 'post':
            #判断post的参数是data还是json传参的
            if json:
                my_log.info('正在发送请求，url:{}，请求参数:{}'.format(url, json))
                return requests.post(url=url,headers=headers,json=json,cookies=cookies, verify=False,timeout=60)
            else:
                my_log.info('正在发送请求，url:{}，请求参数:{}'.format(url, data))
                return requests.post(url=url, headers=headers, data=data, cookies=cookies, verify=False, timeout=60)
        elif method == 'get':
            my_log.info('正在发送请求，url:{}，请求参数:{}'.format(url, params))
            return requests.get(url=url,params=params,headers=headers,cookies=cookies, verify=False, timeout=60)

    def get_head(self,url,uname,pwd):
        '''
        返回用户token
        :param url:
        :param uname:
        :param pwd:
        :return:
        '''
        head = {'content-type': 'application/x-www-form-urlencoded', 'Connection': 'close'}
        data = {
            'deviceCode':'481D3629d2d7978388365460dC5F91D2',
            'loginType':1,
            'networkType':0,
            'smsCode':pwd,
            'userName':uname
        }
        result = self.request(method='post', url=url, headers=head, data=data)
        tokens = result.json()['data']['token']
        token = 'AUTH-TOKEN=' + tokens
        token_head = {'content-type': 'application/x-www-form-urlencoded', 'cookie': token}
        return token_head

    def get_course_code(self,url,head,data):
        '''
        返回课程code
        :param url:
        :param head:
        :param data:
        :return:
        '''
        result = self.request(method='post',url=url,data=data,headers=head)
        # try:
        #     courseCode = result.json()['data']['courseCode']
        #     print('couseCode为'+str(courseCode))
        #     return result
        # except Exception as e:
        #     print('直播已开启')
        return result.json()['code'],result.json()['data']['courseCode'],result.text



class HTTPRequestSession(object):
    '''使用cookies发送请求'''

    def __init__(self):
        #创建一个session对象
        self.session = requests.sessions.Session()

    def request(self,method,url,params=None,data=None,headers=None,cookies=None,json=None ,verify=False,):
        method = method.lower() #转为小写
        if method == 'post':
            #判断post的参数是data还是json传参的
            if json:
                my_log.info('正在发送请求，url:{}，请求json参数:{}'.format(url, json))
                return self.session.post(url=url,headers=headers,json=json,cookies=cookies,  verify=False,timeout=60)
            else:
                my_log.info('正在发送请求，url:{}，请求data参数:{}'.format(url, data))
                return self.session.post(url=url, headers=headers, data=data, cookies=cookies,  verify=False,timeout=60)
        elif method == 'get':
            my_log.info('正在发送请求，url:{}，请求params参数:{}'.format(url, params))
            return self.session.get(url=url,params=params,headers=headers,cookies=cookies,  verify=False,timeout=60)

    def close(self):
        self.session.close()


if __name__ == '__main__':
    r = HTTPRequest()
    user = ['13011111110','13011111111','13011111112','13011111113','13011111114','13011111115','13011111116','13011111117','13011111118','13011111119']
    head = r.get_head(url='http://192.168.0.105:8081/xyxb/userCenter/login',uname='8826',pwd='081588')
    url = 'https://www.xuegean.com/xyxb/specialColumnCenter/startSupervisor'
    # course_code = r.get_course_code(url='https://www.xuegean.com/xyxb/specialColumnCenter/setLiveStatus', head=head,
    #                                           data={'groupCode': '196F0b9C1b282Da069DA0488b64834C0', 'liveStatus': 1})

    response = r.request(method='post',url=url,headers=head,data={'groupCode':'196F0b9C1b282Da069DA0488b64834C0'})
    # print(response.text)
    for i in range(0,10):
        data = {
            'groupCode': '0987cb60ff3e31B149EDacB83AE651E2',
            'phoneNums': user[i]
        }
        # data = {'userName':,'smsCode':''}

        response = r.request(method='post',url='http://192.168.0.105:8081/xyxb/groupCenter/sysAddMember',data=data,headers=head)
        print(response.text)
        print(user[i])
    # for i in range(0,10):
    #     head = r.get_head(url='http://192.168.0.105:8081/xyxb/userCenter/login', uname=user[i], pwd='081588')
    #     print(head)

    '''http://192.168.0.105:8081/xyxb/groupCenter/sysAddMember
    groupCode   0987cb60ff3e31B149EDacB83AE651E2
    phoneNums   13059285936
    '''












    # result = r.request(method='post',url='http://www.xuegean.com/xyxb/groupCenter/groupDetail',data={'groupCode':'196F0b9C1b282Da069DA0488b64834C0'},headers=head)
    # print(result)
    # data = {'groupCode':'196F0b9C1b282Da069DA0488b64834C0','liveStatus':0}
    # course_code = r.get_course_code(url='http://www.xuegean.com/xyxb/specialColumnCenter/setLiveStatus',head=head,data=data)
    # print(course_code)
    # print(result.text)