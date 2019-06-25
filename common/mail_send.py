# -*- coding:utf-8 -*-
# @Time   :2019/6/13 16:35
# @File   :mail_send.py
# @Author :Vsonli
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import datetime

# 写成了一个通用的函数接口，想直接用的话，把参数的注释去掉就好
def sen_email(msg_from='1633979409@qq.com', passwd='lkjdjuhqasyhehbi', msg_to=None, text_content='直播相关的接口测试报告', file_path=None):
    # msg_from = '1095133888@qq.com'  # 发送方邮箱
    # passwd = 'zjvoymwngfhigjss'  # 填入发送方邮箱的授权码（就是刚刚你拿到的那个授权码）
    # msg_to = '1095133998@qq.com'  # 收件人邮箱
    #设置时间为文件名
    now_time = datetime.datetime.now().strftime('%Y_%m_%d')
    msg = MIMEMultipart()
    subject = "直播相关接口测试报告"  # 主题
    # text_content = "你好啊，你猜这是谁发的邮件"
    text = MIMEText(text_content)
    msg.attach(text)
    # docFile = 'C:/Users/main.py'  如果需要添加附件，就给定路径
    if file_path:  # 最开始的函数参数我默认设置了None ，想添加附件，自行更改一下就好
        docFile = file_path
        docApart = MIMEApplication(open(docFile, 'rb').read())
        docApart.add_header('Content-Disposition', 'attachment', filename=now_time+'接口测试报告.html')
        msg.attach(docApart)
    msg['Subject'] = subject
    msg['From'] = msg_from
    # msg['To'] = msg_to
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    try:
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to.split(','), msg.as_string())
        print("发送成功")
    except smtplib.SMTPException as e:
        print("发送失败")
    finally:
        s.quit()