from common.tool import *
from common.my_request import *
import unittest

class Crm_SelectInfo(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/myUser/mySelectInfo'

    def test_selectinfo(self):
        '''我的全部用户：筛选条件'''
        hearders = {
            'Authorization': self.token
        }

        res = Myrequest.get(self.url, header=hearders)
        self.assertEqual(0, res.get('code'))
        print(res.get('data'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    c = Crm_SelectInfo()
    c.test_selectinfo()
