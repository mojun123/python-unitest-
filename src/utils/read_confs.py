
class ReadConf(object):
	"""docstring for Users"""
	def __init__(self, file_path):
		self.file = file_path
		import configparser
		self.config_obj = configparser.ConfigParser()
		

	def get_value_by_key(self, option, section='default'):
		import codecs
		# with codecs.open(self.file, 'r', encoding='utf-8') as f:
		self.config_obj.read(self.file)

		try:
			section = section.lower()
			option = option.lower()
			value = self.config_obj.get(section, option)
			if not value:
				raise Exception("please check conf/login.conf.key: %s value: %s" %(option, value))
			return value
		except Exception as e:
			raise e

	def get_log_by_key(self, option, section='default'):
		# import codecs
		# with codecs.open(self.file, 'r', encoding='utf-8') as f:
		# 	self.config_obj.readfp(f)

		self.config_obj.read(self.file)
		try:
			section = section.lower()
			option = option.lower()
		
			value = self.config_obj.get(section, option)
		
			return value
		except Exception as e:
			return None



