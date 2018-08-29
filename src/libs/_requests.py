import requests

class RequestTemplete(object):
    def __init__(self):
        self.session = requests.session()
        self.url = 'https://judez.clatterans.com'
        self.headers = {}
        self.cookies = {}
        self.verify = False
        self.host = 'judez.clatterans.com'
        self.method = 'get'

    def set_url(self,dns,url):
        self.url = dns + "/" + url

    def _set_url(self, url):
        self.url = url


    def set_proxies(self,proxies):
        if not proxies:
            self.proxies = {
              'http' : 'socks5://192.168.10.20:1080',
              'https': 'socks5://192.168.10.20:1080'
            }
        else:
            self.proxies = proxies
    def set_proxies_disable(self, url_strval=None):
        url_strval = url_strval or self.host
        import os
        os.environ['NO_PROXY'] = url_strval

          
    def set_params(self,param):
        self.params = param

    def set_request_retry(self,url,count_number=3):
        request_retry = requests.adapters.HTTPAdapter(max_retries=count_number)
        self.session.mount(url,request_retry)

    def post(self):
        try:
            self.set_proxies_disable()
            # starttime = datetime.datetime.now()
            self.set_request_retry(self.url)
            response = self.session.post(self.url,data=self.params,
                headers=self.headers,cookies=self.cookies,verify=self.verify,timeout=30)
            # endtime = datetime.datetime.now()
            # responsetime = (endtime - starttime).microseconds   
        except TimeoutError:
             print(TimeoutError)
        return response

    def get(self):
        try:
            self.set_proxies_disable()
            # starttime = datetime.datetime.now()
            self.set_request_retry(self.url)
            # print("cookies:   ",self.cookies)
            response = self.session.get(url=self.url,params=self.params,\
                headers=self.headers,cookies=self.cookies,verify=self.verify,timeout=30)
            # endtime = datetime.datetime.now()
            # responsetime = (endtime - starttime).microseconds

        except TimeoutError:
             print(TimeoutError)
        return response

    def _req(self):
        # print("method",self.method)
        if 'get' == self.method:
            return self.get()
        elif 'post' == self.method:
            return self.post()


    