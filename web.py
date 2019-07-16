#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",#伪装浏览器信息
    "Referer": "https://www.zhihu.com/"#添加当前要跳转的网页的域名，指定是从那个页面跳转过来的，也是反爬虫的技巧之一
}
url ="https://www.zhihu.com/explore"#把url单独以变量形式写出来，直接在get语句中使用引号括住网址，可能会出现errorcode61的错误

r = requests.get(url,headers = headers)

pattern = re.compile('explore-feed.*?requestion_link.*?>(.*?)</a>',re.S)
titles = re.findall(pattern,r.text)
#print(titles)


data = {'name':'amy','age':'12'}
r2 = requests.post("http://httpbin.org/post",data = data)
#print(r2.text)#返回结果中form等部分就是提交的data部分

r3 = requests.get("http://www.jianshu.com",headers=headers)
print(type(r3.status_code),r3.status_code)
print(type(r3.headers),r3.headers)
print(type(r3.cookies),r3.cookies)
print(type(r3.url),r3.url)
print(type(r3.history),r3.history)
