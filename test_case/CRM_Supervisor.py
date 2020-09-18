from common.tool import *
from common.my_request import *
import unittest


class Crm_Supervisor(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/client/supervisor'

    def test_Supervisor(self):
        '''我的全部用户：新建客户：负责人列表'''
        hearders = {
            'Authorization': self.token
        }

        res = Myrequest.get(self.url, header=hearders)
        self.assertEqual(0, res.get('code'))
        print(res.get('data'))

    def tearDown(self):
        pass


if __name__ == '__main__':
    c = Crm_Supervisor()
    c.test_Supervisor()

