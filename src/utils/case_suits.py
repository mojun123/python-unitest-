import unittest
class CaseSuits(object):
	"""docstring for Suits"""
	def __init__(self):
		self.suits = unittest.TestSuite()

	def addTest(self, case_obj, case_name):
		self.suits.addTest(case_obj(case_name))
		return self.suits

	def add_home_suit(self, case_name):
		from src.test_home import HomeTestSuits
		self.addTest(HomeTestSuits, case_name)

	def add_login_suit(self,case_name):
		from src.login_test import LoginTestsuits
		self.addTest(LoginTestsuits,case_name)


	# def add_login_suit(self, case_name):
	# 	from src.test_login import LoginTestSuits
	# 	self.addTest(LoginTestSuits, case_name)
	#
	# def add_mattress_suit(self, case_name):
	# 	from src.test_mattress import MattressTestSuits
	# 	self.addTest(MattressTestSuits, case_name)
	#
	# def add_checkout_suit(self, case_name):
	# 	from src.test_check_out import CheckOutTestSuits
	# 	self.addTest(CheckOutTestSuits, case_name)
	#
	# def add_payment_suit(self, case_name):
	# 	from src.test_select_payment import SelectPaymentTestSuits
	# 	self.addTest(SelectPaymentTestSuits, case_name)