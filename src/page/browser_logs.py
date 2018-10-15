import os
import sys
import time
sys.path.append(os.path.dirname(os.getcwd()))
from page.chrome_base import ChromeBase

class BrowserLogs(ChromeBase):
	def __init__(self):
		super(BrowserLogs, self).__init__()
		# self.get_current_timestamp()
		self.has_browser_msg = False

	# def get_current_timestamp(self):
	# 	self.last_timestamp = time.time()
	# 	return self.last_timestamp

	def get_log(self, log_type):
		'''
		@param:
			browser     - browser log
			driver      - driver log
			perfermance - performance log
			
		'''
		# from pprint import pprint
		# pprint(self.driver.get_log('browser'))
		return self.driver.get_log(log_type)

	def get_browser_log(self):
		'''
		if get js error or 404 or 500 status will show in browser log
		'''
		self.bs_log = self.get_log('browser')
		return self.bs_log

	def parse_browser_log(self):
		log_level_key = 'level'
		log_message_key = 'message'
		log_level_expected_val = 'SEVERE'
		log_entry = self.get_browser_log()
		# from pprint import pprint
		# pprint(log_entry)
		browser_messages = []
		if not log_entry:
			# print(111111111111)
			self.has_browser_msg = True
			return 
		
		for log_info in log_entry:
			log_level = log_info.get(log_level_key)
			log_msg = log_info.get(log_message_key)
			if log_msg and (log_level == log_level_expected_val):
				browser_messages.append(log_msg)

		return browser_messages

	def check_browser_error_by_current_url(self):
		current_url = self.driver.current_url
		# print(current_url)
		netloc = self.get_netloc(current_url)
		# print(netloc)
		# self.check_browser_error_by_host(netloc)
		self.check_browser_error_by_startwith_host(netloc)

	def check_browser_error_by_startwith_host(self, url):
		browser_messages = self.parse_browser_log()
		len_url = len(url)
		if not browser_messages:
			print("Nothing to worry!")
			return
		
		try:
			for item in browser_messages:
				msg = 'Find some error in browser log: \n{}'.format(browser_messages)
				assert url != item[:len_url], msg

		except Exception as e:
			raise e


	def check_browser_error_by_host(self, url):
		browser_messages = self.parse_browser_log()
		# from pprint import pprint
		# pprint (browser_messages)
		
		try:
			import json
			contents = json.dumps(browser_messages)
			
			browser_urls = self.get_urls_in_browser_msgs(contents)
			if not browser_urls:

				return
			browser_urls = ''.join(browser_urls)
			# pprint(browser_urls)
			if browser_urls:
				msg = 'Find some error in browser log: \n' + contents
				assert url not in browser_urls, contents
		except Exception as e:
			raise e
		
	def get_urls_in_browser_msgs(self, browser_msg=''):
		import re
		import json

		if self.has_browser_msg:
			return
		if not browser_msg :
			raise Exception('Did you forget to call parse_browser_log or pass browser msg?')

		try:
			# contents = json.dumps(browser_msg)
			return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', browser_msg)

		except Exception as e:
			from pprint import pprint
			print('--'*20)
			pprint(browser_msg)
			print('--'*20)
			raise e

# 	def get_fresh_log(self, last_timestamp=0):
# 		'''
# 		get the log info after timestamp
# 		@param:
# 			last_timestamp: time stamp
# 		@notice:
# 			driver should set performance log
# 		'''
# 		last_timestamp = last_timestamp or self.last_timestamp
# 		entries = self.driver.get_log("performance")
# 		filtered = []

# 		for entry in entries:
# 			if entry["timestamp"] > self.last_timestamp:
# 				filtered.append(entry)

# 				if entry["timestamp"] > last_timestamp:
# 					last_timestamp = entry["timestamp"]

# 		self.last_timestamp = last_timestamp

# 		return filtered

# 	def get_response_infos(self):
# 		rsp = {
# 			'headers': None,
# 			'status': None
# 		}
# 		for responseReceived in self.driver.get_log('performance'):
# 			try:
# 				response = json.loads(responseReceived[u'message'])[u'message'][u'params'][u'response']
				
# 				if response[u'url'] == self.driver.current_url:
# 					rsp["headers"] = response[u'headers'] 
# 					rsp['status'] = (response[u'status'], response[u'statusText'])
# 			except:
# 				pass
# 		return rsp

# 	def _get_log(self):
		

# 		last_timestamp = self.last_timestamp
# 		entries = self.driver.get_log("performance")
# 		filtered = []

# 		for entry in entries:
# 			# check the logged timestamp against the 
# 			# stored timestamp
# 			if entry["timestamp"] > self.last_timestamp:
# 				filtered.append(entry)

# 				# save the last timestamp only if newer 
# 				# in this set of logs
# 				if entry["timestamp"] > last_timestamp:
# 					last_timestamp = entry["timestamp"]

# 		# store the very last timestamp
# 		self.last_timestamp = last_timestamp

# 		return filtered

# 	def get_performance_logs(self):
# 		self.p_log = self.driver.get_log('performance')
# 		return self.p_log

# 	def get_flash_performance_logs(self):
# 		self.p_new_log = self._get_log()
# 		return self.p_new_log

	

# 	def get_browser_logs(self):
# 		return self.driver.get_log('browser')

# 	def get_driver_logs(self):
# 		return self.driver.get_log('driver')

# 	def get_browser_severe_logs(self, level='SEVERE'):
# 		log_infos = self.get_browser_logs()
# 		# print(22222222, log_infos)
# 		f_level = 'level'
# 		f_msg = 'message'
# 		server_level_logs = []
# 		for plog in log_infos:
# 			# print(plog[f_level])
# 			if plog[f_level] == level:
# 				server_level_logs.append(plog[f_msg])

# 		return server_level_logs


# 	def get_requests_and_response_headers_by_url(self, request_url, level='INFO', key_name='url'):
# 		log_infos = self.p_log
# 		f_level = 'level'
# 		f_msg = 'message'
# 		f_network_response = 'Network.responseReceived'
# 		f_network_sent = '"Network.requestWillBeSent"'
# 		regex = get_regex_by_type('url', request_url)
# 		expect_url = '\"%s\":\"%s\"' % (key_name, request_url)

# 		responsestr = None
# 		requeststr = None


# 		for plog in log_infos:
# 			if plog[f_level] == level:
# 				msg = plog[f_msg]
				
# 				real_url = get_values_by_regex(msg, regex)
# 				if not real_url:
# 					continue
# 				if real_url[0] == expect_url and f_network_response in msg:
# 					responsestr = msg
# 				elif real_url[0] == expect_url and f_network_sent in msg:
# 					requeststr = msg
# 				# if (f_network_response in msg or f_network_sent in msg) and (request_url in msg):
# 				# 	return_logs.append(msg)

# 		return responsestr, requeststr

# 	def get_network_loadingFailed(self, level='INFO'):
# 		log_infos = self.p_log
# 		f_level = 'level'
# 		f_msg = 'message'
# 		f_network_loadingFailed = 'Network.loadingFailed'
		
# 		responsestr = None
		
# 		for plog in log_infos:
# 			if plog[f_level] == level:
# 				msg = plog[f_msg]
				
# 				if f_network_response in msg:
# 					responsestr = msg

# 		return responsestr

# 	def general_request_infos(self, request_str):
# 		if not request_str:
# 			raise Exception("param is empty")
# 		import json
# 		flag_str = 'Network.requestWillBeSent'
# 		try:
# 			jsondata = json.loads(request_str)
# 			msg = jsondata['message']
# 			params = msg['params']
			
# 			if flag_str in request_str:

# 				return params.get('request')

# 		except Exception as e:
# 			raise e

# 	def general_response_infos(self, response_str):
# 		if not response_str:
# 			raise Exception("param is empty")
# 		import json
# 		flag_str = 'Network.responseReceived'
# 		try:
# 			jsondata = json.loads(response_str)
# 			msg = jsondata['message']
# 			params = msg['params']
			
# 			if flag_str in response_str:

# 				return params.get('response')

# 		except Exception as e:
# 			raise e

# 	def get_requests_and_response_infos_by_url(self, request_url, level='INFO', key_name='url'):
# 		log_infos = self.p_log
# 		f_level = 'level'
# 		f_msg = 'message'
# 		f_network_response = 'Network.responseReceived'
# 		f_network_sent = '"Network.requestWillBeSent"'
# 		ret_rsp = None
# 		ret_rq = None
		
# 		for plog in log_infos:
# 			if plog[f_level] == level:
# 				msg = plog[f_msg]
# 				from pprint import pprint
# 				# pprint(msg)
# 				if f_network_response in msg:
# 					response_log_obj = self.general_response_infos(msg)
					
# 					if response_log_obj.get('url') == request_url:
# 						ret_rsp = response_log_obj
# 				elif f_network_sent in msg:
# 					request_log_obj = self.general_request_infos(msg)
# 					if request_log_obj.get('url') == request_url:
# 						ret_rq = request_log_obj
# 				# if (f_network_response in msg or f_network_sent in msg) and (request_url in msg):
# 				# 	return_logs.append(msg)

# 			if ret_rsp and ret_rq:
# 				break

# 		return ret_rsp, ret_rq

# 	def get_requests_and_response_all_infos_by_url(self, request_url, level='INFO', key_name='url'):
# 		log_infos = self.p_log
# 		f_level = 'level'
# 		f_msg = 'message'
# 		f_network_response = 'Network.responseReceived'
# 		f_network_sent = '"Network.requestWillBeSent"'
# 		ret_rsp = []
# 		ret_rq = []
		
# 		for plog in log_infos:
# 			if plog[f_level] == level:
# 				msg = plog[f_msg]

# 				if f_network_response in msg:
# 					response_log_obj = self.general_response_infos(msg)
# 					if request_url in response_log_obj.get('url') :
# 						ret_rsp.append(response_log_obj)
# 				elif f_network_sent in msg:
# 					request_log_obj = self.general_request_infos(msg)
# 					if request_url in request_log_obj.get('url'):
# 						ret_rq.append(request_log_obj)
# 				# if (f_network_response in msg or f_network_sent in msg) and (request_url in msg):
# 				# 	return_logs.append(msg)

# 		return ret_rsp, ret_rq

# 	def get_new_requests_and_response_infos_by_url(self, request_url, level='INFO', key_name='url'):
# 		from pprint import pprint
# 		log_infos = self.p_new_log
# 		f_level = 'level'
# 		f_msg = 'message'
# 		f_network_response = 'Network.responseReceived'
# 		f_network_sent = '"Network.requestWillBeSent"'
# 		ret_rsp = None
# 		ret_rq = None
		
# 		for plog in log_infos:
# 			if plog[f_level] == level:
# 				msg = plog[f_msg]

# 				if f_network_response in msg:
# 					response_log_obj = self.general_response_infos(msg)
# 					if request_url in response_log_obj.get('url'):
# 						pprint(msg)
# 					if response_log_obj.get('url') == request_url:
# 						ret_rsp = response_log_obj
# 				elif f_network_sent in msg:
# 					request_log_obj = self.general_request_infos(msg)
# 					if request_url in request_log_obj.get('url'):
# 						pprint(msg)
# 					if request_log_obj.get('url') == request_url:
# 						ret_rq = request_log_obj
# 				# if (f_network_response in msg or f_network_sent in msg) and (request_url in msg):
# 				# 	return_logs.append(msg)

# 			if ret_rsp and ret_rq:
# 				break

# 		return ret_rsp, ret_rq


# 	def general_request_and_response_infos(self, response_log_obj, request_log_obj):

# 		if not response_log_obj or not request_log_obj:
# 			raise Exception("param is empty")
# 		flag = '----' * 20

# 		infos = """
# General:
# 	Request URL: %s
# 	Request Method: %s
# 	Status Code: %s %s
# 	Remote Address: %s:%s
# 	Referrer Policy: %s
# %s
# Response Headers:
# 	%s
# %s
# Request Headers:
# 	%s
# %s
# Form Data:
# 	%s

# """ %	(
# 			request_log_obj.get('url'),
# 			request_log_obj.get('method'),
# 			response_log_obj.get('status'), response_log_obj.get('statusText'),
# 			response_log_obj.get('remoteIPAddress'), response_log_obj.get('remotePort'),
# 			request_log_obj.get('referrerPolicy'),
# 			flag,
# 			response_log_obj.get('headers'),
# 			flag,
# 			request_log_obj.get('headers'),
# 			flag,
# 			request_log_obj.get('postData')
# 		)
# 		print(infos)

# 	def get_response_status(self, responses):
# 		if not responses:
# 			raise Exception("param is empty")

# 		return responses.get('status') 

	
# 	def get_driver_logs(self, level='SEVERE'):
# 		log_infos = self.driver.get_log('driver')
# 		f_level = 'level'
# 		f_msg = 'message'
# 		server_level_logs = []
# 		for plog in log_infos:
# 			if plog[f_level] == level:
# 				server_level_logs.append(plog[f_msg])

# 		return server_level_logs
