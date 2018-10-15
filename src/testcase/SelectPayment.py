from page.chrome_driver import ChromeDriver as cdriver

class SelectPayment(cdriver):

	def __init__(self, driver=''):
		super(SelectPayment, self).__init__()
		if driver:
			self.driver = driver

	def assert_element_text(self, expected_attr, element):
		real_attr = element.text
		self.assertIn(expected_attr, real_attr)

	def assert_element_style(self, expected_attr='display: none;', element='', reverse=False):
		element = element or self.driver
		
		real_attr = element.get_attribute('style')
		self.assertEqOrNotEqual(expected_attr, real_attr, reverse=reverse)

	def assert_element_radio(self, expected_attr, element, reverse=False):
		real_attr = element.is_selected()
		print(real_attr)
		self.assertEqOrNotEqual(expected_attr, real_attr, reverse=reverse)

	def get_ck_pay_list(self):
		e_class_name = "ck-pay-list"
		return self.find_element_by_class_name(e_class_name)

	def get_ck_pay_list_item(self, index=0):
		e_parent = self.get_ck_pay_list()
		if not e_parent:
			print(self.get_innerHTML(e_parent))
			raise Exception("[Error] cannot locate ck-form")

		e_tage_name = 'li'
		e_child = self.get_element_child_by_tag_name(e_tage_name, index, e_parent)

		return e_child

	def get_credit_card(self):
		return self.get_ck_pay_list_item()

	def get_paypal(self):
		index = 1
		return self.get_ck_pay_list_item(index)

	def get_ck_credit(self):
		e_class_name = 'ck-credit'
		return self.find_element_by_class_name(e_class_name)

	def check_ck_credit(self, expected_attr='display: none;', reverse=False):
		element = self.get_ck_credit()
		self.assert_element_style(expected_attr, element, reverse)

	def get_ck_pay_link(self):
		e_class_name = 'ck-pay-link'
		return self.find_element_by_class_name(e_class_name)

	def check_ck_pay_list(self, expected_attr='display: none;', reverse=False):
		element = self.get_ck_pay_link()
		self.assert_element_style(expected_attr, element, reverse)

	def get_paypal_btn(self):
		e_parent = self.get_ck_pay_link()
		e_tage_name = 'button'
		return self.get_element_child_by_tag_name(e_tage_name, 0, e_parent)

	def get_credit_cardnumber_iframe(self):
		name = '__privateStripeFrame3'
		self.frame_to_be_available_and_switch_to_it_by_name(name)

	def get_credit_exp_date_iframe(self):
		name = '__privateStripeFrame4'
		self.frame_to_be_available_and_switch_to_it_by_name(name)

	def get_credit_cvc_iframe(self):
		name = '__privateStripeFrame5'
		self.frame_to_be_available_and_switch_to_it_by_name(name)
		

	def get_credit_cardnumber(self):
		self.get_credit_cardnumber_iframe()
		print(self.get_innerHTML(self.driver))
		name = 'cardnumber'
		return self.find_element_by_name(name)

	def get_credit_exp_date(self):
		self.get_credit_exp_date_iframe()
		name = 'exp-date'
		return self.find_element_by_name(name)

	def get_credit_cvs(self):
		self.get_credit_cvc_iframe()
		name = 'cvc'
		return self.find_element_by_name(name)

	def fill_in_credit_card_info(self, cardnumber, exp_date, cvc, common_page):
		e_card_number = self.get_credit_cardnumber()
		self.assertIsNotNone(e_card_number)
		e_card_number.clear()
		e_card_number.send_keys(cardnumber)
		self.switch_to_default_content()

		e_exp_date = self.get_credit_exp_date()
		self.assertIsNotNone(e_exp_date)
		e_exp_date.clear()
		e_exp_date.send_keys(exp_date)
		self.switch_to_default_content()

		e_cvc = self.get_credit_cvs()
		self.assertIsNotNone(e_cvc)
		e_cvc.clear()
		e_cvc.send_keys(cvc)

		self.switch_to_default_content()
		e_summary = common_page.get_summary_title()
		self.assertIsNotNone(e_summary)
		self.scroll_to_element(e_summary)
		# e_summary.click() # to blur cvc input element and enabled pay btn

	def get_using_shipping_address_checkbox(self):
		e_id = 'remember'
		return self.find_element_by_id(e_id)

	def check_using_shipping_address_checked(self, expected_attr=True):
		element = self.get_using_shipping_address_checkbox()
		b_selected = element.is_selected()
		self.assertEqual(expected_attr, b_selected)

	def get_credit_cart_btn(self):
		e_id = 'card-element-pay'
		return self.find_element_by_id(e_id)

	def check_credit_cart_btn_status(self, expected_attr=False):
		element = self.get_credit_cart_btn()
		real_attr = element.is_enabled()
		self.assertEqual(expected_attr, real_attr)


	def get_ck_billing(self):
		e_class_name = 'ck-billing'
		return self.find_element_by_class_name(e_class_name)

	def get_ck_billing_form(self):
		e_parent = self.get_ck_billing()
		e_tage_name = 'div'
		return self.get_element_child_by_tag_name(e_tage_name, -1, e_parent)

	def get_credit_radio(self):
		e_id = 'pay1'
		return self.element_to_be_clickable_by_id(e_id)

	def get_paypal_radio(self):
		e_id = 'pay2'
		return self.element_to_be_clickable_by_id(e_id)

	def check_credit_redio_status(self):
		expected_attr = False
		element = self.get_credit_radio()
		self.assert_element_radio(expected_attr, element)

	def check_paypal_redio_status(self):
		expected_attr = False
		element = self.get_paypal_radio()
		self.assert_element_radio(expected_attr, element)






