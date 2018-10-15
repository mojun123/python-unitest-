from selenium import webdriver


import os
import sys
import time
BASEDIR = os.path.dirname(os.getcwd())
sys.path.append(BASEDIR)

from utils import driver_env as denv
from utils import file_handle as fhd

class ChromeBase(object):
	def __init__(self):

		
		self.set_driver_path()
		self.chrome_options = webdriver.ChromeOptions()
		self.capabilities = webdriver.DesiredCapabilities.CHROME
		self.capabilities['loggingPrefs'] = {}
		#if headless start-maximized not work. need to set window size
		self.headless = True
		self.headless_max = True
		self.no_sandbox = True
		self.disable_gpu = True
		self.start_maximized = True
		self.disable_infobars = True
		self.disable_extensions = True
		self.ignore_certificate_errors = True
		self.accept_untrusted_certs = True
		self.assume_untrusted_cert_issuer  = True
		self.platform = 0
		self.mobile_emulation = False

		self.disable_imges = False
		self.b_popup = False
		self.random_user_agent = True
		self.user_agent = ''
		self.proxy = ''

		self.log_level_conf = False
		self.browser_log = False
		self.performance_log = False
		self.driver_log = False
		self.log_level = '--verbose' #open browser and driver log
		# self.server_log = False
		self.test_case_name = 'defaults'
		self.test_class_name = 'log'

	def assrt_page(self):
		assert self.title in self.driver.title
	
	def _open(self, url, page_title):
		try:
			self.driver.get(url)
		except Exception as e:
			raise e
		# assert self.assrt_page(page_title), u"cannot open: %s"%url

	def init_base_infos(self, url, title=''):
		self.url = url
		
		self.title = title
		self.get_netloc()

	def parse_url(self, url=''):
		url = url or self.url
		from urllib.parse import urlparse
		return urlparse(url)

	def get_netloc(self, url=''):
		result = self.parse_url(url)

		self.host =  result.netloc
		return self.host
	
	def open(self, url='', title=''):
		url = url or self.url
		title = title or self.title
		
		return self._open(url, title)

	def init_class_name(self,class_name):
		self.test_class_name = class_name
		
	def init_case_name(self, case_name):
		self.test_case_name = case_name
		

	def init_driver(self, log_name, log_config_file):
	# def init_driver(self, log_name):

		self.set_log_save_fname(log_name)
		self.driver = webdriver.Chrome(
			self.chrome_driver, 
			chrome_options=self.chrome_options, 
			desired_capabilities=self.capabilities,
			service_args=[self.log_level, self.log_path]
		)
		self.get_log_conf(log_config_file)
		self.set_log()
		if self.headless and self.headless_max:
			self.set_headless_maximized()
		
	def set_driver_path(self):
		self.chrome_driver, self.platform = denv.set_driver_path()
		os.environ["webdriver.chrome.driver"] = self.chrome_driver

	def set_window_size(self, width, height):
		self.driver.set_window_size(width, height)

	def set_headless_maximized(self):
		self.set_window_size(1920, 1080)


	def set_chrome_options(self):
		if self.headless:
			self.chrome_options.add_argument("--headless") 
		
		if self.no_sandbox:
			self.chrome_options.add_argument('--no-sandbox') # Bypass OS security model
		if self.disable_gpu and (self.platform == 0):
			self.chrome_options.add_argument('--disable-gpu')  # applicable to windows os only
		if self.start_maximized and not self.headless:
			self.chrome_options.add_argument('--start-maximized')
		if self.disable_infobars:
			self.chrome_options.add_argument('--disable-infobars')
		if self.disable_extensions:
			self.chrome_options.add_argument("--disable-extensions")

		if self.accept_untrusted_certs:
			self.chrome_options.accept_untrusted_certs = True
		if self.assume_untrusted_cert_issuer:
			self.chrome_options.assume_untrusted_cert_issuer = True
		if self.mobile_emulation:
			self.enable_mobile_emulation()

		if self.disable_imges:
			self.disable_img()

		if self.b_popup:
			self.disble_popup()
		if self.random_user_agent:
			self.add_user_agent()
		if self.proxy:
			self.add_proxy(self.proxy)

	def disable_img(self):

		prefs = {"profile.managed_default_content_settings.images": 2}
		self.add_experimental_option("prefs", prefs)

	def disble_popup(self):
		self.chrome_options.add_argument('--disable-popup-blocking')
		
		# prefs = {"profile.default_content_settings.popups": 2}
		# self.add_experimental_option("prefs", prefs)

	def add_experimental_option(self, option, value):

		self.chrome_options.add_experimental_option(option, value) 

	def enable_mobile_emulation(self):
		
		DEVICE = {
			'width': 375,
			'height': 812
		}

		mobile_emulation = {
			# "deviceName": "iPhone X"
			"deviceMetrics": { 
				"width": DEVICE['width'], 
				"height": DEVICE['height'], 
				"pixelRatio": 3.0
			},
			"userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" 
		}
		self.add_experimental_option('mobileEmulation', mobile_emulation)


	def set_options(self, option):
		'''
		https://cs.chromium.org/search/?q=no-sandbox&type=cs
		http://www.assertselenium.com/java/list-of-chrome-driver-command-line-arguments/
		'''
		self.chrome_options.add_argument(option)

	def add_user_agent(self, user_agent_str=None):
		user_agent_str = user_agent_str or self.user_agent
		self.chrome_options.add_argument('--user-agent={}'.format(user_agent_str))

	def set_proxy(self, proxy):
		self.proxy = proxy

	def add_proxy(self, proxy):

		self.chrome_options.add_argument('--proxy-server={}'.format(proxy))

	def set_browser_log_level(self, level):
		'''
		@param:
			https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities#loggingpreferences-json-object
			level: "OFF", "SEVERE", "WARNING", "INFO", "CONFIG", "FINE", "FINER", "FINEST", "ALL".
		'''
		self.capabilities['loggingPrefs']['browser'] = level

	def set_driver_log_level(self, level):
		'''
		@param:
			level: "OFF", "SEVERE", "WARNING", "INFO", "CONFIG", "FINE", "FINER", "FINEST", "ALL".
		@notice:
			get js error form driver log ('INFO')
		'''
		self.capabilities['loggingPrefs']['driver'] = level 

	def set_performance_log_level(self, level):
		'''
		@param:
			level: "OFF", "SEVERE", "WARNING", "INFO", "CONFIG", "FINE", "FINER", "FINEST", "ALL".
		'''
		self.capabilities['loggingPrefs']['performance'] = level

	def set_server_log_level(self, level):
		'''
		@param:
			level: "OFF", "SEVERE", "WARNING", "INFO", "CONFIG", "FINE", "FINER", "FINEST", "ALL".
		'''
		self.capabilities['loggingPrefs']['server'] = level

	def set_base_log_level(self, level):
		'''
		@param:
			level: "OFF", "SEVERE", "WARNING", "INFO", "CONFIG", "FINE", "FINER", "FINEST", "ALL".
		'''
		self.log_level = '--log-level=' + level

	def disable_log(self):
		self.log_level = '--silent'

	def set_log_save_fname(self, log_name):
		'''
		@param:
			--log-path    write server log to file
			--log-level   set log level: ALL, DEBUG, INFO, WARNING, SEVERE, OFF
			--verbose     equivalent to --log-level=ALL
			--silent      log nothing (equivalent to --log-level=OFF)
		'''
		nowTime = time.strftime("%Y%m%d.%H.%M.%S")
		_log_path = os.path.join("..", "log", self.test_class_name, "%s_%s.log" % (log_name, nowTime))
		# print(_log_path)
		fhd.mkdir_if_not_existed(_log_path)
		self.log_path = '--log-path=' + _log_path
		self.log_level = '--verbose'
		# self.log_level = '--silent'
		# self.log_level = '--log-level=INFO'


	def set_log(self):
		if self.log_level_conf :
			self.set_base_log_level(self.log_level_conf)
		if self.browser_log :
			self.set_browser_log_level(self.browser_log)
		if self.performance_log :
			self.set_performance_log_level(self.performance_log)
		if self.driver_log :
			self.set_driver_log_level(self.driver_log)
			
		# if self.server_log :
		# 	self.set_server_log_level(self.server_log)

	def get_log_conf(self, log_config_file):
		from utils.read_confs import ReadConf
		
		config_parser = ReadConf(log_config_file)

		self.log_level_conf = config_parser.get_log_by_key('log_level')

		self.browser_log = config_parser.get_log_by_key('browser')
		self.performance_log = config_parser.get_log_by_key('performance')
		self.driver_log = config_parser.get_log_by_key('driver')
		# self.server_log = config_parser.get_log_by_key('server')

	def set_network_conditions(self, is_offline, 
								latency=170, 
								download_throughput=0, 
								upload_throughput=0,
								throughput=900 * 1024):
		'''
		Sets Chrome network emulation settings.
		@param:
			is_offline - set offline 
			latency    - additional latency (ms)
			download_throughput - maximal throughput
			upload_throughput   - maximal throughput
			throughput - set download and upload both
		'''
		if download_throughput and upload_throughput:

			self.driver.set_network_conditions(
				offline=is_offline,
				latency=latency,   
				download_throughput=download_throughput,  
				upload_throughput=upload_throughput   
			)

		else:
			self.driver.set_network_conditions(
				offline=is_offline,
				latency=latency,   
				throughput=throughput   
			)
		