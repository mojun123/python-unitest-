import unittest
import os
import time
from utils import file_handle as fhd
from utils import commons as chd
from testcase.SelectPayment import SelectPayment
from pprint import pprint
from conf import common_file_setting as cfs


BASEDIR = os.path.dirname(os.getcwd())
G_ORDER_ID = ''


class SelectPaymentTestSuits(unittest.TestCase):


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

		cls.payment_page = SelectPayment()
		cls.payment_page.init_class_name(cls.__name__)

		# cls.payment_page.init_dispatch()
		# cls.payment_page.headless = False
		# cls.payment_page.start_maximized = True
		# cls.payment_page.random_user_agents()
		cls.payment_page.set_chrome_options()
		
		proxy_json_file = os.path.join(BASEDIR,'conf', 'proxy.json')
		proxy = chd.random_proxy_from_file(proxy_json_file)
		cls.payment_page.add_proxy(proxy)
		# cls.payment_page.add_proxy('socks5://192.168.10.20:1081')

		log_conf = os.path.join(BASEDIR,'conf','log.conf')
		cls.payment_page.init_driver('all_logs', log_conf)
		
		cls.start_time = time.time()
		cls.orders = []

	def payment_home(self, url=''):
		self.payment_page.init_case_name(self._testMethodName)

		#1 open home page and add cookie
		url = url or self.url 
		self.payment_page.init_base_infos(url)
		self.payment_page.open()
		from testcase.common_page import CommonPage
		self.c_page = CommonPage(self.payment_page)
		self.c_page.close_popup()

	def login_to_payment(self, b_first=True):

		url = self.url + '/login'
		self.payment_home(url)
		
		b_login = self.c_page.check_username("young")
		if "login" in self.payment_page.driver.current_url and not b_login:
			email, pwd = chd.get_login_infos(BASEDIR)
			self.c_page.shopping_flow_to_login(email, pwd)
			self.c_page.close_popup()

		if not b_first and self.orders:
			order_id = self.orders[0]
			if order_id:
				url = self.url + '/checkout/' + str(order_id)
				self.payment_page.open(url)
				self.c_page.close_popup()
		else:
			#empty cart
			self.c_page.empty_cart()
			self.c_page.check_cartApp_active()

			url = self.url + '/nighslee-10-inch-cool-gel-memory-foam-mattress-twin-size-222'
			self.payment_page.open(url)
			self.c_page.close_popup()

			self.c_page.shopping_flow_to_add_cart()
			self.c_page.shopping_flow_to_click_checkout()
			self.c_page.close_popup()
			self.c_page.check_page_loading_finished()
			order_id = self.c_page.check_out_to_payment(self.url)
			if order_id and order_id not in self.orders:
				self.orders.append(order_id)

		print("current_url  : ", self.payment_page.driver.current_url)
		self.load_conf_info()
		self.c_page.close_popup()


	def load_conf_info(self):

		info_file = cfs.INFOS_FILE['product_infos']
		from utils.commons import importModule
		self.credit_card_info = importModule(info_file, 'credit_card')

	def test_init_status(self):
		self.login_to_payment()
		self.payment_page.check_ck_credit()
		self.payment_page.check_ck_pay_list()
		self.payment_page.check_credit_redio_status()
		self.payment_page.check_paypal_redio_status()

	def test_select_credit(self):
		'''
		just test input a test account to see pay-now button enabled or not
		have no click pay-now button to see paid success or not
		'''
		self.login_to_payment(False)
		elemnet = self.payment_page.get_credit_radio()
		self.payment_page.scroll_to_element(elemnet)
		self.payment_page.check_using_shipping_address_checked()
		self.payment_page.check_credit_cart_btn_status()

		cardnumber = self.credit_card_info.get('cardnumber')
		exp_date = self.credit_card_info.get('exp_date')
		cvc = self.credit_card_info.get('cvc')

		self.payment_page.fill_in_credit_card_info(cardnumber, exp_date, cvc, self.c_page)
		self.payment_page.check_credit_cart_btn_status(True)

	def test_paypal(self):
		self.login_to_payment(False)
		elemnet = self.payment_page.get_paypal_radio()
		self.payment_page.scroll_to_element(elemnet)
		self.payment_page.check_credit_redio_status()
		self.payment_page.check_ck_pay_list('')
		e_continue_paypal = self.payment_page.get_paypal_btn()
		self.payment_page.scroll_to_element(e_continue_paypal)
		self.payment_page.assertIn('paypal', self.payment_page.driver.current_url)

	@classmethod
	def tearDownClass(cls):

		run_time = time.time() - cls.start_time
		print("%s: %.3f" % (cls.__name__, run_time))
		cls.payment_page.driver.quit()

		l_orders = cls.orders
		if l_orders:
			file_name = os.path.join(BASEDIR, 'conf', 'login.conf')

			for order_id in l_orders:
				try:
					from admin_main import cancle_order_by_id 
					print("will be cancel order: ", order_id)
					if order_id:
						cancle_order_by_id(order_id, file_name)
				except Exception as e:
					print(str(e))

def main():
	from utils import case_suits

	test_suits = case_suits.CaseSuits()
	test_suits.add_payment_suit('test_init_status')
	test_suits.add_payment_suit('test_select_credit')
	test_suits.add_payment_suit('test_paypal')
	
	file_name = 'select_payment_test_result_'
	
	from utils import report_to_wechat as rtw
	result = rtw.run_suites(file_name, test_suits.suits)
	rtw.report(result)

if __name__ == "__main__":
	main()
