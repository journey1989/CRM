import unittest
from common.tool import *
from common.my_request import *
class Crm_PhonePlace(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/myUser/getPhonePlace'

    def test_phoneplace(self):
        '''我的全部用户：归属地查询'''
        hearders = {
            'Authorization': self.token
        }

        res = Myrequest.get(self.url, header=hearders)
        self.assertEqual(0, res.get('code'))
        print(res.get('data'))

    def tearDown(self):
        pass


if __name__ == '__main__':
    c = Crm_PhonePlace()
    c.test_phoneplace()