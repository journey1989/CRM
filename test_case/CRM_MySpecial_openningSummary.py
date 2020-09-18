from common.my_request import *
from common.tool import *
import unittest
from urllib.parse import quote
from config.setting import *


class CRM_MyPeriodsMySpecial_openningSummary(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/periodsWorkBoard/special/openningSummary'

    def test_MyPeriodsMySpecial_openningSummary(self):
        '''我的营期-特训营：开营中'''
        term = quote('全部')
        data = {
            'term': term,
            'experienceLevel': 'null'
        }
        headers = {
            'Authorization': self.token
        }
        res = Myrequest.get(self.url, data, headers)

    def tearDown(self):
        pass


if __name__ == '__main__':
    c = CRM_MyPeriodsMySpecial_openningSummary()
    c.test_MyPeriodsMySpecial_openningSummary()

