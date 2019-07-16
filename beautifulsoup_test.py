#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Hello</p>','lxml')
print(soup.p.string)
