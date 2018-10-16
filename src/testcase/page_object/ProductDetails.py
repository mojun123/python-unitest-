from page.base import BasePage

class ProductDetails(BasePage):



	def open(self):
		self._open(self.base_url, self.page_title)

	def check_top_add_to_cart_button(self):
		xpath = '//*[@id="productApp"]/div/section[1]/div[3]/div/button[1]'
		element = self.expected_wait_clickable_by_xpath(element_id)
		return element 
		# print(element, element.get_attribute("value"))
	def check_next_add_to_cart_button(self):
		xpath = '//*[@id="productApp"]/div/section[4]/div[3]/button[1]'
		element = self.expected_wait_clickable_by_xpath(element_id)
		return element 

	def check_cart(self):
		element_id = 'cartApp'
		element = self.expected_wait_located_by_id(element_id)
		return element

	def check_checkout(self):
		xpath = '//*[@id="cartApp"]/div[2]/div[3]/div[1]/button'
		element = self.expected_wait_clickable_by_xpath(element_id)
		return element

	

	

		

		 

