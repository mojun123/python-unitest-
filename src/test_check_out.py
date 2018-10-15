import unittest
import os
import time
from utils import file_handle as fhd
from utils import commons as chd
from testcase.CheckOut import CheckOut
from pprint import pprint
from conf import common_file_setting as cfs

BASEDIR = os.path.dirname(os.getcwd())

class CheckOutTestSuits(unittest.TestCase):

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

		cls.check_out_page = CheckOut()
		cls.check_out_page.init_class_name(cls.__name__)

		# cls.check_out_page.headless = False
		# cls.check_out_page.start_maximized = True
		# cls.check_out_page.random_user_agents()
		cls.check_out_page.set_chrome_options()
		
		proxy_json_file = os.path.join(BASEDIR,'conf', 'proxy.json')
		proxy = chd.random_proxy_from_file(proxy_json_file)
		cls.check_out_page.add_proxy(proxy)
		# cls.check_out_page.add_proxy('socks5://192.168.10.20:1081')

		log_conf = os.path.join(BASEDIR,'conf','log.conf')
		cls.check_out_page.init_driver('all_logs', log_conf)
		
		cls.start_time = time.time()

	def checkout_home(self, url='', b_reset=False):
		self.check_out_page.init_case_name(self._testMethodName)
		url = url or self.url 
		self.check_out_page.init_base_infos(url)
		
		self.check_out_page.open(url)
		from testcase.common_page import CommonPage
		self.c_page = CommonPage(self.check_out_page)
		self.c_page.close_popup()

		if b_reset:
			self.check_out_page.scroll_to_offset(0)

	# def to_login(self):
		
	# 	email, pwd = chd.get_login_infos(BASEDIR)
	# 	self.check_out_page.assertIsNotNone(email)
	# 	self.check_out_page.assertIsNotNone(pwd)
	# 	e_login = self.c_page.login(email, pwd)
	# 	e_login.click()

	# def to_add_cart(self):
		
	# 	#add cart
	# 	element, _ = self.c_page.get_header_add_to_cart_btn()
	# 	self.check_out_page.assertIsNotNone(element)
	# 	self.check_out_page.scroll_to_element(element)
	# 	self.c_page.get_cart_list_child() # to check cart visibale

	# def to_click_checkout(self):

	# 	#click checkout
	# 	self.c_page.close_popup()
	# 	element = self.c_page.get_cart_check_out_btn()
	# 	print(self.check_out_page.get_outerHTML(element))
	# 	self.check_out_page.assertIsNotNone(element)
	# 	self.check_out_page.scroll_to_element(element)
	# 	self.check_out_page.assertIn('checkout', self.check_out_page.driver.current_url)

	def login_to_check_out(self, url=''):
		self.check_out_page.init_case_name(self._testMethodName)
		
		url = self.url + '/login'
		self.checkout_home(url)
		self.c_page.close_popup()
		b_login = self.c_page.check_username("young")
		if "login" in self.check_out_page.driver.current_url and not b_login:
			email, pwd = chd.get_login_infos(BASEDIR)
			self.c_page.shopping_flow_to_login(email, pwd)
			self.c_page.close_popup()

		#empty cart
		self.check_out_page.open(self.url)
		self.c_page.empty_cart()
		# self.check_out_page.refresh()
		self.c_page.check_cartApp_active()

		url = self.url + '/nighslee-10-inch-cool-gel-memory-foam-mattress-twin-size-222'
		self.check_out_page.open(url)
		self.c_page.close_popup()

		self.c_page.shopping_flow_to_add_cart()
		self.c_page.shopping_flow_to_click_checkout()

		self.check_out_page.check_page_loading_finished()

	def load_conf_info(self):

		info_file = cfs.INFOS_FILE['product_infos']
		from utils.commons import importModule
		self.product_list = importModule(info_file, 'products')
		self.shipping_infos = importModule(info_file, 'shipping_info')
		
		selected_file = cfs.INFOS_FILE['selected_product_size']
		select_product = fhd.file_content_to_py_object(selected_file)
		self.size = select_product['size']
		self.get_product_info()

	def test_shipping_address(self):
		self.login_to_check_out()
		self.load_conf_info()

		first_name = self.shipping_infos['first_name']
		self.check_out_page.assert_first_name(first_name)
		last_name = self.shipping_infos['last_name']
		self.check_out_page.assert_last_name(last_name)
		street = self.shipping_infos['street']
		self.check_out_page.assert_street(street)
		apartment_suite = self.shipping_infos['apartment_suite']
		self.check_out_page.assert_apartment_suite(apartment_suite)
		city = self.shipping_infos['city']
		self.check_out_page.assert_city(city)
		state = self.shipping_infos['state']
		self.check_out_page.assert_state(state)
		zip_code = self.shipping_infos['zip_code']
		self.check_out_page.assert_zip_code(zip_code)
		phone = self.shipping_infos['phone']
		self.check_out_page.assert_phone(phone)

	def get_product_info(self):
		for product in self.product_list:
			if product.get('size') == self.size:
				self.product = product
				break
	
	def test_summary_infos(self):

		self.login_to_check_out()
		self.load_conf_info()
		self.check_out_page.assertIsNotNone(self.product)
	
		title = self.product.get('title')
		e_title = self.check_out_page.get_ck_rs_item_child()
		self.check_out_page.assert_ck_rs_text(title, e_title)

		qty = '1'
		e_desc = self.check_out_page.get_ck_rs_item_child(1)
		self.check_out_page.assert_ck_rs_text(qty, e_desc)

		price = self.product.get('price')
		e_price = self.check_out_page.get_ck_rs_item_child(2)
		self.check_out_page.assert_ck_rs_text(price, e_price)

		self.check_out_page.assert_subotal_price(price)

		shipping = self.product.get('shipping')
		self.check_out_page.assert_shipping_cost(shipping)

		self.check_out_page.assert_distcount_style()
		self.check_out_page.assert_total(price)
		# e_continue_payment = self.check_out_page.get_continue_to_payment_btn()
		self.check_out_page.assert_continue_to_payment_status()

	def check_out_to_payment(self):
		self.login_to_check_out()
		self.check_out_page.assertIsNotNone(self.product)
		element = self.check_out_page.get_continue_to_payment_btn_new()
		# self.check_out_page.scroll_to_element(element)
		element.click()
		# self.check_out_page.visibility_of_element_located_by_class_name('icon-paypal')
		self.check_out_page.get_credit_radio()
		expected_url = self.url + '/checkout'
		current_url = self.check_out_page.driver.current_url
		tmp = current_url.replace(expected_url, '').replace('/', '')
		order_id = tmp.split('?')[0]
		print('current_url: ', current_url)
		print(order_id)
		self.check_out_page.assertIsNotNone(order_id)

		cookies_file = cfs.G_COOKIE_FILE['checkout']
		cookies_list = self.check_out_page.get_cookies()
		fhd.pretty_write(cookies_list, cookies_file)

		url_after_checkout_file = cfs.INFOS_FILE['url_after_checkout']
		data = {
			'url': self.check_out_page.driver.current_url,
			'order_id': order_id
		}
		fhd.pretty_write(data, url_after_checkout_file)

	@classmethod
	def tearDownClass(cls):
		# self.check_out_page.driver.close()
		run_time = time.time() - cls.start_time
		print("%s: %.3f" % (cls.__name__, run_time))
		cls.check_out_page.driver.quit()

def main():
	from utils import case_suits

	test_suits = case_suits.CaseSuits()
	test_suits.add_checkout_suit('test_shipping_address')
	test_suits.add_checkout_suit('test_summary_infos')
	
	file_name = 'test_checkout_result_'
	from utils import report_to_wechat as rtw
	result = rtw.run_suites(file_name, test_suits.suits)
	rtw.report(result)


if __name__ == "__main__":
	main()
