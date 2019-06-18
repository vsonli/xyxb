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
def xyxb_live():
    '''点击专栏'''
    url = 'https://www.xuegean.com/xyxb/specialColumnCenter/getStudyFinish'   #1
    get_send_post(url,teacher_heads,mydata,timeout)

    url = 'https://www.xuegean.com/xyxb/specialColumnCenter/groupDetail'    #2
    code = get_send_post(url,teacher_heads,mydata,timeout)
    print(code)

    '''开启直播'''
    couse_data={'groupCode':'196F0b9C1b282Da069DA0488b64834C0','liveStatus':1}
    url = 'https://www.xuegean.com/xyxb/specialColumnCenter/setLiveStatus'      #3
    course = get_course(url,teacher_heads,couse_data,timeout)
    print('course值:'+str(course))

    url = 'https://www.xuegean.com/xyxb/specialColumnCenter/groupDetail'        #4
    get_send_post(url,teacher_heads,mydata,timeout)

    url = 'https://www.xuegean.com/xyxb/groupCenter/updateLastGroupSpeak'   #5
    get_send_post(url,teacher_heads,mydata,timeout)

    couse_code = {'courseCode':course}
    url = 'https://www.xuegean.com/xyxb/specialColumnCenter/listGroupKey'   #6
    get_send_post(url,teacher_heads,couse_code,timeout)

    url = 'https://www.xuegean.com/xyxb/specialColumnCenter/listQuestion'   #7
    get_send_post(url,teacher_heads,mydata,timeout)


    '''开启考勤'''
    url = 'https://www.xuegean.com/xyxb/specialColumnCenter/startSupervisor'    #8
    get_send_post(url,teacher_heads,mydata,timeout)

    url = 'https://www.xuegean.com/xyxb/groupCenter/updateLastGroupSpeak'   #9
    get_send_post(url,teacher_heads,mydata,timeout)

    url = 'https://www.xuegean.com/xyxb/specialColumnCenter/userReckon'     #10
    start_data={'duration':180,'groupCode':'196F0b9C1b282Da069DA0488b64834C0','courseCode':course}
    get_send_post(url, teacher_heads, start_data, timeout)

    urls = 'https://www.xuegean.com/xyxb/specialColumnCenter/listGroupKey'  #11
    get_send_post(urls,teacher_heads,couse_code,timeout)



    print('---------------------------以下为学员和督导之间的上下麦操作---------------------------------')
    '''学员端操作'''
    surl = 'https://www.xuegean.com/xyxb/specialColumnCenter/getStudyFinish'    #12
    get_send_post(surl,student_head,mydata,timeout)

    surl = 'https://www.xuegean.com/xyxb/specialColumnCenter/groupDetail'   #13
    get_send_post(surl,student_head,mydata,timeout)

    sdata={'useType':2,'groupCode':'196F0b9C1b282Da069DA0488b64834C0'}  #14
    surl = 'https://www.xuegean.com/xyxb/groupLiveTicket/isUseTicket'
    get_send_post(surl,student_head,sdata,timeout)

    surl = 'https://www.xuegean.com/xyxb/specialColumnCenter/listQuestion'  #15
    get_send_post(surl,student_head,mydata,timeout)

    surl = 'https://www.xuegean.com/xyxb/specialColumnCenter/listQuestion'  #16
    get_send_post(surl,student_head,mydata,timeout)

    surl = 'https://www.xuegean.com/xyxb/specialColumnCenter/listGroupKey'  #17
    get_send_post(surl,student_head,couse_code,timeout)

    for i in range(6):
        print('开始了核心小组的上下麦')
        '''加入核心小组'''
        groupKey = {'sort':i+1,'courseCode':course}                 #18
        surl = 'https://www.xuegean.com/xyxb/specialColumnCenter/addGroupKey'
        get_send_post(surl,student_head,groupKey,timeout)

        surl = 'https://www.xuegean.com/xyxb/groupCenter/updateLastGroupSpeak'  #19
        get_send_post(surl,student_head,mydata,timeout)


        '''申请发言'''
        editGroupKey = {'status':1,'courseCode':course}
        surl = 'https://www.xuegean.com/xyxb/specialColumnCenter/editGroupKey'  #20
        get_send_post(surl,student_head,editGroupKey,timeout)

        surl = 'https://www.xuegean.com/xyxb/groupCenter/updateLastGroupSpeak'  #21
        get_send_post(surl,student_head,mydata,timeout)



        '''督导操作开始
            同意核心小组发言'''
        editGroupKey = {'courseCode':course,'status':2,'userCode':'48D393a5aBc510B0a9601e3C1A0c9C9A'}       #22
        surl = 'https://www.xuegean.com/xyxb/specialColumnCenter/editGroupKey'
        get_send_post(surl,teacher_heads,editGroupKey,timeout)

        urls = 'https://www.xuegean.com/xyxb/groupCenter/updateLastGroupSpeak'      #23
        get_send_post(urls,teacher_heads,mydata,timeout)
        print('核心小组进行发言十秒')
        time.sleep(10)

        '''终止核心小组发言'''
        editGroupKey = {'courseCode':course,'status':0,'userCode':'48D393a5aBc510B0a9601e3C1A0c9C9A'}       #24
        urls = 'https://www.xuegean.com/xyxb/specialColumnCenter/editGroupKey'
        get_send_post(urls,teacher_heads,editGroupKey,timeout)

        urls = 'https://www.xuegean.com/xyxb/groupCenter/updateLastGroupSpeak'      #25
        get_send_post(urls,teacher_heads,mydata,timeout)

        '''退出核心小组'''
        quitGroupKey = {'courseCode':course,'sort':1}
        urls = 'https://xuegean.com/xyxb/specialColumnCenter/quitGroupKey'      #26
        get_send_post(urls, student_head, quitGroupKey, timeout)

        editGroupKey = {'courseCode': course, 'status': 0}
        urls = 'https://xuegean.com/xyxb/specialColumnCenter/editGroupKey'      #27
        get_send_post(urls, student_head, editGroupKey, timeout)

        urls = 'https://xuegean.com/xyxb/groupCenter/updateLastGroupSpeak'      #28
        get_send_post(urls, student_head, mydata, timeout)

        urls = 'https://xuegean.com/xyxb/groupCenter/updateLastGroupSpeak'      #29
        get_send_post(urls, student_head, mydata, timeout)
        print('结束了第'+str(i+1)+'次的核心小组的上下麦，准备开始下一轮')
        time.sleep(5)
    print('---------------------------学员和督导之间的上下麦操作结束---------------------------------')

    print('正在持续开始直播，等待结束直播。。。。。。')
    time.sleep(10)
    '''结束直播'''
    urls = 'https://www.xuegean.com/xyxb/specialColumnCenter/setLiveStatus'     #30
    end_data={'groupCode':'196F0b9C1b282Da069DA0488b64834C0','liveStatus':0}
    get_send_post(urls,teacher_heads,end_data,timeout)

    urls = 'https://www.xuegean.com/xyxb/specialColumnCenter/userReckon'        #31
    end_data={'groupCode':'196F0b9C1b282Da069DA0488b64834C0','duration':471,'courseCode':course}
    get_send_post(urls,teacher_heads,end_data,timeout)

    urls = 'https://www.xuegean.com/xyxb/groupCenter/updateLastGroupSpeak'      #32
    get_send_post(urls,teacher_heads,mydata,timeout)

    urls = 'https://www.xuegean.com/xyxb/groupCenter/updateLastGroupSpeak'      #33
    get_send_post(urls,teacher_heads,mydata,timeout)

for i  in range(20):
    print('这是第' + str(i + 1) + '次')
    xyxb_live()
    if i == 20:
        print('20次测试已结束')
    else:
        print('第' + str(i + 1) + '次执行结束，准备执行下一轮')
        time.sleep(10)
# url = 'https://www.xuegean.com/xyxb/specialColumnCenter/groupDetail'    #2
# code = get_send_post(url,teacher_heads,mydata,timeout)
# print(code)
#
# '''开启直播'''
# couse_data={'groupCode':'196F0b9C1b282Da069DA0488b64834C0','liveStatus':1}
# url = 'https://www.xuegean.com/xyxb/specialColumnCenter/setLiveStatus'      #3
# course = get_course(url,teacher_heads,couse_data,timeout)
xyxb_live()
# print('course值:'+str(course))