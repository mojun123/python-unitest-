import requests as req
from bs4 import BeautifulSoup
import time
import codecs
from random import randint

# url = 'https://developers.whatismybrowser.com/useragents/explore/software_name/android-browser/2'
def mkdir_if_not_existed(file_name):
	import os
	path = os.path.dirname(file_name)
	if not os.path.exists(path):
		os.makedirs(path)


def pretty_write(py_obj, file_name):
	import os
	import json
	var_name = file_name.replace('+', '_').replace('-', '_') + '_user_agent'
	file_name = os.path.join('..', 'user_agents', var_name + '.py')
	
	try:
		write_contents = json.dumps(py_obj, indent=4)
	except Exception as e:
		print(e)
		write_contents = py_obj
	mkdir_if_not_existed(file_name)
	import codecs
	
	write_contents = var_name  + ' = ' + write_contents
	flag = "More Safari  user agents strings -->>"
	write_contents.replace(flag, '')
	with codecs.open(file_name,'w','utf-8') as fjson:
		fjson.write(write_contents)

def getUa(br, index, lst_type="software"):
	user_agent_list = []
	url = ''
	if lst_type == 'software':
		url = 'https://developers.whatismybrowser.com/useragents/explore/software_name/'+ br + '/' + str(index)
	elif lst_type == 'system':
		url = 'https://developers.whatismybrowser.com/useragents/explore/operating_system_name/'+ br + '/' + str(index)
	elif lst_type == 'platform':
		url = 'https://developers.whatismybrowser.com/useragents/explore/operating_platform/' + br + '/' + str(index)

	print(url)
	proxies = {
			  'http' : 'socks5://192.168.10.20:1081',
			  'https': 'socks5://192.168.10.20:1081'
			}
	headers = {
		'Host': 'developers.whatismybrowser.com',
		'Connection': 'keep-alive',
		'Pragma': 'no-cache',
		'Cache-Control': 'no-cache',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
	}
	
	

	r = req.get(url, proxies=proxies)

	if r.status_code == 200:
		soup = BeautifulSoup(r.content,'html.parser')
	else:
		soup = False

	if soup:
		div = soup.find('tbody')
		lnk = div.findAll('a')

		for i in lnk:
			try:
				user_agent_list.append(i.text)
			except Exception as e:
				raise e
		return user_agent_list
			
	else:
		print('No soup for '+br)

page = 11

lst = ['android-browser','internet-explorer', 
	'firefox', 'facebook-app', 
	'opera-mini', 'opera', 
	'safari','chrome',
	'uc-browser']

operating_system_list = ['ios','macos', 'windows','android']
operating_platform_list = ['iphone', 'ipad']
for i in lst:
	contents = []
	for index in range(1, page):
		contents += getUa(i, index, 'software')
		# sleep(randint(1,20))
		time.sleep(randint(1,20))
	pretty_write(contents, i)

for i in operating_system_list:
	contents = []
	for index in range(1, page):
		contents += getUa(i, index, 'system')
		# sleep(randint(1,20))
		time.sleep(randint(1,20))
	pretty_write(contents, i)

for i in operating_platform_list:
	contents = []
	for index in range(1, page):
		contents += getUa(i, index, 'platform')
		# sleep(randint(1,20))
		time.sleep(randint(1,20))
	pretty_write(contents, i)