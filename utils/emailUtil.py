# -*- coding:utf-8 -*-
import datetime
import os
import smtplib
from ast import literal_eval
from email.mime.text import MIMEText

from utils import getPath as gp
from utils import operationINI as oi


def send_email(content):
    # 配置文件
    email_config_path = gp.filePath("config","email.ini")
    host = oi.getData(filePath=email_config_path,section="email",option="host")  # 邮箱地址
    port = oi.getData(filePath=email_config_path,section="email",option="port")
    sender = oi.getData(filePath=email_config_path,section="email",option="sender")  # 发送账号
    senderName = oi.getData(filePath=email_config_path,section="email",option="senderName")
    pwd = oi.getData(filePath=email_config_path,section="email",option="pswd")  # 邮箱秘钥
    receiver = oi.getData(filePath=email_config_path,section="email",option="received")  # 接收人
    receivers = literal_eval(receiver)
    title = oi.getData(filePath= email_config_path, section= "email", option= "title")

    # file_name = "{}自动巡检报告.txt".format(datetime.datetime.today().strftime("%Y_%m_%d"))
    # 装载邮件内容与附件容器
    # message = MIMEMultipart()
    # message['Subject'] = '{}{}'.format(datetime.datetime.today().strftime("%Y_%m_%d"), ''.join(title))
    # message['To'] = ','.join(receiver)
    # message['From'] = sender

    #装载附件的容器
    # with open(fujian_file, "rb") as f:
    #     email_body = f.read()
    # fujian_msg = MIMEText(email_body, 'base64', 'utf-8')
    # fujian_msg['Content-Type'] = 'application/octer-stream'
    # 附件名称为中文时的写法
    # fujian_msg.add_header("Content-Disposition", "attachment", filename=("gbk", "", file_name))
    # fujian_msg['Content-Disposition'] = 'attachment;filename="{}"'.format(file_name)

    # 装载邮件正文的容器
    content_msg = MIMEText(content,'html','utf-8')
    content_msg['Subject'] = '{}{}'.format(datetime.datetime.today().strftime("%Y_%m_%d"),''.join(title))
    content_msg['To'] = ','.join(receivers)
    content_msg['From'] = "{0}<{1}>".format(senderName, sender)


    #添加容器
    # message.attach(fujian_msg)
    # message.attach(content_msg)


    try:
        smtp = smtplib.SMTP_SSL(host=host, port=port)
        smtp.login(sender, pwd)
        smtp.sendmail(sender, receivers, content_msg.as_string())
        smtp.close()
    except Exception as e:
        print(e)

# 获取最新文件
def new_report():
    log_path = gp.dirPath('log')
    lists = os.listdir(log_path)  # 列出目录下的所有文件和文件夹保存到lists
    lists.sort(key = lambda fn: os.path.getmtime(log_path + "/" + fn))  # 按时间排序
    file_new = os.path.join(log_path, lists[-1])  # 获取最新的文件保存到file_new
    return file_new

if __name__ == "__main__":
    send_email("测试邮件-报告地址为：http://localhost:63342/InterTest/report/report/index.html")