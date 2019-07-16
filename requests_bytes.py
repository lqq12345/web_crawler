#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests

url ="https://github.com/favicon.ico"#把url单独以变量形式写出来，直接在get语句中使用引号括住网址，可能会出现errorcode61的错误

r = requests.get(url)

with open('favicon.ico','wb') as f:#使用open(文件名称，以什么形式打开)方法，'wb'表示以二进制形式打开
    f.write(r.content)#response对象的content属性，如果返回的是图片，音频，视频等文件，Requests会自动解码成bytes类型
