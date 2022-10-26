# -*- coding: utf-8 -*-
import requests
import time

from datetime import datetime

# parameters start
stuid = ""
id = ""
# parameters end

# generate timestamp
date = datetime.now().strftime('%Y-%m-%d|%H:%M:%S')
timestamp = int(round(time.time() * 1000))


headers = {
    'Host': 'zs.nustti.edu.cn',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'Content-type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://zs.nustti.edu.cn/Wechat_Apps_StuMis/yqfk_HealthReport/?k=2022-01-10|16:49:02|35959|922057265769243',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-us,en',
}

params = (
    ('action', 'UpData'),
    ('NowTime', timestamp),
)

data = {
  'data_time': date,
  'data_id': str(id) + '_' + str(timestamp),
  't0': str(stuid),
  't1': '36.0',
  't2': '0',
  't3': '0',
  't4': '0',
  't5_1_id': '320000',
  't5_2_id': '321200',
  't5_3_id': '321202',
  't5_1': '\\u6c5f\\u82cf\\u7701',
  't5_2': '\\u6cf0\\u5dde\\u5e02',
  't5_3': '\\u6d77\\u9675\\u533a',
  't5_dz': '\\u6885\\u5170\\u4e1c\\u8def\\u38\\u53f7',
  't10': '0',
  't6': '0',
  't7': '999',
  't7a': '999',
  't8': '9',
  't9': '9',
  'tt_cip': '',
  'tt_cid': '',
  'tt_cname': '',
  'info_ip_Address4': 'undefined',
  'info_ip_Address5': 'undefined',
  'info_ip_Address6': 'undefined',
  'info_ip_Address2':'\u6c5f\u82cf\u7701\u6cf0\u5dde\u5e02\u002c\u7535\u4fe1',
  'info_ip_Address3': '\u4E2D\u56FD|0|\u6C5F\u82CF\u7701|\u6cf0\u5dde\u5E02|\u7535\u4FE1',
  'location1': '',
  'location2': '\\u2c\\u2c\\u2c\\u2c\\u2c\\u2c\\u2c\\u2c'
}

response = requests.post('https://zs.nustti.edu.cn/Wechat_Apps_StuMis/yqfk_HealthReport/def_serv.asp', headers=headers, params=params, data=data, verify=False)
print(response.text)
