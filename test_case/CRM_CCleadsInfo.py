from common.tool import *
import unittest
from config.setting import *

class Crm_LeadsInfo(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/saleWordBoard/getLeadsInfo'

    def test_LeadsInfo(self):
        '''cc面板：今日分配leads'''
        headers = {
            'Authorization': self.token

        }

        res = Myrequest.get(self.url, header=headers)
        self.assertEqual(0, res.get('code'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    c = Crm_LeadsInfo()
    c.test_LeadsInfo()