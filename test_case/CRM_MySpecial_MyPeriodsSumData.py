from common.my_request import *
from common.tool import *
import unittest
from urllib.parse import quote
from config.setting import *


class CRM_MyPeriodsMySpecial_MyPeriodsSumData(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/periodsWorkBoard/getMyPeriodsSumData'

    def test_MyPeriodsMySpecial_MyPeriodsSumData(self):
        '''我的营期-特训营：营期数据汇总'''
        periods = quote('全部')
        data = {
            'periods': periods,
            'type': BOARDTYPE2
        }
        headers = {
            'Authorization': self.token
        }
        res = Myrequest.get(self.url, data, headers)

    def tearDown(self):
        pass


if __name__ == '__main__':
    c = CRM_MyPeriodsMySpecial_MyPeriodsSumData()
    c.test_MyPeriodsMySpecial_MyPeriodsSumData()

