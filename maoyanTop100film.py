#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests
import re
import json
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',#伪装浏览器信息

}

def get_one_page(url):
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        return response.text
    return None

def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?>.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S
    )
    items = re.findall(pattern,html)
    for item in items:
        yield{
            'index':item[0],
            'image':item[1],
            'title':item[2].strip(),#去除首尾空格
            'actor':item[3].strip()[3:] if len(item[3])>3 else '',#如果元祖的长度大于三才执行前面的与语句，否则返回空
            'time':item[4].strip()[5:],
            'score':item[5].strip()+item[6].strip()
        }
#print(items)

def write_to_file(content):
    with open('maoyanTop100Result.txt','a',encoding='utf-8') as f:
        # print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')#通过 json 库的 dumps() 方法实现字典的序列化，并指定 ensure_ascii 参数为 False，这样可以保证输出的结果是中文形式

def main(offset):
    url ='https://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset = i*10)
        time.sleep(1)#猫眼多了反爬虫，如果速度过快则会无响应，所以这里又增加了一个延时等待

