def deduplicate_list(l_data):
	if not isinstance(l_data, list):
		raise Exception("param is not list")

	if not l_data:
		print("[Warning]param is null")
		return l_data

	new_l_data = list(set(l_data))
	new_l_data.sort(key = l_data.index)

	return new_l_data

def add_cookie_and_refresh(cookie_file, page_obj):

	page_obj.delete_all_cookies()
	page_obj.load_cookie_from_file(cookie_file)
	page_obj.refresh()

def importModule(module_path, variable_name, module_name=''):
	import os
	#fname = "F:\\qa\\testing_coding\\userInfo\\userInfo.csv"
	if not module_name:
		filepath, filename =os.path.split(module_path)
		module_name, _ = os.path.splitext(filename)
		print(module_name, filepath)
		import sys
		sys.path.append(filepath)
	else:
		sys.path.append(module_path)

	#动态加载模块
	#class_name = "TestSample"  #类名
	# module_name = fname	   #模块名（文件名）
	#method_name = "testAdd"  #方法名  
	# variable_name = fname
	if module_name in sys.modules:
		del sys.modules[module_name]

	import importlib  
	module = importlib.import_module(module_name)
	variable_data = getattr(module,variable_name)
	return variable_data

def get_login_infos(base_dir):
	import os
	file = os.path.join(base_dir, 'conf', 'login.conf')
	from utils.read_confs import ReadConf
	config_parser = ReadConf(file)

	email = config_parser.get_value_by_key('email')
	pwd = config_parser.get_value_by_key('pwd')
	return email, pwd

def random_proxy_from_file( proxy_json_file):
	from proxy.requestsproxy import RandomProxy

	_obj = RandomProxy(proxy_json_file)
	_default_proxy = 'socks5://192.168.10.20:1081'
	request_proxy = {
		'https': _default_proxy
	}

	proxys = _obj.check_proxy(request_proxy)
	if not proxys:
		proxys = _obj.random_proxy()
		return _obj.get_proxy_str_from_dict(proxys)
	else:
		return _default_proxy

