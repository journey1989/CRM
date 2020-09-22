from common.my_request import *
from common.tool import *
import unittest


class Crm_RenewalAmount(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/classTeacher/panel/renewalAmount'

    def test_renewalamount(self):
        '''班主任面板：本月续费金额'''
        headers = {'Authorization': self.token}
        res = Myrequest.get(self.url, header=headers)

    def tearDown(self):
        pass


if __name__ == '__main__':
    c = Crm_RenewalAmount()
    c.test_renewalamount()
