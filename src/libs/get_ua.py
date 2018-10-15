import requests as req
from bs4 import BeautifulSoup
import time
import codecs

# url = 'http://www.useragentstring.com/pages/useragentstring.php?name=Firefox'
def mkdir_if_not_existed(file_name):
	import os
	path = os.path.dirname(file_name)
	if not os.path.exists(path):
		os.makedirs(path)


def pretty_write(py_obj, file_name):
	import os
	import json
	var_name = file_name.replace('+', '_')
	file_name = os.path.join('..', 'user_agents', var_name + '.py')
	
	try:
		write_contents = json.dumps(py_obj, indent=4)
	except Exception as e:
		print(e)
		write_contents = py_obj
	mkdir_if_not_existed(file_name)
	import codecs
	
	write_contents = var_name + '_User_Agent' + ' = ' + write_contents
	flag = "More Safari  user agents strings -->>"
	write_contents.replace(flag, '')
	with codecs.open(file_name,'w','utf-8') as fjson:
		fjson.write(write_contents)

def getUa(br):
	user_agent_list = []

	url = 'http://www.useragentstring.com/pages/useragentstring.php?name='+br
	r = req.get(url)

	if r.status_code == 200:
		soup = BeautifulSoup(r.content,'html.parser')
	else:
		soup = False

	if soup:
		div = soup.find('div',{'id':'liste'})
		lnk = div.findAll('a')

		for i in lnk:
			try:
				user_agent_list.append(i.text)
			except Exception as e:
				raise e
		pretty_write(user_agent_list, br)
			
	else:
		print('No soup for '+br)

lst = ['Firefox','Internet+Explorer','Opera','Safari','Chrome','Edge','Android+Webkit+Browser']

for i in lst:
	getUa(i)
	time.sleep(20)