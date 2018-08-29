from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import unittest
import os
import sys
import time
sys.path.append(os.path.dirname(os.getcwd()))
from utils.file_handle import *
from utils._regex import *


class BasePage(object):

	def __init__(self, driver, base_url, page_title):
		self.driver = driver

		self.base_url = base_url
		self.page_title = page_title
		self.last_timestamp = 0

	def assrt_page(self):
		assert self.page_title in self.driver.title
	
	def _open(self, url, page_title):
		try:
			self.driver.get(url)
			return True
		except Exception as e:
			raise e
			return None
		
		self.driver.maximize_window()
		# assert self.assrt_page(page_title), u"cannot open: %s"%url
	
	def open(self):
		return self._open(self.base_url, self.page_title)

	def get_js_error(self):
		logs = self.driver.get_log('browser')
		return logs

	def assert_js_error(self, assert_msg):
		logs = self.get_js_error()
		for log in logs:
			if log['level'] == 'SEVERE':
				assert assert_msg not in log

		

	def expected_wait_clickable_by_id(self, element_id, wait_time=30, attr="default"):

		try:
			element = WebDriverWait(self.driver, wait_time).until(
				EC.element_to_be_clickable((By.ID, element_id)));

			if attr == "default":
				return element
			elif attr == "text":
				return element.text
			else:
				attr = element.get_attribute(attr)
				return attr
		except Exception as e:
			# raise e
			return None

	def expected_wait_clickable_by_class(self, element_class, driver=None, wait_time=30):
		driver = driver or self.driver

		try:
			element = WebDriverWait(driver, wait_time).until(
				EC.element_to_be_clickable((By.CLASS_NAME, element_class)));
			return element
		except Exception as e:
			# raise e
			return None

	def expected_wait_clickable_by_xpath(self, xpath, driver=None, wait_time=30):
		driver = driver or self.driver

		try:
			element = WebDriverWait(driver, wait_time).until(
				EC.element_to_be_clickable((By.XPATH, xpath)));
			return element
		except Exception as e:
			# raise e
			return None

	def expected_wait_clickable_by_tag(self, element_tag_name, driver=None, wait_time=30):
		driver = driver or self.driver

		try:
			element = WebDriverWait(driver, wait_time).until(
				EC.element_to_be_clickable((By.TAG_NAME, element_tag_name)));
			return element
		except Exception as e:
			# raise e
			return None

	def expected_wait_located_by_xpath(self, xpath, wait_time=30, attr="default"):

		try:
			element = WebDriverWait(self.driver, wait_time).until(
				EC.presence_of_element_located((By.XPATH, xpath)));

			if attr == "default":
				return element
			elif attr == "text":
				return element.text
			else:
				attr = element.get_attribute(attr)
				return attr
			# return element
		except Exception as e:
			# raise e
			return None

	def expected_wait_located_by_id(self, element_id, wait_time=30):

		try:
			element = WebDriverWait(self.driver, wait_time).until(
				EC.presence_of_element_located((By.ID, element_id)));
			return element
		except Exception as e:
			# raise e
			return None

	def expected_wait_located_by_class(self, element_class, driver=None, wait_time=30):
		driver = driver or self.driver

		try:
			element = WebDriverWait(driver, wait_time).until(
				EC.presence_of_element_located((By.CLASS_NAME, element_class)));
			return element
		except Exception as e:
			# raise e
			return None


	def expected_wait_located_by_tag(self, element_tag_name, driver=None, wait_time=30):
		driver = driver or self.driver
		try:
			element = WebDriverWait(driver, wait_time).until(
				EC.presence_of_element_located((By.TAG_NAME, element_tag_name)));
			return element
		except Exception as e:
			# raise e
			return None

	
	
	def save_png(self, file_name):
		from PIL import Image
		import io
		verbose = 1
		# from here http://stackoverflow.com/questions/1145850/how-to-get-height-of-entire-document-with-javascript
		js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'
		scrollheight = self.driver.execute_script(js)
		if verbose > 0: 
			print (scrollheight)

		slices = []
		offset = 0
		while offset < scrollheight:
			if verbose > 0: 
				print ("offset: ", offset)

			self.driver.execute_script("window.scrollTo(0, %s);" % offset)
			img = Image.open(io.BytesIO(self.driver.get_screenshot_as_png()))
			offset += img.size[1]
			slices.append(img)

			if verbose > 0:
				self.driver.get_screenshot_as_file('%s/screen_%s.png' % ('/tmp', offset))
				print("scrollheight:", scrollheight)

		screenshot = Image.new('RGB', (slices[0].size[0], scrollheight))
		offset = 0
		for img in slices:
			screenshot.paste(img, (0, offset))
			# offset += img.size[1]
			img_height = img.size[1]
			offset += img_height

			bottom = scrollheight - offset
			if bottom <= img_height:
				offset += bottom - img_height
			print("add offet: ", offset, img.size[0], img.size[1])

		print(img.size)

		# path = os.path.dirname(file_name)
		# if not os.path.exists(path):

		# 	os.makedirs(path)
		mkdir_if_not_existed(file_name)

		screenshot.save(file_name)

	def find_element_by_name(self, e):

		# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
		return self.driver.find_element_by_name(e)

	def find_element_by_xpath(self, e):
		return self.driver.find_element_by_xpath(e)

	def find_elements_by_xpath(self, xpath):
		return self.driver.find_elements_by_xpath(xpath)

	def find_element_by_tag_name(self, e):
		return self.driver.find_element_by_tag_name(e)
			

	def find_element_by_id(self, e):
		return self.driver.find_element_by_id(e)

	def save_screenshot(self, name):
		mkdir_if_not_existed(name)
		return self.driver.save_screenshot(name)
		
	def find_elements_by_tag_name(self, e):
		return self.driver.find_elements_by_tag_name(e)

	def get_cookies(self):
		return self.driver.get_cookies()

	def add_cookie(self, cookies_dict):
		return self.driver.add_cookie(cookies_dict)

	def save_cookie_to_file(self, path):
		with open(path, 'wb') as filehandler:
			pickle.dump(self.driver.get_cookies(), filehandler)

	def load_cookie_from_file(self, path):
		cookies = file_content_to_py_object(path)
		if not cookies or not isinstance(cookies, list):
			raise Exception("get null or not list obj: %s, please check the cookie file" % cookies )
		for cookie in cookies:
			self.driver.add_cookie(cookie)

	def get_element_attribute_by_xpath(self, xpath, attr="href"):
		element = self.expected_wait_clickable_by_xpath(xpath)
		attr = element.get_attribute(attr)
		# self.driver.assertIsNoneNot(attr)
		assert attr != None

		return attr, element

	def assert_element_attribute(self, real_attr, expected_attr, msg="default"):
		if msg == "default":
			msg = "expected attribute: %s, but got real attribute: %s" % (expected_attr, real_attr)
		assert real_attr == expected_attr, msg

	def assertNotEqual_element_attribute(self, real_attr, expected_attr, msg="default"):
		if msg == "default":
			msg = "expected attribute: %s, but got real attribute: %s" % (expected_attr, real_attr)
		assert real_attr != expected_attr, msg

	def assertNotNone_element_attribute(self, expected_attr, msg="default"):
		if msg == "default":
			msg = "expected attribute not null, but got real attribute: %s" % expected_attr
		# print(expected_attr)
		assert expected_attr != None, msg

	def assert_in_element_attribute(self, real_attr, expected_attr, msg="default"):
		if msg == "default":
			msg = "expected attribute: %s, but got real attribute: %s" % (expected_attr, real_attr)
		assert expected_attr in real_attr, msg

	def _click(self, element, expected_url, flag=True):
		element.click()
		current_url = self.driver.current_url
		if not flag:
			self.assert_in_element_attribute(current_url, expected_url)
		else:
			self.assert_element_attribute(current_url, expected_url)

	def check_js_and_save_png(self, save_png_name=""):
		# print(self.get_js_error())
		self.assert_js_error("clatterans")
		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		save_png_name = save_png_name or '../screenshot/default_%s.png' % nowTime
		self.save_png(save_png_name)

	def scroll_to_offset(self, offset=0):
		self.driver.execute_script("window.scrollTo(0, %s);" % offset)


	def get_selected_option_by_xpath(self, xpath):
		# select = Select(driver.find_element_by_id('FCenter'))
		# xpath = '//*[@id="4"]/div[5]/table/tbody/tr/td/select'
		select = Select(self.expected_wait_located_by_xpath(xpath))
		selected_option = select.first_selected_option
		return selected_option.text

	def delete_all_cookies(self):
		self.driver.delete_all_cookies()

	def refresh(self):
		return self.driver.refresh()


	# def get_response_status(self):
	# 	for responseReceived in self.driver.get_log('performance'):
	# 		try:
	# 			response = json.loads(responseReceived[u'message'])[u'message'][u'params'][u'response']
	# 			if response[u'url'] == self.driver.current_url:
	# 				return (response[u'status'], response[u'statusText'])
	# 		except:
	# 			pass
	# 	return None

	# def get_response_header(self):
	# 	for responseReceived in self.driver.get_log('performance'):
	# 		try:
	# 			response = json.loads(responseReceived[u'message'])[u'message'][u'params'][u'response']
				
	# 			if response[u'url'] == self.driver.current_url:
	# 				return response[u'headers']
	# 		except:
	# 			pass
	# 	return None

	def get_response_infos(self):
		rsp = {
			'headers': None,
			'status': None
		}
		for responseReceived in self.driver.get_log('performance'):
			try:
				response = json.loads(responseReceived[u'message'])[u'message'][u'params'][u'response']
				
				if response[u'url'] == self.driver.current_url:
					rsp["headers"] = response[u'headers'] 
					rsp['status'] = (response[u'status'], response[u'statusText'])
			except:
				pass
		return rsp

	def _get_log(self):
		

		last_timestamp = self.last_timestamp
		entries = self.driver.get_log("performance")
		filtered = []

		for entry in entries:
			# check the logged timestamp against the 
			# stored timestamp
			if entry["timestamp"] > self.last_timestamp:
				filtered.append(entry)

				# save the last timestamp only if newer 
				# in this set of logs
				if entry["timestamp"] > last_timestamp:
					last_timestamp = entry["timestamp"]

		# store the very last timestamp
		self.last_timestamp = last_timestamp

		return filtered

	def get_performance_logs(self):
		self.p_log = self.driver.get_log('performance')
		return self.p_log

	def get_new_performance_logs(self):
		self.p_new_log = self._get_log()
		return self.p_new_log

	

	def get_browser_logs(self):
		return self.driver.get_log('browser')

	def get_driver_logs(self):
		return self.driver.get_log('driver')

	def get_browser_severe_logs(self, level='SEVERE'):
		log_infos = self.get_browser_logs()
		# print(22222222, log_infos)
		f_level = 'level'
		f_msg = 'message'
		server_level_logs = []
		for plog in log_infos:
			# print(plog[f_level])
			if plog[f_level] == level:
				server_level_logs.append(plog[f_msg])

		return server_level_logs


	def get_requests_and_response_headers_by_url(self, request_url, level='INFO', key_name='url'):
		log_infos = self.p_log
		f_level = 'level'
		f_msg = 'message'
		f_network_response = 'Network.responseReceived'
		f_network_sent = '"Network.requestWillBeSent"'
		regex = get_regex_by_type('url', request_url)
		expect_url = '\"%s\":\"%s\"' % (key_name, request_url)

		responsestr = None
		requeststr = None


		for plog in log_infos:
			if plog[f_level] == level:
				msg = plog[f_msg]
				
				real_url = get_values_by_regex(msg, regex)
				if not real_url:
					continue
				if real_url[0] == expect_url and f_network_response in msg:
					responsestr = msg
				elif real_url[0] == expect_url and f_network_sent in msg:
					requeststr = msg
				# if (f_network_response in msg or f_network_sent in msg) and (request_url in msg):
				# 	return_logs.append(msg)

		return responsestr, requeststr





	def general_request_infos(self, request_str):
		if not request_str:
			raise Exception("param is empty")
		import json
		flag_str = 'Network.requestWillBeSent'
		try:
			jsondata = json.loads(request_str)
			msg = jsondata['message']
			params = msg['params']
			
			if flag_str in request_str:

				return params.get('request')

		except Exception as e:
			raise e

	def general_response_infos(self, response_str):
		if not response_str:
			raise Exception("param is empty")
		import json
		flag_str = 'Network.responseReceived'
		try:
			jsondata = json.loads(response_str)
			msg = jsondata['message']
			params = msg['params']
			
			if flag_str in response_str:

				return params.get('response')

		except Exception as e:
			raise e

	def get_requests_and_response_infos_by_url(self, request_url, level='INFO', key_name='url'):
		log_infos = self.p_log
		f_level = 'level'
		f_msg = 'message'
		f_network_response = 'Network.responseReceived'
		f_network_sent = '"Network.requestWillBeSent"'
		ret_rsp = None
		ret_rq = None
		
		for plog in log_infos:
			if plog[f_level] == level:
				msg = plog[f_msg]
				from pprint import pprint
				# pprint(msg)
				if f_network_response in msg:
					response_log_obj = self.general_response_infos(msg)
					
					if response_log_obj.get('url') == request_url:
						ret_rsp = response_log_obj
				elif f_network_sent in msg:
					request_log_obj = self.general_request_infos(msg)
					if request_log_obj.get('url') == request_url:
						ret_rq = request_log_obj
				# if (f_network_response in msg or f_network_sent in msg) and (request_url in msg):
				# 	return_logs.append(msg)

			if ret_rsp and ret_rq:
				break

		return ret_rsp, ret_rq

	def get_requests_and_response_all_infos_by_url(self, request_url, level='INFO', key_name='url'):
		log_infos = self.p_log
		f_level = 'level'
		f_msg = 'message'
		f_network_response = 'Network.responseReceived'
		f_network_sent = '"Network.requestWillBeSent"'
		ret_rsp = []
		ret_rq = []
		
		for plog in log_infos:
			if plog[f_level] == level:
				msg = plog[f_msg]

				if f_network_response in msg:
					response_log_obj = self.general_response_infos(msg)
					if request_url in response_log_obj.get('url') :
						ret_rsp.append(response_log_obj)
				elif f_network_sent in msg:
					request_log_obj = self.general_request_infos(msg)
					if request_url in request_log_obj.get('url'):
						ret_rq.append(request_log_obj)
				# if (f_network_response in msg or f_network_sent in msg) and (request_url in msg):
				# 	return_logs.append(msg)

		return ret_rsp, ret_rq

	def get_new_requests_and_response_infos_by_url(self, request_url, level='INFO', key_name='url'):
		from pprint import pprint
		log_infos = self.p_new_log
		f_level = 'level'
		f_msg = 'message'
		f_network_response = 'Network.responseReceived'
		f_network_sent = '"Network.requestWillBeSent"'
		ret_rsp = None
		ret_rq = None
		
		for plog in log_infos:
			if plog[f_level] == level:
				msg = plog[f_msg]

				if f_network_response in msg:
					response_log_obj = self.general_response_infos(msg)
					if request_url in response_log_obj.get('url'):
						pprint(msg)
					if response_log_obj.get('url') == request_url:
						ret_rsp = response_log_obj
				elif f_network_sent in msg:
					request_log_obj = self.general_request_infos(msg)
					if request_url in request_log_obj.get('url'):
						pprint(msg)
					if request_log_obj.get('url') == request_url:
						ret_rq = request_log_obj
				# if (f_network_response in msg or f_network_sent in msg) and (request_url in msg):
				# 	return_logs.append(msg)

			if ret_rsp and ret_rq:
				break

		return ret_rsp, ret_rq


	def general_request_and_response_infos(self, response_log_obj, request_log_obj):

		if not response_log_obj or not request_log_obj:
			raise Exception("param is empty")
		flag = '----' * 20

		infos = """
General:
	Request URL: %s
	Request Method: %s
	Status Code: %s %s
	Remote Address: %s:%s
	Referrer Policy: %s
%s
Response Headers:
	%s
%s
Request Headers:
	%s
%s
Form Data:
	%s

""" %	(
			request_log_obj.get('url'),
			request_log_obj.get('method'),
			response_log_obj.get('status'), response_log_obj.get('statusText'),
			response_log_obj.get('remoteIPAddress'), response_log_obj.get('remotePort'),
			request_log_obj.get('referrerPolicy'),
			flag,
			response_log_obj.get('headers'),
			flag,
			request_log_obj.get('headers'),
			flag,
			request_log_obj.get('postData')
		)
		print(infos)

	def get_response_status(self, responses):
		if not responses:
			raise Exception("param is empty")

		return responses.get('status') 

	
	def get_driver_logs(self, level='SEVERE'):
		log_infos = self.driver.get_log('driver')
		f_level = 'level'
		f_msg = 'message'
		server_level_logs = []
		for plog in log_infos:
			if plog[f_level] == level:
				server_level_logs.append(plog[f_msg])

		return server_level_logs









