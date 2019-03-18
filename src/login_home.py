
import unittest
import os
import time

from src.utils import commons as chd
from src.testcase.page_asserts import login_page_asserts as home
from pprint import pprint









DASEDIR = os.path.dirname(os.getcwd())
#sys.path.append(BASEDIR)

class LoginTestsuits(unittest.TestCase):


	def set_proxies_disable(self, host=None):
	   '''

	   session = requests.Session()
	   session.trust_env = False
	   os.environ['NO_PROXY'] = 'stackoverflow.com'
	   response = requests.get('https://www.stackoverflow.com')
	   '''

	   import os
	   host = host or self.host
	   os.environ['NO_PROXY'] = host

	@classmethod
	def setUpClass(cls):

		cls.url = 'https://www.genkifitness.com/'
		cls.login_page_obj = home.LoginAsserts()
		cls.login_page_obj.headless = False
		cls.login_page_obj.start_maximized = True 
		cls.login_page_obj.set_chrome_options()
		proxy_json_file = os.path.join(DASEDIR,'conf', 'proxy.json')
		# proxy = chd.random_proxy_from_file(proxy_json_file)
		# cls.login_page_obj.add_proxy(proxy)
		#cls.login_page_obj.add_proxy('socks5://192.168.10.20:1081')
		cls.login_page_obj.init_class_name(cls.__name__)

		log_conf = os.path.join(BASEDIR,'conf','log.conf')
		cls.login_page_obj.init_driver('all_logs', log_conf)
		cls.start_time = time.time()

	def login_page(self, url='', b_refersh=True):
		url = url or self.url
		title = 'Genkifitness.com'
		if not b_refersh:
			self.test_case_name = self._testMethodName
			self.login_page_obj.init_case_name(self.test_case_name)
			self.login_page_obj.init_base_infos(url, title)
		self.login_page_obj.open(url)

	def test_learn_more(self):
		self.login_page()
		expected_text = self.login_page_obj.get_login_learn()
		element = self.url + 'article/faqdetails/7'
		self.login_page_obj.check_url_after_click_href(expected_text, element)

	def test_email_address(self):
		self.login_page()


        

        




























































	@classmethod
	def tearDownClass(cls):
		run_time = time.time() - cls.start_time
		print('%s: %.3f' % (cls.__name__,run_time))

def main():
	from src.utils import case_suits
	test_suits = case_suits.Casesuits()
	test_suits.add_home_suit('')






















	file_name = 'login_home_result_'
	from untils import report_to_wechat as rts 
	retry_number = 0
	result = rtw.run_suites(file_name, test_suits.suits, retry_number)

if __name__ == '__mian__':
	main()