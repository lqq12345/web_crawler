#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",#伪装浏览器信息
}

def get_one_page(url):
    response = requests.get(url,headers=headers)
    if respinse.status_code == 200
        return response.text
    return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?>.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield{
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5].strip()+item[6].strip()
        }

def write_to_file(content):
    with open('try.txt','a',encoding = 'utf-8'):
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(offset):
    url = 'https://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset = i*10)
        time.sleep(1)

