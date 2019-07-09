# -*- coding:utf-8 -*-
# @Time   :2019/6/13 16:35
# @File   :mail_send.py
# @Author :Vsonli
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from common.myConf import conf
import datetime


def send_mail(htmlname):
    now_time = datetime.datetime.now().strftime('%Y_%m_%d')
    #第一步：创建一个SMTP对象
    s = smtplib.SMTP()
    #第二步：连接到SMTP服务器
    host = conf.get('email','host')
    s.connect(host, port=conf.get('email','port'))      #连接到服务器，使用地址和端口号
    #第三步：登陆SMTP服务器
    # mail_user = '1633979409@qq.com'   #用户名
    mail_user = conf.get('email','From')
    # mail_pass = 'uobsqzmhqviaefdb'          #邮箱设置的smtp密钥
    mail_pass = conf.get('email','mail_pass')
    s.login(user=mail_user, password=mail_pass)

    #构建邮件内容
    content = '本次通过率为10'
    #主题
    Subject = now_time+'测试报告'
    #发件人
    # From = '1633979409@163.com'
    From = conf.get('email','From')
    #收件人
    # To = '1632411548.@qq.com'
    To = conf.get('email','To')
    #创建可发附件的邮件
    message = MIMEText(content,_charset='utf-8')
    #构造附件
    part = MIMEApplication(open(htmlname,'rb').read(), _subtype=None)
    part.add_header('content-disposition', 'attachment', filename='测试报告.html')
    #封装一个邮件
    msg = MIMEMultipart()
    #加入附件和文本内容
    msg.attach(message)
    msg.attach(part)


    #添加邮件主题
    message['Subject'] = Header(Subject, 'utf-8')
    #添加发送人
    message['From'] = From
    #添加收件人
    message['To'] = To

    #第五步：发生邮箱
    s.sendmail(from_addr=mail_user,to_addrs=To,msg=message.as_string())


# # 写成了一个通用的函数接口，想直接用的话，把参数的注释去掉就好
# def sen_email(msg_from='1633979409@qq.com', passwd='lkjdjuhqasyhehbi', msg_to=None, text_content='直播相关的接口测试报告', file_path=None):
#     # msg_from = '1095133888@qq.com'  # 发送方邮箱
#     # passwd = 'zjvoymwngfhigjss'  # 填入发送方邮箱的授权码（就是刚刚你拿到的那个授权码）
#     # msg_to = '1095133998@qq.com'  # 收件人邮箱
#     #设置时间为文件名
#     now_time = datetime.datetime.now().strftime('%Y_%m_%d')
#     msg = MIMEMultipart()
#     subject = "直播相关接口测试报告"  # 主题
#     # text_content = "你好啊，你猜这是谁发的邮件"
#     text = MIMEText(text_content)
#     msg.attach(text)
#     # docFile = 'C:/Users/main.py'  如果需要添加附件，就给定路径
#     if file_path:  # 最开始的函数参数我默认设置了None ，想添加附件，自行更改一下就好
#         docFile = file_path
#         docApart = MIMEApplication(open(docFile, 'rb').read())
#         docApart.add_header('Content-Disposition', 'attachment', filename=now_time+'接口测试报告.html')
#         msg.attach(docApart)
#     msg['Subject'] = subject
#     msg['From'] = msg_from
#     # msg['To'] = msg_to
#     s = smtplib.SMTP_SSL("smtp.qq.com", 465)
#     try:
#         s.login(msg_from, passwd)
#         s.sendmail(msg_from, msg_to.split(','), msg.as_string())
#         print("发送成功")
#     except smtplib.SMTPException as e:
#         print("发送失败")
#     finally:
#         s.quit()