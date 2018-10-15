from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import os
import time
from utils.driver_env import *
from utils.file_handle import *
from testcase.HomePage import Home
from testcase.Login import Login
from testcase.ProductDetails import ProductDetails
from testcase.ViewCart import ViewCart
from testcase.CheckOut import Checkout
from testcase.SelectPayment import PyamentMethod
from pprint import pprint

G_COOKIE_FILE = {
	'login': os.path.join('..', 'tmp', 'login_cookies.log'),
	'addtocart': os.path.join('..', 'tmp', 'addtocart_cookies.log'),
	'viewcart': os.path.join('..', 'tmp', 'viewcart_cookies.log'),
	'checkout': os.path.join('..', 'tmp', 'checkout_cookies.log'),

}

G_SHOP = {
	'e_product_detail_add_to_cart': "element obj",
	'product_unit_price': "0",
	'url_after_click_checkout': "",
	'credit_card_checkout_url': "",
}

G_PAYMENT_PAGE_OBJECT = None


class CaseHome(unittest.TestCase):

	def random_proxy(self):
		import random
		proxy_list = [
			'192.168.10.20:1080',
			'192.168.10.20:1081',
			'192.168.10.20:1082',
			'192.168.10.20:1083',
			'192.168.10.20:1084'
			]

		return random.choice(proxy_list)

	def set_proxy(self, _proxy):
		# PROXY = "192.168.10.20:1081"

		# # Create a copy of desired capabilities object.
		# desired_capabilities = webdriver.DesiredCapabilities.CHROME.copy()
		# # Change the proxy properties of that copy.
		# desired_capabilities['proxy'] = {
		# 	"httpProxy":PROXY,
		# 	"ftpProxy":PROXY,
		# 	"sslProxy":PROXY,
		# 	"noProxy":None,
		# 	"proxyType":"MANUAL",
		# 	"class":"org.openqa.selenium.Proxy",
		# 	"autodetect":False
		# }
		# return desired_capabilities



		from selenium.webdriver.common.proxy import Proxy, ProxyType

		myprox = Proxy()
		# PROXY = "192.168.10.20:1081"
		myprox.proxy_type = ProxyType.MANUAL
		myprox.http_proxy = _proxy
		myprox.socks_proxy = _proxy
		myprox.ssl_proxy = _proxy

		return myprox

		# chrome_options = webdriver.ChromeOptions()
		# chrome_options.add_argument('--proxy-server=https://192.168.10.20:1081')
		# # driver = webdriver.Chrome(chrome_options=chrome_options)
		# return chrome_options

	def set_proxies_disable(self, host="192.168.10.230"):
		'''
		session = requests.Session()
		session.trust_env = False
		os.environ['NO_PROXY'] = 'stackoverflow.com'
		response = requests.get('http://www.stackoverflow.com')
		'''
		import os
		os.environ['NO_PROXY'] = host

	def check_response_and_js(self, page_obj, url, status=200):
		import json
		rsp_obj, rq_obj = page_obj.get_requests_and_response_infos_by_url(url)
		pprint(rsp_obj)
		pprint(rq_obj)
		page_obj.general_request_and_response_infos(rsp_obj, rq_obj)
		# page_obj.get_new_requests_and_response_infos_by_url(self.host)
		real_status = page_obj.check_response_status(rsp_obj)
		assert real_status == status

		browser_logs = page_obj.get_browser_severe_logs()
		browser_logs = json.dumps(browser_logs, indent=4)
		flag = '----' *20
		msg = """
Got some js error, logs as follow:
%s
%s
%s
""" % (flag, browser_logs, flag)
		assert url not in browser_logs, msg

		

	def setUp(self):
		self.url = "https://qa.clatterans.com/"
		self.host = "qa.clatterans.com"
		self.title = ""
		self.set_proxies_disable(self.host)
		self.chromedriver = set_driver_path()
		os.environ["webdriver.chrome.driver"] = self.chromedriver
		chromeOptions = webdriver.ChromeOptions()
		# chromeOptions.add_argument('--proxy-server=http://192.168.10.20:1087')
		# chromeOptions.add_argument("--headless") # Runs Chrome in headless mode.
		chromeOptions.add_argument('--no-sandbox') # Bypass OS security model
		chromeOptions.add_argument('--disable-gpu')  # applicable to windows os only
		chromeOptions.add_argument('start-maximized') # 
		chromeOptions.add_argument('disable-infobars')
		chromeOptions.add_argument("--disable-extensions")  
		chromeOptions.add_argument("--start-maximized")
		capabilities = webdriver.DesiredCapabilities.CHROME
		capabilities['loggingPrefs'] = { 
			'browser': 'ALL',
			'driver': 'ALL',
			'performance': 'ALL'
		}
		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		log_path = '--log-path=' + os.path.join("..", "log", "chromedriver_%s.log" % nowTime)
		log_type = '--verbose'

		self.driver = webdriver.Chrome(
			self.chromedriver, 
			chrome_options=chromeOptions, 
			desired_capabilities=capabilities,
			service_args=[log_path]
			)
		
		

	def home_page(self):

		title = "Refrigerator Water Filters, Water Filter Online | Clatterans.com" 
		home_page = Home(self.driver, self.url, title)
		return home_page

	def home_page_click_signin_href(self):
		home_page = self.home_page()
		home_page.open()
		element_id = "signin"
		element = home_page.expected_wait_clickable_by_id(element_id)
		element.click()
		b_login = False
		
		element_id = "popup-login-border"
		driver = home_page.driver
		time.sleep(1)
		element = driver.find_element_by_id(element_id)
		
		return element

	@unittest.skip("test")
	def test_succeed_to_click_login(self):

		element = self.home_page_click_signin_href()
		print("element.is_displayed(): ",element.is_displayed())
		msg = "cannot locate login popup "
		self.assertTrue(element.is_displayed(), msg)

	def test_home_page(self):
		home_page = self.home_page()
		b_open = home_page.open()
		# nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		# file_name = os.path.join('..', 'screenshot', 'home', 'Open_homepage_%s.png' % nowTime)
		# home_page.save_screenshot(file_name)
		self.check_response_and_js(home_page, self.url)
		b_title = home_page.assrt_page()

		
# 		import json
# 		rsp_obj, rq_obj = home_page.get_requests_and_response_infos_by_url(self.url)
# 		home_page.general_request_and_response_infos(rsp_obj, rq_obj)

# 		browser_logs = home_page.get_browser_severe_logs()
# 		browser_logs = json.dumps(browser_logs, indent=4)
# 		flag = '----' *20
# 		msg = """
# Got some js error, logs as follow:
# %s
# %s
# %s
# """ % (flag, browser_logs, flag)
# 		assert self.url not in browser_logs, msg
		
		# time.sleep(10)

	def test_login_action(self):
	
		email = "young_yang@limei-trading.com"
		pwd = "123456"

		login_page = Login(self.driver, self.url, self.title)
		self.home_page_click_signin_href()
		element_signin = login_page.login(email, pwd)
		

		#save homepage png after login
		element_signin.click()
		# home_page = self.home_page()
		time.sleep(5)
		# print(self.driver.page_source.encode("utf-8"))

		#assert login success
		element_id = "welcome"
		element = login_page.find_element_by_id(element_id)
		child_element = login_page.find_element_by_tag_name("h2")
		assert "young" in child_element.text

		# pretty_write(self.driver.get_log('performance'),"./testlogin.log")
		# check js error
		self.check_response_and_js(login_page, self.url)

		#save session after login
		# cookies_file = "./tmp/cookies.log"
		cookies_file = G_COOKIE_FILE['login']
		cookies_list = login_page.get_cookies()
		pretty_write(cookies_list, cookies_file)

		
		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		file_name = os.path.join('..', 'screenshot', 'home', 'homepage_after_login_%s.png' % nowTime)
		login_page.save_screenshot(file_name)

	def test_empty_carts(self):
		expected_url = self.url + 'viewcart'
		title = 'Shopping Cart | Clatterans.com'
		viewcart_page = ViewCart(self.driver, expected_url, title)
		#open viewcart page
		viewcart_page.open()
		cookies_file = G_COOKIE_FILE['login']
		viewcart_page.load_cookie_from_file(cookies_file)
		viewcart_page.refresh()
		time.sleep(5)

		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		file_name = os.path.join('..', 'screenshot', 'viewcart', 'cart_before_empty_%s.png' % nowTime)
		viewcart_page.save_screenshot(file_name)

		b_empty = viewcart_page.check_empty_cart()
		assert b_empty != None
		if not b_empty:
			viewcart_page.del_first_product()
			self.test_empty_carts()

		cookies_file = G_COOKIE_FILE['login']
		cookies_list = viewcart_page.get_cookies()
		pretty_write(cookies_list, cookies_file)
		
		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		file_name = os.path.join('..','screenshot', 'viewcart', 'cart_after_empty_%s.png' % nowTime)
		viewcart_page.save_png(file_name)

	def test_add_to_cart_action(self):

		#homepage add login session
		home_page = self.home_page()
		home_page.open()
		# cookies_file = "./tmp/cookies.log"
		cookies_file = G_COOKIE_FILE['login']
		home_page.load_cookie_from_file(cookies_file)

		#get first product's name
		xpath = '//*[@id="main"]/div[4]/div/div[1]/a/p'
		element = home_page.expected_wait_clickable_by_xpath(xpath)
		name = element.text
		#get first product's href
		href = '//*[@id="main"]/div[4]/div/div[1]/a'
		expected_url, _ = home_page.get_element_attribute_by_xpath(href, attr="href")
		#homepage click product's url to product's details page
		home_page._click(element, expected_url)

		#save product detail's page png
		productdetails_page = ProductDetails(self.driver, expected_url, name)
		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		save_png_name = os.path.join('..', 'screenshot', 'products', 'details_%s.png' % nowTime)
		productdetails_page.save_screenshot(save_png_name)
		time.sleep(1)

		#On product details's page, check js error
		#todo server error(500, 404) 
		# productdetails_page.check_js_and_save_png(save_png_name)
		self.check_response_and_js(productdetails_page, self.url)

		
		#if in stock, check add-to-cart button clickable
		element_add_to_cart = productdetails_page.check_instock_add_to_cart()

		#get product's unit price
		unit_price = productdetails_page.get_product_unit_price()
		assert float(unit_price) > 0 
		G_SHOP['product_unit_price'] = unit_price

		#click add-to-cart button
		element_add_to_cart.click()

		print(self.driver.current_url)

		#save session after add-to-cart
		# cookies_file = "./tmp/cookies.log"
		cookies_file = G_COOKIE_FILE['addtocart']
		cookies_list = home_page.get_cookies()
		pretty_write(cookies_list, cookies_file)

	def test_view_action(self):

		#viewcart add add-to-cart session 
		expected_url = self.url + 'viewcart'
		title = 'Shopping Cart | Clatterans.com'
		viewcart_page = ViewCart(self.driver, expected_url, title)
		#open viewcart page
		viewcart_page.open()
		cookies_file = G_COOKIE_FILE['addtocart']
		viewcart_page.load_cookie_from_file(cookies_file)
		viewcart_page.refresh()
		time.sleep(5)

		#save cart png
		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		save_png_name = os.path.join('..', 'screenshot', 'viewcart', 'add_session_then_open_viewcart_%s.png' % nowTime)
		# viewcart_page.check_js_and_save_png(save_png_name)
		viewcart_page.save_screenshot(save_png_name)
		self.check_response_and_js(viewcart_page, expected_url)

		#check viewcart info , should have one product at least
		expected_unit_price = "$" + G_SHOP['product_unit_price']
		real_unit_price = viewcart_page.check_product_unit_price(expected_unit_price)
		viewcart_page.assert_element_attribute(real_unit_price, expected_unit_price)
		expected_qty = "1"
		real_qty = viewcart_page.check_product_qty(expected_qty)
		viewcart_page.assert_element_attribute(real_qty, expected_qty)

		# expected_subtotal = str(float(unit_price) * int(expected_qty))
		# expected_unit_price = "$" + expected_subtotal
		real_subtotal = viewcart_page.check_product_subtotal(expected_unit_price)
		viewcart_page.assert_element_attribute(real_subtotal, expected_unit_price)
		#check checkout button clickable
		checkout_button = viewcart_page.check_checkout_button()

		#check paypal express button clickable
		viewcart_page.check_paypal_express()
		time.sleep(3)

		checkout_button.click()
		print(self.driver.current_url)

		#save session 
		# cookies_file = "./tmp/cookies.log"
		cookies_file = G_COOKIE_FILE['viewcart']
		cookies_list = viewcart_page.get_cookies()
		pretty_write(cookies_list, cookies_file)

		#save cart png
		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		save_png_name = os.path.join('..','screenshot', 'viewcart', 'click_check_out_%s.png' % nowTime)
		# viewcart_page.check_js_and_save_png(save_png_name)
		viewcart_page.save_screenshot(save_png_name)
		self.check_response_and_js(viewcart_page, self.driver.current_url)


	def test_viewcart_checkout_action(self):

		#checkout add view cart session 
		home_page = self.home_page()
		home_page.open()
		# cookies_file = "./tmp/cookies.log"
		cookies_file = G_COOKIE_FILE['viewcart']

		home_page.load_cookie_from_file(cookies_file)
		expected_url = self.url + 'checkout'
		# print(expected_url)
		title = 'Clatterans Clatterans'
		checkout_page = Checkout(self.driver, expected_url, title)
		checkout_page.open()
		time.sleep(10)

		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		save_png_name = os.path.join('..', 'screenshot', 'checkout', 'add_session_checkout_page_%s.png' % nowTime)
		# checkout_page.check_js_and_save_png(save_png_name)
		checkout_page.save_screenshot(save_png_name)
		self.check_response_and_js(checkout_page, expected_url)

		#check checkout's page info, should have one product at least
		expected_unit_price = "$" + G_SHOP['product_unit_price']
		real_subtotal = checkout_page.check_subtotal(expected_unit_price)
		checkout_page.assert_element_attribute(real_subtotal, expected_unit_price)

		shipping_cost = "$" + '0.00'
		real_shipping_cost = checkout_page.check_shipping(shipping_cost)
		checkout_page.assert_element_attribute(real_shipping_cost, shipping_cost)
		real_discount_cost = checkout_page.check_discount(shipping_cost)
		checkout_page.assert_element_attribute(real_discount_cost, shipping_cost)
		real_total = checkout_page.check_total(expected_unit_price)
		checkout_page.assert_element_attribute(real_total, expected_unit_price)

		#check add-new-address button clickable
		button_add_new_address = checkout_page.check_add_new_address_button()
		#check select-payment-method button clickable
		select_payment_method_button = checkout_page.check_select_payment_method_button()
		
		#click select-payment-method button to get next url
		select_payment_method_button.click()
		time.sleep(3)
		G_SHOP['url_after_click_checkout'] = self.driver.current_url
		print(G_SHOP['url_after_click_checkout'])

		cookies_file = G_COOKIE_FILE['checkout']
		cookies_list = checkout_page.get_cookies()
		pretty_write(cookies_list, cookies_file)
		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		save_png_name = os.path.join('..','screenshot', 'checkout', 'click_select_payment_method_page_%s.png' % nowTime)
		# checkout_page.check_js_and_save_png(save_png_name)
		checkout_page.save_screenshot(save_png_name)

	def test_select_payment_method_action(self):

		home_page = self.home_page()
		home_page.open()
		cookies_file = G_COOKIE_FILE['checkout']
		home_page.load_cookie_from_file(cookies_file)

		expected_url = G_SHOP['url_after_click_checkout']
		print(expected_url)
		assert expected_url != ''
		title = 'Clatterans Clatterans'
		payment_method_page = PyamentMethod(self.driver, expected_url, title)
		payment_method_page.open()
		time.sleep(5)

		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		save_png_name = os.path.join('..', 'screenshot', 'checkout', 'orderconfirm', 'add_session_checkout_orderconfirm_page_%s.png' % nowTime)
		# payment_method_page.check_js_and_save_png(save_png_name)
		payment_method_page.save_screenshot(save_png_name)
		self.check_response_and_js(payment_method_page, expected_url)

		#check order info, should have one product at least
		expected_unit_price = "$" + G_SHOP['product_unit_price']
		shipping_cost = "$" + '0.00'
		real_subtotal = payment_method_page.check_subtotal(expected_unit_price)
		payment_method_page.assert_element_attribute(real_subtotal, expected_unit_price)
		
		real_shipping_cost = payment_method_page.check_shipping(shipping_cost)
		payment_method_page.assert_element_attribute(real_shipping_cost, shipping_cost)
		
		real_discount_cost = payment_method_page.check_discount(shipping_cost)
		payment_method_page.assert_element_attribute(real_discount_cost, shipping_cost)
		
		real_total = payment_method_page.check_total(expected_unit_price)
		payment_method_page.assert_element_attribute(real_total, expected_unit_price)

		G_PAYMENT_PAGE_OBJECT = payment_method_page

		#check paypal
		payment_method_page.selected_paypal()
		submit_button = payment_method_page.check_paypal_button()
		time.sleep(3)
		submit_button.click()
		expected_url = "https://www.paypal.com/webapps/hermes?token="
		print(expected_url)
		print(self.driver.current_url)
		assert expected_url in self.driver.current_url
		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		save_png_name = os.path.join('..', 'screenshot', 'checkout', 'orderconfirm', 'click_paypal%s.png' % nowTime)
		# payment_method_page.check_js_and_save_png(save_png_name)
		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		save_png_name = os.path.join('..', 'screenshot', 'checkout', 'add_session_checkout_page_%s.png' % nowTime)
		# checkout_page.check_js_and_save_png(save_png_name)
		payment_method_page.save_screenshot(save_png_name)
		

	def test_select_credit_card_and_submit(self):
		payment_method_page = G_PAYMENT_PAGE_OBJECT 
		assert payment_method_page != None

		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		save_png_name = os.path.join('..', 'screenshot', 'checkout', 'orderconfirm', 'select_creditcard_%s.png' % nowTime)
		# payment_method_page.check_js_and_save_png(save_png_name)

		#check credit card
		element_credit_card = payment_method_page.selected_credit_card()
		element_credit_card.click()

		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		save_png_name = os.path.join('..', 'screenshot', 'checkout', 'orderconfirm', 'click_creditcard_page_%s.png' % nowTime)
		# payment_method_page.check_js_and_save_png(save_png_name)
		payment_method_page.save_screenshot(save_png_name)
		self.check_response_and_js(payment_method_page, payment_method_page.url)

		submit_button = payment_method_page.check_paypal_button()
		time.sleep(3)
		submit_button.click()
		expected_url = self.url + "checkout/creditcard"
		time.sleep(1)
		print(expected_url)
		print(self.driver.current_url)
		assert expected_url in self.driver.current_url
		G_SHOP['credit_card_checkout_url'] = self.driver.current_url

		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		save_png_name = os.path.join('..', 'screenshot', 'checkout', 'orderconfirm', 'creditcard_submit_%s.png' % nowTime)
		# payment_method_page.check_js_and_save_png(save_png_name)

		payment_method_page.save_screenshot(save_png_name)
		self.check_response_and_js(payment_method_page, expected_url)


	def tearDown(self):
		# self.driver.close()
		self.driver.quit()

def run(file_name):
	from libs.HTMLTestRunner import HTMLTestRunner
	import datetime
	import time
	import codecs
   
	todayDate = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
	fname = file_name + todayDate + ".html"
	result_file = os.path.join('..', 'result', fname)
	mkdir_if_not_existed(result_file)
	fp = codecs.open(result_file,"wb",'utf-8')	
	runner = HTMLTestRunner(
			stream=fp,
			title='clatterans shopping main flow',
			description='\
				Included login -> \
				add-sku-to-cart -> \
				checkout -> \
				order-confirm -> \
				select-payment-method -> \
				payment-page'
			)

	suite = unittest.TestSuite()
	# suite.addTest(unittest.makeSuite(CaseHome))
	suite.addTest(CaseHome('test_home_page'))
	# suite.addTest(CaseHome('test_login_action'))
	# suite.addTest(CaseHome('test_empty_carts'))
	# suite.addTest(CaseHome('test_add_to_cart_action'))
	# suite.addTest(CaseHome('test_view_action'))
	# suite.addTest(CaseHome('test_viewcart_checkout_action'))
	# suite.addTest(CaseHome('test_select_payment_method_action'))
	# suite.addTest(CaseHome('test_select_credit_card_and_submit'))
	
	print("start : %s" % time.ctime())
	run_result=runner.run(suite)
	fp.close()
	print("End : %s" % time.ctime())

def test_porxy():
	b_succeed = True
	chromedriver = set_driver_path()
	os.environ["webdriver.chrome.driver"] = chromedriver
	chromeOptions = webdriver.ChromeOptions()
	chromeOptions.add_argument('--proxy-server=http://192.168.10.20:2087')  
	capabilities = webdriver.DesiredCapabilities.CHROME
	capabilities['loggingPrefs'] = {
		'browser':	 'ALL',
		'driver':	  'ALL',
		'performance': 'ALL' 
	}
	driver = webdriver.Chrome(chromedriver, desired_capabilities=capabilities)
	driver.maximize_window();
	url = "https://www.clatterans.com/"
	title = "Refrigerator Water Filters, Water Filter Online | Clatterans.com" 
	from page.base import BasePage
	proxy_page = BasePage(driver, url, title)
	proxy_page.open()
	rsp_str, rq_str = proxy_page.get_requests_and_response_infos_by_url(url)
	if not rsp_str or rsp_str.get('status') != 200:
		b_succeed = False
	
	driver.quit()
	return b_succeed

if __name__ == "__main__":
	file_name = "shopping_"
	

	run(file_name)
