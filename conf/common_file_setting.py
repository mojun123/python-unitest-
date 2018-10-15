import os
G_COOKIE_FILE = {
	'login': os.path.join('..', 'tmp', 'cookies', 'login_cookies.log'),
	'mattress': os.path.join('..', 'tmp', 'cookies', 'mattress_cookies.log'),
	'checkout': os.path.join('..', 'tmp', 'cookies', 'checkout_cookies.log'),
}

INFOS_FILE = {
	'product_infos': os.path.join('..', 'tmp', 'product_infos', 'infos.py'),
	'selected_product_size': os.path.join('..', 'tmp', 'product_infos', 'seleted_product.log'),
	'url_after_checkout': os.path.join('..', 'tmp', 'product_infos', 'url_after_checkout.log'),

}