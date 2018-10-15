

import requests
from utils.file_handle import *
from utils.read_confs import ReadConf


def set_proxies_disable(url_strval="52.64.0.54"):

    import os
    os.environ['NO_PROXY'] = url_strval
data = None
url = "https://admin.bestsaveronline.com/admin.php"
host = "admin.bestsaveronline.com"
cookies_file = "../tmp/admin/cookie_files.log"
session = requests.Session()

ORDER_STATUS = {
	"1": "Cancelled",
	"2": "Pending",
	"3": "Processing",
	"4": "Sent",
	"5": "On Hold"
}

set_proxies_disable(host)

headers = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Connection":"keep-alive",
    # "Connection": "close",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    # "Cookie":"PHPSESSID=pt4qqiqvop1kbe2skj4mlhn7o2; uid=rBABTlrRr08ycCwpA5j+Ag==; __sharethis_cookie_test__=1; __unam=4401563-162c314d49d-51aba8a2-12; CS_FPC=CSCaJa4KwO5cGLBQicd3SIUPPizg2tqtPc0; _uetsid=_uetad4fa78b",
    "Host":host,
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}


def login(file):

	
	user_obj = ReadConf(file)
	email = user_obj.get_value_by_key('email', 'backend')
	pwd = user_obj.get_value_by_key('pwd', 'backend')
	
	method = "post"

	params = {
		'fLogin': email,
		'fPassword': pwd
	}
	import json
	# params = json.dumps(params)
	try:
		response = session.post(url,data=params,
			headers=headers,verify=False,timeout=30)

		return response

	except TimeoutError:
		 print(TimeoutError)
	
def order_details(order_id):
	
	url = "https://admin.bestsaveronline.com/admin.php?dpt=custord&sub=new_orders&od=1&orderID=" + order_id + "&urlToReturn=L2N1c3RvcmQvbmlnaHNsZWVfb3JkZXI/a2V5d29yZFR5cGU9b3JkZXJJRCZ2YXJzPTM1NTM2MiZpdGVtS2V5d29yZFR5cGU9dHJhY2tpbmdOdW1iZXImcz1TaG93"
	method = "get"

	try:
		response = session.get(url,verify=False,timeout=30)
		contents = response.text
		print(url)
		if response.status_code == 200 and ("young_yang@limei-trading.com" in contents) and (order_id in contents):
			print(order_id, response.status_code)
			return url , order_id
		# return response

	except TimeoutError:
		 print(TimeoutError)




def modify_order_status(url, order_id, status=1):

	
	method = "post"
	params = {
		"current_if_notify": "1",
		# "billing_name": "dgdsg ",
		# "billing_address": "dg dgdg ",
		# "billing_zip": "50157",
		# "billing_city": "dgd",
		# "billing_state": "LA",
		"orderid": order_id,
		# "shipping_type": "Shipping",
		# "shipping_firstname": "young yang",
		# "shipping_phone": "417-844-5279",
		# "shipping_address": "1 Main St",
		# "shipping_address1": "",
		# "shipping_zip": "98147",
		# "shipping_city": "NewYork",
		# "shipping_state": "DE",
		# "shipping_country": "United States",
		# "qua_54141_": "1",
		# "Price_54141": "$0.01",
		# "itemID[]": "54141",
		# "PID": "5",
		# "order_amount": "0.01",
		# "order_amount_": "0.01",
		# "total_b4_discount": "0.01",
		"status": status,
		"orders_detailed": "yes",
		"status_comment": "auto test",
		"add_comments": "Change order status",
		"flag": "1",
		"change_mode": "0",
		"item_number": "0"
	}
	import json
	# params = json.dumps(params)
	try:
		response = session.post(url,data=params,
			headers=headers,verify=False,timeout=30)

		return response

	except TimeoutError:
		 print(TimeoutError)


def cancle_order_by_id(orderid, file):
	login(file)

	# order_status = ORDER_STATUS['2']

	url, order_id = order_details(orderid)
	if url and order_id:
		modify_order_status(url, order_id)

if __name__ == '__main__':
	import os
	CURRENT_DIR = os.getcwd()
	BASE_DIR = os.path.dirname(CURRENT_DIR)
	file = os.path.join(BASE_DIR, 'conf', 'login.conf')
	order_list = ['355396', '355420', '355446']
	for item in order_list:
		cancle_order_by_id(item, file)










