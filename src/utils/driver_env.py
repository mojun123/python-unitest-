def get_platform():
	import sys
	platform = sys.platform 
	if 'win' in platform:
		return 0
	elif 'linux' in platform:
		return 1 

def set_driver_path():
	import os
	#todo 
	#param: path auto locate filename and join it in the path
	# set once
	cwd = os.getcwd()
	dir_name = os.path.dirname(cwd)
	platform = get_platform()
	# print(11111, platform)
	if 0 == platform:
		return os.path.join(dir_name,"lib","browser-driver","chrome", "chromedriver.exe"), platform
	elif 1 == platform:
		return os.path.join(dir_name,"lib","browser-driver","chrome", "chromedriver"), platform



