import  unittest
import  os
import time

from src.testcase.page_object import oa_login_in as lg


DASEDIR = os.path.dirname(os.getcwd())


class LoginTestsuits(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = "http://oatest.fandow.com/user/login.html"
        cls.login_page_obj = lg.Login()
        cls.login_page_obj.headless = False
        cls.login_page_obj.start_maximized = True
        cls.login_page_obj.set_chrome_options()
        proxy_json_file = os.path.join(DASEDIR,"conf","proxy.json")
        cls.login_page_obj.init_class_name(cls.__name__)

        log_conf = os.path.join(DASEDIR,'conf',"log.conf")
        cls.login_page_obj.init_driver('all_logs',log_conf)
        cls.start_time = time.time()

    def login_page(self,url = '',b_refersh = True):
        url = self.url or url
        title = "凡岛网络"
        if not b_refersh:
            self.test_case_name = self._testMethodName
            self.login_page_obj.init_case_name(self.test_case_name)
            self.login_page_obj.init_base_infos(url, title)
        self.login_page_obj.open(url)

    def test_login_in(self):
        self.login_page()
        username = self.login_page_obj.get_login_in_username()
        username.send_keys("fd-0001")
        password = self.login_page_obj.get_login_in_password()
        password.send_keys("123456")
        element = self.login_page_obj.get_login_in_click()
        element.click()
        expected_text = "http://oatest.fandow.com/index/index.html"
        atr_text = self.login_page_obj.driver.current_url
        self.login_page_obj.assertIn(expected_text,atr_text)

    @classmethod
    def tearDownClass(cls):
        run_time = time.time()-cls.start_time
        print("%s: %.3f" % (cls.__name__, run_time))
        cls.login_page_obj.driver.quit()

def main():
    from src.utils import case_suits
    test_suits = case_suits.CaseSuits()
    test_suits.add_login_suit("test_login_in")
    time.sleep(3)
    from src.utils import report_to_wechat as rtw
    file_name = "oa_login_result"
    retry_number = 0
    result = rtw.run_suites(file_name, test_suits.suits, retry_number)
    print(result)
    


  
if __name__ == "__main__":
    main()







