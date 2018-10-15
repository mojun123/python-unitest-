from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import os
import sys
BASEDIR = os.path.dirname(os.getcwd())
sys.path.append(BASEDIR)
import time
from utils.driver_env import *
from utils import file_handle as fhd
from utils._regex import *

from page.chrome_driver import ChromeDriver as cdriver

class Tdddd(unittest.TestCase):
	"""docstring for Tdddd"""
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def test_data(self):
		assert 1 != 1
		

class new_test(unittest.TestCase):
	"""docstring for new_test"""
	def setUp(self):
		


		print(self.__class__.__name__)
		pass
		# url = 'https://selenium-python.readthedocs.io/waits.html#explicit-waits'
		# url = 'https://m.clatterans.com/online-whirlpool-refrigerator-water-filter-3-edr3rxd1-4396710-4396841-kenmore-9030-water-filter-3-pack-4.html'
		# url = 'https://qa.clatterans.com/'
		# url = 'https://qa.clatterans.com/text'
		# url = 'https://m.clatterans.com'

		# self.chrome_obj = cdriver()
		# self.chrome_obj.init_base_infos(url)
		# self.chrome_obj.set_proxy('socks5://192.168.10.20:1081')
		# self.chrome_obj.disable_img()

		# log_conf = os.path.join(BASEDIR,'conf','log.conf')
		# self.chrome_obj.init_driver('all_logs', log_conf)


	def test_new(self):
		d_obj = Tdddd()
		d_obj.test_data()
		self.assertIs('ddf','ddf')
		# self.chrome_obj.open()
		# host = self.chrome_obj.host
		# print(host)
		# self.chrome_obj.check_browser_error_by_host(host)
		# self.chrome_obj.check_browser_error_by_current_url()
		# from pprint import pprint
		# element = self.chrome_obj.find_element_by_class_name('act_user')
		# self.chrome_obj.assertIsNone(element)
		# aside_1 = self.chrome_obj.get_element_child_by_tag_name('div', driver=element)
		# pprint(self.chrome_obj.get_innerHTML(aside_1))
		# aside_2 = self.chrome_obj.get_element_child_by_tag_name('div', index=1, driver=element)
		# pprint(self.chrome_obj.get_outerHTML(aside_1))
		# self.chrome_obj.driver.quit()

	def tearDown(self):
		# self.chrome_obj.driver.quit()
		pass
# if __name__ == '__main__':
# 	unittest.main()
# print(dir(unittest.TestCase))
# print(dir(unittest))
# assert type('dd') is str
# try:
# 	browser_log = chrome_obj.driver.get_log('browser')
# 	print(type(browser_log))
# 	fhd.pretty_write(browser_log, "./browser.log")
# except Exception as e:
# 	print("browser_log: ", 111111111111111)
# 	print(str(e))
# 	print(222222222222222)

# try:
# 	performance_log = chrome_obj.driver.get_log('performance')
# 	print(type(performance_log))
# 	fhd.pretty_write(performance_log, "./performance.log")
# except Exception as e:
# 	print("performance_log: ", 111111111111111)
# 	print(str(e))
# 	print(222222222222222)

# try:
# 	driver_log = chrome_obj.driver.get_log('driver')
# 	print(type(driver_log))
# 	fhd.pretty_write(driver_log, "./driver.log")
# except Exception as e:
# 	print("driver_log: ", 111111111111111)
# 	print(str(e))
# 	print(222222222222222)

# try:
# 	server_log = chrome_obj.driver.get_log('server')
# 	print(type(server_log))
# 	fhd.pretty_write(server_log, "./server.log")
# except Exception as e:
# 	print("server_log: ", 111111111111111)
# 	print(str(e))
# 	print(222222222222222)

# element = chrome_obj.driver.find_element_by_id('new-price')
# # element = chrome_obj.driver.find_element_by_class_name('nf-bs-box')
# element.click()
# from pprint import pprint
# pprint(chrome_obj.driver.get_log('browser'))
# print(chrome_obj.driver.log_types)
# # pprint(dir(chrome_obj.driver))

# chrome_obj.driver.close()
# print(type('jdh') is str)
# from utils.commons import importModule
# import os
# BASEDIR = os.path.dirname(os.getcwd())
# file = os.path.join('..', 'tmp', 'product_infos', 'infos.py')
# print(importModule(file, 'products'))

def main():
	import argparse
	parser = argparse.ArgumentParser(description='nighslee testcase params.',
	        epilog='Have a nice day!')

	parser.add_argument('-retry', '--retry', type=str, default='2', help='retry numbers if test failed')

	args = parser.parse_args()

	return args.retry

	# pname = parser.parse_args(['-pname'])

if __name__ == '__main__':
	print(main())


		