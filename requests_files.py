#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests
import re

files = {'file':open('favicon.ico','rb')}
r=requests.post('http://httpbin.org/post',files = files)
print(r.text)
