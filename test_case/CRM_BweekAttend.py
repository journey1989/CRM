from common.my_request import *
from common.tool import *
import unittest


class Crm_WeekAttend(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/classTeacher/panel/weekAttend'

    def test_weekattend(self):
        '''班主任面板：本周上课学员'''
        headers = {'Authorization': self.token}
        res = Myrequest.get(self.url, header=headers)

    def tearDown(self):
        pass


if __name__ == '__main__':
    c = Crm_WeekAttend()
    c.test_weekattend()
