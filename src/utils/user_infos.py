
class Users(object):
	"""docstring for Users"""
	def __init__(self, file_path):
		self.file = file_path
		import configparser
		self.config_obj = configparser.SafeConfigParser()
		

	def get_value_by_key(self, option, section='default'):
		import codecs
		with codecs.open(self.file, 'r', encoding='utf-8') as f:
			self.config_obj.readfp(f)

			try:
				section = section.lower()
				option = option.lower()
				value = self.config_obj.get(section, option)
				if not value:
					raise Exception("please check conf/login.conf.key: %s value: %s" %(option, value))
				return value
			except Exception as e:
				raise e


