from page.base import BasePage

class ViewCart(BasePage):

	def open(self):
		self._open(self.base_url, self.page_title)

	def check_product_unit_price(self, expected_attr):
		xpath = '//*[@id="4"]/div[3]'
		real_attr = self.expected_wait_located_by_xpath(xpath, attr="text")
		# self.assert_in_element_attribute(real_attr, expected_attr)
		# self.assert_element_attribute(real_attr, expected_attr)
		return real_attr

	def check_product_qty(self, expected_attr):
		xpath = '//*[@id="4"]/div[5]/table/tbody/tr/td/select'
		real_attr = self.get_selected_option_by_xpath(xpath)
		# self.assert_element_attribute(real_attr, expected_attr)
		return real_attr

	def check_product_subtotal(self, expected_attr):
		xpath = '//*[@id="4"]/div[6]'
		real_attr = self.expected_wait_located_by_xpath(xpath, attr="text")
		# self.assert_in_element_attribute(real_attr, expected_attr)
		# self.assert_element_attribute(real_attr, expected_attr)
		return real_attr

	# def check_cart_subtotal(self, expected_attr):
	# 	xpath = '//*[@id="viewcart-subtotal"]/div[1]'
	# 	real_attr = self.expected_wait_located_by_xpath(xpath, attr="text")
	# 	self.assert_in_element_attribute(real_attr, expected_attr)
	def check_checkout_button(self):

		xpath = '//*[@id="viewcart-subtotal"]/a/div'
		element = self.expected_wait_located_by_xpath(xpath)
		# self.assertNotNone_element_attribute(element)
		return element

	def check_paypal_express(self):

		xpath = '//*[@id="viewcart-subtotal"]/p[1]/a/img'
		element = self.expected_wait_located_by_xpath(xpath)
		# self.assertNotNone_element_attribute(element)

		return element

	def check_empty_cart(self):
		element_id = "cart-empty"
		element = self.expected_wait_located_by_id(element_id)
		if not element:
			return None
		attr = element.get_attribute('style')
		if attr:
			#if have style: display:block, then cart is empty
			print("id=cart-empty style: ",attr)
			return True
		else:
			print("id=cart-empty style: ",attr)
			return False

	def get_cart_first_sku(self):
		b_empty = self.check_empty_cart()
		element_class_name = "cart-rows"
		element = self.expected_wait_located_by_class(element_class_name)

		if not element:
			return b_empty, None
		if not b_empty:
			try:
				
				cart_col_tag_name = "div"
				cart_col_tag_element = self.expected_wait_located_by_tag(cart_col_tag_name, element)
				return b_empty, cart_col_tag_element

			except Exception as e:
				print("it should find some sku")
		else:
			return b_empty, None

	def is_empty_cart(self):


		element_class_name = "cart-rows"
		element = self.expected_wait_located_by_class(element_class_name)

		if not element:
			return None
		try:
			cart_col_tag_name = "div"
			cart_col_tag_element = self.expected_wait_located_by_tag(cart_col_tag_name, element)
			print("locate cart-rows div")
			print(cart_col_tag_element.get_attribute('innerHTML'))
			# print(2222222222222)
			# print(cart_col_tag_element.get_attribute('outerHTML'))
			# print(333333333333333)


			# if cart_col_tag_element.get_attribute('style'):
			# 	print("rm first product")
			# 	return True
			return False, cart_col_tag_element
		except Exception as e:
			print("cannot locate cart-rows div ")
			return True, None
		

	def del_first_product(self, element):
		if not element:
			print("param is none")
		element_class_name = "del-btn"
		element_del = self.expected_wait_located_by_class(element_class_name, element)

		# element.click()
		return element_del

