from common.tool import *
import unittest
from config.setting import *

class Crm_orderinfo(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/saleWordBoard/getOrdersInfo'

    def test_orderinfo(self):
        '''cc面板：本月成单总数'''
        data = {
            'boardType':BOARDTYPE4
        }

        headers = {
            'Authorization': self.token
        }

        res = Myrequest.get(self.url,data=data, header=headers)
        self.assertEqual(0, res.get('code'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    c = Crm_orderinfo()
    c.test_orderinfo()