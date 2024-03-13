import json
import os
from datetime import datetime
from re import T
import requests
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
JD_cookie = os.environ.get("JD_COOKIE_001")
iku_psd = os.environ.get("IKU_PSD")
email_pwd = os.environ.get("EMAIL_PASSWORD")

def send_email(subject, body):
    sender_email = "3521850769@qq.com"
    sender_password = email_pwd
    receiver_email = "3521850769@qq.com"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    server = smtplib.SMTP("smtp.qq.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("邮件发送成功")


def jd_signin(cookie):
    url = (
        "https://api.m.jd.com/client.action?functionId=signBeanAct&body=%7B%22fp%22%3A%22-1%22%2C%22shshshfp%22%3A%2"
        "2-1%22%2C%22shshshfpa%22%3A%22-1%22%2C%22referUrl%22%3A%22-1%22%2C%22userAgent%22%3A%22-1%22%2C%22jda%22%3A"
        "%22-1%22%2C%22rnVersion%22%3A%223.9%22%7D&appid=ld&client=apple&clientVersion=10.0.4&networkType=wifi&osVer"
        "sion=14.8.1&uuid=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&openudid=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6"
        "&jsonp=jsonp_1645885800574_58482"
    )
    headers = {
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHT"
                      "ML, like Gecko)Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    }
    r = requests.post(url=url, headers=headers)
    json_data = r.text.replace("jsonp_1645885800574_58482(", "").rstrip(");")
    res_title = json.loads(json_data)
    res_title = res_title.get('data').get('dailyAward').get('title')
    return res_title


def iku_signin(username, password):
    login_url = "https://ikuuu.pw/auth/login"
    data = {"email": f"{username}", "passwd": f"{password}", "code": ""}
    login_res = requests.post(login_url, data)
    print(login_res.json())
    cookie = login_res.cookies
    sing_headers = {
        "cookie": "; ".join([f"{name}={value}" for name, value in cookie.items()])
    }
    sign_url = "https://ikuuu.pw/user/checkin"
    sign_res = requests.post(sign_url, headers=sing_headers, data={})
    print(sign_res.json())
    return login_res.json()


title = jd_signin(JD_cookie)
if str(title) not in ("签到成功，", "今天已签到，"):
    subject = "GitHub Actions 运行异常"
    body = f"您的 GitHub Actions 发生了错误，请尽快处理。错误时间：{time.strftime("%Y-%m-%d")}"
    send_email(subject, body)
    print("发送告警邮件")
else:
    print(f"京东签到成功，签到时间:{time_now}")

assert_data = iku_signin('a2401193521@qq.com', f'{iku_psd}')

if str(assert_data) != "{'ret': 1, 'msg': '登录成功'}":
    subject = "GitHub Actions 运行异常"
    body = f"您的 GitHub Actions 发生了错误，请尽快处理。错误时间：{time.strftime("%Y-%m-%d")}"
    send_email(subject, body)
    print("发送告警邮件")
else:
    pass

print(f"--=执行完成=--，执行时间：{time_now}")
