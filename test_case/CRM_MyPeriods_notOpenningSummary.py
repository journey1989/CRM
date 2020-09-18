from common.my_request import *
from common.tool import *
import unittest
from urllib.parse import quote
from config.setting import *

class CRM_MyPeriods_notOpenningSummary(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/periodsWorkBoard/experience/notOpenningSummary'


    def test_MyPeriods_notOpenningSummary(self):
        '''我的营期-体验营：未开营'''
        term = quote('全部')
        data = {
            'term': term,
            'experienceLevel':'null'
        }
        headers = {
            'Authorization': self.token
        }
        res = Myrequest.get(self.url, data, headers)


    def tearDown(self):
        pass


if __name__ == '__main__':
    c = CRM_MyPeriods_notOpenningSummary()
    c.test_MyPeriods_notOpenningSummary()