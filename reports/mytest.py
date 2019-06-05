# -*- coding:utf-8 -*-
# @Time   :2019/6/5 17:59
# @File   :mytest.py
# @Author :Vsonli
import requests
class tesss:
    def get_token(self,username,pwd):
        '''获得督导的token'''
        url = 'http://192.168.0.207:8081/xyxb/userCenter/login'
        head= {'content-type': 'application/x-www-form-urlencoded'}
        data = {
            'deviceCode': '481D3629d2d7978388365460dC5F91D2',
            'loginType': 1,
            'networkType': 0,
            'smsCode': pwd,
            'userName': username
        }
        result = requests.post(url, headers=head, data=data, timeout=60)
        try:
            sul = result.json()['data']['token']
        except:
            sul = result.text
        return sul

    def get_head(self,token):
        '''获得带token的Header'''
        heard = {'content-type': 'application/x-www-form-urlencoded', 'cookie': 'AUTH-TOKEN=' + token}
        return heard

    def get_send_post(self,url, head, data, timeout):
        '''发送post请求'''
        try:
            result = requests.post(url, headers=head, data=data, timeout=timeout)
            response_time = result.elapsed.total_seconds()
        except:
            print(Exception, '失败啦')
        else:
            item = url.split('/')[-1]
            code = result.status_code
            if int(code) == 200 and result.json()['data'] != None:
                resu = result.text
                print(item + '接口通过', '接口响应时间：' + str(response_time) + '秒', resu)
            else:
                resu = result.text
                print(item + '接口失败', '接口响应时间：' + str(response_time) + '秒', resu)

    def get_course(self,url, head, data, timeout):
        '''获得课程code'''
        try:
            result = requests.post(url, headers=head, data=data, timeout=timeout)
            code = result.status_code
            response_time = result.elapsed.total_seconds()
        except:
            print(Exception)
            print('失败啦')
        else:
            item = url.split('/')[-1]
            if int(code) == 200 and result.json()['data'] != None:
                resu = result.text
                print(item + '接口通过', '接口响应时间：' + str(response_time) + '秒', resu)
                courseCode = result.json()['data']['courseCode']
                return courseCode
            else:
                resu = result.text
                print(item + '接口失败', '接口响应时间：' + str(response_time) + '秒', resu)