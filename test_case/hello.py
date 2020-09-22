import allure
from common.tool import testLogin
import unittest,warnings
from common.tool import Myrequest
import pytest, os
from config.setting import *
from ddt import *
@ddt
class TestLoing(unittest.TestCase):


        @file_data('D:\\autotest\\data\\testdata.yaml')
        def testLogin(self,data):

            url = 'self_api/auth/login'
            real_url = urljoin(TESTBASE_URL, url)
            headers = {
                'Content-Type': 'application/json; charset=UTF-8',
                'Origin': 'https://crm.putaoabc.com',
                'Referer': 'https://crm.putaoabc.com/login',
                'Accept': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
                'Cookie': 'uuid=D58656BD-8333-AC8A-7D54-BC5090F92D60'

            }
        #     data = {
        #     "email": "zhangjunfeng@putao-inc.com",
        #     "password": "123456"
        # }
            json_data = json.dumps(data)

            res = Myrequest.post(url=real_url,data=json_data, is_json=False, header=headers)

            token = res['data']['token']


            return token




if __name__ == '__main__':
    #login()
     testLogin()




