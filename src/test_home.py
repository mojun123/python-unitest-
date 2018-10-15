
import unittest
import os
import time

from utils import commons as chd
from testcase.HomePage import Home
from pprint import pprint
#import line_profiler
# if 'profile' not in dir():
# 	def profile(func):
# 		def inner(*args, **kwargs):
# 			return func(*args, **kwargs)
# 		return inner



BASEDIR = os.path.dirname(os.getcwd())
# sys.path.append(BASEDIR)

class HomeTestSuits(unittest.TestCase):


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

		cls.url = "https://www.nighslee.com/"
		cls.home_page_obj = Home()
		# cls.home_page_obj.headless = False
		# cls.home_page_obj.disable_imges = True
		# cls.home_page_obj.start_maximized = True
		cls.home_page_obj.set_chrome_options()
		
		proxy_json_file = os.path.join(BASEDIR,'conf', 'proxy.json')
		proxy = chd.random_proxy_from_file(proxy_json_file)
		cls.home_page_obj.add_proxy(proxy)
		# cls.home_page_obj.add_proxy('socks5://192.168.10.20:1081')
		cls.home_page_obj.init_class_name(cls.__name__)
		
		log_conf = os.path.join(BASEDIR,'conf','log.conf')
		cls.home_page_obj.init_driver('all_logs', log_conf)
		cls.start_time = time.time()

	def home_page(self, url=''):
		url = url or self.url
		self.test_case_name = self._testMethodName
		self.home_page_obj.init_case_name(self.test_case_name)
		title = "Best Memory Foam Mattress & Pillow For Sale Under $500 | Nighslee" 
		self.home_page_obj.init_base_infos(url)
		self.home_page_obj.open(url)
		from testcase.common_page import CommonPage
		self.c_page = CommonPage(self.home_page_obj)
		self.c_page.close_popup()

	def check_home_menu(self, menu_name, reverse=True):
		self.home_page()
		element, e_menu = self.home_page_obj._dispatch(menu_name, reverse)
		try:
			element.click()
			msg = "click {0} cannot jump to {0} page. current_url: ".format(menu_name) + self.home_page_obj.driver.current_url
			if "home" not in menu_name:
				assert menu_name in self.home_page_obj.driver.current_url, msg
				reverse = not reverse
			else:
				reverse = False
			element, _ = self.home_page_obj._dispatch(menu_name, reverse)
			return self.home_page_obj
		except Exception as e:
			print("check_home_menu except: ", self.home_page_obj.get_innerHTML(e_menu))
			self.home_page_obj.check_browser_error_by_current_url()
			nowTime = time.strftime("%Y%m%d.%H.%M.%S")
			file_name = os.path.join('..', 'screenshot', self.__class__.__name__, self.test_case_name, 'cannot-click-%s-%s.png' % (menu_name, nowTime))
			self.home_page_obj.save_png(file_name)
			print("[error] cannot click " + menu_name)
			raise e

	# @profile
	def test_home(self):
		menu_name = "home"
		reverse = False
		self.home_page_obj = self.check_home_menu(menu_name, reverse)
		self.home_page_obj.check_all_menu(menu_name)

	# @profile
	def test_home_mattress(self):
		menu_name = "mattress"
		reverse = True
		self.home_page_obj = self.check_home_menu(menu_name, reverse)
		self.home_page_obj.check_all_menu(menu_name)

	# @profile
	def test_home_reviews(self):
		menu_name = "reviews"
		reverse = True
		self.home_page_obj = self.check_home_menu(menu_name, reverse)
		self.home_page_obj.check_all_menu(menu_name)

	# @profile
	def test_home_faqs(self):
		menu_name = "faqs"
		reverse = True
		self.home_page_obj = self.check_home_menu(menu_name, reverse)
		self.home_page_obj.check_all_menu(menu_name)

	# @profile
	def test_home_contact(self):
		menu_name = "contact"
		reverse = True
		self.home_page_obj = self.check_home_menu(menu_name, reverse)
		self.home_page_obj.check_all_menu(menu_name)

	@classmethod
	def tearDownClass(cls):
		run_time = time.time() - cls.start_time
		print("%s: %.3f" % (cls.__name__, run_time))
		cls.home_page_obj.driver.quit()

def main():
	from utils import case_suits

	test_suits = case_suits.CaseSuits()
	test_suits.add_home_suit('test_home')
	test_suits.add_home_suit(('test_home_mattress'))
	test_suits.add_home_suit(('test_home_reviews'))
	test_suits.add_home_suit(('test_home_faqs'))
	test_suits.add_home_suit(('test_home_contact'))
	
	file_name = "test_home_result_"

	from utils import report_to_wechat as rtw
	result = rtw.run_suites(file_name, test_suits.suits)
	rtw.report(result)

if __name__ == "__main__":
	main()