#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
# mail_user = "zgzjlbs@163.com"  # 用户名
mail_user = "122549797@qq.com"
# mail_pass = "lbs1991wy"  # 口令
mail_pass = "lwnqxrnuerncbgbc"  # 口令
# auth code lwnqxrnuerncbgbc
receivers = ['zgzjlbs@163.com']
sender  = '122549797@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python发送nice...', 'plain', 'utf-8')
message['From'] = Header("lbs wy")
message['To'] = Header("nice meet you")

subject = 'Python SMTP haha'
message['Subject'] = Header(subject, 'utf-8')
print(message)
with smtplib.SMTP() as smtpObj:
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")