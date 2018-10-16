import os
import sys
BASEDIR = os.path.dirname(os.getcwd())
sys.path.append(BASEDIR)

from page.locate_elements import LocateElements

class AssertAttrs(LocateElements):
	

	def save_png(self, file_name=''):
		from PIL import Image
		from utils import file_handle as fhd
		import io
		verbose = 1
		# from here http://stackoverflow.com/questions/1145850/how-to-get-height-of-entire-document-with-javascript
		js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'
		scrollheight = self.driver.execute_script(js)
		if verbose > 0: 
			print (scrollheight)

		slices = []
		offset = 0
		while offset < scrollheight:
			if verbose > 0: 
				print ("offset: ", offset)

			self.driver.execute_script("window.scrollTo(0, %s);" % offset)
			img = Image.open(io.BytesIO(self.driver.get_screenshot_as_png()))
			offset += img.size[1]
			slices.append(img)

			if verbose > 0:
				self.driver.get_screenshot_as_file('%s/screen_%s.png' % ('/tmp', offset))
				print("scrollheight:", scrollheight)

		screenshot = Image.new('RGB', (slices[0].size[0], scrollheight))
		offset = 0
		for img in slices:
			screenshot.paste(img, (0, offset))
			# offset += img.size[1]
			img_height = img.size[1]
			offset += img_height

			bottom = scrollheight - offset
			if bottom <= img_height:
				offset += bottom - img_height
			print("add offet: ", offset, img.size[0], img.size[1])

		print(img.size)
		if not file_name:
			import time
			nowTime = time.strftime("%Y%m%d.%H.%M.%S")
			file_name = os.path.join(BASEDIR, 'screenshot', self.test_class_name, self.test_case_name, 'others-{}.png'.format(nowTime))

		fhd.mkdir_if_not_existed(file_name)

		screenshot.save(file_name)
	
	def assertEqual(self, expected_attr, real_attr, msg=''):
		if not msg:
			msg = " Expected attribute: {}, but got real attribute: {}".format(expected_attr, real_attr)
		try:
			assert expected_attr == real_attr, msg
		except Exception as e:
			self.save_png()
			self.check_browser_error_by_current_url()
			raise e

	def assertNotEqual(self, expected_attr, real_attr, msg=''):
		if not msg:
			msg = " Expected attribute: {} do compare equal to real attribute: {}".format(expected_attr, real_attr)
		try:
			assert expected_attr != real_attr, msg
		except Exception as e:
			self.save_png()
			self.check_browser_error_by_current_url()
			raise e

	def assertTrue(self, expected_attr, msg=''):
		if not msg:
			msg = " Expected attribute: True, but got real attribute: {}".format(expected_attr)
		try:
			assert expected_attr is True, msg
		except Exception as e:
			self.save_png()
			self.check_browser_error_by_current_url()
			raise e

	def assertFalse(self, expected_attr, msg=''):
		if not msg:
			msg = " Expected attribute: False, but got real attribute: {}".format(expected_attr)
		try:
			assert expected_attr is False, msg
		except Exception as e:
			self.save_png()
			self.check_browser_error_by_current_url()
			raise e

	def assertIs(self, expected_attr, real_attr, msg=''):
		if not msg:
			msg = " Expected attribute: {}, but real attribute: {}".format(expected_attr, real_attr)
		try:
			assert expected_attr is real_attr, msg 
		except Exception as e:
			self.save_png()
			self.check_browser_error_by_current_url()
			raise e

	def assertIsNot(self, expected_attr, real_attr, msg=''):
		if not msg:
			msg = " Expected attribute: {} as the same as real attribute: {}".format(expected_attr, real_attr)
		try:
			assert expected_attr is not real_attr, msg 
		except Exception as e:
			self.save_png()
			self.check_browser_error_by_current_url()
			raise e

	def assertIsNone(self, expected_attr, msg=''):
		if not msg:
			msg = " Expected attribute shoule be: None. But got real attribute: {}".format(expected_attr)
		try:
			assert expected_attr is None, msg
		except Exception as e:
			self.save_png()
			self.check_browser_error_by_current_url()
			raise e

	def assertIsNotNone(self, expected_attr, msg=''):
		if not msg:
			msg = " Expected attribute shoule be not: None. But got real attribute: {}".format(expected_attr)
		try:
			assert expected_attr is not None, msg
		except Exception as e:
			self.save_png()
			self.check_browser_error_by_current_url()
			raise e

	def assertIn(self, expected_attr, real_attr, msg=''):
		if not msg:
			msg = " Expected attribute: {} not in the real attribute: {}".format(expected_attr, real_attr)
		try:
			assert expected_attr in real_attr, msg 
		except Exception as e:
			self.save_png()
			self.check_browser_error_by_current_url()
			raise e

	def assertNotIn(self, expected_attr, real_attr, msg=''):
		if not msg:
			msg = " Expected attribute: {} in the real attribute: {}".format(expected_attr, real_attr)
		try:
			assert expected_attr not in real_attr, msg 
		except Exception as e:
			self.save_png()
			self.check_browser_error_by_current_url()
			raise e

	def assertInOrNotIn(self, expected_attr, real_attr, msg='', reverse=False):
		
		if not reverse:
			self.assertIn(expected_attr, real_attr, msg)
		else:
			self.assertNotIn(expected_attr, real_attr, msg)

	def assertEqOrNotEqual(self, expected_attr, real_attr, msg='', reverse=False):
		
		if not reverse:
			self.assertEqual(expected_attr, real_attr, msg)
		else:
			self.assertNotEqual(expected_attr, real_attr, msg)

	def assert_text_by_lower(self, expected_attr, element, msg=''):
		
		try:
			real_attr = element.text
			real_attr = real_attr.lower()
			if not msg:
				msg = " Expected attribute: {} in the real attribute: {}".format(expected_attr, real_attr)
			assert expected_attr in real_attr, msg 
		except Exception as e:
			self.save_png()
			self.check_browser_error_by_current_url()
			raise e

	def assert_attr_in_or_not_by_attr_name(self, expected_attr, attr_name, element, msg='', reverse=False):
		real_attr = element.get_attribute(attr_name)
		if reverse:
			self.assertIn(expected_attr, real_attr, msg)
		else:
			self.assertNotIn(expected_attr, real_attr, msg)