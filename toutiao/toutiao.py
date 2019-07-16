#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from urllib.parse import urlencode
from pyquery import PyQuery as pq
import requests
from pymongo import MongoClient
import os
#hashlib是一个提供字符加密功能的模块，包含MD5和SHA的加密算法
from hashlib import md5
from multiprocessing.pool import Pool


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.3'
}

base_url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search'

#max_page = 14

#使用 MongoDB 存储数据需要做的前提工作
client = MongoClient('mongodb://localhost:27017/')#创造一个 MongoDB 的连接对象
db = client['Weibo']#指定一个要操作的数据库，也可写成 db=client.Weibo
collection = db['Weibo']#指定一个要操作的集合，也可写成 collenction=db.Weibo

#分析ajax，得到结果是，每次请求的url就是base_url+对应的九个参数；获取对应页的返回结果
def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
    }
    url = base_url +urlencode(params)
    #urllib库里面有个urlencode函数，可以把key-value这样的键值对转换成我们想要的格式，返回的是a=1&b=2这样的字符串
#print(url)

    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(response.status_code)
    except requests.ConnectionError as e:
        print('Error',e.args)

#解析返回的结果，从结果中提取我们想要的信息
def get_images(json):
    if json.get('data'):#获取 data 中的内容
        items = json.get('data')
        #print('-------------------------------------------------')
        for item in items:#用generator（生成器）遍历data
            title = item.get('title')#获取 title 中的信息
            #print('item    ')
            images = item.get('image_list')
            for image in images:
                yield {
                    'image': image.get('url'),
                    'title': title
                }#执行过程中遇到“yield”就中断返回一个值，下次又从“yield”后继续执行
    else:
        print('not json')

#把读取到对应url的图片保存下来
def save_image(item): #item就是get_images函数中返回的字典
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))#用对应的标题创建一个文件夹用于存放此标题下获取到的图片
    try:
        response = requests.get(item.get('image'))#根据get_image中获取到图片的url来获取图片
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
            #"{1} {0} {1}".format("hello", "world")  # 设置指定位置  》'world hello world'
            #图片的名称可以使用其内容的 MD5 值，这样可以去除重复
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    #以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
                    f.write(response.content)
            else:
                print('Already Downloaded',file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')

#传入对应的offset表明当前查找的是哪一页，获取当前页的response，然后从返回的json调用get_images提取图片对应的url，把提取出来的每一张图片都保存下来
def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


#把结果写入到MongoDB数据库中
#def save_to_mongo(result):
#    if collection.insert_one(result):#使用 insert() 方法将 result 插入到collenction中
#        print('Save to mongo')
#    else:
#        print('failed to save')

GROUP_START = 1
GROUP_END = 1


#主程序，遍历一下page，先获取每一页的response，然后从返回的json结果中提取想要的信息，然后把结果打印出来并写入MongoDB数据库中
if __name__ == '__main__':
    pool = Pool()#创建进程池
    groups = ([x*20 for x in range(GROUP_START,GROUP_END+1)])#生成器，在x属于[1，21）下生成‘x*20’
    pool.map(main,groups)#把mian函数依次作用于groups生成的每个元素上，得到一个object并返回
    pool.close()#关闭进程池，不再接受新的任务
    pool.join()#主进程阻塞等待子进程的退出（被终止的进程需要被父进程调用wait（join等价于wait），否则进程会变成僵尸进程）

