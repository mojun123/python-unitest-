from page.chrome_driver import ChromeDriver as cdriver

class CheckOut(cdriver):
	def __init__(self, driver=''):
		super(CheckOut, self).__init__()
		if driver:
			self.driver = driver 
	def assert_element_text(self, expected_attr, element):
		real_attr = element.text
		self.assertIn(expected_attr, real_attr)

	def get_ck_form(self):
		e_class_name = "ck-form"
		return self.find_element_by_class_name(e_class_name)

	def get_ck_form_child(self, index=0):
		e_parent = self.get_ck_form()
		if not e_parent:
			print(self.get_innerHTML(e_parent))
			raise Exception("[Error] cannot locate ck-form")

		e_tage_name = 'input'
		e_child = self.get_element_child_by_tag_name(e_tage_name, index, e_parent)

		return e_child

	def get_first_name(self):
		return self.get_ck_form_child()

	def get_input_value(self, element):
		return element.get_attribute('value').encode('utf-8').decode('utf-8')

	def assert_first_name(self, expected_attr='young'):
		element = self.get_first_name()
		print(self.get_outerHTML(element))
		real_attr = self.get_input_value(element)
		self.assertIn(expected_attr, real_attr)

	def get_last_name(self):
		index = 1
		return self.get_ck_form_child(index)

	def assert_last_name(self, expected_attr='yang'):
		element = self.get_last_name()
		print(self.get_outerHTML(element))
		real_attr = self.get_input_value(element)
		self.assertIn(expected_attr, real_attr)

	def get_street(self):
		e_id = 'map_shipping'
		return self.find_element_by_id(e_id)

	def assert_street(self, expected_attr='20 Fisher Creek Dr'):
		element = self.get_street()
		print(self.get_outerHTML(element))
		real_attr = self.get_input_value(element)
		self.assertIn(expected_attr, real_attr)

	def get_apartment_suite(self):
		index = 3
		return self.get_ck_form_child(index)

	def assert_apartment_suite(self, expected_attr=''):
		element = self.get_apartment_suite()
		print(self.get_outerHTML(element))
		real_attr = self.get_input_value(element)
		self.assertIn(expected_attr, real_attr)

	def get_city(self):
		index = 4
		return self.get_ck_form_child(index)

	def assert_city(self, expected_attr=''):
		element = self.get_city()
		print(self.get_outerHTML(element))
		real_attr = self.get_input_value(element)
		self.assertIn(expected_attr, real_attr)

	def get_state(self):
		e_class_name = 'select-container'
		return self.find_element_by_class_name(e_class_name)

	def assert_state(self, expected_attr='Florida'):
		real_attr = self.get_state().text
		self.assertIn(expected_attr, real_attr)

	def get_zip_code(self):
		index = -2
		return self.get_ck_form_child(index)

	def assert_zip_code(self, expected_attr='32327'):
		element = self.get_zip_code()
		print(self.get_outerHTML(element))
		real_attr = self.get_input_value(element)
		self.assertIn(expected_attr, real_attr)

	def get_phone(self):
		index = -1
		return self.get_ck_form_child(index)

	def assert_phone(self, expected_attr='4567894562'):
		element = self.get_phone()
		print(self.get_outerHTML(element))
		real_attr = self.get_input_value(element)
		self.assertIn(expected_attr, real_attr)

	def get_ck_rs_content(self):
		e_class_name = "ck-rs-content"
		return self.find_element_by_class_name(e_class_name)

	def get_ck_rs_content_item(self, index=0):
		e_parent = self.get_ck_rs_content()
		if not e_parent:
			print(self.get_innerHTML(e_parent))
			raise Exception("[Error] cannot locate ck-rs-content")

		e_class_name = 'ck-rs-part'
		e_child = self.get_element_child_by_class_name(e_class_name, index, e_parent)

		return e_child


	def get_ck_rs_part_for_product_infos(self):

		return self.get_ck_rs_content_item()

	def get_ck_rs_part_for_total_infos(self):
		index = -1
		return self.get_ck_rs_content_item(index)

	def get_ck_rs_part_child(self, index=0):
		e_parent = self.get_ck_rs_part_for_product_infos()
		if not e_parent:
			print(self.get_innerHTML(e_parent))
			raise Exception("[Error] cannot locate ck-form")

		e_class_name = 'ck-rs-item'
		e_child = self.get_element_child_by_class_name(e_class_name, index, e_parent)

		return e_child

	def get_ck_rs_item_child(self, index=0):
		'''
		@param:
			0 - title
			1 - desc
			2 - price
		'''
		e_first_ck_rs_item = self.get_ck_rs_part_child()
		if not e_first_ck_rs_item:
			print(self.get_innerHTML(e_first_ck_rs_item))
			raise Exception("[Error] cannot locate ck-form")

		e_tage_name = 'span'
		e_child = self.get_element_child_by_tag_name(e_tage_name, index, e_first_ck_rs_item)

		return e_child


	def assert_ck_rs_text(self, expected_attr, element):
		print(self.get_outerHTML(element))
		real_attr = element.text
		self.assertIn(expected_attr, real_attr)

	def assert_ck_rs_desc(self, expected_attr, element):
		real_attr = element.text
		self.assertIn(expected_attr, real_attr)

	def assert_ck_rs_col_price(self, expected_attr, element):
		print(self.get_outerHTML(element))
		real_attr = element.text
		self.assertIn(expected_attr, real_attr)

	def get_ck_coupon_input(self):
		e_class_name = 'ck-coupon-input'
		return self.find_element_by_class_name(e_class_name)

	def get_ck_coupon_apply(self):
		e_class_name = 'ck-coupon-apply'
		return self.find_element_by_class_name(e_class_name)

	def get_ck_rs_item_total_child(self, index=0):
		e_parent = self.get_ck_rs_part_for_total_infos()
		if not e_parent:
			print(self.get_innerHTML(e_parent))
			raise Exception("[Error] cannot locate ck-form")

		e_tage_name = 'span'
		e_child = self.get_element_child_by_tag_name(e_tage_name, index, e_parent)

		return e_child, e_parent

	def get_subtotal_price(self):
		index = 1
		return self.get_ck_rs_item_total_child(index)

	def assert_subotal_price(self, expected_attr):
		element, _ = self.get_subtotal_price()
		self.assert_element_text(expected_attr, element)

	def get_shipping_cost(self):
		index = 3
		return self.get_ck_rs_item_total_child(index)

	def assert_shipping_cost(self, expected_attr):
		element, _ = self.get_shipping_cost()
		self.assert_element_text(expected_attr, element)

	def get_distcount(self):
		index = 5
		return self.get_ck_rs_item_total_child(index)

	def assert_distcount(self, expected_attr):
		element, _ = self.get_distcount()
		print('disc: ', self.get_outerHTML(element))
		self.assert_element_text(expected_attr, element)

	def assert_distcount_style(self, expected_attr='display', reverse=False):
		element, _ = self.get_distcount()
		print('display: ', self.get_outerHTML(element))
		e_parent = self.get_element_parent(element)

		real_attr = e_parent.get_attribute('style')
		self.assertInOrNotIn(expected_attr, real_attr, reverse=False)


	def get_total(self):
		index = -1
		return self.get_ck_rs_item_total_child(index)

	def assert_total(self, expected_attr):
		element, _ = self.get_total()
		self.assert_element_text(expected_attr, element)

	def get_continue_to_payment_btn(self):
		e_class_name = 'btn'
		return self.find_element_by_class_name(e_class_name)

	def assert_continue_to_payment_status(self, expected_attr='true'):
		element = self.get_continue_to_payment_btn()
		real_attr = element.get_attribute('disabled')
		if not real_attr:

			self.assertNotEqual(expected_attr, real_attr)
		else:
			self.assertNotIn(expected_attr, real_attr)

	def get_summary_title(self):
		e_class_name = 'ck-rs-title'
		return self.find_element_by_class_name(e_class_name)


	def check_page_loading_finished(self):
		'''
		use to judge checkout page loading finished
		'''
		e_class_name = 'ck-rs-title'
		expected_attr = 'Summary'
		return self.text_to_be_present_in_element_by_class_name(e_class_name, expected_attr)

	def get_ck_step_address(self):
		e_class_name = 'ck-step-address'
		return self.find_element_by_class_name(e_class_name)

	def get_continue_to_payment_btn_new(self):
		e_parent = self.get_ck_step_address()
		e_tage_name = 'button'
		return self.get_element_child_by_tag_name(e_tage_name, -1, e_parent)

	def get_credit_radio(self):
		e_id = 'pay1'
		return self.element_to_be_clickable_by_id(e_id)
