#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from lxml import etree

text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
</div>
'''

#html = etree.HTML(text)#初始化，构造一个XPath解析对象，且etree模块可对HTML文本进行自动修正
html = etree.parse('./test.html',etree.HTMLParser())#读取文本文件进行解析
result = etree.tostring(html)
#print(result.decode('utf-8'))

r1 = html.xpath('//li[1]/ancestor::*')
print(r1)

r2 = html.xpath('//li[1]/ancestor::div')
print(r2)

r3 = html.xpath('//li[1]/attribute::*')
print(r3)

r4 = html.xpath('//li[1]/child::a[@href = "link1.html"]')
print(r4)

r5 = html.xpath('//li[1]/descendant::span')
print(r5)

r6 = html.xpath('//li[1]/following::*[2]')
print(r6)

r7 = html.xpath('//li[1]/following-sibling::*')
print(r7)
