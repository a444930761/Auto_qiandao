import os
import http.client

cookie = os.environ.get("JD_COOKIE")

conn = http.client.HTTPSConnection("api.m.jd.com")
payload = ''
headers = {
    'Cookie': cookie,
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Accept': '*/*',
    'Host': 'api.m.jd.com',
    'Connection': 'keep-alive'
}
conn.request("POST",
             "/client.action?functionId=signBeanAct&body=%257B%2522fp%2522%253A%2522-1%2522%252C%2522shshshfp%2522"
             "%253A%2522-1%2522%252C%2522shshshfpa%2522%253A%2522-1%2522%252C%2522referUrl%2522%253A%2522-1%2522%252C"
             "%2522userAgent%2522%253A%2522-1%2522%252C%2522jda%2522%253A%2522-1%2522%252C%2522rnVersion%2522%253A"
             "%25223.9%2522%257D&appid=ld&client=apple&clientVersion=10.0.4&networkType=wifi&osVersion=14.8.1&uuid"
             "=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&openudid=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&jsonp"
             "=jsonp_1645885800574_58482",
             payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
