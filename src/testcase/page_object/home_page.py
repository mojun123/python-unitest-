from src.page.chrome_driver import ChromeDriver as cdriver

class Home(cdriver):
	def __init__(self, driver=''):
		super(Home, self).__init__()
		if driver:
			self.driver = driver

	def get_login_popup(self):
		e_id = 'login-pnl'
		return self.find_element_by_id(e_id)

	#get topViewContainer ui
	def get_topViewContainer(self):
		e_id = 'topViewContainer'
		return self.find_element_by_id(e_id)

	def get_tvc_welcome(self):
		e_id = 'welcome'
		return self.find_element_by_id(e_id)

	def get_tvc_account(self):
		e_id = 'signin'
		return self.find_element_by_id(e_id)

	def get_tvc_account_sign_in_or_register(self):
		e_parent = self.get_tvc_account()
		self.assertIsNotNone(e_parent)
		e_tage_name = 'a'
		element, _ = self.get_element_child_by_tag_name(e_tage_name, 0, e_parent)
		return element

	def get_tvc_account_my_account(self):
		e_parent = self.get_tvc_account()
		self.assertIsNotNone(e_parent)
		e_tage_name = 'a'
		element, _ = self.get_element_child_by_tag_name(e_tage_name, 1, e_parent) 
		return element

	def get_tvc_minicart(self):
		e_id = 'minicart'
		return self.find_element_by_id(e_id)

	def get_tvc_minicart_qty(self):
		e_id = 'mini-qty'
		return self.find_element_by_id(e_id)

	def get_tvc_minicart_price(self):
		e_id = 'mini-amount'
		return self.find_element_by_id(e_id)

	def get_tvc_view_cart_btn(self):
		e_id = 'checkout-btn'
		return self.find_element_by_id(e_id)

	def get_tvc_search(self):
		e_id = 'search-bar'
		return self.find_element_by_id(e_id)

	#get menu area elements
	def get_menu_list(self):
		e_class_name = 'menu-list'
		return self.find_element_by_class_name(e_class_name)

	def get_default_menu_list_sub(self):
		e_class_name = 'menu-list-sub'
		return self.find_element_by_class_name(e_class_name)

	def get_menu_help(self, e_parent=None):
		e_parent = e_parent or self.get_menu_list()
		self.assertIsNotNone(e_parent)
		e_tage_name = 'a'
		element, _ = self.get_element_child_by_tag_name(e_tage_name, -1, e_parent)
		return element

	def get_menu_track_order(self, e_parent=None):
		e_parent = e_parent or self.get_menu_list()
		self.assertIsNotNone(e_parent)
		e_tage_name = 'a'
		element, _ = self.get_element_child_by_tag_name(e_tage_name, -2, e_parent)
		return element

	def get_menu_best_sellers(self, e_parent=None):
		e_parent = e_parent or self.get_menu_list()
		self.assertIsNotNone(e_parent)
		e_tage_name = 'a'
		element, _ = self.get_element_child_by_tag_name(e_tage_name, -3, e_parent)
		return element

	#to get slides area elements
	def get_banner(self):
		e_id = 'slides'
		return self.find_element_by_id(e_id)


	#to get product list 
	def get_product_list(self):
		e_class_name = 'index-glist-wrapper'
		return self.find_element_by_class_name(e_class_name)

	def get_pl_len_sku(self, e_parent=None):
		e_parent = e_parent or self.get_product_list()
		self.assertIsNotNone(e_parent)
		e_class_name = 'index-glist-box'
		return self.get_element_child_by_class_name(e_class_name, 0, e_parent)
		 
	
	def get_pl_first_list_box(self):
		element, _ = self.get_pl_len_sku()
		return element

	def get_pl_first_list_box_href(self, e_parent=None):
		e_parent = e_parent or self.get_pl_first_list_box()
		self.assertIsNotNone(e_parent)
		e_tage_name = 'a'
		element, _ = self.get_element_child_by_tag_name(e_tage_name, 0, e_parent)
		return element

	def get_pl_first_list_box_price(self, e_parent=None):
		e_parent = e_parent or self.get_pl_first_list_box()
		self.assertIsNotNone(e_parent)
		e_class_name = 'glist-price'
		element, _ = self.get_element_child_by_class_name(e_class_name, 0, e_parent)
		return element

	#to get footer area elements
	def get_footer(self):
		e_id = 'footer'
		return self.find_element_by_id(e_id)

	def get_ft_child(self, index=0):
		e_parent = self.get_footer()
		self.assertIsNotNone(e_parent)
		e_class_name = 'mr45'
		element, _ = self.get_element_child_by_class_name(e_class_name, index, e_parent)
		return element

	def get_ft_company_info_ul(self):
		return self.get_ft_child()

	def get_ft_customer_service(self):
		return self.get_ft_child(1)

	def get_ft_shipping_returns(self):
		return self.get_ft_child(2)

	def get_ft_second_child(self, e_parent, index=0):
		self.assertIsNotNone(e_parent)
		e_tage_name = 'a'
		element, _ = self.get_element_child_by_tag_name(e_tage_name, index, e_parent)
		return element

	def get_ft_company_info_ul_child(self, index=0):
		e_parent = self.get_ft_company_info_ul()
		return self.get_ft_second_child(e_parent, index)

	def get_ft_customer_service_child(self, index=0):
		e_parent = self.get_ft_customer_service()

		return self.get_ft_second_child(e_parent, index)

	def get_ft_shipping_returns_child(self, index=0):
		e_parent = self.get_ft_shipping_returns()
		return self.get_ft_second_child(e_parent, index)

	# get footer - company info area href
	def get_ft_cp_about_us(self):

		return self.get_ft_company_info_ul_child()

	def get_ft_terms(self):

		index = 1
		return self.get_ft_company_info_ul_child(index)

	def get_ft_privacy(self):

		index = 2
		return self.get_ft_company_info_ul_child(index)

	def get_ft_warranty(self):

		index = -2
		return self.get_ft_company_info_ul_child(index)

	def get_ft_sit_map(self):

		index = -1
		return self.get_ft_company_info_ul_child(index)

	#get footer - customer service area href
	def get_ft_cs_contact_us(self):
		return self.get_ft_customer_service_child()

	def get_ft_cs_my_account(self):
		index = 1
		return self.get_ft_customer_service_child(index)

	def get_ft_cs_faq(self):
		index = -1
		return self.get_ft_customer_service_child(index)

	#get footer - shipping returns area href
	def get_ft_sr_shipping_guide(self):
		return self.get_ft_shipping_returns_child()

	def get_ft_sr_return_policy(self):
		index = 1
		return self.get_ft_shipping_returns_child(index)

	def get_ft_sr_track_my_order(self):
		index = -1
		return self.get_ft_shipping_returns_child(index)

	def get_livechat(self):
		e_class_name = 'mylivechat_collapsed_text'
		return self.find_element_by_class_name(e_class_name)

	