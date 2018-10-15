from page.chrome_driver import ChromeDriver as cdriver



class Home(cdriver):
	def __init__(self, driver=''):
		super(Home, self).__init__()
		if driver:
			self.driver = driver

	

	def _dispatch(self, command, arg):
		# send(dispatch[command](arg))
		self.res_dispatch = {
			"home": self.check_menu_HOME,
			"mattress": self.check_menu_MATTRESS,
			"reviews": self.check_menu_REVIEWS,
			"faqs": self.check_menu_FAQS,
			"contact": self.check_menu_CONTACT,
		}
		if command not in self.res_dispatch:
			raise Exception("[Error]command: %s not found in: %s"%(command, self.res_dispatch))
		cmd, nav_menu = self.res_dispatch[command](arg)
		return cmd, nav_menu

	def check_all_menu(self, command, arg=True):
		# send(dispatch[command](arg))
		self.res_dispatch = {
			"home": self.check_menu_HOME,
			"mattress": self.check_menu_MATTRESS,
			"reviews": self.check_menu_REVIEWS,
			"faqs": self.check_menu_FAQS,
			"contact": self.check_menu_CONTACT,
		}
		for key, value in self.res_dispatch.items():
			if key == command:
				continue
			cmd, nav_menu = self.res_dispatch[key](arg)
		
	def check_nav_menu(self):
		#home menu ,include HOME, MATTRESS, PILLPW...
		e_class_name = 'header-nav-list'
		e_menu = self.find_element_by_class_name(e_class_name)

		return e_menu

	def check_menu_child(self, index, msg, reverse=False):
		e_ul = self.check_nav_menu()
		# print("check_menu_child: ", self.get_innerHTML(e_ul))
		if not e_ul:
			print(self.get_innerHTML(e_ul))
			raise Exception("[Error] cannot locate header-nav-list")
		msg = msg % self.get_innerHTML(e_ul)
		e_tage_name = 'li'
		element = self.get_element_child_by_tag_name(e_tage_name, index, e_ul)

		attr_name = 'class'
		expected_attr = 'active'
		real_attr = element.get_attribute(attr_name)
		self.assertInOrNotIn(expected_attr, real_attr, reverse=reverse)

		return element, e_ul

	def check_menu_HOME(self, reverse=False):
		
		msg = '[Error]HOME menu not active.menu: %s'
		index = 0
		e_HOME, e_ul = self.check_menu_child(index, msg, reverse)

		self.assertIsNotNone(e_HOME)

		return e_HOME, e_ul

	def check_menu_MATTRESS(self, reverse=True):

		msg = '[Error]MATTRESS menu be actived.should be active HOME menu. menu: %s'
		index = 1
		e_MATTRESS, e_ul = self.check_menu_child(index, msg, reverse)
		self.assertIsNotNone(e_MATTRESS)

		
		return e_MATTRESS, e_ul

	def check_menu_REVIEWS(self, reverse=True):

		msg = '[Error]REVIEWS menu be actived.should be active HOME menu. menu: %s'
		index = -4
		e_REVIEWS, e_ul = self.check_menu_child(index, msg, reverse)

		self.assertIsNotNone(e_REVIEWS)
		
		return e_REVIEWS, e_ul

	def check_menu_FAQS(self, reverse=True):

		msg = '[Error]FAQS menu be actived.should be active HOME menu. menu: %s'
		index = -2
		e_FAQS, e_ul = self.check_menu_child(index, msg, reverse)
		self.assertIsNotNone(e_FAQS)
		
		return e_FAQS, e_ul

	def check_menu_CONTACT(self, reverse=True):
		
		msg = '[Error]CONTACT menu be actived.should be active HOME menu. menu: %s'
		index = -1
		e_CONTACT, e_ul = self.check_menu_child(index, msg, reverse)
		self.assertIsNotNone(e_CONTACT)
		
		return e_CONTACT, e_ul

	def get_cart_parent(self):
		e_class_name = 'header-add-cart'
		element = self.find_element_by_class_name(e_class_name)
		return element
	
	def check_cart_icon(self):
		e_class_name = 'icon-shopping-bag'
		# e_class_name = 'header-add-cart'
		e_cart = self.find_element_by_class_name(e_class_name)
		print(self.get_innerHTML(e_cart))

		# e_div = self.get_cart_parent()
		# if not e_div:
		# 	print(self.get_innerHTML(e_div))
		# 	raise Exception("[Error] cannot locate header-add-cart")
		# print(self.get_innerHTML(e_div))

		# e_tage_name = 'span'
		# e_cart = self.find_element_by_tag_name(e_tage_name, e_div)

		# attr_name = 'class'
		# expected_attr = 'icon'
		# real_attr = e_cart.get_attribute(attr_name)
		# self.assertInOrNotIn(expected_attr, real_attr)

		return e_cart

	def get_username_div(self):
		e_class_name = 'header-right-main'
		element = self.find_element_by_class_name(e_class_name)

		return element

	def get_username_parent(self):
		# e_class_name = 'username'
		# element = self.find_element_by_class_name(e_class_name)

		# return element
		e_username_div = self.get_username_div()
		if not e_username_div:
			print(self.get_innerHTML(e_username_div))
			raise Exception("[Error] cannot locate username")

		e_tage_name = 'li'
		e_user_index = self.find_element_by_tag_name(e_tage_name, e_username_div)
		self.assertIsNotNone(e_user_index)

		return e_user_index

	def get_username_element(self):
		e_username = self.get_username_parent()
		if not e_username:
			print(self.get_innerHTML(e_username))
			raise Exception("[Error] cannot locate username")

		e_tage_name = 'a'
		e_user_index = self.find_element_by_tag_name(e_tage_name, e_username)
		self.assertIsNotNone(e_user_index)

		return e_user_index

	def check_username(self, attr):
		element = self.get_username_element()
		# msg = "[error]expected name: {0}, but got: {1}"
		print(self.driver.current_url)
		real_name  = element.text

		self.assertIn(attr, real_name)

	def check_login(self):
		self.check_username('log in')

	def check_chat_now_button(self):
		element_id = 'button-body'
		element = self.element_to_be_clickable_by_id(element_id)
		return element
	
	def get_subscribe_btn(self):
		e_class_name = 'footer-subscribe-btn'

		return self.find_element_by_class_name(e_class_name)

	def get_subscribe_div(self):
		e_class_name = 'footer-subscribe-group'

		return self.find_element_by_class_name(e_class_name)

	def get_subscribe_input_element(self):
		e_subscribe = self.get_subscribe_div()
		if not e_subscribe:
			print(self.get_innerHTML(e_subscribe))
			raise Exception("[Error] cannot locate username")

		e_tage_name = 'input'
		e_input_email = self.find_element_by_tag_name(e_tage_name, e_subscribe)
		self.assertIsNotNone(e_input_email)

		return e_input_email

	def get_icon_shopping_bag(self):
		
		e_class_name = 'icon-shopping-bag'
		return self.find_element_by_class_name(e_class_name)

