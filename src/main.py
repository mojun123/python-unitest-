from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import os
import time
from utils.driver_env import *
from utils.file_handle import *
from utils.user_infos import Users
from utils.commons import *
from testcase.HomePage import Home

from pprint import pprint
from proxy.requestsproxy import RandomProxy

CURRENT_DIR = os.getcwd()
BASE_DIR = os.path.dirname(CURRENT_DIR)

G_CONTINUE_TEST = None

G_COOKIE_FILE = {
	'login': os.path.join('..', 'tmp', 'cookies', 'login_cookies.log'),
	'addtocart': os.path.join('..', 'tmp', 'cookies', 'addtocart_cookies.log'),
	'viewcart': os.path.join('..', 'tmp', 'cookies', 'viewcart_cookies.log'),
	'checkout': os.path.join('..', 'tmp', 'cookies', 'checkout_cookies.log'),

}

G_SHOP = {
	'e_product_detail_add_to_cart': "element obj",
	'product_unit_price': "0",
	'url_after_viewcart': "",
	'url_after_click_checkout': "",
	'credit_card_checkout_url': "",
	'orderid': 0
}

G_PAYMENT_PAGE_OBJECT = None


class CaseHome(unittest.TestCase):


	def set_proxies_disable(self, host=None):
		'''
		session = requests.Session()
		session.trust_env = False
		os.environ['NO_PROXY'] = 'stackoverflow.com'
		response = requests.get('http://www.stackoverflow.com')
		'''
		import os
		host = host or self.host
		os.environ['NO_PROXY'] = host

	def check_response_status(self, page_obj, url, status=200):
		# page_obj.get_performance_logs()
		import json
		rsp_obj, rq_obj = page_obj.get_requests_and_response_infos_by_url(url)
		if not rsp_obj:
			pprint(page_obj.p_log)
			nowTime = time.strftime("%Y%m%d.%H.%M.%S")
			file_name = os.path.join('..', 'screenshot', 'others', 'no_response_%s.png' % nowTime)
			page_obj.save_png(file_name)
			raise Exception("cannot get request url's response")

		# page_obj.get_new_requests_and_response_infos_by_url(self.host)
		real_status = page_obj.get_response_status(rsp_obj)
		if real_status != status:
			# pprint(page_obj.p_log)
			#show general response infos
			page_obj.general_request_and_response_infos(rsp_obj, rq_obj)
			raise Exception("expected_status: %s, real_status: %s" % (status, real_status))
		# assert real_status == status

	def check_response_infos(self, page_obj, url):
		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		file_name = os.path.join('..', 'screenshot', 'others', 'all_response_%s.png' % nowTime)
		page_obj.save_png(file_name)
		# page_obj.get_performance_logs()
		rsp_obj, rq_obj = page_obj.get_requests_and_response_all_infos_by_url(url)
		if rsp_obj and rq_obj:
			#todo rsp_obj and rq_obj is list in here
			pass
			# page_obj.general_request_and_response_infos(rsp_obj, rq_obj)
		else:
			print('url: ', url)
			pprint(rsp_obj)
			pprint(rq_obj)
			raise Exception("some thing bad")

	def check_js_error(self, page_obj, url):
		import json
		browser_logs = page_obj.get_browser_severe_logs()
		browser_logs = json.dumps(browser_logs, indent=4)
		flag = '----' *20
		msg = """
Got some js error, logs as follow:
%s
%s
%s
""" % (flag, browser_logs, flag)
		assert url not in browser_logs, msg

	def check_proxy(self):

		file = os.path.join(BASE_DIR,'conf', 'proxy.json')
		_obj = RandomProxy()
		_obj.loads_proxy_from_file(file)
		proxys = _obj.check_proxy()
		self.proxy = _obj.get_proxy_str_from_dict(proxys)

		

	def setUp(self):
		
		self.url = "https://www.clatterans.com/"
		self.host = "www.clatterans.com"
		self.title = ""
		self.set_proxies_disable(self.host)
		self.check_proxy()
		msg = "Have no working proxy"
		self.assertIsNotNone(self.proxy, msg)
		self.chromedriver = set_driver_path()
		os.environ["webdriver.chrome.driver"] = self.chromedriver
		chromeOptions = webdriver.ChromeOptions()
		chromeOptions.add_argument('--proxy-server=%s' % self.proxy)
		chromeOptions.add_argument("--headless") # Runs Chrome in headless mode.
		chromeOptions.add_argument('--no-sandbox') # Bypass OS security model
		platform = get_platform()
		if 0 == platform:
			chromeOptions.add_argument('--disable-gpu')  # applicable to windows os only
		# chromeOptions.add_argument('--start-maximized') # 
		chromeOptions.add_argument('--disable-infobars')
		chromeOptions.add_argument("--disable-extensions")  

		capabilities = webdriver.DesiredCapabilities.CHROME
		capabilities['loggingPrefs'] = { 
			'browser': 'ALL',
			'driver': 'ALL',
			'performance': 'ALL'
		}
		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		self.test_case_name = self._testMethodName
		_log_path = os.path.join("..", "log", "chromedriver_%s_%s.log" % (self.test_case_name, nowTime))
		mkdir_if_not_existed(_log_path)
		log_path = '--log-path=' + _log_path
		log_type = '--verbose'

		self.driver = webdriver.Chrome(
			self.chromedriver, 
			chrome_options=chromeOptions, 
			desired_capabilities=capabilities,
			service_args=[log_type, log_path]
			)
		self.start_time = time.time()
		# self.driver.set_window_size(1336, 768)
		self.driver.set_window_size(1920, 1080)
		# self.driver.maximize_window();

	def home_page(self):

		title = "Refrigerator Water Filters, Water Filter Online | Clatterans.com" 
		home_page = Home(self.driver, self.url, title)
		return home_page

	def test_home_page(self):
		home_page = self.home_page()
		b_open = home_page.open()
		time.sleep(1)
		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		file_name = os.path.join('..', 'screenshot', '%s' % self.test_case_name, 'open_home_%s.png' % nowTime)
		home_page.save_png(file_name)
		home_page.get_performance_logs()
		self.check_js_error(home_page, self.url)
		self.check_response_status(home_page, self.url, 200)
		title = self.driver.title
		home_page.assert_element_attribute(title, home_page.page_title)
		element_slides = home_page.check_slider()
		home_page.assertNotNone_element_attribute(element_slides)
		element_signin = home_page.check_sign()
		home_page.assertNotNone_element_attribute(element_signin)
		element_viewcart = home_page.check_viewcart_button()
		home_page.assertNotNone_element_attribute(element_viewcart)
		element_chat_now = home_page.check_chat_now_button()
		home_page.assertNotNone_element_attribute(element_chat_now)
		element_product_list = home_page.check_products()
		home_page.assertNotNone_element_attribute(element_product_list)


	def tearDown(self):
		# self.driver.close()
		run_time = time.time() - self.start_time
		print("%s: %.3f" % (self.test_case_name, run_time))
		self.driver.quit()

def run(file_name):
	# from libs.HTMLTestRunner import HTMLTestRunner
	from libs.retry_HTMLTestRunner import HTMLTestRunner
	import datetime
	import time
	import codecs
   
	todayDate = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
	fname = file_name + todayDate + ".html"
	result_file = os.path.join('..', 'result', fname)
	mkdir_if_not_existed(result_file)
	fp = codecs.open(result_file,"wb",'utf-8')	
	runner = HTMLTestRunner(
			stream=fp,
			title='clatterans shopping main flow',
			description='\
				Included login -> \
				add-sku-to-cart -> \
				checkout -> \
				order-confirm -> \
				select-payment-method -> \
				payment-page',
			retry_total_numbers=2
			)

	suite = unittest.TestSuite()
	# suite.addTest(unittest.makeSuite(CaseHome))
	suite.addTest(CaseHome('test_home_page'))

	print("start : %s" % time.ctime())
	run_result=runner.run(suite)
	fp.close()
	print("End : %s" % time.ctime())
	return run_result



if __name__ == "__main__":
	file_name = "shopping_"
	cookies_path = os.path.join('..',"tmp", "cookies")

	empty_files_in_dir(cookies_path)
	# if test_porxy():

	# 	result = run(file_name)
	# 	report(result)
	result = run(file_name)

