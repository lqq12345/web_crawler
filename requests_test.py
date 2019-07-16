#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests
r=requests.get('https://www.baidu.com')#返回得到一个response对象
print(type(r))
print(r.status_code)
print(type(r.text))#response body的类型是str
print(r.text)#返回resoubse body
print(r.cookies)#cookies的类型是RequestsCookieJar



r1=requests.get('http://httpbin.org/get')
print(type(r1.text))#网页返回的类型实际上是str类型
print(type(r1.json()))#但是是Json格式
print(r1.json())#把返回结果解析得到一个字典格式，但若返回结果不是Json格式没便会出现解析错误，抛出 json.decoder.JSONDecodeError 的异常。

