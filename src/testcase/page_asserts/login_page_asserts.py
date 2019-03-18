from src.testcase.page_object import login_page as jp


class LoginAsserts(jp.Login):
	def __init__(self, driver=''):
		super(LoginAsserts, self).__init__()
		if driver:
			self.driver = driver

		self.default_welcome_text = 'genkifitness'
		self.default_login_popup_style = 'display: none;'	
		self.active_login_popup_style = 'display: block;'

	def check_url_after_click_href(self, key_word, element):
		self.assertIsNotNone(element)
		self.scroll_to_element(element)
		self.assertIn(key_word, self.driver.current_url)

	def cherck_tvc_account_email_address_pass_world(self, _text):
		element = self.get_login_address(self)
		self.assertIsNotNone(element)
		self.assert_text_by_lower(_text, element)
	
		
	