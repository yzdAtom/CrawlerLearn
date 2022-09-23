"""
@Project ：CrawlerLearn 
@File    ：YouDaoJs.py
@IDE     ：PyCharm 
@Author  ：Atomyzd
@Useage    : 破解有道JS
"""
import requests
import time
import random
import hashlib

def main():
    url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42',
               'Referer': 'https://fanyi.youdao.com/',
               'Cookie': 'OUTFOX_SEARCH_USER_ID=1288174167@10.108.162.138; OUTFOX_SEARCH_USER_ID_NCOO=873497961.6983241; ___rl__test__cookies=1663918822165'
               }
    # 表单数据
    timestamp = time.time() * 1000
    salt = str(timestamp) + str(random.randint(0,10))
    temp = "fanyideskweb" + "world" + salt + "Ygy_4c=r#e#4EX^NUGUc5"
    sign = hashlib.md5(temp.encode("utf-8")).hexdigest()
    data = {
        'i': 'world',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'lts': timestamp,
        'bv': '580afdb7a7bc5fa2a6aa633ab0bbd3e4',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
        'Host': 'fanyi.youdao.com',
        'Origin': 'https://fanyi.youdao.com'
    }
    resp = requests.post(url, headers=headers, data=data)
    print(resp.text)


if __name__ == '__main__':
    main()