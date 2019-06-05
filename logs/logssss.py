# -*- coding:utf-8 -*-
# @Time   :2019/6/5 18:00
# @File   :logssss.py
# @Author :Vsonli
from reports.mytest import tesss

r = tesss()
teacher_tokens = r.get_token(username='8826',pwd='081588')
teacher_heads = r.get_head(teacher_tokens)
student_tokens = r.get_token(username='8830',pwd='081588')
student_head = r.get_head(student_tokens)
mydata={'groupCode':'196F0b9C1b282Da069DA0488b64834C0'}
timeout=60
url = 'http://192.168.0.207:8081/xyxb/specialColumnCenter/getStudyFinish'
r.get_send_post(url,teacher_heads,mydata,timeout)

url = 'http://192.168.0.207:8081/xyxb/specialColumnCenter/groupDetail'
r.get_send_post(url,teacher_heads,mydata,timeout)