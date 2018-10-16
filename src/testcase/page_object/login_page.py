from page.chrome_driver import ChromeDriver as cdriver

class Home(cdriver):
	def __init__(self, driver=''):
		super(Home, self).__init__()
		if driver:
			self.driver = driver

	def get_popup_close(self):
		e_id = 'lb-close'
		return self.find_element_by_id(e_id)

	def get_popup_ui(self):
		e_id = 'popup-login-border'
		return self.find_element_by_id(e_id)

	#to get login area
	def get_email(self):
		name = 'loginEmail'
		return self.find_element_by_name(name)

	def get_password(self):
		name = 'loginPassword'
		return self.find_element_by_name(name)

	def get_signin_and_forgot_pwd(self):
		e_parent = self.get_popup_ui()
		self.assertIsNotNone(e_parent)
		e_tage_name = 'tr'
		index = -4
		element, _ = self.get_element_child_by_tag_name(e_tage_name, index, e_parent)
		return element

	def get_signin_and_forgot_pwd_child(self, index=0):
		e_parent = self.get_signin_and_forgot_pwd()
		self.assertIsNotNone(e_parent)
		e_tage_name = 'a'
		element, _ = self.get_element_child_by_tag_name(e_tage_name, index, e_parent)
		return element

	def get_sign_in(self):
		index = 0
		return self.get_signin_and_forgot_pwd_child(index)

	def login(self, email, pwd):

		e_email = self.get_email()
		e_pwd = self.get_password()

		e_email.clear()
		e_email.send_keys(email)
		e_pwd.clear()
		e_pwd.send_keys(pwd)
		e_login = self.get_sign_in()

		return e_login

	def get_forgot_password(self):
		index = 1
		return self.get_signin_and_forgot_pwd_child(index)

	def get_third_part_login(self):
		e_class_name = 'loginSNS'
		return find_element_by_class_name(e_class_name)

	def get_third_part_login_child(self, index=0):
		e_parent = self.get_third_part_login()
		self.assertIsNotNone(e_parent)
		e_tage_name = 'a'
		element, _ = self.get_element_child_by_tag_name(e_tage_name, index, e_parent)
		return element

	def get_facebook(self):
		index = 0
		return self.get_third_part_login_child(index)

	def get_google(self):
		index = 1
		return self.get_third_part_login_child(index)

	#to get register area element
	def get_rg_table(self):
		e_parent = self.get_popup_ui()
		self.assertIsNotNone(e_parent)
		e_tage_name = 'table'
		index = 1 #second table
		element, _ = self.get_element_child_by_tag_name(e_tage_name, index, e_parent)
		return element

	def get_rg_table_child(self, e_tage_name='a', index=0):
		e_parent = self.get_rg_table()
		self.assertIsNotNone(e_parent)
		element, _ = self.get_element_child_by_tag_name(e_tage_name, index, e_parent)
		return element

	def get_rg_email(self):
		name = 'regEmail'
		return self.find_element_by_name(name)

	def get_rg_password(self):
		name = 'regPassword'
		return self.find_element_by_name(name)

	def get_rg_password_confirm(self):
		name = 'regPassword2'
		return self.find_element_by_name(name)

	def get_rg_name(self):
		name = 'regName'
		return self.find_element_by_name(name)

	
	def get_rg_newsletter(self):
		name = 'newsletter'
		return self.find_element_by_name(name)

	def get_rg_terms(self):
		name = 'terms'
		return self.find_element_by_name(name)

	def get_register(self):
		index = -1
		e_tage_name = 'a'
		return self.get_rg_table_child(e_tage_name, index)

	def get_terms_table(self):
		index = -1
		e_tage_name = 'table'
		return self.get_rg_table_child(e_tage_name, index)

	def get_terms_and_conditions(self):
		e_parent = self.get_terms_table()
		self.assertIsNotNone(e_parent)
		e_tage_name = 'a'
		element, _ = self.get_element_child_by_tag_name(e_tage_name, -1, e_parent)
		return element

	def get_newsletter_table(self):
		index = -2
		e_tage_name = 'table'
		return self.get_rg_table_child(e_tage_name, index)

	def get_learn_more(self):
		e_parent = self.get_newsletter_table()
		self.assertIsNotNone(e_parent)
		e_tage_name = 'a'
		element, _ = self.get_element_child_by_tag_name(e_tage_name, -1, e_parent)
		return element
