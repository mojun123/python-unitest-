import os
import sys

sys.path.append(os.path.dirname(os.getcwd()))
from page.assert_attrs import AssertAttrs

class ExcuteJS(AssertAttrs):
	"""docstring for ExcuteJS"""
	def scroll_to_offset(self, offset=0):
		self.driver.execute_script("window.scrollTo(0, %s);" % offset)

	def scroll_to_element_by_js(self, element, alignToTop='true'):
		if element:
			return self.driver.execute_script("arguments[0].scrollIntoView({});".format(alignToTop), element)

	def scroll_to_element(self, element, driver=''):
		driver = driver or self.driver
		from selenium.webdriver.common.action_chains import ActionChains
		actions = ActionChains(driver)

		actions.move_to_element(element)
		actions.click(element)
		actions.perform()

	def click(self, element):
		self.driver.execute_script("arguments[0].click();", element)

	def focus(self, element):
		self.driver.execute_script("arguments[0].focus();", element)

	def blur(self, element):
		self.driver.execute_script("arguments[0].blur();", element)

	def disable_popup(self, element):
		'''
		important meaning style=display:none will not be change
		'''
		self.driver.execute_script("arguments[0].style.setProperty('display', 'none', 'important');", element)

	def assert_url_after_click_href_by_key_word(self, _key_word, element, is_new_tab=False):

		self.assertIsNotNone(element)
		self.scroll_to_element(element)

		if not is_new_tab:
			self.assertIn(_key_word, self.driver.current_url)
		
		else:
			current_window_handle = self.driver.current_window_handle
			window_handles = self.driver.window_handles
			window_handles_qty = len(window_handles)
			self.assert_greater_equal(window_handles_qty, 2)
			self.driver.switch_to_window(window_handles[1])

			self.assertIn(_key_word, self.driver.current_url)
			self.driver.close()
			self.driver.switch_to_window(current_window_handle)

class DriverKeys(ExcuteJS):
	
	def send_keys(self, key, element):
		from selenium.webdriver.common.keys import Keys
		# Keys.SPACE
		element.send_keys(key)
		
class ChromeDriver(DriverKeys):
	"""docstring for ChromeDriver"""
	def set_driver(self, driver):
		self.driver = driver
	
	def save_screenshot(self, name):
		from utils import file_handle as fhd
		fhd.mkdir_if_not_existed(name)
		return self.driver.save_screenshot(name)
		
	def get_cookies(self):
		return self.driver.get_cookies()

	def add_cookie(self, cookies_dict):
		return self.driver.add_cookie(cookies_dict)

	def save_cookie_to_file(self, path):
		with open(path, 'wb') as filehandler:
			pickle.dump(self.driver.get_cookies(), filehandler)

	def load_cookie_from_file(self, path):
		from utils import file_handle as fhd
		cookies = fhd.file_content_to_py_object(path)
		self.assertIsNotNone(cookies)
		self.assertIs(type(cookies), list)
		for cookie in cookies:
			self.driver.add_cookie(cookie)

	def delete_all_cookies(self):
		self.driver.delete_all_cookies()

	def refresh(self):
		return self.driver.refresh()

	def random_user_agents(self, browser_type='chrome'):
		# print(1111111111111)
		user_agents_list = []
		if browser_type == 'android-browser':
			from user_agents import android_browser_user_agent as _ua
			user_agents_list = _ua.android_browser_user_agent
		elif browser_type == 'internet-explorer':
			from user_agents import internet_explorer_user_agent as _ua
			user_agents_list = _ua.internet_explorer_user_agent
		elif browser_type == 'firefox':
			from user_agents import firefox_user_agent as _ua
			user_agents_list = _ua.firefox_user_agent
		elif browser_type == 'facebook-app':
			from user_agents import facebook_app_user_agent as _ua
			user_agents_list = _ua.facebook_app_user_agent
		elif browser_type == 'opera-mini':
			from user_agents import opera_mini_user_agent as _ua
			user_agents_list = _ua.opera_mini_user_agent
		elif browser_type == 'opera':
			from user_agents import opera_user_agent as _ua
			user_agents_list = _ua.opera_user_agent
		elif browser_type == 'safari':
			from user_agents import safari_user_agent as _ua
			user_agents_list = _ua.safari_user_agent
		elif browser_type == 'chrome':
			from user_agents import chrome_user_agent as _ua
			user_agents_list = _ua.chrome_user_agent
		elif browser_type == 'uc-browser':
			from user_agents import uc_browser_user_agent as _ua
			user_agents_list = _ua.uc_browser_user_agent
		elif browser_type == 'ios':
			from user_agents import ios_user_agent as _ua
			user_agents_list = _ua.ios_user_agent
		elif browser_type == 'macos':
			from user_agents import macos_user_agent as _ua
			user_agents_list = _ua.macos_user_agent
		elif browser_type == 'windows':
			from user_agents import windows_user_agent as _ua
			user_agents_list = _ua.windows_user_agent
		elif browser_type == 'android':
			from user_agents import android_user_agent as _ua
			user_agents_list = _ua.android_user_agent
		elif browser_type == 'iphone':
			from user_agents import iphone_user_agent as _ua
			user_agents_list = _ua.iphone_user_agent
		elif browser_type == 'ipad':
			from user_agents import ipad_user_agent as _ua
			user_agents_list = _ua.ipad_user_agent
		else:
			from user_agents import android_browser_user_agent
			user_agents_list += android_browser_user_agent.android_browser_user_agent

			from user_agents import internet_explorer_user_agent
			user_agents_list += internet_explorer_user_agent.internet_explorer_user_agent

			from user_agents import firefox_user_agent
			user_agents_list += firefox_user_agent.firefox_user_agent

			from user_agents import facebook_app_user_agent
			user_agents_list += facebook_app_user_agent.facebook_app_user_agent

			from user_agents import opera_mini_user_agent
			user_agents_list += opera_mini_user_agent.opera_mini_user_agent

			from user_agents import opera_user_agent
			user_agents_list += opera_user_agent.opera_user_agent

			from user_agents import safari_user_agent
			user_agents_list += safari_user_agent.safari_user_agent

			from user_agents import chrome_user_agent
			user_agents_list += chrome_user_agent.chrome_user_agent

			from user_agents import uc_browser_user_agent
			user_agents_list += uc_browser_user_agent.uc_browser_user_agent

			from user_agents import ios_user_agent
			user_agents_list += ios_user_agent.ios_user_agent

			from user_agents import macos_user_agent
			user_agents_list += macos_user_agent.macos_user_agent

			from user_agents import windows_user_agent
			user_agents_list += windows_user_agent.windows_user_agent

			from user_agents import android_user_agent
			user_agents_list += android_user_agent.android_user_agent

			from user_agents import iphone_user_agent
			user_agents_list += iphone_user_agent.iphone_user_agent

			from user_agents import ipad_user_agent
			user_agents_list += ipad_user_agent.ipad_user_agent
		# from pprint import pprint
		# pprint(user_agents_list)

		import random
		self.user_agent = random.choice(user_agents_list)
		return self.user_agent

