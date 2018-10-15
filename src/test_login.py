
import unittest
import os
import time
from utils import file_handle as fhd

from utils import commons as chd
from testcase.Login import Login
from pprint import pprint
from conf import common_file_setting as cfs


BASEDIR = os.path.dirname(os.getcwd())


class LoginTestSuits(unittest.TestCase):


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

	
	@classmethod
	def setUpClass(cls):
		cls.url = "https://www.nighslee.com"
		cls.login_page = Login()
		# cls.login_page.headless = False
		# cls.login_page.start_maximized = True
		cls.login_page.init_class_name(cls.__name__)
		cls.login_page.set_chrome_options()

		proxy_json_file = os.path.join(BASEDIR,'conf', 'proxy.json')
		proxy = chd.random_proxy_from_file(proxy_json_file)
		cls.login_page.add_proxy(proxy)
		# cls.home_page_obj.add_proxy('socks5://192.168.10.20:1081')

		log_conf = os.path.join(BASEDIR,'conf','log.conf')
		cls.login_page.init_driver('all_logs', log_conf)
		cls.start_time = time.time()
		
	def login_home(self, url=''):
		self.test_case_name = self._testMethodName
		self.login_page.init_case_name(self.test_case_name)
		url = url or (self.url + '/login')
		self.login_page.init_base_infos(url)
		self.login_page.open(url)
		from testcase.common_page import CommonPage
		self.c_page = CommonPage(self.login_page)
		self.c_page.close_popup()

	def click_element(self, element, expected_str, page_obj):
		
		element.click()
		page_obj.assertIn(expected_str, page_obj.driver.current_url)

	def test_facebook(self):
		self.login_page.check_browser_error_by_current_url()
		self.login_home()
		
		e_facebook, _ = self.login_page.get_facebook_login_element()
		expected_url = "facebook"
		self.click_element(e_facebook, expected_url, self.login_page)

	def test_twitter(self):
		self.login_page.check_browser_error_by_current_url()
		self.login_home()
		
		e_twitter, _ = self.login_page.get_twitter_login_element()
		expected_url = "twitter"
		self.click_element(e_twitter, expected_url, self.login_page)

	def test_google(self):
		self.login_page.check_browser_error_by_current_url()
		self.login_home()
		
		e_google, _ = self.login_page.get_google_login_element()
		expected_url = "google"
		self.click_element(e_google, expected_url, self.login_page)

	def test_login_form_init_status(self):
		self.login_page.check_browser_error_by_current_url()
		self.login_home()
		
		self.login_page.check_init_login_form_error()
		self.login_page.check_remember_init_status()
		self.login_page.check_login_btn_init_status()

	def test_regist(self):
		self.login_page.check_browser_error_by_current_url()
		self.login_home()
		
		e_regist = self.login_page.get_register_element()
		expected_url = self.url + '/register'
		self.click_element(e_regist, expected_url, self.login_page)

	def test_reset(self):
		self.login_page.check_browser_error_by_current_url()
		self.login_home()
		
		e_reset = self.login_page.get_reset_element()
		expected_url = self.url + '/password/reset'
		self.click_element(e_reset, expected_url, self.login_page)

	@classmethod
	def tearDownClass(cls):
		# self.login_page.driver.close()
		run_time = time.time() - cls.start_time
		print("%s: %.3f" % (cls.__name__, run_time))
		cls.login_page.driver.quit()


def main():
	from utils import case_suits

	test_suits = case_suits.CaseSuits()
	test_suits.add_login_suit('test_facebook')
	test_suits.add_login_suit('test_twitter')
	test_suits.add_login_suit('test_google')
	test_suits.add_login_suit('test_login_form_init_status')
	test_suits.add_login_suit('test_regist')
	test_suits.add_login_suit('test_reset')
	
	file_name = 'test_login_result_'

	from utils import report_to_wechat as rtw
	result = rtw.run_suites(file_name, test_suits.suits)
	rtw.report(result)

if __name__ == "__main__":
	main()
