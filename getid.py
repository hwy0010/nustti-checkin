import requests
import re

# stuid
stuid = ""

def getid():


    cookies = {
        'check_code_str': '6910',
        'creat_t': 'Mon Jan 10 2022 16:16:30 GMT+0800 (China Standard Time)',
        'wait_t': '297',
        'cp%%5Fsys': 'tPi=4rNjc0nzWWrIL0h3SjhvU5aYgkcUIl7aRJqTpD9d2022110161526&cTime%%5Fsend%%5Fmes=0',
        'ASPSESSIONIDAESDQDQR': 'COAOPBPBHDMFMICAHOFLEHEM',
    }

    headers = {
        'Host': 'zs.nustti.edu.cn',
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
        'sec-ch-ua-platform': '"Windows"',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://zs.nustti.edu.cn/yqfk/stu_login/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    params = (
        ('xh', stuid),
        ('phone', '1000000'),
        ('action', 'update_data'),
        ('tPi', '4rNjc0nzWWrIL0h3SjhvU5aYgkcUIl7aRJqTpD9d2022110161526'),
    )

    response = requests.get('http://zs.nustti.edu.cn/yqfk/stu_login/default_serv.asp', headers=headers, params=params, cookies=cookies, verify=False)

    # regexp for 5 nums
    reg = r'\d{5}'
    text = response.text
    id = re.findall(reg, text, re.S)[0]
    return id

if __name__ == '__main__':
    id = getid()
    if id!='00000':
        print ("ID: "+id)
    else:
        print ("学号错误")
        exit(0)
    
