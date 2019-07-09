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


def send_email(path):
    #设置时间为文件名
    now_time = datetime.datetime.now().strftime('%Y_%m_%d')
    uname = conf.get('email','From')
    upwd = conf.get('email','mail_pass')
    msg_to = conf.get('email', 'To')
    host = conf.get('email', 'host')
    port = conf.get('email', 'port')
    msg = MIMEMultipart()
    subject = conf.get('email','subject')
    text_content = now_time+conf.get('email','text_content')
    text = MIMEText(text_content)
    msg.attach(text)
    if path:
        docFile = path
        docApart = MIMEApplication(open(docFile, 'rb').read())
        docApart.add_header('Content-Disposition', 'attachment', filename=now_time+'接口测试报告.html')
        msg.attach(docApart)
    msg['Subject'] = subject
    msg['From'] = conf.get('email','From')
    s = smtplib.SMTP()
    s.connect(host=host,port=port)
    try:
        s.login(user=uname, password=upwd)
        s.sendmail(from_addr=uname, to_addrs=msg_to.split(','), msg=msg.as_string())
        print("发送成功")
    except smtplib.SMTPException as e:
        print("发送失败")
        raise e
    finally:
        s.quit()