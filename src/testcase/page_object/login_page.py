from page.chrome_driver import ChromeDriver as cdriver
 
class Login(cdriver):
	def _init_(self,driver=""):
		super(Login,self).__init__()
		if driver:
			self.driver = driver

	
    #newcustomer
	def get_login_address(self):
		e_name = 'regEmail'
		return self.find_element_by_name(e_name)

	def get_login_emailpassword(self):
		e_name = 'regPassword'
		return self.find_element_by_name(e_name)

	def get_login_confirmpassword(self):
		e_name = 'regPassword2'
		return self.find_element_by_name(e_name)

	def get_login_name(self):
		e_name = 'regName'
		return self.find_element_by_name(e_name)

	def get_login_newsletter(self):
		e_id = 'newsletter'
		return self.find_element_by_id(e_id)

	def get_login_border(self):
		e_id = 'popup-login-border'
		return self.find_element_by_id(e_id)

	def get_login_table(self):
		e_parent = self.get_login_border()
		self.asserIsNotNone(e_parent)
		e_tage_name = 'table'
		element,_ = self.get_element_child_by_tag_name(e_tage_name, 2, e_parent)
		return element
     
	def get_login_td(self):
		e_parent = self.get_login_table()
		self.asserIsNotNone(e_parent)
		e_tage_name = 'td'
		element,_ = self.get_element_child_by_tag_name(e_tage_name, 1, e_parent)
		return element

	def get_login_learn(self):
		e_parent = self.get_login_td()
		self.asserIsNotNone(e_parent)
		e_tage_name = 'a'
		element,_ = self.get_element_child_by_tag_name(e_tage_name, 0, e_parent)
		return element	

	def get_login_aggres(self):
		e_id = 'terms'	
		return self.find_element_by_id(e_id)
    
	def get_login_tr(self):
		e_parent = self.get_login_border()
		self.asserIsNotNone(e_parent)
		e_tage_name = 'tr'
		element,_ = self.get_element_child_by_tag_name(e_tage_name, 9, e_parent)
		return element

	def get_login_td(self):
		e_parent = self.get_login_tr()
		self.asserIsNotNone(e_parent)
		e_tage_name = 'td'
		element,_ = self.get_element_child_by_tag_name(e_tage_name, 1, e_parent)
		return element

	def get_login_terms(self):
		e_parent = self.get_login_td()    
		self.asserIsNotNone(e_parent)
		e_tage_name = 'a'
		element,_ = self.get_element_child_by_tag_name(e_tage_name, 0, e_parent)
		return element 

	def get_login_try(self):
		e_parent = self.get_login_border()
		self.asserIsNotNone(e_parent)
		e_tage_name = 'tr'
		element,_ = self.get_element_child_by_tag_name(e_tage_name, 9, e_parent)
		return element

	def get_login_tdy(self):
		e_parent = self.get_login_try()
		self.asserIsNotNone(e_parent)
		e_tage_name = 'td'
		element,_ = self.get_element_child_by_tag_name(e_tage_name, 1, e_parent)
		return element

	def get_login_register(self):
		e_parent = self.get_login_tdy()    
		self.asserIsNotNone(e_parent)
		e_tage_name = 'a'
		element,_ = self.get_element_child_by_tag_name(e_tage_name, 0, e_parent)
		return element 

	def get_login_loginemail(self):    
		e_name = 'loginEmail'
		return self.find_element_by_name(e_name)

	def get_login_passworld(self):
		e_name = 'loginPassworld'
		return self.find_element_by_name(e_name)
    
	def get_login_sig(self):
		e_parent = self.get_login_border()
		self.asserIsNotNone(e_parent)
		e_tage_name = 'tr'
		elment,_ = self.get_element_child_by_tag_name(e_tage_name, 6, e_parent)
		return element

	def get_login_sigi(self):
		e_parent = self.get_login_sig()
		self.asserIsNotNone(e_parent)
		e_tage_name = 'td'
		element,_ = self.get_element_child_by_tag_name(e_tage_name, 1, e_parent)
		return element
     
	def get_login_sigin(self):
		e_parent = self.get_login_sigi()
		self.asserIsNotNone(e_parent)
		e_tage_name = 'a'
		element,_ = self.get_element_child_by_tag_name(e_tage_name, 0, e_parent)
		return element
    
	def get_login_click(self):
		e_parent = self.get_login_sigi()
		self.asserIsNotNone(e_parent)
		e_tage_name = 'p'
		element,_ = self.get_element_child_by_tag_name(e_tage_name, 0, e_parent)
		return element

	def get_login_clickhere(self):
		e_parent = self.get_login_click()
		self.asserIsNotNone(e_parent)
		e_tage_name = 'a'
		element,_ = self.get_element_child_by_tag_name()
		return element
   
	def get_login_facebook(self):
		e_class_name = 'fa fa-facebook login-facebook'
		return self.find_elemnt_by_class_name(e_class_name)

	def get_login_facebook(self):
		e_class_name = 'fa fa-google-plus login-google'
		return self.find_elemnt_by_class_name(e_class_name)

  
     