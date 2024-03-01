import json
import os
import datetime

import requests
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    sender_email = "3521850769@qq.com"
    sender_password = "kbmhzyfrifhrdbbc"
    receiver_email = "3521850769@qq.com"
    subject = "GitHub Actions 发生错误"
    body = f"您的 GitHub Actions 发生了错误，请尽快处理。{time.strftime("%Y-%m-%d")}"

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
def jd_signin(cookie):
    url = ("https://api.m.jd.com/client.action?functionId=signBeanAct&body=%7B%22fp%22%3A%22-1%22%2C%22shshshfp%22%3A"
           "%22-1%22%2C%22shshshfpa%22%3A%22-1%22%2C%22referUrl%22%3A%22-1%22%2C%22userAgent%22%3A%22-1%22%2C%22jda"
           "%22%3A%22-1%22%2C%22rnVersion%22%3A%223.9%22%7D&appid=ld&client=apple&clientVersion=10.0.4&networkType"
           "=wifi&osVersion=14.8.1&uuid=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&openudid"
           "=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&jsonp=jsonp_1645885800574_58482")
    headers = {"Cookie": cookie,
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHT"
                             "ML, like Gecko)Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"}
    r = requests.post(url=url, headers=headers)
    print(r.text)


def iku_signin(username, password):
    login_url = "https://ikuuu.pw/auth/login"
    data = {"email": f"{username}",
            "passwd": f"{password}",
            "code": ""}
    login_res = requests.post(login_url, data)
    print(login_res.json())
    cookie = login_res.cookies
    sing_headers = {"cookie": "; ".join([f"{name}={value}" for name, value in cookie.items()])}
    sign_url = "https://ikuuu.pw/user/checkin"
    sign_res = requests.post(sign_url, headers=sing_headers, data={})
    print(sign_res.json())
    return login_res.json()


cookie_001 = os.environ.get("JD_COOKIE_001")
iku_psd = os.environ.get("IKU_PSD")
jd_signin(cookie_001)

assert_data = iku_signin('a2401193521@qq.com', f'{iku_psd}')
if str(assert_data) == '{'ret': 1, 'msg': '登录成功'}':
    send_email()
else:
    pass
time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"--=执行完成=--，执行时间：{time}")
