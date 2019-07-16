#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from urllib.parse import urlencode
from pyquery import PyQuery as pq
import requests
from pymongo import MongoClient


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.3'
}

base_url = 'https://m.weibo.cn/api/container/getIndex?'
max_page = 14

#使用 MongoDB 存储数据需要做的前提工作
client = MongoClient('mongodb://localhost:27017/')#创造一个 MongoDB 的连接对象
db = client['Weibo']#指定一个要操作的数据库，也可写成 db=client.Weibo
collection = db['Weibo']#指定一个要操作的集合，也可写成 collenction=db.Weibo

#分析ajax，得到结果是，每次请求的url就是base_url+对应的四个参数；获取对应页的返回结果
def get_page(page):
    params = {
        'type': 'uid',
        'value': '2803301701',
        'containerid': '1076032803301701',
        'page': page
    }
    url = base_url + urlencode(params)#urllib库里面有个urlencode函数，可以把key-value这样的键值对转换成我们想要的格式，返回的是a=1&b=2这样的字符串
#print(url)

    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
    except requests.ConnectionError as e:
        print('Error',e.args)

#解析返回的结果，从结果中提取我们想要的信息
def parse_page(json):
    if json:
        items = json.get('data')#获取 data 中的内容
        #print('-------------------------------------------------')
        items = items.get('cards')
        #print(items)
        #print('-------------------------------------------------')
        for item in items:#用generator（生成器）遍历cards
            item = item.get('mblog')#获取 mblog 中的信息
            print('item    ')
            weibo = {}#定义一个新的字典，将mblog中的各个信息赋值到这个新的字典中以返回
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()#借助于 PyQuery 将正文中国呢到 HTML 标签去掉
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo#执行过程中遇到“yield”就中断返回一个值，下次又从“yield”后继续执行
    else:
        print('not json')

#把结果写入到MongoDB数据库中
def save_to_mongo(result):
    if collection.insert_one(result):#使用 insert() 方法将 result 插入到collenction中
        print('Save to mongo')
    else:
        print('failed to save')

#主程序，遍历一下page，先获取每一页的response，然后从返回的json结果中提取想要的信息，然后把结果打印出来并写入MongoDB数据库中
if __name__ == '__main__':
    for page in range(1,max_page + 1):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
            save_to_mongo(result)

