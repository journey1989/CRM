from common.tool import *
import unittest
from config.setting import *


class Crm_TodayTrialInfo(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/saleWordBoard/getTodayTrialInfo'

    def test_TodayTrialInfo(self):
        '''cc面板：今日预约行为'''
        headers = {
            'Authorization': self.token

        }

        res = Myrequest.get(self.url, header=headers)
        self.assertEqual(0, res.get('code'))

    def tearDown(self):
        pass


if __name__ == '__main__':
    c = Crm_TodayTrialInfo()
    c.test_TodayTrialInfo()