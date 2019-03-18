from src.page.chrome_driver import ChromeDriver as cdriver

class Login(cdriver):
    def __init__(self, driver=''):
        super(Login, self).__init__()
        if driver:
            self.driver = driver

    def get_login_in_username(self):
        e_id = "username"
        return self.find_element_by_id(e_id)

    def get_login_in_password(self):
        e_id = "password"
        return self.find_element_by_id(e_id)

    def get_login_in_click(self):
        e_id = "login-action"
        return self.find_element_by_id(e_id)



