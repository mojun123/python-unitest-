import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 取最新的测试报告
def new_file(test_dir):
    lists = os.listdir(test_dir)
    lists.sort(key=lambda fn:os.path.getatime(test_dir+'\\'+fn))
    file_path = os.path.join(test_dir,lists[-1])
    return file_path

# 发送邮件，发送最新的测试报告

def send_email(nefile):
    f = open(nefile,'rb')
    mail_body = f.read()
    f.close()

    smtpserver = 'smtp.qq.com'
    user = '1696384748@qq.com'
    password = "gmyylcaoftrgdedd"
    sender = '1696384748@qq.com'
    receiver = '281754043@qq.com'
    subject = '自动化测试报告'
    msg = MIMEMultipart('mixed')
    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)

    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html)
    msg['From'] = '1696384748@qq.com'
    msg['To'] = receiver
    msg['Subject'] = Header(subject,'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


one = r'C:\Users\F993\Documents\Tencent Files\1696384748\FileRecv\genkifitness_pc_selenium_testing\genkifitness_pc_selenium_testing\result'
test = new_file(one)
send_email(test)
