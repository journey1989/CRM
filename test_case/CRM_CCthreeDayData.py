from common.tool import *
import unittest
from config.setting import *

class Crm_ThreeDayData(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/saleWordBoard/getThreeDayData'

    def test_ThreeDayData(self):
        '''cc面板：3天内待跟进'''
        headers = {
            'Authorization': self.token

        }

        res = Myrequest.get(self.url, header=headers)
        self.assertEqual(0, res.get('code'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    c = Crm_ThreeDayData()
    c.test_ThreeDayData()