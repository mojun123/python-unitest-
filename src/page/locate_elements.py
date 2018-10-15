from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import os
import sys

sys.path.append(os.path.dirname(os.getcwd()))

from page.browser_logs import BrowserLogs



class LocateElements(BrowserLogs):

	def alert_is_present(self, driver=None, timeout=30):
		try:
			element = WebDriverWait(self.driver, wait_time).until(
				EC.alert_is_present());
			return element
		except Exception as e:
			return False



	def title_is(self, title, driver=None, timeout=30):
		'''
		An expectation for checking the title of a page.
		title is the expected title, 
		which must be an exact match returns True if the title matches, false otherwise.
		'''
		try:
			element = WebDriverWait(self.driver, wait_time).until(
				EC.title_is(title));
			return element
		except Exception as e:
			return False
 

	def title_contains(self, title, driver=None, timeout=30):
		'''
		An expectation for checking that the title contains a case-sensitive substring. 
		title is the fragment of title expected returns True when the title matches, False otherwise
		'''
		try:
			element = WebDriverWait(self.driver, wait_time).until(
				EC.title_contains(title));
			return element
		except Exception as e:
			return False

	def presence_of_element_located(self, by, arg, driver=None, timeout=30):
		'''
		An expectation for checking that an element is present on the DOM of a page. 
		This does not necessarily mean that the element is visible. 
		locator - used to find the element returns the WebElement once it is located
		@param:
			(by, arg) -- locator
			locator is tuple, as follow:
				(By.CLASS_NAME, class name)
				(By.CSS_SELECTOR, css selector)
				(By.ID, id)
				(By.LINK_TEXT, link text)
				(By.NAME, name)
				(By.PARTIAL_LINK_TEXT, partial link text)
				(By.TAG_NAME, tag name)
				(By.XPATH, xpath)

		'''

		driver = driver or self.driver
		try:

			element = WebDriverWait(driver, timeout).until(
				EC.presence_of_element_located((by, arg)))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def presence_of_all_elements_located(self, by, arg, driver=None, timeout=30):
		'''
		An expectation for checking that there is at least one element present on a web page. 
		locator is used to find the element returns the list of WebElements once they are located
		@param:
			(by, arg) -- locator
			locator is tuple, as follow:
				(By.CLASS_NAME, class name)
				(By.CSS_SELECTOR, css selector)
				(By.ID, id)
				(By.LINK_TEXT, link text)
				(By.NAME, name)
				(By.PARTIAL_LINK_TEXT, partial link text)
				(By.TAG_NAME, tag name)
				(By.XPATH, xpath)

		'''

		driver = driver or self.driver
		try:

			element = WebDriverWait(driver, timeout).until(
				EC.presence_of_all_elements_located((by, arg)))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None
			
	def visibility_of_element_located(self, by, arg, driver=None, visibiliy=True, timeout=30):
		'''
		An expectation for checking that an element is present on the DOM of a page and visible. 
		Visibility means that the element is not only displayed but also has a height and width that is greater than 0. 
		locator - used to find the element returns the WebElement once it is located and visible
		@param
			(by, arg) -- locator
			locator is tuple, as follow:
				(By.CLASS_NAME, class name)
				(By.CSS_SELECTOR, css selector)
				(By.ID, id)
				(By.LINK_TEXT, link text)
				(By.NAME, name)
				(By.PARTIAL_LINK_TEXT, partial link text)
				(By.TAG_NAME, tag name)
				(By.XPATH, xpath)
		'''
		driver = driver or self.driver
		element = None
		try:
			if visibiliy:
				element = WebDriverWait(driver, timeout).until(
					EC.visibility_of_element_located((by, arg)))
			else:
				element = WebDriverWait(driver, timeout).until(
					EC.invisibility_of_element_located((by, arg)))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None
		# except KeyError:
		# except TimeoutException:
		 
	def visibility_of(self, by, arg, driver=None, visibiliy=True, timeout=30):
		'''
		An expectation for checking that an element, known to be present on the DOM of a page, is visible.
		Visibility means that the element is not only displayed but also has a height and width that is greater than 0. 
		element is the WebElement returns the (same) WebElement once it is visible
		@param
			(by, arg) -- locator
			locator is tuple, as follow:
				(By.CLASS_NAME, class name)
				(By.CSS_SELECTOR, css selector)
				(By.ID, id)
				(By.LINK_TEXT, link text)
				(By.NAME, name)
				(By.PARTIAL_LINK_TEXT, partial link text)
				(By.TAG_NAME, tag name)
				(By.XPATH, xpath)
		'''
		driver = driver or self.driver
		element = None
		try:
			if visibiliy:
				element = WebDriverWait(driver, timeout).until(
					EC.visibility_of((by, arg)))
			else:
				element = WebDriverWait(driver, timeout).until(
					EC.invisibility_of_element((by, arg)))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def visibility_of_any_elements_located(self, by, arg, driver=None, timeout=30):
		'''
		An expectation for checking that there is at least one element visible on a web page.
		locator is used to find the element returns the list of WebElements once they are located
		@param
			(by, arg) -- locator
			locator is tuple, as follow:
				(By.CLASS_NAME, class name)
				(By.CSS_SELECTOR, css selector)
				(By.ID, id)
				(By.LINK_TEXT, link text)
				(By.NAME, name)
				(By.PARTIAL_LINK_TEXT, partial link text)
				(By.TAG_NAME, tag name)
				(By.XPATH, xpath)
		'''
		driver = driver or self.driver
		
		try:
			
			element = WebDriverWait(driver, timeout).until(
				EC.visibility_of_any_elements_located((by, arg)))
			
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def visibility_of_all_elements_located(self, by, arg, driver=None, timeout=30):
		'''
		An expectation for checking that all elements are present on the DOM of a page and visible. 
		Visibility means that the elements are not only displayed but also has a height and width that is greater than 0. 
		locator - used to find the elements returns the list of WebElements once they are located and visible
		@param
			(by, arg) -- locator
			locator is tuple, as follow:
				(By.CLASS_NAME, class name)
				(By.CSS_SELECTOR, css selector)
				(By.ID, id)
				(By.LINK_TEXT, link text)
				(By.NAME, name)
				(By.PARTIAL_LINK_TEXT, partial link text)
				(By.TAG_NAME, tag name)
				(By.XPATH, xpath)
		'''
		driver = driver or self.driver
		
		try:
			
			element = WebDriverWait(driver, timeout).until(
				EC.visibility_of_all_elements_located((by, arg)))
			
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def text_to_be_present_in_element(self, by, arg, text_, driver=None, timeout=30):
		'''
		An expectation for checking if the given text is present in the specified element. locator, text
		@param:
			(by, arg) -- locator
			locator is tuple, as follow:
				(By.CLASS_NAME, class name)
				(By.CSS_SELECTOR, css selector)
				(By.ID, id)
				(By.LINK_TEXT, link text)
				(By.NAME, name)
				(By.PARTIAL_LINK_TEXT, partial link text)
				(By.TAG_NAME, tag name)
				(By.XPATH, xpath)

		'''

		driver = driver or self.driver
		try:

			element = WebDriverWait(driver, timeout).until(
				EC.text_to_be_present_in_element((by, arg), text_))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def text_to_be_present_in_element_value(self, by, arg, text_, driver=None, timeout=30):
		'''
		An expectation for checking if the given text is present in the specified element. locator, text
		@param:
			(by, arg) -- locator
			locator is tuple, as follow:
				(By.CLASS_NAME, class name)
				(By.CSS_SELECTOR, css selector)
				(By.ID, id)
				(By.LINK_TEXT, link text)
				(By.NAME, name)
				(By.PARTIAL_LINK_TEXT, partial link text)
				(By.TAG_NAME, tag name)
				(By.XPATH, xpath)

		'''

		driver = driver or self.driver
		try:

			element = WebDriverWait(driver, timeout).until(
				EC.text_to_be_present_in_element_value((by, arg), text_))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def url_changes(self, url, timeout=30):
		'''
		An expectation for checking the current url. url is the expected url, 
		which must not be an exact match returns True if the url is different, false otherwise.
		'''
		try:

			element = WebDriverWait(self.driver, timeout).until(
				EC.url_changes(url))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def url_contains(self, url, timeout=30):
		'''
		An expectation for checking that the current url contains a case-sensitive substring. 
		url is the fragment of url expected, returns True when the url matches, False otherwise
		'''
		try:

			element = WebDriverWait(self.driver, timeout).until(
				EC.url_contains(url))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def url_matches(self, url, timeout=30):
		'''
		An expectation for checking the current url. pattern is the expected pattern, 
		which must be an exact match returns True if the url matches, false otherwise.
		'''
		try:

			element = WebDriverWait(self.driver, timeout).until(
				EC.url_matches(url))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def url_to_be(self, url, timeout=30):
		'''
		An expectation for checking the current url. 
		url is the expected url, which must be an exact match returns True if the url matches, false otherwise.
		'''
		try:

			element = WebDriverWait(self.driver, timeout).until(
				EC.url_to_be(url))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def element_to_be_clickable(self, by, arg, driver=None, timeout=30):
		'''
		An Expectation for checking an element is visible and enabled such that you can click it.
		@param:
			(by, arg) -- locator
			locator is tuple, as follow:
				(By.CLASS_NAME, class name)
				(By.CSS_SELECTOR, css selector)
				(By.ID, id)
				(By.LINK_TEXT, link text)
				(By.NAME, name)
				(By.PARTIAL_LINK_TEXT, partial link text)
				(By.TAG_NAME, tag name)
				(By.XPATH, xpath)

		'''

		driver = driver or self.driver
		try:

			element = WebDriverWait(driver, timeout).until(
				EC.element_to_be_clickable((by, arg)))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def element_located_to_be_selected(self, by, arg, driver=None, timeout=30):
		'''
		An expectation for the element to be located is selected. locator is a tuple of (by, path)
		@param:
			(by, arg) -- locator
			locator is tuple, as follow:
				(By.CLASS_NAME, class name)
				(By.CSS_SELECTOR, css selector)
				(By.ID, id)
				(By.LINK_TEXT, link text)
				(By.NAME, name)
				(By.PARTIAL_LINK_TEXT, partial link text)
				(By.TAG_NAME, tag name)
				(By.XPATH, xpath)

		'''

		driver = driver or self.driver
		try:

			element = WebDriverWait(driver, timeout).until(
				EC.element_located_to_be_selected((by, arg)))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def element_selection_state_to_be(self, element, is_selected, driver=None, timeout=30):
		'''
		An expectation for checking if the given element is selected. 
		element is WebElement object is_selected is a Boolean.”
		@param:
			(by, arg) -- locator
			locator is tuple, as follow:
				(By.CLASS_NAME, class name)
				(By.CSS_SELECTOR, css selector)
				(By.ID, id)
				(By.LINK_TEXT, link text)
				(By.NAME, name)
				(By.PARTIAL_LINK_TEXT, partial link text)
				(By.TAG_NAME, tag name)
				(By.XPATH, xpath)

		'''

		driver = driver or self.driver
		try:

			element = WebDriverWait(driver, timeout).until(
				EC.element_selection_state_to_be(element, is_selected))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def element_located_selection_state_to_be(self, by, arg, is_selected, driver=None, timeout=30):
		'''
		An expectation to locate an element and check if the selection state specified is in that state. 
		locator is a tuple of (by, path) is_selected is a boolean
		@param:
			(by, arg) -- locator
			locator is tuple, as follow:
				(By.CLASS_NAME, class name)
				(By.CSS_SELECTOR, css selector)
				(By.ID, id)
				(By.LINK_TEXT, link text)
				(By.NAME, name)
				(By.PARTIAL_LINK_TEXT, partial link text)
				(By.TAG_NAME, tag name)
				(By.XPATH, xpath)

		'''

		driver = driver or self.driver
		try:

			element = WebDriverWait(driver, timeout).until(
				EC.element_located_selection_state_to_be((by, arg), is_selected))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def element_to_be_selected(self, element, driver=None, timeout=30):
		'''
		An expectation for checking the selection is selected. element is WebElement object
		'''

		driver = driver or self.driver
		try:

			element = WebDriverWait(driver, timeout).until(
				EC.element_to_be_selected(element))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def frame_to_be_available_and_switch_to_it(self, by, arg, driver=None, timeout=30):
		'''
		An expectation for checking whether the given frame is available to switch to. 
		If the frame is available it switches the given driver to the specified frame.
		@param:
			(by, arg) -- locator
			locator is tuple, as follow:
				(By.CLASS_NAME, class name)
				(By.CSS_SELECTOR, css selector)
				(By.ID, id)
				(By.LINK_TEXT, link text)
				(By.NAME, name)
				(By.PARTIAL_LINK_TEXT, partial link text)
				(By.TAG_NAME, tag name)
				(By.XPATH, xpath)

		'''

		driver = driver or self.driver
		try:

			element = WebDriverWait(driver, timeout).until(
				EC.frame_to_be_available_and_switch_to_it((by, arg)))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def staleness_of(self, element, driver=None, timeout=30):
		'''
		Wait until an element is no longer attached to the DOM. element is the element to wait for. 
		returns False if the element is still attached to the DOM, true otherwise.
		'''

		driver = driver or self.driver
		try:

			element = WebDriverWait(driver, timeout).until(
				EC.staleness_of(element))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def new_window_is_opened(self, current_handles, driver=None, timeout=30):
		'''
		An expectation that a new window will be opened and have the number of windows handles increase
		'''

		driver = driver or self.driver
		try:

			element = WebDriverWait(driver, timeout).until(
				EC.new_window_is_opened(current_handles))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def number_of_windows_to_be(self, num_windows, driver=None, timeout=30):
		'''
		An expectation for the number of windows to be a certain value.
		'''

		driver = driver or self.driver
		try:

			element = WebDriverWait(driver, timeout).until(
				EC.number_of_windows_to_be(num_windows))
			return element

		except Exception as e:
			# print("wait_for_element timeout: ")
			print(str(e))
			return None

	def find_element(self, by, arg, driver=None, timeout=30):
		'''
		find element by locator.
		@param:
			by, arg -- locator
			locator is tuple, as follow:
				By.CLASS_NAME, class name
				By.CSS_SELECTOR, css selector
				By.ID, id
				By.LINK_TEXT, link text
				By.NAME, name
				By.PARTIAL_LINK_TEXT, partial link text
				By.TAG_NAME, tag name
				By.XPATH, xpath

		'''

		driver = driver or self.driver
		try:
			# self.visibility_of_element_located(by, arg, driver, True, timeout)
			element = WebDriverWait(driver, timeout).until(
				lambda driver: driver.find_element(by, arg))
			return element

		except Exception as e:
			print(str(e))
			# print("wait_for_element timeout: {}".format(arg))
			return None

	def find_elements(self, by, arg, driver=None, timeout=30):
		'''
		find element by locator.
		@param:
			by, arg -- locator
			locator is tuple, as follow:
				By.CLASS_NAME, class name
				By.CSS_SELECTOR, css selector
				By.ID, id
				By.LINK_TEXT, link text
				By.NAME, name
				By.PARTIAL_LINK_TEXT, partial link text
				By.TAG_NAME, tag name
				By.XPATH, xpath

		'''

		driver = driver or self.driver
		try:
			# element = self.presence_of_element_located(by, arg, driver, timeout)
			element = WebDriverWait(driver, timeout).until(
				lambda driver: driver.find_elements(by, arg))
			return element

		except Exception as e:
			print(str(e))
			# print("wait_for_element timeout: {}".format(arg))
			return None

	def find_element_by_id(self, e_id, driver=None, timeout=30):
		return self.find_element(By.ID, e_id, driver, timeout)

	def find_element_by_name(self, e_name, driver=None, timeout=30):
		return self.find_element(By.NAME, e_name, driver, timeout)

	def find_element_by_xpath(self, e_xpath, driver=None, timeout=30):
		return self.find_element(By.XPATH, e_xpath, driver, timeout)

	def find_element_by_link_text(self, e_link_text, driver=None, timeout=30):
		return self.find_element(By.LINK_TEXT, e_link_text, driver, timeout)

	def find_element_by_partial_link_text(self, e_partial_link_text, driver=None, timeout=30):
		return self.find_element(By.PARTIAL_LINK_TEXT, e_partial_link_text, driver, timeout)

	def find_element_by_tag_name(self, e_tag_name, driver=None, timeout=30):
		return self.find_element(By.TAG_NAME, e_tag_name, driver, timeout)

	def find_element_by_class_name(self, e_class_name, driver=None, timeout=30):
		return self.find_element(By.CLASS_NAME, e_class_name, driver, timeout)

	def find_element_by_css_selector(self, e_css_selector, driver=None, timeout=30):
		return self.find_element(By.CSS_SELECTOR, e_css_selector, driver, timeout)

	def find_elements_by_name(self, e_name, driver=None, timeout=30):
		return self.find_elements(By.NAME, e_name, driver, timeout)

	def find_elements_by_xpath(self, e_xpath, driver=None, timeout=30):
		return self.find_elements(By.XPATH, e_xpath, driver, timeout)

	def find_elements_by_link_text(self, e_link_text, driver=None, timeout=30):
		return self.find_elements(By.LINK_TEXT, e_link_text, driver, timeout)

	def find_elements_by_partial_link_text(self, e_partial_link_text, driver=None, timeout=30):
		return self.find_elements(By.PARTIAL_LINK_TEXT, e_partial_link_text, driver, timeout)

	def find_elements_by_tag_name(self, e_tag_name, driver=None, timeout=30):
		return self.find_elements(By.TAG_NAME, e_tag_name, driver, timeout)

	def find_elements_by_class_name(self, e_class_name, driver=None, timeout=30):
		return self.find_elements(By.CLASS_NAME, e_class_name, driver, timeout)

	def find_elements_by_css_selector(self, e_css_selector, driver=None, timeout=30):
		return self.find_elements(By.CSS_SELECTOR, e_css_selector, driver, timeout)

	def page_source(self, driver=None):
		driver = driver or self.driver
		return driver.page_source

	def get_innerHTML(self, element):
		'''
		read innerHTML attribute to get source of the content of the element .Exclude element tag
		Example:
			<div id='element'>
				<div class='test'></div>
			</div>

			element = driver.find_element_by_id('element')
			result = element.get_attribute('innerHTML') 
			
			output:
				
				<div class='test'></div>

		'''
		try:
			return element.get_attribute('innerHTML')
			

		except Exception as e:

			return None

	def get_outerHTML(self, element):
		'''
		outerHTML for source with the current element. Include element tag
		Example:
			<div id='element'>
				<div class='test'></div>
			</div>

			element = driver.find_element_by_id('element')
			result = element.get_attribute('outerHTML') 

			output:
				<div id='element'>
					<div class='test'></div>
				</div>
		
		'''
		try:
			return element.get_attribute('outerHTML')
			

		except Exception as e:

			return None

	def get_element_child_by_name(self, e_name, index=0, driver=None, timeout=30):
		driver = driver or self.driver
		e_childs = self.find_elements_by_name(e_name, driver, timeout)
		if not e_childs:
			print(self.get_innerHTML(driver))
			return 
		result = e_childs[index]
		if not result:
			print(self.get_innerHTML(driver))
			print("cannot find child by index: {} in elements: {}".format(index, e_childs))
			return 
		return result
		

	def get_element_child_by_xpath(self, e_xpath, index=0, driver=None, timeout=30):
		driver = driver or self.driver
		e_childs = self.find_elements_by_xpath(e_xpath, driver, timeout)
		if not e_childs:
			print(self.get_innerHTML(driver))
			return 
		result = e_childs[index]
		if not result:
			print(self.get_innerHTML(driver))
			print("cannot find child by index: {} in elements: {}".format(index, e_childs))
			return 
		return result
		

	def get_element_child_by_link_text(self, e_link_text, index=0, driver=None, timeout=30):
		driver = driver or self.driver
		e_childs = self.find_elements_by_link_text(e_link_text, driver, timeout)
		if not e_childs:
			print(self.get_innerHTML(driver))
			return 
		result = e_childs[index]
		if not result:
			print(self.get_innerHTML(driver))
			print("cannot find child by index: {} in elements: {}".format(index, e_childs))
			return 
		return result
		

	def get_element_child_by_partial_link_text(self, e_partial_link_text, index=0, driver=None, timeout=30):
		driver = driver or self.driver
		e_childs = self.find_elements_by_partial_link_text(e_partial_link_text, driver, timeout)
		if not e_childs:
			print(self.get_innerHTML(driver))
			return 
		result = e_childs[index]
		if not result:
			print(self.get_innerHTML(driver))
			print("cannot find child by index: {} in elements: {}".format(index, e_childs))
			return 
		return result
		

	def get_element_child_by_tag_name(self, e_tag_name, index=0, driver=None, timeout=30):
		driver = driver or self.driver
		e_childs = self.find_elements_by_tag_name(e_tag_name, driver, timeout)
		if not e_childs:
			print(self.get_innerHTML(driver))
			return 
		result = e_childs[index]
		if not result:
			print(self.get_innerHTML(driver))
			print("cannot find child by index: {} in elements: {}".format(index, e_childs))
			return 
		return result
		

	def get_element_child_by_class_name(self, e_class_name, index=0, driver=None, timeout=30):
		driver = driver or self.driver
		e_childs = self.find_elements_by_class_name(e_class_name, driver, timeout)
		if not e_childs:
			print(self.get_innerHTML(driver))
			return 
		result = e_childs[index]
		if not result:
			print(self.get_innerHTML(driver))
			print("cannot find child by index: {} in elements: {}".format(index, e_childs))
			return 
		return result
		

	def get_element_child_by_css_selector(self, e_css_selector, index=0, driver=None, timeout=30):
		driver = driver or self.driver
		e_childs = self.find_elements_by_css_selector(e_css_selector, driver, timeout)
		if not e_childs:
			print(self.get_innerHTML(driver))
			return 
		result = e_childs[index]
		if not result:
			print(self.get_innerHTML(driver))
			print("cannot find child by index: {} in elements: {}".format(index, e_childs))
			return 
		return result
	
	def get_select_element(self, element):
		return Select(element)

	def all_selected_options(self, select_tag):
		'''
		Returns a list of all selected options belonging to this select tag
		'''
		return select_tag.all_selected_options

	def deselect_all(self, select_tag):
		'''
		Clear all selected entries. This is only valid when the SELECT supports multiple selections. 
		throws NotImplementedError If the SELECT does not support multiple selections
		'''
		return select_tag.deselect_all()

	def deselect_by_index(self, index, select_tag):
		'''
		Deselect the option at the given index. 
		This is done by examing the “index” attribute of an element, and not merely by counting.
		@param
			index - The option at this index will be deselected
			throws NoSuchElementException If there is no option with specisied index in SELECT

		'''
		return select_tag.deselect_by_index(index)

	def deselect_by_value(self, value, select_tag):
		'''
		Deselect all options that have a value matching the argument. 
		That is, when given “foo” this would deselect an option like:
			<option value=”foo”>Bar</option>
		@param
			value - The value to match against
			throws NoSuchElementException If there is no option with specisied value in SELECT

		'''
		return select_tag.deselect_by_value(value)

	def deselect_by_visible_text(self, text, select_tag):
		'''
		Deselect all options that display text matching the argument. 
		That is, when given “Bar” this would deselect an option like:
			<option value=”foo”>Bar</option>
		@param
			text - The visible text to match against

		'''
		return select_tag.deselect_by_visible_text(text)

	def first_selected_option(self, select_tag):
		'''
		The first selected option in this select tag (or the currently selected option in a normal select)
		@param
			text - The visible text to match against

		'''
		return select_tag.first_selected_option(text)

	def get_select_options(self, select_tag):
		'''
		Returns a list of all options belonging to this select tag
		'''

		return select_tag.options

	def select_by_index(self, index, select_tag):
		'''
		Select the option at the given index. 
		This is done by examing the “index” attribute of an element, and not merely by counting.
		@param
			index - The option at this index will be selected
			throws NoSuchElementException If there is no option with specisied index in SELECT
		'''
		return select_tag.select_by_index(index)

	def select_by_value(self, value, select_tag):
		'''
		Select all options that have a value matching the argument. 
		That is, when given “foo” this would select an option like:
			<option value=”foo”>Bar</option>
		@param
			value - The value to match against
			throws NoSuchElementException If there is no option with specisied value in SELECT
		'''
		return select_tag.select_by_value(value)

	def select_by_visible_text(self, value, select_tag):
		'''
		Select all options that display text matching the argument. 
		That is, when given “Bar” this would select an option like:
			<option value=”foo”>Bar</option>
		@param
			text - The visible text to match against
			throws NoSuchElementException If there is no option with specisied text in SELECT
		'''
		return select_tag.select_by_visible_text(value)


	def element_to_be_clickable_by_id(self, e_id, driver=None, timeout=30):
		return self.element_to_be_clickable(By.ID, e_id, driver, timeout)

	def element_to_be_clickable_by_name(self, e_name, driver=None, timeout=30):
		return self.element_to_be_clickable(By.NAME, e_name, driver, timeout)

	def element_to_be_clickable_by_xpath(self, e_xpath, driver=None, timeout=30):
		return self.element_to_be_clickable(By.XPATH, e_xpath, driver, timeout)

	def element_to_be_clickable_by_link_text(self, e_link_text, driver=None, timeout=30):
		return self.element_to_be_clickable(By.LINK_TEXT, e_link_text, driver, timeout)

	def element_to_be_clickable_by_partial_link_text(self, e_partial_link_text, driver=None, timeout=30):
		return self.element_to_be_clickable(By.PARTIAL_LINK_TEXT, e_partial_link_text, driver, timeout)

	def element_to_be_clickable_by_tag_name(self, e_tag_name, driver=None, timeout=30):
		return self.element_to_be_clickable(By.TAG_NAME, e_tag_name, driver, timeout)

	def element_to_be_clickable_by_class_name(self, e_class_name, driver=None, timeout=30):
		return self.element_to_be_clickable(By.CLASS_NAME, e_class_name, driver, timeout)

	def element_to_be_clickable_by_css_selector(self, e_css_selector, driver=None, timeout=30):
		return self.element_to_be_clickable(By.CSS_SELECTOR, e_css_selector, driver, timeout)


	def presence_of_element_located_by_id(self, e_id, driver=None, timeout=30):
		return self.presence_of_element_located(By.ID, e_id, driver, timeout)
		
	def presence_of_element_located_by_name(self, e_name, driver=None, timeout=30):
		return self.presence_of_element_located(By.NAME, e_name, driver, timeout)
		
	def presence_of_element_located_by_xpath(self, e_xpath, driver=None, timeout=30):
		return self.presence_of_element_located(By.XPATH, e_xpath, driver, timeout)
		
	def presence_of_element_located_by_link_text(self, e_link_text, driver=None, timeout=30):
		return self.presence_of_element_located(By.LINK_TEXT, e_link_text, driver, timeout)
		
	def presence_of_element_located_by_partial_link_text(self, e_partial_link_text, driver=None, timeout=30):
		return self.presence_of_element_located(By.PARTIAL_LINK_TEXT, e_partial_link_text, driver, timeout)
		
	def presence_of_element_located_by_tag_name(self, e_tag_name, driver=None, timeout=30):
		return self.presence_of_element_located(By.TAG_NAME, e_tag_name, driver, timeout)
		
	def presence_of_element_located_by_class_name(self, e_class_name, driver=None, timeout=30):
		return self.presence_of_element_located(By.CLASS_NAME, e_class_name, driver, timeout)
		
	def presence_of_element_located_by_css_selector(self, e_css_selector, driver=None, timeout=30):
		return self.presence_of_element_located(By.CSS_SELECTOR, e_css_selector, driver, timeout)

	
	def visibility_of_element_located_by_id(self, e_id, driver=None, timeout=30):
		return self.visibility_of_element_located(By.ID, e_id, driver, timeout)
		
	def visibility_of_element_located_by_name(self, e_name, driver=None, timeout=30):
		return self.visibility_of_element_located(By.NAME, e_name, driver, timeout)
		
	def visibility_of_element_located_by_xpath(self, e_xpath, driver=None, timeout=30):
		return self.visibility_of_element_located(By.XPATH, e_xpath, driver, timeout)
		
	def visibility_of_element_located_by_link_text(self, e_link_text, driver=None, timeout=30):
		return self.visibility_of_element_located(By.LINK_TEXT, e_link_text, driver, timeout)
		
	def visibility_of_element_located_by_partial_link_text(self, e_partial_link_text, driver=None, timeout=30):
		return self.visibility_of_element_located(By.PARTIAL_LINK_TEXT, e_partial_link_text, driver, timeout)
		
	def visibility_of_element_located_by_tag_name(self, e_tag_name, driver=None, timeout=30):
		return self.visibility_of_element_located(By.TAG_NAME, e_tag_name, driver, timeout)
		
	def visibility_of_element_located_by_class_name(self, e_class_name, driver=None, timeout=30):
		return self.visibility_of_element_located(By.CLASS_NAME, e_class_name, driver, timeout)
		
	def visibility_of_element_located_by_css_selector(self, e_css_selector, driver=None, timeout=30):
		return self.visibility_of_element_located(By.CSS_SELECTOR, e_css_selector, driver, timeout)

	
	def text_to_be_present_in_element_by_id(self, e_id, text_, driver=None, timeout=30):
		return self.text_to_be_present_in_element(By.ID, e_id, text_, driver, timeout)
		
	def text_to_be_present_in_element_by_name(self, e_name, text_, driver=None, timeout=30):
		return self.text_to_be_present_in_element(By.NAME, e_name, text_, driver, timeout)
		
	def text_to_be_present_in_element_by_xpath(self, e_xpath, text_, driver=None, timeout=30):
		return self.text_to_be_present_in_element(By.XPATH, e_xpath, text_, driver, timeout)
		
	def text_to_be_present_in_element_by_link_text(self, e_link_text, text_, driver=None, timeout=30):
		return self.text_to_be_present_in_element(By.LINK_TEXT, e_link_text, text_, driver, timeout)
		
	def text_to_be_present_in_element_by_partial_link_text(self, e_partial_link_text, text_, driver=None, timeout=30):
		return self.text_to_be_present_in_element(By.PARTIAL_LINK_TEXT, e_partial_link_text, text_, driver, timeout)
		
	def text_to_be_present_in_element_by_tag_name(self, e_tag_name, text_, driver=None, timeout=30):
		return self.text_to_be_present_in_element(By.TAG_NAME, e_tag_name, text_, driver, timeout)
		
	def text_to_be_present_in_element_by_class_name(self, e_class_name, text_, driver=None, timeout=30):
		return self.text_to_be_present_in_element(By.CLASS_NAME, e_class_name, text_, driver, timeout)
		
	def text_to_be_present_in_element_by_css_selector(self, e_css_selector, text_, driver=None, timeout=30):
		return self.text_to_be_present_in_element(By.CSS_SELECTOR, e_css_selector, text_, driver, timeout)


	def frame_to_be_available_and_switch_to_it_by_id(self, e_id, driver=None, timeout=30):
		return self.frame_to_be_available_and_switch_to_it(By.ID, e_id, driver, timeout)
		
	def frame_to_be_available_and_switch_to_it_by_name(self, e_name, driver=None, timeout=30):
		return self.frame_to_be_available_and_switch_to_it(By.NAME, e_name, driver, timeout)
		
	def frame_to_be_available_and_switch_to_it_by_xpath(self, e_xpath, driver=None, timeout=30):
		return self.frame_to_be_available_and_switch_to_it(By.XPATH, e_xpath, driver, timeout)
		
	def frame_to_be_available_and_switch_to_it_by_link_text(self, e_link_text, driver=None, timeout=30):
		return self.frame_to_be_available_and_switch_to_it(By.LINK_TEXT, e_link_text, driver, timeout)
		
	def frame_to_be_available_and_switch_to_it_by_partial_link_text(self, e_partial_link_text, driver=None, timeout=30):
		return self.frame_to_be_available_and_switch_to_it(By.PARTIAL_LINK_TEXT, e_partial_link_text, driver, timeout)
		
	def frame_to_be_available_and_switch_to_it_by_tag_name(self, e_tag_name, driver=None, timeout=30):
		return self.frame_to_be_available_and_switch_to_it(By.TAG_NAME, e_tag_name, driver, timeout)
		
	def frame_to_be_available_and_switch_to_it_by_class_name(self, e_class_name, driver=None, timeout=30):
		return self.frame_to_be_available_and_switch_to_it(By.CLASS_NAME, e_class_name, driver, timeout)
		
	def frame_to_be_available_and_switch_to_it_by_css_selector(self, e_css_selector, driver=None, timeout=30):
		return self.frame_to_be_available_and_switch_to_it(By.CSS_SELECTOR, e_css_selector, driver, timeout)

	def switch_to_default_content(self, driver=''):
		driver = driver or self.driver
		return driver.switch_to_default_content()
	

	def get_element_parent(self, element):

		return self.find_element_by_xpath('..', element)