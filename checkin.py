# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:06:37 2021

@author: hwy0010
"""
import requests
import time
from datetime import datetime

date = datetime.now().strftime('%Y-%m-%d|%H:%M:%S')
timestamp = int(round(time.time() * 1000))

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'DNT': '1',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Content-type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Origin': 'https://zs.nustti.edu.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://zs.nustti.edu.cn/yqfk/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}

params = (
    ('action', 'UpData'),
    ('NowTime', timestamp),
)

data = {
  'data_time': date,
  'data_id': '35959_' + str(timestamp),
  't0': '需修改 学号',
  't1': '36.0',
  't2': '0',
  't3': '0',
  't4': '0',
  't5_1_id': '需修改',
  't5_2_id': '需修改',
  't5_3_id': '需修改',
  't5_1': '需修改',
  't5_2': '需修改',
  't5_3': '需修改',
  't5_dz': '需修改',
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
  'info_ip_Address5': '需修改',
  'info_ip_Address6': '',
  'info_ip_Address1': '需修改',
  'info_ip_Address2': '需修改',
  'info_ip_Address3': '需修改',
  'location1': '\u5B9A\u4F4D\u5931\u8D25,\u7528\u6237\u62D2\u7EDD\u8BF7\u6C42\u5730\u7406\u5B9A\u4F4D',
  'location2': '\\u2c\\u2c\\u2c\\u2c\\u2c\\u2c\\u2c\\u2c'
}

response = requests.post('https://zs.nustti.edu.cn/yqfk/def_serv.asp', headers=headers, params=params, data=data)

print(response.text)




#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://zs.nustti.edu.cn/yqfk/def_serv.asp?action=UpData&NowTime=1634012257968', headers=headers, cookies=cookies, data=data)
