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
    def request(self,method,url,params=None,data=None,headers=None,cookies=None,json=None):
        method = method.lower() #转为小写
        print('传进来的参数：  ',data)
        if method == 'post':
            #判断post的参数是data还是json传参的
            if json:
                my_log.info('正在发送请求，url:{}，请求参数:{}'.format(url, json))
                return requests.post(url=url,headers=headers,json=json,cookies=cookies, timeout=60)
            else:
                my_log.info('正在发送请求，url:{}，请求参数:{}'.format(url, data))
                return requests.post(url=url, headers=headers, data=data, cookies=cookies, timeout=60)
        elif method == 'get':
            my_log.info('正在发送请求，url:{}，请求参数:{}'.format(url, params))
            return requests.get(url=url,params=params,headers=headers,cookies=cookies, timeout=60)

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
        return result.json()['data']['courseCode']



class HTTPRequestSession(object):
    '''使用cookies发送请求'''

    def __init__(self):
        #创建一个session对象
        self.session = requests.sessions.Session()

    def request(self,method,url,params=None,data=None,headers=None,cookies=None,json=None):
        method = method.lower() #转为小写
        if method == 'post':
            #判断post的参数是data还是json传参的
            if json:
                my_log.info('正在发送请求，url:{}，请求参数:{}'.format(url, json))
                return self.session.post(url=url,headers=headers,json=json,cookies=cookies, timeout=60)
            else:
                my_log.info('正在发送请求，url:{}，请求参数:{}'.format(url, data))
                return self.session.post(url=url, headers=headers, data=data, cookies=cookies, timeout=60)
        elif method == 'get':
            my_log.info('正在发送请求，url:{}，请求参数:{}'.format(url, params))
            return self.session.get(url=url,params=params,headers=headers,cookies=cookies, timeout=60)

    def close(self):
        self.session.close()


if __name__ == '__main__':
    r = HTTPRequest()
    head = r.get_head(url='http://192.168.0.207:8081/xyxb/userCenter/login',uname='8826',pwd='081588')
    print(head)
    result = r.request(method='post',url='http://192.168.0.207:8081/xyxb/comment/news/getCount',data={},headers=head)
    print(result)
    data = {'groupCode':'196F0b9C1b282Da069DA0488b64834C0','liveStatus':1}
    course_code = r.get_course_code(url='http://192.168.0.207:8081/xyxb/specialColumnCenter/setLiveStatus',head=head,data=data)
    print(course_code)
    # result = r.request(method='post',url='http://app.fookunion.com/api/business/login',data={'phone':'8613059285937','password':'5530013'})
    # print(result.text)

'''
Cookie: 
__cfduid=d445d889ce889eb526480ecb6796f18a41561446171; 
XSRF-TOKEN=eyJpdiI6IjdNcE95aFgxa1R5MjVUN0o3WFp1RWc9PSIsInZhbHVlIjoialZocmZoUFZJZ3h2bERtSDVQZVJFRWhBektRMzhXZHlNcVZoWVMzcWg4b3BlUGc0K0FkcEU5cDk0VWZzU0VQUCIsIm1hYyI6IjIwZWFmOGY0NGE1MjRmZjAxZWI2MDVlMjhiMGJlOTI0MjkxNjY1N2RjODAwN2JlNTQyYzhjMDIzZTJlNDZkOWQifQ%3D%3D; 
laravel_session=eyJpdiI6Ikc5VXZqeVZHN1dFQnpSRUN2R3l6eEE9PSIsInZhbHVlIjoiWXE5azRyWFJ0ZFJNWmxuU3FkaFl6OXhqS0owbDZEZ0pEMmxQOVpnemRtcVcwNVpaQVJCdnZCZW9ORnNKZjRHYiIsIm1hYyI6IjEwMWE1YmRjOGE1OTYzYmFjNjliN2QwZjdiNmFmYWUyZDUwZTc0NzhjMzNjOTRjNDBlMDAwNTBmYWI2OGVkNGEifQ%3D%3D
'''