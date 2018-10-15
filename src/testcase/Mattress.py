from page.chrome_driver import ChromeDriver as cdriver
		
class Mattress(cdriver):

	def __init__(self, driver=''):
		super(Mattress, self).__init__()
		if driver:
			self.driver = driver 

	def init_dispatch(self):
		
		self.res_dispatch = {
			"twin": self.get_mt_main_size_twin,
			"twin_xl": self.get_mt_main_size_twin_xl,
			"full": self.get_mt_main_size_full,
			"queen": self.get_mt_main_size_queen,
			"king": self.get_mt_main_size_king,
		}

	def get_mattress_sub_menu(self):
		e_class_name = 'header-nav-sub-nav'
		return self.find_element_by_class_name(e_class_name)

	def get_mattress_child(self, index):
		e_ul = self.get_mattress_sub_menu()
		self.assertIsNotNone(e_ul)

		e_tage_name = 'li'
		element = self.get_element_child_by_tag_name(e_tage_name, index, e_ul)

		return element, e_ul

	def get_twin(self):
		
		index = 0
		e_child, e_parent = self.get_mattress_child(index)
		if not e_child:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_parent))
		return e_child, e_parent

	def get_twin_xl(self):
		
		index = 1
		e_child, e_parent = self.get_mattress_child(index)
		if not e_child:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_parent))
		return e_child, e_parent

	def get_full(self):
		
		index = 2
		e_child, e_parent = self.get_mattress_child(index)
		if not e_child:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_parent))
		return e_child, e_parent

	def get_queen(self):
		
		index = 3
		e_child, e_parent = self.get_mattress_child(index)
		if not e_child:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_parent))
		return e_child, e_parent

	def get_king(self):
		
		index = 4
		e_child, e_parent = self.get_mattress_child(index)
		if not e_child:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_parent))
		return e_child, e_parent

	def get_product_seleted(self):
		e_class_name = 'product-selected-text'
		return self.find_element_by_class_name(e_class_name)

	def get_product_seleted_text(self):
		e_class_name = 'product-selected'
		return self.find_element_by_class_name(e_class_name)

	def check_product_seleted_text(self, expected_attr):

		element = self.get_product_seleted_text()
		real_attr = element.text.lower()
		self.assertIn(expected_attr, real_attr)

	def check_product_seleted_text_init_status(self):
		
		expected_attr = 'twin'
		self.check_product_seleted_text(expected_attr)

	def get_product_seleted_list(self):
		e_class_name = 'product-select-list'
		return self.find_element_by_class_name(e_class_name)

	def check_product_selected_list_init_style(self):
		element = self.get_product_seleted_list()
		real_attr = element.get_attribute('style')
		expected_attr = "display: none"

		self.assertIn(expected_attr, real_attr)

	def get_product_selected_list_child(self, index):
		e_ul = self.get_product_seleted_list()
		self.assertIsNotNone(e_ul)

		e_tage_name = 'li'
		element = self.get_element_child_by_tag_name(e_tage_name, index, e_ul)

		return element, e_ul

	def get_product_selected_twin(self):
		
		index = 0
		e_child, e_parent = self.get_product_selected_list_child(index)
		if not e_child:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_parent))
		return e_child, e_parent

	def get_product_selected_twin_xl(self):
		
		index = 1
		e_child, e_parent = self.get_product_selected_list_child(index)
		if not e_child:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_parent))
		return e_child, e_parent

	def get_product_selected_full(self):
		
		index = 2
		e_child, e_parent = self.get_product_selected_list_child(index)
		if not e_child:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_parent))
		return e_child, e_parent

	def get_product_selected_queen(self):
		
		index = 3
		e_child, e_parent = self.get_product_selected_list_child(index)
		if not e_child:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_parent))
		return e_child, e_parent

	def get_product_selected_king(self):
		
		index = 4
		e_child, e_parent = self.get_product_selected_list_child(index)
		if not e_child:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_parent))
		return e_child, e_parent

	def get_mt_header_size(self):
		e_class_name = 'mt-header-size'
		return self.find_element_by_class_name(e_class_name)

	def get_mt_header_size_child(self, index=0):
		e_parent = self.get_mt_header_size()
		self.assertIsNotNone(e_parent)

		e_tage_name = 'button'
		element = self.get_element_child_by_tag_name(e_tage_name, index, e_parent)

		return element, e_parent

	def get_header_add_to_cart_btn(self):
		index = 0
		e_child, e_parent = self.get_mt_header_size_child(index)
		if not e_child:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_parent))
		return e_child, e_parent

	def get_header_title(self):
		e_class_name = 'mt-header-title'
		return self.find_element_by_class_name(e_class_name).text

	def get_mt_main_info(self):
		e_class_name = 'mt-main-info'
		return self.find_element_by_class_name(e_class_name)

	def get_mt_main_info_child(self, index=0, e_tage_name=None):
		e_parent = self.get_mt_main_info()
		if not e_parent:
			print(self.get_innerHTML(e_parent))
			raise Exception("[Error] cannot locate lg-social")

		e_tage_name = e_tage_name or 'div'
		element = self.get_element_child_by_tag_name(e_tage_name, index, e_parent)

		return element, e_parent

	def get_mt_main_info_title(self):
		e_title, e_parent = self.get_mt_main_info_child(index=0, e_tage_name='h2')
		return e_title.text

	def get_mt_main_price(self):
		e_class_name = 'mt-main-price'
		return self.find_element_by_class_name(e_class_name)

	def get_mt_main_price_discount(self):
		e_class_name = 'mt-main-price-discount'
		return self.find_element_by_class_name(e_class_name)

	def get_shipping_tag(self):
		e_class_name = 'mt-main-price-tag'
		return self.find_element_by_class_name(e_class_name)

	def get_mt_main_size_list(self):
		e_class_name = 'mt-main-size-list'
		return self.find_element_by_class_name(e_class_name)

	def get_mt_main_size_child(self, index=0, e_tage_name=None):
		e_parent = self.get_mt_main_size_list()
		if not e_parent:
			print(self.get_innerHTML(e_parent))
			raise Exception("[Error] cannot locate lg-social")

		e_tage_name = e_tage_name or 'li'
		element = self.get_element_child_by_tag_name(e_tage_name, index, e_parent)

		return element, e_parent
	def check_mt_main_size_class(self, element, attr='class', expected_attr='', reverse=False):
		real_attr = element.get_attribute(attr)

		self.assertEqOrNotEqual(expected_attr, real_attr, reverse=reverse)
		
	def get_mt_main_size_child_text(self, element):
		
		child = element.find_element_by_tag_name('div')
		return child.text.strip(), element.get_attribute('class')

	def get_mt_main_size_twin(self):
		
		index = 0
		e_child, e_parent = self.get_mt_main_size_child(index)
		if not e_child:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_parent))
		
		return e_child, e_parent

	def get_mt_main_size_twin_xl(self):
		
		index = 1
		e_child, e_parent = self.get_mt_main_size_child(index)
		if not e_child:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_parent))
		return e_child, e_parent

	def get_mt_main_size_full(self):
		
		index = 2
		e_child, e_parent = self.get_mt_main_size_child(index)
		if not e_child:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_parent))
		return e_child, e_parent

	def get_mt_main_size_queen(self):
		
		index = 3
		e_child, e_parent = self.get_mt_main_size_child(index)
		if not e_child:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_parent))
		return e_child, e_parent

	def get_mt_main_size_king(self):
		
		index = 4
		e_child, e_parent = self.get_mt_main_size_child(index)
		if not e_child:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_parent))
		return e_child, e_parent

	def get_mt_main_addcart_btn(self):
		# e_mt_main_addcart, e_parent = self.get_mt_main_info_child(index=0, e_tage_name='button')

		element, _ = self.get_mt_main_info_child(index=0, e_tage_name='button')
		# print(self.get_outerHTML(element))
		self.assertIn('Add To Cart', element.text)
		return element, None

	def mt_main_size_dispatch(self, command):
		# send(dispatch[command](arg))
		
		if command not in self.res_dispatch:
			raise Exception("[Error]command: %s not found in: %s"%(command, self.res_dispatch))
		# print(self.res_dispatch[command])
		# print(command)
		cmd, nav_menu = self.res_dispatch[command]()
		return cmd, nav_menu

	def check_mt_main_size_status(self, command):

		for key, value in self.res_dispatch.items():
			cmd, nav_menu = self.res_dispatch[key]()
			if key == command:
				if command == 'twin_xl':

					expected_attr =  'twin xl' + ' size' 
				else:
					expected_attr = command + ' size'
				real_header_title =  self.get_header_title().lower()
				self.assertIn(expected_attr, real_header_title)
				real_main_info_title = self.get_mt_main_info_title().lower()
				self.assertIn(expected_attr, real_main_info_title)
				self.check_mt_main_size_class(cmd, expected_attr='active')
			else:
				self.check_mt_main_size_class(cmd)

	def get_mt_main_size_info(self, command):
		if command not in self.res_dispatch:
			raise Exception("[Error]command: %s not found in: %s"%(command, self.res_dispatch))
		cmd, nav_menu = self.res_dispatch[command]()
		e_div = self.presence_of_element_located_by_tag_name('div', cmd)

		e_class_name = 'mt-main-size-price'
		e_price= self.get_element_child_by_class_name(e_class_name, 0, cmd)
		price = e_price.text
		title = self.get_header_title()

		return e_div, price, title

	def get_cartApp(self):
		e_id = 'cartApp'
		# return self.visibility_of_element_located_by_id(e_id)
		return self.find_element_by_id(e_id)

	def check_cartApp_active(self, expected_attr='active', reverse=False):
		element = self.get_cartApp()
		attr = 'class'
		real_attr = element.get_attribute(attr)
		# print(self.get_outerHTML(element))
		self.assertInOrNotIn(expected_attr, real_attr, reverse=reverse)

	def get_cart_list(self):
		
		e_class_name = 'cart-list'
		return self.visibility_of_element_located_by_class_name(e_class_name)

	def get_cart_list_child(self, index=0, e_tage_name=None):
		
		e_parent = self.get_cart_list()
		self.assertIsNotNone(e_parent)

		e_tage_name = e_tage_name or 'li'
		element = self.get_element_child_by_tag_name(e_tage_name, index, e_parent)

		return element, e_parent


	def get_cart_item_name(self, element):
		e_class_name = 'cart-item-name'
		# print(self.get_outerHTML(element))
		return self.visibility_of_element_located_by_class_name(e_class_name, element).text

	def get_cart_num_text(self, qty, element):
		e_class_name = 'cart-num-text'
		return self.text_to_be_present_in_element_by_class_name(e_class_name, qty, element)

	def get_cart_item_price(self, element):
		e_class_name = 'cart-item-price'
		return self.find_element_by_class_name(e_class_name, element).text

	def get_cart_item_right(self, element):
		e_class_name = 'cart-item-right'
		return self.find_element_by_class_name(e_class_name, element)

	def get_cart_item_del(self, element):
		e_class_name = 'cart-item-del'
		return self.element_to_be_clickable_by_class_name(e_class_name, element)

	def get_cart_total(self):
		e_class_name = 'cart-total'
		element = self.presence_of_element_located_by_class_name(e_class_name)
		
		return element

	def get_subtotal_info(self, index=0):
		e_parent = self.get_cart_total()

		e_tage_name = 'li'
		e_subtotal = self.get_element_child_by_tag_name(e_tage_name, index, e_parent)
		return e_subtotal

	def get_cart_total_price(self, element):
		e_class_name='cart-total-value'

		return self.visibility_of_element_located_by_class_name(e_class_name, element)

	def get_subtotal_price(self):
		element = self.get_subtotal_info()
		return self.get_cart_total_price(element).text

	def get_shipping_price(self):

		element = self.get_subtotal_info(index=1)

		return self.get_cart_total_price(element).text

	def get_total_price(self):
		element = self.get_subtotal_info(index = 2)
		return self.get_cart_total_price(element).text

	def get_cart_empty_status(self):
		
		
		e_class_name = 'header-cart-num'
		element = self.find_element_by_class_name(e_class_name)
		real_attr = element.get_attribute('style')
		if not real_attr:
			return False
		return True
		# e_class_name = 'cart-empty'
		# element = self.find_element_by_class_name(e_class_name)
		# real_attr = element.get_attribute('style')
		# if real_attr:
		# 	return False
		# return True

	def check_cart_empty_status(self, expected_attr, reverse=True):
		
		if reverse:
			e_class_name = 'cart-empty-text'
			element = self.text_to_be_present_in_element_by_class_name(e_class_name, "Your cart is empty")

		e_class_name = 'cart-empty'
		element = self.find_element_by_class_name(e_class_name)
		real_attr = element.get_attribute('style')
		self.assertInOrNotIn(expected_attr, real_attr, reverse=reverse)

	def get_cart_header(self):
		e_class_name = 'cart-header'
		return self.find_element_by_class_name(e_class_name)

	def get_cart_close(self):
		element = self.get_cart_header()
		e_tage_name = 'span'
		index = 1
		return self.get_element_child_by_tag_name(e_tage_name, index, element)

	def get_cart_num_control(self):
		e_class_name = 'cart-num-control'
		return self.find_element_by_class_name(e_class_name)

	def get_cart_num_control_child(self, e_tage_name='button', index=0):
		element = self.get_cart_num_control()

		return self.get_element_child_by_tag_name(e_tage_name, index, element)

	def get_cart_num_control_add(self):
		# element = self.get_cart_num_control()
		return self.get_cart_num_control_child(index=1)

	def check_cart_num_control_del_status(self, expected_attr='true', reverse=False):
		
		e_cart_control_del = self.get_cart_num_control_child()
		real_attr = e_cart_control_del.get_attribute('disabled')
		self.assertEqOrNotEqual(expected_attr, real_attr, reverse=reverse)

	def get_cart_check_out_btn(self):
		
		e_class_name = 'cart-main'
		element = self.find_element_by_class_name(e_class_name)

		xpath = "//button[contains(@class, 'cart-checkout')]"
		return self.find_element_by_xpath(xpath, element)

	# def get_cart_check_out_btn_new(self):
	# 	e_class_name = 'cart-main'
	# 	element = self.find_element_by_class_name(e_class_name)

		
	# 	index = -1
	# 	e_tage_name = 'button'
	# 	return self.get_element_child_by_tag_name(e_tage_name, index, element)
	def get_banner(self):
		e_id = 'banner'
		return self.find_element_by_id(e_id)
		# self.assertIsNotNone(element)

	def check_banner(self):
		e_id = 'banner'
		element = self.visibility_of_element_located_by_id(e_id)
		self.assertIsNotNone(element)

	def get_shipping_cost_tag(self):
		e_class_name = 'mt-main-price-tag'
		return self.find_element_by_class_name(e_class_name)

	def assert_is_freeshipping(self, expected_attr='free'):
		element = self.get_shipping_cost_tag()
		self.assertIn(expected_attr, real_attr)

	# def close_popup(self):
	# 	from testcase import HomePage as hp
	# 	hp.close_popup(self)

	# def get_icon_shopping_bag(self, driver=''):
	# 	if driver:
	# 		self.set_driver(driver)
	# 	from testcase import HomePage as hp
	# 	h_page = hp.Home(self.driver)
	# 	# h_page.set_driver(self.driver)
	# 	return h_page.get_icon_shopping_bag(self)

	# def check_cart_icon(self, driver=''):
	# 	if driver:
	# 		self.set_driver(driver)
		
	# 	from testcase import HomePage as hp
	# 	h_page = hp.Home(self.driver)
	# 	# h_page.set_driver(self.driver)
	# 	return h_page.check_cart_icon()

	# def login(self, email, pwd):
		
	# 	from testcase.Login import Login
	# 	l_page = Login(self.driver)
	# 	# l_page.set_driver(self.driver)
	# 	return l_page.login(email, pwd)

	def del_item(self, first_element_in_cart):
		e_item_del = self.get_cart_item_del(first_element_in_cart)
		e_item_del.click()
		self.check_cart_empty_status('display', True)

	def empty_cart(self, common_page):
		
		b_empty = False
		max_run = 100
		count = 0
		while not b_empty and count < 100:
			count += 1

			b_empty = self.get_cart_empty_status()

			if not b_empty:

				e_cart_icon = common_page.check_cart_icon()
				self.scroll_to_element(e_cart_icon)
				
				# e_cart_icon.click()

				first_item_in_cart, _ = self.get_cart_list_child()
				self.del_item(first_item_in_cart)
				b_empty = self.get_cart_empty_status()

		e_cart_close = self.get_cart_close()
		self.scroll_to_element(e_cart_close)

