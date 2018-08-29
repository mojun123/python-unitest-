from page.base import BasePage

class Home(BasePage):

	def open(self):
		self._open(self.base_url, self.page_title)

	def check_slider(self):
		
		element_id = "slides"
		element = self.expected_wait_located_by_id(element_id)
		return element

	def check_sign(self):
		
		element_id = "signin"
		element = self.expected_wait_clickable_by_id(element_id)
		return element

	def check_viewcart_button(self):
		
		element_id = "checkout-btn"
		element = self.expected_wait_clickable_by_id(element_id)
		return element

	def check_chat_now_button(self):
		
		element_class = "mylivechat_collapsed_text"
		element = self.expected_wait_located_by_class(element_class)
		return element

	def check_products(self):
		
		element_class = "index-glist"
		element = self.expected_wait_located_by_class(element_class)
		return element
	
		
		
	
		