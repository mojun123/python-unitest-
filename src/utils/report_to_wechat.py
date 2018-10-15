def get_param_from_cmd():
	import argparse
	parser = argparse.ArgumentParser(description='nighslee testcase params.',
	        epilog='Have a nice day!')
	parser.add_argument('-retry', '--retry', type=str, default='2', help='retry numbers if test failed')
	args = parser.parse_args()
	return args.retry

def run_suites(file_name, suits, retry_nums=2):
	# from libs.HTMLTestRunner import HTMLTestRunner
	
	from libs.retry_HTMLTestRunner import HTMLTestRunner
	import datetime
	import time
	import codecs
	import os
	from utils import file_handle as fhd
   
	todayDate = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
	fname = file_name + todayDate + ".html"
	result_file = os.path.join('..', 'result', fname)
	fhd.mkdir_if_not_existed(result_file)
	fp = codecs.open(result_file,"wb",'utf-8')
	total_retry = retry_nums or get_param_from_cmd()

	runner = HTMLTestRunner(
				stream=fp,
				title='clatterans shopping main flow',
				description='\
					Included login -> \
					add-sku-to-cart -> \
					checkout -> \
					order-confirm -> \
					select-payment-method -> \
					payment-page',
				retry_total_numbers=int(total_retry)
				)

	if not retry_nums :

			
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

		
		

	
	print("start : %s" % time.ctime())
	run_result=runner.run(suits)
	fp.close()
	print("End : %s" % time.ctime())
	return run_result



def report(result):
	import os
	import sys
	BASEDIR = os.path.dirname(os.getcwd())
	sys.path.append(BASEDIR)
	from libs._requests import RequestTemplete
	from utils import commons as chd

	_req = RequestTemplete()
	url = 'https://oa.jiebeili.cn/websiteSystemNotify'
	_req._set_url(url)
	if result.failure_count or result.error_count:
		count = str(result.success_count + result.failure_count + result.error_count)
		success = str(result.success_count)
		fail = str(result.failure_count)
		error = str(result.error_count)
		failures = chd.deduplicate_list(result.failures)
		errors = chd.deduplicate_list(result.errors)
		contents = "Have some failures: \n{}\nHave some errors: \n{}\n".format(failures, errors)
		# import json
		# contents = json.dumps(contents, indent=4)
		number = 2048
		len_content = len(contents)

		total = int(len_content/number)
		if total<1:
			total = 1
		else: 
			total += 1
		for count in range(0, total):
		
			end = count * number + number
			data = contents[count * number: end]

			params = {
				'rev': 'youngy',
				'title': "total: %s, pass: %s, fail: %s, error: %s" % (count, success, fail, error),
				'content': "{}".format(data)

			}
			_req.set_params(params)
			_req.method = "post"
			_req._req()