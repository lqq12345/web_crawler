#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests

r = requests.get('https://baidu.com')
print(r.cookies)#调用cookies属性即获得Cookies
for key,value in r.cookies.items():#用items()方法将其化为元组组成列表，遍历输出每一个Cookie的名和值
    print(key + '=' + value)

headers = {
    'Cookie': 'l_n_c=1; q_c1=a04bb53b39b24db688e8bc29f1979775|1557061260000|1557061260000; _xsrf=9f1700d79a082df6aad6d673c950ca00; n_c=1; d_c0="AOCnGQIZYg-PTuRflpHeOxxJZ3XCRNd3EGE=|1557061262"; _zap=37ff80d9-1518-4e57-8866-194a6137faba; _xsrf=6IZVzcKupo7bjoqa9mNCgzcX9ZH2cRqD; l_cap_id="ZjliMTU1ZTVhNWRlNDA4YmFhOWEzMjVhYTFiNzM1MWY=|1557144860|c61251f137134fbfec2c20a6cac8a54682c32de2"; r_cap_id="YmQ2MGMwMWM1NjAxNDY4ZDlmZjFhZWMyYzk1NWU4NjM=|1557144860|4047b58958a99090212141ea331ebcbcd0913585"; cap_id="ZjliY2JiZTA0MDMyNDhhOWI2YjgxNzkwNDAxNWY4MDE=|1557144860|2ccb5ccd0029da2e4390385e255981fca58c96e6\"; tgw_l7_route=060f637cd101836814f6c53316f73463; capsion_ticket="2|1:0|10:1557319810|14:capsion_ticket|44:YjdlMjgxZGQxNzVmNDcwYWJlYTEyNmUxNWE0MjRkNjk=|5139d4ef76b0cdee372f27a00f71998416a5afecca5b48584e0510b28e615a58"; z_c0="2|1:0|10:1557319847|4:z_c0|92:Mi4xb1hlR0JBQUFBQUFBNEtjWkFobGlEeVlBQUFCZ0FsVk5weDdBWFFCbTVkak9NbWpocEtCYXZiRDVvMUVmckczcUhn|979ace95579fb1eaeff80937c6d5e4c285eee0b2d7565e9d6d66883a6a819e8d"',
    
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
}
url = 'https://www.zhihu.com/'
r1 = requests.get(url,headers = headers)
print(r1.text)
