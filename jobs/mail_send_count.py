# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def send_mail():
    sender = '729608526@qq.com'
    receiver = ['zhengxiang@cyou-inc.com']
    subject = '标注系统-每天打标注数量统计'
    smtpserver = 'smtp.qq.com'
    username = '729608526@qq.com'
    password = 'uzksheulwgnxbchf'
    msg = MIMEText('你好', 'plain', 'utf-8')

    msg['From'] = formataddr(["zhengxiang@cyou-inc.com", 'zhengxiang'])
    msg['Subject'] = subject
    msg['Cc'] = 'zheng729608526@sina.com'

    smtp = smtplib.SMTP(smtpserver)
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    send_mail()
