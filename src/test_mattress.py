import unittest
import os
import time
from utils import file_handle as fhd
from utils import commons as chd
from testcase.Mattress import Mattress
from pprint import pprint
from conf import common_file_setting as cfs


BASEDIR = os.path.dirname(os.getcwd())

class MattressTestSuits(unittest.TestCase):


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
		cls.mattress_page = Mattress()
		cls.mattress_page.init_class_name(cls.__name__)
		cls.mattress_page.init_dispatch()
		# cls.mattress_page.headless = False
		# cls.mattress_page.start_maximized = True
		# cls.mattress_page.b_popup = True
		# cls.mattress_page.random_user_agents()
		cls.mattress_page.set_chrome_options()
		proxy_json_file = os.path.join(BASEDIR,'conf', 'proxy.json')
		proxy = chd.random_proxy_from_file(proxy_json_file)
		cls.mattress_page.add_proxy(proxy)
		# cls.mattress_page.add_proxy('socks5://192.168.10.20:1081')
		log_conf = os.path.join(BASEDIR,'conf','log.conf')
		cls.mattress_page.init_driver('all_logs', log_conf)
		
		cls.start_time = time.time()

	def mattress_home(self, url='', b_refresh=False, b_reset=False):

		self.mattress_page.init_case_name(self._testMethodName)
		url = url or self.url + '/nighslee-10-inch-cool-gel-memory-foam-mattress-twin-size-222'
		self.mattress_page.init_base_infos(url)
		self.mattress_page.open()
		if b_refresh:
			self.mattress_page.refresh()
		if b_reset:
			self.mattress_page.scroll_to_offset(0)
		from testcase.common_page import CommonPage
		self.c_page = CommonPage(self.mattress_page)
		self.c_page.close_popup()

	def click_element(self, element, expected_str, page_obj):
		
		self.mattress_page.scroll_to_element_by_js(element)
		element.click()
		page_obj.assertIn(expected_str, page_obj.driver.current_url)

	def test_default_check_out_page(self):
		self.mattress_home()
		# self.mattress_page.open()

		self.mattress_page.check_product_seleted_text_init_status()
		self.mattress_page.check_product_selected_list_init_style()
		e_twin = self.mattress_page.get_mt_main_size_twin()
		self.mattress_page.check_mt_main_size_status('twin')

	def check_different_size_infos(self, product_size='twin'):
		self.mattress_home()
		# self.mattress_page.open()

		element, _ = self.mattress_page.mt_main_size_dispatch(product_size)
		self.mattress_page.scroll_to_element(element)
		self.mattress_page.check_mt_main_size_status(product_size)
		if product_size == 'twin_xl':
			product_size = 'twin xl'
		self.mattress_page.check_product_seleted_text(product_size)

	# 	_, price, title = self.mattress_page.get_mt_main_size_info(product_size)
	# 	shipping_cost = self.mattress_page.get_shipping_cost_tag()

	# def handle_product_infos(self, product_size, title, price, shipping):
	# 	if "free" in shipping.lower():
	# 		shipping = '$0'

	# 	data = {
	# 		'size': product_size,
	# 		'title': title,
	# 		'price': price,
	# 		'shipping'; shipping
	# 	}

	# 	file_name = cfs.G_COOKIE_FILE['product']
	# 	import codecs
	# 	with codecs.open(file_name, 'wb', 'utf-8') as f_obj:

	def test_mt_main_size_default(self):
		self.check_different_size_infos()

	def test_mt_main_size_twin_xl(self):
		size = 'twin_xl'
		self.check_different_size_infos(size)

	def test_mt_main_size_full(self):
		size = 'full'
		self.check_different_size_infos(size)

	def test_mt_main_size_queen(self):
		size = 'queen'
		self.check_different_size_infos(size)

	def test_mt_main_size_king(self):
		size = 'king'
		self.check_different_size_infos(size)

	def add_to_cart_and_del_item(self, product_size='', is_add_qty=False, is_del_item=True, is_close_cart=True):
		'''
		check all size , add to cart and del 
		@param:
			product_size - twin, twin xl, full, queen, king
				default: empty. mearning donot select size, just click add to cart
			is_add_qty: check add qty and del qty
		'''
		
		if product_size:
			element, _, _ = self.mattress_page.get_mt_main_size_info(product_size)
			self.mattress_page.scroll_to_element(element)
		else:
			product_size = 'twin'

		# self.mattress_page.check_cartApp_active()
		qty = 1
		shipping_cost = '$0'
		_, price, title = self.mattress_page.get_mt_main_size_info(product_size)
		e_add_to_cart, _ = self.mattress_page.get_mt_main_addcart_btn()
		self.mattress_page.scroll_to_element(e_add_to_cart)

		first_item_in_cart, _ = self.mattress_page.get_cart_list_child()
		self.mattress_page.assertEqual(title, self.mattress_page.get_cart_item_name(first_item_in_cart))
		self.mattress_page.assertEqual(price, self.mattress_page.get_cart_item_price(first_item_in_cart))
		self.mattress_page.get_cart_num_text(str(qty), first_item_in_cart)
		
		#check total infos
		self.mattress_page.assertEqual(price, self.mattress_page.get_subtotal_price())
		self.mattress_page.assertEqual(price, self.mattress_page.get_total_price())
		self.mattress_page.assertEqual(shipping_cost, self.mattress_page.get_shipping_price())
		self.mattress_page.check_cart_empty_status('display', False)
		self.mattress_page.check_cart_num_control_del_status()
		if is_add_qty:
			e_cart_control_add = self.mattress_page.get_cart_num_control_add()
			self.mattress_page.scroll_to_element(e_cart_control_add)
			self.mattress_page.check_cart_num_control_del_status('', True)
			qty += 1
			new_price = float(price.strip().replace('$', '')) * 2
			new_price = '$' + str(new_price)
			first_item_in_cart, _ = self.mattress_page.get_cart_list_child()
			self.mattress_page.get_cart_num_text(str(qty), first_item_in_cart)
			self.mattress_page.assertEqual(new_price, self.mattress_page.get_cart_item_price(first_item_in_cart))
			self.mattress_page.assertEqual(new_price, self.mattress_page.get_subtotal_price())
			self.mattress_page.assertEqual(new_price, self.mattress_page.get_total_price())
			self.mattress_page.assertEqual(shipping_cost, self.mattress_page.get_shipping_price())

			e_cart_control_del = self.mattress_page.get_cart_num_control_child()
			self.mattress_page.scroll_to_element(e_cart_control_del)
			qty -= 1
			first_item_in_cart, _ = self.mattress_page.get_cart_list_child()
			self.mattress_page.get_cart_num_text(str(qty), first_item_in_cart)
			self.mattress_page.assertEqual(price, self.mattress_page.get_cart_item_price(first_item_in_cart))

			self.mattress_page.assertEqual(price, self.mattress_page.get_subtotal_price())
			self.mattress_page.assertEqual(price, self.mattress_page.get_total_price())
			self.mattress_page.assertEqual(shipping_cost, self.mattress_page.get_shipping_price())
			self.mattress_page.check_cart_num_control_del_status()
		if is_del_item:
			self.mattress_page.del_item(first_item_in_cart)
		if is_close_cart:
			self.close_cart_UI()

		return product_size, qty
		
	def close_cart_UI(self):
		e_cart_close = self.mattress_page.get_cart_close()
		self.mattress_page.scroll_to_element(e_cart_close)
		self.mattress_page.check_cartApp_active(reverse=True)

	def check_add_to_cart_and_del_item(self, product_size='', is_add_qty=False):
		self.mattress_home(b_reset=True)
		# self.empty_cart_with_login()
		# self.mattress_page.check_banner()
		e_banner = self.mattress_page.get_banner()
		if e_banner:
			self.c_page.close_popup(e_banner)
		self.mattress_page.check_cart_empty_status('display')
		self.add_to_cart_and_del_item(product_size, is_add_qty)
		
	def test_add_cart_and_del_default(self):
		print("window size: ", self.mattress_page.driver.get_window_size())
		self.check_add_to_cart_and_del_item()

	def test_add_cart_and_del_twin_xl(self):
		size = 'twin_xl'
		self.check_add_to_cart_and_del_item(size, True)

	def test_add_cart_and_del_full(self):
		size = 'full'
		self.check_add_to_cart_and_del_item(size)

	def test_add_cart_and_del_queen(self):
		size = 'queen'
		self.check_add_to_cart_and_del_item(size)

	def test_add_cart_and_del_king(self):
		size = 'king'
		self.check_add_to_cart_and_del_item(size)

	def test_add_cart_and_del_twin(self):
		size = 'twin'
		self.check_add_to_cart_and_del_item(size) 
		
	def test_cart_checkout_without_login(self):

		self.mattress_home(b_reset=True)
		# self.mattress_page.open()
		self.mattress_page.check_cart_empty_status('display')
		self.add_to_cart_and_del_item(is_del_item=False, is_close_cart=False)
		e_check_out = self.mattress_page.get_cart_check_out_btn()
		self.mattress_page.scroll_to_element(e_check_out)
		self.mattress_page.assertIn('register', self.mattress_page.driver.current_url)

		self.c_page.close_popup()
		e_icon_shopping_bag = self.c_page.get_icon_shopping_bag()
		self.mattress_page.scroll_to_element(e_icon_shopping_bag)
		self.mattress_page.check_cartApp_active()

		first_item_in_cart, _ = self.mattress_page.get_cart_list_child()
		self.mattress_page.del_item(first_item_in_cart)

	def login_and_empty_cart(self):
		self.to_login()
		self.c_page.close_popup()
		self.mattress_page.empty_cart(self.c_page)


	def to_login(self):
		url = self.url + '/login'
		self.mattress_home(url)

		email, pwd = chd.get_login_infos(BASEDIR)
		self.mattress_page.assertIsNotNone(email)
		self.mattress_page.assertIsNotNone(pwd)
		e_login = self.c_page.login(email, pwd)
		e_login.click()

	@classmethod
	def tearDownClass(cls):

		run_time = time.time() - cls.start_time
		print("%s: %.3f" % (cls.__name__, run_time))
		cls.mattress_page.driver.quit()

def main():
	from utils import case_suits

	test_suits = case_suits.CaseSuits()
	test_suits.add_mattress_suit('test_default_check_out_page')
	test_suits.add_mattress_suit('test_mt_main_size_default')
	test_suits.add_mattress_suit('test_mt_main_size_twin_xl')
	test_suits.add_mattress_suit('test_mt_main_size_full')
	test_suits.add_mattress_suit('test_mt_main_size_queen')
	test_suits.add_mattress_suit('test_mt_main_size_king')
	test_suits.add_mattress_suit('test_add_cart_and_del_default')
	test_suits.add_mattress_suit('test_add_cart_and_del_twin_xl')
	test_suits.add_mattress_suit('test_add_cart_and_del_full')
	test_suits.add_mattress_suit('test_add_cart_and_del_queen')
	test_suits.add_mattress_suit('test_add_cart_and_del_king')
	test_suits.add_mattress_suit('test_add_cart_and_del_twin')
	test_suits.add_mattress_suit('test_cart_checkout_without_login')
	# test_suits.add_mattress_suit('login_and_empty_cart')
	
	file_name = 'test_mattress_result_'
	from utils import report_to_wechat as rtw
	result = rtw.run_suites(file_name, test_suits.suits)
	rtw.report(result)

if __name__ == "__main__":

	main()

