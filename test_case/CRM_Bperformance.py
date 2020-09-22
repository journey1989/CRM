from common.my_request import *
from common.tool import *
import unittest


class Crm_Performance(unittest.TestCase):

    def setUp(self):
        self.token = testLogin()
        self.url = 'https://ctest.putaoabc.net.cn/self_api/classTeacher/panel/performance'

    def test_performance(self):
        '''班主任面板：本月业绩'''
        headers = {'Authorization': self.token}
        res = Myrequest.get(self.url, header=headers)

    def tearDown(self):
        pass


if __name__ == '__main__':
    c = Crm_Performance()
    c.test_performance()
