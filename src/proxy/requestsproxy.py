import requests

class RandomProxy(object):
	"""docstring for RandomProxy"""
	def __init__(self, proxy_file):
		super(RandomProxy, self).__init__()
		self.url = 'https://developers.google.com/speed/pagespeed/insights'
		self.proxy_file = proxy_file

	def get_proxy_str(self, host, port, proxy_type='http'):
		if proxy_type == 'https':
			return 'https://{0}:{1}'.format(host, port)
		elif proxy_type == 'http':
			return 'http://{0}:{1}'.format(host, port)
		elif proxy_type == 'socks5':
			return 'socks5://{0}:{1}'.format(host, port)
		elif proxy_type == 'socks4':
			return 'socks4://{0}:{1}'.format(host, port)

	def get_proxy_str_from_dict(self, proxies):
		if not proxies:
			return 
		if not isinstance(proxies, dict):
			raise Exception('param is not dict: %s' % proxies)

		for key, val in proxies.items():
			return "{0}://{1}".format(key, val)


	def loads_proxy_from_file(self, file=None):
		# file = '../../conf/proxy.json'
		file = file or self.proxy_file
		import json
		import codecs
		with codecs.open(file, 'rb','utf-8') as file_obj:
			try:
				self.proxies = json.load(file_obj)
				return self.proxies
			except Exception as e:
				raise e 

	def check_proxy(self, proxy):
		try:
			print("used proxy: {}".format(proxy))
			session = requests.Session()
			request_retry = requests.adapters.HTTPAdapter(max_retries=1)
			session.mount(self.url,request_retry)
			rsp = session.get(self.url, proxies=proxy, timeout=5)
			if rsp.status_code != 200:
				return False
			else:
				print(rsp.status_code)
				return proxy
		except Exception as e:
			print("cannot connected by this proxy: {}\n".format(proxy))
			print(str(e))
			return False

	def random_proxy(self, proxies=None):
		if proxies and not isinstance(proxies, list):
			raise Exception("proxies is not a list")
		import random

		proxies = proxies or self.loads_proxy_from_file()
		total = len(proxies)
		used_proxy = []
		
		b_ok = False
		while not b_ok :


			proxie =  random.choice(proxies)
			print('proxie: ', proxie)
			if proxie in used_proxy:
				continue
			count = len(used_proxy)
			if count == total :
				print("have no work proxy")
				b_ok = True
				break
			new_proxie = self.check_socks(proxie)
			b_ok = self.check_proxy(new_proxie)
			print("b_ok: ", b_ok)
			if b_ok:
				return proxie
			used_proxy.append(proxie)


	# def check_proxy(self, proxies=None):
	# 	import random

	# 	proxies = proxies or self.proxies
	# 	print(proxies)
	# 	total = len(proxies)
	# 	used_proxy = []
		
	# 	b_ok = False
	# 	count = 0
	# 	while not b_ok :


	# 		proxie =  random.choice(proxies)
	# 		print('proxie: ', proxie)
	# 		if proxie in used_proxy:
	# 			continue
	# 		count = len(used_proxy)
	# 		if count == total :
	# 			print("have no work proxy")
	# 			b_ok = True
	# 			break
	# 		new_proxie = self.check_socks(proxie)
	# 		try:
	# 			# rsp = requests.get(self.url, proxies=new_proxie, timeout=5)
	# 			session = requests.Session()
	# 			request_retry = requests.adapters.HTTPAdapter(max_retries=1)
	# 			session.mount(self.url,request_retry)
	# 			rsp = session.get(self.url, proxies=new_proxie, timeout=5)
	# 			if rsp.status_code != 200:
	# 				used_proxy.append(proxie)
	# 				print(rsp.status_code)
	# 				b_ok = False
	# 			else:

	# 				print(rsp.status_code)
	# 				return proxie
	# 		except Exception as e:
	# 			print("cannot connected by this proxy: ",str(e))
	# 			b_ok = False
			
	def check_socks(self, proxies):
		if not isinstance(proxies, dict):
			raise Exception("param is not dict")

		for key ,val in proxies.items():
			if 'socks' in key:
				print("socks to https")
				proxies = {
					'https': key + '://' + val
				}

		return proxies

def test():
	file = '../../conf/proxy.json'
	_obj = RandomProxy(file)
	proxys = _obj.random_proxy()
	# proxys = _obj.check_proxy()
	print(proxys)
	print(_obj.get_proxy_str_from_dict(proxys))


if __name__ == '__main__':
	test()

