# -*- coding: utf-8 -*-
#  @ Date   : 2022/9/13 14:18
#  @ Author : RichardLau_Cx
#  @ Project: bakingOven-cn
#  @ File   : mail_sending.py
#  @ IDE    : PyCharm


import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

host_ = "localhost"  # 如果SMTP在本机上

# 第三方SMTP服务（QQ）
mail_host = "smtp.qq.com"
port_ = 465
account = "xxx@qq.com"  # 发送者邮箱
password = "xxx xxx"  # 授权码
receivers = ["xxx@qq.com"]  # 接收者邮箱List

# 设置邮件内容细节
message = MIMEMultipart()
message['From'] = Header("xxx", "utf-8")  # 发送者昵称
message['To'] = Header("指导", "utf-8")  # 接收者昵称
message['Subject'] = Header("来自用户的一份报告邮件", "utf-8")  # 邮件主题
message.attach(MIMEText('用户的记录数据报告文件。', 'plain', 'utf-8'))  # 邮件内容

# 构建邮件附件
attach_ = MIMEText(open('report.xlsx', 'rb').read(), 'base64', 'utf-8')
attach_["Content-Type"] = 'application/octet-stream'
attach_["Content-Disposition"] = 'attachment; filename="report.xlsx"'
message.attach(attach_)

try:
    smtp_ = smtplib.SMTP_SSL(mail_host, port=port_)
    smtp_.login(user=account, password=password)
    smtp_.sendmail(account, receivers, message.as_string())

except smtplib.SMTPException:
    pass
