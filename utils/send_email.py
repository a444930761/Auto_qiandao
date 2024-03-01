"""
本文件为发送QQ邮件的相关配置，使用QQ的smtp服务，端口25
如需自定义配置,仅需修改 to、send_mail、send_pass 三项即可
"""
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    try:
        server = smtplib.SMTP("smtp.qq.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("邮件发送成功")
    except Exception as e:
        print("邮件发送失败")
        print(e)
    finally:
        server.quit()
      
