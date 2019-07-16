#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests
import re

cookies = {
    "d_c0": "AECA7v-aPwqPTiIbemmIQ8abhJy7bdD2VgE=|1468847182",
    "login": "NzM5ZDc2M2JkYzYwNDZlOGJlYWQ1YmI4OTg5NDhmMTY=|1480901173|9c296f424b32f241d1471203244eaf30729420f0",
    "n_c": "1",
    "q_c1": "395b12e529e541cbb400e9718395e346|1479808003000|1468847182000",
    "l_cap_id": "NzI0MTQwZGY2NjQyNDQ1NThmYTY0MjJhYmU2NmExMGY=|1480901160|2e7a7faee3b3e8d0afb550e8e7b38d86c15a31bc",
    "d_c0": "AECA7v-aPwqPTiIbemmIQ8abhJy7bdD2VgE=|1468847182",
    "cap_id": "N2U1NmQwODQ1NjFiNGI2Yzg2YTE2NzJkOTU5N2E0NjI=|1480901160|fd59e2ed79faacc2be1010687d27dd559ec1552a"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.3",
    "Referer": "https://www.zhihu.com/"
}

url ="https://www.zhihu.com/explore"

r = requests.get(url, headers = headers)
pattern = re.compile('explore-feed.*?requestion_link.*?>(.*?)</a>',re.S)
titles = re.findall(pattern,r.text)
print(titles)
