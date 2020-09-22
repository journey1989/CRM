from common.my_request import *
from common.tool import *
import unittest


class Crm_MonthNoAttend(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/classTeacher/panel/monthNoAttend'

    def test_monthnoattend(self):
        '''班主任面板：本月未上课学员'''
        headers = {'Authorization': self.token}
        res = Myrequest.get(self.url, header=headers)

    def tearDown(self):
        pass


if __name__ == '__main__':
    c = Crm_MonthNoAttend
    c.test_monthnoattend()
