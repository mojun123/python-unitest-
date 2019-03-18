import os
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.remote.webdriver import WebElement

sys.path.append(os.path.dirname(os.getcwd()))

from src.page.locate_elements import LocateElements

class LocateElementsByJS(LocateElements):
	"""docstring for LocateElementsByJS"""
	
	def get_parent_by_js(self, element, timeout=30):
		
		# try:
			
		# 	return WebDriverWait(self.driver, timeout).until(dget_parent_by_js(element))
			
		# except Exception as e:
		# 	# print("wait_for_element timeout: ")
		# 	raise e
		# 	return None
		try:
			return self.driver.execute_script( "return arguments[0].parentNode;", element)
		except NoSuchElementException as e:
			raise e
		except WebDriverException as e:
			raise e

		
	def get_children_by_js(self, element):
		try:
			return self.driver.execute_script( "return arguments[0].children;", element)
		except NoSuchElementException as e:
			raise e
		except WebDriverException as e:
			raise e
		
	def get_children_by_index(self, driver='', index=0):
		driver = driver or self.driver
		all_childrens = self.get_children_by_js(driver)
		try:
			return all_childrens[index]
		except Exception as e:
			raise e
		



# class dget_parent_by_js(object):
# 	""" Expect an alert to be present."""
# 	def __init__(self, element):
# 		self.element = element

# 	def __call__(self, driver):
# 		try:
# 			e_parent = _execute_script( driver, ("return arguments[0].parentNode;", self.element))
# 			assert e_parent != None
# 			return e_parent
# 		except Exception as e:
# 			raise e

# def _execute_script(driver, by):
# 	from selenium.common.exceptions import WebDriverException
# 	try:
# 		return driver.execute_script(by)
# 	except WebDriverException as e:
# 		raise e
