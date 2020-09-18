from common.tool import testLogin
import unittest,json
from common.tool import Myrequest
from config.setting import *
class Crm_TmkQuotaStatisticsData(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/tmkWordBoard/getTmkQuotaStatisticsData'

    def test_TmkQuotaStatisticsData(self):
        '''TMK面板：指标统计'''

        headers = {'Authorization': self.token}
        data = {
            'type': 0
        }
        res = Myrequest.get(self.url, data, headers )
        self.assertEqual(0, res.get('code'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    c = Crm_TmkQuotaStatisticsData()
    c.test_TmkQuotaStatisticsData()