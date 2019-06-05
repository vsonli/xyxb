# -*- coding:utf-8 -*-
# @Time   :2019/6/5 12:16
# @File   :xyxbtest.py
# @Author :Vsonli
from common.apicom import *
import time

teacher_tokens = get_token()
teacher_heads = get_head(teacher_tokens)
student_tokens = get_student_token()
student_head = get_head(student_tokens)
mydata={'groupCode':'196F0b9C1b282Da069DA0488b64834C0'}
timeout=60

'''点击专栏'''
url = 'http://192.168.0.207:8081/xyxb/specialColumnCenter/getStudyFinish'
get_send_post(url,teacher_heads,mydata,timeout)

url = 'http://192.168.0.207:8081/xyxb/specialColumnCenter/groupDetail'
get_send_post(url,teacher_heads,mydata,timeout)


'''开启直播'''
couse_data={'groupCode':'196F0b9C1b282Da069DA0488b64834C0','liveStatus':1}
url = 'http://192.168.0.207:8081/xyxb/specialColumnCenter/setLiveStatus'
course = get_course(url,teacher_heads,couse_data,timeout)
print('course值:'+str(course))

url = 'http://192.168.0.207:8081/xyxb/specialColumnCenter/groupDetail'
get_send_post(url,teacher_heads,mydata,timeout)

url = 'http://192.168.0.207:8081/xyxb/groupCenter/updateLastGroupSpeak'
get_send_post(url,teacher_heads,mydata,timeout)

couse_code = {'courseCode':course}
print(couse_code)
url = 'http://192.168.0.207:8081/xyxb/specialColumnCenter/listGroupKey'
get_send_post(url,teacher_heads,couse_code,timeout)
time.sleep(3)
url = 'http://192.168.0.207:8081/xyxb/specialColumnCenter/listQuestion'
get_send_post(url,teacher_heads,mydata,timeout)


'''开启考勤'''
url = 'http://192.168.0.207:8081/xyxb/specialColumnCenter/startSupervisor'
get_send_post(url,teacher_heads,mydata,timeout)

url = 'http://192.168.0.207:8081/xyxb/groupCenter/updateLastGroupSpeak'
get_send_post(url,teacher_heads,mydata,timeout)

url = 'http://192.168.0.207:8081/xyxb/specialColumnCenter/userReckon'
start_data={'duration':180,'groupCode':'196F0b9C1b282Da069DA0488b64834C0','courseCode':course}
time.sleep(3)
urls = 'http://192.168.0.207:8081/xyxb/specialColumnCenter/listGroupKey'
get_send_post(urls,teacher_heads,couse_code,timeout)
time.sleep(3)
'''结束直播'''
urls = 'http://192.168.0.207:8081/xyxb/specialColumnCenter/setLiveStatus'
end_data={'groupCode':'196F0b9C1b282Da069DA0488b64834C0','liveStatus':0}
get_send_post(urls,teacher_heads,end_data,timeout)

urls = 'http://192.168.0.207:8081/xyxb/specialColumnCenter/userReckon'
end_data={'groupCode':'196F0b9C1b282Da069DA0488b64834C0','duration':471,'courseCode':couse_data}
get_send_post(urls,teacher_heads,end_data,timeout)
time.sleep(3)
urls = 'http://192.168.0.207:8081/xyxb/groupCenter/updateLastGroupSpeak'
get_send_post(urls,teacher_heads,mydata,timeout)

urls = 'http://192.168.0.207:8081/xyxb/groupCenter/updateLastGroupSpeak'
get_send_post(urls,teacher_heads,mydata,timeout)