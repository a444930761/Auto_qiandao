import json
import os
import http.client


def jd_sign(cookie):
    conn = http.client.HTTPSConnection("api.m.jd.com")
    url = (
        "/client.action?functionId=signBeanAct&body=%257B%2522fp%2522%253A%2522-1%2522%252C%2522shshshfp%2522%253A%2522"
        "-1%2522%252C%2522shshshfpa%2522%253A%2522-1%2522%252C%2522referUrl%2522%253A%2522-1%2522%252C%2522userAgent"
        "%2522%253A%2522-1%2522%252C%2522jda%2522%253A%2522-1%2522%252C%2522rnVersion%2522%253A%25223.9%2522%257D"
        "&appid=ld&client=apple&clientVersion=10.0.4&networkType=wifi&osVersion=14.8.1&uuid"
        "=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&openudid=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&jsonp"
        "=jsonp_1645885800574_58482")
    headers_001 = {
        'Cookie': cookie
    }
    conn.request("POST", url=url, headers=headers_001)
    res = conn.getresponse()
    response = res.read().decode("utf-8")
    json_str = response[response.index('(') + 1:response.rindex(')')]
    response_json = json.loads(json_str)
    print(response_json.get('data').get('dailyAward'))


cookie_001 = os.environ.get("JD_COOKIE_001")
cookie_002 = os.environ.get("JD_COOKIE_002")

jd_sign(cookie_001)
jd_sign(cookie_002)
print("---=执行完成=---")
