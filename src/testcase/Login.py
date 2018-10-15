from page.chrome_driver import ChromeDriver as cdriver

class Login(cdriver):
	def __init__(self, driver=''):
		super(Login, self).__init__()
		if driver:
			self.driver = driver

	def close_popup(self):
		from testcase import HomePage as hp
		hp.close_popup(self)

	def get_login_social(self):
		e_class_name = 'lg-social'
		return self.find_element_by_class_name(e_class_name)

	def get_social_child(self, index):
		e_div = self.get_login_social()
		if not e_div:
			print(self.get_innerHTML(e_div))
			raise Exception("[Error] cannot locate lg-social")

		e_tage_name = 'a'
		element = self.get_element_child_by_tag_name(e_tage_name, index, e_div)

		return element, e_div

	def get_facebook_login_element(self):
		
		index = 0
		e_facebook, e_div = self.get_social_child(index)
		if not e_facebook:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_div))

		return e_facebook, e_div

	def get_twitter_login_element(self):
		
		index = 1
		e_twitter, e_div = self.get_social_child(index)
		if not e_twitter:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_div))

		return e_twitter, e_div

	def get_google_login_element(self):
		
		index = 2
		e_google, e_div = self.get_social_child(index)
		if not e_google:
			raise Exception("[err]cannot get child element: %s in: %s" %(index, e_div))

		return e_google, e_div

	def get_login_form(self):
		
		e_class_name = 'lg-form'
		e_form = self.find_element_by_class_name(e_class_name)
		if not e_form:
			print(self.get_innerHTML(e_form))
			raise Exception("[Error] cannot locate lg-form")
		return e_form

	def get_login_form_error(self):
		e_class_name = 'lg-error'
		lg_error = self.find_element_by_class_name(e_class_name)
		if not lg_error:
			print(self.get_innerHTML(lg_error))
			raise Exception("[Error] cannot locate lg-error")
		return lg_error

	def check_init_login_form_error(self):
		lg_error = self.get_login_form_error()
	
		style_str = lg_error.get_attribute('style')
		expected_style = "display: none"
		msg = "login form init status should no error info: %s" % self.get_innerHTML(lg_error)
		self.assertIn(expected_style, style_str, msg)

	def get_login_form_input_group(self, index=0):
		
		e_class_name = 'input-group'
		e_form = self.get_login_form()
		e_input = self.get_element_child_by_class_name(e_class_name, index, e_form)
		return e_input

	def get_login_form_child(self, index, attr_name):


		e_input_div = self.get_login_form_input_group(index)
		
		element = self.presence_of_element_located_by_tag_name(attr_name, driver=e_input_div)

		if not element:
			raise Exception("[Error] cannot locate email. email groups: %s" % e_input_div)

		return element
	
	def get_email_input(self):

		
		e_tage_name = "input"
		index = 0
		e_email = self.get_login_form_child(index, e_tage_name)
		return e_email

	def get_email_input_error(self):
		e_tage_name = "span"
		index = 0
		e_email = self.get_login_form_child(index, e_tage_name)
		return e_email

	def get_password_input(self):
		
		
		e_tage_name = "input"
		index = 1
		e_password = self.get_login_form_child(index, e_tage_name)
		return e_password

	def get_password_input_error(self):
		e_tage_name = "span"
		index = 1
		e_password = self.get_login_form_child(index, e_tage_name)
		return e_password

	def get_remember_input(self):
		
		e_tage_name = "input"
		index = 2
		e_remember = self.get_login_form_child(index, e_tage_name)
		return e_remember

	def check_remember_init_status(self, expected_seleted=True):
		e_remember = self.get_remember_input()
		b_selected = e_remember.is_selected()
		msg = "expected status: %s, but got status: %s" % (expected_seleted, b_selected)
		self.assertEqual(expected_seleted, b_selected, msg)

	def get_login_btn_input(self):
		
		e_tage_name = "button"
		index = 3
		e_login_btn = self.get_login_form_child(index, e_tage_name)
		return e_login_btn

	def check_login_btn_status(self, expected_disabled=None):
		"""
		@param:
			expected_disabled is None:
				meaning log in button is active
			init status:
				login button is diabled
		"""

		e_login_btn = self.get_login_btn_input()
		disabled = e_login_btn.get_attribute('disabled')
		
		msg = "expected status: %s, but got status: %s" % (expected_disabled, disabled)
		
		assert disabled == expected_disabled, msg

	def check_login_btn_init_status(self):
		expected_disabled = "true"
		self.check_login_btn_status(expected_disabled)

	def get_login_bottom(self):
		e_class_name = 'lg-bottom'
		e_bottom = self.find_element_by_class_name(e_class_name)
		if not e_bottom:
			print(self.get_innerHTML(e_bottom))
			raise Exception("[Error] cannot locate lg-form")
		return e_bottom

	def get_login_bottom_child(self, index=0):
		e_bottom_div = self.get_login_bottom()
		
		e_class_name = 'a'
		e_a= self.get_element_child_by_tag_name(e_class_name, index, e_bottom_div)
		return e_a

	def get_register_element(self):
		index = 0
		e_register = self.get_login_bottom_child(index)
		self.assertIsNotNone(e_register)

		return e_register

	def get_reset_element(self):
		index = 1
		e_reset = self.get_login_bottom_child(index)
		self.assertIsNotNone(e_reset)

		return e_reset

	def login(self, email, pwd):

		e_email = self.get_email_input()
		e_pwd = self.get_password_input()

		e_email.clear()
		e_email.send_keys(email)
		e_pwd.clear()
		e_pwd.send_keys(pwd)
		e_login = self.get_login_btn_input()

		return e_login

