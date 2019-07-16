x                                                                  # -*- coding: utf-8 -*-

import requests
import json
import csv

#定义要爬取的微博ID
id = '1562288742'

#设置代理IP
proxy_addr='122.241.72.191.808'

#定义获取头
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
}

#定义页面打开函数
def use_proxy(url,proxy_addr):
	s=requests.Session()
	s.proxies = {proxy_addr}
	req = s.get(url,headers = headers)
	return req.text
	
#获取微博主页的containerid（爬取微博内容时需要）
def get_containerid(url):
	data = use_proxy(url,proxy_addr)#从微博上抓取下来的网页源码是json形式的
	#json.loads(字符串)将json代码转化成Python代码，输出是一个字典，然后用Python的get()方法，获取键值为'data'的内容
	content = json.loads(data).get('data')
	for data in content.get('tabsInfo').get('tabs'):
		if(data.get('tab_type')=='weibo'):
			containerid=data.get('containerid')
	return containerid

#获取微博账号的用户基本信息，如：微博昵称、微博地址、微博头像、关注人数、粉丝数、性别等
def get_userInfo(id):
	url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
	data=use_proxy(url,proxy_addr)
	content=json.loads(data).get('data')
	profile_image_url=content.get('userInfo').get('profile_image_url')
	description=content.get('userInfo').get('description')
	profile_url=content.get('userInfo').get('profile_url')
	verified=content.get('userInfo').get('verified')
	guanzhu=content.get('userInfo').get('follow_count')
	name=content.get('userInfo').get('screen_name')
	fensi=content.get('userInfo').get('followers_count')
	gender=content.get('userInfo').get('gender')
	urank=content.get('userInfo').get('urank')
	with open(file,'w',encoding='utf-16') as fh:
		writer=csv.writer(fh)
		writer.writerow(['微博昵称：'+name,'微博主页地址：'+profile_url,'微博头像地址：'+profile_image_url,'是否认证：'+str(verified),'微博说明：'+description,'关注人数：'+str(guanzhu),'粉丝数：'+str(fensi),'性别：'+gender,'微博等级：'+str(urank)])
		
	
	#with open(file,'a',encoding='utf-8') as fh:
	#	fh.write("微博昵称："+name+"\n"+"微博主页地址："+profile_url+"\n"+"微博头像地址："+profile_image_url+"\n"+"是否认证："+str(verified)+"\n"+"微博说明："+description+"\n"+"关注人数："+str(guanzhu)+"\n"+"粉丝数："+str(fensi)+"\n"+"性别："+gender+"\n"+"微博等级："+str(urank)+"\n")
	#	print("微博昵称："+name+"\n"+"微博主页地址："+profile_url+"\n"+"微博头像地址："+profile_image_url+"\n"+"是否认证："+str(verified)+"\n"+"微博说明："+description+"\n"+"关注人数："+str(guanzhu)+"\n"+"粉丝数："+str(fensi)+"\n"+"性别："+gender+"\n"+"微博等级："+str(urank)+"\n")

#获取微博内容信息,并保存到文本中，内容包括：每条微博的内容、微博详情页面地址、点赞数、评论数、转发数等
def get_weibo(id,file):
	i=1
	while True:
		url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
		weibo_url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id+'&containerid='+get_containerid(url)+'&page='+str(i)
		try:
			data=use_proxy(weibo_url,proxy_addr)
			content=json.loads(data).get('data')
			cards=content.get('cards')
			if(len(cards)>0):
				for j in range(len(cards)):
					print("-----正在爬取第"+str(i)+"页，第"+str(j)+"条微博------")
					card_type=cards[j].get('card_type')
					if(card_type==9):
						mblog=cards[j].get('mblog')
						attitudes_count=mblog.get('attitudes_count')
						comments_count=mblog.get('comments_count')
						created_at=mblog.get('created_at')
						reposts_count=mblog.get('reposts_count')
						scheme=cards[j].get('scheme')
						text=mblog.get('text')
						with open(file,'a',encoding='utf-16') as fh:
							fieldnames = ['微博地址','发布时间','微博内容','点赞数','评论数','转发数']
							writer = csv.DictWriter(fh,fieldnames=fieldnames)
							if i==1 and j==0:
								writer.writeheader()
							writer.writerow({'微博地址':scheme,'发布时间':created_at,'微博内容':text,'点赞数':attitudes_count,'评论数':comments_count,'转发数':reposts_count})
						
                        #with open(file,'a',encoding='utf-8') as fh:
                        #    fh.write("----第"+str(i)+"页，第"+str(j)+"条微博----"+"\n")
                        #    fh.write("微博地址："+str(scheme)+"\n"+"发布时间："+str(created_at)+"\n"+"微博内容："+text+"\n"+"点赞数："+str(attitudes_count)+"\n"+"评论数："+str(comments_count)+"\n"+"转发数："+str(reposts_count)+"\n")
				i+=1
			else:
				break
		except Exception as e:
			print(e)
			pass

if __name__=="__main__":
	#file=id+".txt"
	file = id+".csv"
	get_userInfo(id)
	get_weibo(id,file)
