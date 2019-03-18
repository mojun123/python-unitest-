
import unittest
import os
import time

from src.utils import commons as chd
from src.testcase.page_asserts import home_page_asserts as hpa
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

		cls.url = "https://www.genkifitness.com/"
		cls.home_page_obj = hpa.HomeAsserts()
		cls.home_page_obj.headless = False

		cls.home_page_obj.start_maximized = True
		cls.home_page_obj.set_chrome_options()
		
		proxy_json_file = os.path.join(BASEDIR,'conf', 'proxy.json')
		# proxy = chd.random_proxy_from_file(proxy_json_file)
		# cls.home_page_obj.add_proxy(proxy)
		#cls.home_page_obj.add_proxy('socks5://192.168.10.20:1081')
		cls.home_page_obj.init_class_name(cls.__name__)
		
		log_conf = os.path.join(BASEDIR,'conf','log.conf')
		cls.home_page_obj.init_driver('all_logs', log_conf)
		cls.start_time = time.time()

	def home_page(self, url='', b_refresh=True):
		url = url or self.url
		title = 'Genkifitness.com'
		if not b_refresh:
			self.test_case_name = self._testMethodName
			self.home_page_obj.init_case_name(self.test_case_name)
			self.home_page_obj.init_base_infos(url, title)
		self.home_page_obj.open(url)


	def test_welcome_without_login(self):
		self.home_page(False)
		self.home_page_obj.check_tvc_welcome()

	def test_init_login_popup(self):
		self.home_page()
		self.home_page_obj.check_login_popup_status()

	def test_active_login_popup(self):
		self.home_page()
		e_sign_in_or_register = self.home_page_obj.get_tvc_account_sign_in_or_register()
		e_sign_in_or_register.click()
		self.home_page_obj.check_login_popup_status(True)

	def test_my_account_href_without_login(self):
		self.home_page()
		element = self.home_page_obj.get_tvc_account_my_account()
		expected_text = self.url + 'login?r=/myaccount'
		self.home_page_obj.check_url_after_click_href(expected_text, element)

	def test_view_cart_href(self):
		self.home_page()
		element = self.home_page_obj.get_tvc_view_cart_btn()
		expected_text = self.url + 'viewcart'
		self.home_page_obj.check_url_after_click_href(expected_text, element)

	def test_best_sellers_href(self):
		self.home_page()
		element = self.home_page_obj.get_menu_best_sellers()
		expected_text = self.url + 'bestseller'
		self.home_page_obj.check_url_after_click_href(expected_text, element)

	def test_track_my_order_href(self):
		self.home_page()
		element = self.home_page_obj.get_menu_track_order()
		expected_text = self.url + 'trackorder'
		self.home_page_obj.check_url_after_click_href(expected_text, element)

	def test_help_href(self):
		self.home_page()
		element = self.home_page_obj.get_menu_help()
		expected_text = self.url + 'article/faq'
		self.home_page_obj.check_url_after_click_href(expected_text, element)

	def test_product_list_qty(self):
		self.home_page()
		_, list_skus = self.home_page_obj.get_pl_len_sku()
		expected_qty = 8
		self.home_page_obj.assertEqual(expected_qty, len(list_skus))

	def test_first_sku_infos(self):
		self.home_page()
		 
		e_title = self.home_page_obj.get_pl_first_list_box_href()
		e_title_text = e_title.text
		e_title_text = e_title_text.replace('\"', '')
		import re
		e_title_text = re.sub(r'\s+', ' ', e_title_text)
		e_price = self.home_page_obj.get_pl_first_list_box_price()
		e_price_text = e_price.text

		sku_info_file = os.path.join(BASEDIR, 'conf', 'expected_infos', 'home_page_list_sku_infos.conf')

		from src.utils.read_confs import ReadConf
		config_parser = ReadConf(sku_info_file)
		section = 'first_sku_infos'
		expected_title = config_parser.get_value_by_key('title', section)
		expected_title = re.sub(r'\s+', ' ', expected_title)
		expected_price = config_parser.get_value_by_key('price', section)
		expected_url = config_parser.get_value_by_key('url', section)

		self.home_page_obj.assertIn(expected_title, e_title_text)
		self.home_page_obj.assertIn(expected_price, e_price_text)

		self.home_page_obj.scroll_to_element(e_title)
		self.home_page_obj.assertIn(expected_url, self.home_page_obj.driver.current_url)

	def test_about_us(self):
		self.home_page()
		element = self.home_page_obj.get_ft_cp_about_us()
		expected_text = self.url + 'article/about'
		self.home_page_obj.check_url_after_click_href(expected_text, element)
	
	def test_terms(self):
		self.home_page()
		element = self.home_page_obj.get_ft_terms()
		expected_text = self.url + 'article/terms'
		self.home_page_obj.check_url_after_click_href(expected_text, element)
	
	def test_privacy(self):
		self.home_page()
		element = self.home_page_obj.get_ft_privacy()
		expected_text = self.url + 'article/privacy'
		self.home_page_obj.check_url_after_click_href(expected_text, element)
	
	def test_warranty(self):
		self.home_page()
		element = self.home_page_obj.get_ft_warranty()
		expected_text = self.url + 'article/warranty'
		self.home_page_obj.check_url_after_click_href(expected_text, element)
	
	def test_sit_map(self):
		self.home_page()
		element = self.home_page_obj.get_ft_sit_map()
		expected_text = self.url + 'sitemap'
		self.home_page_obj.check_url_after_click_href(expected_text, element)

	def test_contact_us(self):
		self.home_page()
		element = self.home_page_obj.get_ft_cs_contact_us()
		expected_text = self.url + 'contactus'
		self.home_page_obj.check_url_after_click_href(expected_text, element)
	
	def test_ft_my_account_without_login(self):
		self.home_page()
		element = self.home_page_obj.get_ft_cs_my_account()
		expected_text = self.url + 'login?r=/myaccount'
		self.home_page_obj.check_url_after_click_href(expected_text, element)
	
	def test_faq(self):
		self.home_page()
		element = self.home_page_obj.get_ft_cs_faq()
		expected_text = self.url + 'article/faq'
		self.home_page_obj.check_url_after_click_href(expected_text, element)

	def test_shipping_guide(self):
		self.home_page()
		element = self.home_page_obj.get_ft_sr_shipping_guide()
		expected_text = self.url + 'article/shipping'
		self.home_page_obj.check_url_after_click_href(expected_text, element)
	
	def test_return_policy(self):
		self.home_page()
		element = self.home_page_obj.get_ft_sr_return_policy()
		expected_text = self.url + 'article/return'
		self.home_page_obj.check_url_after_click_href(expected_text, element)
	
	def test_ft_track_my_order(self):
		self.home_page()
		element = self.home_page_obj.get_ft_sr_track_my_order()
		expected_text = self.url + 'trackorder'
		self.home_page_obj.check_url_after_click_href(expected_text, element)

	def test_welcome_with_login(self):
		expected_text = 'yang'
		self.check_tvc_welcome(expected_text)

	@classmethod
	def tearDownClass(cls):
		run_time = time.time() - cls.start_time
		print("%s: %.3f" % (cls.__name__, run_time))
		cls.home_page_obj.driver.quit()

def main():
	from src.utils import case_suits

	test_suits = case_suits.CaseSuits()
	test_suits.add_home_suit('test_welcome_without_login')
	test_suits.add_home_suit('test_init_login_popup')
	test_suits.add_home_suit('test_active_login_popup')
	test_suits.add_home_suit('test_my_account_href_without_login')
	test_suits.add_home_suit('test_view_cart_href')
	# test_suits.add_home_suit('test_best_sellers_href')
	# test_suits.add_home_suit('test_track_my_order_href')
	# test_suits.add_home_suit('test_help_href')
	# test_suits.add_home_suit('test_product_list_qty')
	# test_suits.add_home_suit('test_first_sku_infos')
	# test_suits.add_home_suit('test_about_us')
	# test_suits.add_home_suit('test_terms')
	# test_suits.add_home_suit('test_privacy')
	# test_suits.add_home_suit('test_warranty')
	# test_suits.add_home_suit('test_sit_map')
	# test_suits.add_home_suit('test_contact_us')
	# test_suits.add_home_suit('test_ft_my_account_without_login')
	# test_suits.add_home_suit('test_faq')
	# test_suits.add_home_suit('test_shipping_guide')
	# test_suits.add_home_suit('test_return_policy')
	# test_suits.add_home_suit('test_ft_track_my_order')

	
	file_name = "test_home_result_"

	from src.utils import report_to_wechat as rtw
	retry_number = 0
	result = rtw.run_suites(file_name, test_suits.suits, retry_number)
	from src.utils.sendemail import send_email
	from src.utils.sendemail import new_file
	test_report = r'C:\Users\F993\Documents\Tencent Files\1696384748\FileRecv\genkifitness_pc_selenium_testing\genkifitness_pc_selenium_testing\result'
	test = new_file(test_report)
	send_email(test)

if __name__ == "__main__":
	main()