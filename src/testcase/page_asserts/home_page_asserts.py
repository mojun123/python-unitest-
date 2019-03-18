from src.testcase.page_object import home_page as hp



class HomeAsserts(hp.Home):
	def __init__(self, driver=''):
		super(HomeAsserts, self).__init__()
		if driver:
			self.driver = driver

		self.default_welcome_text = 'genkifitness'
		self.default_login_popup_style = 'display: none;'
		self.active_login_popup_style = 'display: block;'

	def check_tvc_welcome(self, _text=''):
		element = self.get_tvc_welcome()
		self.assertIsNotNone(element)
		_text = _text or self.default_welcome_text
		self.assert_text_by_lower(_text, element)

	def check_tvc_account_sign_in_or_register_text(self, _text):
		element = self.get_tvc_account_sign_in_or_register()
		self.assertIsNotNone(element) 
		self.assert_text_by_lower(_text, element)

	def check_login_popup_status(self, b_active=False):
		element = self.get_login_popup()
		self.assertIsNotNone(element)
		expected_attr = self.default_login_popup_style
		if b_active:
			expected_attr = self.active_login_popup_style
		attr_name = 'style'
		self.assert_attr_in_or_not_by_attr_name(expected_attr, attr_name, element, reverse=True)
		return element

	def check_url_after_click_href(self, key_word, element):
		self.assertIsNotNone(element)
		self.scroll_to_element(element)
		self.assertIn(key_word,self.driver.current_url)
    
	

	