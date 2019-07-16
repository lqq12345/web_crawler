#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pymongo

#链接到数据库
client = pymongo.MongoClient(host='localhost',port=27017)
#client = MongoClient('mongodb://localhost:27017/')

#指定数据库
db = client.test
#db = client['test']

#指定集合
collection = db.students
#collection = db['students']

#数据
student = {
    'id':'20170101',
    'name':'Jordan',
    'age':20,
    'gender':'male'
}

result = collection.insert_one(student)
print (result)
