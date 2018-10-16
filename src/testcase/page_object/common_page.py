	

class CommonPage(object):
	def __init__(self, page_obj):
		self.page_obj = page_obj
		self.driver = page_obj.driver

	def get_popup(self):
		e_id = 'CouponPop'
		return self.page_obj.find_element_by_id(e_id, timeout=5)

	def close_popup(self, element=''):
		try:
			element = element or self.get_popup() 
			if element:
				self.page_obj.disable_popup(element)
		except Exception as e:
			print(str(e))

	def login(self, email, pwd):
		
		from testcase.Login import Login
		l_page = Login(self.driver)
		return l_page.login(email, pwd)

	def check_username(self, name):
		from testcase.HomePage import Home 
		hp_page = Home(self.driver)
		try:
			h_page.check_username(name)
			return True
		except Exception as e:
			
			return False
	def get_icon_shopping_bag(self):
		
		from testcase import HomePage as hp
		h_page = hp.Home(self.driver)
		return h_page.get_icon_shopping_bag()

	def check_cart_icon(self):
		
		from testcase import HomePage as hp
		h_page = hp.Home(self.driver)
		return h_page.check_cart_icon()

	def empty_cart(self):
		from testcase.Mattress import Mattress
		m_page = Mattress(self.driver)
		return m_page.empty_cart(self)

	def check_cartApp_active(self):
		from testcase.Mattress import Mattress
		m_page = Mattress(self.driver)
		return m_page.check_cartApp_active(reverse=True)
	
	def get_cart_list_child(self):
		from testcase.Mattress import Mattress
		m_page = Mattress(self.driver)
		return m_page.get_cart_list_child()

	def get_header_add_to_cart_btn(self):
		from testcase.Mattress import Mattress
		m_page = Mattress(self.driver)
		return m_page.get_header_add_to_cart_btn()

	def get_cart_check_out_btn(self):
		from testcase.Mattress import Mattress
		m_page = Mattress(self.driver)
		return m_page.get_cart_check_out_btn()

	'''
	shopping flows
	'''
	def shopping_flow_to_login(self, email, pwd):
		
		self.page_obj.assertIsNotNone(email)
		self.page_obj.assertIsNotNone(pwd)
		e_login = self.login(email, pwd)
		e_login.click()

	def shopping_flow_to_add_cart(self):
		
		#add cart
		element, _ = self.get_header_add_to_cart_btn()
		self.page_obj.assertIsNotNone(element)
		self.page_obj.scroll_to_element(element)
		self.get_cart_list_child() 

	def shopping_flow_to_click_checkout(self):

		#click checkout
		self.close_popup()
		element = self.get_cart_check_out_btn()
		self.page_obj.assertIsNotNone(element)
		self.page_obj.scroll_to_element(element)
		self.page_obj.assertIn('checkout', self.page_obj.driver.current_url)

	def check_page_loading_finished(self):
		from testcase.CheckOut import CheckOut
		ck_page = CheckOut(self.driver)
		return ck_page.check_page_loading_finished()

	def get_summary_title(self):
		from testcase.CheckOut import CheckOut
		ck_page = CheckOut(self.driver)
		return ck_page.get_summary_title()


	def get_continue_to_payment_btn_new(self):
		from testcase.CheckOut import CheckOut
		ck_page = CheckOut(self.driver)
		return ck_page.get_continue_to_payment_btn_new()

	def check_out_to_payment(self, url):

		element = self.get_continue_to_payment_btn_new()
		# self.page_obj.scroll_to_element(element)
		element.click()

		self.page_obj.get_credit_radio()
		expected_url = url + '/checkout'
		current_url = self.page_obj.driver.current_url
		tmp = current_url.replace(expected_url, '').replace('/', '')
		order_id = tmp.split('?')[0]
		print('current_url: ', current_url)
		print(order_id)
		self.page_obj.assertIsNotNone(order_id)

		return order_id


	def open_mattress_page(self):
		from testcase import HomePage as hp
		h_page = hp.Home(self.driver)
		
		element, _ = h_page.check_menu_MATTRESS()
		self.page_obj.scroll_to_element(element)

		from testcase.Mattress import Mattress
		m_page = Mattress(self.driver)
		e_banner = m_page.get_banner()
		self.close_popup(e_banner)

		