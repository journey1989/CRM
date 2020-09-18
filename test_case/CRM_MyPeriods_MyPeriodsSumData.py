from common.my_request import *
from common.tool import *
import unittest
from urllib.parse import quote
from config.setting import *


class CRM_MyPeriods_MyPeriodsSumData(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/periodsWorkBoard/getMyPeriodsSumData'

    def test_MyPeriods_MyPeriodsSumData(self):
        '''我的营期-体验营：营期数据汇总'''
        periods = quote('全部')
        data = {
            'periods': periods,
            'type': BOARDTYPE1
        }
        headers = {
            'Authorization': self.token
        }
        res = Myrequest.get(self.url, data, headers)

    def tearDown(self):
        pass


if __name__ == '__main__':
    c = CRM_MyPeriods_MyPeriodsSumData()
    c.test_MyPeriods_MyPeriodsSumData()

