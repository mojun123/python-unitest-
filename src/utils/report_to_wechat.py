def get_param_from_cmd():
	import argparse
	parser = argparse.ArgumentParser(description='nighslee testcase params.',
	        epilog='Have a nice day!')
	parser.add_argument('-retry', '--retry', type=str, default='2', help='retry numbers if test failed')
	args = parser.parse_args()
	return args.retry

def run_suites(file_name, suits, retry_nums=2):
	# from src.libs.HTMLTestRunner import HTMLTestRunner
	
	from src.libs.retry_HTMLTestRunner import HTMLTestRunner
	import datetime
	import time
	import codecs
	import os
	from src.utils import file_handle as fhd
	todayDate = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
	fname = file_name + todayDate + ".html"
	result_file = os.path.join('..', 'result', fname)
	fhd.mkdir_if_not_existed(result_file)
	fp = codecs.open(result_file,"wb",'utf-8')
	total_retry = retry_nums or get_param_from_cmd()

	runner = HTMLTestRunner(
				stream=fp,
				title='oa main flow',
				# description='\
				# 	Included login -> \
				# 	add-sku-to-cart -> \
				# 	checkout -> \
				# 	order-confirm -> \
				# 	select-payment-method -> \
				# 	payment-page',
				description = "oa",
				retry_total_numbers=int(total_retry)
				)

	if not retry_nums:

			
		runner = HTMLTestRunner(
				stream=fp,
				title='oa main flow',
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



