


def mkdir_if_not_existed(file_name):
	import os
	path = os.path.dirname(file_name)
	if not os.path.exists(path):
		os.makedirs(path)

def pretty_write(py_obj, file_name):
	import os
	import json
	try:
		write_contents = json.dumps(py_obj, indent=4)
	except Exception as e:
		print(e)
		write_contents = py_obj
	mkdir_if_not_existed(file_name)
	import codecs
	
	
	with codecs.open(file_name,'w','utf-8') as fjson:
		fjson.write(write_contents)

def file_content_to_py_object(file_name):

	import codecs
	import json
	with codecs.open(file_name,'r','utf-8') as fjson:
		contents = fjson.read()
		try:
			return json.loads(contents)
		except Exception as e:
			raise e

def get_confs(file_name):
	import configparser
	import codecs
	 
	cp = configparser.SafeConfigParser()
	with codecs.open(file_name, 'r', encoding='utf-8') as f:
		cp.readfp(f)

		return cp
def empty_files_in_dir(path):
	if path == "." or path == '/' or path == '//':
		raise Exception("param error: %s" % path )
	import os
	import shutil
	# path = os.path.join('..','tmp')
	for root, dirs, files in os.walk(path):
		for f in files:
			os.unlink(os.path.join(root, f))
		for d in dirs:
			shutil.rmtree(os.path.join(root, d))




